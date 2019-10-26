---
layout: post
permalink: pubs
---
<?php include_once("analyticstracking.php") ?>

<table class="table table-hover" >
	For the IEEE publications on this page, be sure to follow the <a href="https://journals.ieeeauthorcenter.ieee.org/become-an-ieee-journal-author/publishing-ethics/guidelines-and-policies/policy-posting-your-journal-article">IEEE ethics and guidelines policy</a> when citing or using any of these materials. A skeleton of the policy is posted in the following paragraph.
	<hr>

	© 2019 IEEE.  Personal use of any of these materials is permitted.  Permission from IEEE must be obtained for all other uses, in any current or future media, including reprinting/republishing any of these materials for advertising or promotional purposes, creating new collective works, for resale or redistribution to servers or lists, or reuse of any copyrighted component of these works in other works.<br>

<!-- 	For more information, please see IEEE's preprints <a href="https://journals.ieeeauthorcenter.ieee.org/become-an-ieee-journal-author/publishing-ethics/guidelines-and-policies/policy-posting-your-journal-article/">Policy: Posting Your Journal Article.</a> -->

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
	      				(Appeared in) <a href="{{ paper.venue_web }}" target="blank">{{ paper.venue }}.  </a> {{ paper.year }}.
	      			{% endif %}
		      	{% else %}
		      		({{ paper.paper_status }}) {{ paper.venue }}.
		      	{% endif %}
		      	</td>
	      	</tr>
    	{% endfor %}
  	{% endfor %}
</table>
