
I am a third-year Electrical Engineering Ph.D. student currently focused on biomedical robotics and applied control systems. I currently work with [Nick Gans](www.utdallas.edu/~ngans), [Steve Jiang](http://profiles.utsouthwestern.edu/profile/150563/steve-jiang.html), and [Tyler Summers](http://me.utdallas.edu/people/summers.html). My research is at the intersection of a buzzing field of learning research and an interesting field of systems theory: machine learning and control systems. Control theory helps me in formulating mathematical models while machine learning allows me the luxury of making sense out of chaotic data in order to drive real-world control applications. I try to solve problems that are difficult to model with existing mechanical models and Newtonian methods. I research along the lines of optimal control, adaptive neural dynamics, stability and robustness of performance, mostly in dynamical systems.
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

### Research Philosophy

I am a strong believer in **open science/technology** and **reproducible research**. If the problem is being avoided because it is difficult, then **you** should be the one solving it. I believe solid algorithms and codebases should be freely available to inquirers after knowledge. Open-sourcing one's code spurs force multipliers, which help get more work done _**faster and cheaper**_. To keep catastrophically good algorithms and codes more productive, one has to make them more accessible to other users and potential new developers. Therefore, I actively publish code of my works and that of others on [my github page](https://github.com/lakehanne). I am the author of [savitzky-golay](https://github.com/lakehanne/Savitzky-Golay/), [Soft-NeuroAdapt](https://github.com/lakehanne/soft-neuro-adapt), [farnn](https://github.com/lakehanne/farnn), [ensenso](https://github.com/lakehanne/ensenso) among others. Some of the projects that I have contributed to are pinned to my [github profile page](https://github.com/lakehanne.git).


## <i class="fa fa-chevron-right"></i> News
<table class="table table-hover">

<tr>
  <td class='col-md-3'>August 2017</td>
  <td>The camera-ready version of our <a href="https://arxiv.org/abs/1703.03821v3">Soft-NeuroAdapt</a> paper was accepted to IROS, and it is now live on arxiv. Codes are on <a href="https://github.com/lakehanne/soft-neuro-adapt">github</a>.</td>
</tr>

<tr>
  <td class='col-md-3'>July 2017</td>
  <td> A submission I co-authored on quantifying the sensitivity and building robustness into reinforcement-centric controllers got accepted to  <a href="https://iros2018.com">IROS</a> abstract only track. Codes <a href="https://github.com/lakehanne/gps/tree/corl">here</a>. Video <a href="https://www.youtube.com/watch?v=mNpU2oNcPtU&t=14s"> here.</a></td>
</tr>

<tr>
  <td class='col-md-3'>July 2017</td>
  <td>I won the  <a href="{{ site.url }}/scholternships#roscon">ROSCon</a> scholarship to attend the 2017 ROS Conference in Vancouver, BC!</td>
</tr>

<tr>
  <td class='col-md-3'>June 2017</td>
  <td>Brandon Amos' <a href="https://arxiv.org/pdf/1703.00443.pdf">OptNet paper</a> was accepted to ICML. I am mentioned in the acknowledgement section alongside <a href="https://en.wikipedia.org/wiki/Ian_Goodfellow">Ian Goodfellow</a>.</td>
</tr>

</table>

[iros-paper]: https://arxiv.org/abs/1703.03821
