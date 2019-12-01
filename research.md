---
layout: post
permalink: research
mathjax: true
---

<?php include_once("analyticstracking.php") ?>


<a name="research"></a>
### Research Abridgment

> An overview of my current research.


Across our planet, in rich and poor nations alike, cancer remains an existential burden on healthful living.  In 2019 alone, an estimated 1,762,450 new cancer cases will be diagnosed in the United States, whereupon 606,880 cases will lead to fatality<sup>[ACS 2019](https://www.cancer.org/research/cancer-facts-statistics/all-cancer-facts-figures/cancer-facts-figures-2019.html)</sup>. This is projected to cost approximately $147.3 billion or 4.2% of overall health care spending. Cancer mortality is having pronounced effects on low- and middle-income countries as well, with the International Agency for Research on Cancers estimating that the highest cancer incidence will fall on low- and middle-income countries over the coming decades <sup>[IARC Report 2019][IARC2019]</sup>. 

Means of treating cancers may include one or a combination of drugs, radiation therapy, immunotherapy,  stem cell transplant, targeted therapy, precision therapy, chemotherapy or surgery. Among the different locations where cancers can exist in the human body, cancers of the head and neck (H&N) region tend to be most fatal because of the sensitivity of  H&N organs. Thus, an all-of-the-above solution is not always the most suitable means for treating H&N cancers. 
Radiation Therapy (RT), often in conjunction with surgery and chemotherapy, is an invaluable single cancer treatment modality nowadays owing to its cost-effectiveness (accounting for only 5% of the total cost of cancer care <sup>[Ringborg Report][RingborgReport]</sup>), and its advanced mode of radiation production and delivery: shaping the geometry of high-energy  conformal radiation so that it allows radiation escalation to a tumor target while simultaneously sparing organs-at-risk (OARs). Matter-of-factly, half of all cancer patients do undergo RT treatment during the course of their illness with an estimated 40% of all  curative treatment being performed using RT<sup>[Cancer and RT](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3298009/)</sup>. <!-- Owing to its advanced radiation delivery method, RT is often the most suitable treatment method for H&N cancers. --> 

Owing to the accurate dose realization requirement in RT delivery, the head and neck region must be made immobile during the administration of dose, as motions of the order of 2mm or 2 degrees deviation from a desired trajectory can cause eczema, brain lesions or other post-treatment complications<sup>Takakura et al.</sup>. The state-of-the-art positioning method for avoiding dose miss is to immobilize the patient with rigid metallic frames or masks<sup>[Fig 1](#fig-rigid)</sup>. 

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
        caption='<b>Fig 1</b>: <i>(Left)</i> H&N immobilized with Thermoplastic Mould. <i>(Right)</i> H&N immobilized with Rigid Frame. A screw is typically drilled into the skull to render the patient immobile. The mask is further secured to the table with mechanical screws. Masks and frames generally attenuate high-energy photons meant to deliver curative dose to tumors.'
%}

<br>

Mask-based immobilization uses thermoplastics  (see left inset of [Fig 1](#fig-rigid)). Before the patient wears the mask, the solid thermoplast is allowed to stretch by heating it in water to a preset temperature. When the molecular bonds in the thermoplast weaken, a patient may wear it and use it to secure their head to the couch on which they supinely lie. However, these masks reduce immobilization accuracy owing to flex (producing a drift of up to \\(6mm\\)) as well as shrinkage. For deep tumors nearby sensitive organs such as the brain stem, or during single isocenter multiple-target stereotactic radiosurgery (SRS) treatment modalities, masks are not suitable given the high sensitivity of head motion along the rotatory axis.
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

The CyberKnife system (see Fig 2), in spite of its advanced mode of beam repositioning and radiation delivery, requires a frame or an immobilization mask, and is incapable of real-time closed-loop feedback head motion corrections when the treatment beam is on. The CyberKnife Synchrony, while capable of precise, non-surgical tumor and lesions treatment in SRS and stereotactic body radiotherapy (SBRT), only executes _a-priori_ trajectories; furthermore, it is only FDA-approved for lung tumors' treatment; correction requirements in systems such as this require far less accuracy, typically \\(< 5mm\\)<sup>[Keall-Report]</sup>than brain targets. Additionally, real-time closed-loop head motion compensation for the CyberKnife system is inhibited by its high load-to-weight ratio which indirectly affects its repeatability: as an open kinematic chain, it exhibits poor accuracy since the weight of the segments that follow each link in the robot and the load of the mechanical structure contributes to the large flexure of torques; its links inherently magnify errors from shoulder out to the end-effector, consequently hampering its use for sophisticated control strategies that may minimize or eliminate load-dependent errors; additionally, its setup distance from the patient is a recipe for delayed execution of control laws in ensuring that radiation beam reaches its target without significantly affecting dose delivery. Given its stiffness (it weighs 160kg), it has a complicated actuation system so that its passive bending stiffness overwhelms the degree of deformation for rapid patient repositioning. 

Frameless and Maskless (F&M) positioning systems are an emerging non-invasive immobilization technology in radiosurgery; they work without utilizing rigid masks and frames -- reducing side effects and optimizing patient comfort without giving away too much in efficiency or effectiveness. The goal is to correct patient motion, ideally with a closed-loop feedback controller implemented  in real-time on a high-precision robotic system -- improving the satisfaction of patients and clinicians, and maximizing dose delivered to a tumor whilst minimizing healthy tissues' exposure to radiation. 

Parallel robot configurations have found good use along this research thrust. This is despite their higher number of actuated joints. In a way, this is an advantage because they distribute the weight of the load around the links of the robot, improving manipulation accuracy as a result. They also exhibit a desirable lightness property (albeit at the expense of a reduced workspace) that minimize the flexure torques that are otherwise common with open kinematic chains. Thus, parallel kinematic configurations, in theory, enable greater precision with minimal control complications owing to the non-cummulativeness of actuator errors<sup>[Hunt1983]</sup>.

Recent frameless and maskless research research directions include the steel-cast assembled 4-DOF robot of [Wiersma Group][Xinmin4DOF], which corrected all translation axis motions and a pitch rotatory head motion; the HexaPOD parallel manipulator of [Hermann Group][HerrmannHexaPODMPC] utilized a system identification and model predictive control approach to correct a tumor position on an Hexapod; and the in-house fabricated 6-DOF Stewart-Gough platform of [Wiersma Group][BelcherThesis]. However, these systems share common drawbacks e.g.

+ given their constant-curvature end-effectors/platforms, they are incapable of providing sophisticated manipulation e.g. for the inadvertent respiratory motions that often induce deviation from a target in RT, or fractal axis motions on the couch;
    
+ being made out of rigid bodies (often steel and aluminum which have considerable , attenuation properties to the ionizing radiation); the degree of dose attenuation has to be factored into treatment plans when these systems get commissioned; and
    
+ exhibiting planar platforms/tool frames, there is an inherent delay in head motion compensation along the patient's frontal axis that may inhibit clinical accuracy.
 
To improve the treatment planning process, these drawbacks need to be addressed. This would require the interdisciplinary effort of engineers, roboticists, physicists, and surgeons alike. In my line of work, we try to sidestep these issues. Our philosophy is to do away with radio-opaque/rigid bodies in the parallel robot compensation mechanisms. Fundamentally, we utilize inflatable air bladders (`IABs`), which are hollow spherical soft robot chambers that mitigate these issues. These `IABs` are continuum, compliant and configurable (C<sup>3</sup>) soft elastomeric actuators, with two concentric soft material shells -- so chosen to simplify the mathematical model of the deformation kinematics as well as to provide therapeutic and comfortable patient motion compensation during RT.

<!-- Most of my PhD work was focussed on a system identification and statistical approach to their modeling; owing to their medium fidelity in control scenarios, I mitigated unmodeled dynamics and model uncertainties using standard techniques from indirect adaptive control (with projection to handle unbounded errors), optimal control (for setpoint/trajectory regulation) and some neural network adaptive control laws to mitigate unmodeled uncertainties in the system model. In the latter part of my PhD, I started thinking more about deriving closed-form expressions for their kinematics. With continuum mechanics and elastic deformations, we are now able to derive the `soft ik`,  and the dynamical model that governs their deformation. This is derived from `Cauchy's laws of motion` and `Truesdell's determinism for the stress principle`. Writing the direct kinematics of the mechanism becomes a relatively easier problem, allowing for elegant mathematical formulae in predicting a deformation behavior under a given stress and/or internal pressurization.   -->

The IABs inflate, deflate, extend or contract governed by their material moduli, incompressibility and internal pressurization when given a reference trajectory. By controlling the amount of fluid in the internal cavities of these IABs, we can write a forward kinematic map that compensates head motion deviations in real-time. Furthermore, leveraging `Cauchy's laws of motion` and `Truesdell's determinism for the stress principle`, we can write out the `soft IK` necessary for a required actuation given a desired head pose. Essentially, the hardware design can absorb the reactive force wrench from the patient's displacement/orientation during manipulation, thus guaranteeing patient's comfort without sacrificing the efficiency or effectiveness of radiation delivery. Their radio-transparency to ionizing radiation make situating them close to the tumor source an attractive option for fast motion compensation -- mitigating against the inherent delay between the computation of control signals and actuation in rigid compensation works. An old prototype of the SoRo Mechanism for manipulating the H&N region of a patient in stereotactic radiosurgery is shown in Fig. 3. I invite you to look through my [publications](/pubs) if you are further interested in this research.

{% 
    include fig.html 
        file='assets/setup.png' 
        max-width='95%' 
        align='middle'
        caption='<b>Fig 3: </b>C<sup>3</sup> SoRos in a parallel kinematic configuration around the Head and Neck Region. © Lekan Molu, 2019. Thanks to Erik Pearson of UChicago RadOnc for the CAD Model of the Gantry and Turntable.'
%}
<br>

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
