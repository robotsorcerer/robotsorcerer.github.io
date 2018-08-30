---
layout: post
date: 2018-08-22 13:10:00
title: "Optimality vs. Stability of Feedback Control Systems"
excerpt: "A system under the effect of an optimal controller may not necessarily be stable."
permalink: opti-stable
comments: true
mathjax: true
category: [control, stability, optimality]
---
{% include mathjax.md %}

- [Table of Contents](#table-o-conts)
- [Introduction](#intro)
- [Stability vs optimality](#case)
- [Optimality](#issues)


<a name="intro"></a>
### Intro

The question of the connection between optimality and stability is a curious thing.  On the one hand, we are led to believe that if we can find an optimal control law, that can execute a plan, with the least amount of energy possible, then we are satisfied to know we have fulfilled the specifications posed in  our objective function. But consider: an optimal controller is not necessarily a stable controller for a system. Why so? I lay out my case in the next section.

<a name="case"></a>
### Stability vs optimality
Systems under the influence of optimal control laws enjoy a nice set of properties, provided that the associated cost functional enforces a constraint that is desirable on the state and control. LQ optimal control systems have nice gain and phase margins coupled with reduced sensitivity and I understand that there are similar properties that have been shown for nonlinear systems. Optimal control has the attractive property that the control effort is not wasted in mitigating the effects of nonlinearities as it chooses among a set of policies (or stabilizing control sequences) that yield a desirable effect on the system. The intractability of the HJB equation however makes optimal control as a synthesis tool for nonlinear problems a painful one.

Enter Lyapunov stability. Lyapunov defines classical stability as the system's behavior near an equilibrium point such that there exists a real number \\(\delta(\epsilon, t\_0)>0\\) for every real \\(\epsilon > 0\\) for which the state of the system is bound -- essentially a local stability concept, a scalar bound that expresses how far away a system could ever get from the equilibrium (based on how far away it started).  As Engineers, we do not want to limit ourselves to this local stability context. We want every motion starting sufficiently close to the equilibrium state to converge to the equilibrium as time approaches _ad infinitum_. Asymptotic stability captures this need. But again, asymptotic stability is as well a local concept since we do not know _a priori_ how much magnitude we want for the bound.  Enter equiasymptotic stability in the large. For an \\(r>0\\) that is fixed and arbitrarily large, we find that as \\(t \rightarrow \infty\\), all motions converge to the equilibrium uniformly in the initial state from which they start for \\(\|x_0\| \le r \\).

Note that all these definitions merely impose a constraint on the behavior of the states as they evolve over the trajectories of the system. That begs the question, can a control law be stable, yet not optimal (or vice versa)? I think so. Why?

<a name="issues"></a>
### Optimality

> This section has an update based on what I found from Freeman and Kokotovic's 1996 Paper in the Int'l J. Optimal & Control. Please skip to the [updated part](#updatedOptStab)

Optimality, as Bellman would have us think, deals with reaching the goal state with as minimal an energy as possible. I would think that the principle of optimality and Lyapunov stability have a fundamental disconnect. It seems to me that we may find an optimal control law that is not stable (i.e it’s V(x) gradient function does not strictly decrease along the trajectories of the solution to the dynamic system’s differential equation).

~~To buttress this fact, consider that the concepts of stability and optimality appeared in the consciousness of control theorists at two distinct and disconnected eras (or so to say) in history. On the one hand, Lyapunov's thesis got published in the Soviet union in the 1890's but his work was not available in English until 1947. Even so, western researchers did not adequately grasp its usefulness until Kalman's 1960 seminal paper on the second method of Lyapunov. Meanwhile, Bellman's last formal work on DP and applied DP did not become published until 1962. What is more intriguing is that not anywhere in Bellman's stability tests (as far as I can tell from what I have read from his books) did he use Lyapunov analyses' rigor to establish the stability of his principle of optimality methods. Kalman, remarked in his paper in 1960 that  few researchers were aware of Lyapunov methods. We can make a fairly accurate "guesstimation" that had Bellman been aware of Lyapunov's analyses earlier, it might have creeped into his optimality analyses.~~

~~I had an exchange with someone about this a while ago, and I am quoting the caveats they expressed in their agreement with my observation below.~~


> ~~1) If optimality is concerned only with the cost from initial condition to final condition, a control law that makes the system unstable might be desirable as unstable systems tend to be very fast.~~

> ~~2) The problem is what happens when you reach the final condition?  An unstable system will not stop there, but will overshoot the goal and go off to infinity.  So you must have the ability to switch to a stabilizing controller when you reach the goal.~~

> ~~An example is in fighter aircraft.  I understand that they become unstable during certain maneuvers such as tight turns so they can move very fast, but then “catch” themselves and stabilize before going too far from the equilibrium.~~

<a name="updatedOptStab"></a>
**UPDATE [Aug 28, 2018]**

Most of the discussions below are drawn from Freeman and Kokotovic's ^[Freeman_Kokotovic] 1996 work on _point-wise min-norm control laws for robust control lyapunov functions_.

They provide an optimality-based method for choosing a _stabilizing_ control law once an rclf is known without resorting to cancellation or domination of nonlinear terms, which do not necessarily possess the desirable properties of optimality and may lead to poor robustness and wasted control effort.

The value function for a meaningful optimal stabilization problem is a Lyapunov function for the closed-loop system.

* Every meaningful value function is a Lyapunov function (Freeman and Kokotovic, 1996). Every Lyapunov function for every stable closed-loop system is also a value function for a meaningful optimal stabilization problem.

* Every Lyapunov function is a meaningful value function

Both bullets above are important since the first point helps with the analysis of the stability of an optimal feedback control system, while the second link will have implications for their synthesis.

* Every robust control lyapunov function (rclf) is a meaningful upper value function

  - Every rclf solves the Hamilton Jacobi Isaacs equation associated with a meaningful game. For a known rclf, a feedback law that is optimal w.r.t a meaningful cost functional can be constructed. Matter-of-factly, this can be accomplished without solving the HJI equation for the upper value function or without constructing a cost functional as the optimal feedback can be directly calculated from the rclf without recourse to the HJI equation. Such control laws are called _pointwise min-norm_ control laws and each one inherits the desirable properties of optimality because _every pointwise min-norm control law is optimal for a meaningful game_.

Essentially, this task is an _inverse optimal stabilization problem_ where for LTI systems, the solution involves choosing a candidate value function and then constructing a meaningful cost functional in order to make the HJB equation valid. For open-loop stable nonlinear systems, one can find a solution by choosing the candidate value function as a Lyapunov function for the open-loop system. For openloop _unstable_ systems, one can choose a candidate value function as a clf for the system. In Freeman and Kokotovic's [^Freeman_Kokotovic], actually the authors solve the inverse optimal _robust_ stabilization problem for systems with disturbances and showed that evert rclf is an upper value function for a meaningful differential game.


[^Freeman_Kokotovic]: Freeman, R. A., & Kokotovic, P. V. (1996). Inverse Optimality in Robust Stabilization. SIAM Journal on Control and Optimization, 34(4), 1365–1391. https://doi.org/10.1137/S0363012993258732
