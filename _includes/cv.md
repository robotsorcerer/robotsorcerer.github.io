
<h2><i class="fa fa-chevron-right"></i><i class="fa fa-chevron-right"></i><a href="https://en.wikipedia.org/wiki/Ikigai">Ikigai</a></h2>

The rise in computational power together with the pervasiveness of big data has created new computing modalities which has spurred an emergent digital economy, and has spawned new business value chains. Across these spates of recent developments, the question of resilience and reliability, safety and robustness, as well as the assured predictability of behavior in the (autonomous) systems that we design and build has become timely and crucial. Emergent autonomous AI systems must make decisions under imperfect circumstances based on environment information that is available from an array of perceptual inputs and their representation, reason through self-enumerated possible actions, and safely execute the ones that provide a meaningful state transition in the environment in which they act --- all the while guaranteeing safety, stability, and resilience under external disturbances. Broadly, one can think of autonomous AI systems along two general threads: (i) situated autonomy, such as an automated airline ticket reservation system that reserves and makes decisions based on provided input by an external agent; and (ii) embodied autonomy, that is agents with perceptual sensors and proprioceptive actuators that effect a physical environmental change upon interaction; an example in this latter category are physical robots that sense the world directly through contact, and react adaptively to effect a change in representation of their environment via feedback. In both situated and embodied autonomy, we expect algorithms to deliver performance specifications without a glitch as we automate away tasks that humans have traditionally performed for over a century. My core research exists at the intersection of three intertwined fields that encapsulate important questions surrounding situatedness and embodiments: **robotics**, **control theory**, and **machine learning**. Robotics is crucial for the automation of physical embodiments. Control theory offers the crucial scientific recipé that establishes strong robustness and resilient foundations in otherwise flimsy AI models and policies (encompassing situatedness and embodiments). And machine learning provides the relaxation to devise generalist algorithmics that transcend narrow applications to broad usage. Motivated by what is possible with hitherto unexplored and large-scale engineering feats across these three disciplines, my research seeks to deconstruct the challenges that modern technology presents viz., (i) combining the elegance of mathematical rigor in imbuing resilience and robustness into the little margins that exist in safety-critical embodiments; (ii) reasoning possible automation capabilities into existence through abstract sub-task modules in a hierarchy of systems architectural principles; this is guided by clear conceptual analyses baked in the tradition of classical scientific rigor; and (iii) leveraging bio-inspiration to build emergent agent-centric situated AI and functional embodied automation systems. As I plan and act, I will continue to collaborate with  various researchers with relevant expertise around the planet as we construct new insights on solving difficult automation problems, and broaden our understanding of the problems that are relevant to the future. Stimulating rapid growth in our understanding of critical structures to complex systems, we shall bring to bear new inventions to a safe and desired haven that fosters a neat co-existence with human beings in everyday living.
<h4><i class="fa fa-chevron-right"></i><i class="fa fa-chevron-right"></i> <a href="/research">Further reading</a></h4>


