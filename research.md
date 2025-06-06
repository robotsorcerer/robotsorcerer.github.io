---
layout: page
---


<!-- <center> -->
<!-- <a href="#revs"><font size="4">Introduction / </font></a> -->
### Contents

<h4><a>A Research North Star</a></h4>
<a href="#expose"><font size="4"> Research Exposé / </font></a>
<a href="#incubate"><font size="4"> R&T Incubations  </font></a>
<br>
<h4><a>Automation, Physics, Algorithmics, and AI</a></h4>
<a href="#safety"><font size="4"> An S23R Agora / </font></a>
<a href="#explore"><font size="4"> Towards living and functional robots / </font></a>
<a href="#cumbersome"><font size="4"> Explorative Learning  </font></a>
<br>
<h4><a>Miscellaneous</a></h4>
<a href="#service"><font size="4"> Service / </font></a>
<a href="#mentor"><font size="4">Mentoring  / </font></a>
<a href="#teaching"><font size="4">Teaching  / </font></a>
<a href="#fdbks"><font size="4">Reports. </font></a>
<!-- </center> -->

<a name="expose"></a>
#### Research Exposé

The rise in computational power together with the pervasiveness of big data has created new computing modalities which has spurred an emergent digital economy, and has spawned new business value chains. Across these spates of recent developments, questions of resilience and reliability, safety and robustness, as well as the assured predictability of behavior in the (autonomous) systems that we design and build has become timely and crucial. Emergent autonomous AI systems must make decisions under imperfect circumstances based on environment information that is available from an array of perceptual inputs and their representation, reason through self-enumerated possible actions, and safely execute the ones that provide a meaningful state transition in the environment in which they act --- all the while guaranteeing safety, stability, and resilience under external disturbances. Broadly, one can think of autonomous AI systems along two general threads: (i) situated autonomy, such as an automated airline ticket reservation system that reserves and makes decisions based on provided input by an external agent; and (ii) embodied autonomy, that is agents with perceptual sensors and proprioceptive actuators that effect a physical environmental change upon interaction; an example in this latter category are physical robots that sense the world directly through contact, and react adaptively to effect a change in representation of their environment via feedback. In both situated and embodied autonomy, we expect algorithms to deliver performance specifications without a glitch as we automate away tasks that humans have traditionally performed for over a century. My core research exists at the intersection of three intertwined fields that encapsulate important questions surrounding situatedness and embodiments: **robotics**, **control theory**, and **machine learning**. Robotics is crucial for the automation of physical embodiments. Control theory offers the necessary scientific recipé that establishes strong robustness and resilient foundations in otherwise flimsy AI models and policies (encompassing situatedness and embodiments). And machine learning provides the relaxation to devise generalist algorithmics that transcend narrow applications to broad usage. Motivated by what is possible with hitherto unexplored and large-scale engineering feats across these three disciplines, my research seeks to deconstruct the challenges that modern technology presents viz., (i) combining the elegance of mathematical rigor in imbuing resilience and robustness into the little margins that exist in safety-critical embodiments; (ii) reasoning possible automation capabilities into existence through abstract sub-task modules among a hierarchy of systems components; this is guided by clear conceptual analyses baked in the tradition of classical scientific rigor; and (iii) leveraging bio-inspiration to build emergent agent-centric situated AI and functional embodied automation systems. As I plan and act, I will continue to collaborate with  various researchers with relevant expertise around the planet; this will foster new insights on solving difficult automation problems, and broaden our understanding of the problems that are relevant to our collective future. Stimulating rapid growth in our understanding of critical components to buiding resilient complex systems, we shall bring new inventions to a stable, safe, robust, resilient, and reliable (S23R) haven that fosters a neat co-existence with human beings in everyday living.

<a name="incubations"></a>
### Research and Technology Incubations: A North Star


To accelerate the turn-around time from research ideation to formalized incubation of products, we strive to realize these visions via systematic and strategic missions across teams and geographies within and without Microsoft. Our overarching aim is to connect diverse workstreams and efforts through cross-geographic community-building and cross-discipline collaborations that enable the smothering of conventions (when needed), mothering of inventions, and acceleration of lava-stage technologies into established technological impact. The threads under investigation are further described in what follows.

<a name="safe"></a>
#### Between Messrs Bellman and Isaacs: An Agora for S23R in Complex Systems.

