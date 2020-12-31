---
layout: default
title: Lekan
---

<div class="col-md-2 vcenter idxHdr">
  <a href="/downloads/me-style.jpg">
   </a>
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

 <h2><i class="fa fa-chevron-right"></i><i class="fa fa-chevron-right"></i> Side Projects</h2>

+ <a href="https://github.com/lakehanne/screws" target="blank"> Screw theory and elastic deformations: </a> Screws (in Mathematica and Matlab) applied to continuum dynamics. Codes and  examples.
+ <a href="https://github.com/lakehanne/gps" target="blank">GPS</a>: A re-implementation of Levine et al's guided policy search algorithm in ROS indigo.
+ <a href="https://github.com/lakehanne/ensenso" target="blank">Ensenso</a>: ROS and point cloud library bridges to the <a href="https://www.ensenso.com/" target="blank">Ensenso 3D N35 camera factory api</a>.
+ <a href="https://github.com/lakehanne/awesome-screw-theory" target="blank"> Awesome Screw Theory</a>: A curated list of papers that apply screw theory for soft and rigid robots control.
+ <a href="https://github.com/lakehanne/awesome-neurocontrol" target="blank">Awesome Neuro-Control</a>: A curated list of papers that apply neural dynamics to control systems.
+ <a href="https://github.com/lakehanne/shells.git" target="blank"> Bourne Again Shells</a>: Short & fun bash scripts.
+ <a href="https://github.com/lakehanne/Savitzky-Golay" target="blank">SAVGOL</a>: A c++11 implementation of the vandermonde matrix as well as savityzky-golay differentiation filter and smoothing coefficients.
+ <a href="https://github.com/lakehanne/keyence" target="blank">Keyence</a>: Basic api in c and c++ for streaming sensed data from the <a href="https://www.keyence.com/landing/measure/lp_blp_ljv_1079.jsp?aw=google-kaenLJ213101bb-br&k_clickid=0b5a6233-6a63-4e33-9721-b8207086947a&gclid=CjwKCAjwo9rtBRAdEiwA_WXcFvZDgBqvXU8-yPeZJrXOrhdXY-t-cM62PvMffbMwAmovJDj-uPjSIhoCyAEQAvD_BwE" target="blank">Keyence LJV-7300 line scanner</a>.
+ <a href="/chemrob" target="blank"> Chemistry of robotics:</a> Creating useful elastomers for your soft robotic components.
<!-- + <a href="/downloads/fb" target="blank"> data structure commons</a>: a collection of solutions to interesting software engineering questions. <a href="https://github.com/lakehanne/SWEngr">source code.</a>  -->
+ <a href="https://github.com/lakehanne/gocator" target="blank">Gocator</a>: ROS and PCL bridges to the <a href="https://lmi3d.com/products/gocator-3D-smart-sensors" target="blank"> LMI Gocator Line Scanning Sensor</a>.
+ <a href="{{ site.url }}/readlist"> Reading list (Old, very old, and so deprecated)</a>:  A collection of papers I <strike>am currently</strike> reading/implementing.
+    <a href="/downloads/save_dijs" target="blank">Radiation therapy dose influence matrices </a>: Extracting fluence based on the Varian Medical Systems' C#/Python API from Eclipse. Core API courtesy of Mike Folkerts (Varian). 

<br><br>

<!-- Strava summary -->
<h2><i class="fa fa-chevron-right"></i><i class="fa fa-chevron-right"></i>Strava Activities Summary</h2>

<p>Regular mortal on two wheels here. As often as I can get away from the lab, I like to pedal the metals of my bike, often logging approximately 120 miles a week -- during cycling season. I ride rain or shine, hell or highwater -- in the parching heats of sultry Texas, or the blustering cold winds of the  Midwest and the Eastern Seaboard. If you are in my area and would love to tag along on a ride, do not hesitate to shoot me an email. 

Texas, Illinois, Wisconsin, Indiana, Pennsylvania, Delaware and New Jersey Rider. Below is a screenshot of my recent activities summary. </p>
  <iframe height='160' width='400' frameborder='0' allowtransparency='true' scrolling='no' src='https://www.strava.com/athletes/29996478/activity-summary/a1ced5c81ee2203640950cbaf24d5fb53d84bafb'></iframe>

<br><br>
Last updated on {% include last-updated.txt %}
