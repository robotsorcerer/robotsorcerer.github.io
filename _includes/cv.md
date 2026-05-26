
<h4 class="cv-h"><i class="fa fa-user"></i> Bio Snippet</h4>

<p><a href="https://en.wikipedia.org/wiki/Ikigai" target=_blank>Ikigai:</a> My research portfolio has a consistent throughline that is grounded in principled frameworks for autonomy viz., integrating <b>learning-enabled safety-critical control</b> and <b>systems representation</b> for <b>robust scalable decision-making (usually under uncertainty)</b>. My research arc spans MSR NYC, Amazon Robotics, UPenn, and UTD/UTSW. Prior to my academic career, I was in the manufacturing sector, integrating modern manufacturing processes in FMCG production lines with large-scale distributed supply chain management.</p> 

<div class="bio-timeline">
   <div class="bio-tl-item">
    <span class="bio-tl-year">2026 – Present</span>
    <div class="bio-tl-role">Senior Research Scientist, <a href="https://www.amazonrobotics.com">Amazon Robotics.</a>    </div>
  </div> 
  <div class="bio-tl-item">
    <span class="bio-tl-year">2025 – Present</span>
    <div class="bio-tl-role">Researcher, Stealth Research Lab.</div>
  </div>
  <div class="bio-tl-item">
    <span class="bio-tl-year">2021 – 2025</span>
    <div class="bio-tl-role">Senior Researcher, Microsoft Research Lab (NYC).</div>
  </div>
  <div class="bio-tl-item">
    <span class="bio-tl-year">2019 – 2021</span>
    <div class="bio-tl-role">Adjunct Faculty, <a href="https://brandeis.edu/">Brandeis University, Graduate School of Professional Studies</a>.</div>
  </div>
  <div class="bio-tl-item">
    <span class="bio-tl-year">2019 – 2021</span>
    <div class="bio-tl-role">Postdoctoral Researcher, <a href="https://www.med.upenn.edu/">University of Pennsylvania, Perelman School of Medicine</a>⏪Transferred from UChicago DCAM.</div>
  </div>
  <div class="bio-tl-item">
    <span class="bio-tl-year">2018 | 2016</span>
    <div class="bio-tl-role">Mechatronics Intern, <a href="https://www.amazonrobotics.com/#/">Amazon Robotics</a> (Advanced Robotics Lab), MA | Research Intern (Robot Learning), <a href="https://www.preferred-networks.jp/en/">Preferred Networks</a>, Tokyo.</div>
  </div>
<!--   <div class="bio-tl-item">
    <span class="bio-tl-year">2016</span>
    <div class="bio-tl-role">Mechatronics Intern, <a href="https://www.amazonrobotics.com/#/">Amazon Robotics</a> (Advanced Robotics Lab), Greater Boston, MA.</div>
  </div> -->
  <div class="bio-tl-item">
    <span class="bio-tl-year">2014 – 2019</span>
    <div class="bio-tl-role">PhD Student, <a href="https://ecs.utdallas.edu/~opo140030/">University of Texas at Dallas</a> &amp; Visiting Student, <a href="https://www.utsouthwestern.edu/labs/maia/about/meet-our-team.html">UT Southwestern Medical Center</a>.</div>
  </div>
  <div class="bio-tl-item">
    <span class="bio-tl-year">2011 – 2013</span>
    <div class="bio-tl-role">Student, <a href="https://www.sheffield.ac.uk/acse">University of Sheffield, Automatic Control and Systems Engineering</a>.</div>
  </div>
  <div class="bio-tl-item">
    <span class="bio-tl-year">2009 – 2011</span>
    <div class="bio-tl-role">(Manufacturing/Production) Supply Chain Manager, Apapa Plant, <a href="https://www.coca-colahellenic.com/">Coca-Cola Hellenic Bottling Company.</a></div>
  </div>
</div>


<a name="news"></a>
<h4 class="cv-h"><i class="fa fa-newspaper-o"></i> Select News Highlights</h4>

<div class="cv-news-feed">
  {% for item in site.data.news.news_items %}
  {% for subitem in item.subnewsitems %}
  {% unless subitem.highlight == false %}
  <div class="cv-news-item is-highlighted">
    <span class="cv-news-badge">{{ subitem.date }}</span>
    <span class="cv-news-text">{{ subitem.content }}</span>
  </div>
  {% endunless %}
  {% endfor %}
  {% endfor %}
