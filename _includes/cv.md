
<h2><i class="fa fa-chevron-right"></i><i class="fa fa-chevron-right"></i> Bio Snippet </h2>

<h4><i class="fa fa-chevron-right"></i><i class="fa fa-chevron-right"></i>Research Focus</h4>
   <a href="https://en.wikipedia.org/wiki/Ikigai">**Ikigai**</a>: **Control Theory** <span>&#8745;</span> **Robotics** <span>&#8745;</span> **Machine <del>L</del>Earning** (Not in that order). <br>
   **Fund-my-research buzzwords**: Artificial Intelligence, Machine Learning, Data Science.<br>
   **Expert buzzwords**: System Identification, Control Theory, State Estimation.

<h4><i class="fa fa-chevron-right"></i><i class="fa fa-chevron-right"></i> Research Experience</h4>
  - Senior Researcher, Microsoft Research Lab (NYC), 2021 - Present 
  - Adjunct Faculty, [Brandeis University, Graduate School of Professional Studies](https://brandeis.edu/), (2019 - Present).
  - Postdoctoral Researcher, [The University of Pennsylvania, Perelman School of Medicine](https://www.med.upenn.edu/) (2019 - 2021).
  - Postdoctoral Scholar, [The University of Chicago, Pritzker School of Medicine](https://pritzker.uchicago.edu/) (2019).
  - Research Intern (Robot Learning), [Preferred Networks](https://www.preferred-networks.jp/en/), Tokyo, Japan (Ended 2018).
  - Mechatronics Intern, [Amazon Robotics](https://www.amazonrobotics.com/#/) (Advanced Robotics Lab), Greater Boston, MA (2016).
  - Student, [The University of Texas at Dallas, School of Engineering](https://ecs.utdallas.edu/~opo140030/) (2014 - 2019).
  - Visiting Student, [UT Southwestern Medical Center, Medical Physics and Engineering](https://www.utsouthwestern.edu/labs/maia/about/meet-our-team.html)  (2014 - 2019).
  - Student, [The University of Sheffield, Automatic Control and Systems Engineering](https://www.sheffield.ac.uk/acse) (Ended 2012/2013).
  <!-- - Supply Chain Manager, [Coca-Cola Hellenic Bottilng Co.](https://coca-colahellenic.com/), Lagos/Athens (2009 - 2011). -->


<h4><i class="fa fa-chevron-right"></i><i class="fa fa-chevron-right"></i>Select News Highlights</h4>
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
<h4><a href="{{ sites }}/news">Archived news</a></h4>
</table>

<h4><i class="fa fa-chevron-right"></i><i class="fa fa-chevron-right"></i> Select Talks, Classes, and Conferences</h4>
<h6>Recent Job Talks</h6>
- [Automating Treatment Planning in Radiation Therapy](#), Microsoft Research NYC Seminar (Senior Researcher -- Reinforcement Learning), New York City, March 2021.
- [Automating Treatment Planning in Radiation Therapy](#), Auris Health, Johnson & Johnson (Senior Research Scientist -- Robotic Radiosurgery), San Francisco, Feb 2021.
<!--
    /assets/presentations/MSR.pdf
    /assets/presentations/AurisHealth.pdf
 -->
<h6>Recent Class Notes</h6>
- [The Mathematical Foundations of Robotics](/downloads/Papers/RBOT101.pdf), Brandeis University, Spring 2021.
- [Robot Manipulation, Planning and Control](/downloads/Papers/RBOT250.pdf), Brandeis University, Spring 2020.
<h6>Older Job Talks</h6>
- Soft Robots-based Position Correction Mechanisms in Intensity-Modulated Radiation Therapy. Open Robotics Foundation, Mountain View, CA, USA. January 2019.
- Robotic Radiotherapy: Automating Position Correction in Intensity-Modulated Radiation Therapy, Department of Energy Resources Engineering. Stanford University, Stanford, CA, USA. November 2018.
- Robotic Radiotherapy: Automating Position Correction in Intensity-Modulated Radiation Therapy, Department of Radiation and Cellular Oncology, The University of Chicago, Chicago, IL, USA. November 2018.
<h6>Antiquated Talks</h6>
- Minimax Iterative Dynamic Game, Department of Brain Robot Interface. Computational Neuroscience Labs, ATR, Osaka, Japan. August 2018.  
- Neural Networks and Adaptive Control, Preferred Networks Tech. Talk, Chiyoda-ku, Tokyo. Japan. August 2018.
- SoftNeuroAdapt: A 3-DoF Neuro-Adaptive Healthcare System.  Google Robotics, Mountain View, CA. USA (Presented by Nick Gans). September 2017.
- A Wearable Soft Robot Modular System for Head and Neck Motion Correction in Intensity-Modulated Radiation Therapy. University of Texas at Arlington Research Institute (UTARI), Fort Worth, Texas, USA. May 2019.
- Soft Robotic Modules as Position Correcting Mechanisms in Cancer RT, 3rd Entrepreneurship Forum & Start-up Competition, Vancouver, BC, Canada. September 2017.


<h4><i class="fa fa-chevron-right"></i><i class="fa fa-chevron-right"></i>  Professional Activities.</h4>
- [IEEE International Conference on Robotics and Automation](https://icra2021.org), Associate Editor.
- [NYAS, The New York Academy of Sciences](https://www.nyas.org/), Member.
- [IEEE RAS, Robotics and Automation Society](https://www.ieee-ras.org/), Member.
- [AAPM: The American Association of Physicists in Medicine](https://w3.aapm.org/my_aapm/index.php), Junior Member.
- [ASTRO, The American Society for Radiation Oncology](https://www.astro.org/), Member.

<h4><i class="fa fa-chevron-right"></i><i class="fa fa-chevron-right"></i> Editorial Services </h4>
  - External Grants Reviewer (AI for Species Discovery), [National Geographic Society](https://www.nationalgeographic.org/), 2020 - Present.
  - Associate Editor, [ICRA, An IEEE International Conference on Robotics and Automation](https://www.icra2020.org/), 2020-2021.
  - Reviewer, [Automatica, A Journal of IFAC, The International Federation of Automatic Control](https://www.journals.elsevier.com/automatica"), 2017 - Present.
  - Reviewer, [World Congress, The IFAC, The International Federation of Automatic Control](https://www.ifac-control.org/events/ifac-world-congress-21th-wc-2020), 2017 - Present.  
  - Reviewer, [CDC, An IEEE International Conference on Decision and Control.](https://cdc2020.ieeecss.org/)
  - Reviewer, [IROS, An IEEE/Robotics Society of Japan International Conference on Intelligent Robots and Systems Reviewer](https://www.iros2019.org/), 2017 - Present.
  - [DSCC, Dynamic Systems and Control Conference, The American Society of Mechanical Engineers](https://event.asme.org/DSCC).
  - Reviewer, [ACC, An IEEE Control Systems Society/American Control Conference](http://acc2020.a2c2.org/), 2017 - Present.
  - Reviewer, [JBHI, An IEEE Journal of Biomedical and Health Informatics](https://jbhi.embs.org/), 2019 - Present.
  - Reviewer, [Access, An IEEE Journal](https://ieeeaccess.ieee.org/?http://ieeeaccess.ieee.org/), 2018 - Present.
  - Reviewer, [NCAA, Neural Computing and Applications, A Springer Journal](https://link.springer.com/journal/521), 2017 - Present.
  - Reviewer, [ICML, International Conference on Machine Learning](https://icml.cc/), 2017 - Present.


<br>

<!-- Strava summary -->
<h4><i class="fa fa-chevron-right"></i><i class="fa fa-chevron-right"></i>Strava Activities Summary</h4>

<p>Regular mortal on two wheels here. As often as I can get away from the lab, I like to pedal the metals of my bike, often logging approximately 120 miles a week -- during cycling season. I ride rain or shine, hell or highwater -- in the parching heats of sultry Texas, or the blustering cold winds of the  Midwest and the Eastern Seaboard. If you are in my area and would love to tag along on a ride, do not hesitate to shoot me an email.

Texas, Illinois, Wisconsin, Indiana, Pennsylvania, Delaware and New Jersey Rider. Below is a screenshot of my recent activities summary. </p>
  <iframe height='160' width='400' frameborder='0' allowtransparency='true' scrolling='no' src='https://www.strava.com/athletes/29996478/activity-summary/a1ced5c81ee2203640950cbaf24d5fb53d84bafb'></iframe>



<br>

 <h4><i class="fa fa-chevron-right"></i><i class="fa fa-chevron-right"></i> Side Projects</h4>

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


<br>

<h4><i class="fa fa-chevron-right"></i><i class="fa fa-chevron-right"></i> Recent Readings </h4>

 -  1776 -- David McCullough.
 -  Made to Stick: Why Some Ideas Survive and Others Die -- Chip Heath and Dan Heath.
 -  Eye of the Hurricane: An Autobiography -- Richard Bellman.
 -  Advice for a Young Investigator -- Santiago Ramon y Cajal.
 -  Profiles in Courage -- John Fitzgerald Kennedy.
