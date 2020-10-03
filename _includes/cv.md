
<h2><i class="fa fa-chevron-right"></i><i class="fa fa-chevron-right"></i> Bio Snippet </h2>

<h4><i class="fa fa-chevron-right"></i><i class="fa fa-chevron-right"></i>Research Focus</h4>
   <a href="https://en.wikipedia.org/wiki/Ikigai">**Ikigai**</a>: **Control Theory** <span>&#8745;</span> **Robotics** <span>&#8745;</span> **Machine <del>L</del>Earning** (Not in that order). <br>
   **Fund-my-research buzzwords**: Artificial Intelligence, Big Data, Data Science.<br>
   **Antiquated buzzwords**: System Identification, Data Mining.

<h4><i class="fa fa-chevron-right"></i><i class="fa fa-chevron-right"></i>Current/Past University Affiliations</h4>
  - Postdoctoral Researcher, [The University of Pennsylvania, Perelman School of Medicine](https://www.med.upenn.edu/) (2019 - Present).
  - Postdoctoral Scholar, [The University of Chicago, Pritzker School of Medicine](https://pritzker.uchicago.edu/) (2019 - Present).
  - Adjunct Instructor, [Brandeis University, Graduate School of Professional Studies](https://brandeis.edu/), Robot Manipulation, Motion Planning and Control,  (2019 - Present).
  - Student, [The University of Texas at Dallas, School of Engineering](https://ecs.utdallas.edu/~opo140030/) (Ended 2019).
  - Visiting Student, [UT Southwestern Medical Center, Medical Physics and Engineering](https://www.utsouthwestern.edu/labs/maia/about/meet-our-team.html)  (Ended 2019).
  -  Student, [The University of Sheffield, Automatic Control and Systems Engineering](https://www.sheffield.ac.uk/acse) (Ended 2012/2013).

<h4><i class="fa fa-chevron-right"></i><i class="fa fa-chevron-right"></i>Previous Company Affiliations</h4>
  -  [Amazon Robotics](https://www.amazonrobotics.com/#/) (Advanced Robotics Lab), Greater Boston Area, MA (Ended 2016).
  - [Preferred Networks](https://www.preferred-networks.jp/en/), Tokyo, Japan (Ended 2018).
  - [Coca-Cola](https://coca-colahellenic.com/), Lagos/Athens (Ended 2011).

<h4><i class="fa fa-chevron-right"></i><i class="fa fa-chevron-right"></i>  Professional Activities</h4>
- [IEEE International Conference on Robotics and Automation](https://icra2021.org), Associate Editor
- [NYAS, The New York Academy of Sciences](https://www.nyas.org/), Member 
- [IEEE RAS, Robotics and Automation Society](https://www.ieee-ras.org/), Member
- [AAPM: The American Association of Physicists in Medicine](https://w3.aapm.org/my_aapm/index.php), Junior Member
- [ASTRO, The American Society for Radiation Oncology](https://www.astro.org/), Member

<h2><i class="fa fa-chevron-right"></i><i class="fa fa-chevron-right"></i>Select News Highlights</h2>
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

<h2><i class="fa fa-chevron-right"></i><i class="fa fa-chevron-right"></i> Select Invited Talks</h2>

 - Soft Robots-based Position Correction Mechanisms in Intensity-Modulated Radiation Therapy. Open Robotics Foundation, Mountain View, CA, USA. January 2019.

- Robotic Radiotherapy: Automating Position Correction in Intensity-Modulated Radiation Therapy, Department of Energy Resources Engineering. Stanford University, Stanford, CA, USA. November 2018.

- Robotic Radiotherapy: Automating Position Correction in Intensity-Modulated Radiation Therapy, Department of Radiation and Cellular Oncology, The University of Chicago, Chicago, IL, USA. November 2018.

- Minimax Iterative Dynamic Game, Department of Brain Robot Interface. Computational Neuroscience Labs, ATR, Osaka, Japan. August 2018.
  
- Neural Networks and Adaptive Control, Preferred Networks Tech. Talk, Chiyoda-ku, Tokyo. Japan. August 2018.

- SoftNeuroAdapt: A 3-DoF Neuro-Adaptive Healthcare System.  Google Robotics, Mountain View, CA. USA. September 2017. [Work presented by Nick Gans].

- A Wearable Soft Robot Modular System for Head and Neck Motion Correction in Intensity-Modulated Radiation Therapy. University of Texas at Arlington Research Institute, Fort Worth, Texas, USA. May 2019.

<!-- 
- Soft Robotic Modules as Position Correcting Mechanisms in Cancer RT, 3rd Entrepreneurship Forum & Start-up Competition, EFSC'17, Vancouver, BC, Canada. September 2017.

<h4><i class="fa fa-chevron-right"></i><i class="fa fa-chevron-right"></i> Awards and Honors</h4>
 -  NSF Doctoral Consortium Award, 2017
 -  Mary and Richard Templeton Graduate Fellowship, 2017 
 -  Ericsson Graduate Fellowship, 2015
 -  President’s Teaching Excellence Award for Teaching Assistants, Nom. 2017
 -  Jonsson Scholarship, 2014
 -  IEEE Robotics and Automation Society (RAS) Travel Award, 2018
 -  Golden Key Honor, 2016
 -  IEEE RAS/ISAM<sup>International Symposium on Assembly and Manufacturing</sup>Travel Award, 2016
 -  Google AI Travel and Conference Grant, 2018
 -  ROSCon Scholarship, 2017
-->

<h4><i class="fa fa-chevron-right"></i><i class="fa fa-chevron-right"></i> Peer Review Service</h4>
  - [Automatica, A Journal of IFAC, The International Federation of Automatic Control](https://www.journals.elsevier.com/automatica").
  - [World Congress, The IFAC, The International Federation of Automatic Control](https://www.ifac-control.org/events/ifac-world-congress-21th-wc-2020).  
  - [ICRA, An IEEE International Conference on Robotics and Automation.](https://www.icra2020.org/)
  - [CDC, An IEEE International Conference on Decision and Control.](https://cdc2020.ieeecss.org/)
  - [IROS, An IEEE/Robotics Society of Japan International Conference on Intelligent Robots and Systems](https://www.iros2019.org/).
  - [DSCC, Dynamic Systems and Control Conference, The American Society of Mechanical Engineers](https://event.asme.org/DSCC).
  - [ACC, An IEEE Control Systems Society/American Control Conference](http://acc2020.a2c2.org/).
  - [JBHI, An IEEE Journal of Biomedical and Health Informatics](https://jbhi.embs.org/).
  - [Access, An IEEE Journal](https://ieeeaccess.ieee.org/?http://ieeeaccess.ieee.org/).
  - [NCAA, Neural Computing and Applications, A Springer Journal](https://link.springer.com/journal/521).
  - [ICML, International Conference on Machine Learning](https://icml.cc/)
  - External Grants Reviewer, [National Geographic Society](https://www.nationalgeographic.org/).

<!-- <h4><i class="fa fa-chevron-right"></i><i class="fa fa-chevron-right"></i>Awards and Honors</h4>
  -  Google AI Travel and Conference Grant (2018)
  - IEEE Robotics and Automation Society (RAS) Travel Award (2018/2017/2016)
  - NSF Doctoral Consortium Award (2017)
  - Mary and Richard Templeton Graduate Fellowship (2017)
  - Open Software for Robotics Foundation Scholarship (2017)
  - President’s Excellence Award for Teaching Assistants (Nom. 2017)
  - Golden Key International Honour Society (2016)
  - Ericsson Graduate Fellowship (2015)
  - Jonsson Scholarship (2014)
  - PTDF Overseas Fellowship (2012).
  - Best Chemistry Student (West African Senior School Examinations -- Two Years in a Row). -

   Thanks to my committee members, <a href="https://ece.illinois.edu/directory/profile/mspong">Mark Spong</a>, <a href=""> Tyler Summers</a>, <a href="">Yonas Tadesse</a> and <a href=""> Nick Gans</a>, and my UTSW mentor, <a href="https://profiles.utsouthwestern.edu/profile/150563/steve-jiang.html">Steve Jiang</a>.



  - [Brandeis University](https://www.brandeis.edu/gps/), [Adjunct Instructor, Robot Manipulation, Planning and Control](https://www.brandeis.edu/gps/current-students/academic-information/course?acad_year=2020&crse_id=014100) (2019 - Present).
-->
