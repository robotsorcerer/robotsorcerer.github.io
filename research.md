---
layout: page
---


<!-- <center> -->
<!-- <a href="#revs"><font size="4">Introduction / </font></a> -->
### Contents

<a href="#expose"><font size="4"> Research Exposé / </font></a>
<a href="#incubate"><font size="4"> R&T Incubations / </font></a>
<a href="#safety"><font size="4"> Between Bellman and Isaacs </font></a>
<br>
<a href="#explore"><font size="4"> Not Cumbersome Robots Again! / </font></a>
<a href="#cumbersome"><font size="4"> Explorative Learning  </font></a>
<br>
<a href="#service"><font size="4"> Service / </font></a>
<a href="#mentor"><font size="4">Mentoring  / </font></a>
<a href="#teaching"><font size="4">Teaching  / </font></a>
<a href="#fdbks"><font size="4">Reports. </font></a>
<!-- </center> -->

<a name="expose"></a>
##### Research Exposé

The rise in computational power together with the pervasiveness of big data has created new computing modalities which has spurred an emergent digital economy, and has spawned new business value chains. Across these spates of recent developments, the question of resilience and reliability, safety and robustness, as well as the assured predictability of behavior in the (autonomous) systems that we design and build has become timely and crucial. Emergent autonomous AI systems must make decisions under imperfect circumstances based on environment information that is available from an array of perceptual inputs and their representation, reason through self-enumerated possible actions, and safetly execute the ones that provide a meaningful state transition in the environment in which they act --- all the while guaranteeing safety, stability, and resilience under external disturbances. Broadly, one can think of autonomous AI systems along two general threads: (i) situated autonomy, such as an automated airline ticket reservation system that reserves and makes decisions based on provided input by an external agent; and (ii) embodied autonomy, that is agents with perceptual sensors and proprioceptive actuators that make a physical change in their environment; an example in this latter category are physical robots that sense the world directorly through contact, and react adaptively to effect a change in representation of their environment bvia feedback. In both situated and embodied autonomy, we expect algrithms to deliver performance specifications without a glitch as we automate away tasks that humans have traditionally performed for over a century. My core research exists at the intersection of three intertwined fields that encapsulate important questions surrounding situatedness and embodiments: **robotics**, **control theory**, and **machine learning**. Robotics is crucial for the automation of physical embodiments. Control theory offers the strong scientific rigor that establishes strong robustness and resilient foundations in flimsy AI models and policies (that encompass situatedness and embodiments). And machine learning provides the relaxation to devise generalist algorithmics that transcend narrow applications to general usage in contemporary society. Motivated by what is possible with hitherto unexplored and large-scale engineering feats across these three disciplnes, my research seeks to deconstruct the challenges that modern technology presents viz., (i) combining the elegance of mathematical rigor in imbuing resilience and robustness into the little margins that exist in safety-critical embodiments; (ii) reasoning possible automation capabilities into existence through abstract sub-task modules in a hierarchy of system architectural principles; this is guided by clear conceptual analyses baked in the tradition of classical scientific rigor; and (iii) leveraging bio-inspiration to build emergent agent-centric situated AI and embodied robotic systems as we continue to usher in a safe and desired haven for future technologies that can co-exist with human beings in everyday living.


<a name="incubations"></a>
### Research and Technology Incubations: A North Star


To accelerate the turn-around time from research ideation to formalized incubation and products, we strive to realize these visions via systematic and strategic missions (within and outside Microsoft) that connect diverse workstreams and teams through cross-geographic community-building and cross-discipline collaborations. Our goal is to smother conventions (when needed), mother new inventions, and accelerate the realization of lava-stage technologies. The threads under investigation are further described in what follows.

<a name="safe"></a>
##### Between Messrs Bellman and Isaacs: Safety-Critical Systems?

The digital, electronic, and cyberphysical interfaces in the modern systems that we develop are growing ever more complex. The need to guarantee performance as envisioned by the systems architect in the face of uncertainty has become ever more timely. To deploy modern systems in the wild, modern software must process generated data at multiple levels of abstraction within reasonable time, and guarantee consistency in system performance in spite of the dangers that may evolve if nominally envisioned system performance falter. To address this concern, we take the approach that considers software architectures for the numerical analysis of the safety assurance (ascertaining the freedom of a system from harm) in a _verification_ sense. By verification, we mean generating evidence that a system, or any its components satisfy all specified requirements and functional and allocated baselines. An ensuing approach considered validation systems, that is, providing certifiable evidence that system capabilities comply with an end-user's performance requirements and satisfy its intended operational environment's specifications. 

