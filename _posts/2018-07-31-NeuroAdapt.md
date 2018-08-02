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

### Intro

It's been more than a year since my last post. I am sorry. I blame the publish or perish academic mantra. Now that I've stocked up on a few more papers, I shall try to keep up to date elucidating topics that capture my imagination right here. Before we dive into the proper topic, allow me the opportunity to delve a little deeper into the role of neural networks in adaptive control theory.


### On adaptive systems

The motivation for adaptive control was from systems with changing parameters over time. As I understand it, adaptive control can deal with any size of parametric uncertainty, as well as dynamic uncertainties arising from neglected dynamics if correct robust algorithms are used. The bounds for the allowable dynamic uncertainites cannot be calculated as easily as in the nonadaptive case because of the nonlinear nature of the adaptive system coupled with the fact that the plant parameters are deemed unknown. Adaptive Control designed for LTI plants give rise to a closed-loop system that is nonlinear. As a result traditional methods of analyzing stability such as poles, zeros, gain and phase margins make little sense for system analysis. Nonlinear techniques based on Lyapunov analysis and passivity arguments plus linear systems theory can be used in establishing the stability/robustness and margins that are not so easy to compute as in the LTI case. LTI methods can be used in understanding the dynamics of robust modification laws to adaptive systems e.g. dynamic normalizing signal that limits the rate of adaptation to be finite and small relative to level of dynamic uncertainty. The limitation of estimated controller parameters to assume large values eliminates the possibility of high gain control. High gain or high speed control can increase instability due to high bandwidth that the controller is subjected to.

> LTI methods can be used in understanding the dynamics of robust modification laws to adaptive systems e.g. dynamic normalizing signal that limits the rate of adaptation to be finite and small relative to level of dynamic uncertainty.

### Some history

So you see, adaptive control is really complex to tune and get right. A bit of a background here. Adaptive control research was motivated in the '50s by the problem of designing autopilots whose parameters changed over a wide operating range in speeds and altitudes. Fixed-gain controllers could not solve the frequent parameter variations in such systems. Therefore, people developed gain scheduling techniques using auxiliary measurements of airspeed. With gain scheduling came rudimentary methods of adjusting the adaptation mechanism in model reference systems -- the idea was to develop a self-tuning controller that adapted for parameter variations in a closed-loop reference model scheme. Adjustment mechanisms developed included sensitivity rules such as the M.I.T. rule, which performed reasonably well under some conditions. Rudolf Kalman in 1958 rigorously analyzed the self-tuning controller and established the explicit identification of the controller parameters of a linear SISO plant so that these could be used to tune an optimal linear quadratic controller. In the 60's, Parks [1966], demonstrated use of Lyapunov analysis in establishing the stability and convergence of adaptive systems. Advances in system identification enhanced the way update laws were determined for model reference schemes. Stochastic control and dynamic programming (from the work of Bellman) coupled with Lyapunov stability placed a firm footing on proving convergence for adaptive control systems. The '70s era witnessed a resurgence in the complete proofs of stability for model reference adaptive schemes e.g. Lyapunov state space proofs from Narendra, Lin and Valavani, and Morse. In the discrete time deterministic and stochastic domains, stability proofs also appeared about this time. Then came Rohr's example whereby the assumptions of stability were found to be very sensitive to the presence of unmodeled dynamics (e.g. ignored high-frequency parasitic modes in order not to complicate controller design). Researchers started working on the robustness of adaptive schemes and their sensitivity to transient behaviors. The extension of adaptive control to linear time-varying parameters was a major obstacle until the '80s when basic robustness questions were answered. Tactics such as dead-zone modification, dynamic normalizing signal together with leakage or parameter projection were used to deal with a great deal of parameter variations. This class included slowly-varying parameters as well as infrequent jumps in parameter values. In several cases, the error from time-varying signals can be reduced through proper parameterizations of the time-varying plant model used in the control design. In the linear time-varying case, stability margins, bandwidth margins, bandwidth, frequency domain characteristics, poles, zeros do not make much sense even for time-varying parameters unless approximations are made using the assumption of slowly varying parameters, etc (See Bellman's Applied Dynamic Programing Book esp. chapter on numerical approximations and why calculus of variations is not sufficient for real-world problems).

