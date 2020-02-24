---
layout: post
permalink: research
mathjax: true
---

<?php include_once("analyticstracking.php") ?>


<a name="research"></a>
### Research Abridgment

<!-- > An overview of my current research. -->
> If you are not too familiar with MRI imaging modalities and photon-based radiation therapy for cancer treatment, please skip to the [motivation section](#motivation) before continuing.

<!--
Means of treating cancers may include one or a combination of drugs, radiation therapy, immunotherapy,  stem cell transplant, targeted therapy, precision therapy, chemotherapy or surgery. Among the different locations where cancers can exist in the human body, cancers of the head and neck (H&N) region tend to be most fatal because of the sensitivity of  H&N organs. Thus, an all-of-the-above solution is not always the most suitable means for treating H&N cancers.
Radiation Therapy (RT), often in conjunction with surgery and chemotherapy, is an invaluable single cancer treatment modality nowadays owing to its cost-effectiveness (accounting for only 5% of the total cost of cancer care <sup>[Ringborg Report][RingborgReport]</sup>), and its advanced mode of radiation production and delivery: shaping the geometry of high-energy  conformal radiation so that it allows radiation escalation to a tumor target while simultaneously sparing organs-at-risk (OARs). Matter-of-factly, half of all cancer patients do undergo RT treatment during the course of their illness with an estimated 40% of all  curative treatment being performed using RT<sup>[Cancer and RT](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3298009/)</sup>. Owing to its advanced radiation delivery method, RT is often the most suitable treatment method for H&N cancers. -->

<!-- Owing to the accurate dose realization requirement in RT delivery, the head and neck region must be made immobile during the administration of dose, as motions of the order of 2mm or 2 degrees deviation from a desired trajectory can cause eczema, brain lesions or other post-treatment complications<sup>Takakura et al.</sup>. The state-of-the-art positioning method for avoiding dose miss is to immobilize the patient with rigid metallic frames or masks<sup>[Fig 1](#fig-rigid)</sup>.

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

To improve the treatment planning process, these drawbacks need to be addressed. This would require the interdisciplinary effort of engineers, roboticists, physicists, and surgeons alike. In my line of work, we try to sidestep these issues. Our philosophy is to do away with radio-opaque/rigid bodies in the parallel robot compensation mechanisms. Fundamentally, we utilize inflatable air bladders (`IABs`), which are hollow spherical soft robot chambers that mitigate these issues. These `IABs` are continuum, compliant and configurable (C<sup>3</sup>) soft elastomeric actuators, with two concentric soft material shells -- so chosen to simplify the mathematical model of the deformation kinematics as well as to provide therapeutic and comfortable patient motion compensation during RT. -->

<!-- Most of my PhD work was focussed on a system identification and statistical approach to their modeling; owing to their medium fidelity in control scenarios, I mitigated unmodeled dynamics and model uncertainties using standard techniques from indirect adaptive control (with projection to handle unbounded errors), optimal control (for setpoint/trajectory regulation) and some neural network adaptive control laws to mitigate unmodeled uncertainties in the system model. In the latter part of my PhD, I started thinking more about deriving closed-form expressions for their kinematics. With continuum mechanics and elastic deformations, we are now able to derive the `soft ik`,  and the dynamical model that governs their deformation. This is derived from `Cauchy's laws of motion` and `Truesdell's determinism for the stress principle`. Writing the direct kinematics of the mechanism becomes a relatively easier problem, allowing for elegant mathematical formulae in predicting a deformation behavior under a given stress and/or internal pressurization.   -->

<!-- The IABs inflate, deflate, extend or contract governed by their material moduli, incompressibility and internal pressurization when given a reference trajectory. By controlling the amount of fluid in the internal cavities of these IABs, we can write a forward kinematic map that compensates head motion deviations in real-time. Furthermore, leveraging `Cauchy's laws of motion` and `Truesdell's determinism for the stress principle`, we can write out the `soft IK` necessary for a required actuation given a desired head pose. Essentially, the hardware design can absorb the reactive force wrench from the patient's displacement/orientation during manipulation, thus guaranteeing patient's comfort without sacrificing the efficiency or effectiveness of radiation delivery. Their radio-transparency to ionizing radiation make situating them close to the tumor source an attractive option for fast motion compensation -- mitigating against the inherent delay between the computation of control signals and actuation in rigid compensation works. An old prototype of the SoRo Mechanism for manipulating the H&N region of a patient in stereotactic radiosurgery is shown in Fig. 3. I invite you to look through my [publications](/pubs) if you are further interested in this research.

{%
    include fig.html
        file='assets/setup.png'
        max-width='95%'
        align='middle'
        caption='<b>Fig 3: </b>C<sup>3</sup> SoRos in a parallel kinematic configuration around the Head and Neck Region. © Lekan Molu, 2019. Thanks to Erik Pearson of UChicago RadOnc for the CAD Model of the Gantry and Turntable.'
%}
<br> -->


#### **Goals**

- [x] Non-magnetic patient motion stabilizing mechanism compatible with magnetic resonance imaging (MRI) machines  
- [x] Radio-transparent patient motion stabilizer for _real-time_ and _precise_ cancer radiation therapy modalities
- [x] Verify that a 6-DOF target motion of a patient is <= 0.5 mm and <= 0.5 deg for greater than 95% of the treatment time.

#### **Aims**
- [ ] Simulation of a 6-DOF motion compensation soft robot for MRI-LINACs

- [ ] Design and construction of an MRI-LINAC soft robotic motion correction mechanism

- [ ] Phantom-based and healthy human volunteer trials

These exploratory lines of research inquiry are relevant to public health and have transformational clinical potential because they may provide:

- Proof-of-concept evidence that soft robots are compatible with standalone MRI imaging modalities;

- Evidence of precise and automatic motion management with non-magnetic and radiation-transparent soft robots in emerging hybrid MRI-linear accelerators;

- An emergence of a better brain and head and neck (H&N) cancer management technology that can be adapted to confined spaces under MRI coils.


#### **Applications**

This technology shall be applicable to the following treatment modalities:

- [x]  Standalone MRIs

- [x]  Emerging MRI-LINAC technologies

- [x]  Head and Neck Cancer Radiation Therapy

- [x] Brain Cancer Radiation Therapy

#### **Advantages**

This proposed technology shall have the following advantage over rigid immobilization systems:

- [x] Negate the deleterious effects of **interfractional** setup variation on patients;

- [x] Correct the complex **intrafractional geometric uncertainties** such as posture changes, and body deformation with minimal invasiveness;

- [x] Eliminate **radiation attenuation** associated with the metallic components of frames and rigid robotic patient motion compensation systems;

- [x] Correct the **flex drifting errors** associated with thermoplastic face masks;

- [x] Do **not interfere with the MRI's magnetic field**.



<a name='motivation' />
### **Background and Motivation**

- Current radiation therapy (RT) treatment modalities use computed tomography scans of body tissues to segment organs before treatment.

- Accurate radiation dose targeting requires subdegree and submillimeter patient motion correction.


- These CT images lack fine contrast that distinguish bony-tissues from non-bony and soft tissues.

- High contrast delineation of cancerous tissues from healthy surrounding tissues can further improve dose escalation to the tumor while simultaneously sparing surrounding healthy tissues; this is especially true for brain or head and neck (H&N) cancers.

- Magnetic resonance imaging (MRI) is an advanced imaging modality for internal body organs. Combined with RT, MRI-based RT is becoming an emerging technology with the potential for improving target and organs-at-risk (OAR) contrast for brain and H&N cancers.

- Recent research directions have demonstrated the compatibility of MRI with linear accelerator (LINAC)-based photon treatment of cancers. <u>_Unfortunately, the quality of MRI imaging is limited by the artifacts caused by patient head motion._</u>  

- **_What if we could automatically correct patient motion during MRI imaging/RT/stereotactic radiosurgery so that we can eliminate the deleterious effects of patient motion uncertainities in MRIs, and photon/proton-based therapies?_**



<a name='existing-technologies' />
### **Existing Technologies and Limitations**

- Currently in clinics, we use a frame or an immobilization mask to render the patient static while they lie supine on a couch
    - &#9746; This is incapable of real-time closed-loop feedback head motion corrections when the treatment beam is on (See Fig. 1).

    - &#9746; The invasiveness, inconvenience and discomfort associated with the frame are a principal cause of poor patient compliance and poor clinical efficacy.

    - &#9746; For some patients, frame placement is not possible due to extreme cranial anatomy or prior surgical bone flaps. In addition, the frame prohibits cases when multiple RT deliveries are needed as patients cannot be subjected to daily attachment and removal of the frame.
    - &#9746; The limitations of frames have spurred clinics using thermoplastic face masks. These result in decreased accuracy arising from mask flex (drift of up to 2-6mm), and changes in the mask from repeated application and shrinking
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
_Fig 1. L-R (a) The Brown-Robert-Wells SRS frame; (b) A thermoplastic face mask in RT (c) A thermoplastic facemask with add-on MRI coils in MRI imaging (d) The Wiersma Stewart-Gough platform (e) The Ostyn platform_

#### **Recent Research Directions**

- &#9746; Explorative robotic positioning research studies have  demonstrated the feasibility of maintaining stable patient cranial motion consistent with treatment plans. For example, the  Wiersma Lab's Stewart-Gough platform, illustrated in Fig 1d, achieves <= 0.5mm and <= 0.5 deg positioning accuracy 90% of the time, while the Ostyn six degrees-of-freedom (DOF) plastic Stewart-Gough platform (Fig. 1e) uses stepper motors to actuate the legs of its parallel plastic platform.

- &#9746; These systems, while aiding better clinical accuracy, utilize rigid metallic components, electric motors and linear actuators which are not suitable for MRI imaging: they interfere with the magnets of the MRI machine and can lead to patient fatality or significant damage to the MRI machine.



{%
    include fig.html
        file='downloads/soro/mri_coils.jpg'
        height=200
        max-width='100%'
        align='middle'
%}
_Fig 2. MRI Treatment Setup. &copy; Kevin Teo/Rodney Wiersma, UPenn Radiation Oncology. L-R (a) Patient immobilization with thermoplastic masks under the MRI tube (b) the MRI coils are typically overlaid on the mask above the patient's face (c) owing to the large magnetic fields of the MRI machine, metallic objects are not admissible. Hence, parallel rigid mechanisms such as the Wiersma or Ostyn robot would not be feasible. These lack soft compliance necessary in such advanced imaging modalities._

#### **Other Technologies**

- The CyberKnife Synchrony, while capable of precise, non-surgical tumor and lesions treatment in SRS and stereotactic body radiotherapy (SBRT), only executes _a-priori_ trajectories (see Fig 3).

- Real-time closed-loop head motion compensation for the CyberKnife system is inhibited by its high load-to-weight ratio which indirectly affects its repeatability
    - Given its stiffness (it weighs 160kg), it has a complicated actuation system so that its passive bending stiffness overwhelms the degree of deformation for rapid patient repositioning.


{%
    include fig_2.html
        file='assets/cyberknife.jpg'
        file2='assets/cyberknife_rotating.jpg'
        height=240
        width=370
%}
<br>
_Fig 3. The Cyberknife system ©Cyberknife._

<!-- **Proposal: A 6-DOF Soft Robot Patient Motion Correction Mechanism for MRI-guided Adaptive Radiation Therapy.** -->



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



