<h4><i class="fa fa-chevron-right"></i><i class="fa fa-chevron-right"></i>Bio Snippet</h4> 
> No fluff research science and engineering only. 





Over the past few months I've been chasing one theme across robotics, autonomous systems, and large-scale decision-making:

🔐 **How do we make intelligent systems both scalable and certifiably safe?**

🔹 **HJ-Gauss**

Classical Hamilton–Jacobi (HJ) safety verification is a powerful tool for computing safety envelopes from backward reachable sets/tubes. Unfortunately, traditional grid-based levelset solvers suffer from the curse of dimensionality.

In our latest work, we show that a viscous form of the HJ equation admits a generalized Cole–Hopf-type transformation that converts nonlinear HJ PDEs into a quasilinear Gaussian heat-kernel. The heat kernel informs a sampling-based algorithm for safe sets computation. The result is a scalable Monte Carlo framework with provable convergence and contraction guarantees, alongside a memory footprint that grows linearly — O(N·n), for n state dimensions and N samples — instead of exploding as O(Mⁿ) for M grid points.

Put differently: we trade combinatorial grid explosion in TVD-Runge-Kutta levelset schemes for controllable sampling in a Picard iterative scheme. The *price* we pay is the sampling count for a good BRT resolution. The *payoff* is verification at a scale that was previously out of reach. As a stress test, we certify the safety of aerial **starling murmurations** of up to **100,000 birds** (*sturnus vulgaris*) under multi-predator (peregrine falcon) pursuit games — a 4-D, massively multi-agent problem no grid solver can hold in memory — and we do it on **commodity CPUs**. Adding birds is essentially free: the value function is computed once, then each agent is certified by a single forward evaluation. Even better, the certificate is not just a number: its reachable-set topology reads out *how* safety is won or lost — defensive **cordon formation and its collapse**, **flock fragmentation**, and **flash expansion** — straight from the geometry of the value function.

📄 Paper: https://arxiv.org/abs/2605.18566  💻 Code: https://github.com/robotsorcerer/levelsetpy/tree/main/monte_carlo

✍️ Collaborations 🤝: 🏛️ Cranfield & Seoul National University 🌐

🔹 **A Regression Scheme for Robust Diffusion Policies**

**Why do diffusion policies become unreliable over long planning horizons?** One reason is that they discretize continuous physical phenomena before learning even begins. The resulting interpolation errors accumulate across rollouts, degrading long-horizon planning and control.

Rather than approximate diffusion over discretized state representations, we formulate diffusion directly in the Cameron–Martin function space. Using the backward Kolmogorov PDE, stochastic score matching is replaced with the solution of a deterministic boundary value problem (BVP). Standard DDPM in this infinite-dimensional framework requires only three minimal changes: (i) replacing white Gaussian noise in the forward Ornstein–Uhlenbeck (OU) process with colored noise; (ii) replacing score matching with a precision-weighted Cameron–Martin loss; and (iii) introducing a robustness Kolmogorov residual metric for inference-time sampling.

The resulting framework facilitates policy failure prognosis while improving long-horizon planning. We validate the framework on certified decision-making tasks in robot manipulation and control and lean manufacturing resource planning. Broadly, this work demonstrates that moving diffusion from finite-dimensional grids to function space yields a mathematically grounded framework for robust long-horizon planning and control.


📄 Paper: https://arxiv.org/abs/2606.18186 

🔹 **Distributed Optimization over Games — Applications to Trauma Resuscitation in ER Workflows.**

I'm also excited that our work on distributed generalized Nash equilibrium seeking for trauma-resuscitation teams has been accepted to the IFAC World Congress.

Developed in collaboration with colleagues at Cornell Tech 🏛️ and grounded in clinical workflows at Weill Cornell Medicine 🏛️, the framework studies decision-coordination among multidisciplinary medical/healthcare worker teams under uncertainty, resource constraints, and extreme time pressure.

This takes recent ideas from games over networks, optimization, and distributed control for applications far beyond physical autonomy.

✍️ Collaborations 🤝: 🏛️ AirLab @ Cornell Tech.

🧵 The thread connecting all of these projects is simple:

🧭 **Building principled foundations for autonomy by unifying learning, control, optimization, and safety into scalable frameworks for real-world deployment systems.**

Papers and preprints:
📄 HJ-Gauss: https://arxiv.org/abs/2605.18566
📄 RoboDiff: https://scriptedonachip.com/downloads/Papers/robodiff.pdf
📄 IFAC 2026: https://scriptedonachip.com/downloads/Papers/IFAC26.pdf

#Robotics #AI #MachineLearning #ControlTheory #AutonomousSystems #SafetyCriticalAI #DiffusionModels #OperationsResearch #IndustrialAI