### There is still ground to cover

Adaptive control applied to nonlinear systems is in its infancy. Why is this so?

> Adaptive control applied to nonlinear systems is in its infancy.

In nonlinear systems, it is not only the parameters that are nonlinear, but also the functions (Bellman has plenty to say about this).  Adaptive control was designed to stabilize system parameters by adapting for nonlinear parameters  and **NOT** nonlinear functions. The extension of adaptive controllers to nonlinear systems from LTI and LTV systems is therefore a complicated one. There are two general cases of adopting adaptive control to nonlinear systems:

+ nonlinear systems whose nonlinear functions are known but unknown parameters appear linearly.
  - Easy: check!

+ the nonlinear functions are assumed known by multiplying nonlinear basis functions with unknown parameters to be determined.
  - Complex: welcome to control theory!

This second option falls under categories where the basis functions are typically deduced from **neural networks** parameters (or weights as they are called these days) and they are assumed to appear linearly e.g. in a single layer network <strong>(so far, this is what has been analytically proven; correct me if I am wrong)</strong>. This property is fundamental for developing analytical stability results with large regions of attraction. In my opinion, analytical stability and the associated existence and uniqueness proofs are really elegant on paper but seldom lend themselves to much usefulness in the laboratory. Why? Most of the computers we use nowadays are only capable of arithmetic operations. Such analytical solutions that we prove oftentimes require integration and differentiation. On modern digital computers, we must therefore resolve such differentiations and integrations by means of approximations (e.g. finite differences or the trapezoidal rule, a la integration). We must occasionally roll up our sleeves and use our mathematical spades if we do not wish to suffer the usual atrophy of armchair philosophers, or so says R.E. Bellman.


### The case for numerically-stable large-scale adaptve control

To paraphrase the legendary Karl Astrom, "adaptive systems have witnessed the formalization of methods" for designing control and automation algorithms in linear and mildly nonlinear systems. There are pertinent nonlinear problems that adaptive systems have not solved.

<!-- Adaptive control was primarily invented for systems with changing dynamics. While stability and robustness guarantees for time-varying parameters in a system have been established using techniques such as dynamic normalizing signals, dead zone modification, and parameter projection [1], adaptive systems have not fully realized their original potential of providing control systems that adapt intelligently to the world's dynamics. -->

For severe nonlinearities (e.g. systems that possess sub-harmonics and cascades to chaos [2]), the uncertainties and unknowns are unknown nonlinear functions coupled with parameters that appear nonlinear-in-the-parameters of a system [1]. Existing adaptive system methods cannot be applied to these problems due to the lack of universal eigenfunctions or Lyapunov exponents [6].

Current approaches for solving unknown system nonlinearities  resort to linear approximations about nominal trajectories so as to obtain locally stable solutions [3]. Mildly nonlinear system harmonics are treated with Volterra kernels and wavelet analyses. However, linear approximations about nominal local  trajectories provide no global stabilizing control law guarantees. And Volterra kernels fail in systems with nonlinear sub-harmonics. A crucial component of these methods are that they assume a structure about the underlying nonlinearity. Therefore, we still rely on linearized nominal approximations  when we attempt to control complex dynamical systems such as aircrafts, chemical plants and oil and gas manufacturing processes etc [3].

<!-- In order to advance the state-of-the-art, and extend our solutions to challenging problems such as natural language processing, dynamic computer vision segmentation, consistent and safe  autonomous driving, efficient distributed automation and manufacturing processes, and climate prediction, we must solve the nonlinear problem and device intelligent adaptive controllers. -->

The most successful severely nonlinear model estimators of today are deep learning models, often trained with back-propagation. Given the intractability of the solvability of nonlinear control problems (e.g. with the Hamilton-Jacobi-Bellman equation), deep networks have found use as efficient function approximators that compactly parameterize high-dimensional control laws(e.g. in deep reinforcement learning). However, these deep neuro-estimators and neuro-controllers lack formal robustness and stability guarantees. These methods have the following drawbacks, namely:

