
<!-- > No fluff research science and engineering [ikigai](https://en.wikipedia.org/wiki/Ikigai).  -->

[Ikigai](https://en.wikipedia.org/wiki/Ikigai): Roboticist-scientist hybrid across the physical and virtual automation stack — algorithmic theory and practice of AI, RL, ML, and control systems on automatons(read: robots). 

**Research snippet:** AI is a general-purpose technology with a potential for disruptive technological breakthroughs that may stimulate new (digital) economic value chains in society. Today, our scientific understanding of the fundamental algorithmic mechanisms needed to transform this emerging technology into  provably safe and robust (embodied) _biological systems_ and _safety-critical physical infrastructure_ are far behind its empirical engineering performance.  In this sentiment, I exert my scientific research inquiry on agentic embodied AI systems --- with a particular emphasis on answers to big questions surrounding their _safety, stability, robustness, reliability, and resilience (S23R)_ in safety-critical infrastructure. The <b>topical angles of attack within my research stack</b> encompass: distributed generalized Nash-equilibrium seeking games, diffusion sampling in infinite-dimensional spaces, <a href="{{ site.url }}/downloads/Papers/h2hinf.pdf"  target="_blank">robust policy optimization</a>, <a href="{{ site.url }}/downloads/Papers/SoRoPD.pdf"  target="_blank">reduced-order model and control of multi-arm</a> and collaborative robots, <a href="https://arxiv.org/abs/2311.03534">representation learning in large observation spaces</a>, autonomous c-space exploration, and <a href="{{ site.url }}/downloads/Papers/levelsetpy.pdf"  target="_blank">Hamilton-Jacobi analysis</a> for runtime assurance in complex autonomous systems (read: cyberphysical systems). Balanced and ballasted along the trajectories of these research paths (perhaps, take a quick gander on recent <a href="{{ site.url }}/#talks" target="_blank"> recent talks</a> and <a href="{{ site.url }}/pubs"  target="_blank"> publication preprints</a>), I am interested in runtime assurance tooling and orchestration mechanisms that imbue S23R guarantees in emerging agentic embodied structural systems. If you are interested in collaborating, please do not hesitate to <a href="mailto:lekanmolu@molux-labs.llc" class="author-social" target="_blank"><i class="fa fa-fw fa-envelope-o"></i>shoot me an email</a> .

<h4><i class="fa fa-chevron-right"></i><i class="fa fa-chevron-right"></i> Research Chronology</h4>
- Principal Researcher and Founder, Stealth Startup (2025 -- Present).
- Senior Researcher, Microsoft Research Lab (NYC), (2021 -- 2025).
- Adjunct Faculty, [Brandeis University, Graduate School of Professional Studies](https://brandeis.edu/), (2019 - 2021).
- Postdoctoral Researcher, [The University of Pennsylvania, Perelman School of Medicine](https://www.med.upenn.edu/) (2019 - 2021).
- Postdoctoral Scholar, [The University of Chicago, Pritzker School of Medicine](https://pritzker.uchicago.edu/) (2019).
- Research Intern (Robot Learning), [Preferred Networks](https://www.preferred-networks.jp/en/), Tokyo, Japan (Ended 2018).
- Mechatronics Intern, [Amazon Robotics](https://www.amazonrobotics.com/#/) (Advanced Robotics Lab), Greater Boston, MA (2016).
- Student, [The University of Texas at Dallas, School of Engineering](https://ecs.utdallas.edu/~opo140030/) (2014 - 2019).
- Visiting Student, [UT Southwestern Medical Center, Medical Physics and Engineering](https://www.utsouthwestern.edu/labs/maia/about/meet-our-team.html)  (2014 - 2019).  
- Student, [The University of Sheffield, Automatic Control and Systems Engineering](https://www.sheffield.ac.uk/acse) (Ended 2012/2013).

<a name="news"></a>
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
<!-- <h4><a href="{{ sites }}/news">Archived news</a></h4> -->
</table>
 
<a name="talks"></a>
<h5><i class="fa fa-chevron-right"></i><i class="fa fa-chevron-right"></i>Talk Highlights</h5>
- [Towards Ubiquitous Robotics Automation](downloads/Papers/RAI-Inst.pdf). The Robotics and AI Institute. Cambridge, MA. 09/25.
- [State Representation in Reinforcement Learning](downloads/Papers/BostonDynamics.pdf). Google DeepMind Robotics, SF, CA. 08/25.
- [System Identification for Planning in Reinforcement Learning](#). [Wayve Technologies Ltd.](https://wayve.ai/) London, UK. 08/25.  
- [Embodied Intelligence in Open Embodiments](downloads/Papers/BostonDynamicsMain.pdf). Boston Dynamics, Inc. Waltham, MA. 08/25. [Appendix](/BostonDynamicsApp.pdf).
- [Robustness and Efficient State Representation in Open Embodiments' Automation](downloads/Papers/Yale.pdf), META Reality Labs, SF. 07/25.
- [Layered, hierarchical nonlinear control of soft robotic systems](downloads/Papers/McGill.pdf), McGill University Engineering/MILA. 11/24.
- [On the Robustness and Convergence of Policy Optimization in Continuous-Time Mixed H2/H-infinity Stochastic Control](#), Yale University Engineering/CS Faculty, New Haven, Conn. 11/23.
- [Dynamics from Pixels as Time Integrations of Neural Lie Group Homomorphisms](downloads/Papers/Yale.pdf), MSR Game Intelligence Group, Cambridge, UK. Fall 2023.
- Learning without Rewards, [Microsoft Research Summit](https://www.microsoft.com/en-us/research/event/microsoft-research-summit-2021/). Fall 2021.
- [A Short Treatise on the Kinematics and Kinetics of Robots -- Slides](/downloads/Papers/screw_slides.pdf), MSR NYC. 2022.
- [The Mathematical Foundations of Robotics](/downloads/Papers/RBOT101.pdf), Brandeis University. 2021.
- [Robot Manipulation, Planning and Control](/downloads/Papers/RBOT250.pdf), Brandeis University. 2020.
- [L1 Adaptive Control -- Courtesy of Naira Hovakimyan. 10/1/2015](/downloads/Papers/L1Adaptive.pdf)
- [Automating Treatment Planning in Radiation Therapy](#), Microsoft Research NYC, New York City. Winter 2021.
- [Automating Treatment Planning in Radiation Therapy](#), Auris Health, Johnson & Johnson. San Francisco, CA, 2021.
- Soft Robots-based Position Correction Mechanisms in Intensity-Modulated Radiation Therapy. Open Robotics Foundation, Mountain View, CA, USA, 2019.
- Robotic Radiotherapy: Automating Position Correction in Intensity-Modulated Radiation Therapy, Department of Energy Resources Engineering. Stanford University, Stanford, CA, USA, 2018.
- Robotic Radiotherapy: Automating Position Correction in Intensity-Modulated Radiation Therapy, Department of Radiation and Cellular Oncology, The University of Chicago, Chicago, IL, USA, 2018.
- Minimax Iterative Dynamic Game, Department of Brain Robot Interface. Computational Neuroscience Labs, ATR, Osaka, Japan, 2018.  
- Soft Robotic Modules as Position Correcting Mechanisms in Cancer RT, 3rd Entrepreneurship Forum & Start-up Competition, EFSC'17, Vancouver, BC, Canada, 2017.
- Neural Networks and Adaptive Control, Preferred Networks Tech. Talk, Chiyoda-ku, Tokyo. Japan, 2018. 
<br>


<a name="mentor"></a>
 <h4><i class="fa fa-chevron-right"></i><i class="fa fa-chevron-right"></i>  Mentoring Activities.</h4>

Previous interns, postdocs, and students include:

+ [Taylor Webb](https://scholar.google.nl/citations?user=WCmrJoQAAAAJ&hl=en). Princeton Neuroscience PhD; UCLA Postdoc &rarr; MSR Postdoc, '24/25   &rarr; Assistant Professor, University de Montreal.
+ [Leilei Cui](https://scholar.google.com/citations?user=RbczS_gAAAAJ&hl=en&oi=ao). MSR Intern, '22   &rarr; NYU Engineering PhD &rarr; Posdoctoctoral Scholar, MIT &rarr; Assistant Professor, Univ. of New Mexico.
<!-- + [Hanwen Cao](https://hwcao17.github.io/). UCSD PhD Student &rarr; MSR Intern '25 (co-advised by [Jeff](https://www.microsoft.com/en-us/research/people/jedelmer/), [Akshay](https://people.cs.umass.edu/~akshay/), [Nikolay](https://natanaso.github.io/), and [Yulun](https://tianyulun.com/)).  -->
+ [Abulikemu Abuduweili](https://scholar.google.com/citations?user=6Oro5g8AAAAJ&hl=en). CMU Robotics PhD student &rarr; MSR Intern '24 (co-advised by [Elise van der Pol](https://www.elisevanderpol.nl/), and [Naoki Wake](https://www.microsoft.com/en-us/research/people/nawake/)) &rarr; Research Scientist, Reliant Robotics.
+ [Anurag Koul](https://koulanurag.dev/), Oregon State PhD, MSR Postdoc, '23-'24 &rarr; Applied Scientist II, Amazon NYC.
+ [Shaoru Chen](https://shaoruchen.github.io). Penn ESE PhD, University of Pennsylvania &rarr; MSR Postdoc ('23-'24) &rarr; LinkedIn Senior ML Engineer.
+ Etiosa Omeike. Princeton ECE BS &rarr;  MSR Undergrad Intern, 2023 &rarr; Yale CS PhD student (advised by [Prof. Marynel Vazquez)](https://www.marynel.net/).
+ [Thomas Zhang](https://thomaszh3.github.io/), MSR Intern, '23. UPenn PhD Student advised by [Prof. Nik Matni](https://nikolaimatni.github.io/).
+ [Gilbert Bahati](https://www.gbahati.com/home), Caltech MechE PhD Student (Advised by Prof. [Aaron Ames](http://ames.caltech.edu/)).
+ [Haoxiang You](https://ialab.yale.edu/members/haoxiang-you.html). Yale MAE PhD Student. Advised by Prof. [Ian Abraham](https://ialab.yale.edu/).
+ Harry Vuong. Brandeis University MS 2020/2021 &rarr; Robotic Systems Engineer, Universal Robots A/S. 
+ [Harley Wiltzer](https://harwiltz.github.io/), MSR Intern, 2023. McGill PhD Student advised by Profs. [David Meger](https://www.cim.mcgill.ca/~dmeger/) and [Marc Bellemare](http://www.marcgbellemare.info/).
+  [Adwait Kulkarn](https://www.linkedin.com/in/adwaitkulkarni93), 2017-2018 Masters intern &rarr; (VP of Smart Trailer Engineering, [Drov. Tech, MN](http://drovtech.com)).
+  [Rachel Thompson](https://github.com/rsthomp), 2017 Plano High School &rarr; University of Texas as Dallas &rarr; MIT CSAIL undergrad &rarr; Brown University PhD.
+  [Ajith Venkateswaran](https://www.linkedin.com/in/ajithvenkateswaran), 2016-2017 Masters Intern &rarr; Amazon Robotics LLC &rarr; University of Texas at Dallas &rarr; Senior Software Engineer, Johnson & Johnson &rarr; SW Tech Lead (Embedded Automotive Platforms), Wayve.
+  [Blessing Kolawole](https://www.linkedin.com/in/blessingkolawole/), Undergrad Assistant. (CS PhD student, Tufts University). 

<a name="service"></a>
<h4><i class="fa fa-chevron-right"></i><i class="fa fa-chevron-right"></i> Editorial/Community Services</h4>
- **Co-Organizer**, Microsoft Cortex Research Series, FY25, 2024 - 2025.
- **Mentee Lead**, (Microsoft) Technology and Research (T&R) Mentoring Ring FY25, 2024 - 2025.
- **Co-Coordinator**, Reinforcement Learning Discussion Group Series, Microsoft Research, 2023 - 2024.
- American Control Conference, Chair, Nonlinear Systems Session, Denver, Colorado, July 2025.
- IEEE Control and Decision Conference, Chair, Numerical Methods in Control, Milano, Italia, December 2024.
- **Member**, IEEE Robotics and Automation Technical Committee on (i) Soft Robotics; (ii) Cognitive Robotics; (iii) Algorithms for Planning and Control; (iv) Automation in Health Care Management; (v) Aerial Robotics and Unmanned Aerial Vehicles. 2023 - Present.
- **Associate Editor**, [IEEE International Conference on Robotics and Automation (ICRA) Workshops](https://www.icra2023.org/), 2022-2023.
- **Associate Editor**, [IEEE International Conference on Robotics and Automation (ICRA)](https://www.icra2020.org/), 2020-2021.
- **External Grants Reviewer**, AI for Species Discovery, [National Geographic Society](https://www.nationalgeographic.org/), 2020 - 2021.
- **Journal Reviewer**: [Automatica (IFAC -- The International Federation of Automatic Control)](https://www.journals.elsevier.com/automatica"), IEEE Letters to Control Systems Society (L-CSS), IEEE Robotics and Automation Letters (RA-L), [Journal of Biomedical and Health Informatics](https://jbhi.embs.org/) (JBHI), Institute of Physics (IOP): The International Journal of Biomedical Physics and Engineering (PhysMed), [IEEE Access](https://ieeeaccess.ieee.org/?http://ieeeaccess.ieee.org/), [Neural Computing and Applications (NCAA)](https://link.springer.com/journal/521).
- **Conference Reviewer**: IEEE International Conference on Robotics and Automation (ICRA), IEEE International Conference on Decision and Control (CDC), IEEE/Robotics Society of Japan International Conference on Intelligent Robots and Systems (IROS), [Dynamic Systems and Control Conference -- The American Society of Mechanical Engineers (DSCC)](https://event.asme.org/DSCC), [American Control Conference (ACC)](http://acc2020.a2c2.org/), [International Conference on Machine Learning (ICML)](https://icml.cc/), [International Conference on Learning Representations (ICLR)](https://iclr.cc/), IFAC -- World Congress, Neural Information Processing Systems (NeurIPS).

 <h4><i class="fa fa-chevron-right"></i><i class="fa fa-chevron-right"></i>  Professional Activities.</h4>

 - [IEEE](https://www.ieee.org/), Member.
 - [IEEE RAS, Robotics and Automation Society](https://www.ieee-ras.org/), Member.
 - [IEEE CSS, Control Systems Society](https://www.ieeecss.org/), Member.
 <font size=2>(Strikethroughs signify societies I was a part of but whose membership I no longer belong).</font>
 - ~~[AAPM: The American Association of Physicists in Medicine](https://w3.aapm.org/my_aapm/index.php), Junior Member.~~
 - ~~[ASTRO, The American Society for Radiation Oncology](https://www.astro.org/), Member~~.
 - ~~[NYAS, The New York Academy of Sciences](https://www.nyas.org/), Member~~.


<a name="sports"></a>
<h4><i class="fa fa-chevron-right"></i><i class="fa fa-chevron-right"></i>Life, liberty, and the pursuit of the KOMs</h4>

<p>As often as I can get away from the lab, I like to ride my road bike. I ride rain or shine, hell or highwater -- whether it's in the parching heats of sultry Texas, or the blustering cold winds of the  Midwest and the Eastern Seaboard. States "bikeprint":  MA, NH, CT, NY, NJ, PA, DE, FL, TX, IL, WI, IN, HI, WA. Below is a screenshot of my recent activities summary. </p>
  <iframe height='160' width='400' frameborder='0' allowtransparency='true' scrolling='no' src='https://www.strava.com/athletes/29996478/activity-summary/a1ced5c81ee2203640950cbaf24d5fb53d84bafb'></iframe>

<br>
<h4><i class="fa fa-chevron-right"></i><i class="fa fa-chevron-right"></i> Recent Readings </h4>
 Below are the books in my current reading list.
 <h5><i class="fa fa-chevron-right"></i><i class="fa fa-chevron-right"></i> 2025 Readings</h5>
 -  Now it can be told: The story of the Manhattan project -- (General) Leslie M. Groves.
 -  The Idea Factory: Bell Labs and the Great Age of American Innovation -- Jon Gertner (H/T: <a href="https://www.microsoft.com/en-us/research/people/akshaykr/">Akshay</a>!).
 -  The Demon of Unrest -- Erik Larson (H/T: <a href="https://www.linkedin.com/in/julia-kirby-73b8b44/">Julia Kirby</a> for the rec!). 
 -  Successful Negotiating: Letting the Other Person Have <i>Your</i> way -- Ginny Pearson Barnes.
 -  On Natural Selection -- Charles Darwin.
 -  Isaac Asimov's Caliban -- Rober MacBride Allen.
 -  How to avoid a Climate Disaster -- Bill Gates.
 -  A Tale of Two Cities -- Charles Dickens.
 -  True Compass -- Edward Kennedy. 
 <h5><i class="fa fa-chevron-right"></i><i class="fa fa-chevron-right"></i> Oldies and Goodies</h5>
 -  Knowing Mandela -- John Carlin.
 -  The Startup Way -- Eric Ries.
 -  Democracy in America -- Alexis De Toqueville.
 -  The Sun Also Rises -- Ernest Hemingway.
 -  John Adams -- David McCullough.
 -  ~~The Federalist -- Alexander Hamilton, John Jay, and James Madison.~~
 -  ~~Team of Rivals: The Political Genius of Abraham Lincoln --  Doris Kearns Goodwin.~~
 -  ~~No Ordinary Time, Franklin and Eleanor Roosevelt: The Home Front in World War II -- Doris Kearns Goodwin.~~
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
