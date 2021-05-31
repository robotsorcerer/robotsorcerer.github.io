---
layout: post
date: 2021-05-31 13:10:00
title: "Control Commons"
excerpt: "Just a random collection of stability, continuity, existence, and uniqueness theorems for nonlinear control"
permalink: control-commons
comments: true
category: [control, stability, nonlinear-control]
---
{% include mathjax.md %}


- [Table of Contents](#table-o-conts)
- [Introduction](#intro)
- [Definitions, Theorems, Lemmas etc](#defs)
- [Nonlinear Control Theory](#nlnr)
- [Stability](#stab)
- [Control Barrier Functions](#CBFs)
  - [Invariant Sets](#Invariance)
  - [Forward Invariant Sets, Safety](#safety)
  - [Class Kappa Functions](#class-kappa)
  - [Control Barrier Functions Definition](#cbf-proper)


<a name="intro"></a>
### **Introduction**

Here are a few control theorems, concepts and diagrams that I think every control student should know. I keep updating this post, so please check back from time to time.

Side node: First version online: August 8, 2018. Wrote it up on the JR train one night in the summer of '18 while exploring the Japaneasy countryside  from Tokyo to Sendai.


<a name="defs"></a>
### Definitions, Theorems, Lemmas and such.

<a name="nlnr"></a>
#### **Nonlinear Control Theory**

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

+ In contrast to popular belief that the energy of a system and a Lyapunov function are the same, they are not the same. Why? Because **the Lyapunov function, \\(V(x)\\), is not unique**. To quote Kalman, "a system whose energy \\(E\\) decreases _on the average_, but not necessarily at each instant, is stable but \\(E\\) is not necessarily a Lyapunov function."

+ **Lyapunov analysis and optimization**: Suppose a performance index is defined to be the error criterion between a measured and an estimated signal; suppose further that this criterion is integrated w.r.t time, then the performance index is actually a Lyapunov function -- provided that the error is not identically zero along any trajectory of the system.

+ **Existence, uniqueness, and continuity theorem**:

  Let \\(f(x, t)\\) be continuous in \\(x,t\\), and satisfy a Lipschitz condition in some region about any state \\(x\_0\\) passing through time \\(t\_0\\):

  \begin{align}
    R(x\_0, t\_0) &=
      ||x - x\_0|| \le b(x\_0) \nonumber
  \end{align}

  \begin{align}
    R(x\_0, t\_0) &= ||t - t\_0|| \le c(t\_0)  \quad (b, c) > 0
  \end{align}

with the Lipschitz condition satisfied for \\((x,t), (y,t)\\) \\(\in\\) \\(R(x\_0, t\_0)\\), then it follows that
\begin{align}
  ||f(x,t) - f(y,t)|| \le k \, ||x-y|| \nonumber
\end{align}

where \\(k>0\\) depends on \\(b, c\\). THUS,
  - there exists a unique solution \\(\Phi(t; x\_0, t\_0)\\) of \\(dx/dt\\), that starts as \\(x\_0, t\_0\\) for all \\(\|t - t\_0\| \le a(t\_0)\\),

  - \\(a(t\_0) \ge \text{ Min (}\{c(t\_0), b(x(t\_0))/M(x\_0, t\_0)\}\\), where \\(M(x\_0, t\_0)\\) is the maximum assumed by the continuous function \\(f(x,t)\\) in the closed, bounded set \\(R(x\_0, t\_0)\\)

  - in some small neighborhood of \\(x\_0, t\_0\\), the solution is continuous in its arguments

Observe that the Lipschitz condition only implies continuity of \\(f\\) in \\(x\\) but not necessarily in \\(t\\); as it is implied by the bounded derivatives in \\(x\\). Note that the local lipschitz condition required by the theorem only implies desired properties of a solution near \\(x\_0, t\_0\\).

The _finite escape time_ (that is the solution leaves any compact set within a finite time) quandary does not allow us to make conclusions surrounding arbitrarily large values of \\(t\\). The phrase “**finite escape time**” describes the concept that a trajectory escapes to infinity at a finite time. **In order that a differential equation accurately represent a physical system, the possibility of finite escape time has to be mitigated by an explicit assumption to the contrary.** If the Lipschitz condition holds for \\(f\\) everywhere, then there can be no finite escape time. The proof is easy by integrating both sides of \eqref{eq:diff_eq} and using

\begin{align}
  \Phi(t; x\_0, t\_0) \le ||x\_0|| + || \int_{t\_0}^{t}f(\Phi(\tau; x\_0, t\_0), \tau)d\tau ||
\end{align}

\begin{align}
||x\_0|| + k \int_{t\_0}^{t}f(\Phi(\tau; x\_0, t\_0), \tau)d\tau
\end{align}

where \\(f(\cdot)\\) obeys the lipschitz condition,

\begin{align}
  ||f(x,t) - f(y,t)|| \le k \, ||x-y||. \nonumber
\end{align}

By the Gronwall-Bellman lemma,

\begin{align}
  ||\Phi(t; x\_0, t\_0) ||  \le [\exp \, k (t - t\_0)] ||x_0 || \nonumber
\end{align}

which is less than \\(\infty \\) for any finite \\((t - t\_0)\\).

<a name="stab"></a>
### **Stability**

My definitions follow from R.E Kalman's 1960 seminal paper since they are clearer to understand compared to the myriad of definitions that exist in many texts today. **Stability concerns the deviation about some fixed motion**. So, we will be considering the deviations from the equilibrium state \\(x\_e\\) of a free dynamic system.

Simply put, here is how Kalman defines stability, if \eqref{eq:diff_eq} is slightly perturbed from its equilibrium state at the origin, all subsequent motions remain in a correspondingly small neighborhood of the origin. Harmonic oscillators are a good example of this kind of stability. **Lyapunov** himself defines stability like so:

+ An equilibrium state \\(x\_e\\) of a free dynamic system is _stable_ i.e. for every real number \\(\epsilon>0\\), there exists a real number \\(\delta(\epsilon, t\_0)>0\\) such that \\(\|x\_0 - x\_e\| \le \delta \\) implies

\begin{align}
  ||\Phi(t; x\_0, t\_0) - x\_e|| \le \epsilon \quad \forall \quad t \ge t\_0 \nonumber
\end{align}

This is best imagined from the figure below:


<div class="fig figcenter fighighlight">
  <img src="/assets/control/stability.png" width="100%" height="450" align="middle">  
  <div class="figcaption" align="middle">Fig. 1. The basic concept of stability. Courtesy of R.E. Kalman
  </div>
</div>

Put differently, the system trajectory can be kept arbitrarily close to the origin/equilibrioum if we start the trajectory sufficiently close to it. If there is stability at some initial time, \\(t\_0\\), there is stability for any other initial time \\(t\_1\\), provided that all motions are continuous in the initial state.

+ Asymptotic stability: The requirement that we start sufficiently close to the origin and stay in the neighborhood of the origin is a rather limiting one in most practical engineering applications. We would want to require that our motion should return to equilibrium after any small perturbation. Thus, the classical definition of Lyapunov stability is
  + an equilibrium state \\(x\_e\\) of a free dynamic system is _**asymptotically stable**_ if
    - it is stable; and
    - every motion starting sufficiently near \\(x\_e\\) converges to \\(x\_e\\) as \\(t \rightarrow \infty\\).

  +  Put differently, there is some real constant \\(r(t\_0)>0\\) and to every real number
  \\(\mu > 0\\) there corresponds a real number \\(T(\mu, x\_0, t\_0)\\) such that \\(||x\_0 - x\_e|| \le r(t\_0)\\) implies

  \begin{align}
    \||\Phi(T; x\_0, t\_0)\|| \le \mu \quad \forall \quad t \ge t\_0 + T \nonumber
  \end{align}


  <div class="fig figcenter fighighlight">
    <img src="/assets/control/asymptotic_stability.png" width="80%" height="350" align="middle">  
    <div class="figcaption" align="left">Fig. 2. Definition of asymptotic stability. Courtesy of R.E. Kalman
    </div>
  </div>

Asymptotic stability is also a local concept since we do not know aforetime how small \\(r(t\_0)\\) should be. For motions starting at the same distance from \\(x\_e\\), none will remain at a larger distance than \\(\mu\\) from \\(x\\) at arbitrarily large values of time. Or to use Massera's definition:

+ An equilibrium state \\(x\_e\\) of a free dynamic system is _**equiasymptotically stable**_ if
  - it is stable
  - every motion starting sufficiently near \\(x\_e\\) converges to \\(x\\), as \\(t \rightarrow \infty\\) uniformly in \\(x\_0\\)

**Interrelations between stability concepts**

This I gleaned from Kalman's 1960 paper on the second method of Lyapunov.

  <div class="fig figcenter fighighlight">
    <img src="/assets/control/control_concepts.png" width="100%" height="450" align="middle">  
    <div class="figcaption" align="middle">Fig. 3. Interrelations between stability concepts. Courtesy of R.E. Kalman
    </div>
  </div>

+ For _linear systems_, stability is independent of the distance of the initial state from \\(x\_e\\). Nicely defined as such:
    - an equilibrium state \\(x\_e\\) of a free dynamic system is _asymptotically (equiasymptotically) stable in the large_ if
    (i) it is stable

    (ii) every motion converges to \\(x\_e\\) as \\(t \rightarrow \infty \\), i.e., every motion converges to \\(x\_e\\), uniformluy in \\(x_0\\) for \\(x\_0 \le r\\), where \\(r\\) is fixed but arbitrarily large



<a name="CBFs"></a>
### **Control Barrier Functions**

For the nonlinear control affine function,

\begin{align}
    \dot{\boldsymbol{x}} = \boldsymbol{f}(\boldsymbol{x}) + \boldsymbol{g}(\boldsymbol{x})\boldsymbol{u}
    \label{eq:cbfs::control_affine}
\end{align}

where \\(\boldsymbol{x} \in \mathbb{R}^n\\), \\(\boldsymbol{u} \in \mathbb{R}^m\\), and \\(\boldsymbol{f}: \mathbb{R}^n \rightarrow \mathbb{R}^n\\), and \\(\boldsymbol{g}: \mathbb{R}^n \rightarrow \mathbb{R}^n \times \mathbb{R}^m\\) are locally Lipschitz functions, with continuity on \\(\mathbb{R}^n\\). For a Lipschitz continuous state feedback \\(\boldsymbol{k}: \mathbb{R}^n \rightarrow \mathbb{R}^m\\), we can write the closed-loop system dynamics as 

\begin{align}
    \dot{\boldsymbol{x}} = \boldsymbol{f}_{cl} \triangleq \boldsymbol{f}(\boldsymbol{x}) + \boldsymbol{g}(\boldsymbol{x})\boldsymbol{k}(\boldsymbol{x}).
    \label{eq:cbf::closed_loop}
\end{align}

whereupon the locally Lipschitz continuous property  of \\(\boldsymbol{f}, \boldsymbol{g} \\), and  \\(\boldsymbol{k}\\) implies that \\( \boldsymbol{f}\_{cl} \\) takes the local Lipzchitz continuity property. Thus, for any initial condition \\(\boldsymbol{x}\_0: \boldsymbol{x}(0) \in \mathbb{R}^n\\), we must have a maximum time interval \\(I(\boldsymbol{x}\_0) = [0, t\_{max})\\)  such that \\(\boldsymbol{x}(t)\\) is the solution of \eqref{eq:cbf::closed_loop} on \\(I(\boldsymbol{x}(0))\\). Here, \\(\boldsymbol{f}_{cl}\\) is forward complete, \\(t\_{max} = \infty\\).


<a name="Invariance"></a>
#### **Safe Sets, and Invariance**

Safety with CBFs are in general realized with the notion of safe sets within the state space that the system must remain in order for it to be considered safe. 

We define a zero-superlevel set \\(\mathcal{C} \subset \mathbb{R}^n\\) of a continuously differentiable function \\(h: \mathbb{R}^n \rightarrow \mathbb{R}\\), i.e.

\begin{align}
  \mathcal{C} = \\{ \boldsymbol{x} \in \mathbb{R}^n: h(x) \ge 0 \\},
\end{align}

such that on the boundary of the superlevel set, \\(\partial \mathcal{C} \triangleq \\{ \boldsymbol{x} \in \mathbb{R}^n: h(x) = 0 \\} \\); and in the interior of the \\(0\\)-superlevel set, we have \\(Int (\mathcal{C}) \triangleq \\{ \boldsymbol{x} \in \mathbb{R}^n: h(x) > 0 \\} \\). It is generally assumed that \\(\mathcal{C}\\) is nonempty (\i.e. \\(\mathcal{C} \neq \emptyset \\)) and it contains no isolated points, (i.e. \\(Int (\mathcal{C}) = \mathcal{C}\\)).  **\\(\mathcal{C}\\) defines the safe set.** Let us now define the concept of forward invariance and safety:

<a name="safety"></a>
#### **Forward Invariance and Safety**

A set \\(\mathcal{C} \subset \mathbb{R}^n \\) is said to be **forward invariant** if for every \\(\boldsymbol{x}\_0 \in \mathcal{C}\\), the solution \\(\boldsymbol{x}(t)\\) of \eqref{eq:cbf::closed_loop} satisfies \\(\boldsymbol{x}(t) \subset \mathcal{C}\\) for all \\(t \in I(\boldsymbol{x\_0}\\). The system in \eqref{eq:cbf::closed_loop} is said to be **safe** if it exists on the \\(0\\)-superlevel set \\(\mathcal{C}\\) such that the set \\(\mathcal{C}\\) is forward invariant.

<a name="class-kappa"></a>
#### **Digression: Class \\(\mathcal{K}\\) functions**

Here, I give a few background definitions that will enable us to define control barrier functions adequately.

+ **Class \\(\mathcal{K}\\) Function**: Supose we have a continuous function \\(\alpha: [0, a) \rightarrow \mathbb{R}\_+\\), where \\(a>0\\), we say \\(\alpha\\) is a **_class \\(\mathcal{K}\\) (\\(\alpha \in \mathcal{K}\\))_** function if \\(\alpha(0) = 0\\) and \\(\alpha\\) is strictly monotonically increasing.

+ **Class \\(\mathcal{K}\_\infty\\) Function**: Supose we have a continuous function \\(\alpha: [0, a) \rightarrow \mathbb{R}\_+, a = \infty\\), we say \\(\alpha\\) is a **_class \\(\mathcal{K}\_\infty \, (\alpha \in \mathcal{K}\_\infty\\))_** function if \\(\alpha(0) = 0\\) and \\(\lim\_{r\rightarrow \infty}\alpha(r)=\infty\\) is strictly monotonically increasing.

+ **Extended class \\(\mathcal{K}\\)**: A continuous function \\(\alpha: (-b, a) \rightarrow \mathbb{R} \\) with \\(a, b > 0\\), belongs to the _**extended class**_ \\(\mathcal{K}\\) (\\(\alpha \in \mathcal{K}\_e\\) ) if \\(\alpha(0) = 0\\) and \\(\alpha\\) is strictly monotonically increasing. 

+ **Extended class \\(\mathcal{K}\_\infty\\)**: If \\(a, b = \infty, \, \lim\_{r\rightarrow -\infty} \alpha(r) = -\infty\\),  and \\(\lim_{r\rightarrow \infty} \alpha(r) = \infty \\), then \\(\alpha\\)  is said to belong to an _**extended class**_  \\(\mathcal{K}\_\infty (\alpha \in  \mathcal{K}\_{\infty, e}). \\) 



 <div class="fig figcenter fighighlight">
        <img src="/assets/control/class-kappa.jpg" width="100%" height="450" align="middle">  
        <div class="figcaption" align="middle">Fig. 4.  Naive Representation of Class Kappa functions. For CBFs, we are generally interested in the class-kappa infinity-extended functions.
        </div>
      </div>

<a name="cbf-proper"></a>
### **Control Barrier Functions**

Now that we have an understanding of the prerequisites, we can give a statement that describes CBFs

Suppose that \\(\mathcal{C} \subset \mathbb{R}^n\\) is a \\(0\\)-superlevel set of a continuously differentiable function \\(h: \mathbb{R}^n \rightarrow \mathbb{R} \\) with \\(0\\) a regular value. The function \\(h\\) is a **control barrier function** for \eqref{eq:cbfs::control_affine} on the superlevel set \\(\mathcal{C}\\) if there exists \\(\alpha \in \mathcal{K}\_{\infty,e}\\) such that for all \\(\boldsymbol{x} \in \mathbb{R}^n\\), we have

\begin{align}
  \sup\_{\boldsymbol{u} \in \mathbb{R}^m} \dot{h}(\boldsymbol{x}, \boldsymbol{u}) &\triangleq \nabla h(\boldsymbol{x}) (\boldsymbol{f}(\boldsymbol{x}) + \boldsymbol{g}(\boldsymbol{x})) 
  &= \boldsymbol{L_f} h(\boldsymbol(x)) + \boldsymbol{L_g} h(\boldsymbol(x)) \boldsymbol{u} \ge -\alpha(h(\boldsymbol{x}))
  %
  \label{eq:cbfs::cbf-def}
\end{align}
%
with \\(\boldsymbol{L_f} h(\boldsymbol(x))\\) and \\(\boldsymbol{L_g} h(\boldsymbol(x))\\) being [Lie derivatives](https://en.wikipedia.org/wiki/Lie_derivative).

It follows that for a CBF \\(h\\) for system \eqref{eq:cbfs::control_affine} and an \\(\alpha \in \mathcal{K}\_{\infty, e}\\), the point-wise set of all control values that satisfies \eqref{eq:cbfs::cbf-def} is given by,

\begin{align}
  K_{cbf}(\boldsymbol{x}) \triangleq \\{ \boldsymbol{u} \in \mathbb{R}^m  | \dot{h}(\boldsymbol{x, u}) \ge -\alpha(h(\boldsymbol{x}))
  \\}.
\end{align}

### **Optimization-based Control** 

The question of unifying optimality in a control theoretical sense with stability guarantees such as the ones that Lyapunov analyses provide is a fascinating one. The beauty of CBFs is that we can elegantly write out our feedback control term for a control affine system dynamics such that we can create a safety-critical controller, as provided by the bound of the class-\\(\mathcal{K}\_{\infty, e}\\) in the definition of our CBF as given earlier as follows:

Oh, by the way, CBFs provide necessary and sufficient conditions on safety. I may flesh this out in a future post in the future. But for kicks, you may have a look at this hot damn paper: [A. D. Ames, X. Xu, J. W. Grizzle and P. Tabuada, "Control Barrier Function Based Quadratic Programs for Safety Critical Systems," in IEEE Transactions on Automatic Control, vol. 62, no. 8, pp. 3861-3876, Aug. 2017, doi: 10.1109/TAC.2016.2638961.](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=7782377).

**Safety-Critical Control**

[To be continued]


Last updated: May 31, 2021
