---
layout: post
permalink: soro
mathjax: true
---

<?php include_once("analyticstracking.php") ?>


<a name="research"></a>
# Mechanism Synthesis

> Soft Robot Motion Compensators.

## State of the Art

- AAPM requires 2mm and \\(2^\circ \\) accuracy

- Only available in few select clinics

- Requires a frame or an immobilization mask

- Incapable of real-time closed-loop feedback head motion corrections when the treatment beam is on

- The CyberKnife Synchrony, while capable of precise, non-surgical tumor and lesions treatment in SRS and stereotactic body radiotherapy (SBRT), only executes _a-priori_ trajectories

- Real-time closed-loop head motion compensation for the CyberKnife system is inhibited by its high load-to-weight ratio which indirectly affects its repeatability

- Given its stiffness (it weighs 160kg), it has a complicated actuation system so that its passive bending stiffness overwhelms the degree of deformation for rapid patient repositioning.

{% 
    include fig.html 
        file='assets/cyberknife.jpg' 
        max-width='85%' 
        align='middle'
        caption='<b>Fig 1:</b> The beam repositioning system ©Cyberknife.'
%}
<br>

Frameless and Maskless (F&M) positioning systems are an emerging non-invasive immobilization technology in radiosurgery; they work without utilizing rigid masks and frames -- reducing side effects and optimizing patient comfort without giving away too much in efficiency or effectiveness. The goal is to correct patient motion, ideally with a closed-loop feedback controller implemented  in real-time on a high-precision robotic system -- improving the satisfaction of patients and clinicians, and maximizing dose delivered to a tumor whilst minimizing healthy tissues' exposure to radiation. 

## Proposed Soft Robot Mechanism

### Soft Robot Actuators

{% 
    include fig_2.html 
        file='downloads/soro/soro_top_down.png' 
        file2='downloads/soro/soro_chamber.png' 
        height=350
        width=360
%}

<br>
'<b>Fig 2</b>: <i>(Left)</i> Top view of discrete layers of soft robot. <i>(Right)</i> Internal Hollow Chamber of Soft Robot.'

{% 
    include fig_2.html 
        file='downloads/soro/soro_cross.png' 
        file2='downloads/soro/soro_cover.png' 
        height=350
        width=360
%}

<br>
'<b>Fig 2</b>: <i>(Left)</i> Cross section of the Soft Robot and its Cover. <i>(Right)</i>  Bottom View of Hollow Base for Pipe and Hose Fittings.'

{% 
    include fig_2.html 
        file='downloads/soro/soro_top.png' 
        file2='downloads/soro/soro_butt.png' 
        height=340
        width=360
%}

<br>
'<b>Fig 3</b>: <i>(Left)</i> Smooth soft robot in a Gaussian curvature at full inflation. <i>(Right)</i> Base of the soft robot with hole orifice for pneumatic tube fittings.'


<br>

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
