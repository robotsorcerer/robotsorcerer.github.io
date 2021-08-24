---
layout: post
date: 2021-08-24 11:51:00
title: "Re: On Souganidis and Evans' proof of the optimality condition for the lower value of the Cauchy problem HJ Equation."
excerpt: "Necessary and sufficiency conditions, differentiability and continuity assumptions, and analytical solutions to optimal control problems."
permalink: optimal-control
comments: true
mathjax: true
category: [control,optimal-control]
---
{% include mathjax.md %}


The text below concerns the proof derived by Evans and Souganidis in their 1984 seminal paper that related the "weaker" (or viscosity) solution to the _cauchy problem_ of HJ equations' lower value, viz.,

Evans, L. C., & Souganidis, P. E. (1984). Differential games and representation formulas for solutions of Hamilton-Jacobi-Isaacs equations. Indiana Univ. Math. J, 33(5), 773–797.

Specifically, equation 3.4 under Theorem 3.1  should read,

\begin{align}
  W(t,x) \ge \sup\_{y \in M(t)} \left{ \int\_t^{t+\sigma} h\left((s, x(s), y(s), \delta[y](s)\right) ds + V\left((t+\sigma), x(t+\sigma)\right)\right} - \epsilon
\end{align}

and not

\begin{align}
  W(t,x) \ge \sup\_{y \in M(t)} \left{ \int\_t^{t+\sigma} h\left((s, x(s), \delta[y](s)\right) ds + V\left((t+\sigma), x(t+\sigma)\right)\right} - \epsilon
\end{align}

The authors omitted the controls term \\(y(s) \in Y\\).  