<h4><i class="fa fa-chevron-right"></i><i class="fa fa-chevron-right"></i> Research Chronology</h4>
- Senior Researcher, Microsoft Research Lab (NYC), 2021 - Present.
- Adjunct Faculty, [Brandeis University, Graduate School of Professional Studies](https://brandeis.edu/), (2019 - 2021).
- Postdoctoral Researcher, [The University of Pennsylvania, Perelman School of Medicine](https://www.med.upenn.edu/) (2019 - 2021).
- Postdoctoral Scholar, [The University of Chicago, Pritzker School of Medicine](https://pritzker.uchicago.edu/) (2019).
- Research Intern (Robot Learning), [Preferred Networks](https://www.preferred-networks.jp/en/), Tokyo, Japan (Ended 2018).
- Mechatronics Intern, [Amazon Robotics](https://www.amazonrobotics.com/#/) (Advanced Robotics Lab), Greater Boston, MA (2016).
- Student, [The University of Texas at Dallas, School of Engineering](https://ecs.utdallas.edu/~opo140030/) (2014 - 2019).
- Visiting Student, [UT Southwestern Medical Center, Medical Physics and Engineering](https://www.utsouthwestern.edu/labs/maia/about/meet-our-team.html)  (2014 - 2019).  
- Student, [The University of Sheffield, Automatic Control and Systems Engineering](https://www.sheffield.ac.uk/acse) (Ended 2012/2013).

<h4><i class="fa fa-chevron-right"></i><i class="fa fa-chevron-right"></i> Select News Highlights</h4>
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

<a name="mentor"></a>
 <h4><i class="fa fa-chevron-right"></i><i class="fa fa-chevron-right"></i>  Mentoring Activities.</h4>

I enjoy working with/mentoring young students/scientists in teaching and research capacities alike. Before MSFT, I was an adjunct faculty at Brandeis up in Waltham, MA. Current or past students, interns and postdocs include:

+ [Leilei Cui](https://scholar.google.com/citations?user=RbczS_gAAAAJ&hl=en&oi=ao) (advised by [Zhong-Ping Jiang](https://engineering.nyu.edu/faculty/zhong-ping-jiang)). MSR Intern, 2022   &rarr; NYU Engineering PhD &rarr; Posdoctoctoral Scholar, MIT.
+ [Abulikemu Abuduweili](https://scholar.google.com/citations?user=6Oro5g8AAAAJ&hl=en). CMU Robotics PhD student &rarr; MSR Intern 2024; being co-advised together with [Elise van der Pol](https://www.elisevanderpol.nl/), [Qiuyuan Huang](https://scholar.google.com/citations?user=U7Mmyc8AAAAJ&hl=en), and [Naoki Wake](https://www.microsoft.com/en-us/research/people/nawake/).
+ [Anurag Koul](https://koulanurag.dev/), Oregon State University, Microsoft Research Postdoc, 2022 - 2024.  Present: Senior Research Scientist, Amazon NYC.
+ [Gilbert Bahati](https://www.gbahati.com/home), Caltech Mechanical Engineering PhD Student (Advised by Dr. [Aaron Ames](http://ames.caltech.edu/)).
+ Harry Vuong. Brandeis University MS 2020/2021 &rarr; Robotic Systems Engineer, Universal Robots A/S. 
+ [Harley Wiltzer](https://harwiltz.github.io/), Microsoft Research Intern, 2023. McGill PhD Student advised by [David Meger](https://www.cim.mcgill.ca/~dmeger/) and [Marc Bellemare](http://www.marcgbellemare.info/).
+ [Thomas Zhang](https://thomaszh3.github.io/), Microsoft Research Intern, 2023. UPenn PhD Student advised by [Nik Matni](https://nikolaimatni.github.io/).
+  [Adwait Kulkarn](https://www.linkedin.com/in/adwaitkulkarni93), 2017-2018 Masters intern &rarr; (VP of Smart Trailer Engineering, [Drov. Tech, MN](http://drovtech.com)).
+  [Rachel Thompson](https://github.com/rsthomp), 2017 Plano High School &rarr; University of Texas as Dallas &rarr; MIT CSAIL undergrad &rarr; Brown University PhD.
+ Etiosa Omeike. Princeton ECE Junior &rarr;  Microsoft Undergraduate Research Intern, 2023.
+  [Ajith Venkateswaran](https://www.linkedin.com/in/ajithvenkateswaran), 2016-2017 Masters Intern &rarr; Amazon Robotics LLC &rarr; University of Texas at Dallas &rarr; Senior Software Engineer, Johnson & Johnson.
+  [Blessing Kolawole](https://www.linkedin.com/in/blessingkolawole/), Undergrad Assistant. (CS PhD student, Tufts University).
+ [Shaoru Chen](https://shaoruchen.github.io). Penn ESE, University of Pennsylvania &rarr; Microsoft Research Postdoc (2023-?).
 
<h4><i class="fa fa-chevron-right"></i><i class="fa fa-chevron-right"></i> Select Talks, Classes, and Conferences</h4>
<h5><i class="fa fa-chevron-right"></i><i class="fa fa-chevron-right"></i>Talk Highlights</h5>
- [Dynamics from Pixels as Time Integrations of Neural Lie Group Homomorphisms](downloads/Papers/Yale.pdf), MSR Game Intelligence Group, Cambridge, UK. Fall 2023.
- [On the Robustness and Convergence of Policy Optimization in Continuous-Time Mixed H2/H-infinity Stochastic Control](#), Yale University Engineering/CS Faculty, New Haven, Conn. Fall 2023.
<!-- - [Modeling and Control of Flexible Structures in Virtual Reality Environments](#), McGill University Engineering/MILA, Winter 2024. -->
- Learning without Rewards, [Microsoft Research Summit](https://www.microsoft.com/en-us/research/event/microsoft-research-summit-2021/), Fall 2021.
- [Automating Treatment Planning in Radiation Therapy](#), Microsoft Research NYC, New York City, Winter 2021.
- [Automating Treatment Planning in Radiation Therapy](#), Auris Health, Johnson & Johnson, San Francisco, CA, 2021.
- Soft Robots-based Position Correction Mechanisms in Intensity-Modulated Radiation Therapy. Open Robotics Foundation, Mountain View, CA, USA, 2019.
- Robotic Radiotherapy: Automating Position Correction in Intensity-Modulated Radiation Therapy, Department of Energy Resources Engineering. Stanford University, Stanford, CA, USA, 2018.
- Robotic Radiotherapy: Automating Position Correction in Intensity-Modulated Radiation Therapy, Department of Radiation and Cellular Oncology, The University of Chicago, Chicago, IL, USA, 2018.
- Minimax Iterative Dynamic Game, Department of Brain Robot Interface. Computational Neuroscience Labs, ATR, Osaka, Japan, 2018.  
- Soft Robotic Modules as Position Correcting Mechanisms in Cancer RT, 3rd Entrepreneurship Forum & Start-up Competition, EFSC'17, Vancouver, BC, Canada, 2017.
- Neural Networks and Adaptive Control, Preferred Networks Tech. Talk, Chiyoda-ku, Tokyo. Japan, 2018. 

<h4><i class="fa fa-chevron-right"></i><i class="fa fa-chevron-right"></i> Editorial/Community Services</h4>
- **Mentee Lead**, (Microsoft) Technology and Research (T&R) Mentoring Ring FY25, 2024 - 2025.
- **Co-Coordinator**, Reinforcement Learning Discussion Group Series, Microsoft Research, 2023 - 2024.
- **Member**, IEEE Robotics and Automation Technical Committee on (i) Soft Robotics; (ii) Cognitive Robotics; (iii) Algorithms for Planning and Control; (iv) Automation in Health Care Management; (v) Aerial Robotics and Unmanned Aerial Vehicles. 2023 - Present.
- **Associate Editor**, [IEEE International Conference on Robotics and Automation (ICRA) Workshops](https://www.icra2023.org/), 2022-2023.
- **Associate Editor**, [IEEE International Conference on Robotics and Automation (ICRA)](https://www.icra2020.org/), 2020-2021.
- **External Grants Reviewer**, AI for Species Discovery, [National Geographic Society](https://www.nationalgeographic.org/), 2020 - 2021.
- **Journal Reviewer**: [Automatica (IFAC -- The International Federation of Automatic Control)](https://www.journals.elsevier.com/automatica"), IEEE Letters to Control Systems Society (L-CSS), IEEE Robotics and Automation Letters (RA-L), [Journal of Biomedical and Health Informatics](https://jbhi.embs.org/) (JBHI), Institute of Physics (IOP): The International Journal of Biomedical Physics and Engineering (PhysMed), [IEEE Access](https://ieeeaccess.ieee.org/?http://ieeeaccess.ieee.org/), [Neural Computing and Applications (NCAA)](https://link.springer.com/journal/521).
- **Conference Reviewer**: IEEE International Conference on Robotics and Automation (ICRA), IEEE International Conference on Decision and Control (CDC), IEEE/Robotics Society of Japan International Conference on Intelligent Robots and Systems (IROS), [Dynamic Systems and Control Conference -- The American Society of Mechanical Engineers (DSCC)](https://event.asme.org/DSCC), [American Control Conference (ACC)](http://acc2020.a2c2.org/), [International Conference on Machine Learning (ICML)](https://icml.cc/), [International Conference on Learning Representations (ICLR)](https://iclr.cc/), IFAC -- World Congress, Neural Information Processing Systems (NeurIPS).

<h5><i class="fa fa-chevron-right"></i><i class="fa fa-chevron-right"></i> Classes and Useful Presentations</h5>
- [A Short Treatise on the Kinematics and Kinetics of Robots -- Slides](/downloads/Papers/screw_slides.pdf), MSR NYC, 2022.
- [The Mathematical Foundations of Robotics](/downloads/Papers/RBOT101.pdf), Brandeis University, 2021.
- [Robot Manipulation, Planning and Control](/downloads/Papers/RBOT250.pdf), Brandeis University, 2020.
- [L1 Adaptive Control -- Courtesy of Naira Hovakimyan. 10/1/2015](/downloads/Papers/L1Adaptive.pdf)
<br>
 <h4><i class="fa fa-chevron-right"></i><i class="fa fa-chevron-right"></i>  Professional Activities.</h4>

 - [IEEE](https://www.ieee.org/), Member.
 - [IEEE RAS, Robotics and Automation Society](https://www.ieee-ras.org/), Member.
 - [IEEE CSS, Control Systems Society](https://www.ieeecss.org/), Member.
 <font size=2>(Strikethroughs signify societies I was a part of but whose membership I no longer belong).</font>
 - ~~[AAPM: The American Association of Physicists in Medicine](https://w3.aapm.org/my_aapm/index.php), Junior Member.~~
 - ~~[ASTRO, The American Society for Radiation Oncology](https://www.astro.org/), Member~~.
 - ~~[NYAS, The New York Academy of Sciences](https://www.nyas.org/), Member~~.

<h4><i class="fa fa-chevron-right"></i><i class="fa fa-chevron-right"></i>Life, liberty, and the pursuit of the KOMs</h4>

<p>As often as I can get away from the lab, I like to ride my (road/mountain/Grandma's) bike. I ride rain or shine, hell or highwater -- whether it's in the parching heats of sultry Texas, or the blustering cold winds of the  Midwest and the Eastern Seaboard. States I have ridden so far include: NY, NJ, MA, NH, PA, DE, TX, IL, WI, IN, HI, WA. Below is a screenshot of my recent activities summary. </p>
  <iframe height='160' width='400' frameborder='0' allowtransparency='true' scrolling='no' src='https://www.strava.com/athletes/29996478/activity-summary/a1ced5c81ee2203640950cbaf24d5fb53d84bafb'></iframe>

<br>
<h4><i class="fa fa-chevron-right"></i><i class="fa fa-chevron-right"></i> Recent Readings </h4>
 Below are a list of books in my current reading list.
 <h5><i class="fa fa-chevron-right"></i><i class="fa fa-chevron-right"></i> 2024 Readings</h5>
 -  The Federalist -- Alexander Hamilton, John Jay, and James Madison.
 -  The Startup Way -- Eric Ries.
 -  No Ordinary Time, Franklin and Eleanor Roosevelt: The Home Front in World War II -- Doris Kearns Goodwin.
 -  Successful Negotiating: Letting the Other Person Have <i>Your</i> way -- Ginny Pearson Barnes.
 -  On Natural Selection -- Charles Darwin.
 -  Isaac Asimov's Caliban -- Rober MacBride Allen.
 -  How to avoid a Climate Disaster -- Bill Gates.
 -  A Tale of Two Cities -- Charles Dickens.
 -  True Compass -- Edward Kennedy. 
 <h5><i class="fa fa-chevron-right"></i><i class="fa fa-chevron-right"></i> Oldies and Goodies</h5>
 -  Knowing Mandela -- John Carlin.
 -  Democracy in America -- Alexis De Toqueville.
 -  Team of Rivals: The Political Genius of Abraham Lincoln --  Doris Kearns Goodwin.
 -  The Sun Also Rises -- Ernest Hemingway.
 -  John Adams -- David McCullough.
 -  ~~The Prison Letters of Nelson Mandela -- Edited by Sham Venter.~~
 -  ~~Mandela, The Authorized Biography  -- Anthony Sampson.~~
 -  ~~1776 -- David McCullough.~~
 -  ~~Founding Fathers -- Gordon Leidner.~~
 -  ~~Managing Up -- Rosanne Badowski~~.
 -  ~~Eye of the Hurricane: An Autobiography -- Richard Bellman~~.
 -  ~~Advice for a Young Investigator -- Santiago Ramon y Cajal~~.
 -  ~~Richard Feynmann: A Life in Science -- John and Mary Gribblin~~.
 -  ~~Made to Stick: Why Some Ideas Survive and Others Die -- Chip Heath and Dan Heath.~~
 -  ~~Profiles in Courage -- John Fitzgerald Kennedy.~~