</div>

<div class="cv-news-feed" id="news-more" style="display:none;">
  {% for item in site.data.news.news_items %}
  {% for subitem in item.subnewsitems %}
  {% if subitem.highlight == false %}
  <div class="cv-news-item">
    <span class="cv-news-badge">{{ subitem.date }}</span>
    <span class="cv-news-text">{{ subitem.content }}</span>
  </div>
  {% endif %}
  {% endfor %}
  {% endfor %}
</div>

<button class="mentoring-toggle" id="news-toggle">
  <i class="fa fa-chevron-down"></i> Show all news
</button>
<script>
document.getElementById('news-toggle').addEventListener('click', function(){
  var m = document.getElementById('news-more');
  var open = m.style.display !== 'none';
  m.style.display = open ? 'none' : 'block';
  this.innerHTML = open
    ? '<i class="fa fa-chevron-down"></i> Show all news'
    : '<i class="fa fa-chevron-up"></i> Show fewer';
});
</script>


<a name="talks"></a>
<h5 class="cv-h"><i class="fa fa-microphone"></i> Talk Highlights</h5>


<div class="talk-grid">
<!--  <div class="talk-card">
    <div class="talk-meta"><span class="talk-date">04/26</span><span class="talk-venue"><i class="fa fa-map-marker"></i> Amazon Robotics Fulfillment Technologies, MA/WA</span></div>
    <div class="talk-title"><a href="downloads/Papers/AR.pdf">Distributionally-Informed Production Control: Bridging Diffusion and HJ-Safety Verification.</a></div>
  </div>-->
  <div class="talk-card">
    <div class="talk-meta"><span class="talk-date">11/25</span><span class="talk-venue"><i class="fa fa-map-marker"></i> Chan-Zuckerberg Initiative, San Francisco, CA</span></div>
    <div class="talk-title"><a href="downloads/Papers/CZI.pdf" target=blank>Reinforcement and Supervised Learning in Medical Physics & Engineering</a></div>
  </div>
  <div class="talk-card">
    <div class="talk-meta"><span class="talk-date">09/25</span><span class="talk-venue"><i class="fa fa-map-marker"></i> Robotics &amp; AI Institute, Cambridge MA</span></div>
    <div class="talk-title"><a href="downloads/Papers/RAI-Inst.pdf" target=blank>Towards Ubiquitous Robotics Automation</a></div>
  </div>
  <div class="talk-card">
    <div class="talk-meta"><span class="talk-date">08/25</span><span class="talk-venue"><i class="fa fa-map-marker"></i> Google DeepMind Robotics, SF CA</span></div>
    <div class="talk-title"><a href="downloads/Papers/BostonDynamics.pdf" target=blank>State Representation in Reinforcement Learning</a></div>
  </div>
  <div class="talk-card">
    <div class="talk-meta"><span class="talk-date">08/25</span><span class="talk-venue"><i class="fa fa-map-marker"></i> Wayve Technologies, London UK</span></div>
    <div class="talk-title">System Identification for Planning in Reinforcement Learning</div>
  </div>
  <div class="talk-card">
    <div class="talk-meta"><span class="talk-date">08/25</span><span class="talk-venue"><i class="fa fa-map-marker"></i> Boston Dynamics, Waltham MA</span></div>
    <div class="talk-title"><a href="downloads/Papers/BostonDynamicsMain.pdf" target=blank>Embodied Intelligence in Open Embodiments</a> <a href="/BostonDynamicsApp.pdf" class="talk-appendix">Appendix</a></div>
  </div>
</div>

