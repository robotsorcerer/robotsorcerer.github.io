---
layout: post
date: 2018-08-21 13:10:00
title: "On Optimality and Stability"
excerpt: "A system under the effect of an optimal controller may not necessarily be stable."
permalink: opti-stable
comments: true
mathjax: true
category: [control, stability, optimality]
---
{% include mathjax.md %}

- [Table of Contents](#table-o-conts)
- [Introduction](#intro)
- [The case on stability vs optimality](#case)
- [Optimality issues](#issues)


<a name="intro"></a>
### Intro

The question of the connection between optimality and stability is a curious thing. On the one hand, we are triggered to believe that if we can find an optimal control law, that can execute a plan, with the least amount of energy possible, then we are satisfied to know we have fulfilled the specifications posed in  our objective function. But consider: an optimal controller is not necessarily a stable controller for a system. Why so? I lay out my case in the next section.

<a name="case"></a>
### The case on stability vs optimality

On the one hand, Lyapunov defines classical stability as the system's behavior near an equilibrium point such that there exists a real number \\(\delta(\epsilon, t\_0)>0\\) for every real \\(\epsilon > 0\\) for which the state of the system is bound -- essentially a local stability concept, a scalar bound that expresses how far away a system could ever get from the equilibrium (based on how far away it started).  As Engineers, we do not want to limit ourselves to this local stability context. We want every motion starting sufficiently close to the equilibrium state to to converge to the equilibrium as time approaches _ad infinitum_. Asymptotic stability captures this need elegantly. But again, asymptotic stability is as well a local concept since we do not know _a priori_ how much magnitude we want for the bound.  Enter equiasymptotic stability in the large. For an \\(r\\) that is fixed and arbitrarily large, we find that as \\(t \rightarrow \infty\\), all motions converge to the equilibrium uniformly in the initial state from which they start for \\(\|x_0\| \le r \\).

Note that all these definitions merely impose a constraint on the behavior of the states as they evolve over the trajectories of the system. That begs the question, can a control law be stable, yet not optimal? I think so. Why?

<a name="issues"></a>
### Optimality issues

Optimality, as Bellman would have us think, deals with reaching the goal state with as minimal a path as possible (we could define least time paths, least energy paths, et cetera, which are not necessarily the same) . AFAIK, the principle of optimality and Lyapunov stability have a fundamental disconnect. It seems to me that we may find an optimal control law that is not stable (i.e it’s V(x) gradient function does not strictly decrease along the trajectories of the solution to the dynamic system’s differential equation).

To buttress this fact, consider that the concepts of stability and optimality appeared in the consciousness of control theorists at two distinct and disconnected eras (or so to say) in history. On the one hand, Lyapunov's thesis got published in the Soviet union in the 1890's but his work was not available in English until 1947. Even so, western researchers did not adequately grasp its usefulness until Kalman's 1960 seminal paper on the second method of Lyapunov. Meanwhile, Bellman's last formal work on DP and applied DP did not become published until 1962. Even so, what is more intriguing is that not anywhere in Bellman's stability tests (as far as I can tell from what I have read from his books) did he use Lyapunov analysis' rigor to establish the stability of his methods. Kalman, remarked in his paper in 1960 that  few researchers were aware of Lyapunov methods. We can make a fairly accurate guesstimation that had Bellman been aware of Lyapunov's analyses earlier, it might have creeped into his optimality analyses.
