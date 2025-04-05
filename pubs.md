---
layout: post
permalink: pubs
---


© {{ "now" | date: "%Y" }} IEEE.  Personal use of the IEEE materials here is permitted.  Permission from IEEE must be obtained for all other uses, in any current or future media, including reprinting/republishing any of these materials for advertising or promotional purposes, creating new collective works, for resale or redistribution to servers or lists, or reuse of any copyrighted component of these works in other works. <br><br>


<table class="table table-hover" >

<hr>

<center>
<a href="#submits"><font size="4">Submitted / </font></a>
<!-- <a href="#unpubs"><font size="4">Preprints / </font></a> -->
<!-- <a href="#revs"><font size="4">Under Revision / </font></a> -->
<a href="#pubs"><font size="4"> Published / </font></a>
<a href="#reps"><font size="4">Technical Reports /</font></a>
<a href="#abstracts"><font size="4">Presentations. / </font></a>
</center>

<a name="submits"></a>
<table  class="table table-hover" >
<center><h3><b>Submitted Works</b></h3></center>
		{% for item in site.data.papers.publications %}
	    	{% for paper in item.paperitems %}
          	{% if paper.paper_status contains "Submitted" %}
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

<!-- <hr>
<a name="unpubs"></a>
<table  class="table table-hover" >
  	<center><h3><b><a href="https://en.wikipedia.org/wiki/Working_paper">Preprints/Evolving Drafts</a></b></h3></center>
{% for item in site.data.papers.publications %}
  	{% for paper in item.paperitems %}
	          	{% if paper.paper_status contains "Manuscript" %}
		        	<tr>
		          		<td width="95%" align="left"><a href="{{ paper.location }}" 	target="blank">{{  paper.title  }}.</a><br>
		          			{% for author in paper.authors %}
		          				{{ author  }}
		          			{% endfor %}
			      		</td>
		      		</tr>
		      	{% endif %}
	    	{% endfor %}
	  	{% endfor %}
</table> -->

<hr>
<a name="pubs"></a>
<table  class="table table-hover" >
<center><h3><b>Accepted or Published Works</b></h3></center>

{% for item in site.data.papers.publications %}
	{% for paper in item.paperitems %}
      	{% if paper.paper_status=="Accepted" %}
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



<hr>
<a name="abstracts"></a>
<table  class="table table-hover" >
<center><h3><b>Presentations</b></h3></center>

{% for item in site.data.papers.publications %}
	{% for paper in item.paperitems %}
      	{% if paper.paper_status contains "Abstract"  or paper.venue contains "Oral Presentation" %}
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

<a name="revs"></a>
<!-- <table  class="table table-hover" >
<center><h3><b>Revision for Final Decision</b></h3></center>
		{% for item in site.data.papers.publications %}
	    	{% for paper in item.paperitems %}
          	{% if paper.paper_status contains "Revision" %}
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
</table> -->

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

