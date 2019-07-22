---
layout: default
title: Lekan O'Molu
---

<div class="col-md-2 vcenter idxHdr">
  <a href="/downloads/me-style.jpg">
   </a>
  <!-- -->
</div>

<br>
{% include cv.md %}
<br>

<h2><i class="fa fa-chevron-right"></i><i class="fa fa-chevron-right"></i>Recent Blog Posts</h2>

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
<h4><a href="/blog">View all blogposts </a></h4>
<br>

<h2><i class="fa fa-chevron-right"></i><i class="fa fa-chevron-right"></i>Select News</h2>
<table class="table table-hover">
    {% for item in site.data.news.news_items %}
    {% for subitem in item.subnewsitems %} 
        {% unless subitem.highlight == false %}
        <tr>
          <td>{{ subitem.content }} </td>
          <td class="col-md-3" style="text-align: right;">{{ subitem.date | date: "%B %e, %Y" }}</td>
        </tr>
      {% endunless %}
    {% endfor %}
  {% endfor %}
</table> 
<h4><a href="{{ sites }}/news">View archived news</a></h4>
<br>

<!-- Strava summary -->
<h2><i class="fa fa-chevron-right"></i><i class="fa fa-chevron-right"></i>Strava Activities Summary</h2>
<p>I pedal the metal of an unstable bi-pedal locomotor device (aka bike), often logging approximately 120 miles a week, weather permitting. I currently own a 2018 <a href="https://www.trekbikes.com/us/en_US/us/en_US/bikes/road-bikes/performance-road-bikes/domane/domane-al/domane-al-3/p/23526/">TREK Domane AL3</a> road bike (62cm, because why not? I am 6'7" --fyi, this is why not). It has served me well in the states of Texas, Illinois, and Indiana. I hope it serves in Michigan, Wisconsin and Pennsylvania soon. Below are my activities summary on strava.</p>
  <iframe height='200' width='700' frameborder='0' allowtransparency='true' scrolling='no' src='https://www.strava.com/athletes/29996478/activity-summary/a1ced5c81ee2203640950cbaf24d5fb53d84bafb'></iframe>


<!-- Side projects  -->
 <h2><i class="fa fa-chevron-right"></i><i class="fa fa-chevron-right"></i> Side Projects</h2>
 <p>When I am free, I like to read. I read -- a lot! Research papers, history books, engineering junkies and such.</p>
+    <a href="https://github.com/lakehanne/awesome-neurocontrol">awesome neuro-control</a>: A curated list of papers that apply neural dynamics to control systems.<br>

+ <a href="https://github.com/lakehanne/awesome-screw-theory"> awesome screw theory</a>: A curated list of papers that apply screw theory for soft and rigid robots control.<br>

+ <a href="{{ site.url }}/scholternships"> advice for fellowships, internships, conference grants applications</a><br>
+ <a href="{{ site.url }}/readlist18"> summer'18 reading list</a>:  Bellman and Optimal Control<br>
+ <a href="{{ site.url }}/readlist"> summer'17 reading list</a>:  RAS Papers<br>
+ <a href="https://github.com/lakehanne/shells.git"> bash-scripts</a>:   Short and fun bash scripts.<br>
+ <a href="https://github.com/lakehanne/conference-tracker"> control/robotics/ai conference tracker</a><br>
+ <a href="https://github.com/lakehanne/research-group-resources">research group resources</a>:  Borrowed from Jean Yang.


<!-- Strava Extended -->
<h2><i class="fa fa-chevron-right"></i><i class="fa fa-chevron-right"></i>Extended Strava Activities</h2>
<p>Extended display of my recent physical therapy activities on strava</p>
<iframe height='454' width='700' frameborder='0' allowtransparency='true' scrolling='no' src='https://www.strava.com/athletes/29996478/latest-rides/a1ced5c81ee2203640950cbaf24d5fb53d84bafb'></iframe>

<br><br>
Last updated on {% include last-updated.txt %}
