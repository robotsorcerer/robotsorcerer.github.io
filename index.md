---
layout: default
title: Lekan Ogunmolux
---

<div class="col-md-2 vcenter idxHdr">
  <!-- <a href="/downloads/me-style.jpg"> -->
    <!-- <img src="/downloads/me-style.jpg" align="right"
         style="border-radius: 20px; margin: 10px; max-width: none;
         alt="Me."/>
  <!-- </a> --> 
  <img src="/downloads/Pat.jpg" alt="Me" align="right" style="width:100px;height:100px;">
</div>
<br>

{% include cv.md %}

## <i class="fa fa-chevron-right"></i> Recent Blog Posts

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

## <i class="fa fa-chevron-right"></i> Fun Side Projects
+ [EE/ML conference tracker](https://github.com/lakehanne/conference-tracker).
+ [Awesome Neuro-Control](https://github.com/lakehanne/awesome-neurocontrol):
  A curated list of papers that apply neural dynamics to control systems.
+ [Research Group Resources](https://github.com/lakehanne/research-group-resources).
+ [My summer reading list](/readlist-summer17/):
  Hosted on GitHub pages.
+ [bash-scripts](https://github.com/lakehanne/bash):
  Short and fun bash scripts.
+ [This website](https://github.com/lakehanne/lakehanne.github.io):
  Built with Jekyll and hosted on GitHub pages.

---

Last updated on {% include last-updated.txt %}