<div class="talk-grid" id="talks-more" style="display:none;">
  <div class="talk-card">
    <div class="talk-meta"><span class="talk-date">07/25</span><span class="talk-venue"><i class="fa fa-map-marker"></i> META Reality Labs, SF CA</span></div>
    <div class="talk-title"><a href="downloads/Papers/Yale.pdf" target=blank>Robustness and Efficient State Representation in Open Embodiments</a></div>
  </div>
  <div class="talk-card">
    <div class="talk-meta"><span class="talk-date">11/24</span><span class="talk-venue"><i class="fa fa-map-marker"></i> McGill University / MILA</span></div>
    <div class="talk-title"><a href="downloads/Papers/McGill.pdf" target=blank>Layered, Hierarchical Nonlinear Control of Soft Robotic Systems</a></div>
  </div>
  <div class="talk-card">
    <div class="talk-meta"><span class="talk-date">11/23</span><span class="talk-venue"><i class="fa fa-map-marker"></i> Yale University Engineering / CS</span></div>
    <div class="talk-title">Robustness and Convergence of Policy Optimization in Mixed H2/H-&#x221e; Stochastic Control</div>
  </div>
  <div class="talk-card">
    <div class="talk-meta"><span class="talk-date">Fall 2023</span><span class="talk-venue"><i class="fa fa-map-marker"></i> MSR Game Intelligence Group, Cambridge UK</span></div>
    <div class="talk-title"><a href="downloads/Papers/Yale.pdf" target=blank>Dynamics from Pixels as Time Integrations of Neural Lie Group Homomorphisms</a></div>
  </div>
  <div class="talk-card">
    <div class="talk-meta"><span class="talk-date">2022</span><span class="talk-venue"><i class="fa fa-map-marker"></i> MSR NYC</span></div>
    <div class="talk-title"><a href="/downloads/Papers/screw_slides.pdf" target=blank>A Short Treatise on the Kinematics and Kinetics of Robots</a></div>
  </div>
  <div class="talk-card">
    <div class="talk-meta"><span class="talk-date">Fall 2021</span><span class="talk-venue"><i class="fa fa-map-marker"></i> Microsoft Research Summit</span></div>
    <div class="talk-title">Learning without Rewards</div>
  </div>
  <div class="talk-card">
    <div class="talk-meta"><span class="talk-date">2021</span><span class="talk-venue"><i class="fa fa-map-marker"></i> Brandeis University</span></div>
    <div class="talk-title"><a href="/downloads/Papers/RBOT101.pdf" target=blank>The Mathematical Foundations of Robotics</a></div>
  </div>
  <div class="talk-card">
    <div class="talk-meta"><span class="talk-date">2021</span><span class="talk-venue"><i class="fa fa-map-marker"></i> MSR NYC / Auris Health (J&amp;J), SF</span></div>
    <div class="talk-title">Automating Treatment Planning in Radiation Therapy</div>
  </div>
</div>

<button class="mentoring-toggle" id="talks-toggle">
  <i class="fa fa-chevron-down"></i> Show all talks
</button>
<script>
document.getElementById('talks-toggle').addEventListener('click', function(){
  var m = document.getElementById('talks-more');
  var open = m.style.display !== 'none';
  m.style.display = open ? 'none' : 'grid';
  this.innerHTML = open
    ? '<i class="fa fa-chevron-down"></i> Show all talks'
    : '<i class="fa fa-chevron-up"></i> Show fewer';
});
</script>


<a name="mentor"></a>
<h4 class="cv-h"><i class="fa fa-users"></i> Mentoring Activities</h4>

<p style="font-size:.88rem;margin-bottom:10px;">Previous interns, postdocs, and students include:</p>

<div class="mentoring-grid">
  <div class="mentee-card">
    <a href="https://scholar.google.nl/citations?user=WCmrJoQAAAAJ&hl=en" target=blank>Taylor Webb</a>
    <div class="mentee-trail">Princeton Neuroscience PhD · UCLA Postdoc → MSR Postdoc '24/25 → Asst. Professor, Université de Montréal</div>
  </div>
  <div class="mentee-card">
    <a href="https://scholar.google.com/citations?user=RbczS_gAAAAJ&hl=en&oi=ao" target=blank>Leilei Cui</a>
    <div class="mentee-trail">MSR Intern '22 → NYU Engineering PhD → Postdoctoral Scholar, MIT → Asst. Professor, Univ. of New Mexico</div>
  </div>
  <div class="mentee-card">
    <a href="https://harwiltz.github.io/" target=blank>Harley Wiltzer</a>
    <div class="mentee-trail">MSR Intern '23 · McGill PhD (advised by <a href="https://www.cim.mcgill.ca/~dmeger/">Meger</a> &amp; <a href="http://www.marcgbellemare.info/">Bellemare</a>) → MTS, Inception Labs</div>
  </div>
  <div class="mentee-card">
    <a href="https://scholar.google.com/citations?user=6Oro5g8AAAAJ&hl=en" target=blank>Abulikemu Abuduweili</a>
    <div class="mentee-trail">CMU Robotics PhD → MSR Intern '24 → Researcher, Apple Robotics</div>
  </div>
