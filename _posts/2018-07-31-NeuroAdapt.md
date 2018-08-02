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

To paraphrase the legendary Karl Astrom, "adaptive systems have witnessed the formalization of methods" for designing control and automation algorithms in linear and mildly nonlinear systems. There are pertinent nonlinear problems that adaptive systems have not solved. Adaptive control was primarily invented for systems with changing dynamics. While stability and robustness guarantees for time-varying parameters in a system have been established using techniques such as dynamic normalizing signals, dead zone modification, and parameter projection [1], adaptive systems have not fully realized their original potential of providing control systems that adapt intelligently to the world's dynamics.

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


[1]. Ioannou, P., & Fidan, B. (2006). Adaptive control tutorial. Society for Industrial and Applied Mathematics, 2006

[2]. Billings, S. Nonlinear system identification. NARMAX methods in the Time, Frequency, and Spatio-Temporal Domains. John Wiley & Sons Ltd. 2013.

[3]. Lavretsky, E. & Wise, K. Robust Adaptive Control. With Aerospace Applications. Springer 2005.

[4]. Ogunmolu, O., Gans, N., & Summers, T. (2017).
Robust Zero-Sum Deep Reinforcement Learning. arXiv preprint:1710.00491.

[5]. Ogunmolu, O., Kulkarni, A., Tadesse, Y., Gu, X., Jiang, S., & Gans, N. Soft-NeuroAdapt: A 3-DOF Neuro-Adaptive Patient Pose Correction System For Frameless and Maskless Cancer Radiotherapy. In IEEE/RSJ International Conference on Robots and Systems. 2017.

[6]. Ogunfunmi, T. Adaptive Nonlinear System Identification. Springer. 2007

[7]. Bellman, R.E., Dreyfus, S.E. Applied Dynamic Programming, United States Air Force Project RAND. May 1962
