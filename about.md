---
layout: page
permalink: about
---

<?php include_once("analyticstracking.php") ?>

<img src="/downloads/Pat.jpg" alt="Me" align="right" style="width:100px;height:100px;">
Welcome to my blog, where theory meets practice, and where scientific elegance meets cool engineering impact. Fields that consume the bulk of my attention currently include control theory, deep learning, robotics and certainly reinforcement learning.

My work explores better model representation in dynamical systems using state-of-the-art neural network function approximators to determine accurate system models, for example in adaptive control or model predictive control of complex nonlinear systems. My background is in Physics and Control theory and I spend my PhD research exploring better ways of automating motion alignment correction systems in clinical cancer radiotherapy of malignant cancers of the head and neck region. The novelty of my work includes (i) the design and use of soft robots with morphological computation properties to dynamically adjust patient motion along desired degrees of freedom during cancer radiotherapy treatment; (ii) adaptive function approximators to model these coupled nonlinearities.  As these soft actuators are nonlinear, a lot of effort goes into formulating the model properties of the hardware in order to obtain an effective controller that can deliver the required sub-millimeter and sub-degree accuracy. Owing to the recent advances in sequential deep learning frameworks in terms of their accuracy and precision in generating powerful models for tasks including speech recognition and machine language translation, I leverage on these technologies to create dynamic models of the patient testbed and to design appropriate adaptive controllers to scale.

<!--
#### Research Background

In stereotactic radiosurgery of the head and neck region, patients are typically positioned in a supine manner on a 6-DOF robotic couch for motion alignment correction with respect to an incident radiation. As such, the precision of delivery of the radiation dose to target tumor is extremely important. Target miss in dosimetry angle or positioning errors arising from patient positioning errors have been known to cause eczema, brain complications and the exposure of organs at risks.
{% include fig.html
max-width="200px" file="/imgs/homepage/igrt_setup.jpg" alt="igrt setup"
float="right"  border="1px dotted black"  margin="0px 0px 15px 20px" align="right"
 %}
To prevent the patient from drifting from pre-calibrated pose on the 6-DOF robotic treatment couch, clinicians fixate metallic rings/frames or elastic plastic masks on the patient's head and neck region so that involuntary motion by the patient is greatly minimized. But the use of such rings or masks have undesirable effects such as attenuating the radiation beam (thus minimizing incident dose and treatment efficacy) or making the patient uncomfortable.
The majority of such masks employed do not compensate for real-time patient deviation from planned targets. To compensate for such drifts, I have formulated a [neuro-adaptive controller][iros-paper] for a network of compliant soft-robot systems to automatically move the patient's head and neck to desired pose based on a learning based finite-state machine.

{% include fig.html
max-width="100px" file="/imgs/homepage/moveit.jpg" alt="igrt setup"
float="right"  border="1px dotted black"  margin="0px 0px 15px 20px" align="right"
 %}

The idea is that by actuating elastomeric polymer enclosures that inflate or deflate based on the amount of air that is sent into them or by the amount of pressure that is exerted on them by a human-body part (such as head or neck), we can achieve a desired level of pose in frameless or maskless radiotherapy without sacrificing patient comfort or treatment efficacy as existing technologies allow. This is a revolutionizing approach to the current way frameless radiotherapy is practiced.

My solution is the only one so far that achieves desired actuation in closed-loop control and in real time without sacrificing time, treatment efficiency or patient comfort -- all based on a data-driven modeling approach and a mathematically proven stable neural-network based controller to compensate for the dynamics of the system. -->

### Things I do for fun

+ I am a co-owner of the Linux, OpenStack and Unix Networking video tutorials on [this](https://www.youtube.com/channel/UC-0PMn0rKV_ZOHF-qX6N3fQ/videos) youtube page.

+ I am a member of North Texas Drone Users Group.  

+ I enjoy mentoring committed undergraduates, masters students and high school students that are interested in computer vision and robotics. Two of them are currently working in industry.

+ When I am not busy, I am probably on [quora](https://www.quora.com/profile/Lekan-4), the [ros.org forum](http://answers.ros.org) or the [pytorch forum](http://discuss.pytorch.org) answering and posting questions.
