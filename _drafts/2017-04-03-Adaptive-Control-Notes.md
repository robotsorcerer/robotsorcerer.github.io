---
layout: post
date: 2017-04-03 12:25:00
title: "Neural Networks and Adaptive Control"
excerpt: "Adaptive systems are inherently nonlinear. Their behavior therefore is quite complex, which makes them difficult to analyze. Progress in theory has been slow, and much work remains before a reasonably complete, coherent theory is available."
permalink: adaptive-control
comments: true
mathjax: true
category: [control]
---


### Neural Networks and Adaptive Control

Adaptive systems are inherently nonlinear. Their behavior therefore is quite complex, which makes them difficult to analyze. Progress in theory has been slow, and much work remains before a reasonably complete, coherent theory is available. <br>-- Karl Astrom

### Table of Contents
<ul>
<li><a href="#preamble">Preamble</a></li>
<li><a href="#introduction">Introduction</a></li>
<li><a href="#feedback-linearization">Feedback Linearization</a></li>
<li><a href="#clf">Control Lyapunov Function</a></li>
</ul>

<a name="user-content-preamble"></a>
#### Preamble

Over the past five-some months, my research has come full circle at the intersection of neural networks and nonlinear adaptive systems. The notes below are jottings I made during my learning process. I hope it helps folks just immersing themselves into nonlinear adaptive control using neural networks and function approximators. These notes were sporadically written and may contain some minor typos and shenanigans. I implore the humble inquirer after knowledge to bite the meat, and not my silly typographical errors. Please leave comments if you find errors.

<a name="user-content-introduction"></a>
#### Introduction

The motivation for adaptive control was from systems whose parameters varied with time. Adaptive control can deal with any size of parametric uncertainty as well as dynamic uncertainties arising from neglected dynamics if correct robust algorithms are used. The bounds for the allowable dynamic uncertainites cannot be calculated as easily as in the nonadaptive case because of the nonlinear nature of the adaptive system coupled with the fact that the plant parameters are deemed unknown.

<p>Note:</p>
<ul>
<li>
<p>Adaptive Control designed for LTI plants give rise to a closed-loop system that is nonlinear.</p>
</li>
<li>
<p>As a result poles, zeros, gain and phase margins make little sense for system analysis.</p>
</li>
<li>
<p>Nonlinear techniques based on Lyapunov analysis and passivity arguments plus linear systems theory can be used in establishing the stability/robustness and margins that are not so easy to compute as in the LTI case.</p>
</li>
<li>
<p>LTI methods can be used in understanding the dynamics of robust modification laws to adaptive systems e.g. dynamic normalizing signal that limits the rate of adaptation to be finite and small relative to level of dynamic uncertainty.</p>
</li>
<li>
<p>The limitation of estimated controller parameters to assume large values eliminates the possibility of high gain control</p>
</li>
<li>
<p>High gain or high speed control can increase instability due to high bandwidth that the controller is subjected to.</p>
</li>
</ul>
<blockquote>
<p>LTI methods can be used in understanding the dynamics of robust modification laws to adaptive systems e.g. dynamic normalizing signal that limits the rate of adaptation to be finite and small relative to level of dynamic uncertainty.</p>
</blockquote>

So you see, adaptive control are really complex to tune and get right. A bit of a background below.

