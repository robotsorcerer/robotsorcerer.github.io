---
layout: post
date: 2017-05-14 13:28:00
title: "Should I use ROS or MuJoCo?"
excerpt: ""
permalink: mujoco-ros
comments: true
mathjax: true
category: [Q&A,ros,mujoco]
---

This was my answer to a question posted in an email thread to our research group's email list at UTD. The question goes like this:
<br></br>
________________________________________
From: XXX@utdallas.edu
Sent: Sunday, May 14, 2017 9:29 AM
To: XXX@lists.utdallas.edu
Subject: RE: [robotec] MuJoCo

Thanks for sharing!

From the documentation, looks like MuJoCo is faster and therefore better to simulate computational intensive controllers like MPC. Gazebo provides other engines as well and seems like is more popular in the ROS community. How to choose between the available options? Which one would you recommend?

Thanks,
XXX

#### Answer

Great question.

Question: How to choose between the available options? Which one would you recommend?
=======================================================

TL; DR
If you do not care for accuracy of simulated controller numerical results, if you are not simulating parallel linkages, if you do not need code parallelization (i.e. your computation is not crazy intensive) or if you are not simulating contact and friction, I would choose ROS. Easy to use and straightforward to build fairly complex models.  


Proper (Long) Answer
==========================================================
ROS and Gazebo (OSRF tools) are indeed popular in the robotics community like you mentioned and they have their pros. It took me a while to see their limit when using them for research purposes.

Definition
-------------
ROS = Plumbing + Tools + Capabilities + Ecosystem

Plumbing: ROS provides publish-subscribe messaging infrastructure designed to support the quick and easy construction of distributed computing systems.

Tools: ROS provides an extensive set of tools for configuring, starting, introspecting, debugging, visualizing, logging, testing, and stopping distributed computing systems.

Capabilities: ROS provides a broad collection of libraries that implement useful robot functionality, with a focus on mobility, manipulation, and perception.

Ecosystem: ROS is supported and improved by a large community, with a strong focus on integration and documentation. ros.org is a one-stop-shop for finding and learning about the thousands of ROS packages that are available from developers around the world. answers.ros.org is a rich online community of ros packages users from around the world asking questions and getting help on how to use ROS.

So getting a simple dynamics kicking should not be a lot of hassle as the documentation is rich and the online community is very active in supporting newbies.

In the early days, the plumbing, tools, and capabilities were tightly coupled, which has both advantages and disadvantages. On the one hand, by making strong assumptions about how a particular component will be used, developers are able to quickly and easily build and test complex integrated systems. On the other hand, users are given an "all or nothing" choice: to use an interesting ROS component, you pretty much had to jump in to using all of ROS.

8+ years in after Andrew Ng and co. conceived the platform, the core system has matured considerably, and developers are hard at work refactoring code to separate plumbing from tools from capabilities, so that each may be used in isolation. In particular, people are aiming for important libraries that were developed within ROS to become available to non-ROS users in a minimal-dependency fashion (e.g. OMPL and PCL libraries).

(Disclaimer: I  borrowed  the foregoing from Brian Gerkey's/my answer to a similar quora question about a year ago)

For serially linked robot arms and other non-parallel linkages, ROS is a great simulation tool and "middleware".  However, there are bottlenecks with ROS.

What ROS calls URDF (Universal Robot Description Format), which is the abstraction tool for rigid body dynamics, is not universal in any sense of the word. URDF models written in ROS are  out-of-the-box incompatible with Gazebo, its sister physics engine (see this question/wiki: http://answers.gazebosim.org/question/14891/conversion-from-urdf-to-sdf-using-gzsdf-issues/).  More so, state representation in OSRF tools such as ROS is represented in a tree-like manner. I learnt this late last year when simulating parallel linkages. The internal ROS XML  parser interprets constructed linkages as a deep binary tree and not graphs. This makes  simulating parallel linkages almost (actually) impossible. Repeat, actually impossible. They have a fix for this in Gazebo SDF but it is not straightforward. So developers spend a huge chunk of time migrating code from one OSRF framework to another.

Good controller algorithm formulations are based on numerical optimization (think MPC, differential dynamic programming, sampling-based motion-planning or reinforcement learning). Gazebo was designed around the ODE (Open Dynamics Engine) and Bullet physics engines which provide the states in over-complete Cartesian coordinates and enforce joint constraints via numerical optimization. This is good enough for disconnected bodies with few joint constraints but becomes a pain for complex dynamics such as humanoids or simulating human-robot interactions. Running complex simulations for huge candidate evaluations of humanoids can run into months using ROS (e.g. Todorov's de novo synthesis). Whereas MUJOCO is optimized for parallel processing, distributed evaluation of possible controllers from which a candidate controller is chosen.

ODE simulators optimize the controller to the engine. This makes the controller cheat during simulations in ways that mean generated control laws may be physically unrealizable. Speed and accuracy? Controller optimization with MoveIt! (a motion planning framework from OSRF) is mostly done in a single threaded code without the advantage of explicit parallelization of code to make e.g. IK solutions faster. Implementation of concurrency and multithreading is left to the user (this is a big no-no for someone not interested in software engineering).

ROS is strictly written based on the assumption that the user is running a Linux kernel. So users not familiar with Linux are thrown aback when they first get exposed to it. With MUJOCO, you do not need Linux or OSX as it works on Windows OS just fine. MUJOCO also use an XML parser to interpret links and joints and so it is able to read ROS URDFs and xacro files okay. But it doesn't work the other way (see this answer from Todorov: http://www.mujoco.org/forum/index.php?threads/ros-gazebo-integration.3371/)

MPC implementations are elegant only when the model is accurate. Unexpected poor performance of an MPC controller will often be due to poor modeling assumptions (Rossiter).  If the simulation engine emphasizes simulation stability over control law precision, we have a problem.  And this is my problem with Gazebo and ROS generally. I read it somewhere in one of Todorov's papers (can't remember where I found it) that the floating point ops of MUJOCO were unit tested to >>355 decimal points. The OSRF community may be good at community based software engineering for robotics but you have to give Todorov the credit. He had the patience and tenacity to develop such a robust software for control simulation. People stopped paying attention to floating point operational precision back in the late 80's/90's.

What's more? MUJOCO allows you to write your models in C. Engineers are head over boots for Matlab but I am all for a program or modeling software that stays close to ones and zeros as much as possible. It means being less dumbfounded when things do not work as you envisioned and greater flexibility in being the master and architect of your creation.

Just my two cents. My perspective may be limited by what I do not yet know. So take my response with a grain of salt.
