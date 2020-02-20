---
layout: post
permalink: soro
mathjax: true
---

<?php include_once("analyticstracking.php") ?>


<a name="research"></a>
## Patient Motion Control in MRI-LINACs with Soft Robots

**Goal** 

- [x] Non-magnetic and radio-transparent patient motion control for real-time and _precise_ cancer therapy

**Applications**

- [x]  Standalone MRIs

- [x]  Emerging MRI-LINAC technogies

- [x]  Head and Neck Cancer Radiation Therapy

- [x] Brain Cancer Radiation Therapy

**Advantages**

- [x] Negate the deleterious effects of **interfractional** setup variation on patients; 

- [x] Correct the complex **intrafractional geometric uncertainties** such as posture changes, and body deformation with minimal invasiveness; 

- [x] Eliminate **radiation attenuation** associated with the metallic components of frames and rigid robotic patient motion compensation systems; 

- [x] Correct the **flex drifting errors** associated with thermoplastic face masks; 

- [x] Do **not interfere with the MRI's magnetic field**.

**Proposed Setup**

{% 
    include fig_4.html 
        file='downloads/soro/setup_nogantry_sv.png' 
        file2='downloads/soro/setup_nogantry_fv.png' 
        file4='downloads/soro/setup_flexi.png' 
        file3='downloads/soro/patient_no_gantry_closeup.jpg' 
        height=200
        width=180
        align='middle'
%}

<br>

### **Motivation**

- Current radiation therapy (RT) treatment modalities use computed tomography scans of body tissues to segment organs before treatment. 

- Accurate radiation dose targeting requires subdegree and submillimeter patient motion correction.


- These CT images lack fine contrast that distinguish bony-tissues from non-bony and soft tissues. High contrast delineation of cancerous tissues from healthy surrounding tissues can further improve dose escalation to the tumor while simultaneously sparing surrounding healthy tissues; this is especially true for brain or head and neck (H\&N) cancers. 
- Magnetic resonance imaging (MRI) is an advanced imaging modality of internal body organs. Combined with RT, MRI-based RT is becoming an emerging technology with the potential for improving target and organs-at-risk (OAR) contrast for brain and H\&N cancers. 
- Recent research directions have demonstrated the compatibility of MRI with linear accelerator (LINAC)-based photon treatment of cancers.  Unfortunately, the quality of MRI imaging is limited by the artifacts caused by patient head motion.  
- **_What if we could automatically correct patient motion during MRI imaging/RT/stereotactic radiosurgery so that we can eliminate the deleterious effects of patient motion uncertainities in MRIs, and photon/proton-based therapies? How do we negate patient motion?_**


### **Existing Technologies**

- Currently in clinics, we use a frame or an immobilization mask to render the patient static while they lie supine on a couch
    - &#9746; This is incapable of real-time closed-loop feedback head motion corrections when the treatment beam is on (See Fig. 1).
    - &#9746; The invasiveness, inconvenience and discomfort associated with the frame are a principal cause of poor patient compliance and poor clinical efficacy.
    - &#9746; For some patients, frame placement is not possible due to extreme cranial anatomy or prior surgical bone flaps. In addition, the frame prohibits cases when multiple RT deliveries are needed as patients cannot be subjected to daily attachment and removal of the frame. 
    - &#9746; The limitations of frames has spurred clinics using thermoplastic face masks. These result in decreased accuracy arising from mask flex (drift of up to 2-6mm), and changes in the mask from repeated application and shrinking
    - &#9746; Such inaccuracies are not suitable for deep tumors located near critical structures such as the brain stem or for newer treatment modalities such as single isocenter multiple-target stereotactic radiosurgery (SRS), which are highly sensitive to rotational head motions. 

{% 
    include fig_5.html 
        file='downloads/soro/SRSFrame.png' 
        file2='downloads/soro/frame1.jpg' 
        file3='downloads/soro/mri_coils_1.jpg' 
        file4='downloads/soro/WiersmaRobotPatient.jpg' 
        file5='downloads/soro/ostyn.jpg' 
        height=115
        width=146
%}

