---
layout: post
date: 2018-08-04 13:10:00
title: "Control Concepts"
excerpt: "Just a random collection of theorems, existence and uniqueness for nonlinear control."
permalink: control-concepts
comments: true
category: [control]
---
{% include mathjax.md %}

- [Table of Contents](#table-o-conts)
- [Introduction](#intro)
- [Definitions Theorems, Lemmans](#defs)
- [Nonlinear Control Theory](#nlnr)


<a name="intro"></a>
### Intro

Here are a few control theorems, concepts and diagrams that I think every control student should know. I keep updating this post, so please check back from time to time.

<a name="defs"></a>
### Definitions, Theorems, Lemmas and such.

<a name="nlnr"></a>
#### Nonlinear Control Theory

+ Interrelations between stability concepts: This I gleaned from Dr. Rudolf Kalman's 1960 paper on the second method of Lyapunov.

<div class="fig figcenter fighighlight">
  <img src="/assets/control/control_concepts.png" width="100%" height="300" align="middle">  
  <div class="figcaption" align="middle">Fig. 1. Interrelations between stability concepts. Courtesy of R.E. Kalman
  </div>
</div>

+ A differential equation of the form

\begin{align}
  dx/dt = f(x, u(t), t), \quad -\infty < t < +\infty
  \label{eq:diff_eq}
\end{align}

is said to be free (or unforced) if \\(u(t) \equiv 0\\) for all \\(t\\). That is \eqref{eq:diff_eq} becomes

\begin{align}
  dx/dt = f(x, t), \quad -\infty < t < +\infty
  \label{eq:unforced}
\end{align}

+ If the differential equation in \eqref{eq:diff_eq} does not have an explicit dependence on time, but has an implicit dependence on time, through \\(u(t)\\), then the system is said to be stationary. In other words, a dynamic system is **stationary** if

\begin{align}
  f(x, u(t), t) \equiv f(x, u(t))
  \label{eq:stationary}
\end{align}

+ A stationary system \eqref{eq:stationary} that is free is said to be _invariant under time translation_, i.e.


\begin{align}
  \Phi(t; x\_0, t\_0) = \Phi(t + \tau; x\_0, t\_0 + \tau)
  \label{eq:free_stat}
\end{align}
    - \\(\Phi(t; x\_0, t\_0)\\) is the analytical solution to \eqref{eq:diff_eq}; it is generally interpreted as the solution of \eqref{eq:diff_eq}, with fixed \\(u(t)\\), going through state \\(x_0\\) at time \\(t_0\\) and observed at time \\(t\\) later on. This is a clearer way of representing the d.e.'s solution as against \\(x(t)\\), which is popularly used in most text nowadays.

  - \\(\Phi(\cdot)\\) is generally referred to the transition function, since it relates the transformation from \\(x(t\_0)\\) to \\(x(t)\\).

  - For a physical system, \\(\Phi\\) has to be _continuous in all of its arguments._
.

+ If the rate of change \\(dE(x)/dx\\) of an isolated physical system is negative for every possible state x, except for a single equilibrium state \\(x\_e\\), then the energy will continually decrease until it finally assumes its minimum value \\(E(x)\\).

+ The **first method of Lyapunov** deals with questions of stability using an explicit representation of the solutions of a differential equation
  - Note that the **second method** is more of a historical misnomer, perhaps more accurately described as a philosophical point of view rather than a systematic method. Successful application requires the user's ingenuity.

+ In contrast to popular belief that the energy of a system and a Lyapunov function are the same, they are not the same. Why? Because **the Lyapunov function, (\\V(x)\\), is not unique**. To quote Kalman, "a system whose energy \\(E\\) decreases _on the average_, but not necessarily at each instant, is stable but \\(E\\) is not necessarily a Lyapunov function."

+ **Lyapunov analysis and optimization**: Suppose a performance index is defined to be the error criterion between a measured and an estimated signal; suppose further that this criterion is integrated w.r.t time, then the performance index is actually a Lyapunov function -- provided that the error is not identically zero along any trajectory of the system.

+ **Existence, uniqueness, and continuity theorem**:

  - Let \\(f(x, t)\\) be continuous in \\(x,t\\), and satisfy a Lipschitz condition in some region about any state \\(x\_0\\) passing through time \\(t\_0\\):

  \begin{align}
    R(x\_0, t\_0) = \begin{cases}
      ||x - x\_0|| \le b(x\_0) \nonumber \\
      ||t - t\_0|| \le c(t\_0)  \quad (b, c) > 0
    \end{cases}
  \end{align}

with the Lipschitz condition satisfied for \\((x,t), (y,t)\\) i\\(\in\\) \\(R(x\_0, t\_0)\\), then it follows that
\begin{align}
  ||f(x,t) - f(y,t)|| \le k \, ||x-y|| \nonumber
\end{align}

where \\(k>0\\) and it depends on \\(b, c\\). THUS,
   -   there exists a unique solution \\(\Phi(t; x\_0, t\_0)\\) of \\(dx/dt\\), that starts as \\(x\_0, t\_0\\) for all \\( |t - t\_0| \le a(t\_0) \\),

      - \\(a(t\_0) \ge \text{ Min }\{c(t\_0), b(x(t\_0))/M(x\_0, t\_0)\}\\), where \\(M(x\_0, t\_0)\\) is the maximum assumed by the continuous function \\(f(x,t)\\) in the closed, bounded set \\(R(x\_0, t\_0)\\)
  - In some small neighborhood of \\(x\_0, t\_0\\), the solution is continuous in its arguments

Observe that the Lipschitz condition only implies continuity of \\(f\\) in \\(x\\) but not necessarily in \\(t\\); as it is implied by the bounded derivatives in \\(x\\). Note that the local lipschitz condition required by the theorem only implies desired properties of a solution near \\(x\_0, t\_0\\). The _finite escape time_ (that is it leaves any compact set within a finite time.) quandary does not allow us to make conclusions surrounding arbitrarily large values of \\(t\\). The phrase “finite escape time” is used to describe the phenomenon that a trajectory escapes to infinity at a finite time. **In order that a differential equation accurately represent a physical system, the possibility of finite escape time has to be mitigated by an explicit assumption to the contrary.** If the Lipschitz condition holds for \\(f\\) everywhere, then there can be no finite escape time. The proof is easy by integrating both sides of \eqref{diff_eq} and using

\begin{align}
  \Phi(t; x\_0, t\_0) \le ||x\_0|| + || \int_{t\_0}^{t}f(\Phi(\tau; x\_0, t\_0), \tau)d\tau || \nonumber \\
  ||x\_0|| + k \int_{t\_0}^{t}f(\Phi(\tau; x\_0, t\_0), \tau)d\tau
\end{align}

where \\(f(\cdot)\\) obeys the lipschiz condition

\begin{align}
  ||f(x,t) - f(y,t)|| \le k \, ||x-y|| \nonumber
\end{align}

By the Gronwall-Bellman lemma,

\begin{align}
  ||\Phi(t; x\_0, t\_0) ||  \le [exp k (t - t\_0)] ||x_0 || \nonumber
\end{align}

which is less than \\(\infty \\) for any finite (t - t\_0)
