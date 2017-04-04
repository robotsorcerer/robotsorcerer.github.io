---
layout: post
date: 2017-04-03 19:25:00
title: "<center>Adaptive Control Notes</center>"
excerpt: "<center>Adaptive systems are inherently nonlinear. Their behavior therefore is quite complex, which makes them difficult to analyze. Progress in theory has been slow, and much work remains before a reasonably complete, coherent theory is available. <br>-- Karl Astrom</center>"
permalink: Adaptive-Control-Notes
comments: true
mathjax: true
---

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
  TeX: { equationNumbers: { autoNumber: "AMS" } }
});
</script>

<!--Mathjax Parser -->
<script type="text/javascript" async
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-MML-AM_CHTML">
</script>

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
  tex2jax: {inlineMath: [['$','$'], ['\\(','\\)']]}
});
</script>

### [Table of Contents](#table-of-contents):

  - [Introduction](#introduction)
  - [Feedback Linearization](#feedback-linearization)    
<!--    - [Array decays to a pointer](#array-decays-to-a-pointer)    
    - [Atoi Implementation](#atoi-implementation)
    - [Reversing a string](#reverse-a-string)
    - [Const Iterator on a vector dynamic set](#const-iterator)
    - [Unordered Map](#unordered-map)
    - [Matrix Multiply](#matrix-multiply)
  - [Sorting](#sorting)
    - [Insert-Sort (2.1-1)](#insert-sort)
    - [Insert-Sort in Descending Order (2.1-2)](#insert-sort-in-descending-order)
    - [LineSearch (2.1-3)](#lineSearch)
    - [Merge-Sort (2.3-1)](#merge-sort)
    - [HeapSort](#heapsort)
    - [QuickSort](#quicksort)
    - [Randomized-QuickSort](#randomized-quicksort)
  - [Data Structures](#data-structures)
    - [Queues](#queue)
    - [Stack](#stack)
    - [Minimum/Maximum value in an array](#min)
    - [Simulatneous minimum and maximum in an array](#Simulatneous-min-and-max)
    - [Deque](#Deque)
    - [Array-based List](#list-array)
    - [Singly-Linked List](#singly-linked-list)
    - [Doubly-Linked List](#doubly-linked-list) 
    - [Binary Search Tree](#binary-tree)    -->

## Notes updated sporadically at best. Bear my typos. Bite the meat not the language.

<a name='introduction'></a>
## `Introduction`

The motivation for adaptive control was from systems whose parameters varied with time. Adaptive control can deal with any size of parametric uncertainty as well as dynamic uncertainites arising from neglected dynamics if the correct robust algorithms are used. The bounds for the allowable dynamic uncertainites cannot be calculated as easily as in the nonadaptive case because of the nonlinear nature of the adaptive system coupled with the fact that the plant parameters are deemed unknown. 

Note:

- Adaptive Control designed for LTI plants give rise to a closed-loop system that is nonlinear. 

- As a result, poles, zeros, gain and phase margins make little sense.

- Nonlinear techniques based on Lyapunov analysis and passivity arguments plus linear systems theory are used in establishing the stability/robustness and margins that are not so easy to compute as in the LTI case.

- LTI methods can be used in understanding the dynamics of robust modification laws to adaptive systems e.g. dynamic normalizing signal that limits the rate of adaptation to be finite and small relative to level of dynamic uncertainty.

- The limitating of estimated controller parameters to assume large values eliminates the possibility of high gain control

- High gain or high speed control can increase instability due to high bandwidth that the controller is subjected to.

The extension of adaptive control to linear time-varying parameters was a major obstacle until the 80s when basic robustness questions were answered. Tactics such as dead-zone modification, dynamic normalizing signal together with leakage or parameter projection were used to deal with a great deal of parameter variations. This class included slowly-varying parameters as well as infrequent jumps in parameter values. In several cases, the error from time-varying signals can be reduced through proper parameterizations of the time-varying plant model used in the control design. In the linear time-varying case, stability margins, bandwidth margins, bandwidth, frequency domain characteristics, poles, zeros do not make much sense even for time-varying parameters unless approximations are made using the assumption of slowly varying parameters, etc.

Adaptive control applied to nonlinear systems is its infancy. Why is this?
In nonlinear systems, it is not only the parameters that are nonlinear, but also the functions. Adaptive control was designed to stabilize while adapting for nonlinear parameters  and not nonlinear functions. The extension of adaptive controllers to nonlinear systems from LTI and LTV systems is therefore a complicated one. There are two general cases of adopting adaptive control to nonlinear systems: (i) nonlinear systems whose nonlinear functions are known but unknown parameters appear linearly. (ii) the nonlinear functions are assumed known by multiplying nonlinear basis functions with unknown parameters to be determined. The basis functions are typically from neural networks and they are assumed to appear linearly e.g. in a single layer. This property is fundamental to developing analytical stability results with large regions of attraction.

<a name='feedback-linearization'></a>
### Feedback Linearization

Feedback linearization consists in changing the coordinates of a system so as to cancel all or most of the unknown nonlinear terms so that the system behaves as a linear or partly linear system. Consider the following system

\begin{align}
  \dot{x} = f(x) + g(x)u, \nonumber \\
  y = h(x)
  \label{eq:nlnr1}
\end{align}

where \\(x \in \mathbb{R}^n, u,y \in \mathbb{R} \text{ and } f,g,h, \\) are smooth nonlinear functions.

Differentiating \\(y\\) in \eqref{eq:nlnr1} with respect to time, we find that

\begin{align}
\dot{y} = \dfrac{\partial{h}}{\partial{x}}(x) f(x) +     \dfrac{\partial{h}}{\partial{x}}(x) g(x) u,
\label{eq:ydot}
\end{align}

where

\begin{align}
\dfrac{\partial{h}}{\partial{x}}(x) f = \dfrac{\partial{h}}{\partial{x}_1}(x) f_1 + \cdots + \dfrac{\partial{h}}{\partial{x}_n}(x) f_n \triangleq L_f \, f
\label{eq:Lie}
\end{align}

where \\(L_f f\\) is the <i>Lie derivative</i>. If \\(\frac{\partial{h}}{\partial{x}}(x_0) \, g(x_0) \neq 0\\) at some point \\(x_0\\), then the system of \eqref{eq:nlnr1} is said to be of relative degree 1 at \\(x_0\\). For an LTI system, this means the output is different from the input by one integrator only. This would be a strictly proper tranfer function. A good way of thinking about this is that the output has to be differentiated by the number of the relative degree(s) until the input appears in the output expression. 

If \\(\frac{\partial{h}}{\partial{x}}(x) \, g(x) = 0 \forall x \in B_x_0 \text{ of } x_0 \\), then one can take the second derivatiove of \\(y\\) to obtain (abusing notation an d dropping the parentheses terms,

\begin{align}
\ddot{y} = \dfrac{\partial}{\partial{x}} \left(\dfrac{\partial{h}}{\partial{x}}f\right)f + \dfrac{\partial}{\partial{x}}\left(\dfrac{\partial{h}}{\partial{x}}f\right) g \, u.
\end{align}

If \\(\frac{\partial}{\partial{x}} \left(\frac{\partial{h}}{\partial{x}}(x)f(x)\right)g(x) \, |_{x = x_0} \neq 0\\) then \eqref{eq:nlnr1} is said to have a relative degree 2 at \\(x_0\\). We can continue the differentiation in a neighborhood of \\(x_0\\) if \\(\frac{\partial}{\partial{x}} \left(\frac{\partial{h}}{\partial{x}}(x)f(x)\right)g(x) = 0\\) in the neighborhood of \\(x_0\\). 

More generally, 

\begin{align}
L_f^i h = \dfrac{\partial}{\partial{x}}\left(\dfrac{\partial}{\partial{x}} \cdot \dfrac{\partial}{\partial{x}} \left(\dfrac{\partial{h}}{\partial{x}}f\right) \Cdot f \cdots \right) \Cdot f \right) \Cdot f.
\end{align}
