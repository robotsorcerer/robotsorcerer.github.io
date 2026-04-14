---
layout: post
permalink: pubs
---

<div class="pubs-copyright">
© {{ "now" | date: "%Y" }} IEEE. Personal use of the IEEE materials here is permitted. Permission from IEEE must be obtained for all other uses, in any current or future media, including reprinting/republishing for advertising or promotional purposes, creating new collective works, for resale or redistribution to servers or lists, or reuse of any copyrighted component of these works in other works.
</div>

<div class="pubs-nav">
  <a href="#submits">Submitted</a> &middot;
  <a href="#pubs">Accepted/Published</a> &middot;
  <a href="#reps">Technical Reports</a> &middot;
  <a href="#abstracts">Presentations</a>
</div>

<!-- ═══════════════════════════════════════
     SUBMITTED
═══════════════════════════════════════ -->
<a name="submits"></a>
<div class="pub-section-title"><i class="fa fa-clock-o"></i>&nbsp; Submitted Works</div>

{% for item in site.data.papers.publications %}
  {% for paper in item.paperitems %}
    {% if paper.paper_status contains "Submitted" %}
<div class="pub-card">
  <div class="pub-card-inner">
    <div class="pub-thumb">
      {% if paper.thumbnail %}
        <img src="{{ paper.thumbnail }}" alt="thumbnail">
      {% else %}
        <div class="pub-no-thumb"><i class="fa fa-file-text-o"></i></div>
      {% endif %}
    </div>
    <div class="pub-body">
      <div class="pub-title">
        {% if paper.location and paper.location != "" and paper.location != "#" %}
          <a href="{{ paper.location }}" target="_blank">{{ paper.title }}</a>
        {% else %}
          {{ paper.title }}
        {% endif %}
      </div>
      <div class="pub-authors">
        {% for author in paper.authors %}{{ author }} {% endfor %}
      </div>
      <div class="pub-venue">
        {% if paper.venue_web and paper.venue_web != "" %}
          <a href="{{ paper.venue_web }}" target="_blank"><i>{{ paper.venue }}</i></a>
        {% else %}
          <i>{{ paper.venue }}</i>
        {% endif %}
      </div>
      <div class="pub-meta-row">
        <span class="pub-year">{{ paper.year }}</span>
        <span class="pub-badge badge-submitted">Under Review</span>
      </div>
      {% if paper.abstract %}
        <div class="pub-abstract-btn" onclick="this.classList.toggle('is-open'); this.nextElementSibling.classList.toggle('is-open');">
          <i class="fa fa-chevron-down"></i> Abstract
        </div>
        <div class="pub-abstract">{{ paper.abstract }}</div>
      {% endif %}
    </div>
  </div>
</div>
    {% endif %}
  {% endfor %}
{% endfor %}
<!-- ═══════════════════════════════════════
     ACCEPTED / PUBLISHED
═══════════════════════════════════════ -->
<a name="pubs"></a>
<div class="pub-section-title"><i class="fa fa-check-circle"></i>&nbsp; Accepted or Published Works</div>

{% for item in site.data.papers.publications %}
  {% for paper in item.paperitems %}
    {% if paper.paper_status == "Accepted" %}
<div class="pub-card">
  <div class="pub-card-inner">
    <div class="pub-thumb">
      {% if paper.thumbnail %}
        <img src="{{ paper.thumbnail }}" alt="thumbnail">
      {% else %}
        <div class="pub-no-thumb"><i class="fa fa-file-text-o"></i></div>
      {% endif %}
    </div>
    <div class="pub-body">
      <div class="pub-title">
        {% if paper.location and paper.location != "" and paper.location != "#" %}
          <a href="{{ paper.location }}" target="_blank">{{ paper.title }}</a>
        {% else %}
          {{ paper.title }}
        {% endif %}
      </div>
      <div class="pub-authors">
        {% for author in paper.authors %}{{ author }} {% endfor %}
      </div>
      <div class="pub-venue">
        {% if paper.venue_web and paper.venue_web != "" %}
          <a href="{{ paper.venue_web }}" target="_blank"><i>{{ paper.venue }}</i></a>
        {% else %}
          <i>{{ paper.venue }}</i>
        {% endif %}
      </div>
      <div class="pub-meta-row">
        <span class="pub-year">{{ paper.year }}</span>
        <span class="pub-badge badge-accepted">Published</span>
        {% if paper.video %}
          <a href="{{ paper.video }}" target="_blank" class="pub-badge badge-report"><i class="fa fa-play-circle"></i> Video</a>
        {% endif %}
      </div>
      {% if paper.abstract %}
        <div class="pub-abstract-btn" onclick="this.classList.toggle('is-open'); this.nextElementSibling.classList.toggle('is-open');">
          <i class="fa fa-chevron-down"></i> Abstract
        </div>
        <div class="pub-abstract">{{ paper.abstract }}</div>
      {% endif %}
    </div>
  </div>
