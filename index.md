---
layout: default
title: Lekan O'Molu
---

<div class="col-md-2 vcenter idxHdr">
  <a href="/downloads/me-style.jpg">
    <!-- <img src="/downloads/me-style.jpg" alt="Me" align="left" style="width:100px;height:100px;">  -->
   </a>
  <!-- -->
</div>

<br>
{% include cv.md %}

 <h2><i class="fa fa-chevron-right"></i>Recent Blog Posts</h2>

<table class="table table-hover">
  {% for post in site.posts limit: 3 %}
    {% unless post.draft %}
    <tr>
      <td><a href="{{ post.url }}">{{ post.title }}</a></td>
      <td class="col-md-3" style="text-align: right;">{{ post.date | date: "%B %e, %Y" }}</td>
    </tr>
    {% endunless %}
  {% endfor %}
</table>
<h4><a href="/blog">View all</a></h4>

 <h2><i class="fa fa-chevron-right"></i> Side Projects</h2>
+    <a href="https://github.com/lakehanne/awesome-neurocontrol">awesome neuro-control</a>: A curated list of papers that apply neural dynamics to control systems.<br>

+ <a href="https://github.com/lakehanne/awesome-screw-theory"> awesome screw theory</a>: A curated list of papers that apply screw theory for soft and rigid robots control.<br>

+ <a href="{{ site.url }}/scholternships"> advice for fellowships, internships, conference grants applications</a><br>
+ <a href="{{ site.url }}/readlist18"> summer'18 reading list</a>:  Bellman and Optimal Control<br>
+ <a href="{{ site.url }}/readlist"> summer'17 reading list</a>:  RAS Papers<br>
+ <a href="https://github.com/lakehanne/shells.git"> bash-scripts</a>:   Short and fun bash scripts.<br>
+ <a href="https://github.com/lakehanne/conference-tracker"> control/robotics/ai conference tracker</a><br>
+ <a href="https://github.com/lakehanne/research-group-resources">research group resources</a>:  Borrowed from Jean Yang.

<br><br>
---<br>
Last updated on {% include last-updated.txt %}