</div>

<div class="mentoring-grid mentoring-overflow" id="mentoring-more" style="display:none;">
  <div class="mentee-card">
    <a href="https://koulanurag.dev/" target=blank>Anurag Koul</a>
    <div class="mentee-trail">Oregon State PhD · MSR Postdoc '23–'24 → Applied Scientist II, Amazon NYC</div>
  </div>
  <div class="mentee-card">
    <a href="https://shaoruchen.github.io" target=blank>Shaoru Chen</a>
    <div class="mentee-trail">Penn ESE PhD → MSR Postdoc '23–'24 → LinkedIn Senior ML Engineer</div>
  </div>
  <div class="mentee-card">
    Etiosa Omeike
    <div class="mentee-trail">Princeton ECE BS → MSR Undergrad Intern '23 → Yale CS PhD (advised by <a href="https://www.marynel.net/">Prof. Marynel Vazquez</a>)</div>
  </div>
  <div class="mentee-card">
    <a href="https://www.gbahati.com/home">Gilbert Bahati</a>
    <div class="mentee-trail">Caltech MechE PhD (advised by <a href="http://ames.caltech.edu/">Prof. Aaron Ames</a>)</div>
  </div>
  <div class="mentee-card">
    Harry Vuong
    <div class="mentee-trail">Brandeis MS '20/'21 → Robotic Systems Engineer, Universal Robots A/S</div>
  </div>
  <div class="mentee-card">
    <a href="https://www.linkedin.com/in/adwaitkulkarni93">Adwait Kulkarn</a>
    <div class="mentee-trail">Masters intern '17–'18 → VP Smart Trailer Engineering, <a href="http://drovtech.com">Drov. Tech, MN</a></div>
  </div>
  <div class="mentee-card">
    <a href="https://github.com/rsthomp">Rachel Thompson</a>
    <div class="mentee-trail">Plano HS '17 → UT Dallas → MIT CSAIL undergrad → Brown University PhD</div>
  </div>
  <div class="mentee-card">
    <a href="https://www.linkedin.com/in/ajithvenkateswaran">Ajith Venkateswaran</a>
    <div class="mentee-trail">Masters Intern '16–'17 → Amazon Robotics → J&amp;J → SW Tech Lead (Embedded Automotive), Wayve</div>
  </div>
  <div class="mentee-card">
    <a href="https://www.linkedin.com/in/blessingkolawole/">Blessing Kolawole</a>
    <div class="mentee-trail">Undergrad Assistant → CS PhD, Tufts University</div>
  </div>
</div>

<button class="mentoring-toggle" id="mentoring-toggle">
  <i class="fa fa-chevron-down"></i> Show all mentees
</button>
<script>
document.getElementById('mentoring-toggle').addEventListener('click', function(){
  var m = document.getElementById('mentoring-more');
  var open = m.style.display !== 'none';
  m.style.display = open ? 'none' : 'grid';
  this.innerHTML = open
    ? '<i class="fa fa-chevron-down"></i> Show all mentees'
    : '<i class="fa fa-chevron-up"></i> Show fewer';
});
</script>


<a name="service"></a>
<h4 class="cv-h"><i class="fa fa-university"></i> Editorial / Community Service</h4>