+ they place an emphasis on depth (hence their capacity for large memory consumption) rather than sparsity, making them over-parameterized systems, that are very sensitive to noise and disturbance;  

+  being black boxes, they lack stabilizing guarantees in trained policies so that trained deep neuro-controllers are often unstable and exhibit brittleness in the real-world [4]

+ they place an overwhelming emphasis on memorization of static dataset  as opposed to adaptability and analyzability as new data samples become available;

+  so far, neuro-adaptive control methods that guarantee Lyapunov stability have not been applied to the class of problems where the curse-of-dimensionality is a challenge[7].  

### My neuro-adaptive journey

Therefore, to achieve adaptive systems' original goals, we must revisit these persisting problems and devise sparse, adaptive neuro-estimators, and neuro-control laws.

I focus on the approximation properties of deep networks for representing complex systems. I also research the Lyapunov stability and synthesis of complex nonlinear control problems. My goal is to find solutions that assure optimality, guarantee robustness and stability for complex autonomous behaviors. Leveraging on information theory and learning-based approaches, I research difficult to automate large-scale autonomous control problems. I approach this problem in strides. Currently, in my PhD research, I study these nonlinearities in automating patient motion correction during clinical radiotherapy.

<!-- My work has been published in robotics and automation society venues these past three years. -->

<!-- Recently, I rigorously expounded on the adaptability, robustness and compact representation of an unknown nonlinear system using deep recurrent networks$^5$. I extended techniques from classical Lyapunov synthesis of LTI model reference control systems to the nonlinear-in-the-parameters problem. The idea was to capture the nonlinear properties of a biomedical soft robot system and derive stabilizing control laws for their actuation via inverse Lyapunov theory. My approach, unique in its representational power, and novel in its stabilizing control law generation, won the NSF Doctoral Consortium award at the just concluded IROS 2017. I know that major progress is within my reach. I am applying to the ai residency program within google in order to continue exploring this problem. Google Brain and X have some of the brightest researchers in the field of learning based control and adaptive systems in the world. I am applying to these groups because of the opportunity to continue to harness my talent, exploring the challenges and open problems in the field, as I continue to make important contributions to science and technology. -->

<!-- Being a google ai residency fellow will equip me with more research freedom, as I build discipline expertise. Honing my research skills, my contributions to the research community will have greater impact. And gaining proficient discipline expertise, this will stimulate rapid progress in my research career path. My goal is to ultimately be in a research position where I can train future researchers that aspire to tackle the important technological problems of our time -- therefore improving the quality of the AI research ecosystem. -->

### Efforts in crossing the Rubicon

The neural network adaptive control part starts on the 11th slide.

For completeness' sake, I am attaching the full slides here. It does more justice to the subject than I could ever rewrite in markdown :). Enjoy and feel free to ask questions in the comments section!

### Teaser Slides

These slides deal with understanding the the role of neural networks in adaptive control theory. It is based on a talk Nick gave at Google Robotics last year.

[Soft-Neuro-Adapt](/assets/presentations/google.pdf)


### References

[1]. Ioannou, P., & Fidan, B. (2006). Adaptive control tutorial. Society for Industrial and Applied Mathematics, 2006

[2]. Billings, S. Nonlinear system identification. NARMAX methods in the Time, Frequency, and Spatio-Temporal Domains. John Wiley & Sons Ltd. 2013.

[3]. Lavretsky, E. & Wise, K. Robust Adaptive Control. With Aerospace Applications. Springer 2005.

[4]. Ogunmolu, O., Gans, N., & Summers, T. (2017).
Robust Zero-Sum Deep Reinforcement Learning. arXiv preprint:1710.00491.

[5]. Ogunmolu, O., Kulkarni, A., Tadesse, Y., Gu, X., Jiang, S., & Gans, N. Soft-NeuroAdapt: A 3-DOF Neuro-Adaptive Patient Pose Correction System For Frameless and Maskless Cancer Radiotherapy. In IEEE/RSJ International Conference on Robots and Systems. 2017.

[6]. Ogunfunmi, T. Adaptive Nonlinear System Identification. Springer. 2007

[7]. Bellman, R.E., Dreyfus, S.E. Applied Dynamic Programming, United States Air Force Project RAND. May 1962
