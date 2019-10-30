---
layout: page
permalink: about
---

<?php include_once("analyticstracking.php") ?>

### Intro

<!-- #### Tell me what you got -->

Welcome to my web presence! I am an interdisciplinary researcher who combines the scientific elegance of machine learning and control theory with the practical impact of modern robotics to create technological solutions that improve healthcare delivery for cancer  patients. I am currently a postdoctoral researcher at the University of Pennsylvania's School of Medicine and I was previously a visiting postdoctoral scholar at the University of Chicago's School of Medicine. In my postdoctoral research duties, I work on problems spanning conceptualization of new hardware  and software tools for improving the **treatment planning** process in _cancer radiation therapy_. I love working with cerebral/talented people. I am largely an independent researcher who enjoys self-direction at my own projects/goals. Yet, I value collaboration across domains and with people of diverse expertise. I read widely and study avidly: my interests span the sciences, technical disciplines (hello, chemistry, physics and engineering) to history and public affairs (really?). A big believer in open science and reproducible research, I try to make my publications and codes public to the extent that I can: see my [publications page](/pubs) and  [github repos](https://github.com/lakehanne). I am particularly mindful of inclusion in hi-tech, STEM, policy-making, and governance. **I am not a robot**. My PGP key on most public key servers is 03E3 58FB 1D98 869E 8ABE 1EF0 E6A1 2F95 B720 BBB5.  

**TL;DR**: I study, build, and use robots, oftentimes tinkering with AI-based control systems. 

<!-- My work has made meaningful impact in disciplines within and outside medicine and engineering, with citations from government and highered learning research institutions across the globe. 
Example institutions that have used my work include the National Aeronautics and Space Agency's Jet Propulsion Laboratory (NASA JPL), the 6th R&D institute of South Korea's Agency for Defense Development, Uber AI Labs, and the Chinese Academy of Sciences among others. -->


### Background

I was ~~buttered and bread~~ born and bred in Southern Nigeria. I spent most of my adolescent years in the only logical place in the whole wide world where one can maximize one's 'life-fun-index': [Lagos](https://en.wikipedia.org/wiki/Lagos). I speak and write fluently in [Yoruba](https://en.wikipedia.org/wiki/Yoruba_language) and English -- languages I have used throughout my entire life. Having lived in Japan, I acquired a basic understanding of ~~Japaneasy~~ Japanese. I am working on a working-level proficiency (still another mile!). I love to meet people from other places and backgrounds -- it strengthens my understanding of the human culture. My accent has often been compared to the French one, though I have no idea what that is. I enjoy Afro-Jazz, Japanese Jazz, and alternative rock music genres. I do have an electric guitar, which I lazily play when I'm depressed. Someday, I do hope to be a street entertainer (_wouldn't that be fun?_).
<!-- There are many places I call home including but not limited to the following: Lagos, Tokyo, [City of Sheafs](https://en.wikipedia.org/wiki/Sheffield)(will always be my spiritual home), Dallas, TX and [Shikaakwa](http://www.todayifoundout.com/index.php/2013/07/how-chicago-got-its-name/).  --> 
At various times in my little time on this planet, I have been a [_Shikaakwaan_](http://www.todayifoundout.com/index.php/2013/07/how-chicago-got-its-name/), a _[Lagosian](https://en.wiktionary.org/wiki/Lagosian)_, a _[Sheffielder](https://www.urbandictionary.com/define.php?term=Sheffielder) (home of my forever friends)_, a _Bostonian_, a _Londoner_, an _[Edokko](https://web-japan.org/tokyo/know/edokko/edo.html)_,  and a  _[Dallasite](https://www.dmagazine.com/frontburner/2012/01/are-we-dallasites-or-dallasonians-fort-worthers-or-fort-worthians-etymology-tells-us-who-we-are/) (Eh!)_. 

#### Research Abridgment

Across our planet, in rich and poor nations alike, cancer remains an existential burden on healthful living.  In 2019 alone, an estimated 1,762,450 new cancer cases will be diagnosed in the United States, wherein 606,880 cases will lead to fatality<sup>[ACS 2019](https://www.cancer.org/research/cancer-facts-statistics/all-cancer-facts-figures/cancer-facts-figures-2019.html)</sup>. This is projected to cost approximately $147.3 billion or 4.2% of overall health care spending (per 2017 budget). Cancer mortality is having pronounced effects on low- and middle-income countries as well with the International Agency for Research on Cancers estimating that the highest cancer incidence will fall on low- and middle-income countries over the coming decades <sup>[IARC Report 2019](https://www.iarc.fr/wp-content/uploads/2019/07/IARC-brochure-EN-June_2019.pdf)</sup>. 

Means of treating cancers may include one or a combination of drugs, radiation therapy, immunotherapy,  stem cell transplant, targeted therapy, precision therapy, chemotherapy or surgery. Among the different locations where cancers can exist in the human body, cancers of the head and neck (H&N) region tend to be most fatal because of the sensitivity of  H&N organs. Thus, an all-of-the-above solution is not always the most suitable means for treating H&N cancers. 
Radiation Therapy (RT), often in conjunction with surgery and chemotherapy, is an invaluable single cancer treatment modality nowadays owing to its cost-effectiveness (accounting for only 5% of the total cost of cancer care <sup>[Ringborg Report](https://www.tandfonline.com/doi/abs/10.1080/02841860310010826)</sup>, and its advanced mode of radiation production and delivery: shaping the geometry of high-energy  conformal radiation so that it allows radiation escalation to a tumor target while simultaneously sparing organs-at-risk (OARs). Matter-of-factly, half of all cancer patients do undergo RT treatment during the course of their illness with an estimated 40% of all  curative treatment being performed using RT<sup>[Baskar12](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3298009/)</sup>. Owing to its advanced radiation delivery method, RT is often the most suitable treatment method for H&N cancers. 

Owing to the accurate dose realization requirement in RT, the head and neck region must be made immobile during the administration of dose, as motions of the order of 2mm or 2 degrees deviation from a desired trajectory have been known to cause eczema, brain lesions and other post-treatment complications. The state-of-the-art positioning method for avoiding dose miss is to immobilize the patient with rigid metallic frames or masks<sup>[Fig 1](#fig-rigid)</sup>. 

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

However, these frames attenuate dose and and the stress of wearing and removing rigid masks intermittently over many months of treatment fractionation can be painful for the patient. 

{% 
    include fig.html 
        file='assets/cyberknife.jpg' 
        max-width='85%' 
        align='middle'
        caption='<b>Fig 2:</b> The beam repositioning system ©Cyberknife.'
%}

<br>
Frameless and maskless (F&M) RT is an emerging non-invasive radiosurgery treatment modality that aims to stem this issue. The goal of F&M RT is to control and correct a patient's motion, ideally with a closed-loop feedback controller implemented on a high-precision manipulation system (usually robots) in **real-time** during RT. Since patient deviation from target trajectory is frequent during treatment, parallel robots (matter-of-factly, 6-legged Stewart-Gough platforms) have emerged as a means of immobilizing patients in research scenarios. However, such parallel robots:

+ share their complete workspace with body tissues, a safety concern since rigid robot components lack compliance and their end effectors add "hard shocks" to the patients' body during manipulation;

+ are incapable of providing sophisticated 3D manipulation with their constant-curvature components; and

+ the inadvertent respiratorial and internal organ motions often induce deviation from a target beyond the recommentations of AAPM Task Group 17, namely 2mm and 2 degrees tolerance.

In my line of work, we try to sidestep these issues. Our philosophy is to do away with radio-opaque/rigid bodies in the compensation mechanism. Fundamentally, we utilize inflatable air bladders (`IABs`) to mitigate these highlighted issues. These `IABs` are continuum, compliant and configurable (C<sup>3</sup>) soft elastomeric actuators that provide therapeutic and comfortable patient motion compensation during RT. Most of my PhD work was focussed on a system identification and statistical approach to their modeling; I then leveraged adaptive and optimal control to mitigate unmodeled uncertainties in the system model. Toward the end of my PhD, I started thinking more about deriving closed-form expressions for their kinematics. Leveraging techniques from continuum mechanics and elastic deformations, we are now able to derive the `soft ik`,  and the dynamical model that governstheir actuations based on Cauchy's continuum laws and Truesdell's stress from determinism principle. Writing the direct kinematics of the mechanism becomes relatively easier a problem now, allowing for elegant mathematical formulae in predicting a deformation behavior under a given stress and internal pressurization. A prototype of the SoRo Mechanism for manipulating the H&N region of a patient in stereotactic radiosurgery is shown in Fig. 3.

{% 
    include fig.html 
        file='assets/setup.png' 
        max-width='95%' 
        align='middle'
        caption='<b>Fig 3: </b>C<sup>3</sup> SoRos in a parallel kinematic configuration around the Head and Neck Region. ©Lekan Molu, 2019.'
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

#### Miscellaneous

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
migrated from the Delta area of Nigeria (Warri, specifically) to Yorubaland many generations ago. They fully assimilated into the local Yoruba culture, and became part [Ifá](https://en.wikipedia.org/wiki/If%C3%A1) divinators, and part [Ogun](https://en.wikipedia.org/wiki/Ogun)  worshippers to boot (it is rather amusing that I chose the Engineering profession given that Ogun is generally worshipped by blacksmiths and technologists); "molu" is a compressed form of "mu olu", often abbreviated as "m'olu" or "molu" in contemporary Yoruba; it means "to take victory" or something of that facsimile. If you're catching my drift already, you'll see where this is going: Ogunmolu means "the god of iron prevailed". It's altogether pronounced as "O-goon-moe-loo". There you go.


+   When I am not busy, I am probably on [quora](https://www.quora.com/profile/Lekan-4), the [ros answers forum](http://answers.ros.org) or the [pytorch forum](http://discuss.pytorch.org) answering and posting questions.

+   Among the places I call home include Lagos, Nigeria; Sheffield, United Kingdom; Boston, MA; and of course Tokyo, Japan.
[iros-paper]: https://arxiv.org/abs/1703.03821v3

-->
