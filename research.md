---
layout: page
---


<center>
<!-- <a href="#revs"><font size="4">Introduction / </font></a> -->
<a href="#serv"><font size="4"> Service / </font></a>
<a href="#mentor"><font size="4">Mentoring /</font></a>
<a href="#teaching"><font size="4">Teaching / </font></a>
<a href="#fdbks"><font size="4">Reports. </font></a>
</center>


### Research and Technology Incubations: A North Star


To accelerate the turn-around time from research ideation to formalized incubation and production, we strive to realize these visions via systematic missions that connect diverse workstreams and teams through cross-geographic community-building. Our goal is to smother conventions (when needed) and accelerate the invention of new technologies.


##### Exposé (again!)

The rise in computational power together with the pervasiveness of big data has created new computing possibilities, technological innovations, and has spawned new business value chains including the evolving and emergent digital economy. Across these spates of development in modern society, the question of resilience and reliability, safety and robustness, as well as the assured predictability of behavior in the (autonomous) systems that we design and build has become timely and crucial. Emergent autonomous AI systems must make decisions with imperfect information, reason about the world through situated data (such as an automated airline ticket reservation system) and embodiment alike (such as a physical robot). In all these, we expect many automation systems to deliver without glitch as we automate away tasks that humans have traditionally done for over a century. My core research exists at the intersection of three intertwined fields, that is, robotics, control theory, and machine learning. My research, often motivated by within large scale engineering possibilities, seeks to deconstruct the challenges that modern technology presents: combining the elegance of strong mathematical rigor in imbuing resilience and robustness into the little margins that exist in emerging autonomous systems; reasoning future technologies into existence though clear conceptual analyses baked in strong scientific rigor, and leveraging bio-inspiration to build emergent agent-centric systems as we continue to usher in a safe and desired haven for new technologies.


##### Learning to Explore in Unstructured Spaces

 The emergence of powerful foundation models has improved the reasoning capability of many AI systems leading to their wide adoption in solving a variety of problems including question-answering and vision processing tasks. In embodied two-dimensional and three-dimensional (3D) vision-enabled planning and control systems (often within hazardous environments) however, wrong (model) predictions or mis-specified (vision-language) actions during tasks’ execution can lead to deleterious consequences (in money, time, health, or even lives). Disciplined modularity in physical and virtual embodied reasoning systems is one way to imbue stability, robustness, and safety into embodied decision-making systems. Such systems must be amenable to efficient optimization -- combining discrete high-level abstraction modules (for reliably predicting and delineating environmental structure) with continuous low-level decision-making modules (that inform stable and safe world exploration). This hierarchical planning scheme in successive hybrids of discrete and continuous modules, informed by the power of existing foundation models together with combinatorial optimization, and trained on large application-specific datasets so that they are generalizable will inform robustness in agent-centric environment-agnostic decision-making, and guarantee safety during tasks’ executions via designed error-checking mechanisms.

 Our efforts in this space leverage modularization for automatic geometry delineation of component objects within any generic three-dimensional world. This is followed by an efficient obstacle-free space computational supervised learning module that first decomposes every detected structural component into convex structures. An iterative semi-definite convex programming algorithm, in an incrementally building of the collision-free configuration space of the entire environment, then follows. Making fast optimal decisions is important in many engineering systems and virtual three-dimensional systems. A bottleneck to such optimal decisions is determining what areas of space to explore. By having an automated algorithm that determines what regions of the environment is worth exploring, the problem of optimal decision-making is significantly reduced to a subset of the entire C-space. This scheme twill help engineers and planners reduce time to explore, gather data, or reason about an environment before making decision.

Connection to existing planning schemes: 

+ Going beyond kinodynamical reasoning that is the mainstay of classical planning systems towards an ensemble of foundation models for abstract world models including objects detection and segmentation, c-free computation, and low-level shortest path planning, minimum spanning tree problems,  and low-level control for hierarchical decision-making;

+ Connecting the output of the ensemble of eclectic models above to scaled network-based (combinatorial/convex) optimization framework that allows formulating decision-making at the intercept of high-level abstract reasoning about the world and low-level controller actions;

