
Hello there. I am a third-year Electrical Engineering Ph.D. student currently focused on biomedical robotics and applied control systems.

#### Research Background

In radiotherapy treatment of cancer of the head and neck (H&N) region, patients are typically positioned in a supine manner on a 6-DOF robotic couch for motion alignment correction with respect to an incident radiation, used to target malignant tumors. As such, the precision of delivery of the radiation dose to target tumor is extremely important. Target miss in dosimetry angle or positioning errors arising from patient positioning errors have been known to cause eczema, brain complications and the exposure of organs at risks.
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

<!-- My solution is the only one so far that achieves desired actuation in closed-loop control and in real time without sacrificing time, treatment efficiency or patient comfort -- all based on a data-driven modeling approach and a mathematically proven stable neural-network based controller to compensate for the dynamics of the system. -->

### Research Philosophy

I am a strong believer in **open science/technology** and **groundbreaking, reproducible research**. If the problem is being avoided because it is difficult, then **you** should be the one solving it. I don't believe PhD students should be paper writers. You should study a problem well-enough, get familiar with it well-enough and propose clear, precise solutions that will stand the test of time. Sadly, this may mean you get to write less papers than your colleagues, but hey, no one wants to hire an ideas regurgitator anyway. I believe solid algorithms and codebases should be freely available to the humble inquirers after knowledge. Open-sourcing one's code spurs force multipliers, which help get more work done _**faster and cheaper**_. To keep wicked algorithms and codes more productive, one has to make them more accessible to other users and potential new developers. Therefore, I actively publish code of my works and that of others on [my github page](https://github.com/lakehanne). I am the author of [savitzky-golay](https://github.com/lakehanne/Savitzky-Golay/), [farnn](https://github.com/lakehanne/farnn), [ensenso](https://github.com/lakehanne/ensenso) among others. Projects that I have contributed to are pinned to my [github profile page](https://github.com/lakehanne.git).


### Things I do for fun

+ I am a co-owner of the Linux, OpenStack and Unix Networking video tutorials on [this](https://www.youtube.com/channel/UC-0PMn0rKV_ZOHF-qX6N3fQ/videos) youtube page.

+ I am a member of North Texas Drone Users Group. ~~Come July 8, I will be a part of the Guinness World Record Fly-in in the Dallas metroplex. We are a community of 1600 drone users in the DFW area. This fly-in will be the largest RC-controlled swarm  of quads on the world in a single run~~. 

+ I enjoy mentoring committed undergraduates, masters students and high school students that are interested in computer vision and robotics. Two of them are currently working in industry. 

<!-- + I enjoy cycling with my little man in the shortly-before-dusk hours around my neighborhood. -->

## <i class="fa fa-chevron-right"></i> News
<table class="table table-hover">
<tr>
  <td class='col-md-3'>June 2017</td>
  <td>Our <a href="https://arxiv.org/abs/1703.03821">3-DoF Neuro-Adaptive Controller</a> paper has been accepted to <a href="http://iros2017.org">IROS 2017</a> and the camera-ready version will soon be uploaded to arxiv.</td>
</tr>
<tr>
  <td class='col-md-3'>June 2017</td>
  <td>Brandon Amos' <a href="https://arxiv.org/pdf/1703.00443.pdf">OptNet paper</a> was accepted to ICML. I am mentioned in the acknowledgement section alongside <a href="https://en.wikipedia.org/wiki/Ian_Goodfellow">Ian Goodfellow</a>.</td>
</tr>
</table>

[iros-paper]: https://arxiv.org/abs/1703.03821
