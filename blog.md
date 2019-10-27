---
layout: post
permalink: blog
---
<?php include_once("analyticstracking.php") ?>

<ul class="posts">
  {% for post in site.posts %}
  <br>
    <li><span class = "post-date">
      <time>{{ post.date | date: "%b %-d, %Y" }}</time></span>
        <a class= "post-link" href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a>
      <br>
      {{  post.excerpt  }}
    </li>
  {% endfor %}
</ul>