+ Incorporating safety-based controllers at this lower level for real-time, and modular decision-making. Building accessible and robust software systems that encapsulate this modular pipeline for general-purpose agents – physical (including robotics), virtual, mixed-reality, and simulated-reality alike.


**Relevant Papers:**

+ Mastering Collision-free computation via convex decomposition and neural networks. Lekan Molu. Nature. May 2025.

+ PCLAST: Discovering Plannable Continuous Latent States.
Anurag Koul, Shivakanth Sujit, Shaoru Chen, Ben Evans, Lili Wu, Lekan Molu, Byron Xu, Rajan Chari, Riashat Islam, Raihan Seraj, Yonathan Efroni, Miroslav Dudík, John Langford, Alex Lamb. International Conference on Learning Representations (ICLR). September 2023.

+ Guaranteed discovery of controllable latent states with multi-step inverse models. Alex Lamb, Riashat Islam, Yonathan Efroni, Aniket Didolkar, Dipendra Misra, Dylan Foster, Lekan Molu, Rajan Chari, Akshay Krishnamurthy, John Langford. Transactions in Machine Learning Research. December 2022.

+ Interaction-Grounded Learning with Action-inclusive Feedback. Tengyang Xie, Akanksha Saran, Dylan J Foster, Lekan Molu, Ida Momennejad, Nan Jiang, Paul Mineiro, and John Langford.
Neural Information Processing Systems (Neurips). May 2022.


##### What do Mr. Bellman or Isaacs have to do with Safety-Critical Systems?

Okay, let's talk about current AI decision-making systems. 

With the growing complexity of digital, electronic, and cyberphysical interfaces in the modern systems that we develop, the need to guarantee performance as envisioned by the systems architect in the face of uncertainty has become ever more timely. To deploy modern systems in the wild, modern software must be able to process generated data at multiple levels of abstraction within reasonable time yet guarantee consistency in system performance in spite of the dangers that may evolve if nominally envisioned system performance falter. To address this concern, we take the approach that considers software architectures for the numerical analysis of the safety assurance (ascertaining the freedom of a system from harm)in a _verification_ sense, that is, generating evidence that a system, or any its components satisfy all specified requirements and functional and allocated baselines and validation, that is, providing certifiable evidence that system capabilities comply with an end-user's performance requirements and satisfy its intended operational environment's specifications. 

Our efforts in this space involve exploiting various angles-of-attack assault on the Hamilton-Jacobi-Bellman and Hamilton-Jacobi-Isaacs equation in recommending and building safety into modern AI systems. 

**Relevant papers:**

+  Mastering Collision-free computation via convex decomposition and neural networks, Lekan Molu. Nature, May 2025.

+  A Generalized Nash Equilibrium Policy for Large Scale Multi-agent Systems, Lekan Molu. Proceedings of the National Academy of Sciences. April 2025.

+  A Sampling Scheme for Reachable Sets Computation, Lekan Molu. IEEE 64th Conference on Control and Decision. March 2025.

+  Is the Bellman Equation Enough for Learning Control? Haoxiang You, Lekan Molu, and Ian Abraham, Reinforcement Learning Theory Conference, 2025. March 2025.

+  LevelSetPy: A GPU-Accelerated Package for Resolving Hyperbolic Hamilton-Jacobi Partial Differential Equations, Lekan Molu. ACM Transactions on Mathematical Software. April 2024.

+  The Python LevelSet Toolbox (LevelSetPy), Lekan Molu. IEEE 63rd Conference on Decision and Control (CDC), Milano, Italia. December 2024.

+  Verification-aided Learning Neural Network Barrier Functions with Termination Guarantees. Shaoru Chen, Lekan Molu, and Mahyar Fazlyab. American Control Conference (ACC), Toronto, ON. May 2024.

+  Mixed H2/H-Infinity Policy Learning Synthesis. Lekan Molu. World Congress, International Federation of Automatic Control, Yokohama, Japan. July 2023.




##### Why are our robots so cumbersome?


