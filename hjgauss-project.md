---
layout: page
title: "HJ-Gauss: Sampling-based HJ Reachability"
permalink: hjgauss-project
comments: false
---

<div class="pubs-nav">
  <a href="#paper">Paper</a> &middot;
  <a href="#mapf">MAPF Companion</a> &middot;
  <a href="#slides-full">Full-Exposition Slides</a> &middot;
  <a href="#slides-mapf">MAPF/AMFS Slides</a> &middot;
  <a href="#exposition">Blog Exposition</a>
</div>

One-stop shop for **HJ-Gauss**. The current formulation retains the complete residual of a
generalized Cole--Hopf transformation, giving a semilinear heat equation whose mild form couples
Gaussian initial-condition and nonlinear source integrals. Deterministic field solvers and a
depth-first nonlinear Monte Carlo Picard point evaluator implement complementary forms of this equation. This page collects the paper,
its validation animations, the multi-agent path-finding (MAPF) companion, the slide decks, and the
long-form exposition.

---

<a name="paper"></a>
### Paper: Sampling-based HJ Reachability

**Lekan Molu.** HJ-Gauss transformation theory, deterministic transformed-PDE validation, and
measured nonlinear Monte Carlo Picard point-query scaling. The 100,000-state experiment evaluates
one precomputed reduced field and is not a coupled population solve.

<a class="btn" href="{{ site.baseurl }}/downloads/Papers/hjgauss.pdf" target="_blank" rel="noopener noreferrer">Open the 28-page PDF</a>

<div class="pdf-embed-wrap">
  <embed src="{{ site.baseurl }}/downloads/Papers/hjgauss.pdf" type="application/pdf" width="100%" height="700px" />
</div>

#### Animated numerical comparisons

Each comparison animation advances through the saved horizons as **reference field → transformed
solver → absolute difference**. Select a card to open the GIF.

<div class="hjg-animation-grid">
  <a href="{{ site.baseurl }}/downloads/Papers/assets/anim/roysoc_rockets.gif" target="_blank" rel="noopener noreferrer">
    <img src="{{ site.baseurl }}/downloads/Papers/assets/anim/roysoc_rockets_poster.png" alt="Rockets reference, transformed-solver, and absolute-difference animation poster">
    <span>Rockets</span>
  </a>
  <a href="{{ site.baseurl }}/downloads/Papers/assets/anim/roysoc_dubins.gif" target="_blank" rel="noopener noreferrer">
    <img src="{{ site.baseurl }}/downloads/Papers/assets/anim/roysoc_dubins_poster.png" alt="Dubins-vehicle reference, transformed-solver, and absolute-difference animation poster">
    <span>Dubins vehicles</span>
  </a>
  <a href="{{ site.baseurl }}/downloads/Papers/assets/anim/roysoc_double_integrator.gif" target="_blank" rel="noopener noreferrer">
    <img src="{{ site.baseurl }}/downloads/Papers/assets/anim/roysoc_double_integrator_poster.png" alt="Double-integrator reference, transformed-solver, and absolute-difference animation poster">
    <span>Double integrator</span>
  </a>
  <a href="{{ site.baseurl }}/downloads/Papers/assets/anim/roysoc_murmuration.gif" target="_blank" rel="noopener noreferrer">
    <img src="{{ site.baseurl }}/downloads/Papers/assets/anim/roysoc_murmuration_poster.png" alt="Starling-inspired reference, transformed-solver, and absolute-difference animation poster">
    <span>Starling-inspired geometry</span>
  </a>
  <a href="{{ site.baseurl }}/downloads/Papers/assets/anim/roysoc_colehopf_scaling.gif" target="_blank" rel="noopener noreferrer">
    <img src="{{ site.baseurl }}/downloads/Papers/assets/anim/roysoc_colehopf_scaling_poster.png" alt="Nonlinear Monte Carlo Picard runtime and point-query memory scaling">
    <span>Monte Carlo scaling</span>
  </a>
</div>

---

<a name="mapf"></a>
### Companion: Certified Conflict Prediction for MAPF

Dynamics-aware safety certification for multi-agent path finding (MAPF) on structured floors, plus
a conflict score usable to grade diffusion-based planners.

<a class="btn" href="{{ site.baseurl }}/downloads/Papers/hjgauss_mapf.pdf" target="_blank" rel="noopener noreferrer">Download PDF</a>

<div class="pdf-embed-wrap">
  <embed src="{{ site.baseurl }}/downloads/Papers/hjgauss_mapf.pdf" type="application/pdf" width="100%" height="700px" />
</div>

---

<a name="slides-full"></a>
### Slides: Full Theory & Experiments

The complete conference-style deck: motivation, the $$O(M^n)$$ wall, the Cole-Hopf trick, Picard
quasi-linearization for general Hamiltonians, and the rockets/Dubins/starling results.

<a class="btn" href="{{ site.baseurl }}/downloads/Papers/hjgauss_slides.pdf" target="_blank" rel="noopener noreferrer">Download Slides (PDF)</a>

<div class="pdf-embed-wrap">
  <embed src="{{ site.baseurl }}/downloads/Papers/hjgauss_slides.pdf" type="application/pdf" width="100%" height="700px" />
</div>

---

<a name="slides-mapf"></a>
### Slides: Certified Conflict Prediction for MAPF (AMFS)

Slide deck for the MAPF/AMFS companion work — dynamics-aware conflict certification and its use as
a diffusion-planner scoring signal.

<a class="btn" href="{{ site.baseurl }}/downloads/Papers/hjgauss_mapf_slides.pdf" target="_blank" rel="noopener noreferrer">Download Slides (PDF)</a>

<div class="pdf-embed-wrap">
  <embed src="{{ site.baseurl }}/downloads/Papers/hjgauss_mapf_slides.pdf" type="application/pdf" width="100%" height="700px" />
</div>

---

<a name="exposition"></a>
### Full Blog Exposition

A worked, from-scratch narrative of the theory (with full Cole-Hopf derivation and the finite-sample
concentration proof in the appendices), the actual solver code, and the validated benchmark tables.

<a class="btn" href="{{ site.baseurl }}/hjgauss">Read the full exposition &rarr;</a>

---

**Code:** <a href="https://github.com/robotsorcerer/levelsetpy/tree/main/levelsetpy/cole-hopf" target="_blank" rel="noopener noreferrer">github.com/robotsorcerer/levelsetpy/tree/main/levelsetpy/cole-hopf</a>

<style>
.pdf-embed-wrap { margin: 1em 0 2em 0; border: 1px solid #ddd; }
.pdf-embed-wrap embed { display: block; }
a.btn {
  display: inline-block;
  padding: 0.5em 1.1em;
  margin: 0.5em 0 1em 0;
  background: #2a6496;
  color: #fff !important;
  border-radius: 4px;
  text-decoration: none;
  font-weight: 600;
}
a.btn:hover { background: #1f4c73; }
.hjg-animation-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 1rem;
  margin: 1rem 0 2rem;
}
.hjg-animation-grid a {
  display: block;
  border: 1px solid #d7e5ee;
  border-radius: 8px;
  background: #f7fbfd;
  color: #173b55;
  text-decoration: none;
  overflow: hidden;
  box-shadow: 0 3px 10px rgba(23,59,85,0.08);
}
.hjg-animation-grid img { display: block; width: 100%; height: auto; }
.hjg-animation-grid span { display: block; padding: 0.65rem 0.8rem; font-weight: 700; }
@media (max-width: 640px) { .hjg-animation-grid { grid-template-columns: 1fr; } }
</style>