- Recent research directions
    - &#9746; Explorative robotic positioning research studies have  demonstrated the feasibility of maintaining stable patient cranial motion consistent with treatment plans. For example, the  Wiersma Lab's Stewart-Gough platform, illustrated in Fig 1d, achieves <= 0.5mm and <= 0.5 deg positioning accuracy 90% of the time, while the Ostyn six degrees-of-freedom (DOF) plastic Stewart-Gough platform (Fig. 1e) uses stepper motors to actuate the legs of its parallel plastic platform. 
    - &#9746; These systems, while aiding better clinical accuracy, utilize rigid metallic components, electric motors and linear actuators which are not suitable for MRI imaging: they interfere with the magnets of the MRI machine and can lead to patient fatality or significant damage to the MRI machine.


<br>
_Fig 1. L-R (a) The Brown-Robert-Wells SRS frame; (b) the thermoplastic face mask in classical RT (c) a thermoplastic facemask with add-on MRI coils in MRI imaging (d) the Wiersma Stewart-Gough model (e) the Ostyn robot_


{% 
    include fig.html 
        file='downloads/soro/mri_coils.jpg' 
        height=420
        max-width='100%'
        align='middle'
%}
<br>
_Fig 2. MRI Treatment Setup. &copy; Kevin Teo/Rodney Wiersma, UPenn Radiation Oncology. L-R (a) Patient immobilization with thermoplastic masks under the MRI tube (b) the MRI coils are typically overlaid on the mask above the patient's face (c) owing to the large magnetic fields of the MRI machine, metallic objects are not admissible. Hence, parallel rigid mechanisms such as the Wiersma or Ostyn robot would not be feasible. These lack soft compliance necessary in such advanced imaging modalities._

- The CyberKnife Synchrony, while capable of precise, non-surgical tumor and lesions treatment in SRS and stereotactic body radiotherapy (SBRT), only executes _a-priori_ trajectories (see Fig 3).

- Real-time closed-loop head motion compensation for the CyberKnife system is inhibited by its high load-to-weight ratio which indirectly affects its repeatability
    - Given its stiffness (it weighs 160kg), it has a complicated actuation system so that its passive bending stiffness overwhelms the degree of deformation for rapid patient repositioning. 


{% 
    include fig_2.html 
        file='assets/cyberknife.jpg' 
        file2='assets/cyberknife_rotating.jpg' 
        height=240
        width=340
        caption='<b>Fig 3:</b> The Cyberknife system ©Cyberknife.'
%}

<br>

<!-- Fig. 1. Frameless and Maskless (F&M) positioning systems are an emerging non-invasive immobilization technology in radiosurgery; they work without utilizing rigid masks and frames -- reducing side effects and optimizing patient comfort without giving away too much in efficiency or effectiveness. The goal is to correct patient motion, ideally with a closed-loop feedback controller implemented  in real-time on a high-precision robotic system -- improving the satisfaction of patients and clinicians, and maximizing dose delivered to a tumor whilst minimizing healthy tissues' exposure to radiation. 
 -->

**Proposal: A 6-DOF Soft Robot Patient Motion Correction Mechanism for MRI-guided Adaptive Radiation Therapy.**



#### Actuators Geometrical Model

{% 
    include fig_5.html 
        file='downloads/soro/discrete_soro.png'
        file2='downloads/soro/soro_chamber.png' 
        file3='downloads/soro/soro_cross.png' 
        file4='downloads/soro/soro_cover.png' 
        file5='downloads/soro/soro_top.png' 
        height=130
        width=145
%}

<br> <center>Fig. 2. Actuator Model</center>

<br><br><br>


#### Circumferential Deformation 

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


### Deformation Videos 

**Equiaxial Deformation**

<iframe src="/downloads/soro/circ_bulge_real.mp4" width="240" height="240" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:3px solid #666; margin-bottom:5px; max-width: 48%;" allowfullscreen> </iframe>

<iframe src="/downloads/soro/circ_bulge_real2.mp4" width="240" height="240" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:3px solid #666; margin-bottom:5px; max-width: 48%;" allowfullscreen> </iframe>

<iframe src="/downloads/soro/circ_bulge_real3.mp4" width="240" height="240" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:3px solid #666; margin-bottom:5px; max-width: 48%;" allowfullscreen> </iframe>

<br>

**CCOARSE Deformation**

<iframe src="/downloads/soro/zero_to_hero.mp4" width="250" height="250" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:3px solid #666; margin-bottom:5px; max-width: 48%;" allowfullscreen> </iframe>

<iframe src="/downloads/soro/puncture_resist.mp4" width="250" height="250" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:3px solid #666; margin-bottom:5px; max-width: 48%;" allowfullscreen> </iframe> 
<br>