<p>Adaptive control research was motivated in the 50s by the problem of designing autopilots whose parameters changed over a wide operating range in speeds and altitudes. Fixed-gain controllers could not solve the frequent parameter variations in such systems. Therefore, people developed gain scheduling techniques using auxiliary measurements of airspeed. With gain scheduling came rudimentary methods of adjusting the adaptation mechanism in model reference systems -- the idea was to develop a self-tuning controller that adapted for parameter variations in a closed-loop reference model scheme. Adjustment mechnisms developed included sensitivity rules such as M.I.T. rule, which performed reasonably well under some conditions. Rudolf Kalman in 1958 rigorously analyzed the self-tuning controller and established the explicit identification of the controller parameters of a linear SISO plant so that these could be used to tune an optimal linear quadratic controller.</p>
<p>In the 60's, Parks [1966], demonstrated use of Lyapunov analysis in establishing the stability and convergence of adaptive systems. Advances in system identification enhanced the way update laws were determined for model reference schemes. Stochastic control and dynamic programming (from the work of Bellman) coupled with Lyapunov stability placed a firm footing on proving convergence for adaptive control systems. The 70s era witnessed a resurgence in the complete proofs of stability for model reference adaptive schemes e.g. Liapunov state space proofs from Narendra, Lin &amp; Valavani and Morse. In the discrete time deterministic and stochastic domains, stability proofs also appeared about this time. Then came Rohr's example whereby the assumptions of stability were found to be very sensitive to the presence of unmodeled dynamics (e.g. ignored high-frequency parasitic modes in order not to complicate controller design). Researchers started working on the robustness of adaptive schemes and their sensitivity to transient behaviors.</p>
<blockquote>
<p>The 70s era witnessed a resurgence in the complete proofs of stability for model reference adaptive schemes e.g. Liapunov state space proofs from Narendra, Lin &amp; Valavani and Morse. In the discrete time deterministic and stochastic domains, stability proofs also appeared about this time. Then came Rohr's example whereby the assumptions of stability were found to be very sensitive to the presence of unmodeled dynamics</p>
</blockquote>
<p>The extension of adaptive control to linear time-varying parameters was a major obstacle until the 80s when basic robustness questions were answered. Tactics such as dead-zone modification, dynamic normalizing signal together with leakage or parameter projection were used to deal with a great deal of parameter variations. This class included slowly-varying parameters as well as infrequent jumps in parameter values. In several cases, the error from time-varying signals can be reduced through proper parameterizations of the time-varying plant model used in the control design. In the linear time-varying case, stability margins, bandwidth margins, bandwidth, frequency domain characteristics, poles, zeros do not make much sense even for time-varying parameters unless approximations are made using the assumption of slowly varying parameters, etc.</p>
<p>Adaptive control applied to nonlinear systems is in its infancy. Why is this so?
In nonlinear systems, it is not only the parameters that are nonlinear, but also the functions. Adaptive control was designed to stabilize system parameters by adapting for nonlinear parameters  and <strong>NOT</strong> nonlinear functions. The extension of adaptive controllers to nonlinear systems from LTI and LTV systems is therefore a complicated one. There are two general cases of adopting adaptive control to nonlinear systems: (i) nonlinear systems whose nonlinear functions are known but unknown parameters appear linearly. (ii) the nonlinear functions are assumed known by multiplying nonlinear basis functions with unknown parameters to be determined. The second option falls under categories where the basis functions are typically deduced from neural networks parameters (or weights as they are called) and they are assumed to appear linearly e.g. in a single layer <strong>(so far, this is what has been analytically proven)</strong>. This property is fundamental to developing analytical stability results with large regions of attraction.</p>
<p>Some control background below.</p>
<p><a name="user-content-feedback-linearization"></a></p>
#### Feedback Linearization

<p>Feedback linearization consists in changing the coordinates of a system so as to cancel all or most of the unknown nonlinear terms so that the system behaves as a linear or partly linear system. Consider the following system</p>

<p>\begin{align}
\label{eq:nlnr1}
\dot{x} = f(x) + g(x)u,  \
y = h(x)
\end{align}</p>

