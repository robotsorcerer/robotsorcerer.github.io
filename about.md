---
layout: page
permalink: about
mathjax: true
---

<?php include_once("analyticstracking.php") ?>

### Intro

<!-- #### Tell me what you got -->

Welcome to my web presence! I am an `interdisciplinary researcher` who combines the scientific elegance of `machine learning` and `control theory` with the practical impact of `robotics` to create technological solutions for cancer  patients' healthcare. I am currently a postdoctoral researcher at the `University of Pennsylvania's School of Medicine` and I was previously a visiting postdoctoral scholar at the `University of Chicago's School of Medicine`. I work on problems spanning `conceptualization` of new `hardware`  and `software` tools for improving the `treatment planning` process in `cancer radiation therapy`. I am largely an independent researcher who enjoys self-direction at my own projects/goals. Yet, I value collaboration across domains and with people of diverse expertise. I read widely and study avidly: my interests span the sciences, technical disciplines (hello, chemistry, physics and engineering) to history and public affairs (really?). A big believer in open science and reproducible research, I try to make my publications and codes public to the extent that I can: see my [publications page](/pubs) and  [github repos](https://github.com/lakehanne). I am particularly mindful of inclusion in hi-tech, STEM, policy-making, and governance. **I am not a robot**. My PGP key on most public key servers is 03E3 58FB 1D98 869E 8ABE 1EF0 E6A1 2F95 B720 BBB5.  

**TL;DR**: I study, build, and use robots, oftentimes tinkering with AI-based control systems. 

<!-- My work has made meaningful impact in disciplines within and outside medicine and engineering, with citations from government and highered learning research institutions across the globe. 
Example institutions that have used my work include the National Aeronautics and Space Agency's Jet Propulsion Laboratory (NASA JPL), the 6th R&D institute of South Korea's Agency for Defense Development, Uber AI Labs, and the Chinese Academy of Sciences among others. -->

### Research Abridgment

