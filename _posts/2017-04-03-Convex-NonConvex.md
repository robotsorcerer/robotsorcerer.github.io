---
layout: post
date: 2017-04-05 11:15:00
title: "<center>Backpropagation and convex programming</center>"
excerpt: "<center>A contraint-based approach to solving the backpropagation optimization problem in nonlinear model reference adaptive systems.</center>"
permalink: Adaptive-Control-Notes
comments: true
mathjax: true
---

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
  TeX: { equationNumbers: { autoNumber: "AMS" } }
});
</script>

<!--Mathjax Parser -->
<script type="text/javascript" async
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-MML-AM_CHTML">
</script>

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
  tex2jax: {inlineMath: [['$','$'], ['\\(','\\)']]}
});
</script>

### [Table of Contents](#table-of-contents):
   
  - [Introduction](#introduction)
  - [Problem formulation: Solving the standard-form QP in a Backprop setting](#problem-formulation)  
  - [Slack Variables](#slack-variables)
  - [Initialization](#initialization)  


<a name='introduction'></a>
## Introduction

The backpropagation algorithm is very useful for general optimization tasks. Particularly, in deep learning applications, great progress has been made due to the effectiveness of the backprop algorithm. Whereas in traditional control applications, we typically use feedback regulation to stabilize the states of the system, in model reference adaptive control systems, we typically want to specify an index of performance to determine the "goodness" of our adaptation. An auxiliary dynamic system called the __reference model__ is used in generating this index of performance (IP). The reference model specifies in terms of the input and states of the model a given index of performance. A comparison check is used to determine appropriate  control laws  by comparing the given IP and measured IP based on the outputs of the adjustable system to that of the reference model system. 

Note that the comparator block in an MRAS system does use the difference from the comparator block to either modify the parameters of the adjustable system or to generate auxiliary input signals which modify the difference between the two IP's expressed as a functional of the difference between the IPs of the reference model and the adjustable system.

## Nonlinear (Multivariable) Model Reference Adaptive Systems

With nonlinear (possibly multivariable systems), it is typical to approximate the unknown function \\(f(.)\\) with a function approximator such as simple neural networks. To date, the state-of-the-art method in optimizingh the weights of a neural networkis the [backpropagation algorithm](https://mattmazur.com/2015/03/17/a-step-by-step-backpropagation-example/).  But the optimizationin classical backprop is unrolled end-to-end so that the complexity of the network increases supposingthat we want to add as <i>argmin layer</i>. When we want the backpropagation algorithm to generate control laws that fit into our actuator constraints such as model predictive control schemes allow, we cannot easily fit a convex optimization layer into the backprop algorithm using classical gradient descent. 

> "When we want the backpropagation algorithm to generate control laws that fit into our actuator constraints such as model predictive control schemes allow, we cannot easily fit a convex optimization layer into the backprop algorithm using classical gradient descent."

This is because in the backpropagation algorithm, the explicit Jacobians of the gradients of the system's energy function with respect to system parameters is not exactly formulated. But in control applications, we would want to define a quadratic programming layer as the last layer of our neural network optimization algorithm so that effective control laws that exactly fit into actuator saturation limits are generated. Doing this requires a bit of tweaking of the backprop algorithm on our part. 

<a name="problem-formulation"></a>
### Problem formulation: Solving the standard-form QP in a Backprop setting

We define the standard QP canonical form problem with inequality contraints thus:

\begin{align}
\text{minimize} \quad  \frac{1}{2}x^TQx + q^Tx \\
\text{ subject to }  	\quad G x \le h
\label{eq:orig}
\end{align}

where \\(Q\\) is a symmetric, positive definite matrix \\(\in \mathbb{R}^n, q \in \mathbb{R}^n, G \in \mathbb{R}^{p \times n}, \text{ and } h \in \mathbb{R}^p \\).

Suppose we have our convex quadratic optimization problem in canonical form, we can use primal-dual interior point methods (PDIPM) to find an optimal solution to such a problem (PDIPMs are the state-of-the-art in solving such problems currently, for example, see [Boyd and Mattingley](https://stanford.edu/~boyd/papers/pdf/code_gen_impl.pdf)). Primal-dual methods with Mehrota predictor-corrector are effective and consistent for reliably solving QP embedded optimization problems within 5-25iterations, without warm-start.

<a name="slack-variables"></a>
### Introduce Slack Variables
Given \eqref{eq:orig}, we can introduce slack variables, \\(s \in \mathbb{R}^p\\) like so,

$$
\text{minimize}  \quad \frac{1}{2}x^TQx + q^Tx \\
\text{ subject to }  \quad G x + s =  h, \qquad s \ge 0,
\label{eq:orig1}
$$

where \\(x \in \mathbb{R}^n, s \in \mathbb{R}^p\\). Let a dual cvariable \\(z \in \mathbb{R}^p \\) be associated with the inequality constraint, then we can define the KKT conditiopns for \eqref{eq:orig1} as 

$$
Gx + s = h, \quad s \ge 0 \\
z \ge 0 \\
Qx + q + G^T = 0 \\ \\
z_i s_i = 0, i = 1, \ldots, p.
$$

<a name="initialization"></a>
### Initialization

For the primal and dual problems:

$$
 \text{minimize} \quad \frac{1}{2}x^T Q  x + p^T x + (\frac{1}{2}\|s\|^2_2) \\
 \text{ subject to } \quad Gx + s = h \\
 \text{with \\(x\\) and \\(s\\) as variables to be optimized and} \\
  \text{maximize} \quad -\frac{1}{2}w^T Q  w - h^T z + (\frac{1}{2}\|z\|^2_2) \\
 \text{ subject to } \quad Qw + G^T z +  q = 0 \\
 \text{ with variables w and z to be optimized},
$$
	
when the primal and dual starting points \\(\hat{x}, \hat{s}, \hat{y}, \hat{z} \\) are not given, they can be initiated as proposed by Vanderberghe in [cvxopt](http://www.seas.ucla.edu/~vandenbe/publications/coneprog.pdf) namely, by solving the set of linear equations

$$
\begin{bmatrix}
G & 0 & -I  \\
A & 0 & 0 \\
Q & A^T & G^T
\end{bmatrix}

\begin{bmatrix}
z \\
y \\
x \\
\end{bmatrix}
=
\begin{bmatrix}
h \\
p \\
-q \\
\end{bmatrix}
$$

and assume that \\(\hat{x} = x,\hat{y} = y\\). 