Our efforts in this space involve exploiting various angles-of-attack assault on the Hamilton-Jacobi-Bellman and Hamilton-Jacobi-Isaacs equation in recommending and building safety into modern AI and cntrol systems. 

**Relevant papers**
+  Verification-aided Learning Neural Network Barrier Functions with Termination Guarantees. Shaoru Chen, Lekan Molu, and Mahyar Fazlyab. American Control Conference (ACC), Toronto, ON. May 2024.
+  A Generalized Nash Equilibrium Policy for Large Scale Multi-agent Systems, Lekan Molu. Proceedings of the National Academy of Sciences. April 2025.
+  A Sampling Scheme for Reachable Sets Computation, Lekan Molu. IEEE 64th Conference on Control and Decision. March 2025.
+  Is the Bellman Equation Enough for Learning Control? Haoxiang You, Lekan Molu, and Ian Abraham, Reinforcement Learning Theory Conference, 2025. March 2025.
+  LevelSetPy: A GPU-Accelerated Package for Resolving Hyperbolic Hamilton-Jacobi Partial Differential Equations, Lekan Molu. ACM Transactions on Mathematical Software. April 2024.
+  The Python LevelSet Toolbox (LevelSetPy), Lekan Molu. IEEE 63rd Conference on Decision and Control (CDC), Milano, Italia. December 2024.
+  Mixed H2/H-Infinity Policy Learning Synthesis. Lekan Molu. World Congress, International Federation of Automatic Control, Yokohama, Japan. July 2023.


##### On contemporary robots being cumbersome (in size and to operate)?


Most robot manipulator mechanisms that are largely used in academe and industry today emerged from the anthropomorphic design of Harry Asada at CMU in the early '80s. Designed to act the way humans do, they were built with rigid mechanical links that enforce dexterity and reasonably accurate manipulability. To avoid large hysteresis during repeated operations, they are manufactured to be sturdy, with parts made of rigid metals. This introduces hazards in human-robot environments. In addition, being a collection of rigid metals, adjoined by mostly rotary joints, they magnify errors from shoulder all the way out to the end effector, making precision intractable in precision automation. I can anticipate the question on the top of your mind: if modern robot manipulators were designed to behave like human arms, why has the community given up on making robots with improved stiffness-to-weight ratios, improved bending, and twisting capabilities, and manipulability beyond the geometric primitives that the workspace of rigid robots provide? Practically every AI stack built for robots nowadays is premised on the assumption that models and policies will evolve on the anthropomorphic kinematically redundant robot arm configuration. 

In the future, I envision pervasive robot configurations whose design is premised on the [embodied intelligence principle]((https://www.iris.sssup.it/handle/11382/461975), informed by [morphological computation]((https://philpapers.org/rec/HAUOAO) that is situated in many natural organisms. Natural organisms with embodied intelligence exploit their intrinsic morphological computation by integrating internal control computations with their structure for adaptive motion strategies. This embodied intelligence paradigm can inspire new design, modeling, and control paradigms in adaptive automation with soft robots. Soft robots yield more improved  stiffness-to-weight ratios and can offer better reactiveness and adaptiveness to movement strategies that otherwise rigid robots are not capable of. In this design philosophy, rather than reject external disturbances and physical constraints, continuum soft robots must harness external forces and physical constraints for improved stiffness-to-weight ratio, bending, torsion, and twisting capabilities etc -- behaviors unlike of rigid robots. 

My goal in this paradigm is to fully take advantage of these foundational embodied intelligence principles. Novel mechanism designs are emerging given recent advances in material engineering. Even so, new kinematics, kinetics, and control methods for continuum robots are emerging. This thread aims to erect a cantilever bridge from the theoretical foundations of embodied intelligence to (i) the harnessing of natural organisms’ morphology in soft robots’ configurations and mechanism design; (ii) the precise mathematical modeling tools  for predicting soft mechanisms behavior -- via ODE-based reduced-order finite dimensional control, and PDE-based modeling of continuum robots; and (iii) to the emerging control methods for managing model complexity via time-scale separation and layered control architectures. When all of this are laid out to a sufficient degree of exposition, my goal is to leverage the power of machine learning from sensory experimental data to model and control behavior seamly.

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