<div class="service-grid">
  <div class="service-card">
    <div class="service-card-label"><i class="fa fa-users"></i> Leadership &amp; Organization</div>
    <ul>
      <li><strong>Co-Organizer</strong>, Microsoft Cortex Research Series, FY25, 2024–2025.</li>
      <li><strong>Mentee Lead</strong>, (Microsoft) T&amp;R Mentoring Ring FY25, 2024–2025.</li>
      <li><strong>Co-Coordinator</strong>, RL Discussion Group Series, Microsoft Research, 2023–2024.</li>
    </ul>
  </div>
  <div class="service-card">
    <div class="service-card-label"><i class="fa fa-gavel"></i> Conference Chairing</div>
    <ul>
      <li>ACC, Chair — Nonlinear Systems Session, Denver, CO, July 2025.</li>
      <li>IEEE CDC, Chair — Numerical Methods in Control, Milano, Italia, Dec. 2024.</li>
    </ul>
  </div>
  <div class="service-card">
    <div class="service-card-label"><i class="fa fa-edit"></i> Editorial Roles</div>
    <ul>
      <li><strong>Associate Editor</strong>, <a href="https://www.icra2023.org/">ICRA Workshops</a>, 2022–2023.</li>
      <li><strong>Associate Editor</strong>, <a href="https://www.icra2020.org/">ICRA</a>, 2020–2021.</li>
      <li><strong>External Grants Reviewer</strong>, AI for Species Discovery, <a href="https://www.nationalgeographic.org/">National Geographic Society</a>, 2020–2021.</li>
    </ul>
  </div>
  <div class="service-card">
    <div class="service-card-label"><i class="fa fa-check-square-o"></i> Reviewing</div>
    <ul>
      <li><strong>Journals</strong>: Automatica, IEEE L-CSS, IEEE RA-L, JBHI, IOP PhysMed, IEEE Access, NCAA.</li>
      <li><strong>Conferences</strong>: ICRA, CDC, IROS, DSCC, ACC, ICML, ICLR, IFAC World Congress, NeurIPS.</li>
    </ul>
  </div>
  <div class="service-card service-card--wide">
    <div class="service-card-label"><i class="fa fa-sitemap"></i> IEEE Robotics and Automation Society Technical Committees</div>
    <p style="font-size:.82rem;margin:0;">Member, IEEE RAS TC on Algorithms for Planning and Control of Robot Motion. 2024 – Present.</p>
    <p style="font-size:.82rem;margin:0;">Member, IEEE RAS TC on Soft Robotics. 2023 – Present.</p>
    <p style="font-size:.82rem;margin:0;">Member, IEEE RAS TC on Cognitive Robotics. 2023 – Present.</p>
    <p style="font-size:.82rem;margin:0;">Member, IEEE RAS TC on Automation in Health Care. 2023 – Present.</p>
    <p style="font-size:.82rem;margin:0;">Member, IEEE RAS TC on Aerial Robotics. 2023 – Present.</p>
    <p style="font-size:.82rem;margin:0;">Member, IEEE RAS TC on UAVs. 2023 – Present.</p>
  </div>
</div>

<h4 class="cv-h"><i class="fa fa-briefcase"></i> Professional Memberships</h4>

<div class="memberships-wrap">
  <div class="memberships-active">
    <a href="https://www.ieee.org/" class="membership-chip" target="_blank"><i class="fa fa-check-circle"></i> IEEE</a>
    <a href="https://www.ieee-ras.org/" class="membership-chip" target="_blank"><i class="fa fa-check-circle"></i> IEEE RAS</a>
    <a href="https://www.ieeecss.org/" class="membership-chip" target="_blank"><i class="fa fa-check-circle"></i> IEEE CSS</a>
  </div>
  <div class="memberships-former">
    <span class="memberships-former-label">Former</span>
    <a href="https://w3.aapm.org/my_aapm/index.php" class="membership-chip membership-chip--former" target="_blank">AAPM</a>
    <a href="https://www.astro.org/" class="membership-chip membership-chip--former" target="_blank">ASTRO</a>
    <a href="https://www.nyas.org/" class="membership-chip membership-chip--former" target="_blank">NYAS</a>
  </div>
</div>


<a name="sports"></a>
<h4 class="cv-h"><i class="fa fa-bicycle"></i> Life, Liberty, and the Pursuit of KOMs</h4>

