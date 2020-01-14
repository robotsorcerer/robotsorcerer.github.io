---
layout: default
title: Lekan
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
<h4><a href="/blog">View all blog posts </a></h4>
<br>

<!-- Side projects  -->
 <h2><i class="fa fa-chevron-right"></i><i class="fa fa-chevron-right"></i> Side Projects</h2>
<!--  <p>At leisure, I like to read: research papers, history books, and engineering texts inter alia. Highlighted below are some of my reading lists in the past, or codes you might find useful.</p> -->

+ <a href="https://github.com/lakehanne/screws" target="blank"> screw theory and elastic deformations: </a> screws (in mathematica and matlab) applied to continuum dynamics, codes and  examples.
+ <a href="https://github.com/lakehanne/gps" target="blank">gps</a>: a re-implementation of Levine et al's guided policy search algorithm in ros indigo.
+ <a href="https://github.com/lakehanne/ensenso" target="blank">ensenso</a>: ros and point cloud library bridges to the <a href="https://www.ensenso.com/" target="blank">ensenso 3D N35 camera factory api</a>.
+ <a href="https://github.com/lakehanne/awesome-screw-theory" target="blank"> awesome screw theory</a>: a curated list of papers that apply screw theory for soft and rigid robots control.
+ <a href="https://github.com/lakehanne/awesome-neurocontrol" target="blank">awesome neuro-control</a>: a curated list of papers that apply neural dynamics to control systems.
+ <a href="https://github.com/lakehanne/shells.git" target="blank"> bourne again shells</a>: short & fun bash scripts.
+ <a href="https://github.com/lakehanne/Savitzky-Golay" target="blank">savgol</a>: a c++11 implementation of the vandermonde matrix as well as savityzky-golay differentiation filter and smoothing coefficients.
+ <a href="https://github.com/lakehanne/keyence" target="blank">keyence</a>: basic api in c and c++ for streaming sensed data from the <a href="https://www.keyence.com/landing/measure/lp_blp_ljv_1079.jsp?aw=google-kaenLJ213101bb-br&k_clickid=0b5a6233-6a63-4e33-9721-b8207086947a&gclid=CjwKCAjwo9rtBRAdEiwA_WXcFvZDgBqvXU8-yPeZJrXOrhdXY-t-cM62PvMffbMwAmovJDj-uPjSIhoCyAEQAvD_BwE" target="blank">keyence LJV-7300 line scanner</a>.
+ <a href="/chemrob" target="blank"> the chemistry of robotics:</a> ideas and tips for cooking things up out of various chemical compounds in order to create useful elastomers for your soft robot components.
+ <a href="/downloads/fb" target="blank"> data structure commons</a>: a collection of solutions to interesting software engineering questions. <a href="https://github.com/lakehanne/SWEngr">source code.</a> 
+ <a href="https://github.com/lakehanne/gocator" target="blank">gocator</a>: ros and point cloud library bridges to the <a href="https://lmi3d.com/products/gocator-3D-smart-sensors" target="blank"> LMI gocator line scanning sensor</a>.
+ <a href="{{ site.url }}/readlist"> reading list</a>:  a collection of papers I am currently reading/implementing.
+    <a href="/downloads/save_dijs" target="blank">radiation therapy dose influence matrices </a>: extracting fluence based on the varian medical systems c#/python api from eclipse. core api courtesy of mike folkerts over at UCSD/UTSW/Varian. 
<!-- + <a href="{{ site.url }}/scholternships"> advice for fellowships, internships, conference grants applications</a> -->
+ <a href="{{ site.url }}/readlist18" target="blank"> summer'18 reading list</a>:  Bellman and Optimal Control.

<!-- Strava summary -->
<h2><i class="fa fa-chevron-right"></i><i class="fa fa-chevron-right"></i>Strava Activities Summary</h2>
<!-- <p><b>News:</b><i> Come next Summer, I will be participating in the <a href="https://www.greenway.org/new-york-to-philadelphia-greenway-ride?fbclid=IwAR3lxRjYiwy0hL1mVJJ8QZ7GnN5zKJge4O1pcNq9GwkpthQe8tXO2y3bPxY">NYC-to-Philly Greenway Ride</a> together with cyclists from all over the United States and France in a 130-mile ride over two days, starting from Manhattan, through Princeton, and ending in Philadelphia. As part of my contribution to green travel, I ask that if you are able, to please consider donating in my name on the following <a href="https://www.greenway.org/new-york-to-philadelphia-greenway-ride?fbclid=IwAR3lxRjYiwy0hL1mVJJ8QZ7GnN5zKJge4O1pcNq9GwkpthQe8tXO2y3bPxY">webpage.</a></i> 
</p> -->

<p>Regular mortal on two wheels here. As often as I can get away from the lab, I like to pedal the metals of my bike, often logging approximately 120 miles a week -- during cycling season. I ride rain or shine, hell or highwater -- in the parching heats of sultry Texas, or the blustering cold winds of the  Midwest and the Eastern Seaboard. If you are in my area and would love to tag along on a ride, do not hesitate to shoot me an email. Upcoming Gran-Fondos that I have on my calendar include a return trip to Atlantic City from Philadelphia with friends from Penn Medicine and Penn Engineering; in the summer, together with other athletes from Chicago, California and France, we are riding the East Coast Greenway Alliance's inaugural NYC-to-Philly 130 mile route. 

States where I have ridden so far include Texas, Illinois, Wisconsin, Indiana, Pennsylvania, Delaware and New Jersey. Below is a screenshot of my recent activities summary. </p>
  <iframe height='160' width='400' frameborder='0' allowtransparency='true' scrolling='no' src='https://www.strava.com/athletes/29996478/activity-summary/a1ced5c81ee2203640950cbaf24d5fb53d84bafb'></iframe>



<br><br>
Last updated on {% include last-updated.txt %}
