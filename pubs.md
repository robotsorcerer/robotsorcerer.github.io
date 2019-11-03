---
layout: post
permalink: pubs
---
<?php include_once("analyticstracking.php") ?>

<table class="table table-hover" >
	<!--For the IEEE publications on this page, be sure to follow the <a href="https://journals.ieeeauthorcenter.ieee.org/become-an-ieee-journal-author/publishing-ethics/guidelines-and-policies/policy-posting-your-journal-article">IEEE ethics and guidelines policy</a> when citing or using any of these materials. A skeleton of the policy is posted in the following paragraph.
	<hr> -->

© 2019 IEEE.  Unless a manuscript has not been published, personal use of any of these materials is permitted.

Permission from IEEE must be obtained for all IEEE publications for other uses, in any current or future media, including reprinting/republishing any of these materials for advertising or promotional purposes, creating new collective works, for resale or redistribution to servers or lists, or reuse of any copyrighted component of these works in other works.<br>

<h3><b>Published</b></h3>
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

<table  class="table table-hover" >	
  	<h3><b>Under Review</b></h3>
		{% for item in site.data.papers.publications %}
	    	{% for paper in item.paperitems %}
	          	{% if paper.paper_status contains "Submit" %}
		        	<tr>
		          		<td width="95%" align="left"><a href="{{ paper.location }}" 	target="blank">{{  paper.title  }}.</a><br>
		          			{% for author in paper.authors %}
		          				{{ author  }}
		          			{% endfor %}<br>
		      				<a href="{{ paper.venue_web }}" target="blank"><i>{{ paper.venue }}</i>.  </a> {{ paper.year }}.
			      		</td>
		      		</tr>
		      	{% endif %}
	    	{% endfor %}
	  	{% endfor %}	
</table>

<table  class="table table-hover" >	
  	<h3><b><a href="https://en.wikipedia.org/wiki/Working_paper">Working Papers</a></b></h3>
		{% for item in site.data.papers.publications %}
	    	{% for paper in item.paperitems %}
	          	{% if paper.paper_status contains "Manuscript" %}
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


<!--     {% for item in site.data.papers.publications %}
    	{% for paper in item.paperitems %}
	        <tr>
	          <td width="95%" align="left"><a href="{{ paper.location }}" target="blank">{{  paper.title  }}.</a><br>
	          	{% for author in paper.authors %}
	          		{{ author  }}
	          	{% endfor %}<br>
	          	{% if paper.venue_web %}
		          	{% if paper.paper_status !="Accepted" %}
	      				({{ paper.paper_status }}) <a href="{{ paper.venue_web }}" target="blank">{{ paper.venue }},  </a> {{ paper.year }}.
	      			{% else %}
	      				(Appeared in) <a href="{{ paper.venue_web }}" target="blank">{{ paper.venue }}.  </a> {{ paper.year }}.
	      			{% endif %}
		      	{% else %}
		      		({{ paper.paper_status }}) {{ paper.venue }}.
		      	{% endif %}
		      	</td>
	      	</tr>
    	{% endfor %}
  	{% endfor %} -->	  	