</div>
    {% endif %}
  {% endfor %}
{% endfor %}

<!-- ═══════════════════════════════════════
     TECHNICAL REPORTS
═══════════════════════════════════════ -->
<a name="reps"></a>
<div class="pub-section-title"><i class="fa fa-file-text"></i>&nbsp; Technical Reports</div>

{% for item in site.data.papers.publications %}
  {% for paper in item.paperitems %}
    {% if paper.paper_status contains "Technical" %}
<div class="pub-card">
  <div class="pub-card-inner">
    <div class="pub-thumb">
      {% if paper.thumbnail %}
        <img src="{{ paper.thumbnail }}" alt="thumbnail">
      {% else %}
        <div class="pub-no-thumb"><i class="fa fa-file-text-o"></i></div>
      {% endif %}
    </div>
    <div class="pub-body">
      <div class="pub-title">
        {% if paper.location and paper.location != "" and paper.location != "#" %}
          <a href="{{ paper.location }}" target="_blank">{{ paper.title }}</a>
        {% else %}
          {{ paper.title }}
        {% endif %}
      </div>
      <div class="pub-authors">
        {% for author in paper.authors %}{{ author }} {% endfor %}
      </div>
      <div class="pub-venue">
        {% if paper.venue_web and paper.venue_web != "" %}
          <a href="{{ paper.venue_web }}" target="_blank"><i>{{ paper.venue }}</i></a>
        {% else %}
          <i>{{ paper.venue }}</i>
        {% endif %}
      </div>
      <div class="pub-meta-row">
        <span class="pub-year">{{ paper.year }}</span>
        <span class="pub-badge badge-report">Technical Report</span>
      </div>
      {% if paper.abstract %}
        <div class="pub-abstract-btn" onclick="this.classList.toggle('is-open'); this.nextElementSibling.classList.toggle('is-open');">
          <i class="fa fa-chevron-down"></i> Abstract
        </div>
        <div class="pub-abstract">{{ paper.abstract }}</div>
      {% endif %}
    </div>
  </div>
</div>
    {% endif %}
  {% endfor %}
{% endfor %}

<!-- ═══════════════════════════════════════
     PRESENTATIONS / ABSTRACTS
═══════════════════════════════════════ -->
<a name="abstracts"></a>
<div class="pub-section-title"><i class="fa fa-microphone"></i>&nbsp; Presentations</div>

{% for item in site.data.papers.publications %}
  {% for paper in item.paperitems %}
    {% if paper.paper_status contains "Abstract" or paper.paper_status contains "Oral" %}
<div class="pub-card">
  <div class="pub-card-inner">
    <div class="pub-thumb">
      {% if paper.thumbnail %}
        <img src="{{ paper.thumbnail }}" alt="thumbnail">
      {% else %}
        <div class="pub-no-thumb"><i class="fa fa-microphone"></i></div>
      {% endif %}
    </div>
    <div class="pub-body">
      <div class="pub-title">
        {% if paper.location and paper.location != "" and paper.location != "#" %}
          <a href="{{ paper.location }}" target="_blank">{{ paper.title }}</a>
        {% else %}
          {{ paper.title }}
        {% endif %}
      </div>
      {% if paper.authors.size > 1 %}
      <div class="pub-authors">
        {% for author in paper.authors %}{{ author }} {% endfor %}
      </div>
      {% endif %}
      <div class="pub-venue">
        {% if paper.venue_web and paper.venue_web != "" %}
          <a href="{{ paper.venue_web }}" target="_blank"><i>{{ paper.venue }}</i></a>
        {% else %}
          <i>{{ paper.venue }}</i>
        {% endif %}
      </div>
      <div class="pub-meta-row">
        <span class="pub-year">{{ paper.year }}</span>
        {% if paper.paper_status contains "Oral" %}
          <span class="pub-badge badge-oral"><i class="fa fa-microphone"></i> Oral</span>
        {% else %}
          <span class="pub-badge badge-report">Abstract</span>
        {% endif %}
      </div>
    </div>
  </div>
</div>
    {% endif %}
  {% endfor %}
{% endfor %}
