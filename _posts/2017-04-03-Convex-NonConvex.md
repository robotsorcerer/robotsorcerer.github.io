---
layout: post
date: 2017-04-05 11:15:00
title: "<center>Backpropagation and convex programming</center>"
excerpt: "<center>A contraint-based approach to solving the backpropagation optimization problem in nonlinear model reference adaptive systems.</center>"
permalink: QP-Layer-MRAS
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
  - [Nonlinear (Multivariable) Model Reference Adaptive Systems](#nonlinear)
  - [Problem formulation: Solving the standard-form QP in a Backprop setting](#problem-formulation)  
  - [Slack Variables](#slack-variables)
  - [Initialization](#initialization)  


<a name='introduction'></a>
## Introduction

The backpropagation algorithm is very useful for general optimization tasks. Particularly, in deep learning applications, great progress has been made due to the effectiveness of the backprop algorithm. Whereas in traditional control applications, we typically use feedback regulation to stabilize the states of the system, in model reference adaptive control systems, we typically want to specify an index of performance to determine the "goodness" of our adaptation. An auxiliary dynamic system called the __reference model__ is used in generating this index of performance (IP). The reference model specifies in terms of the input and states of the model a given index of performance. A comparison check is used to determine appropriate  control laws  by comparing the given IP and measured IP based on the outputs of the adjustable system to that of the reference model system. 

Note that the comparator block in an MRAS system does use the difference from the comparator block to either modify the parameters of the adjustable system or to generate auxiliary input signals which modify the difference between the two IP's expressed as a functional of the difference between the IPs of the reference model and the adjustable system.

<a name="nonlinear"></a>
## Nonlinear (Multivariable) Model Reference Adaptive Systems

With nonlinear (possibly multivariable systems), it is typical to approximate the unknown function \\(f(.)\\) with a function approximator such as simple neural networks. To date, the state-of-the-art used in optimizing the weights of a neural network is the [backpropagation algorithm](https://mattmazur.com/2015/03/17/a-step-by-step-backpropagation-example/).  But the optimization in classical backprop is unrolled end-to-end so that the complexity of the network increases supposing that we want to add an <i>argmin layer</i> before the final neural network layer that generates control laws. When we want the backpropagation algorithm to generate control laws that fit into our actuator constraints such as model predictive control schemes allow, we cannot easily fit a convex optimization layer into the backprop algorithm using classical gradient descent. 

> "When we want the backpropagation algorithm to generate control laws that fit into our actuator constraints such as model predictive control schemes allow, we cannot easily fit a convex optimization layer into the backprop algorithm using classical gradient descent."

This is because in the backpropagation algorithm, the explicit Jacobians of the gradients of the system's energy function with respect to system parameters is not exactly formulated (but rather are ordered derivatives which fluctuate about the global/local minimum when the weights of the network converge). To generate control laws such as torques to control a motor arm in a multi-dof robot-arm for example, we would want to define a quadratic programming layer as the last layer of our neural network optimization algorithm so that effective control laws that exactly fit into actuator saturation limits are generated. Doing this requires a bit of tweaking of the backprop algorithm on our part. 

<a name="problem-formulation"></a>
### Problem formulation: Solving the standard-form QP in a Backprop setting

When trying to construct a controller for a regulator, or MRAS system, we may imagine that the way to deribve the controller would be a search process for a control scheme that takes an arbitrary nonzero initial state to the zero state, hopefully as fast as possible. If the system is controllable, then we may require our controller taking the syste, from state \\(x(t\_0)\\) to the zero state at time \\(T\\). If \\(T\\) is closer to \\(t\_0\\), more control effort would be required to bear states to \\(t\_0\\) to ensure the states transfer. In most engineering systems, an upper bound is set on the magnitudes of the variables for pragmatic purposes. It therefore becomes impossible to take \\(T\\) to \\(0\\) without exceeding the control bounds. Unless we are ready to bear high gain terms in our controller parameters, the control is not feasible for finite T. So what to do? To meet the practical bounds manufacturers place on physical actuators, it suffices to manually formulate these bounds as constrainst into our control design objectives. An example of such measures is in the linear quadratic regulator problem e.g.

\begin{align}
\int_{t_0}^{T} u'(t)u(t)dt, or  \qquad \int_{t_0}^{T} [u'(t)u(t)]^{\frac{1}{2}} 
\end{align}
etc. 

Model predictive controllers have explicit ways of cformulating these constraints into the controller design as well. To the best of my knowledge, there are no rules for tuning the parameters of an MRAC system so that the control laws generated in our adjustment mechanism are scaled into the bounds of the underlying actuator. 

Because, we mostly deal with lower and upper bounds in such scenarios, the QP problem I formulate below are limited to inequality constraints only. For  equality constraints QP problems, I implore the reader to read [Mattingley and Boyd's formulation](https://stanford.edu/~boyd/papers/pdf/code_gen_impl.pdf), [Vanderberghe's CVX Optimization paper](http://www.seas.ucla.edu/~vandenbe/publications/coneprog.pdf), or  Brandon Amos' ICML submission available [here](https://arxiv.org/pdf/1703.00443.pdf).


We define the standard QP canonical form problem with inequality contraints thus:

\begin{align}
\text{minimize} \quad  \frac{1}{2}x^TQx + q^Tx 
\label{eq:orig}
\end{align}

subject to 	\\(\quad G x \le h\\)

where \\(Q \succeq \mathbb{S}^+_0 \\) i.e. it is a symmetric, positive semi-definite matrix \\(\in \mathbb{R}^n, q \in \mathbb{R}^n, G \in \mathbb{R}^{p \times n}, \text{ and } h \in \mathbb{R}^p \\).

Suppose we have our convex quadratic optimization problem in canonical form, we can use primal-dual interior point methods (PDIPM) to find an optimal solution to such a problem (PDIPMs are btw the state-of-the-art in solving such problems currently, see [Boyd and Mattingley](https://stanford.edu/~boyd/papers/pdf/code_gen_impl.pdf)). Primal-dual methods with Mehrota predictor-corrector are effective and consistent for reliably solving QP embedded optimization problems within 5-25iterations, without warm-start.

<a name="slack-variables"></a>
### Introducing Slack Variables
Given \eqref{eq:orig}, we can introduce slack variables, \\(s \in \mathbb{R}^p\\) like so,

\begin{align}
\text{minimize}  \quad \frac{1}{2}x^TQx + q^Tx 
\label{eq:orig1}
\end{align}


subject to \\( \quad G x + s =  h, \qquad s \ge 0\\),

where \\(x \in \mathbb{R}^n, s \in \mathbb{R}^p\\). Let a dual variable \\(z \in \mathbb{R}^p \\) be associated with the inequality constraint, then we can define the KKT conditiopns for \eqref{eq:orig1} as 

$$
Gx + s = h, \quad s \ge 0 \\
z \ge 0 \\
Qx + q + G^T = 0 \\ \\
z_i s_i = 0, i = 1, \ldots, p.
$$

More formally, if we write the Lagrangian of the system in \eqref{eq:orig} as 

\begin{align}
L(z, \lambda) = \frac{1}{2}x^TQx + q^Tx +\lambda^T(Gz -h)
\label{eq:Lagrangian}
\end{align}

then it follows that the KKT for [stationarity, primal feasibility and complementary slackness](https://www.cs.cmu.edu/~ggordon/10725-F12/slides/16-kkt.pdf) are thus defined


\begin{align}
Q x^* + q + G^T \lambda^* = 0 , 
\label{eq:KKTLagrangian}
\end{align}

\\(K (\lambda^*) (Gz* - h) = 0  \\)

where \\(K(\cdot) = \textbf{diag}(k) \\) i.e. it creates a matrix diagonal of the entries of the vector \\(k\\). Computing the time-derivative of \eqref{eq:KKTLagrangian}, we find that 

$$
dQ x^* + Q dx + dq + dG^T \lambda^* + G^T d\lambda = 0 \\
K(\lambda^*)\left(G x^* - h\right) = 0
$$

Vectorizing, we find that 

$$
\begin{bmatrix}
Q & G^T   \\
K(\lambda^*) G & K(dGx^* - h)  \\
\end{bmatrix}

\begin{bmatrix}
dx \\
d\lambda \\
\end{bmatrix}
=
\begin{bmatrix}
-dQ x^* - dq - dG^T \lambda^* \\
-K(\lambda^*) dG x^* + DK(\lambda^*) dh \\
\end{bmatrix}
$$

so that the Jacobians of the variables to be optimized can be formed (i.e. \\(x^*, \lambda^*\\)) with respect to the states of the system. Finidng \\(\dfrac{\partial J}{\partial h^*}\\), for example, would involve  passing \\(dh\\) as identity and setting other terms on the rhs to zero. After solving the equation, the desired Jacobian would be \\(dz\\). 


<a name="initialization"></a>
### Initialization

For the primal and dual problems:

$$
 \text{minimize} \quad \frac{1}{2}x^T Q  x + p^T x + (\frac{1}{2}\|s\|^2_2) \\
 \text{ subject to } \quad Gx + s = h \\
$$

 with \\(x\\) and \\(s\\) as variables to be optimized and

$$
  \text{maximize} \quad -\frac{1}{2}w^T Q  w - h^T z + (\frac{1}{2}\|z\|^2_2) \\
 \text{ subject to } \quad Qw + G^T z +  q = 0 \\
$$

 with variables \\(w\\) and \\(z\\) to be optimized,
	
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

The initial value of \\(\hat{s}\\) is computed from the residual \\(h - Gx = -z\\), as 

$$
\hat{s} = \begin{cases}
	-z \qquad  \text{ if } \alpha_p < 0  \qquad else \\
	-z + (1+\alpha_p)\textbf{e} 
\end{cases}
$$

for \\(\alpha\_p = inf \{\alpha | -z + \alpha \textbf{e} \succeq 0\} \\).

Similarly, \\(z\\) at the first iteration is computed as follows

$$
\hat{z} = \begin{cases}
	z \qquad  \text{ if } \alpha_d < 0  \qquad else \\
	z + (1+\alpha_d)\textbf{e} 
\end{cases}
$$

for \\(\alpha\_d = inf \{\alpha | z + \alpha \textbf{e} \succeq 0\}\\).

Note \\(\textbf{e}\\) is identity.