<p>where \(x \in \mathbb{R}^n, u,y \in \mathbb{R} \text{ and } f,g,h, \) are smooth nonlinear functions.</p>
<p>Differentiating \(y\) in \eqref{eq:nlnr1} with respect to time, we find that</p>
<p>\begin{align}
\dot{y} = \dfrac{\partial{h}}{\partial{x}}(x) f(x) +     \dfrac{\partial{h}}{\partial{x}}(x) g(x) u,
\label{eq:ydot}
\end{align}</p>
<p>where</p>
<p>\begin{align}
\dfrac{\partial{h}}{\partial{x}}(x) f = \dfrac{\partial{h}}{\partial{x}_1}(x) f_1 + \cdots + \dfrac{\partial{h}}{\partial{x}_n}(x) f_n \triangleq L_f , f
\label{eq:Lie}
\end{align}</p>
<p>where \(L_f f\) is the <i>Lie derivative</i>. If \(\frac{\partial{h}}{\partial{x}}(x_0) , g(x_0) \neq 0\) at some point \(x_0\), then the system of \eqref{eq:nlnr1} is said to be of relative degree 1 at \(x_0\). For an LTI system, this means the output is different from the input by one integrator only. This would be a strictly proper tranfer function. A good way of thinking about this is that the output has to be differentiated by the number of the relative degree(s) until the input appears in the output expression.</p>
<p>If \(\frac{\partial{h}}{\partial{x}}(x) , g(x) = 0 \forall x \in {B_x}_0 \text{ of } x_0 \), then one can take the second derivative of \(y\) to obtain (abusing notation and dropping the terms in parentheses),</p>
<p>\begin{align}
\ddot{y} = \dfrac{\partial}{\partial{x}} \left(\dfrac{\partial{h}}{\partial{x}}f\right)f + \dfrac{\partial}{\partial{x}}\left(\dfrac{\partial{h}}{\partial{x}}f\right) g , u.
\end{align}</p>
<p>If \(\frac{\partial}{\partial{x}} \left(\frac{\partial{h}}{\partial{x}}(x)f(x)\right) g(x) , |\ _{x = x_0} \neq 0 \) then \eqref{eq:nlnr1} is said to have a relative degree 2 at \(x_0\).
We can continue the differentiation in a neighborhood of \(x_0\) if \(\frac{\partial}{\partial{x}} \left(\frac{\partial{h}}{\partial{x}}(x)f(x)\right)g(x) = 0 \) in the neighborhood of \(x_0\).</p>
<blockquote>
<p>There are two general cases of adopting adaptive control to nonlinear systems: (i) nonlinear systems whose nonlinear functions are known but unknown parameters appear linearly. (ii) the nonlinear functions are assumed known by multiplying nonlinear basis functions with unknown parameters to be determined.</p>
</blockquote>
<p>More generally,</p>
<p>\begin{align}
L_f^i h = \dfrac{\partial}{\partial{x}}\left(\dfrac{\partial}{\partial{x}} \left(\cdot \dfrac{\partial}{\partial{x}} \left(\dfrac{\partial{h}}{\partial{x}}f\right) \cdot f \cdots \right) \cdot f \right) \cdot f.
\end{align}</p>
<p>Defining</p>
<p>\begin{align}
L_g L_fh \triangleq \frac{\partial(L_fh)}{\partial x}\cdot g,
\end{align}</p>
<p>then the SISO nonlinear system \eqref{eq:nlnr1} has a relative degree \(\rho = n\) at a point \(x_0\) if</p>
<p>(i)  \(L_g L_f^i h(x) = 0 \forall x \in {B_x}_0, \) where \({B_x}_0\) is some neighborhood of \(x_0\) \(\forall i  = 1, 2, 3, \ldots, \rho - 2. \)</p>
<p>(ii) \(L_g L_f^{\rho -1} h(x_0) \neq 0. \)</p>
<p>if \eqref{eq:nlnr1} has relative degree \(\rho = n\) at \(x\), where \(n\) is the order of \eqref{eq:nlnr1}, then given the transfoirmation</p>
<p>\begin{align}
z_1 = y = h(x), \qquad z_2 = \dot{y} = L_f h(x), \qquad z_3 = \ddot{y} = L_f^2 h(x),
\end{align}</p>
<p>\begin{align}
z_i = y^{(i-1)} = L_f^{(i-1)} h(x) , \ldots, z_n = y^{(n-1)} = L_f^{n-1} h(x).
\end{align}</p>
<p>we find that</p>
<p>$$
\dot{z}_1 = z_2, \nonumber \
\dot{z}<em>1 = z_2, \nonumber \
\quad \vdots  \nonumber \
\dot{z}</em>{n-1} = z_n,   \nonumber \
\dot{z}_n = L_f^nh(x) + (L_gL_f^{n-1}h(x))u,  \
y = z_1
\label{eq:canon}
$$</p>
<p>which is the <strong><i>canonical form</i></strong> of the system with <em><strong>no zero dynamics</strong></em>.  From feedback linearization, we find that</p>
<p>\begin{align}
u = \dfrac{1}{L_g L_f^{n-1}h(x)}[\nu - L_f^n h(x)],
\label{eq:control}
\end{align}</p>
<p>where \(\nu \in \mathbb{R} \) is the new input, leading to the LTI system</p>
<p>$$
\dot{z}_1 = z_2, \
\dot{z}<em>2 = z_3, \
\quad \vdots  \
\dot{z}</em>{n-1} = z_n, \
\dot{z}_n = \nu, \
y = z_1
$$</p>
<p>Vectorizing the two equations, we have</p>
<p>\begin{align}
\dot{z} = A z + B \nu, \qquad y = C^T z,
\label{eq:linear}
\end{align}</p>
<p>where</p>
<p>$$
A =
\begin{bmatrix}
0      &amp;    1   &amp;    0   &amp; \ldots &amp;    0   \
\vdots &amp; \ddots &amp; \ddots &amp; \ddots &amp; \vdots \
\vdots &amp;        &amp; \ddots &amp; \ddots &amp;    0   \
\vdots &amp;        &amp;        &amp; \ddots &amp;    1   \
0      &amp; \ldots &amp; \ldots  &amp; \ldots &amp;    0   \
\end{bmatrix},</p>
<p>\qquad
B =
\begin{bmatrix}
0 \
\vdots \
\vdots \
1
\end{bmatrix},</p>
<p>\quad
C = \begin{bmatrix}
1 \ 0 \ \vdots \ \vdots \ 0
\end{bmatrix}
$$</p>
<p>\eqref{eq:linear} is an observable and controllable LTI system, and thus the input \(\nu\) can be carefully chosen to meet regulation or tracking objectives for the plant output \(y\). The \eqref{eq:control} cancels all nonlinearities and turns the closed-loop system to an LTI one. If \eqref{eq:nlnr1} has relative degree \(\rho &lt; n \), the change of coordinates become</p>
<p>\begin{align}
z_1 = y, \quad z_2 = \dot{y}, \ldots \quad z_\rho = y^{(\rho-1)} = L_f^{(\rho -1)h(x) }
\end{align}</p>
<p>thus resulting in</p>

