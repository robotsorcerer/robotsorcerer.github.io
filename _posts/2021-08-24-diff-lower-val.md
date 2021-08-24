---
layout: post
date: 2021-08-24 11:51:00
title: "On Souganidis and Evans' proof of the optimality condition for the lower value of the Cauchy problem HJ Equation."
excerpt: "Fix to lower value of Cauchy problem HJ equation proof."
permalink: Souganidis
comments: true
mathjax: true
category: [control,optimal-control]
---
{% include mathjax.md %}


The text below concerns the proof derived by Evans and Souganidis in their 1984 paper that related the "weaker" (or viscosity) solution to the _cauchy problem_ of HJ equations' lower value, viz.,

> Evans, L. C., & Souganidis, P. E. (1984). Differential games and representation formulas for solutions of Hamilton-Jacobi-Isaacs equations. Indiana Univ. Math. J, 33(5), 773–797.

Specifically, equation 3.4 under Theorem 3.1  should read,

\begin{align}
  W(t,x) \ge \sup\_{y \in M(t)} \{ \int\_t^{t+\sigma} h \left(s, x(s), y(s), \delta \[y\](s) \right)  ds + V\left(t+\sigma, x(t+\sigma) \right) \} - \epsilon
\end{align}

and not

\begin{align}
  W(t,x) \ge \sup\_{y \in M(t)} \{ \int\_t^{t+\sigma} h \left(s, x(s), \delta \[y\](s) \right)  ds + V\left(t+\sigma, x(t+\sigma) \right) \} - \epsilon
\end{align}

The authors omitted the control term \\( y(s) \in Y \vert y \\)  is measurable.  
