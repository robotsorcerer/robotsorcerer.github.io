---
layout: post
title: Dynamic Fusion: Reconstruction and Tracking of Non-rigid scenes in Real-Time
comments: true
date: 2015-07-07 21:20:25
excerpt: "Dynamic Fusion is an approach for solving a volumetric flow field that transforms the state of the scene at each time instant into a fixed, canonical frame."
permalink: pretty
---

###Review of Richard Newcombe's CVPR 2015 Dynamic Fusion Best Paper

####Introduction

**Dynamic Fusion** is an approach for solving a volumetric flow field that transforms the state of the scene at each time instant into a fixed, canonical frame. For a person in motion, the transformation remakes the subject's motion by warping each body configuration into the first frame's pose. After the warps, the scene is effectively rigid, and standard KinectFusion updates can be used to obtain a high quality, denoised reconstruction. The progressively denoised reconstruction can then be transformed back into the live frame using the inverse map with each point in the canonical frame transformed to its location in the live frame.
The basic challenge this work solves is the an approach for non-rigid transformation and fusion that retains the optimality properties of volumetric scan fusion which was originally developed for rigid scenes. Undoing the scene motion to enable fusion of all observations into a single _fixed_ frame can be efficiently achieved by computing the inverse of the volumetric scan.