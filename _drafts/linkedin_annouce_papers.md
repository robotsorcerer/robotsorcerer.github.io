

A few recent research updates: Over the past few months, I've been exploring a common theme across robotics, autonomous systems, and large-scale decision making:

**How do we make intelligent systems both scalable and certifiably safe?**

🔹 **HJ-Gauss**

Classical Hamilton–Jacobi (HJ) safety verification is one of the most powerful tools we have for computing safety envelopes and backward reachable sets. Unfortunately, traditional grid-based solvers suffer from the curse of dimensionality.

In our latest work, we show that a viscous form of the HJ equation admits a generalized Cole–Hopf-type transformation that converts nonlinear safety verification into a quasilinear Gaussian heat-kernel for inference. The result is a scalable Monte Carlo framework with provable convergence and concentration guarantees.

In short: we trade combinatorial grid explosion in TVD-Runge-Kutta schemes for controllable sampling. The price we pay is the resolution of the BRT and the number of samples required for a good target set/tube.

This opens the door to safety verification in settings that were previously computationally out of reach, including large-scale multi-agent systems and autonomous robot fleets.

Paper: https://scriptedonachip.com/downloads/Papers/hjgauss.pdf; Code: https://github.com/robotsorcerer/levelsetpy/tree/monte_carlo

__Collaboration with colleagues at Cranfield and Seoul National Univerity__

🔹 **RoboDiff: A Regression Scheme for Robust Diffusion Policies**

Diffusion policies have transformed robot policy learning, but most current approaches remain fundamentally finite-dimensionali (FD). FD diiffusion discretizes the data before applying the diffusion algorithm. Seeing that the underlying diffusion process is infinite-dimensional, is it any wonder that this discretize-data-before-diffusion scheme misaligns policies from the physical phenomena they seek to control? FD Diffusion are essentially trained on grid artifacts; grid resolution seeds interpolation errors; errors compound across sampling rollouts. Hence, long-horizon planning become wacky.  

This work extends diffusion-based decision making into the Cameron-Martin (function) space, leveraging the backward Kolmogorov PDE to replace stochastic score-matching with a determinisitic BVP. Standard DDPM in this infinite-dimensional framework admits three minimal changes to the deployment scheme: (i) colored noise in place of white corrupting noise in the forward OU process; (ii) score-matching replacement with a precision-weighted Cameron-Martin loss; and (iii) the introduction of a robustness Kolmogorov residual metric for inference-time sampling.

This framework provides principled uncertainty quantification, improved long-horizon planning behavior. We validate our hypothesis on certified decision-making for robot manipulation/control and lean manufacturing resource planning applications.

Paper: https://arxiv.org/abs/2606.18186

🔹 **Distributed Optimization over Games --- Applications to ER Workflows.**

I'm also excited that our work on distributed generalized Nash equilibrium seeking for trauma-resuscitation teams has been accepted to the IFAC World Congress.

Developed in collaboration with colleagues at Cornell Tech and grounded in clinical workflows at Weill Cornell Medicine, the framework studies decision-coordination among multidisciplinary medical/healthcare worker teams under uncertainty, resource constraints, and extreme time pressure.

This takes recent ideas from games over networks, optimization, and distributed control for applications far beyond physical autonomy.

The thread connecting all of these projects is simple:

**Building principled foundations for autonomy by unifying learning, control, optimization, and safety into scalable frameworks for real-world deployment systems.**

Papers and preprints:
📄 HJ-Gauss: https://scriptedonachip.com/downloads/Papers/hjgauss.pdf
📄 RoboDiff: https://scriptedonachip.com/downloads/Papers/robodiff.pdf
📄 IFAC 2026: https://scriptedonachip.com/downloads/Papers/IFAC26.pdf

#Robotics #AI #MachineLearning #ControlTheory #AutonomousSystems #SafetyCriticalAI #DiffusionModels #OperationsResearch #IndustrialAI
