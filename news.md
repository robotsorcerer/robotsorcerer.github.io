---
layout: post
permalink: news
---


<table class="table table-hover">
    {% for item in site.data.news.news_items %}
    {% for subitem in item.subnewsitems %} 
        <tr>
          <td>{{ subitem.content }} </td>
          <td class="col-md-3" style="text-align: right;">{{ subitem.date | date: "%B %e, %Y" }}</td>
        </tr>
    {% endfor %}
  {% endfor %}
</table> 