<div class="cycling-wrap">
  <div class="cycling-text">
    <p>When away from work, I am probably on my road bike. I ride rain or shine, hell or highwater. From the parching heats of sultry Texas to the blustering cold winds of the Northeast.</p>
    <div class="cycling-states-label">Countries bikeprint</div>
    <div class="cycling-states">
      <span><img src="https://upload.wikimedia.org/wikipedia/commons/4/41/Flag_of_Austria.svg" alt="Austria flag" style="height:1em;"> AT</span>
      <span><img src="https://upload.wikimedia.org/wikipedia/commons/c/cf/Flag_of_Canada.svg" alt="Canada flag" style="height:1em;"> CA</span>
      <span><img src="https://upload.wikimedia.org/wikipedia/commons/f/f3/Flag_of_Switzerland.svg" alt="Switzerland flag" style="height:1em;"> CH</span>
      <span><img src="https://upload.wikimedia.org/wikipedia/commons/b/ba/Flag_of_Germany.svg" alt="Germany flag" style="height:1em;"> DE</span>
      <span><img src="https://upload.wikimedia.org/wikipedia/commons/9/9a/Flag_of_Spain.svg" alt="Spain flag" style="height:1em;"> ES</span>
      <span><img src="https://upload.wikimedia.org/wikipedia/commons/b/bc/Flag_of_Finland.svg" alt="Finland flag" style="height:1em;"> FI</span>
      <span><img src="https://upload.wikimedia.org/wikipedia/commons/0/03/Flag_of_Italy.svg" alt="Italy flag" style="height:1em;"> IT</span>
      <span><img src="https://upload.wikimedia.org/wikipedia/commons/9/9e/Flag_of_Japan.svg" alt="Japan flag" style="height:1em;"> JP</span>
      <span><img src="https://upload.wikimedia.org/wikipedia/commons/7/79/Flag_of_Nigeria.svg?utm_source=commons.wikimedia.org&utm_campaign=index&utm_content=original" alt="Naija flag" style="height:1em;"> NG</span>
      <span><img src="https://upload.wikimedia.org/wikipedia/commons/5/5c/Flag_of_Portugal.svg" alt="Portugal flag" style="height:1em;"> PT</span>
      <span><img src="https://upload.wikimedia.org/wikipedia/commons/8/83/Flag_of_the_United_Kingdom_%283-5%29.svg?utm_source=commons.wikimedia.org&utm_campaign=index&utm_content=original" alt="UK flag" style="height:1em;"> UK</span>
      <span><img src="https://upload.wikimedia.org/wikipedia/commons/a/a4/Flag_of_the_United_States.svg" alt="US flag" style="height:1em;"> US</span>
    </div>
    <div class="cycling-states-label" style="margin-top:8px;">US States bikeprint</div>
    <div class="cycling-states">
      <span><img src="https://upload.wikimedia.org/wikipedia/commons/9/96/Flag_of_Connecticut.svg" alt="Connecticut flag" style="height:1em;"> CT</span>
      <span><img src="https://upload.wikimedia.org/wikipedia/commons/c/c6/Flag_of_Delaware.svg?utm_source=commons.wikimedia.org&utm_campaign=index&utm_content=original" alt="Delaware flag" style="height:1em;"> DE</span>
      <span><img src="https://upload.wikimedia.org/wikipedia/commons/f/f7/Flag_of_Florida.svg" alt="Florida flag" style="height:1em;"> FL</span>
      <span><img src="https://upload.wikimedia.org/wikipedia/commons/e/ef/Flag_of_Hawaii.svg" alt="Hawaii flag" style="height:1em;"> HI</span>
      <span><img src="https://upload.wikimedia.org/wikipedia/commons/a/ac/Flag_of_Indiana.svg" alt="Indiana flag" style="height:1em;"> IN</span>
      <span><img src="https://upload.wikimedia.org/wikipedia/commons/0/01/Flag_of_Illinois.svg?utm_source=commons.wikimedia.org&utm_campaign=index&utm_content=original" alt="Illinois flag" style="height:1em;"> IL</span>
      <span><img src="https://upload.wikimedia.org/wikipedia/commons/f/f2/Flag_of_Massachusetts.svg?utm_source=commons.wikimedia.org&utm_campaign=index&utm_content=original" alt="Massachusetts flag" style="height:1em;"> MA</span>
      <span><img src="https://upload.wikimedia.org/wikipedia/commons/2/28/Flag_of_New_Hampshire.svg" alt="New Hampshire flag" style="height:1em;"> NH</span>
      <span><img src="https://upload.wikimedia.org/wikipedia/commons/9/92/Flag_of_New_Jersey.svg" alt="New Jersey flag" style="height:1em;"> NJ</span>
      <span><img src="https://upload.wikimedia.org/wikipedia/commons/1/1a/Flag_of_New_York.svg" alt="New York flag" style="height:1em;"> NY</span>
      <span><img src="https://upload.wikimedia.org/wikipedia/commons/f/f7/Flag_of_Pennsylvania.svg" alt="Pennsylvania flag" style="height:1em;"> PA</span>
      <span><img src="https://upload.wikimedia.org/wikipedia/commons/2/28/Flag_of_Puerto_Rico.svg" alt="Puerto Rico flag" style="height:1em;"> PR</span>
      <span><img src="https://upload.wikimedia.org/wikipedia/commons/f/f7/Flag_of_Texas.svg" alt="Texas flag" style="height:1em;"> TX</span>
      <span><img src="https://upload.wikimedia.org/wikipedia/commons/2/22/Flag_of_Wisconsin.svg" alt="Wisconsin flag" style="height:1em;"> WI</span>
      <span><img src="https://upload.wikimedia.org/wikipedia/commons/5/54/Flag_of_Washington.svg" alt="Washington flag" style="height:1em;"> WA</span>
    </div>
  </div>
  <div class="cycling-strava">
    <iframe height='160' width='100%' frameborder='0' allowtransparency='true' scrolling='no'
      src='https://www.strava.com/athletes/29996478/activity-summary/a1ced5c81ee2203640950cbaf24d5fb53d84bafb'
      style="border-radius:8px;min-width:220px;max-width:340px;display:block;"></iframe>
  </div>
