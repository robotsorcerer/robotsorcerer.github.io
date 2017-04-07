---
layout: post
date: 2017-04-03 19:25:00
title: "<center>Neural Networks and Adaptive Control</center>"
excerpt: "<center>Adaptive systems are inherently nonlinear. Their behavior therefore is quite complex, which makes them difficult to analyze. Progress in theory has been slow, and much work remains before a reasonably complete, coherent theory is available. <br>-- Karl Astrom</center>"
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
   
  - [Preamble](#preamble)
  - [Introduction](#introduction)
  - [Feedback Linearization](#feedback-linearization) 
  - [Control Lyapunov Function](#clf)   

<a name="preamble"></a>
## Preamble

Over the past five-some months, my research has come full circle at the intersection of neural networks and nonlinear adaptive systems. The notes below are jottings I made during my learning process. I hope it helps folks just immersing themselves into nonlinear adaptive control using neural networks and function approximators. These notes were sporadically written and may contain some minor typos and shenanigans. I implore the humble inquirer after knowledge to bite the meat, and not my silly typographical errors. Please leave comments if you find errors.

<a name='introduction'></a>
## Introduction

The motivation for adaptive control was from systems whose parameters varied with time. Adaptive control can deal with any size of parametric uncertainty as well as dynamic uncertainties arising from neglected dynamics if correct robust algorithms are used. The bounds for the allowable dynamic uncertainites cannot be calculated as easily as in the nonadaptive case because of the nonlinear nature of the adaptive system coupled with the fact that the plant parameters are deemed unknown. 

Note:

- Adaptive Control designed for LTI plants give rise to a closed-loop system that is nonlinear. 

- As a result poles, zeros, gain and phase margins make little sense for system analysis.

- Nonlinear techniques based on Lyapunov analysis and passivity arguments plus linear systems theory can be used in establishing the stability/robustness and margins that are not so easy to compute as in the LTI case.

- LTI methods can be used in understanding the dynamics of robust modification laws to adaptive systems e.g. dynamic normalizing signal that limits the rate of adaptation to be finite and small relative to level of dynamic uncertainty.

- The limitation of estimated controller parameters to assume large values eliminates the possibility of high gain control

- High gain or high speed control can increase instability due to high bandwidth that the controller is subjected to.

> LTI methods can be used in understanding the dynamics of robust modification laws to adaptive systems e.g. dynamic normalizing signal that limits the rate of adaptation to be finite and small relative to level of dynamic uncertainty.

So you see, adaptive control are really complex to tune and get right. A bit of a background below.

Adaptive control research was motivated in the 50s by the problem of designing autopilots whose parameters changed over a wide operating range in speeds and altitudes. Fixed-gain controllers could not solve the frequent parameter variations in such systems. Therefore, people developed gain scheduling techniques using auxiliary measurements of airspeed. With gain scheduling came rudimentary methods of adjusting the adaptation mechanism in model reference systems -- the idea was to develop a self-tuning controller that adapted for parameter variations in a closed-loop reference model scheme. Adjustment mechnisms developed included sensitivity rules such as M.I.T. rule, which performed reasonably well under some conditions. Rudolf Kalman in 1958 rigorously analyzed the self-tuning controller and established the explicit identification of the controller parameters of a linear SISO plant so that these could be used to tune an optimal linear quadratic controller. 

In the 60's, Parks [1966], demonstrated use of Lyapunov analysis in establishing the stability and convergence of adaptive systems. Advances in system identification enhanced the way update laws were determined for model reference schemes. Stochastic control and dynamic programming (from the work of Bellman) coupled with Lyapunov stability placed a firm footing on proving convergence for adaptive control systems. The 70s era witnessed a resurgence in the complete proofs of stability for model reference adaptive schemes e.g. Liapunov state space proofs from Narendra, Lin & Valavani and Morse. In the discrete time deterministic and stochastic domains, stability proofs also appeared about this time. Then came Rohr's example whereby the assumptions of stability were found to be very sensitive to the presence of unmodeled dynamics (e.g. ignored high-frequency parasitic modes in order not to complicate controller design). Researchers started working on the robustness of adaptive schemes and their sensitivity to transient behaviors. 

> The 70s era witnessed a resurgence in the complete proofs of stability for model reference adaptive schemes e.g. Liapunov state space proofs from Narendra, Lin & Valavani and Morse. In the discrete time deterministic and stochastic domains, stability proofs also appeared about this time. Then came Rohr's example whereby the assumptions of stability were found to be very sensitive to the presence of unmodeled dynamics

The extension of adaptive control to linear time-varying parameters was a major obstacle until the 80s when basic robustness questions were answered. Tactics such as dead-zone modification, dynamic normalizing signal together with leakage or parameter projection were used to deal with a great deal of parameter variations. This class included slowly-varying parameters as well as infrequent jumps in parameter values. In several cases, the error from time-varying signals can be reduced through proper parameterizations of the time-varying plant model used in the control design. In the linear time-varying case, stability margins, bandwidth margins, bandwidth, frequency domain characteristics, poles, zeros do not make much sense even for time-varying parameters unless approximations are made using the assumption of slowly varying parameters, etc.

Adaptive control applied to nonlinear systems is in its infancy. Why is this so?
In nonlinear systems, it is not only the parameters that are nonlinear, but also the functions. Adaptive control was designed to stabilize system parameters by adapting for nonlinear parameters  and **NOT** nonlinear functions. The extension of adaptive controllers to nonlinear systems from LTI and LTV systems is therefore a complicated one. There are two general cases of adopting adaptive control to nonlinear systems: (i) nonlinear systems whose nonlinear functions are known but unknown parameters appear linearly. (ii) the nonlinear functions are assumed known by multiplying nonlinear basis functions with unknown parameters to be determined. The second option falls under categories where the basis functions are typically deduced from neural networks parameters (or weights as they are called) and they are assumed to appear linearly e.g. in a single layer __(so far, this is what has been analytically proven)__. This property is fundamental to developing analytical stability results with large regions of attraction.

Some control background below.

<a name='feedback-linearization'></a>
### Feedback Linearization

Feedback linearization consists in changing the coordinates of a system so as to cancel all or most of the unknown nonlinear terms so that the system behaves as a linear or partly linear system. Consider the following system

\begin{align}
  \dot{x} = f(x) + g(x)u,  \\
  y = h(x)
  \label{eq:nlnr1}
\end{align}

where \\(x \in \mathbb{R}^n, u,y \in \mathbb{R} \text{ and } f,g,h, \\) are smooth nonlinear functions.

Differentiating \\(y\\) in \eqref{eq:nlnr1} with respect to time, we find that

\begin{align}
\dot{y} = \dfrac{\partial{h}}{\partial{x}}(x) f(x) +     \dfrac{\partial{h}}{\partial{x}}(x) g(x) u,
\label{eq:ydot}
\end{align}

where

\begin{align}
\dfrac{\partial{h}}{\partial{x}}(x) f = \dfrac{\partial{h}}{\partial{x}_1}(x) f_1 + \cdots + \dfrac{\partial{h}}{\partial{x}_n}(x) f_n \triangleq L_f \, f
\label{eq:Lie}
\end{align}

where \\(L\_f f\\) is the <i>Lie derivative</i>. If \\(\frac{\partial{h}}{\partial{x}}(x_0) \, g(x\_0) \neq 0\\) at some point \\(x\_0\\), then the system of \eqref{eq:nlnr1} is said to be of relative degree 1 at \\(x\_0\\). For an LTI system, this means the output is different from the input by one integrator only. This would be a strictly proper tranfer function. A good way of thinking about this is that the output has to be differentiated by the number of the relative degree(s) until the input appears in the output expression. 

If \\(\frac{\partial{h}}{\partial{x}}(x) \, g(x) = 0 \forall x \in {B\_x}\_0 \text{ of } x\_0 \\), then one can take the second derivative of \\(y\\) to obtain (abusing notation and dropping the terms in parentheses), 

\begin{align}
\ddot{y} = \dfrac{\partial}{\partial{x}} \left(\dfrac{\partial{h}}{\partial{x}}f\right)f + \dfrac{\partial}{\partial{x}}\left(\dfrac{\partial{h}}{\partial{x}}f\right) g \, u.
\end{align}

If \\(\frac{\partial}{\partial{x}} \left(\frac{\partial{h}}{\partial{x}}(x)f(x)\right) g(x) \, |\ \_{x = x\_0} \neq 0 \\) then \eqref{eq:nlnr1} is said to have a relative degree 2 at \\(x\_0\\). 
We can continue the differentiation in a neighborhood of \\(x\_0\\) if \\(\frac{\partial}{\partial{x}} \left(\frac{\partial{h}}{\partial{x}}(x)f(x)\right)g(x) = 0 \\) in the neighborhood of \\(x\_0\\). 

> There are two general cases of adopting adaptive control to nonlinear systems: (i) nonlinear systems whose nonlinear functions are known but unknown parameters appear linearly. (ii) the nonlinear functions are assumed known by multiplying nonlinear basis functions with unknown parameters to be determined.

More generally, 

\begin{align}
L\_f^i h = \dfrac{\partial}{\partial{x}}\left(\dfrac{\partial}{\partial{x}} \left(\cdot \dfrac{\partial}{\partial{x}} \left(\dfrac{\partial{h}}{\partial{x}}f\right) \cdot f \cdots \right) \cdot f \right) \cdot f.
\end{align}

Defining

\begin{align}
L\_g L\_fh \triangleq \frac{\partial(L\_fh)}{\partial x}\cdot g,
\end{align}

then the SISO nonlinear system \eqref{eq:nlnr1} has a relative degree \\(\rho = n\\) at a point \\(x\_0\\) if

(i)  \\(L\_g L\_f^i h(x) = 0 \forall x \in {B\_x}\_0, \\) where \\({B\_x}\_0\\) is some neighborhood of \\(x\_0\\) \\(\forall i  = 1, 2, 3, \ldots, \rho - 2. \\)

(ii) \\(L\_g L\_f^{\rho -1} h(x\_0) \neq 0. \\)

if \eqref{eq:nlnr1} has relative degree \\(\rho = n\\) at \\(x\\), where \\(n\\) is the order of \eqref{eq:nlnr1}, then given the transfoirmation 

\begin{align}
z\_1 = y = h(x), \qquad z\_2 = \dot{y} = L\_f h(x), \qquad z\_3 = \ddot{y} = L\_f^2 h(x), 
\end{align}

\begin{align}
z\_i = y^{(i-1)} = L\_f^{(i-1)} h(x) , \ldots, z\_n = y^{(n-1)} = L\_f^{n-1} h(x).
\end{align}

we find that 

$$
\dot{z}_1 = z_2, \nonumber \\
\dot{z}_1 = z_2, \nonumber \\
\quad \vdots  \nonumber \\
\dot{z}_{n-1} = z_n,   \nonumber \\
\dot{z}_n = L_f^nh(x) + (L_gL_f^{n-1}h(x))u,  \\
y = z_1
\label{eq:canon}
$$

which is the **<i>canonical form</i>** of the system with _**no zero dynamics**_.  From feedback linearization, we find that 

\begin{align}
u = \dfrac{1}{L\_g L\_f^{n-1}h(x)}[\nu - L\_f^n h(x)],
\label{eq:control}
\end{align}

where \\(\nu \in \mathbb{R} \\) is the new input, leading to the LTI system

$$
\dot{z}_1 = z_2, \\
\dot{z}_2 = z_3, \\
\quad \vdots  \\
\dot{z}_{n-1} = z_n, \\
\dot{z}_n = \nu, \\
y = z_1
$$

Vectorizing the two equations, we have

\begin{align}
\dot{z} = A z + B \nu, \qquad y = C^T z, 
\label{eq:linear}
\end{align}

where 

$$
A = 
\begin{bmatrix}
0      &    1   &    0   & \ldots &    0   \\
\vdots & \ddots & \ddots & \ddots & \vdots \\
\vdots &        & \ddots & \ddots &    0   \\
\vdots &        &        & \ddots &    1   \\
0      & \ldots & \ldots  & \ldots &    0   \\
\end{bmatrix},

\qquad 
B = 
\begin{bmatrix}
0 \\
\vdots \\
\vdots \\
1
\end{bmatrix},

\quad 
C = \begin{bmatrix}
1 \\ 0 \\ \vdots \\ \vdots \\ 0
\end{bmatrix}
$$

\eqref{eq:linear} is an observable and controllable LTI system, and thus the input \\(\nu\\) can be carefully chosen to meet regulation or tracking objectives for the plant output \\(y\\). The \eqref{eq:control} cancels all nonlinearities and turns the closed-loop system to an LTI one. If \eqref{eq:nlnr1} has relative degree \\(\rho < n \\), the change of coordinates become

\begin{align}
z\_1 = y, \quad z\_2 = \dot{y}, \ldots \quad z\_\rho = y^{(\rho-1)} = L\_f^{(\rho -1)h(x) }
\end{align}

thus resulting in 

$$
\dot{z}_1 = z_2 \\
\vdots \\
\dot{z}_{\rho-1} = z_\rho \\
\dot{z}_\rho = L_f^\rho h(x) + \left(L_gL_f^{\rho-1}h(x)\right) u
$$

Since the order of the system is \\(n\\), we are gonna need \\(n - \rho \\) states; we can define functions \\(h\_{\rho+1}(x), \ldots, h\_n(x)\\) with \\(\frac{\partial{h}\_i(x)}{\partial{x}g(x)} = 0, \, i = \rho +1, \ldots, n\\) and define the \\(n - \rho\\)  states as 

\\(z\_{\rho+1} = h\_{\rho + 1}, \ldots, z\_n = h\_n(x)\\)

arising in the additional states

$$
\dot{z}_{\rho+1} = \dfrac{\partial{h}_{\rho+1}(x)}{\partial{x}}\cdot f(x) \triangleq \phi\_{\rho +1}(z), \\
\quad \vdots \\
\dot{z}_{n} = \dfrac{\partial{h}_{n}(x)}{\partial{x}}\cdot f(x) \triangleq \phi_{n}(z), \\
y = z_1
$$

where \\(z = [z\_1, z\_2, \ldots, z\_n]^T\\) is the new state. With feedback linearization, we have 

\begin{align}
u = \dfrac{1}{L\_g L\_f^{\rho-1}h(x)}[\nu - L\_f^\rho h(x)],
\label{eq:control2}
\end{align}

so that we have the system

$$
\dot{z}_1 = z_2 \\
\vdots \\
\dot{z}_{\rho-1} = z_\rho \\
\dot{z}_\rho = \nu, \\
\dot{\rho + 1} = \phi_{\rho +1}(z), \\
\quad \vdots \\
\dot{z}_n = \phi_n(z), \\
y = z_1.
$$

We see that the input \\(\nu\\) may be utilized to drive the output \\(y\\) and states \\(z_1, \ldots, z_\rho\\) to zero or meet some regulation goal for \\(y\\). When the choice of controller \\(\nu\\) does not guarantee that the states \\(z_{\rho+1}, \ldots, z_n \\) are bounded despite \\(z\_1, \ldots, z\_\rho\\) being  driven to zero, we say the states \\(\dot{z}\_{\rho+1}, \ldots, \dot{z}\_n\\) are the zero dynamics of \eqref{eq:nlnr1}. These are the dynamics of \eqref{eq:nlnr1} when \\(y\\) and its first \\(\rho\\) derivatives are set to zero. When the equilibrium states of the \\(z\_{\rho+1}\\) are asymptotically stable, the system is said to be <i>minimum-phase</i>.

The process illustrated above is called I/O feedback linearization. When there are no zero dynamics involved, the process is called <i> full-state feedback linearization</i>.

<a name="clf"></a>
## Control Lyapunov Functions

Lyapunov functions are useful not only in the analysis of adaptive control systems but also as stabilizing feedback control design laws. The central concept is to make the Lyapunov function \\(V\\) and its time derivative obey Lyapunov stability conditions for a closed-loop system.

### Lyapunov's Direct Method 

Lyapunov stability means the sum of all the __energy__ of a system will be continuously dissipated when the system settles to an equilibrium position. This is a statement of the Lyapunov's Direct (or second) method. In other words, we can investigate the stability of an \\(n\\)-dimensional dynamical system by analyzing the change in the behavior of its energy function. Stability analyses are difficult to verify in nonlinear systems and Lyapunov analysis helps us in gaining an insight into system behavior. Take a mass-spring-damper system below, for example. 

<!-- <div class="fig figcenter fighighlight">
  <img src="/imgs/adaptive/msd.jpg" width="80%" height="60%" align="middle">  
  <div class="figcaption" align="middle">Mass-Spring-Damper System.
  </div>
</div> -->

![Mass-Spring-Damper System](/imgs/adaptive/msd.jpg)

Pulling and releasing the mass does not inform us of the system's stability whatsoever. The question of stability in the system is therefore difficult to verify:4, linearization is nearly impossible as it is only marginally stable. But if we can write out the closed-form equations of the system's mechanical energy, we can differentiate this to understand what happens if the mass settles to equilibrium. For observe, 

\begin{align}
V(x) &= \underbrace{\dfrac{1}{2}m \dot{x}^2}\_{\text{kinetic energy}} + \underbrace{\int\_{0}^{x}\left(k\_0x + k\_1x^3\right)dx}\_{\text{potential energy}}
\end{align}

\begin{align}
 &= \frac{1}{2}m \dot{x}^2 + \dfrac{1}{2}k\_0x^2 + {1}{4}k\_1 x^4
\end{align}

The rate of change of the system's energy along the trajectories of the system's motion therefore becomes

\begin{align}
\dot{V}(x) &= m \dot{x} \ddot{x} + \left(k\_0 x + k\_1x^3\right) \dot{x}
\end{align}

\begin{align}
&= \dot{x} \left(-b \dot{x} \|\dot{x}\|\right) = -b \|\dot{x}\|^3 \le 0
\end{align}

#### Being developed