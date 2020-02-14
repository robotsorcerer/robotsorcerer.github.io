---
layout: post
permalink: soro
mathjax: true
---

<?php include_once("analyticstracking.php") ?>


<a name="research"></a>
# Mechanism Synthesis

<!-- > Soft Robot Motion Compensators.

## State of the Art

- AAPM requires 2mm and \\(2^\circ \\) accuracy

- Only available in few select clinics

- Requires a frame or an immobilization mask

- Incapable of real-time closed-loop feedback head motion corrections when the treatment beam is on

- The CyberKnife Synchrony, while capable of precise, non-surgical tumor and lesions treatment in SRS and stereotactic body radiotherapy (SBRT), only executes _a-priori_ trajectories

- Real-time closed-loop head motion compensation for the CyberKnife system is inhibited by its high load-to-weight ratio which indirectly affects its repeatability

- Given its stiffness (it weighs 160kg), it has a complicated actuation system so that its passive bending stiffness overwhelms the degree of deformation for rapid patient repositioning. 


        caption='<b>Fig 1:</b> The beam repositioning system ©Cyberknife.'-->

{% 
    include fig_2.html 
        file='assets/cyberknife.jpg' 
        file2='assets/setup.png'
        height=250
        width=360
%}
<br>

Fig. 1. Frameless and Maskless (F&M) positioning systems are an emerging non-invasive immobilization technology in radiosurgery; they work without utilizing rigid masks and frames -- reducing side effects and optimizing patient comfort without giving away too much in efficiency or effectiveness. The goal is to correct patient motion, ideally with a closed-loop feedback controller implemented  in real-time on a high-precision robotic system -- improving the satisfaction of patients and clinicians, and maximizing dose delivered to a tumor whilst minimizing healthy tissues' exposure to radiation. 

<!-- ## Proposed Soft Robot Mechanism


{% 
    include fig.html 
        file='assets/setup.png' 
        max-width='100%' 
        align='middle'
        caption='<b>Fig 5: </b>C<sup>3</sup> SoRos in a parallel kinematic configuration around the Head and Neck Region. © Lekan Molu, 2019. Thanks to Erik Pearson of UChicago RadOnc for the CAD Model of the Gantry and Turntable.'
%}
<br> -->

### Soft Robot Actuators: Model

{% 
    include fig_5.html 
        file='downloads/soro/soro_top_down.png' 
        file2='downloads/soro/soro_chamber.png' 
        file3='downloads/soro/soro_cross.png' 
        file4='downloads/soro/soro_cover.png' 
        file5='downloads/soro/soro_top.png' 
        height=145
        width=145
%}

<br> <center>Fig. 2. Actuator Model</center>

<br><br><br>


### Circumferential bulge

{% 
    include fig_5.html 
        file='downloads/soro/circ_bulge1.jpg' 
        file2='downloads/soro/circ_bulge2.jpg' 
        file3='downloads/soro/circ_bulge3.jpg' 
        file4='downloads/soro/circ_bulge4.jpg' 
        file5='downloads/soro/circ_bulge5.jpg' 
        height=145
        width=145
%}

<br>
<br>
<center><b>Fig 3</b>. Bulge upon pneumatic actuation.</center>
<br>
<br>

#### CCOARSE Deformation

{% 
    include fig_5.html 
        file='downloads/soro/ds_3mm_l1.jpg' 
        file2='downloads/soro/ds_3mm_l2.jpg' 
        file3='downloads/soro/ds_3mm_l3.jpg' 
        file4='downloads/soro/ds_3mm_l4.jpg' 
        file5='downloads/soro/ds_3mm_l4_touch.jpg'
        height=145
        width=145
%}

<br>
<center><b>Fig 4.</b> Circumferentially-Constrained and Radially Symmetric Fiber-Elastomer (CCOARSE). </center>


<br>


### Videos 

<iframe src="/assets/soro/zero_to_hero.mp4" width="250" height="250" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:3px solid #666; margin-bottom:5px; max-width: 48%;" allowfullscreen> </iframe>

<iframe src="/assets/soro/circ_bulge_real.mp4" width="250" height="250" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:3px solid #666; margin-bottom:5px; max-width: 48%;" allowfullscreen> </iframe>
<br>
