---
layout: post
date: 2017-04-05 11:15:00
title: "Backpropagation and convex programming in MRAS systems."
excerpt: "A contraint-based approach to solving the backpropagation optimization problem in nonlinear model reference adaptive systems."
permalink: QP-Layer-MRAS
comments: true
mathjax: true
category: [convex,qpth,backpropagation]
---

{% include mathjax.md %}

### [Table of Contents](#table-of-contents):

  - [Introduction](#introduction)
  - [Nonlinear (Multivariable) Model Reference Adaptive Systems](#nonlinear)
  - [Solving Quadratic Programming in a Backprop setting](#problem-formulation)  
  - [Slack Variables](#slack-variables)
  - [QP Layer as the last layer in backpropagation](#limitation-backprop)
  - [QP Algorithm](#initialization)
  - [Example Code](#example-codes)
  - [Acknowlegment](#acknowledgements)


<a name='introduction'></a>
## Introduction

The backpropagation algorithm is very useful for general optimization tasks, particularly in neural network function approximators and deep learning applications. Great progress in nonlinear function approximation has been made due to the effectiveness of the backprop algorithm. Whereas in traditional control applications, we typically use feedback regulation to stabilize the states of the system, in model reference adaptive control systems, we want to specify an index of performance to determine the "goodness" of our adaptation. An auxiliary dynamic system called the __reference model__ is used in generating this index of performance (IP). The reference model specifies in terms of the input and states of the model a given index of performance and a comparison check determines appropriate  control laws  by comparing the given IP and measured IP based on the outputs of the adjustable system to that of the reference model system. This is called the **error state space**.

<a name="nonlinear"></a>
### Nonlinear Model Reference Adaptive Systems

With nonlinear systems, the unknown nonlinearity, say \\(f(.)\\), is usually approaximated with a function approximator such as a single hidden layer neural network. To date, the state-of-the-art used in adjusting the weights of a neural network is the [backpropagation algorithm](https://mattmazur.com/2015/03/17/a-step-by-step-backpropagation-example/).  The optimization in classical backprop is unrolled end-to-end so that the complexity of the network increases when we want to add an <i>argmin differentiation layer</i> before the final neural network layer. The final layer determines the controller parameters or generates the control laws used in adjusting the plant behavior. Fitting the control laws into actuator constraints such as model predictive control schemes allow is not explicitly formulated when using the backprop algorithm; ideally, we would want to fit a quadratic convex layer to compute controller parameters exactly. We cannot easily fit a convex optimization layer into the backprop algorithm using classical gradient descent because the explicit Jacobians of the gradients of the system's energy function with respect to system parameters is not exactly formulated (but rather are ordered derivatives which fluctuate about the global/local minimum when the weights of the network converge).


> The final layer determines the controller parameters or generates the control laws used in adjusting the plant behavior. Fitting the control laws into actuator constraints such as model predictive control schemes allow is not explicitly formulated when using the backprop algorithm; ideally, we would want to fit a quadratic convex layer to compute controller parameters exactly.

To generate control laws such as torques to control a motor arm in a multi-dof robot-arm for example, we would want to define a quadratic programming layer as the last layer of our neural network optimization algorithm so that effective control laws that exactly fit into actuator saturation limits are generated. Doing this requires a bit of tweaking of the backprop algorithm on our part.

<a name="problem-formulation"></a>
### Solving Quadratic Programming in a Backprop setting

When trying to construct a controller for a regulator, or an MRAS system, we may imagine that the control law determination is a search process for a control scheme that takes an arbitrary nonzero initial state to a zero state, ideally in a short amount of time. If the system is controllable, then we may require the controller taking the system, from state \\(x(t\_0)\\) to the zero state at time \\(T\\). If \\(T\\) is closer to \\(t\_0\\) than not, more control effort would be required to bear states to \\(t\_0\\). This would  ensure the transfer of states. In most engineering systems, an upper bound is set on the magnitudes of the variables for pragmatic purposes. It therefore becomes impossible to take \\(T\\) to \\(0\\) without exceeding the control bounds. Unless we are ready to tolerate high gain terms in the controller parameters, the control is not feasible for finite T. So what do we do? To meet the practical bounds manufacturers place on physical actuators, it suffices to manually formulate these bounds as constraints into the control design objectives.  

Model predictive controllers have explicit ways of incorporating these constraints into the control design. There are no rules for tuning the parameters of an MRAC system so that the control laws generated in our adjustment mechanism are scaled into the bounds of the underlying actuator.

Since most controller hardware constraints are specified in terms of lower and upper bounded saturation, the QP problem formulated below is limited to inequality constraints. For  equality-constrained QP problems, [Mattingley and Boyd](https://stanford.edu/~boyd/papers/pdf/code_gen_impl.pdf), [Vanderberghe's CVX Optimization](http://www.seas.ucla.edu/~vandenbe/publications/coneprog.pdf), or  Brandon Amos' [ICML submission](https://arxiv.org/pdf/1703.00443.pdf) offer good treatments.

> There are no rules for tuning the parameters of an MRAC system so that the control laws generated in our adjustment mechanism are scaled into the bounds of the underlying actuator.


We define the standard QP canonical form problem with inequality contraints thus:

\begin{align}
\text{minimize} \quad  \frac{1}{2}x^TQx + q^Tx
\label{eq:orig}
\end{align}

subject to 	

\begin{align}
G x \le h  \nonumber
\end{align}

where \\(Q \succeq \mathbb{S}^n_+ \\) (i.e. a symmetric, positive semi-definite matrix) \\(\in \mathbb{R}^n, q \in \mathbb{R}^n, G \in \mathbb{R}^{p \times n}, \text{ and } h \in \mathbb{R}^p \\). Suppose we have our convex quadratic optimization problem in canonical form, we can use primal-dual interior point methods (PDIPM) to find an optimal solution to such a problem. PDIPMs are the state-of-the-art in solving such problems. Primal-dual methods with Mehrota predictor-corrector are consistent for reliably solving QP embedded optimization problems within 5-25iterations, without warm-start ([Boyd and Mattingley, 2012](https://stanford.edu/~boyd/papers/pdf/code_gen_impl.pdf)).

<a name="slack-variables"></a>
### Slack Variables
Given \eqref{eq:orig}, one can introduce slack variables, \\(s \in \mathbb{R}^p\\) as follows,

\begin{align}
\text{minimize}  \quad \frac{1}{2}x^TQx + q^Tx
\label{eq:orig1}
\end{align}

subject to

\begin{align}
\quad G x + s =  h, \qquad s \ge 0 \nonumber
\end{align}

where \\(x \in \mathbb{R}^n, s \in \mathbb{R}^p\\). If we let a dual variable \\(z \in \mathbb{R}^p \\) be associated with the inequality constraint, then we can define the KKT conditions for \eqref{eq:orig1} as

$$
Gx + s = h, \quad s \ge 0 \\
z \ge 0 \\
Qx + q + G^T = 0 \\ \\
z_i s_i = 0, i = 1, \ldots, p.
$$

More formally, if we write the Lagrangian of system \eqref{eq:orig} as

\begin{align}
L(z, \lambda) = \frac{1}{2}x^TQx + q^Tx +\lambda^T(Gz -h)
\label{eq:Lagrangian}
\end{align}

it follows that the KKT for [stationarity, primal feasibility and complementary slackness](https://www.cs.cmu.edu/~ggordon/10725-F12/slides/16-kkt.pdf) are,


\begin{align}
Q x^\ast + q + G^T \lambda^\ast = 0 ,
\label{eq:KKTLagrangian}
\end{align}

$$
K \left(\lambda^\ast\right) \left(G x^\ast - h\right) = 0
$$

where \\(K(\cdot) = \textbf{diag}(k) \\) is an operator that creates a matrix diagonal of the entries of the vector \\(k\\). Computing the time-derivative of \eqref{eq:KKTLagrangian}, we find that

\begin{align}
dQ x^* + Q dx + dq + dG^T \lambda^* + G^T d\lambda = 0
\label{eq:KKTDiff}
\end{align}

$$
K(\lambda^*)\left(G x^* - h\right) = 0
$$

<a name="limitation-backprop"></a>
### QP Layer as the last layer in backpropagation

Vectorizing \eqref{eq:KKTDiff}, we find  

$$
\begin{bmatrix}
Q & G^T   \\
K(\lambda^\ast) G & K(dGx^\ast - h)  \\
\end{bmatrix}

\begin{bmatrix}
dx \\
d\lambda \\
\end{bmatrix}

=

\begin{bmatrix}
-dQ x^\ast - dq - dG^T \lambda^\ast \\
-K(\lambda^\ast) dG x^\ast + DK(\lambda^\ast) dh \\
\end{bmatrix}
$$

so that the Jacobians of the variables to be optimized can be formed with respect to the states of the system. Finding \\(\dfrac{\partial J}{\partial h^*}\\), for example, would involve  passing \\(dh\\) as identity and setting other terms on the rhs in the equation above to zero. After solving the equation, the desired Jacobian would be \\(dz\\). With backpropagation, however, the explicit Jacobians are useless  since the gradients of the network parameters are computed using chain rule for <i>ordered derivatives</i> i.e.

$$
\dfrac{\partial ^+ J}{ \partial h_i} = \dfrac{\partial J}{ \partial h_i} + \sum_{j > i} \dfrac{\partial ^+ J}{\partial h_j} \dfrac{ {\partial} h_j}{ \partial h_i}
$$

where the derivatives with superscripts denote <i>ordered derivatives</i> and those with subscripts denote ordinary partial derivatives. The simple partial derivatives denote the direct effect of \\(h\_i\\) on \\(h\_j\\) through the <i>linear set of equations </i> that determine \\(h\_j\\). To illustrate further, suppose that we have a system of equations given by

$$
x_2 = 3  x_1 \\
x_3 = 5  x_1 + 8  x_2
$$

The ordinary partial derivatives of \\(x\_3\\) with respect to \\(x\_1\\) would be \\(5\\). However, the ordered derivative of \\(x\_3\\) with respect to \\(x\_1\\) would be \\(29\\) (because of the indirect effect by way of \\(x\_2\\)).

So with the backprop algorithm, we would form the left matrix-vector product with a previous backward pass vector, \\(\frac{\partial J}{\partial x^\ast} \in \mathbb{R}^n \\); this is mathematically equivalent to  \\(\frac{\partial J}{ \partial x^\ast} \cdot \frac{\partial x^\ast}{ \partial h} \\). Therefore, computing the solution for the derivatives of the optimization variables \\(dx, d\lambda\\), we have through the matrix inversion of \eqref{eq:KKTDiff},

$$
\begin{bmatrix}
dx \\ d\lambda
\end{bmatrix}
=
\begin{bmatrix}
Q & G^T K(\lambda^\ast) \\
G & K(Gx^\ast - h)
\end{bmatrix}^{-1}
=
\begin{bmatrix}
{\dfrac{dJ}{dx^\ast}}^T \\ 0
\end{bmatrix}.
$$

The relevant gradients with respect to every QP paramter is given by

$$
\dfrac{\partial J}{\partial q} = d_x, \qquad \dfrac{\partial J}{ \partial h} = -K(\lambda^\ast) d_\lambda \\

\dfrac{\partial J}{\partial Q} = \frac{1}{2}(d_x x^T + x d_x^T),  \qquad \dfrac{\partial J}{\partial G} = K(\lambda^\ast)(d_\lambda z^T + \lambda d_z^T
)
$$

<a name="initialization"></a>
### QP Initialization

For the primal problem,

$$
 \text{minimize} \quad \frac{1}{2}x^T Q  x + p^T x + (\frac{1}{2}\|s\|^2_2) \\
 \text{ subject to } \quad Gx + s = h \\
$$

 with \\(x\\) and \\(s\\) as variables to be optimized, the corresponding dual problem is,

$$
  \text{maximize} \quad -\frac{1}{2}w^T Q  w - h^T z + (\frac{1}{2}\|z\|^2_2) \\
 \text{ subject to } \quad Qw + G^T z +  q = 0 \\
$$

 with variables \\(w\\) and \\(z\\) to be optimized.

<a name="optimization-steps"></a>
### Optimization Steps

-	When the primal and dual starting points \\(\hat{x}, \hat{s}, \hat{y}, \hat{z} \\) are unknown, they can be initialized as proposed by Vanderberghe in [cvxopt](http://www.seas.ucla.edu/~vandenbe/publications/coneprog.pdf) namely, we solve the following linear equations

$$
\begin{bmatrix}
G &  -I  \\
Q & G^T
\end{bmatrix}

\begin{bmatrix}
z \\
x \\
\end{bmatrix}
=
\begin{bmatrix}
h \\
-q \\
\end{bmatrix}
$$

with the assumption that \\(\hat{x} = x,\hat{y} = y\\).

The initial value of \\(\hat{s}\\) is computed from the residual \\(h - Gx = -z\\), as

$$
\hat{s} = \begin{cases}
	-z \qquad  \text{ if } \alpha_p < 0  \qquad else \\
	-z + (1+\alpha_p)\textbf{e}
\end{cases}
$$

for \\(\alpha\_p = \text{ inf } \{ \alpha \| -z + \alpha \textbf{e} \succeq 0 \} \\).

Similarly, \\(z\\) at the first iteration is computed as follows

$$
\hat{z} = \begin{cases}
	z \qquad  \text{ if } \alpha_d < 0  \qquad else \\
	z + (1+\alpha_d)\textbf{e}
\end{cases}
$$

for \\(\alpha\_d = \text{ inf } \{ \alpha \| z + \alpha \textbf{e} \succeq 0 \} \\).

Note \\(\textbf{e}\\) is identity.


-	Following Boyd and Mattingley's convention, we can compute the afiine scaling directions by solving the system,


	$$
	\begin{bmatrix}
	G    &I &0\\
	0   &K(z) & K(s) \\
	Q 	&0 	&G^T
	\end{bmatrix}

	\begin{bmatrix}
	\Delta z^{aff} \\
	\Delta s^{aff} \\
	\Delta x^{aff}
	\end{bmatrix}
	=
	\begin{bmatrix}
	-Gx - s + h \\
	-K(s)z \\
	-G^Tz + Qx + q
	\end{bmatrix}
	$$

	with \\( K(s) \text{ as } \textbf{diag}(s) \text{ and } K(z) \text{ as } \textbf{diag(z)} \\)

-	The centering-plus-corrector directions  can be used to efficiently compute the primal and sualvariables by solving

	$$
	\begin{bmatrix}
	G    &I &0\\
	0   &K(z) & K(s) \\
	Q 	&0 	&G^T
	\end{bmatrix}

	\begin{bmatrix}
	\Delta z^{cc} \\
	\Delta s^{cc} \\
	\Delta x^{cc}
	\end{bmatrix}
	=
	\begin{bmatrix}
	0 \\
	\sigma \mu \textbf{e} - K(\Delta s^{aff}) \Delta z^{aff} \\
	0
	\end{bmatrix}
	$$

	where

	\begin{align}
	\alpha = \left(\dfrac{(s+ \alpha \Delta s^{aff})^T(z + \alpha \Delta z^{aff})}{s^Tz}\right)^3 \nonumber
	\end{align}

	and the step size \\(\alpha = \text{sup} {\alpha \in [0, 1] \| s + \alpha \Delta s^{aff} \ge 0, \, z + \alpha \Delta z^{aff} \ge 0}. \\)

- Finding the primal and dual variables is then a question of composing the two updates in the foregoing to yield

	$$
	x \leftarrow x + \alpha \Delta x, \\
	s \leftarrow s + \alpha \Delta s, \\
	z \leftarrow z + \alpha \Delta z.
	$$

<a name="example-codes"></a>
### Example code

An example implementation of this algorithm in the PyTorch Library is available on my [github page](https://github.com/lakehanne/RAL2017/blob/devel/pyrnn/src/model.py).

<a name="acknowledgements"></a>
### Acknowledgment

I would like to thank [Brandon Amos](https://bamos.github.io/) of the CMU Locus Lab for his generosity in answering my questions while using his [qpth OptNET framework](https://locuslab.github.io/qpth/).
