---
layout: post
permalink: pubs
---
<?php include_once("analyticstracking.php") ?>

> Intent upon giving as much as I have gotten, here are my contributions, given freely and cheerfully.

<!-- , as I shine my little light more and more upon the unknown until our collective knowledge is as bright as the perfect day.  -->


© 2019 IEEE.  Personal use of the IEEE materials here is permitted.  Permission from IEEE must be obtained for all other uses, in any current or future media, including reprinting/republishing any of these materials for advertising or promotional purposes, creating new collective works, for resale or redistribution to servers or lists, or reuse of any copyrighted component of these works in other works.<br><br>


<table class="table table-hover" >
	<!--For the IEEE publications on this page, be sure to follow the <a href="https://journals.ieeeauthorcenter.ieee.org/become-an-ieee-journal-author/publishing-ethics/guidelines-and-policies/policy-posting-your-journal-article">IEEE ethics and guidelines policy</a> when citing or using any of these materials. A skeleton of the policy is posted in the following paragraph. Unless a manuscript has not been published, personal use of any of these materials is permitted.

	<hr> -->


<center>
<a href="#unpubs"><font size="4">Working Papers / </font></a>
<a href="#revs"><font size="4">Papers Under Review / </font></a>
<a href="#pubs"><font size="4">Published Papers / </font></a>
<a href="#reps"><font size="4">Technical Reports.</font></a>
</center>

<a name="unpubs"></a>
<!-- <table  class="table table-hover" >	
  	<center><h3><b><a href="https://en.wikipedia.org/wiki/Working_paper">Working Papers</a></b></h3></center>
		These papers are working manuscripts of ideas I am actively exploring in my head or rapidly prototyping, machines I have built and now tearing apart in order to build more robustness and and explore underactuation and more natural dynamics. I would be happy to hear from you on how to improve them etc.
		{% for item in site.data.papers.publications %}
	    	{% for paper in item.paperitems %}
	          	{% if paper.paper_status contains "Manuscript" %}
		        	<tr>
		          		<td width="95%" align="left"><a href="{{ paper.location }}" 	target="blank">{{  paper.title  }}.</a><br>
		          			{% for author in paper.authors %}
		          				{{ author  }}
		          			{% endfor %} 
		      				<a href="{{ paper.venue_web }}" target="blank"><i>{{ paper.venue }}</i></a> {{ paper.year }}.
			      		</td>
		      		</tr>
		      	{% endif %}
	    	{% endfor %}
	  	{% endfor %}	
</table>
 -->
<!-- 
<a name="revs"></a>
<table  class="table table-hover" >	
  	<center><h3><b>Papers Under Review</b></h3></center>
		{% for item in site.data.papers.publications %}
	    	{% for paper in item.paperitems %}
	          	{% if paper.paper_status contains "Submit" %}
		        	<tr>
		          		<td width="95%" align="left"><a href="{{ paper.location }}" 	target="blank">{{  paper.title  }}.</a><br>
		          			{% for author in paper.authors %}
		          				{{ author  }}
		          			{% endfor %}<br>
		      				<a href="{{ paper.venue_web }}" target="blank"><i>{{ paper.venue }}</i>.  </a> ({{ paper.paper_status }}) {{ paper.year }}.
			      		</td>
		      		</tr>
		      	{% endif %}
	    	{% endfor %}
	  	{% endfor %}	
</table>
 -->

<a name="pubs"></a>
<table  class="table table-hover" >	
<center><h3><b>Published Works</b></h3></center>

Premier IEEE Robotics and Automation Society, Algorithmic Foundations of Robotics, and Medical Physics publications (WAFR, IROS, NIPS, PhysMed, and ICRA) are highly selective venues for archival papers, similar to selective IEEE journals in visibility and strong scientific/engineering communications.

		{% for item in site.data.papers.publications %}
	    	{% for paper in item.paperitems %}
	          	{% if paper.paper_status contains "Accepted" %}
		        	<tr>
		          		<td width="95%" align="left"><a href="{{ paper.location }}" 	target="blank">{{  paper.title  }}.</a><br>
		          			{% for author in paper.authors %}
		          				{{ author  }}
		          			{% endfor %}<br>
		      				<a href="{{ paper.venue_web }}" target="blank"><i>{{ paper.venue }}</i>.  </a> {{ paper.year }}.<br>
			      		</td>
		      		</tr>
		      	{% endif %}
	    	{% endfor %}
	  	{% endfor %} 	
</table>

<a name="reps"></a>
<table  class="table table-hover" >	
  	<center><h3><b>Technical Reports</b></h3></center>
		{% for item in site.data.papers.publications %}
	    	{% for paper in item.paperitems %}
	          	{% if paper.paper_status contains "Technical" %}
		        	<tr>
		          		<td width="95%" align="left"><a href="{{ paper.location }}" 	target="blank">{{  paper.title  }}.</a><br>
		          			{% for author in paper.authors %}
		          				{{ author  }}
		          			{% endfor %} 
		      				<a href="{{ paper.venue_web }}" target="blank"><i>{{ paper.venue }}</i>.  </a> {{ paper.year }}.
			      		</td>
		      		</tr>
		      	{% endif %}
	    	{% endfor %}
	  	{% endfor %}	
</table>
