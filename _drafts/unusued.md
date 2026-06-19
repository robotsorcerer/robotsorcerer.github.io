<h4><i class="fa fa-chevron-right"></i><i class="fa fa-chevron-right"></i>Bio Snippet</h4> 
> No fluff research science and engineering only. 





A few recent research updates: Over the past few months, I've been exploring a common theme across robotics, autonomous systems, and large-scale decision making:

**How do we make intelligent systems both scalable and certifiably safe?**

🔹 **HJ-Gauss**

Classical Hamilton–Jacobi (HJ) safety verification is one of the most powerful tools we have for computing safety envelopes and backward reachable sets. Unfortunately, traditional grid-based solvers suffer badly from the curse of dimensionality.

In our latest work, we show that a viscous form of the HJ equation admits a generalized Cole–Hopf-type transformation that converts nonlinear safety verification into Gaussian heat-kernel inference. The result is a scalable Monte Carlo framework with provable convergence and concentration guarantees.

In short: we trade combinatorial grid explosion for controllable sampling.

This opens the door to safety verification in settings that were previously computationally out of reach, including large-scale multi-agent systems and autonomous robot fleets.

---  (Collaboration with colleagues at Cranfield and Seoul National Univerity)

🔹 **RoboDiff: A Regression Scheme for Robust Diffusion Policies**

Diffusion policies have transformed robot policy learning, but most current approaches remain fundamentally finite-dimensional.

RoboDiff extends diffusion-based decision making into function space, combining infinite-dimensional diffusion models with formal control verification. The framework provides principled uncertainty quantification, improved long-horizon planning behavior, and certified decision-making for production-control and supply-chain applications.

The broader goal is to move beyond policies that merely perform well empirically toward policies that can also provide verifiable guarantees.

🔹 **Distributed Optimization over Games --- Applications to ER Workflows.**

I'm also excited that our work on distributed generalized Nash equilibrium seeking for trauma-resuscitation teams has been accepted to the IFAC World Congress.

Developed in collaboration with researchers and clinicians at Weill Cornell Medicine, the framework studies how multidisciplinary medical teams can coordinate decisions under uncertainty, resource constraints, and extreme time pressure.

It's rewarding to see ideas from game theory, optimization, and distributed control finding applications far beyond traditional robotics.

The thread connecting all of these projects is simple:

---  (Collaboration with Cornell Tech colleagues, inspired by Weill Cornell Medicine ER Clinical Workflows)

**Building principled foundations for autonomy by unifying learning, control, optimization, and safety into scalable frameworks for real-world decision-making.**

Papers and preprints:
📄 HJ-Gauss: https://scriptedonachip.com/downloads/Papers/hjgauss.pdf
📄 RoboDiff: https://scriptedonachip.com/downloads/Papers/robodiff.pdf
📄 IFAC 2026: https://scriptedonachip.com/downloads/Papers/IFAC26.pdf

#Robotics #AI #MachineLearning #ControlTheory #AutonomousSystems #SafetyCriticalAI #DiffusionModels #OperationsResearch #IndustrialAI
