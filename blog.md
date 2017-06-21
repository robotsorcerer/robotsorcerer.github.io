---
layout: post
---
  <ul class="posts">
    {% for post in site.posts %}
    <br>
      <li><span class = "post-date">
        <time>{{ post.date | date: "%b %-d, %Y" }}</time></span>
        <center>
          <a class= "post-link" href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a>
        </center>
        <br>
        <center>{{  post.excerpt  }}</center>
      </li>
    {% endfor %}
    </ul>