</div>


<h4 class="cv-h"><i class="fa fa-book"></i> Recent Readings</h4>
<div class="reading-shelf-label">2026</div>
<div class="book-grid">
  <div class="book-card">
    <div class="book-title">Eye of the Hurricane</div>
    <div class="book-author">Richard Bellman</div>
  </div>
  <div class="book-card">
    <div class="book-title">Endurance</div>
    <div class="book-author">Scott Kelly</div>
  </div>
  <div class="book-card">
    <div class="book-title">American Sniper</div>
    <div class="book-author">Chris Kyle</div>
  </div>
  <div class="book-card">
    <div class="book-title">Hot, Flat, and Crowded</div>
    <div class="book-author">Thomas L. Friedman</div>
  </div>
  <div class="book-card">
    <div class="book-title">The Odyssey</div>
    <div class="book-author">Homer, Translated by Robert Fitzgerald</div>
  </div>
  <div class="book-card">
    <div class="book-title">The World is Flat: A Brief History of the 21st Century.</div>
    <div class="book-author">Thomas L. Friedman</div>
  </div>
  <div class="book-card">
    <div class="book-title">Thomas Paine and the Clarion Call for American Independence</div>
    <div class="book-author">Harlow Giles Unger</div>
  </div>
  <div class="book-card">
    <div class="book-title">A Higher Loyalty</div>
    <div class="book-author">James Comey</div>
  </div>
  <div class="book-card">
    <div class="book-title">D-Day</div>
    <div class="book-author">Stephen Ambrose</div>
  </div>
  <div class="book-card book-card--read">
    <span class="book-read-badge"><i class="fa fa-check"></i> Read</span>
    <div class="book-title">Genghis Khan and the Making of the Modern World</div>
    <div class="book-author">Jack Weatherford</div>
  </div>
  <div class="book-card book-card--read">
    <span class="book-read-badge"><i class="fa fa-check"></i> Read</span>
    <div class="book-title">1929: Inside the Greatest Crash in Wall Street History -- And How It Shattered A Nation</div>
    <div class="book-author">Andrew Ross Sorkin</div>
  </div>
</div>

<div class="reading-shelf-label">2025</div>
<div class="book-grid">
  <div class="book-card book-card--read">
    <span class="book-read-badge"><i class="fa fa-check"></i> Read</span>
    <div class="book-title">Now It Can Be Told: The Story of the Manhattan Project</div>
    <div class="book-author">(General) Leslie M. Groves</div>
  </div>
  <div class="book-card book-card--read">
    <span class="book-read-badge"><i class="fa fa-check"></i> Read</span>
    <div class="book-title">The Idea Factory: Bell Labs and the Great Age of American Innovation</div>
    <div class="book-author">Jon Gertner</div>
  </div>
  <div class="book-card">
    <div class="book-title">Isaac Asimov's Caliban</div>
    <div class="book-author">Roger MacBride Allen</div>
  </div>
  <div class="book-card book-card--read">
    <span class="book-read-badge"><i class="fa fa-check"></i> Read</span>
    <div class="book-title">Now They Will Have to Die</div>
    <div class="book-author">James Verini</div>
  </div>
  <div class="book-card">
    <div class="book-title">Successful Negotiating: Letting the Other Person Have <em>Your</em> Way</div>
    <div class="book-author">Ginny Pearson Barnes</div>
  </div>
  <div class="book-card">
    <div class="book-title">True Compass</div>
    <div class="book-author">Edward Kennedy</div>
  </div>
