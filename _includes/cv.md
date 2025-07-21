
<h4><i class="fa fa-chevron-right"></i><i class="fa fa-chevron-right"></i><a href="https://en.wikipedia.org/wiki/Ikigai">Ikigai || TL; DR </a></h4>
- **Emergent embodied intelligence** via morphological computation in physically adaptible and reactive robotic systems (including soft robots and deformables): finite reduced-order, fractional, and learned models, ode- and pde-based control, time-scale separation of heterogeneous dynamics, and layered control.<br>
- **Machine learning (read: optimization) in control and planning**: Self-aware, situationally-aware systems (e.g. physical robots, augmented, and virtual reality agents) that self-organize by systemic constraints (read: not imposed objectives).
- **Safety in decision-making**: HJ equations, and constrained numerical algorithms.

 
<h4><i class="fa fa-chevron-right"></i><i class="fa fa-chevron-right"></i>Bio Snippet</h4>

<b>Full-stack, innovation-oriented roboticist</b> (rigid, semi-rigid, and soft) -- mechanism design, (constrained) [configuration](/downloads/Papers/RBOT101.pdf) and [kinematic analysis](/downloads/Papers/screw_slides.pdf), and [AI/ML stack](downloads/Papers/IROS18.pdf). Algorithmics expertise encompassing the theory and practice of the AI, ML, and Control automation stack in virtual and physical automatons. Currently, a Senior Researcher within the Machine Learning group at Microsoft Research Core -- New York City. Research efforts span the complete ideation gamut from conceptualization, rigorous theoretical analysis, to abundant empirical and embodied proof-of-concept on real-world physical systems: Lekan has worked on (i) [understanding the fundmental modeling](/downloads/Papers/SoRoPD.pdf) blocks and devising principles for the [fast whole-body layered control of soft, deformable robots](/downloads/Papers/SoRoSPT.pdf) -- inpired by [his previous efforts in their applications to head and neck coplanar cancer radiation therapy](/downloads/Papers/ContinuumI.pdf); (ii) [RL state representation theory](https://arxiv.org/pdf/2207.08229.pdf); (iii) the role of [RL in the fractionated cancer radiation patient treatment planning stack](https://aapm.onlinelibrary.wiley.com/doi/abs/10.1118/1.4924100). Not too long ago, hemmed in by the delayed rewards associated with RL, with his colleagues they were concerned with (iv) [the theory behind agentic systems that learn instanteneously via interaction](https://arxiv.org/abs/2206.08364); and encumbered by safety of learned Bellman-like policies deployed in hazardous environments, he recently contributed a (v) [the scalable library for the numerical computation of safety certificates](/downloads/Papers/levelsetpy.pdf) when [controlling large-scale dynamical systems](https://arxiv.org/pdf/2403.07308.pdf). Before multimodal learning was cool, at Amazon Fulfillment Technlogies, he orchestrated a full-stack navigation system on the Pioneer P3-DX robot based on [Alexa's Echo](https://www.amazon.com/b/?node=9818047011&ref_=mars_byline_aucc_branded) voice commands and pixel-based navigation. Before behavior cloning became cool, he explored [learned nonlinear controllers via human imitation](https://github.com/robotsorcerer/LyapunovLearner) on the [Torobo anthropomorphic robot arm](https://robotics.tokyo/products/torobo/), based on dynamical systems and Lyapunov analysis. These days, when Lekan is among his friends, they ask one another ["how do we create efficient numerical algorithms  for agentic systems](https://www.ibm.com/think/topics/agentic-ai-vs-generative-ai) tasked with autonomous navigation and dexterous manipulation within [multimodal, unstructured, non-localized open-embodiments](https://arxiv.org/pdf/2503.20020)"? What a hard-knock life! Among other service activities within and without MSFT, Lekan is a part of the robotics steering committee out of the [embodied AI research efforts](https://www.microsoft.com/en-us/research/collaboration/embodied-ai/people/) within the various cross-geographic teams throughout the company; he helped seed the current Cortex seminar series from a narrow RL research focus to a company-wide appeal within MSFT. Lekan is active in the machine learning, IEEE Control Systems, and IEEE Robotics and Automation Societies. The questions that keep Lekan up at night can be found on his [research page](/research). So is Lekan a research scientist or an Engineer? Day of the week and the problem-at-hand, if you ask him.

PS: Lekan Molu is the double diminutive form of Olalekan Ogunmolu, my full legal name. I prefer to go by Lekan Molu in all professional and informal settings. You are welcome!

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

<a name="mentor"></a>
 <h4><i class="fa fa-chevron-right"></i><i class="fa fa-chevron-right"></i>  Mentoring Activities.</h4>

Previous interns, postdocs, and students include:

+ [Taylor Webb](https://scholar.google.nl/citations?user=WCmrJoQAAAAJ&hl=en). Princeton Neuroscience PhD; UCLA Postdoc &rarr; MSR Postdoc, '24/25   &rarr; Assistant Professor, University de Montreal.
+ [Leilei Cui](https://scholar.google.com/citations?user=RbczS_gAAAAJ&hl=en&oi=ao). MSR Intern, '22   &rarr; NYU Engineering PhD &rarr; Posdoctoctoral Scholar, MIT &rarr; Assistant Professor, Univ. of New Mexico.
+ [Hanwen Cao](https://hwcao17.github.io/). UCSD PhD Student &rarr; MSR Intern '25 (co-advised by [Jeff](https://www.microsoft.com/en-us/research/people/jedelmer/), [Akshay](https://people.cs.umass.edu/~akshay/), [Nikolay](https://natanaso.github.io/), and [Yulun](https://tianyulun.com/)). 
+ [Abulikemu Abuduweili](https://scholar.google.com/citations?user=6Oro5g8AAAAJ&hl=en). CMU Robotics PhD student &rarr; MSR Intern '24 (co-advised by [Elise van der Pol](https://www.elisevanderpol.nl/), and [Naoki Wake](https://www.microsoft.com/en-us/research/people/nawake/)) &rarr; Research Scientist, Reliant Robotics.
+ [Anurag Koul](https://koulanurag.dev/), Oregon State PhD, MSR Postdoc, '23-'24 &rarr; Applied Scientist II, Amazon NYC.
+ [Shaoru Chen](https://shaoruchen.github.io). Penn ESE PhD, University of Pennsylvania &rarr; MSR Postdoc ('23-'24) &rarr; LinkedIn ML Engineer.
+ Etiosa Omeike. Princeton ECE BS &rarr;  MSR Undergrad Intern, 2023 &rarr; Yale CS PhD student (advised by [Prof. Marynel Vazquez)](https://www.marynel.net/).
+ [Thomas Zhang](https://thomaszh3.github.io/), MSR Intern, '23. UPenn PhD Student advised by [Prof. Nik Matni](https://nikolaimatni.github.io/).
+ [Gilbert Bahati](https://www.gbahati.com/home), Caltech MechE PhD Student (Advised by Prof. [Aaron Ames](http://ames.caltech.edu/)).
+ [Haoxiang You](https://ialab.yale.edu/members/haoxiang-you.html). Yale MAE PhD Student. Advised by Prof. [Ian Abraham](https://ialab.yale.edu/).
+ Harry Vuong. Brandeis University MS 2020/2021 &rarr; Robotic Systems Engineer, Universal Robots A/S. 
+ [Harley Wiltzer](https://harwiltz.github.io/), MSR Intern, 2023. McGill PhD Student advised by [David Meger](https://www.cim.mcgill.ca/~dmeger/) and [Marc Bellemare](http://www.marcgbellemare.info/).
+  [Adwait Kulkarn](https://www.linkedin.com/in/adwaitkulkarni93), 2017-2018 Masters intern &rarr; (VP of Smart Trailer Engineering, [Drov. Tech, MN](http://drovtech.com)).
+  [Rachel Thompson](https://github.com/rsthomp), 2017 Plano High School &rarr; University of Texas as Dallas &rarr; MIT CSAIL undergrad &rarr; Brown University PhD.
+  [Ajith Venkateswaran](https://www.linkedin.com/in/ajithvenkateswaran), 2016-2017 Masters Intern &rarr; Amazon Robotics LLC &rarr; University of Texas at Dallas &rarr; Senior Software Engineer, Johnson & Johnson &rarr; SW Tech Lead (Embedded Automotive Platforms), Wayve.
<!-- +  [Blessing Kolawole](https://www.linkedin.com/in/blessingkolawole/), Undergrad Assistant. (CS PhD student, Tufts University). -->
 
<a name="talks"></a>a>
<h4><i class="fa fa-chevron-right"></i><i class="fa fa-chevron-right"></i> Select Talks, Classes, and Conferences</h4>
<h5><i class="fa fa-chevron-right"></i><i class="fa fa-chevron-right"></i>Talk Highlights</h5>
- [Layered, hierarchical nonlinear control of soft robotic systems](downloads/Papers/McGill.pdf), McGill University Engineering/MILA, Nov. 2024.
- [On the Robustness and Convergence of Policy Optimization in Continuous-Time Mixed H2/H-infinity Stochastic Control](#), Yale University Engineering/CS Faculty, New Haven, Conn. Fall 2023.
- [Dynamics from Pixels as Time Integrations of Neural Lie Group Homomorphisms](downloads/Papers/Yale.pdf), MSR Game Intelligence Group, Cambridge, UK. Fall 2023.
- Learning without Rewards, [Microsoft Research Summit](https://www.microsoft.com/en-us/research/event/microsoft-research-summit-2021/), Fall 2021.
- [A Short Treatise on the Kinematics and Kinetics of Robots -- Slides](/downloads/Papers/screw_slides.pdf), MSR NYC, 2022.
- [The Mathematical Foundations of Robotics](/downloads/Papers/RBOT101.pdf), Brandeis University, 2021.
- [Robot Manipulation, Planning and Control](/downloads/Papers/RBOT250.pdf), Brandeis University, 2020.
- [L1 Adaptive Control -- Courtesy of Naira Hovakimyan. 10/1/2015](/downloads/Papers/L1Adaptive.pdf)
- [Automating Treatment Planning in Radiation Therapy](#), Microsoft Research NYC, New York City, Winter 2021.
- [Automating Treatment Planning in Radiation Therapy](#), Auris Health, Johnson & Johnson, San Francisco, CA, 2021.
- Soft Robots-based Position Correction Mechanisms in Intensity-Modulated Radiation Therapy. Open Robotics Foundation, Mountain View, CA, USA, 2019.
- Robotic Radiotherapy: Automating Position Correction in Intensity-Modulated Radiation Therapy, Department of Energy Resources Engineering. Stanford University, Stanford, CA, USA, 2018.
- Robotic Radiotherapy: Automating Position Correction in Intensity-Modulated Radiation Therapy, Department of Radiation and Cellular Oncology, The University of Chicago, Chicago, IL, USA, 2018.
- Minimax Iterative Dynamic Game, Department of Brain Robot Interface. Computational Neuroscience Labs, ATR, Osaka, Japan, 2018.  
- Soft Robotic Modules as Position Correcting Mechanisms in Cancer RT, 3rd Entrepreneurship Forum & Start-up Competition, EFSC'17, Vancouver, BC, Canada, 2017.
- Neural Networks and Adaptive Control, Preferred Networks Tech. Talk, Chiyoda-ku, Tokyo. Japan, 2018. 
<br>

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
