---
layout: page
title: "HJ-Gauss: Monte Carlo HJ Reachability"
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

One-stop shop for everything related to **HJ-Gauss**: a Monte Carlo scheme for Hamilton-Jacobi
reachability that replaces the grid with samples, giving $$O(N \cdot n)$$ memory instead of the
usual $$O(M^n)$$ grid blow-up. This page collects the paper, the multi-agent path finding (MAPF)
companion work, both conference slide decks, and the full narrative write-up in one place.

---

<a name="paper"></a>
### Paper: HJ-Gauss — A Monte Carlo HJ Reachability Scheme

**Molu, Renganathan, Cho.** Theory (Cole-Hopf reduction, Picard quasi-linearization, finite-sample
concentration bounds), a 45-dimensional 15-rocket pursuit-evasion game, and a 100,000-bird starling
murmuration — validated against a grid-based reference solver over 30 Monte Carlo seeds.

<a class="btn" href="{{ site.baseurl }}/downloads/Papers/hjgauss.pdf" target="_blank" rel="noopener noreferrer">Download PDF</a>

<div class="pdf-embed-wrap">
  <embed src="{{ site.baseurl }}/downloads/Papers/hjgauss.pdf" type="application/pdf" width="100%" height="700px" />
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

**Code:** <a href="https://github.com/robotsorcerer/levelsetpy/tree/main/monte_carlo" target="_blank" rel="noopener noreferrer">github.com/robotsorcerer/levelsetpy/tree/main/monte_carlo</a>

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
</style>