</div>

<div class="reading-shelf-label" style="margin-top:18px;">Oldies &amp; Goodies</div>
<div class="book-grid">
  <div class="book-card">
    <div class="book-title">Knowing Mandela</div>
    <div class="book-author">John Carlin</div>
  </div>
  <div class="book-card">
    <div class="book-title">Democracy in America</div>
    <div class="book-author">Alexis De Tocqueville</div>
  </div>
  <div class="book-card">
    <div class="book-title">The Sun Also Rises</div>
    <div class="book-author">Ernest Hemingway</div>
  </div>
  <div class="book-card">
    <div class="book-title">John Adams</div>
    <div class="book-author">David McCullough</div>
  </div>
  <div class="book-card">
    <div class="book-title">On Natural Selection</div>
    <div class="book-author">Charles Darwin</div>
  </div>
  <div class="book-card">
    <div class="book-title">A Tale of Two Cities</div>
    <div class="book-author">Charles Dickens</div>
  </div>
  <div class="book-card">
    <div class="book-title">How to Avoid a Climate Disaster</div>
    <div class="book-author">Bill Gates</div>
  </div>

  
  <div class="book-card book-card--read">
    <span class="book-read-badge"><i class="fa fa-check"></i> Read</span>
    <div class="book-title">The Federalist</div>
    <div class="book-author">Hamilton, Jay &amp; Madison</div>
  </div>
  <div class="book-card book-card--read">
    <span class="book-read-badge"><i class="fa fa-check"></i> Read</span>
    <div class="book-title">The Demon of Unrest</div>
    <div class="book-author">Erik Larson</div>
  </div>
  <div class="book-card book-card--read">
    <span class="book-read-badge"><i class="fa fa-check"></i> Read</span>
    <div class="book-title">Team of Rivals</div>
    <div class="book-author">Doris Kearns Goodwin</div>
  </div>
  <div class="book-card book-card--read">
    <span class="book-read-badge"><i class="fa fa-check"></i> Read</span>
    <div class="book-title">No Ordinary Time</div>
    <div class="book-author">Doris Kearns Goodwin</div>
  </div>
  <div class="book-card book-card--read">
    <span class="book-read-badge"><i class="fa fa-check"></i> Read</span>
    <div class="book-title">1776</div>
    <div class="book-author">David McCullough</div>
  </div>
  <div class="book-card book-card--read">
    <span class="book-read-badge"><i class="fa fa-check"></i> Read</span>
    <div class="book-title">Founding Fathers</div>
    <div class="book-author">Gordon Leidner</div>
  </div>
  <div class="book-card book-card--read">
    <span class="book-read-badge"><i class="fa fa-check"></i> Read</span>
    <div class="book-title">Managing Up</div>
    <div class="book-author">Rosanne Badowski</div>
  </div>
  <div class="book-card book-card--read">
    <span class="book-read-badge"><i class="fa fa-check"></i> Read</span>
    <div class="book-title">Think Again</div>
    <div class="book-author">Adam Grant</div>
  </div>
  <div class="book-card book-card--read">
    <span class="book-read-badge"><i class="fa fa-check"></i> Read</span>
    <div class="book-title">Eye of the Hurricane: An Autobiography</div>
    <div class="book-author">Richard Bellman</div>
  </div>
  <div class="book-card book-card--read">
    <span class="book-read-badge"><i class="fa fa-check"></i> Read</span>
    <div class="book-title">Advice for a Young Investigator</div>
    <div class="book-author">Santiago Ramon y Cajal</div>
  </div>
  <div class="book-card book-card--read">
    <span class="book-read-badge"><i class="fa fa-check"></i> Read</span>
    <div class="book-title">Richard Feynman: A Life in Science</div>
    <div class="book-author">John &amp; Mary Gribblin</div>
  </div>
  <div class="book-card book-card--read">
    <span class="book-read-badge"><i class="fa fa-check"></i> Read</span>
    <div class="book-title">Made to Stick</div>
    <div class="book-author">Chip Heath &amp; Dan Heath</div>
  </div>
  <div class="book-card book-card--read">
    <span class="book-read-badge"><i class="fa fa-check"></i> Read</span>
    <div class="book-title">Profiles in Courage</div>
    <div class="book-author">John Fitzgerald Kennedy</div>
  </div>
</div>
