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
+ <a href="/SWEngr" target="blank"> data structure commons</a>: my solutions (in python) to a collection of interesting software engineering questions at the FAANG. <a href="">source code.</a> 
+ <a href="https://github.com/lakehanne/ensenso" target="blank">ensenso</a>: ros and point cloud library bridges to the <a href="https://www.ensenso.com/" target="blank">ensenso 3D N35 camera factory api</a>.
+ <a href="https://github.com/lakehanne/awesome-screw-theory" target="blank"> awesome screw theory</a>: a curated list of papers that apply screw theory for soft and rigid robots control.
+ <a href="https://github.com/lakehanne/awesome-neurocontrol" target="blank">awesome neuro-control</a>: a curated list of papers that apply neural dynamics to control systems.
+ <a href="https://github.com/lakehanne/shells.git" target="blank"> bourne again shells</a>: short & fun bash scripts.
+ <a href="https://github.com/lakehanne/Savitzky-Golay" target="blank">savgol</a>: a c++11 implementation of the vandermonde matrix as well as savityzky-golay differentiation filter and smoothing coefficients.
+ <a href="https://github.com/lakehanne/keyence" target="blank">keyence</a>: basic api in c and c++ for streaming sensed data from the <a href="https://www.keyence.com/landing/measure/lp_blp_ljv_1079.jsp?aw=google-kaenLJ213101bb-br&k_clickid=0b5a6233-6a63-4e33-9721-b8207086947a&gclid=CjwKCAjwo9rtBRAdEiwA_WXcFvZDgBqvXU8-yPeZJrXOrhdXY-t-cM62PvMffbMwAmovJDj-uPjSIhoCyAEQAvD_BwE" target="blank">keyence LJV-7300 line scanners factory api</a>.
+ <a href="/chemrob" target="blank"> the chemistry of robotics:</a> ideas and tips for mixing sh#t up out of various chemical compounds in order to create useful elastomers for your soft robot components.
+ <a href="https://github.com/lakehanne/gocator" target="blank">gocator</a>: ros and point cloud library bridges to the <a href="https://lmi3d.com/products/gocator-3D-smart-sensors" target="blank"> LMI gocator line scanning sensor factory api</a>.
+ <a href="{{ site.url }}/readlist"> reading list</a>:  a collection of papers I am currently reading/implementing.
+    <a href="/downloads/save_dijs" target="blank">radiation therapy dose influence matrices </a>: extracting fluence based on the varian medical systems c#/python api from eclipse. core api courtesy of mike folkerts over at UCSD/UTSW/Varian. 
<!-- + <a href="{{ site.url }}/scholternships"> advice for fellowships, internships, conference grants applications</a> -->
+ <a href="{{ site.url }}/readlist18" target="blank"> summer'18 reading list</a>:  Bellman and Optimal Control.

<!-- Strava summary -->
<h2><i class="fa fa-chevron-right"></i><i class="fa fa-chevron-right"></i>Strava Activities Summary</h2>
<p>Regular mortal on two wheels hoping to someday be a world champ here. As often as I can get away from the lab, I like to pedal the metals of my bike, often logging approximately 120 miles a week during cycling season (riding rain or shine, hell or highwater during the cycling season). I ride in the parching heats of sultry Texas, the blustering cold winds of the  Midwest and the Eastern Seaboard. In the winter, I get sloppy with my usual ride schedule and pile on more fat :-). 
<!--   I own a 62cm  2018 <a href="https://www.trekbikes.com/us/en_US/us/en_US/bikes/road-bikes/performance-road-bikes/domane/domane-al/domane-al-3/p/23526/">TREK Domane AL3</a> road bike.  -->
  States where I have ridden so far include Texas, Illinois, Wisconsin, Indiana, Pennsylvania, Delaware and New Jersey. Below is a screenshot of my recent activities summary. Feel free to follow me on Strava as I pursue <i>life, liberty and the trails!</i></p>
  <iframe height='160' width='400' frameborder='0' allowtransparency='true' scrolling='no' src='https://www.strava.com/athletes/29996478/activity-summary/a1ced5c81ee2203640950cbaf24d5fb53d84bafb'></iframe>


<br><br>
Last updated on {% include last-updated.txt %}