The [cyberphysical interfaces](https://www.nsf.gov/funding/opportunities/cps-cyber-physical-systems) in the modern systems that we develop are growing ever more complex. The need to guarantee performance as envisioned by the systems architect in the face of uncertainty has become even ever more timely given the possible dangers of having nominally envisioned system performance faltering. To deploy modern systems in unstructured complex environments, modern software must process generated data at multiple levels of abstraction within reasonable time, and guarantee consistency in system performance in spite of the debiliating circumstances. To address this concern, we consider software architectures for the numerical analysis of the safety assurance of a system (ascertaining the freedom of a system from harm) in a _verification_ sense. By verification, we mean generating evidence that a system, or any its components satisfy all specified requirements and functional and allocated baselines. In tandem, we are evolving a sister thread that considers validation systems --- that is, providing certifiable evidence that system capabilities comply with an end-user's performance requirements and satisfy its intended operational environment's specifications. 

Our efforts in this space involve sustaining various angles-of-attack assault (learning and physics-based) on the Hamilton-Jacobi-Bellman and Hamilton-Jacobi-Isaacs equations in recommending and building S23R into modern AI and cntrol systems. 

**Relevant papers**
+  [Cole-Hopf nonconvex optimization for reachable sets on viscous Hamilton-Jacobi PDEs](/downloads/Papers/ProxSampReach.pdf), Lekan Molu. IEEE 64th Conference on Control and Decision. (Submitted)  March 2025.
+  [Hopf-Lax nonconvex optimization for reachable sets on non-viscous Hamilton-Jacobi PDEs](/downloads/Papers/ProxSampReachNonViscous.pdf), Lekan Molu. IEEE 64th Conference on Control and Decision. (Submitted) March 2025.
+  [Is the Bellman Equation Enough for Learning Control?](https://arxiv.org/abs/2503.02171) Haoxiang You, Lekan Molu, and Ian Abraham, Reinforcement Learning Theory Conference, 2025. (Submitted) March 2025.
+  A Generalized Nash Equilibrium Policy for Large Scale Multi-agent Systems, Lekan Molu. Proceedings of the National Academy of Sciences. May 2025.
+  [Verification-aided Learning Neural Network Barrier Functions with Termination Guarantees](https://arxiv.org/pdf/2403.07308.pdf), Shaoru Chen, Lekan Molu, and Mahyar Fazlyab. American Control Conference (ACC), Toronto, ON. May 2024.
+  [LevelSetPy: A GPU-Accelerated Package for Resolving Hyperbolic Hamilton-Jacobi Partial Differential Equations](https://dl.acm.org/journal/toms), Lekan Molu. ACM Transactions on Mathematical Software. April 2024.
+  [The Python LevelSet Toolbox (LevelSetPy)](downloads/Papers/levelsetpy_cdc.pdf), Lekan Molu. IEEE 63rd Conference on Decision and Control (CDC), Milano, Italia. December 2024.
+  [Mixed H2/H-Infinity Policy Learning Synthesis](/downloads/Papers/ifac.pdf). Lekan Molu. World Congress, International Federation of Automatic Control, Yokohama, Japan. July 2023.

<a name="explore"></a>
#### Learning to Explore in Unstructured Spaces

The emergence of powerful foundation models has improved the reasoning capability of many AI systems leading to their wide adoption in solving a variety of problems including question-answering and vision processing tasks. In embodied two-dimensional and three-dimensional (3D) vision-enabled planning and control systems (often within hazardous environments) however, wrong (model) predictions or mis-specified (vision-language) actions during tasks’ execution can lead to deleterious consequences (in money, time, health, or even lives). Disciplined modularity in physical and virtual embodied reasoning systems is one way to imbue stability, robustness, and safety into embodied decision-making systems. Such systems must be amenable to efficient optimization -- combining discrete high-level abstraction modules (for reliably predicting and delineating environmental structure) with continuous low-level decision-making modules (that inform stable and safe world exploration). This hierarchical planning scheme in successive combinations of discrete and continuous modules, informed by the power of large foundation models that encapsulate combinatorial optimization within large application-relevant datasets  will make them generalizable. This will inform robustness in agent-centric, environment-agnostic, decision-making, and guarantee safety during tasks’ executions via designed error-checking mechanisms.

Our efforts in this space leverage modularization for automatic geometry delineation of component objects within any generic three-dimensional world. This is followed by an efficient obstacle-free space computational supervised learning module that first decomposes every detected structural component into convex structures. An iterative semi-definite convex programming algorithm, in an incrementally building of the collision-free configuration space of the entire environment, then follows. Making fast optimal decisions is important in many engineering systems and virtual three-dimensional systems. A bottleneck to such optimal decisions is determining what areas of space to explore. By having an automated algorithm that determines what regions of the environment is worth exploring, the problem of optimal decision-making is significantly reduced to a subset of the entire C-space. This scheme twill help engineers and planners reduce time to explore, gather data, or reason about an environment before making decision.

**Connection to existing planning schemes**

+ Going beyond kinodynamical reasoning that is the mainstay of classical planning systems towards an ensemble of large models for abstract world models including objects segmentation, c-free computation, and low-level shortest path planning, minimum spanning tree problems,  and low-level control for hierarchical decision-making;
+ Connecting the output of the ensemble of eclectic models above to scaled network-based (combinatorial/convex) optimization framework that allows formulating decision-making at the intercept of high-level abstract reasoning about the world and low-level controller actions;
+ Incorporating safety-based controllers at this lower level for real-time, and modular decision-making. Building accessible and robust software systems that encapsulate this modular pipeline for general-purpose agents – physical (including robotics), virtual, mixed-reality, and simulated-reality alike.

**Relevant Papers:**

+ Mastering Collision-free computation via convex decomposition and neural networks. Lekan Molu. Nature. May 2025.
+ [PCLAST: Discovering Plannable Continuous Latent States](downloads/Papers/PCLAST.pdf), Anurag Koul, Shivakanth Sujit, Shaoru Chen, Ben Evans, Lili Wu, Lekan Molu, Byron Xu, Rajan Chari, Riashat Islam, Raihan Seraj, Yonathan Efroni, Miroslav Dudík, John Langford, Alex Lamb. International Conference on Learning Representations (ICLR). September 2023.
+ [Guaranteed discovery of controllable latent states with multi-step inverse models](https://arxiv.org/pdf/2207.08229.pdf). Alex Lamb, Riashat Islam, Yonathan Efroni, Aniket Didolkar, Dipendra Misra, Dylan Foster, Lekan Molu, Rajan Chari, Akshay Krishnamurthy, John Langford. Transactions in Machine Learning Research. December 2022.
+ [Interaction-Grounded Learning with Action-inclusive Feedback](https://arxiv.org/abs/2206.08364), Tengyang Xie, Akanksha Saran, Dylan J Foster, Lekan Molu, Ida Momennejad, Nan Jiang, Paul Mineiro, and John Langford.
Neural Information Processing Systems (Neurips). May 2022.

#### For the love of life: Can we have (functional) robots that behave like a living organism?


Most robot manipulator mechanisms that are largely used in academe and industry today emerged from the anthropomorphic design of Harry Asada at CMU in the early '80s. Designed to act the way humans do, they were built with rigid mechanical links that enforce dexterity and reasonably accurate manipulability. To avoid large hysteresis during repeated operations, they are manufactured to be sturdy, with parts made of rigid metals. This introduces hazards in human-robot environments. In addition, being a collection of rigid metals, adjoined by mostly rotary joints, they magnify errors from shoulder all the way out to the end effector, making precision intractable in precision automation. I can anticipate the question on the top of your mind: if modern robot manipulators were designed to behave like human arms, why has the community given up on making robots with improved stiffness-to-weight ratios, improved bending, and twisting capabilities, and manipulability beyond the geometric primitives that the workspace of rigid robots provide? Practically every AI stack built for robots nowadays is premised on the assumption that models and policies will evolve on the anthropomorphic kinematically redundant robot arm configuration. 

In the future, I envision pervasive robot configurations whose design is premised on the [embodied intelligence principle](https://www.iris.sssup.it/handle/11382/461975), informed by [morphological computation](https://philpapers.org/rec/HAUOAO) that is situated in many natural organisms. Natural organisms with embodied intelligence exploit their intrinsic morphological computation by integrating internal control computations with their structure for adaptive motion strategies. This embodied intelligence paradigm can inspire new design, modeling, and control paradigms in adaptive automation with soft robots. Soft robots yield more improved  stiffness-to-weight ratios and can offer better reactiveness and adaptiveness to movement strategies that otherwise rigid robots are not capable of. In this design philosophy, rather than reject external disturbances and physical constraints, continuum soft robots must harness external forces and physical constraints for improved stiffness-to-weight ratio, bending, torsion, and twisting capabilities etc -- behaviors unlike of rigid robots. 

My goal in this paradigm is to fully take advantage of these foundational embodied intelligence principles. Novel mechanism designs are emerging given recent advances in material engineering. Even so, new kinematics, kinetics, and control methods for continuum robots are emerging. This thread aims to erect a cantilever bridge from the theoretical foundations of embodied intelligence to (i) the harnessing of natural organisms’ morphology in soft robots’ configurations and mechanism design; (ii) the precise mathematical modeling tools  for predicting soft mechanisms behavior -- via ODE-based reduced-order finite dimensional control, and PDE-based modeling of continuum robots; and (iii) to the emerging control methods for managing model complexity via time-scale separation and layered control architectures. When all of this are laid out to a sufficient degree of exposition, my goal is to leverage the power of machine learning from sensory experimental data to model and control behavior seamly.

**Relevant papers:**

+ [On the number synthesis for deformable robots parameters identification](/downloads/Papers/SoRoIdent.pdf). Lekan Molu. IEEE 64th Conference on Control and Decision. March 2025.
+ [Fast Whole-Body Strain Regulation in Continuum Robots](Fast Whole-Body Strain Regulation in Continuum Robots). Lekan Molu. American Control Conference (ACC), Denver, CO. June 2025.
+ [Lagrangian Properties and Control of Soft Robots Modeled with Discrete Cosserat Rods](downloads/Papers/SoRoPD.pdf). Lekan Molu and Shaoru Chen. Conference on Decision and Control (CDC). March 2024.
+ [Mechanism and Model of a Soft Robot for Head Stabilization in Cancer Radiation Therapy](/downloads/Papers/ContinuumI.pdf). Olalekan Ogunmolu, Xinmin Liu, Nick Gans, and Rodney Wiersma. IEEE International Conference on Robotics and Automation (ICRA), Paris, France. May 2020.


<a name="serv"></a>
#### **Community Service**

I am an active member of the AI, control, and robotics research communities — regularly engaging in peer reviewing activities for [NeurIPS](https://nips.cc/), [International Federation of Automatic Control](https://www.ifac-control.org/) -- World Congress and Automatica alike, [Institute of Physics](https://www.iop.org/),  [ICML](https://icml.cc/), IEEE Access, [Conference on Decision and Control](https://2021.ieeecdc.org/), [IROS](https://en.wikipedia.org/wiki/International_Conference_on_Intelligent_Robots_and_Systems), [American Control Conference](https://acc2021.a2c2.org/),  ASME's [DSCC](https://event.asme.org/DSCC),  [ICRA](https://www.ieee-ras.org/conferences-workshops/fully-sponsored/icra), and [Neural Computing and Applications](https://www.springer.com/journal/521) among others.

I am an active member of the Control Systems Society, often serving as session chair at our leading conferences on the planet, that is Control and Decision Conference and the American Control Conference. In addition, I serve regularly as Associate Editor for IEEE Robotics' flagship conference -- International Conference on Robotics and Automation (ICRA). Since January 2020, I have been a judge for NatGeo's [AI for Species Discovery Grant Applications](https://www.nationalgeographic.org/funding-opportunities/grants/). 


<a name="teaching"></a>
#### [Old-ish] Teaching Keepsakes

~~I mostly teach a mixture of undergrad and graduate level classes in Robotics at Brandeis.~~

I have left Brandeis.

#### A Short Treatise on Robots' Kinematics and Kinetics.

+ Being a tutorial organized for my colleagues in the MSR NYC RL Group. June, 2022. 

+ [Course Resources]
	+ [Introduction and Kinematic Geometry](/downloads/Papers/robots_slides/intro_linkages.pdf)
		- Mechanics and Mechanisms, Pairs and Linkages, Serial, Parallel and Hyperredundant Robots
	+ [Mobility of Kinematic Structures](/downloads/Papers/robots_slides/mobility.pdf)
		- Freedoms, Constraints, The General (Relative) Mobility Criterion.
	+ [Rigid Body Motions in R^3](/downloads/Papers/robots_slides/rbm_euler.pdf)
		- Motions in R^3, Euler and Fick Angle Parameterizations; Axis/Angle Parameterizations, Composition of Rotations.
	+ [Rigid Body Motions with Screw Theory](/downloads/Papers/robots_slides/rbm_screws.pdf)
		- Screws: Displacement, Twists, Wrench. Group Theory Brief Intro. Connections of Screws with Rotations. The Exponential Map.


#### **RBOT250: The Mathematical Foundations of Robotics, Spring 2021.**

+ [Course Resource](/downloads/Papers/RBOT250.pdf)


#### **RBOT101: Robot Manipulation, Planning and Control, Spring 2020.**

+ [Course Resource](/downloads/Papers/RBOT101.pdf)

#### **EECS 4342: Introduction to Robotics, Fall 2016.**

This was a course I helped teach back in grad school to a mixture of Seniors and first-year ECE Masters students.The website I made in 2016 is highlighted below.

+ [Introduction to Robotics - EECS 5375](http://service-lab.github.io/)

+ [Lecture One](http://service-lab.github.io/Lecture-1/)


<a name="fdbks"></a>
#### **In the words of my students:**

_"Thank you again Lekan. [Taking RBOT 250 with you] was quite a journey. But I feel more confident now with ROS because I figured all of the ROS system. I'll be looking forward to see you run the class again."_

_"Dr. Molu is very caring about his students. I love how he makes time for me to run over course notes, point out helpful reading materials, and work through problems together with me. I enjoy the examples and exercises he tasks us with."_

_"I want to thank Lekan for teaching this course, I definitely learned a lot. I am interested in auditing it when Lekan runs it again."_