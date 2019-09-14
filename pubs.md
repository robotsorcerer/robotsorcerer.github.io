---
layout: post
permalink: pubs
---
<?php include_once("analyticstracking.php") ?>
<table class="table table-hover" >
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
</table> 