Across our planet, in rich and poor nations alike, cancer remains an existential burden on healthful living.  In 2019 alone, an estimated 1,762,450 new cancer cases will be diagnosed in the United States, whereupon 606,880 cases will lead to fatality<sup>[ACS 2019](https://www.cancer.org/research/cancer-facts-statistics/all-cancer-facts-figures/cancer-facts-figures-2019.html)</sup>. This is projected to cost approximately $147.3 billion or 4.2% of overall health care spending (per 2017 budget). Cancer mortality is having pronounced effects on low- and middle-income countries as well with the International Agency for Research on Cancers estimating that the highest cancer incidence will fall on low- and middle-income countries over the coming decades <sup>[IARC Report 2019][IARC2019]</sup>. 

Means of treating cancers may include one or a combination of drugs, radiation therapy, immunotherapy,  stem cell transplant, targeted therapy, precision therapy, chemotherapy or surgery. Among the different locations where cancers can exist in the human body, cancers of the head and neck (H&N) region tend to be most fatal because of the sensitivity of  H&N organs. Thus, an all-of-the-above solution is not always the most suitable means for treating H&N cancers. 
Radiation Therapy (RT), often in conjunction with surgery and chemotherapy, is an invaluable single cancer treatment modality nowadays owing to its cost-effectiveness (accounting for only 5% of the total cost of cancer care <sup>[Ringborg Report][RingborgReport]</sup>, and its advanced mode of radiation production and delivery: shaping the geometry of high-energy  conformal radiation so that it allows radiation escalation to a tumor target while simultaneously sparing organs-at-risk (OARs). Matter-of-factly, half of all cancer patients do undergo RT treatment during the course of their illness with an estimated 40% of all  curative treatment being performed using RT<sup>[Cancer and RT](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3298009/)</sup>. Owing to its advanced radiation delivery method, RT is often the most suitable treatment method for H&N cancers. 

Owing to the accurate dose realization requirement in RT delivery, the head and neck region must be made immobile during the administration of dose, as motions of the order of 2mm or 2 degrees deviation from a desired trajectory can cause eczema, brain lesions or other post-treatment complications. The state-of-the-art positioning method for avoiding dose miss is to immobilize the patient with rigid metallic frames or masks<sup>[Fig 1](#fig-rigid)</sup>. 

{% 
    include fig.html 
        file='assets/head-plastic.jpg' 
        max-width='45%' 
        align='left'
        float='left'
%}
{% 
    include fig.html 
        file='assets/head-rigid.jpg' 
        max-width='75%' 
        align='middle'
        float='middle'
        caption='<b>Fig 1</b>: <i>(Left)</i> H&N immobilized with Thermoplastic Mould. <i>(Right)</i> H&N immobilized with Rigid Frame. A screw is typically drilled into the skull to render the patient immobile. The mask is further secured to the table with mechanical screws. Masks and frames generally attenuate high-energy photons meant to deliver curative dose to tumor.'
%}

<br>

Mask-based immobilization uses thermoplastics  (see left inset of [Fig 1](#fig-rigid)). Before the patient wears the mask, the solid thermoplast is allowed to stretch by heating it in water to a preset temperature. When the molecular bonds in the thermoplast weaken, a patient may wear it and use it to secure their head to the couch on which they supinely lie. However, these masks reduce immobilization accuracy owing to flex (producing a drift of up to \\(6mm\\)) as well as shrinkage. For deep tumors nearby sensitive organs such as the brain stem, or for  single isocenter multiple-target stereotactic radiosurgery (SRS) treatment modalities, masks are not suitable given the high sensitivity of head motion along the rotatory axis.

Frame-based immobilization involves a metal ring screwed to the skull of the patient, which is then bolted to the treatment table (see right inset of [Fig 1](#fig-rigid)). The invasive nature and discomfort of the frame causes poor compliance to trajectory tracking and reduces clinical efficacy. Even so, for certain patients frame placement is impossible given their unique cranial anatomy or prior surgical bone flaps; the frame limits the use of multiple RT delivery as patients cannot be subjected to daily attachment and removal of the frame. 

Setup errors between fractionated treatments (interfractional errors) or patient motion errors during a treatment session (intrafractional errors) often need to be corrected _in real-time_ during treatment. Currently in clinics, the treatment is stopped, and the machine is recalibrated when the error is too large for this process to go on. The discomfort caused by head and neck masks and frames in prolonged treatment (i) can increase the voluntary and involuntary motion of  patients; (ii) are time-consuming to calibrate on a treatment machine since doses are usually delivered in fractions over many weeks or months; (iii) lack real-time position correction of the patient's head motion; and (iv) have been known to cause patient discomfort after treatment. 


{% 
    include fig.html 
        file='assets/cyberknife.jpg' 
        max-width='85%' 
        align='middle'
        caption='<b>Fig 2:</b> The beam repositioning system ©Cyberknife.'
%}
<br>

The CyberKnife system (see Fig 2), in spite of its advanced mode of beam repositioning and radiation delivery, requires a frame or an immobilization mask, and is incapable of real-time closed-loop feedback head motion corrections when the treatment beam is on. The CyberKnife Synchrony, while capable of precise, non-surgical tumor and lesions treatment in SRS and stereotactic body radiotherapy (SBRT), only executes _a-priori_ trajectories; furthermore, it is only FDA-approved for lung tumors' treatment; correction requirements in systems such as this require far less accuracy, typically \\(< 5mm\\)<sup>[Keall-Report]</sup>than brain targets. Additionally, real-time closed-loop head motion compensation for the CyberKnife system is inhibited by its high load-to-weight ratio which indirectly affects its repeatability: as an open-loop kinematic chain, it exhibits poor accuracy since the weight of the segments that follow each link in the robot and the load of the mechanical structure contributes to the large flexure of torques; its links inherently magnify errors from shoulder out to the end-effector, consequently hampering its use for sophisticated control strategies that may minimize or eliminate load-dependent errors; additionally, its setup distance from the patient is a recipe for delayed execution of control laws in ensuring that radiation beam reaches its target without significantly affecting dose delivery. Given its stiffness (it weighs 160kg), it exhibits a high load-to-weight ratio, with a complicated actuation system so that its passive bending stiffness overwhelms the degree of deformation for rapid patient repositioning. 

positioning systems are an emerging non-invasive immobilization technology in radiosurgery; they work without utilizing rigid masks and frames -- reducing side effects and optimizing patient comfort with little trade-off in efficiency or effectiveness. The goal is to correct patient motion, ideally with a closed-loop feedback controller implemented  in real-time on a high-precision robotic system -- improving the satisfaction of patients and clinicians, and maximizing dose delivered to a tumor whilst minimizing healthy tissues' exposure to radiation. Parallel robot configurations have found good use along this research thrust. This is despite their higher number of actuated joints. In a way, this is an advantage because they distribute the weight of the load around the links of the robot, improving manipulation accuracy as a result; they also exhibit a desirable lightness property (albeit at the expense of a reduced workspace), and minimize the flexure torques that are otherwise common with open-loop kinematic chains. Thus, parallel kinematic configurations, in theory, enable greater precision with minimal control complications owing to the non-cummulativeness of actuator errors<sup>[Hunt1983]</sup>.

Recent F&M research research directions include the steel-cast assembled 4-DOF robot of [Wiersma Group][Xinmin4DOF], which corrected all translation axis motion and a pitch rotatory head motion; the HexaPOD parallel manipulator of [Coventry Uni's Group][HerrmannHexaPODMPC] utilized a system identification and model predictive control approach to correct a tumor position on an Hexapod; or the in-house fabricated 6-DOF Stewart-Gough platform of [Wiersma Group][BelcherThesis]. However, these configurations systems share common drawbacks e.g.

+ given their constant-curvature end-effectors/platforms, they are incapable of providing sophisticated manipulation e.g. for the inadvertent respiratory motions that often induce deviation from a target in RT;
    
+ being made out of rigid bodies, the attenuation of ionizing radiation dose has to be factored into treatment plans when these systems get commissioned; and
    
+ exhibiting planar platforms/tool frames, there is an inherent delay in head motion compensation along the patient's frontal axis that may inhibit clinical accuracy.
 
To improve the treatment planning process, these drawbacks need to be addressed. This would require the interdisciplinary effort of engineers, roboticists, physicists, and surgeons alike. In my line of work, we try to sidestep these issues. Our philosophy is to do away with radio-opaque/rigid bodies in the parallel robot compensation mechanism. Fundamentally, we utilize inflatable air bladders (`IABs`) to mitigate these highlighted issues. These `IABs` are continuum, compliant and configurable (C<sup>3</sup>) soft elastomeric actuators, with internal hollow chambers, and an external material shell -- so chosen to provide therapeutic and comfortable patient motion compensation during RT. Most of my PhD work was focussed on a system identification and statistical approach to their modeling; owing to their medium fidelity in control scenarios, I mitigated unmodeled dynamics and model uncertainties using standard techniques from indirect adaptive control (with projection to handle unbounded errors), optimal control (for setpoint/trajectory regulation) and some neural network adaptive control laws to mitigate unmodeled uncertainties in the system model. In the latter part of my PhD, I started thinking more about deriving closed-form expressions for their kinematics. With continuum mechanics and elastic deformations, we are now able to derive the `soft ik`,  and the dynamical model that governs their deformation is derived from `Cauchy's laws of motion` and `Truesdell's determinism for the stress principle`. Writing the direct kinematics of the mechanism becomes a relatively easier problem, allowing for elegant mathematical formulae in predicting a deformation behavior under a given stress and/or internal pressurization. A prototype of the SoRo Mechanism for manipulating the H&N region of a patient in stereotactic radiosurgery is shown in Fig. 3. I invite you to look through my [publications](/pubs) if you are further interested in this research.

{% 
    include fig.html 
        file='assets/setup.png' 
        max-width='95%' 
        align='middle'
        caption='<b>Fig 3: </b>C<sup>3</sup> SoRos in a parallel kinematic configuration around the Head and Neck Region. © Lekan Molu, 2019. Thanks to Erik Pearson of UChicago RadOnc for the CAD Model of the Gantry and Turntable.'
%}
<br>

They inflate, deflate, extend or contract governed by their material moduli, incompressibility and internal pressurization when given a reference trajectory. By controlling the amount of fluid in the internal cavities of these IABs, we can compensate motion deviation in real-time. Our hardware design absorbs the reactive pressure from the patient's displacement during manipulation, guaranteeing patient's comfort. Their radio-transparency to ionizing radiation make situating them close to the tumor source an attractive option for fast motion compensation -- mitigating against the inherent delay between the computation of control signals and actuation in rigid compensation works. 
<!-- 
For more background on this research, head over to [our group page](https://radonc.uchicago.edu/) and see our publications. -->

<!-- In a broader scope, my work explores better model representation in dynamical systems using state-of-the-art neural network function approximators, for example in adaptive control or model predictive control of complex nonlinear systems. My background is in Physics and Control theory and I spend my research exploring better ways of automating motion alignment correction systems in clinical cancer radiotherapy of malignant cancers of the head and neck region. The novelty of my work includes (i) the design and use of soft robots with morphological computation properties to dynamically adjust patient motion along desired degrees of freedom during cancer radiotherapy treatment; (ii) leveraging Cosserat's beam theory, nonlinear deformation theory, finite elastic deformation, Luh's algorithm, and screw theory for the kinodynamic planning and execution of trajectories by these soft and semi-rigid continuum robots. -->

<!--
#### Research Background

In stereotactic radiosurgery of the head and neck region, patients are typically positioned in a supine manner on a 6-DOF robotic couch for motion alignment correction with respect to an incident radiation. As such, the precision of delivery of radiation dose to target tumor is extremely important. Target miss in dosimetry angle or errors arising from patient positioning have been known to cause eczema, brain complications, and the exposure of organs at risks.
{% include fig.html
max-width="200px" file="/imgs/homepage/igrt_setup.jpg" alt="igrt setup"
float="right"  border="1px dotted black"  margin="0px 0px 15px 20px" align="right"
 %}
To prevent the patient from drifting from pre-calibrated pose on the 6-DOF robotic treatment couch, clinicians fixate metallic rings/frames, or elastic plastic masks on the patient's head and neck region so that involuntary motion by the patient is greatly minimized. But the use of such rings or masks have undesirable effects such as attenuating the radiation beam (thus minimizing incident dose and treatment efficacy), or making the patient uncomfortable.
The majority of such masks employed do not compensate for real-time patient deviation from planned targets. To compensate for such drifts, I proposed a [neuro-adaptive controller][iros-paper] for a network of compliant soft-robot systems to automatically move the patient's head and neck to desired pose based on a learning based finite-state machine.

{% include fig.html
max-width="100px" file="/imgs/homepage/moveit.jpg" alt="igrt setup"
float="right"  border="1px dotted black"  margin="0px 0px 15px 20px" align="right"
 %}

The idea is that by actuating elastomeric polymer enclosures that inflate or deflate based on the amount of air that is sent into them or by the amount of pressure that is exerted on them by a human-body part (such as the head or neck), one can achieve a desired level of pose in frameless or maskless radiotherapy without sacrificing patient comfort or treatment efficacy as existing technologies allow. -->

### Origins of this specie

I was ~~buttered and bread~~ born and bred in Southern Nigeria. I spent most of my adolescent years in the only logical place in the whole wide world where one can maximize one's 'life-fun-index': [Lagos](https://en.wikipedia.org/wiki/Lagos). I speak and write fluently in [Yoruba](https://en.wikipedia.org/wiki/Yoruba_language) and English -- languages I have used throughout my entire life. Having lived in Japan, I acquired a basic understanding of ~~Japaneasy~~ Japanese. I am working on a working-level proficiency (still another mile!). I love to meet people from other places and backgrounds -- it strengthens my understanding of the human culture. My accent has often been compared to the French one, though I have no idea what that is. I enjoy Afro-Jazz, Japanese Jazz, and alternative rock music genres. I do have an electric guitar, which I lazily play when I'm depressed. Someday, I do hope to be a street entertainer (_wouldn't that be fun?_).
There are many places I call home including [Chicago](http://www.todayifoundout.com/index.php/2013/07/how-chicago-got-its-name/), [Lagos](https://en.wiktionary.org/wiki/Lagosian),  [Sheffield](https://www.urbandictionary.com/define.php?term=Sheffielder), and Boston. 
<!--At various times in my little time on this planet, I have been a [_Shikaakwaan_](http://www.todayifoundout.com/index.php/2013/07/how-chicago-got-its-name/), a _[Lagosian](https://en.wiktionary.org/wiki/Lagosian)_, a _[Sheffielder](https://www.urbandictionary.com/define.php?term=Sheffielder) (home of my forever friends)_, a _Bostonian_, a _Londoner_, an _[Edokko](https://web-japan.org/tokyo/know/edokko/edo.html)_,  and a  _[Dallasite](https://www.dmagazine.com/frontburner/2012/01/are-we-dallasites-or-dallasonians-fort-worthers-or-fort-worthians-etymology-tells-us-who-we-are/) (Eh!)_.  -->

### Miscellaneous

+   I fancy conceptualization, finding issues and directions, definitions, expositions and critical insight. I like to investigate the physics behind machines, and to understand the interconnectedness of components, seeing design flaws,  and improvising upon them.

<!-- + I regularly peer-review for the following academic conferences and journals:

    &nbsp; &nbsp; &nbsp; &nbsp; - Institute of Physics: Measurement Science and Technology (Journal)

    &nbsp; &nbsp; &nbsp; &nbsp; - International Conference on Robotics and Automation (ICRA)

    &nbsp; &nbsp; &nbsp; &nbsp; - International Conference on Intelligent Robots and Systems (IROS)

    &nbsp; &nbsp; &nbsp; &nbsp; - Neural Computing and Applications (NCAA Journal)

    &nbsp; &nbsp; &nbsp; &nbsp; - International Federation of Automatic Control (IFAC) World Congress

    &nbsp; &nbsp; &nbsp; &nbsp; - American Control Conference (ACC) -->

<!-- + I had my masters degree in Control Systems from Sheffield Uni in the UK.

+ I had my Bachelors in Physics. Specifically, my thesis was on the single fractional parentage coefiicients in the sd-shell nuclei, advised by [Prof. Ademola Amusa](https://www.linkedin.com/in/ademola-amusa-b40812122/). -->

<!-- + In a previous life, I was a manager at Coca-Cola HBC. The thrill of discovery and the joy  of creative achievement led me to embrace the limited earning prospects of an academic life. -->

+ ~~I am a co-owner of the Linux, OpenStack, and Unix Networking video tutorials on [this](https://www.youtube.com/channel/UC-0PMn0rKV_ZOHF-qX6N3fQ/videos) youtube page.~~ Too busy eating cheap seminar foods on campus. [Strong Reject!](http://strongreject.com/)

+ ~~I am a member of North Texas Drone Users Group. We fly our drones, micro-UAVs, and mini-planes around the DFW area every Saturday just to disturb the peace and quiet of boring citizens.~~ I am no longer active with this group.


+ I enjoy mentoring committed undergraduates, masters students, and occasionally high school students that are interested in computer vision, control, and robotics.

    &nbsp; &nbsp; &nbsp; &nbsp; -   [Ajith](https://www.linkedin.com/in/ajithvenkateswaran) is a Senior Robotics Software Engineer at Samsung Research, America.

    &nbsp; &nbsp; &nbsp; &nbsp; -   [Adwait](https://www.linkedin.com/in/adwaitkulkarni93) is an Engineer at [Drov. Tech, MN](http://drovtech.com).

    &nbsp; &nbsp; &nbsp; &nbsp; -   [Rachel](https://github.com/rsthomp) is currently an undergrad at MIT's CSAIL department.

    &nbsp; &nbsp; &nbsp; &nbsp; -   [Blessing]() is resuming as a CS PhD student at Tufts in the Fall.

<!-- + I still consider Sheffield my adopted home. Biggest village in Yorkshire, where I've made some of my biggest mistakes; where I've met some of the best people I could ever hope to know. City of hills. Home of the Yorkshire pudding. Of thee I sing!
#### Name Etymology

People often ask me how to pronounce my name, and its meaning. Here we go:

+ Lekan is the short form of "Olalekan", which literally means "wealth increased by a factor of one" in [Yoruba](https://en.wikipedia.org/wiki/Yoruba_language), a (Benin-Congo) language of the [Yoruba people](https://en.wikipedia.org/wiki/Yoruba_people) of West Africa.

+ Lekan is pronounced "Lay-con", or "Lay-kañ", where "añ" is akin to the intonation of "ION" in say, "captION".  

+ My last name is rather a little long-winding to roll on the tongue. But let me deconstruct its meaning first. From what I understand, my paternal ancestors
migrated from the Delta area of Nigeria (Warri, specifically) to Yorubaland many generations ago. They fully assimilated into the local Yoruba culture, and became part [Ifá](https://en.wikipedia.org/wiki/If%C3%A1) divinators, and part [Ogun](https://en.wikipedia.org/wiki/Ogun)  worshippers to boot (it is rather amusing that I chose the Engineering profession given that Ogun is generally worshipped by blacksmiths and technologists); "molu" is a compressed form of "mu olu", often abbreviated as "m'olu" or "molu" in contemporary Yoruba; it means "to take victory" or something of that facsimile. If you're catching my drift already, you'll see where this is going: Ogunmolu means "the god of iron prevailed". It's altogether pronounced as "O-goon-moh-loo". There you go.


+   When I am not busy, I am probably on [quora](https://www.quora.com/profile/Lekan-4), the [ros answers forum](http://answers.ros.org) or the [pytorch forum](http://discuss.pytorch.org) answering and posting questions.

+   Among the places I call home include Lagos, Nigeria; Sheffield, United Kingdom; Boston, MA; and of course Tokyo, Japan.
[iros-paper]: https://arxiv.org/abs/1703.03821v3

-->

### References 

[IARC2019]: https://www.iarc.fr/wp-content/uploads/2019/07/IARC-brochure-EN-June_2019.pdf

+ [IARC Brochure: A Unique Agency, June 2019][IARC2019]

[Baskar19]: https://scholar.google.com/scholar_url?url=https://www.ncbi.nlm.nih.gov/pmc/articles/pmc3298009/&hl=en&sa=T&oi=gsb-gga&ct=res&cd=0&d=2296803199726912578&ei=PPy_XYKPCYeQmAGr1puoAg&scisig=AAGBfm2Gk_oOcTq0QajQZ4Vp_bf9IiIEQg 

+ [Baskar, Rajamanickam, Kuo Ann Lee, Richard Yeo, and Kheng-Wei Yeoh. "Cancer and radiation therapy: current advances and future directions." International journal of medical sciences 9, no. 3 (2012): 193.][Baskar19]

[RingborgReport]: https://scholar.google.com/scholar_url?url=https://www.tandfonline.com/doi/pdf/10.1080/02841860310010826&hl=en&sa=T&oi=gsb-gga&ct=res&cd=0&d=9053926701978851676&ei=gPu_XaaRD8rtmQHY7L-ICg&scisig=AAGBfm1hoZbHKgpFcqBS5JeEyBDQc6N5Mg

+ [Ringborg, Ulrik, David Bergqvist, Bengt Brorsson, Eva Cavallin-Ståhl, Jeanette Ceberg, Nina Einhorn, Jan-erik Frödin et al. "The Swedish Council on Technology Assessment in Health Care (SBU) systematic overview of radiotherapy for cancer including a prospective survey of radiotherapy practice in Sweden 2001--summary and conclusions." Acta Oncologica 42, no. 5-6 (2003): 357-365.][RingborgReport]

+ [Keall, Paul J., Gig S. Mageras, James M. Balter, Richard S. Emery, Kenneth M. Forster, Steve B. Jiang, Jeffrey M. Kapatoes et al. "The management of respiratory motion in radiation oncology report of AAPM Task Group 76 a." Medical physics 33, no. 10 (2006): 3874-3900.][Keall-Report]

[Keall-Report]: https://scholar.google.com/scholar_url?url=https://aapm.onlinelibrary.wiley.com/doi/full/10.1118/1.2349696&hl=en&sa=T&oi=gsb-gga&ct=res&cd=0&d=16883262995404466763&ei=kPG_XbPSBM32mQHzlZmoAw&scisig=AAGBfm0_dEagRqfdmdv2HRGW96vZ4Y8Vxw

+ [Liu, Xinmin, Andrew H. Belcher, Zachary Grelewicz, and Rodney D. Wiersma. "Robotic stage for head motion correction in stereotactic radiosurgery." In 2015 American Control Conference (ACC), pp. 5776-5781. IEEE, 2015.][Xinmin4DOF]

[Xinmin4DOF]: https://scholar.google.com/scholar_url?url=https://www.researchgate.net/profile/Xinmin_Liu2/publication/282928634_Robotic_stage_for_head_motion_correction_in_stereotactic_radiosurgery/links/5693b99408ae820ff0727bb5/Robotic-stage-for-head-motion-correction-in-stereotactic-radiosurgery.pdf&hl=en&sa=T&oi=gsb-gga&ct=res&cd=0&d=306093932951640353&ei=5fK_Xej2KIjTmQH4ho_oBw&scisig=AAGBfm01ovpaXREjk99p5H5DtD2mXLprAA

+ [Herrmann, Christian, Lei Ma, and Klaus Schilling. "Model predictive control for tumor motion compensation in robot assisted radiotherapy." IFAC Proceedings Volumes 44, no. 1 (2011): 5968-5973.][HerrmannHexaPODMPC]

[HerrmannHexaPODMPC]: https://scholar.google.com/scholar_url?url=https://www.sciencedirect.com/science/article/pii/S147466701644560X&hl=en&sa=T&oi=gsb&ct=res&cd=0&d=12168071717874672865&ei=FfO_XY2MOIeQmAGr1puoAg&scisig=AAGBfm3ImR8PwLFO61aeFdeeorV6DpLtqw

+ [Patient Motion Management with 6DOF Robotics for Frameless and Maskless Stereotactic Radiosurgery][BelcherThesis]

[BelcherThesis]: https://scholar.google.com/scholar_url?url=http://search.proquest.com/openview/c8ffdee64db65e61136903fcfc899c07/1%3Fpq-origsite%3Dgscholar%26cbl%3D18750%26diss%3Dy%26casa_token%3DRyN4hR-RX8cAAAAA:lfnvPQ8e9anJyXH_PlGRZkWVs3C7QnyXufLaz4sgk-6RbldrubjV5hn-9SNYoLb8lSBgbMkA-A&hl=en&sa=T&oi=gsb-gga&ct=res&cd=0&d=6826969054585395406&ei=SfO_XemdBYeQmAGr1puoAg&scisig=AAGBfm2cw00mWWKT2yCH8irjsl3oasping

+ [Hunt, K. H. "Structural kinematics of in-parallel-actuated robot-arms." (1983): 705-712.][Hunt1983]

[Hunt1983]: https://scholar.google.com/scholar_url?url=https://asmedigitalcollection.asme.org/mechanicaldesign/article-abstract/105/4/705/434199&hl=en&sa=T&oi=gsb&ct=res&cd=0&d=13895107842347352799&ei=Gz3AXa-3LYSSmAHvzKuQBA&scisig=AAGBfm1KATfuWQu50FZC-2s-pgn4qw-VIw