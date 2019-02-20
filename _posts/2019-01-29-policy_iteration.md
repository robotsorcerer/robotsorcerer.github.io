---
layout: post
date: 2019-01-29 19:40:00
title: "Policy Iteration -- A Review"
excerpt: "A system under the effect of an optimal controller may not necessarily be stable."
permalink: opti-stable
comments: true
mathjax: true
category: [control, stability, optimality]
---
{% include mathjax.md %}

#### Adapted from Bertsekas' Approximate Policy Iteration Review Paper

First, a background. There are unique solutions to the Bellman equations

\\(J\_\mu(i) = \sum_{j=1}^{n}p\_{ij}(\mu(i))(g(i, \mu(i), j) + \alpha  J\_\mu(j)), \quad i =1, \ldots, n
\\)

where \\(u \in U(i)\\) are the controls at state \\(i=1, \ldots, n\\), \\(p_{ij}(u)\\) are the transition probabilities and \\(g(i,u,j)\\) are the costs for transitioning from \\(i\\) to \\(j\\) under control \\(u\\). A stationary policy \\(\mu\\) is a function from states \\(i\\) to admissible controls \\(u \in U(i)\\), and \\(J\_\mu(i)\\) is the cost of starting from state \\(i\\) and using policy \\(\mu\\)

Policy iteration is a major alternative to value iteration  -- it generates a set of policies and associated cost functions through iterations that have two phases: _policy evaluation_ and _policy improvement_. Policy evaluation is where the costs function of a policy is evaluated and policy improvement is where a new policy is generated. In the exact form of the algorithm, the current policy \\(\mu\\) is improved by finding \\(\bar{\mu}\\) that satisfies the contraction equation \\(T\_{\bar{\mu}}J\_\mu = TJ\_\mu\\). The improved policy \\(\bar{\mu}\\) is found by solving the following system of linear equations

\\(
  J\_{\bar{\mu}} = T\_{\bar{\mu}} J\_{\bar{\mu}}
\\)

where \\(T\\) is the so-called sup-norm contraction. The new cost-vector pair,  (\\(J\_{\bar{\mu}}, \bar{\mu} \\)), is then used to start a new iteration.

In a variant of the algorithm, the improved policy \\(\bar{\mu}\\) is evaluated by applying \\(T\_{\bar{\mu}}\\) a finite amount of times to an approximated evaluation of the preceding policy \\(\mu\\), denoted by \\(\tilde{J}\_\mu\\). This is the "optimistic" or "modified" policy iteration, with the motivation that in problems with large states, matrix inversuion is impractical.

**The exact form of policy iteration converges to an optimal cost-policy pair for any initial conditions** i.e. in a finite amount of iterations when policy number is finite, e.g. discounted MDPs.  When optimistic policy iteration is asynchronously implemented (e.g. irregularly, one state at a time), the convergence is fragile, requiring that the initial pair (\\(\tilde{J}\_{\mu^0}, \mu^0\\)) satisfy \\(T\_{\mu^0}\tilde{J}\_{\mu^0} \le \tilde{J}\_{\mu^0}\\).


#### Policy Iteration with Cost Function Approximation