\begin{align}
\dot{z}\_1 = z\_2 \ldots, \dot{z}{\rho-1} = z\_\rho, \ldots \dot{z}\_\rho = L\_f^\rho h(x) + \left(L\_gL_f^{\rho-1}h(x)\right) u
\end{align}

<p>Since the order of the system is \(n\), we are gonna need \(n - \rho \) states; we can define functions \(h_{\rho+1}(x), \ldots, h_n(x)\) with \(\frac{\partial{h}_i(x)}{\partial{x}g(x)} = 0, , i = \rho +1, \ldots, n\) and define the \(n - \rho\)  states as</p>
<p>\(z_{\rho+1} = h_{\rho + 1}, \ldots, z_n = h_n(x)\)</p>
<p>arising in the additional states</p>
<p>$$
\dot{z}<em>{\rho+1} = \dfrac{\partial{h}</em>{\rho+1}(x)}{\partial{x}}\cdot f(x) \triangleq \phi_{\rho +1}(z), \
\quad \vdots \
\dot{z}<em>{n} = \dfrac{\partial{h}</em>{n}(x)}{\partial{x}}\cdot f(x) \triangleq \phi_{n}(z), \
y = z_1
$$</p>
<p>where \(z = [z_1, z_2, \ldots, z_n]^T\) is the new state. With feedback linearization, we have</p>
<p>\begin{align}
u = \dfrac{1}{L_g L_f^{\rho-1}h(x)}[\nu - L_f^\rho h(x)],
\label{eq:control2}
\end{align}</p>
<p>so that we have the system</p>
<p>$$
\dot{z}<em>1 = z_2 \
\vdots \
\dot{z}</em>{\rho-1} = z_\rho \
\dot{z}<em>\rho = \nu, \
\dot{\rho + 1} = \phi</em>{\rho +1}(z), \
\quad \vdots \
\dot{z}_n = \phi_n(z), \
y = z_1.
$$</p>
<p>We see that the input \(\nu\) may be utilized to drive the output \(y\) and states \(z_1, \ldots, z_\rho\) to zero or meet some regulation goal for \(y\). When the choice of controller \(\nu\) does not guarantee that the states \(z_{\rho+1}, \ldots, z_n \) are bounded despite \(z_1, \ldots, z_\rho\) being  driven to zero, we say the states \(\dot{z}_{\rho+1}, \ldots, \dot{z}_n\) are the zero dynamics of \eqref{eq:nlnr1}. These are the dynamics of \eqref{eq:nlnr1} when \(y\) and its first \(\rho\) derivatives are set to zero. When the equilibrium states of the \(z_{\rho+1}\) are asymptotically stable, the system is said to be <i>minimum-phase</i>.</p>
<p>The process illustrated above is called I/O feedback linearization. When there are no zero dynamics involved, the process is called <i> full-state feedback linearization</i>.</p>
<p><a name="user-content-clf"></a>
#### Control Lyapunov Functions

