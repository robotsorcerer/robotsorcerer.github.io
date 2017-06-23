---
layout: default
title: Lekan Ogunmolu
---

<div class="col-md-2 vcenter idxHdr">
  <a href="/downloads/me-style.jpg">
    <!-- <img src="/downloads/me-style.jpg" alt="Me" align="left" style="width:100px;height:100px;">  -->
   </a>
  <!-- -->
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

## <i class="fa fa-chevron-right"></i> Side Projects
+ [EE/ML conference tracker](https://github.com/lakehanne/conference-tracker).
+ [Awesome Neuro-Control](https://github.com/lakehanne/awesome-neurocontrol):
  A curated list of papers that apply neural dynamics to control systems.
+ [Research Group Resources](https://github.com/lakehanne/research-group-resources):
  Borrowed from Jean Yang.
+ [My summer reading list]( {{ site.url }}/readlist/):
  Hosted on GitHub pages.
+ [bash-scripts](https://github.com/lakehanne/shells.git):
  Short and fun bash scripts.
+ [This website](https://github.com/lakehanne/lakehanne.github.io):
  Built with Jekyll and hosted on GitHub pages.
+ [Applying to fellowships, internships, conference grants]( {{ site.url }}/scholternships)

---

Last updated on {% include last-updated.txt %}