The family of robot mechanisms that are largely used today emerged from the anthropomorphic design of Harry Asada at CMU in the early '80s. If modern robot manipulators were designed to behave like human arms, why has the community given up on making robots act the way humans do? Instead, we have accepted the Asada mechanism as the default configuration and practically every AI stack built for robots nowadays is premised on the assumption that models and policies will evolve on the anthropomorphic kinematically redundant robot arm design. Hear me out: natural organisms with embodied intelligence exploit their intrinsic morphological computation by integrating internal control computations with their structure for adaptive motion strategies. This embodied intelligence paradigm has inspired new design, modeling, and control paradigms in adaptive automation with soft robots – yielding more improved robot mechanisms with low stiffness-to-weight ratios and more reactiveness and adaptiveness to movement strategies in the physical world. In this design philosophy, rather than reject external disturbances and physical constraints, continuum soft robots must harness external forces and physical constraints for improved stiffness-to-weight ratio, bending, torsion, and twisting capabilities etc -- behaviors unlike of rigid robots. However, most design, modeling, and control schemes do not fully take advantage of these foundational principles. Novel mechanism designs are emerging given recent advances in material engineering. Even so, new kinematics, kinetics, and control methods for continuum robots are emerging. This thread aims to erect a cantilever bridge from the theoretical foundations of embodied intelligence to (i) the harnessing of natural organisms’ embodied intelligence in soft robots’ mechanism design; (ii) precise mathematical modeling tools  for predicting soft mechanisms behavior -- via ODE-based reduced-order finite dimensional control, and PDE-based modeling of continuum robots; (iii) emerging control methods for managing model complexity via time-scale separation and layered control architectures; and (iv) the power of machine learning from sensory experimental data to model and control behavior. 

**Relevant papers:**

+ On the number synthesis for deformable robots parameters identification. Lekan Molu. IEEE 64th Conference on Control and Decision. March 2025.

+ Fast Whole-Body Strain Regulation in Continuum Robots. Lekan Molu. American Control Conference (ACC), Denver, CO. June 2025.

+ Lagrangian Properties and Control of Soft Robots Modeled with Discrete Cosserat Rods. Lekan Molu and Shaoru Chen. Conference on Decision and Control (CDC). March 2024.

+ Mechanism and Model of a Soft Robot for Head Stabilization in Cancer Radiation Therapy. Olalekan Ogunmolu, Xinmin Liu, Nick Gans, and Rodney Wiersma. IEEE International Conference on Robotics and Automation (ICRA), Paris, France. May 2020.


<a name="serv"></a>
#### **Community Service**

I am an active member of the AI, control, and robotics research communities — regularly engaging in peer reviewing activities for [NeurIPS](https://nips.cc/), [International Federation of Automatic Control](https://www.ifac-control.org/) -- World Congress and Automatica alike, [Institute of Physics](https://www.iop.org/),  [ICML](https://icml.cc/), IEEE Access, [Conference on Decision and Control](https://2021.ieeecdc.org/), [IROS](https://en.wikipedia.org/wiki/International_Conference_on_Intelligent_Robots_and_Systems), [American Control Conference](https://acc2021.a2c2.org/),  ASME's [DSCC](https://event.asme.org/DSCC),  [ICRA](https://www.ieee-ras.org/conferences-workshops/fully-sponsored/icra), and [Neural Computing and Applications](https://www.springer.com/journal/521) among others.

Since January 2020, I have been a judge for NatGeo's [AI for Species Discovery Grant Applications](https://www.nationalgeographic.org/funding-opportunities/grants/). I am an active member of the Control Systems Society, often serving as session chair at our leading conferences on the planet -- Control and Decision Conference and the American Control Conference. In addition, I serve regularly as Associate Editor for IEEE Robotics' flagship conference -- International Conference on Robotics and Automation (ICRA).


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
##### **In the words of my students:**

_"Thank you again Lekan. [Taking RBOT 250 with you] was quite a journey. But I feel more confident now with ROS because I figured all of the ROS system. I'll be looking forward to see you run the class again."_

_"Dr. Molu is very caring about his students. I love how he makes time for me to run over course notes, point out helpful reading materials, and work through problems together with me. I enjoy the examples and exercises he tasks us with."_

_"I want to thank Lekan for teaching this course, I definitely learned a lot. I am interested in auditing it when Lekan runs it again."_