---
layout: post
permalink: pubs
---
<?php include_once("analyticstracking.php") ?>
<!-- <table class="table table-hover" >
    {% for item in site.data.papers.publications %}
    	{% for paper in item.paperitems %} 
	        <tr>
	          <td width="95%" align="left"><a href="{{ paper.location }}" target="blank">{{  paper.title  }}.</a><br>
	          	{% for author in paper.authors %}
	          		{{ author  }}
	          	{% endfor %}<br>
	          	{% if paper.venue_web %}
		          	{% if paper.paper_status !="Accepted" %}
	      				({{ paper.paper_status }}) <a href="{{ paper.venue_web }}" target="blank">{{ paper.venue }},  {{ paper.year }}.</a> 
	      			{% else %}
	      				<a href="{{ paper.venue_web }}" target="blank">{{ paper.venue }},  {{ paper.year }}.</a> 
	      			{% endif %}
		      	{% else %}
		      		({{ paper.paper_status }}) {{ paper.venue }}.
		      	{% endif %}
		      	</td>
	      	</tr>
    	{% endfor %}
  	{% endfor %}
</table>  -->

<table class="table table-hover" >
	© 2019 IEEE.  Personal use of any of these materials is permitted.  Permission from IEEE must be obtained for all other uses, in any current or future media, including reprinting/republishing this material for advertising or promotional purposes, creating new collective works, for resale or redistribution to servers or lists, or reuse of any copyrighted component of this work in other works.”<br>

	For more information, please see IEEE's preprints <a href="https://journals.ieeeauthorcenter.ieee.org/become-an-ieee-journal-author/publishing-ethics/guidelines-and-policies/policy-posting-your-journal-article/">Policy: Posting Your Journal Article.</a>

    {% for item in site.data.papers.publications %}
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
	      				Appeared in <a href="{{ paper.venue_web }}" target="blank">{{ paper.venue }}.  </a> {{ paper.year }}.
	      			{% endif %}
		      	{% else %}
		      		({{ paper.paper_status }}) {{ paper.venue }}.
		      	{% endif %}
		      	</td>
	      	</tr>
    	{% endfor %}
  	{% endfor %}
</table> 