Lyapunov functions are useful not only in the analysis of adaptive control systems but also as stabilizing feedback control design laws. The central concept is to make the Lyapunov function \\(V\\) and its time derivative obey Lyapunov stability conditions for a closed-loop system.

#### Lyapunov's Direct Method
<p>Lyapunov stability means the sum of all the <strong>energy</strong> of a system will be continuously dissipated when the system settles to an equilibrium position. This is a statement of the Lyapunov's Direct (or second) method. In other words, we can investigate the stability of an \(n\)-dimensional dynamical system by analyzing the change in the behavior of its energy function. Stability analyses are difficult to verify in nonlinear systems and Lyapunov analysis helps us in gaining an insight into system behavior. Take a mass-spring-damper system below, for example.</p>

<p>Pulling and releasing the mass does not inform us of the system's stability whatsoever. The question of stability in the system is therefore difficult to verify:4, linearization is nearly impossible as it is only marginally stable. But if we can write out the closed-form equations of the system's mechanical energy, we can differentiate this to understand what happens if the mass settles to equilibrium. For observe,</p>
<p>\begin{align}
V(x) &amp;= \underbrace{\dfrac{1}{2}m \dot{x}^2}_{\text{kinetic energy}} + \underbrace{\int_{0}^{x}\left(k_0x + k_1x^3\right)dx}_{\text{potential energy}}
\end{align}</p>
<p>\begin{align}
&amp;= \frac{1}{2}m \dot{x}^2 + \dfrac{1}{2}k_0x^2 + {1}{4}k_1 x^4
\end{align}</p>
<p>The rate of change of the system's energy along the trajectories of the system's motion therefore becomes</p>
<p>\begin{align}
\dot{V}(x) &amp;= m \dot{x} \ddot{x} + \left(k_0 x + k_1x^3\right) \dot{x}
\end{align}</p>
<p>\begin{align}
&amp;= \dot{x} \left(-b \dot{x} |\dot{x}|\right) = -b |\dot{x}|^3 \le 0
\end{align}</p>


#### Being developed
  