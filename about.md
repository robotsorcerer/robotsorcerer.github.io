---
layout: page
permalink: about
---

<?php include_once("analyticstracking.php") ?>

<!-- <img src="/downloads/Pat.jpg" alt="Me" align="right" style="width:100px;height:100px;"> -->
Welcome to my blog, where theory meets practice, and where scientific elegance meets cool engineering impact. Fields that consume the bulk of my attention currently include control theory, game theory, robotics, and certainly deep/reinforcement learning.


<!-- My work explores better model representation in dynamical systems using state-of-the-art neural network function approximators to determine accurate system models, for example in adaptive control or model predictive control of complex nonlinear systems. My background is in Physics and Control theory and I spend my PhD research exploring better ways of automating motion alignment correction systems in clinical cancer radiotherapy of malignant cancers of the head and neck region. The novelty of my work includes (i) the design and use of soft robots with morphological computation properties to dynamically adjust patient motion along desired degrees of freedom during cancer radiotherapy treatment; (ii) adaptive function approximators to model these coupled nonlinearities.  As these soft actuators are nonlinear, a lot of effort goes into formulating the model properties of the hardware in order to obtain an effective controller that can deliver the required sub-millimeter and sub-degree accuracy. Owing to the recent advances in sequential deep learning frameworks in terms of their accuracy and precision in generating powerful models for tasks including speech recognition and machine language translation, I leverage on these technologies to create dynamic models of the patient testbed and to design appropriate adaptive controllers to scale. -->

<!-- I am a part of the SeRViCE lab at UT Dallas, advised by [Nick Gans](www.utdallas.edu/~ngans). I spent the summer and fall semesters of 2017 partly in [Tyler Summer's](http://me.utdallas.edu/people/summers.html) [control, optimization, and networks lab](http://www.utdallas.edu/~tyler.summers/), where I worked on game theoretic approaches to reinforcement learning problems.
I am also a member of the [medical artificial intelligence and automation lab](http://www.utsouthwestern.edu/labs/maia/about/meet-our-team.html) (MAIA) within the medical engineering division of UT Southwestern's Radiation Oncology department. Here, I work on learning control problems for optimal beam angle orientation during intensity modulated cancer radiotherapy. I am privileged to be advised by [Steve Jiang](http://profiles.utsouthwestern.edu/profile/150563/steve-jiang.html). -->

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

The idea is that by actuating elastomeric polymer enclosures that inflate or deflate based on the amount of air that is sent into them or by the amount of pressure that is exerted on them by a human-body part (such as the head or neck), one can achieve a desired level of pose in frameless or maskless radiotherapy without sacrificing patient comfort or treatment efficacy as existing technologies allow.

### Random Facts

+ I am a member of North Texas Drone Users Group. We fly our drones, micro-UAVs, and mini-planes around the DFW area every Saturday just to disturb the peace and quiet of boring citizens.

+ I am a co-owner of the Linux, OpenStack, and Unix Networking video tutorials on [this](https://www.youtube.com/channel/UC-0PMn0rKV_ZOHF-qX6N3fQ/videos) youtube page.

+ I regularly peer-review for the following academic conferences and journals:

    &nbsp; &nbsp; &nbsp; &nbsp; - Institute of Physics: Measurement Science and Technology (Journal)

    &nbsp; &nbsp; &nbsp; &nbsp; - International Conference on Robotics and Automation (ICRA)

    &nbsp; &nbsp; &nbsp; &nbsp; - International Conference on Intelligent Robots and Systems (IROS)

    &nbsp; &nbsp; &nbsp; &nbsp; - Neural Computing and Applications (NCAA Journal)

    &nbsp; &nbsp; &nbsp; &nbsp; - International Federation of Automatic Control (IFAC) World Congress

    &nbsp; &nbsp; &nbsp; &nbsp; - American Control Conference (ACC)

+ I had my masters degree in Control Systems from Sheffield Uni in the UK.

+ I had my Bachelors in Physics. Specifically, my thesis was on the single fractional parentage coefiicients in the sd-shell nuclei, advised by [Prof. Ademola Amusa](https://www.linkedin.com/in/ademola-amusa-b40812122/).

+ I enjoy mentoring committed undergraduates, masters students, and occasionally high school students that are interested in computer vision and robotics.

    &nbsp; &nbsp; &nbsp; &nbsp; -   [Ajith](https://www.linkedin.com/in/ajithvenkateswaran) is a Senior Robotics Software Engineer in Samsung Research, America.

    &nbsp; &nbsp; &nbsp; &nbsp; -   [Adwait](https://www.linkedin.com/in/adwaitkulkarni93) is an Engineer at Drov. Tech, MN.

    &nbsp; &nbsp; &nbsp; &nbsp; -   [Rachel](https://github.com/rsthomp) is currently an undergrad at MIT's CSAIL department.

+   I enjoy working with hardware, observing the physics of things, and devising the interconnectedness of disparate electro-mechanical components in order to bring about a congruent whole.

<!-- + I still consider Sheffield my adopted home. Biggest village in Yorkshire, where I've made some of my biggest mistakes; where I've met some of the best people I could ever hope to know. City of hills. Home of the Yorkshire pudding. Of thee I sing! -->
+  Since people often ask me about how to pronounce my name, and its meaning, Lekan is the short form of "Olalekan", which literally means "wealth increased by a factor of one" in [Yoruba](https://en.wikipedia.org/wiki/Yoruba_language), a (Benin-Congo) language of the [Yoruba people](https://en.wikipedia.org/wiki/Yoruba_people) of West Africa. It is pronounced "Lay-con", or "Lay-kañ", where "añ" is akin to the intonation of "TION" "capTION".  My last name is rather a little long-winding to roll on the tongue. But let me give a background first. From what I understand, my paternal ancestors were [Ifá](https://en.wikipedia.org/wiki/If%C3%A1) divinators who from time to time worshipped the god of iron, referred to as Ogun in the Yoruba language; "molu" is the short form of "mu olu", often abbreviated as "m'olu" in written scripts; it means "take victory" or something of that sort. Therefore, Ogunmolu means "the god of iron prevailed". It's altogether pronounced as "O-goon-moh-loo". There you go.

+   When I am not busy, I am probably on [quora](https://www.quora.com/profile/Lekan-4), the [ros.org forum](http://answers.ros.org) or the [pytorch forum](http://discuss.pytorch.org) answering and posting questions.

+   Among the places I call home include Lagos, Nigeria; Sheffield, United Kingdom; Boston, MA; and of course Tokyo, Japan.

[iros-paper]: https://arxiv.org/abs/1703.03821v3
