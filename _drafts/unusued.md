<h4><i class="fa fa-chevron-right"></i><i class="fa fa-chevron-right"></i>Bio Snippet</h4> 
> No fluff research science and engineering only. 





Over the past few months I've been chasing one theme across robotics, autonomous systems, and large-scale decision-making:

🔐 **How do we make intelligent systems both scalable and certifiably safe?**

🔹 **HJ-Gauss**

Classical Hamilton–Jacobi (HJ) safety verification is one of the most powerful tools for computing safety envelopes and backward reachable sets. Unfortunately, traditional grid-based solvers suffer from the curse of dimensionality.

In our latest work, we show that a viscous form of the HJ equation admits a generalized Cole–Hopf-type transformation that converts nonlinear HJ PDEs into a quasilinear Gaussian heat-kernel. The heat kernel informs a sampling-based algorithm for safe sets computation. The result is a scalable Monte Carlo framework with provable convergence and concentration guarantees, and a memory footprint that grows linearly — O(N·n) in samples and state dimension — instead of exploding as O(Mⁿ) on a grid.

In short: we trade combinatorial grid explosion in TVD-Runge-Kutta levelset schemes for controllable sampling in a Picard iterative scheme. The price we pay is accuracy — BRT resolution is now bounded by sample count rather than grid size.

The payoff is verification at a scale that was previously out of reach. As a stress test, we certify the safety of aerial **starling murmurations** of up to **100,000 birds** (*sturnus vulgaris*) under multi-predator (peregrine falcon) pursuit games — a 4-D, massively multi-agent problem no grid solver can hold in memory — and we do it on **commodity CPUs**. Adding birds is essentially free: the value function is computed once, then each agent is certified by a single forward evaluation. Better still, the certificate is not just a number: its reachable-set topology reads out *how* safety is won or lost — defensive **cordon formation and its collapse**, **flock fragmentation**, and **flash expansion** — straight from the geometry of the value function.

📄 Paper: https://arxiv.org/abs/2605.18566  💻 Code: https://github.com/robotsorcerer/levelsetpy/tree/monte_carlo

🤝 Collaborations: 🏛️ Cranfield & Seoul National University 🌐

🔹 **RoboDiff: A Regression Scheme for Robust Diffusion Policies**

Diffusion policies have transformed robot policy learning, but most current approaches remain fundamentally finite-dimensional (FD). FD diffusion discretizes the data before applying the diffusion algorithm. 
FD diffusion is essentially trained on grid artifacts; grid resolution seeds interpolation errors; errors compound across sampling rollouts. Hence, long-horizon planning breaks down. Seeing that the underlying diffusion process is infinite-dimensional, is it any wonder that this _discretize-data-before-diffusion_ scheme misaligns policies from the physical phenomena they seek to control?

This work extends diffusion-based decision making into the Cameron-Martin (function) space, leveraging the backward Kolmogorov PDE to replace stochastic score-matching with a deterministic BVP. Standard DDPM in this infinite-dimensional framework admits three minimal changes to the deployment scheme: (i) colored noise in place of white corrupting noise in the forward Ornstein-Uhlenbeck (OU) process; (ii) score-matching replacement with a precision-weighted Cameron-Martin loss; and (iii) the introduction of a robustness Kolmogorov residual metric for inference-time sampling.

This framework provides principled uncertainty quantification and improved long-horizon planning. We validate our hypothesis on certified decision-making for robot manipulation/control and lean manufacturing resource planning applications.

✍️ Solo Contribution

📄 Paper: https://arxiv.org/abs/2606.18186

🔹 **Distributed Optimization over Games — Applications to Trauma Resuscitation in ER Workflows.**

I'm also excited that our work on distributed generalized Nash equilibrium seeking for trauma-resuscitation teams has been accepted to the IFAC World Congress.

Developed in collaboration with colleagues at Cornell Tech 🏛️ and grounded in clinical workflows at Weill Cornell Medicine 🏛️, the framework studies decision-coordination among multidisciplinary medical/healthcare worker teams under uncertainty, resource constraints, and extreme time pressure.

This takes recent ideas from games over networks, optimization, and distributed control for applications far beyond physical autonomy.

🤝 Collaboration: 🏛️ Cornell Tech.

🧵 The thread connecting all of these projects is simple:

🧭 **Building principled foundations for autonomy by unifying learning, control, optimization, and safety into scalable frameworks for real-world deployment systems.**

Papers and preprints:
📄 HJ-Gauss: https://arxiv.org/abs/2605.18566
📄 RoboDiff: https://scriptedonachip.com/downloads/Papers/robodiff.pdf
📄 IFAC 2026: https://scriptedonachip.com/downloads/Papers/IFAC26.pdf

#Robotics #AI #MachineLearning #ControlTheory #AutonomousSystems #SafetyCriticalAI #DiffusionModels #OperationsResearch #IndustrialAI
