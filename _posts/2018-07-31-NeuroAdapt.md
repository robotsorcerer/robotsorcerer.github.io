---
layout: post
date: 2018-07-31 02:19:00
title: "Neural Networks and Adaptive Control"
excerpt: "This post deals with understanding the the role of neural networks in adaptive control theory. It is mostly based on my oral presentation at 2017 IROS and at Google Robotics in Mountain View."
permalink: neuro-adaptive-control
comments: true
category: [control,adaptive-control]
---
{% include mathjax.md %}

+ [Table of Contents](#table-contents)

+ [Intro](#intro)

+ [History Teaser](#history)

+ [Adaptive Systens](#adaptive-systems)

  - [Nonlinear neuro-control](#nonlinear)

  - [Adaptive Neuro-Control: The Reconstruction Error Brouhaha](#brouhaha)

  - [Reconstruction Error Python Example](#rec-example)


<a name="table-contents"></a>
### Intro

It's been more than a year since my last post. I am sorry. I blame the publish or perish academic mantra. Now that I am toward the end of my degree, I shall try to keep up to date by elucidating on topics that capture my imagination right here. Before we dive into the proper topic, allow me the opportunity to delve a little deeper into the history and and how the development of adaptive control theory became a field of study.


<a name="history"></a>
#### History Teaser

Adaptive control research was motivated in the '50s by the problem of designing autopilots whose parameters changed over a wide operating range in speeds and altitudes. Classical fixed-gain controllers could not solve the frequent parameter variations in such systems. Therefore people developed gain scheduling techniques with auxiliary measurements of airspeed in controlling aircrafts. With gain scheduling came basic methods for adjusting the adaptation mechanism in model reference systems -- the idea was to develop a self-tuning controller that adapted for parameter variations in a closed-loop reference model scheme. Adjustment mechanisms developed included sensitivity rules such as the M.I.T. rule, which performed reasonably well under some conditions. Rudolf Kalman in 1958 rigorously analyzed the self-tuning controller and established the explicit identification of the controller parameters of a linear SISO (Single-Input, Single-Output) plant so that these could be used to tune an optimal linear quadratic (LQ) controller. In the 60's, Parks [1966], demonstrated use of Lyapunov analysis in establishing the stability and convergence of adaptive systems. Advances in system identification enhanced the way update laws were determined for model reference schemes. Stochastic control and dynamic programming coupled with Lyapunov stability laws placed a firm footing on proving convergence for adaptive control systems. The '70s era witnessed a resurgence in the complete proofs of stability for model reference adaptive schemes e.g. Lyapunov state space proofs from Narendra, Lin and Valavani, and Morse. In the discrete time deterministic and stochastic domains, stability proofs also appeared about this time. Then came Rohr's example in the '80's where the assumptions of stability were found to be very sensitive to the presence of unmodeled dynamics (e.g. ignored high-frequency parasitic modes in order not to complicate controller design). Researchers started working on the robustness of adaptive schemes and their sensitivity to transient behaviors. The extension of adaptive control to linear time-varying parameters was a major obstacle until the '80s when basic robustness questions were answered. Tactics such as dead-zone modification, dynamic normalizing signal together with leakage or parameter projection were used to deal with a great deal of parameter variations. This class included slowly-varying parameters as well as infrequent jumps in parameter values. In several cases, the error from time-varying signals were reduced through proper parameterizations of the time-varying plant model used in the control design.

<a name="adaptive-systems"></a>
#### On adaptive systems

If we relax the restrictive assumptions that govern the implementation of adaptive control on physical systems, adaptive control can deal with any size of parametric uncertainty, as well as the dynamic uncertainties that arise from neglected dynamics if correct robust algorithms are used. Most of the stability results on adaptive systems that appeared in the '80s dealt mostly with cases where no modeling errors were present -- a very restrictive assumption [^Ioannou1] <sup>&</sup> [^Ioannou2]. While LTI methods can be used in understanding the dynamics of robust modification laws to adaptive systems e.g. dynamic normalizing signal that limits the rate of adaptation to be finite and small relative to level of dynamic uncertainty, adaptive control designed for LTI plants give rise to closed-loop systems that are nonlinear [^Sastry]. Thus, traditional methods for analyzing stability such as poles, zeros, gain and phase margins make little sense for analyzing such nonlinear systems. The limitation of estimated controller parameters to assume large values eliminates the possibility of high gain control [^Sastry] as high gain or high speed control can increase instability due to the high bandwidth that the controller gets subjected to. Therefore, people focused on the development of robust adaptive control systems, where closed-loop stability properties were guaranteed not just in the presence of large parametric uncertainty, but also in the presence of modeling errors that involved **additive disturbances** and **unmodeled dynamics**.  Even then, these methods made assumptions about the nature of the uncertainties in such systems by assuming the bound on the uncertainty was known aforetime. However, the bounds on the allowable dynamic uncertainties cannot be calculated as easily as in the nonadaptive case because of the nonlinear nature of the adaptive system coupled with the fact that the plant parameters are deemed unknown.

Techniques such as backstepping and parameter-tuning functions appeared in literature in the '90s for Lyapunov stability and estimation schemes (mostly from Prof. Kokotovic's group, [^Kokotovic1] <sup>&</sup> [^Kokotovic2]) and they proved to be quite good control design strategies. However, these studies assumed nonlinearities that were known ahead of time -- assumptions that make adaptive control very difficult to implement in the real world. Nonlinear techniques based on Lyapunov analysis and passivity arguments plus linear systems theory were used in establishing the stability/robustness margins that are not so easy to compute as in the LTI case.

> Techniques such as backstepping and parameter-tuning functions appeared in literature in the '90s (mostly from Prof. Kokotovic's group, [^Kokotovic1] <sup>&</sup> [^Kokotovic2]) for Lyapunov stability and estimation schemes and they proved to be quite good control design strategies.

In the linear time-varying case, stability margins, bandwidth margins, bandwidth, frequency domain characteristics, poles, zeros do not make much sense even for time-varying parameters unless approximations are made using the assumption of slowly varying parameters, etc (See [^Bellman]'s Applied Dynamic Programing Book esp. chapter on numerical approximations and why calculus of variations is not sufficient for real-world problems).

<a name="nonlinear"></a>
### Nonlinear neuro-control

In nonlinear systems, it is not only the parameters that are nonlinear (e.g. simple Riemann integral functionals), but also the functions that enter through the arguments of the right hand side of an ode (_the so-called problem of Bolza[^1] or the problem of Mayer [^2], which are both special cases of the Riemann-Stieltjes integral [^3] readily come to mind_ ).  Adaptive control was designed to stabilize system parameters by adapting for nonlinear _parameters_  and **NOT** nonlinear functions. The extension of adaptive controllers to nonlinear systems from LTI and LTV systems is therefore a complicated one. There are two general cases of adopting adaptive control to nonlinear systems:

+ nonlinear systems whose nonlinear functions are known but unknown parameters appear linearly.
  - easy: check! Techniques from feedback linearization, backstepping and such are good for such approaches

+ the nonlinear functions are assumed known by multiplying nonlinear basis functions with unknown parameters to be determined.
  - welcome to control theory!

This second option falls under categories where the basis functions are typically deduced from **function approximation** parameters (or weights as they are called these days) and they are assumed to appear linear-in-the-parameters of the nonlinear system. This linear-in-the-parameters property is fundamental for developing analytical stability results with large regions of attraction.

However, most nonlinear systems do not have such linear-in-the-parameters structure. Therefore approximation techniques such as these simplified ones call for a greater application of the mind. Over the last several years, neural networks have developed as an approximation technique for unknown nonlinearities. Although from a mathematical control standpoint, the neural networks are just one subset of many class of function approximators that have been used in controlling nonlinear processes. Other approximators include polynomial functions, radial basis functions, spline functions, and fuzzy logic systems (as a side note, the Sendai railway system in Japan is controlled by fuzzy set membership rules and its [efficiency](http://skisko.blogspot.com/2005/06/fuzzy-logic-and-its-practical-use-in.html) has been said to be comparable to that of the blue railway line in the Los Angeles metro system).

It is 2018 and it is certainly no doubt that neural networks have found much use in controlling very uncertain, nonlinear, and complex systems. If you are in a foreign country and you find yourself using google translate, there is a decent chance that a giant composite neural network in the backend is doing the heavy-lifting for you. So also in image recognition and music composition among others neural networks have solved problems that were once thought impossible due to the great computational resources required. The question is how can we harness the role of neural networks in control of large processes and still guarantee stability as opposed to say, dumb reinforcement learning (which basically optimizes an index of performance without regard to stability)?

<!-- ### The case for numerically-stable neuro-adaptve control -->

To paraphrase the legendary Karl Astrom, "adaptive systems have witnessed the formalization of methods" for designing control and automation algorithms in linear and mildly nonlinear systems. There are, however, pertinent nonlinear problems that adaptive systems have not solved. More so, there are quite a few restrictive assumptions on the network reconstruction error that may mitigate the efficacy of an effective neuro-controller such as (i) the inadequacy of the online approximator to exactly match an uncertain nonlinear function despite the selection of optimal weights (i.e. the so-called ideal matching conditions are not satisfied).

<a name="brouhaha"></a>
#### Adaptive Neuro-Control: The Reconstruction Error Brouhaha

To illustrate the way the reconstruction error can make the life of a control designer really miserable,  I shall be borrowing the example from [^Polycarpou]<sup>'s</sup> IEEE TAC 1996 paper on "Stable Adaptive Neural Control Scheme for Nonlinear Systems".

Suppose that we have a second-order system,

\begin{align}
  \dot{x\_1} &= x\_2 + f^\star(x\_1) \quad \nonumber \newline
  \dot{x\_2} & = u
  \label{eq:second_order_ode}
\end{align}

where \\(f^\star\\) is an unknown smooth function. We seek to drive the system output \\(y = x\_1 \\) to a small neighborhood of the origin. Without loss of generality, we shall denote the estimate of the smooth function \\(f\\) as

\begin{align}
  f^\star(x\_1) = f(x\_1) + \phi(x\_1)
\end{align}

where \\(\phi\\) is an unknown  function denoting the system uncertainty (could also be modeling errors). We will be turning off the adaptation in our neural network by requiring the neural network to approximate the unknown uncertainty \\(\phi(x\_1)\\) rather than the overall dynamic system \\(f\\). We thus end up with a nominal controller which, for example, could be a linear approximation of \\(f(x\_1)\\) for linear control methods.

Let us consider the online approximation of \\(\phi\\) by linearly parameterized radial basis functions with fixed centers and widths. It follows that we can rewrite \eqref{eq:second_order_ode} as

\begin{align}
  \dot{x\_1} = x\_2 + f(x\_1) + \theta^{\star^T} \zeta(x\_1) + \delta(x\_1)
\end{align}

where \\(\zeta: \mathbb{R}\rightarrow \mathbb{R}^n\\) is a known vector of smooth basis functions, \\(\theta^\star \in \mathbb{R}^n\\) is an unknown weight vector which is chosen to represent \\(\theta\\) such that it minimizes \\(\delta(x\_1)\\) for all \\(x\_1 \in \Omega\\), where \\(\Omega \subset \mathbb{R}\\) is a compact region, i.e.,

\begin{align}
  \theta^\star := \arg \min \{\sup_{x\_1 \in \Omega} | \phi(x\_1) - \theta^T \zeta(x\_1)|\};
\end{align}

\\(\delta\\) denotes the network reconstruction error, which we will interpret as

\begin{align}
  \delta(x\_1) = \phi(x\_1) - \theta^{\star^T} \zeta(x\_1).
\end{align}

The network reconstruction error is very crucial in representing the _minimum possible deviation_ from the unknown function \\(\phi\\) and the I/O of the function approximator. Generally, by the _universal approximation theorem for neural networks[^Funahashi]_, one can make \\(\delta\\) arbitrarily small on a compact set by making the number of parameters (or weights) i.e. \\(n\\) really large.


+ Assumption I: On the compact region \\(\Omega \subset R\\), \begin{align}
\|\delta(x\_1)\| \le \psi^\star \quad \forall \, x\_1 \in \Omega,
\label{eq:error_bound}
\end{align}

 where \\(\psi^\star \ge 0\\) is an unknown bound.

What becomes clear from \eqref{eq:error_bound} is that \\(\psi^\star\\) is not unique owing to any \\(\bar{\psi}^\star > \psi^\star \\). So let us define \\(\psi^\star\\) to be the smallest (nonnegative) constant such that \eqref{eq:error_bound} is satisfied.

We will be showing _semi-global_ stability for the system in \eqref{eq:second_order_ode} in the next subsection for values of \\(x\_1(t) \in \Omega \\) where the the set \\(\Omega\\) and bounding parameter \\(\psi^\star\\) can be arbitrarily large. When \\(x\_1\\) in \eqref{eq:error_bound} holds for all values in the real space, we have _global stability_.

#### Proof of semi-global stability

This section is not too important if you do not care for proofs but it will help in forming the conclusions we will be making in the next subsection.

We could change coordinates as follows:

\begin{align}
  z\_1 &= x\_1  \nonumber \newline
  z\_2 &= x\_2  - \alpha (x\_1, \theta, \psi),
  \label{eq:diff_eq}
\end{align}

where, \\(\alpha (x\_1, \theta, \psi) = -x\_1 - f(x\_1) - \theta^T \zeta(x\_1) - \beta\_1(x\_1, \psi)\\), and \\(\beta\_1(\cdot)\\) is a functional to be shortly defined; suppose further that we set the weighting estimation error and the _adaptive bounding parameter_ error as \\(\tilde{\theta} = \theta - \theta^\star\\), and \\(\tilde{\psi} = \psi - \psi\_m^\star\\) respectively, where \\({\psi\_m}^\star := \text{ max } \, \{ [\psi^\star, \psi^0] \}\\) such that \\(\psi^0 \ge 0 \\), then we can then define a lyapunov function as follows:

\begin{align}
  V = \frac{1}{2}(z\_1^2 + z\_2^2 + \tilde{\theta}^T \Gamma^{-1} \tilde{\theta} + \gamma^{-1}\tilde{\psi}^2),
\end{align}

where \\(\Gamma\\) is a (symmetric) positive definite matrix -- the adaptation gain for the vector \\(\theta\\), and \\(\gamma > 0\\) is the adaptation gain for the basis functions \\(\psi\\). We find that the time derivative of the lyapunov function satisfies,

\begin{align}
  \dot{V} = z\_1 \dot{z}\_1 + z\_2 \dot{z}\_2 + \tilde{\theta}^T \Gamma^{-1} \dot{\theta} + \gamma^{-1}\tilde{\psi}\dot{\psi}
\end{align}

so that

\begin{align}
  \dot{V} &= z\_1 \dot{x}\_1 + z\_2 \left(\dot{x}\_2 - \frac{\partial \alpha}{\partial x\_1} \dot{x\_1} - \frac{\partial \alpha}{\partial \theta}\dot{\theta} - \frac{\partial \alpha}{\partial \psi}\dot{\psi} \right) + \tilde{\theta}^T \Gamma^{-1} \dot{\theta} + \gamma^{-1}\tilde{\psi}\dot{\psi} \newline
          %
          &:= z\_1 \left(x\_2 + f(x\_1) + {\theta^\star}^T \zeta(x\_1) + \delta(x\_1) \right) +
              z\_2 \left(u - \frac{\partial \alpha}{\partial x\_1} \dot{x\_1} - \frac{\partial \alpha}{\partial \theta}\dot{\theta} - \frac{\partial \alpha}{\partial \psi}\dot{\psi} \right) \nonumber \newline
              & + \qquad \qquad \tilde{\theta}^T \Gamma^{-1} \dot{\theta} + \gamma^{-1}\tilde{\psi}\dot{\psi}
\end{align}

Abusing notation and dropping the templated arguments, we find that,

\begin{align}
  \dot{V} = z\_1 \left(z\_2 + \alpha + f + {\theta^\star}^T\zeta + \delta \right) +
             & z\_2 \left[u - \frac{\partial \alpha}{\partial x\_1}  (x\_2 + f + {\theta^\star}^T\zeta + \delta ) - \frac{\partial \alpha}{\partial \theta}\dot{\theta} - \frac{\partial \alpha}{\partial \psi}\dot{\psi}  \right] \nonumber \newline
             & + \tilde{\theta}^T \Gamma^{-1} \dot{\theta} + \gamma^{-1}\tilde{\psi}\dot{\psi}
\end{align}

which translates to

\begin{align}
  \dot{V} &= z\_1 z\_2 + z\_1\left(-z\_1 - f - \theta^T\zeta + f + {\theta^\star}^T\zeta + \delta\right)  +
              \nonumber \newline
             & \qquad z\_2 \left[u - \frac{\partial \alpha}{\partial x\_1}  (z\_2 + \alpha + f + {\theta^\star}^T\zeta + \delta ) - \frac{\partial \alpha}{\partial \theta}\dot{\theta} - \frac{\partial \alpha}{\partial \psi}\dot{\psi}  \right] + \nonumber \newline
            & \qquad  \tilde{\theta}^T \Gamma^{-1} \dot{\theta} + \gamma^{-1}\tilde{\psi}\dot{\psi} \label{eq:lyap_inter} \newline
            %
            &:= {z\_1}^2 + z\_1 z\_2 + z\_2\left[u - \frac{\partial \alpha}{\partial x\_1}  (z\_2 - z\_1 - \hat{\theta}^T \zeta - \beta\_1 + \delta ) - \frac{\partial \alpha}{\partial \theta}\dot{\theta} - \frac{\partial \alpha}{\partial \psi}\dot{\psi}  \right]  + \nonumber \newline
           & \qquad  \tilde{\theta}^T \Gamma^{-1} \dot{\theta} + \gamma^{-1}\tilde{\psi}\dot{\psi} \nonumber \newline
\end{align}

which is a result of substituting the expression for \\(\alpha\\) in \eqref{eq:lyap_inter}. Therefore,

\begin{align}
\dot{V} &= {z\_1}^2 + z\_1 z\_2 + z\_2\left[u - \frac{\partial \alpha}{\partial x\_1}  (z\_2 - z\_1 -  \beta\_1 + \delta ) - \frac{\partial \alpha}{\partial \theta}\dot{\theta} - \frac{\partial \alpha}{\partial \psi}\dot{\psi}  \right]  + \nonumber \newline
& \qquad  \tilde{\theta}^T \Gamma^{-1} \left[\dot{\theta} - \Gamma \zeta z\_1 - \Gamma \zeta z\_2  \frac{\partial \alpha}{\partial x\_1}  \right] - z\_1 \left(\beta\_1\- \delta \right) + \gamma^{-1}\tilde{\psi}\dot{\psi} \newline
%
      &:= {z\_1}^2 + z\_1 z\_2 + z\_2\left[u - \frac{\partial \alpha}{\partial x\_1}  (x\_2 + f  + \theta^T \zeta + \delta ) - \frac{\partial \alpha}{\partial \theta}\dot{\theta} - \frac{\partial \alpha}{\partial \psi}\dot{\psi}  \right]  + \nonumber \newline
      & \qquad  \tilde{\theta}^T \Gamma^{-1} \left[\dot{\theta} - \Gamma \zeta (z\_1 - z\_2  \frac{\partial \alpha}{\partial x\_1})  \right] - z\_1 \left(\beta\_1\- \delta \right) + \gamma^{-1}\tilde{\psi}\dot{\psi} \newline
      %
      &:= {z\_1}^2 + z\_1 z\_2 + z\_2\left[u - \frac{\partial \alpha}{\partial x\_1}  (x\_2 + f  + \theta^T \zeta + \delta ) - \frac{\partial \alpha}{\partial \theta}\dot{\theta} - \frac{\partial \alpha}{\partial \psi}\dot{\psi}  \right]  + \nonumber \newline
      & \qquad  \tilde{\theta}^T \Gamma^{-1} \left[\dot{\theta} - \Gamma \zeta (z\_1 - z\_2  \frac{\partial \alpha}{\partial x\_1})  \right] - z\_1 \left(\beta\_1\- \delta \right) + \gamma^{-1}\tilde{\psi}\dot{\psi}
\end{align}

Finally,

\begin{align}
  \dot{V} &= {z\_1}^2 + z\_1 z\_2 + z\_2\left[u - \frac{\partial \alpha}{\partial x\_1}  (x\_2 + f  + \theta^T \zeta ) - \frac{\partial \alpha}{\partial \theta}\dot{\theta} - \frac{\partial \alpha}{\partial \psi}\dot{\psi}  \right]  + \nonumber \newline
  & \qquad  \tilde{\theta}^T \Gamma^{-1} \left[\dot{\theta} - \Gamma \zeta (z\_1 - z\_2  \frac{\partial \alpha}{\partial x\_1})  \right] - \frac{\partial \alpha}{\partial x\_1}  \delta - z\_1 \left(\beta\_1\- \delta \right) + \gamma^{-1}\tilde{\psi}\dot{\psi}
  \label{eq:lyap_final}
\end{align}

Equation \eqref{eq:lyap_final} is pivotal since it will help us prove the stability of the neuro-adaptive system under consideration. We would want all terms in that equation to be negative along the trajectories of the solution to \eqref{eq:diff_eq}.

>Equation \eqref{eq:lyap_final} is pivotal since it will help us prove the stability of the neuro-adaptive system under consideration. We would want all terms in that equation to be negative along the trajectories of the solution to \eqref{eq:diff_eq}.

If we select the following control law,

\begin{align}
  u &= -z\_1 - z\_2 + \frac{\partial \alpha}{\partial x\_1}  (x\_2 + f  + \theta^T \zeta ) + \frac{\partial \alpha}{\partial \theta}\dot{\theta} + \frac{\partial \alpha}{\partial \psi}\dot{\psi} - \beta\_2(x\_1, x\_2, \theta, \psi),
\end{align}

where \\(\beta\_2(x\_1, x\_2, \theta, \psi)\\) is some function that is to be later on defined, then it follows that
the time derivative of the Lyapunov function becomes,

\begin{align}
  \dot{V} &= -{z\_1}^2 - {z\_2}^2 +  \tilde{\theta}^T \Gamma^{-1} \left[\dot{\theta} - \Gamma \zeta (z\_1 - z\_2  \frac{\partial \alpha}{\partial x\_1})  \right] + \Lambda
  \label{eq:lyap_lambda}
\end{align}

with \\(\Lambda\\) denoting,

\begin{align}
  \Lambda(x\_1, x\_2, \theta, \psi) = - z\_1(\beta\_1 - \delta) - z\_2(\beta\_2 + \frac{\partial \alpha}{\partial x\_1} \delta) + \gamma^{-1}\tilde{\psi}\dot{\psi}
\end{align}

Lyapunov stability requires the time derivative of \\(V(\cdot)\\) to be negative definite outside of the origin. By a close examination of \eqref{eq:lyap_lambda}, we see that save the last two terms, \\(\dot{V}\\) is already \\(< 0 \\) when \\(z\_{1,2} \neq 0\\). To knock out the third term, we'll set the adaptation update law for \\(\theta\\) as,

\begin{align}
  \dot{\theta} = \Gamma \zeta (z\_1 - z\_2  \frac{\partial \alpha}{\partial x\_1}).
\end{align}

Furthermore, to prevent parameter drift of the network parameters, we'll add the standard \\(\sigma\\)-modification leakage term to the equation in the foregoing as follows:

\begin{align}
  \dot{\theta} = \Gamma \zeta \left[z\_1 - z\_2  \frac{\partial \alpha}{\partial x\_1} - \sigma (\theta - \theta^0)\right],
\end{align}

where \\(\sigma > 0\\) and \\(\theta^0\\) are constants to be chosen by the user. We can then define the adaptation law for \\(\psi\\) in terms of \\(\beta\_1, \beta\_2\\) like so,

\begin{align}
  \beta\_1 &= \psi \omega\_1 \nonumber \newline
  \beta\_2 &= \psi \omega\_2
\end{align}

where for a small positive constant \\(\epsilon\\), we have that

\begin{align}
  \omega\_1 (x\_1) &= \text{tanh}(\frac{z\_1}{\epsilon}) \nonumber \newline
  \omega\_2 (x\_1, x\_2, \theta, \psi) &= p \, \text{tanh}(\frac{z\_2 \, p}{\epsilon}) \nonumber \newline
  p(x\_1, x\_2, \psi) &= |\dfrac{\partial \alpha}{\partial x\_1}|.
\end{align}

We will introduce the inequality \\( \underline{\psi}\_m^\star \le \delta \le \bar{\psi}\_m^\star \\) so that

\begin{align}
  \Lambda &= -z\_1 \psi \omega\_1 + z\_1 \delta - z\_2 \psi \omega - z\_2 \frac{\partial \alpha}{\partial x\_1}\delta + \gamma^{-1} \tilde{\psi}\dot{\psi} \nonumber \newline
  & \le -z\_1(\tilde{\psi} + \psi\_m^\star) \omega\_1 + |z\_1| \psi\_m^\star - z\_2(\tilde{\psi} + \psi\_m^\star) \omega\_2 + |z\_2| p \psi\_m^\star + \psi^{-1} \tilde{\psi} \dot{\psi}.
  \label{eq:lambda}
\end{align}

Sorting \eqref{eq:lambda}, we find that

\begin{align}
  \Lambda \le \psi\_m^\star(|z\_1| - z\_1\omega\_1) + \psi\_m^\star(|pz\_2| - z\_2\omega\_2) + \gamma^{-1}\tilde{\psi}[\dot{\psi} - \gamma(z\_1\omega\_1 + z\_2 \omega\_2)].
\end{align}


**This section is currently under development. Please check back in a few days**

#### The case for stable adaptive large-scale neuro-control

<!-- For severe nonlinearities (e.g. systems that possess sub-harmonics and cascades to chaos [^Billings]), the uncertainties and unknowns are unknown nonlinear functions coupled with parameters that appear nonlinear-in-the-parameters of a system [^Ioannou-tut]. Existing adaptive system methods cannot be applied to these problems due to the lack of universal eigenfunctions or Lyapunov exponents [^Ogunfunmi].

Current approaches for solving unknown system nonlinearities  resort to linear approximations about nominal trajectories so as to obtain locally stable solutions [^Lavretsky]. Mildly nonlinear system harmonics are treated with Volterra kernels and wavelet analyses. However, linear approximations about nominal local  trajectories provide no global stabilizing control law guarantees. And Volterra kernels fail in systems with nonlinear sub-harmonics. A crucial component of these methods are that they assume a structure about the underlying nonlinearity. Therefore, we still rely on linearized nominal approximations  when we attempt to control complex dynamical systems such as aircrafts, chemical plants and oil and gas manufacturing processes etc [3].

 In order to advance the state-of-the-art, and extend our solutions to challenging problems such as natural language processing, dynamic computer vision segmentation, consistent and safe  autonomous driving, efficient distributed automation and manufacturing processes, and climate prediction, we must solve the nonlinear problem and device intelligent adaptive controllers. 

The most successful severely nonlinear model estimators of today are deep learning models, often trained with back-propagation. Given the intractability of the solvability of nonlinear control problems (e.g. with the Hamilton-Jacobi-Bellman equation for \\(n>3\\), for an \\(n\\)-dimensional state), deep networks have found use as efficient function approximators that compactly parameterize high-dimensional control laws(e.g. in deep reinforcement learning). However, these deep neuro-estimators and neuro-controllers lack formal robustness and stability guarantees. These methods have the following drawbacks, namely:

+ they place an emphasis on depth (hence their capacity for large memory consumption) rather than sparsity, making them over-parameterized systems, that are very sensitive to noise and disturbance;  

+  being black boxes, they lack stabilizing guarantees in trained policies so that trained deep neuro-controllers are often unstable and exhibit brittleness in the real-world [^Ogunmolu]

+ they place an overwhelming emphasis on memorization of static dataset  as opposed to adaptability and analyzability as new data samples become available;

+  so far, neuro-adaptive control methods that guarantee Lyapunov stability have not been applied to the class of problems where the curse-of-dimensionality is a challenge[7].  

### My neuro-adaptive journey

Therefore, to achieve adaptive systems' original goals, we must revisit these persisting problems and devise sparse, adaptive neuro-estimators, and neuro-control laws.

I focus on the approximation properties of deep networks for representing complex systems. I also research the Lyapunov stability and synthesis of complex nonlinear control problems. My goal is to find solutions that assure optimality, guarantee robustness and stability for complex autonomous behaviors. Leveraging on information theory and learning-based approaches, I research difficult to automate large-scale autonomous control problems. I approach this problem in strides. Currently, in my PhD research, I study these nonlinearities in automating patient motion correction during clinical radiotherapy.

### Efforts in crossing the Rubicon

For completeness' sake, I am attaching the full slides of my recent talk on this subject here. These slides deal with understanding the the role of neural networks in adaptive control theory. It is based on a talk Nick gave at Google Robotics last year as well as my talk at PFN this year. It does more justice to the subject than I could ever rewrite in markdown :). Enjoy and feel free to ask questions in the comments section!

[Soft-Neuro-Adapt](/assets/presentations/google.pdf)
-->

### References

[^Ioannou-tut]: Ioannou, P., & Fidan, B. (2006). Adaptive control tutorial. Society for Industrial and Applied Mathematics, 2006

[^Billings]: Billings, S. Nonlinear system identification. NARMAX methods in the Time, Frequency, and Spatio-Temporal Domains. John Wiley & Sons Ltd. 2013.

[^Lavretsky]: Lavretsky, E. & Wise, K. Robust Adaptive Control. With Aerospace Applications. Springer 2005.

[^Ogunmolu]: Ogunmolu, O., Gans, N., & Summers, T. (2017). Robust Zero-Sum Deep Reinforcement Learning. arXiv preprint:1710.00491.

[^Ogunmolu-SNA]: Ogunmolu, O., Kulkarni, A., Tadesse, Y., Gu, X., Jiang, S., & Gans, N. Soft-NeuroAdapt: A 3-DOF Neuro-Adaptive Patient Pose Correction System For Frameless and Maskless Cancer Radiotherapy. In IEEE/RSJ International Conference on Robots and Systems. 2017.

[^Ogunfunmi]: Ogunfunmi, T. Adaptive Nonlinear System Identification. Springer. 2007

[^Bellman]: Bellman, R.E., Dreyfus, S.E. Applied Dynamic Programming, United States Air Force Project RAND. May 1962

[^1]: The problem of Bolza involves finding the extremum of a function of the end-point b, as in \\(J(y) = \int\_{a}^{b} g(z(x), y(x), x) dx + h(z(b), y(b), b)\\) with \\(x\\) and \\(y\\) subject to \\( \dfrac{dz}{dx} = H(z, y, x), \qquad z(0) = c\_1 \\)

[^2]: The problem of Mayer in the calculus of variations attempts to find the extremum of a function of the end point \\(b\\), \\(J(y) = h(z(b), y(b), b) \\)

[^3]: The Riemann-Stieltjes integral is describable by \\(J(y) = \int\_{a}^{b} g(z(x), y(x), x) dG(x)\\)



[^Ioannou1]: Ioannou, P. A.  and Sun, J.  Robust Adaptive Control. Englewood Cliffs, NJ: Prentice-Hall, 1995.

[^Ioannou2]: Ioannou, P. A. and Datta, A.  “Robust adaptive control: A unified approach,” Proc. IEEE, vol. 79, no. 12, pp. 1736-1768, 1991.

[^Kokotovic1]: I. Kanellakopoulos, P. V. Kokotovic, and A. S. Morse, “Systematic design of adaptive controllers for feedback linearizable systems,” IEEE Trans. Automat. Contr., vol. 36, no. 11, pp. 1241-1253, 1991.

[^Kokotovic2]: M. Krstic and P. V. Kokotovic, “Adaptive nonlinear design with controller-identifier separation and swapping,” IEEE Trans. Automat. Contr., vol. 40, no. 3, pp. 426440, 1995.

[^Sastry]: Sastry, Shankar, and Marc Bodson. Adaptive control: stability, convergence and robustness. Courier Corporation, 2011.

[^Polycarpou]: [Polycarpou, M. M. (1996). Stable adaptive neural control scheme for nonlinear systems. IEEE Transactions on Automatic Control, 41(3), 447–451.](https://doi.org/10.1109/9.486648)

[^Funahashi]: Funahashi, Ken-Ichi (1989). On the approximate realization of continuous mappings by neural networks Neural Networks. Elsevier, 1989.
