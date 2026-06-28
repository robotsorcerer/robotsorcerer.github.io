---
layout: post
permalink: news
---


<!-- Featured Starling Murmurations Item — content sourced from _data/news.yaml (HJGauss_NeurIPS26) -->
<div style="position: relative; display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-bottom: 2rem; border-radius: 0.5rem; overflow: hidden; min-height: 300px;">
  <!-- Funnel/Cordon Formation -->
  <div style="position: relative; background-image: url(/assets/starlings_funnel.jpg); background-size: cover; background-position: center; border-radius: 0.5rem;">
    <div style="position: absolute; inset: 0; background: linear-gradient(135deg, rgba(0,0,0,0.2) 0%, rgba(0,0,0,0.25) 100%);"></div>
  </div>

  <!-- Split Formation -->
  <div style="position: relative; background-image: url(/assets/starlings_split.jpg); background-size: cover; background-position: center; border-radius: 0.5rem;">
    <div style="position: absolute; inset: 0; background: linear-gradient(135deg, rgba(0,0,0,0.2) 0%, rgba(0,0,0,0.25) 100%);"></div>
  </div>

  <!-- Overlaid News Content -->
  <style>
    @keyframes autoScroll {
      0% { transform: translateY(0); }
      50% { transform: translateY(-50%); }
      50.1% { transform: translateY(0); }
      100% { transform: translateY(0); }
    }
    .starling-news-scroll {
      animation: autoScroll 20s linear infinite;
    }
  </style>
  <div style="position: absolute; inset: 0; z-index: 10; display: flex; align-items: center; justify-content: center; padding: 2rem; background: linear-gradient(90deg, rgba(0,0,0,0.35) 0%, rgba(0,0,0,0.45) 50%, rgba(0,0,0,0.35) 100%); border-radius: 0.5rem;">
    <div style="color: #ffffff; text-align: left; max-height: 100%; overflow: hidden; width: 100%;">
      <div class="starling-news-scroll">
        {%- assign hjg = site.data.news.news_items | where: "items", "HJGauss_NeurIPS26" | first -%}
        {%- assign hjg_item = hjg.subnewsitems[0] -%}
        <div>
          <span style="display: block; font-size: 0.9rem; color: #FFB84D; font-weight: 700; margin-bottom: 0.75rem; text-shadow: 0 2px 6px rgba(0,0,0,0.8);">{{ hjg_item.date }}</span>
          <p style="margin: 0 0 2rem 0; font-size: 0.88rem; font-weight: 500; line-height: 1.6; text-shadow: 0 2px 5px rgba(0,0,0,0.8);">{{ hjg_item.content }}</p>
        </div>
        <div>
          <span style="display: block; font-size: 0.9rem; color: #FFB84D; font-weight: 700; margin-bottom: 0.75rem; text-shadow: 0 2px 6px rgba(0,0,0,0.8);">{{ hjg_item.date }}</span>
          <p style="margin: 0; font-size: 0.88rem; font-weight: 500; line-height: 1.6; text-shadow: 0 2px 5px rgba(0,0,0,0.8);">{{ hjg_item.content }}</p>
        </div>
      </div>
    </div>
  </div>
</div>


<!-- Featured RoboDiff Item — content sourced from _data/news.yaml (Robodiff) -->
<div style="position: relative; margin-bottom: 2rem; border-radius: 0.5rem; overflow: hidden; min-height: 300px;">
  <div style="position: relative; background-image: url(/assets/robodiff.gif); background-size: cover; background-position: center; border-radius: 0.5rem; min-height: 300px;">
    <div style="position: absolute; inset: 0; background: linear-gradient(135deg, rgba(0,0,0,0.2) 0%, rgba(0,0,0,0.25) 100%);"></div>

    <style>
      @keyframes autoScrollRobodiff {
        0% { transform: translateY(0); }
        50% { transform: translateY(-50%); }
        50.1% { transform: translateY(0); }
        100% { transform: translateY(0); }
      }
      .robodiff-news-scroll {
        animation: autoScrollRobodiff 18s linear infinite;
      }
      .robodiff-news-scroll a { color: #4FC3F7; font-weight: 600; }
    </style>
    <div style="position: absolute; inset: 0; z-index: 10; display: flex; align-items: center; justify-content: center; padding: 2rem; background: linear-gradient(90deg, rgba(0,0,0,0.35) 0%, rgba(0,0,0,0.45) 50%, rgba(0,0,0,0.35) 100%); border-radius: 0.5rem;">
      <div style="color: #ffffff; text-align: left; max-height: 100%; overflow: hidden; width: 100%;">
        <div class="robodiff-news-scroll">
          {%- assign robodiff = site.data.news.news_items | where: "items", "Robodiff" | first -%}
          {%- assign robodiff_item = robodiff.subnewsitems[0] -%}
          <div>
            <span style="display: block; font-size: 0.9rem; color: #FFB84D; font-weight: 700; margin-bottom: 0.75rem; text-shadow: 0 2px 6px rgba(0,0,0,0.8);">{{ robodiff_item.date }}</span>
            <p style="margin: 0 0 2rem 0; font-size: 0.88rem; font-weight: 500; line-height: 1.6; text-shadow: 0 2px 5px rgba(0,0,0,0.8);">{{ robodiff_item.content }}</p>
          </div>
          <div>
            <span style="display: block; font-size: 0.9rem; color: #FFB84D; font-weight: 700; margin-bottom: 0.75rem; text-shadow: 0 2px 6px rgba(0,0,0,0.8);">{{ robodiff_item.date }}</span>
            <p style="margin: 0; font-size: 0.88rem; font-weight: 500; line-height: 1.6; text-shadow: 0 2px 5px rgba(0,0,0,0.8);">{{ robodiff_item.content }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>


<!-- Shared styles for the generic auto-scrolling news reels -->
<style>
  .news-reel {
    position: relative;
    margin-bottom: 1.5rem;
    border-radius: 0.5rem;
    overflow: hidden;
    min-height: 220px;
  }
  /* Animated background layer — keeps every reel "alive" regardless of text length */
  .news-reel-bg { position: absolute; z-index: 0; background-size: cover; background-position: center; }
  .news-reel-bg--photo {
    inset: -6%;
    animation: reelPan 26s ease-in-out infinite alternate;
  }
  @keyframes reelPan {
    from { transform: scale(1.02) translate(0, 0); }
    to   { transform: scale(1.16) translate(-3%, -3%); }
  }
  .news-reel-bg--grad {
    inset: 0;
    background-size: 220% 220%;
    animation: reelFlow 20s ease infinite;
  }
  @keyframes reelFlow {
    0%   { background-position: 0% 50%; }
    50%  { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
  }
  .news-reel:hover .news-reel-bg { animation-play-state: paused; }
  .news-reel-overlay {
    position: absolute; inset: 0; z-index: 10;
    display: flex; align-items: center; justify-content: center;
    padding: 1.75rem;
    background: linear-gradient(90deg, rgba(0,0,0,0.45) 0%, rgba(0,0,0,0.55) 50%, rgba(0,0,0,0.45) 100%);
  }
  .news-reel-mask { color:#fff; text-align:left; width:100%; max-height:180px; overflow:hidden; }
  @keyframes newsReelScroll { from { transform: translateY(0); } to { transform: translateY(-50%); } }
  .news-reel-scroll { animation: newsReelScroll 26s linear infinite; }
  .news-reel:hover .news-reel-scroll { animation-play-state: paused; }
  @media (prefers-reduced-motion: reduce) {
    .news-reel-bg, .news-reel-scroll { animation: none !important; }
  }
  .news-reel-date { display:block; font-size:0.85rem; color:#FFB84D; font-weight:700; margin-bottom:0.5rem; text-shadow:0 2px 6px rgba(0,0,0,0.8); }
  .news-reel-text { margin:0; font-size:0.9rem; font-weight:500; line-height:1.6; text-shadow:0 2px 5px rgba(0,0,0,0.85); }
  .news-reel a { color:#7ec8f0; font-weight:600; }
</style>

{% assign sorted_news = site.data.news.news_items | sort: 'sortdate' | reverse %}
{% for item in sorted_news %}
{% unless item.items == 'HJGauss_NeurIPS26' or item.items == 'Robodiff' %}
{% assign it = item.subnewsitems[0] %}
{%- assign theme = item.theme -%}
{%- unless theme -%}
  {%- assign c = it.content | downcase -%}
  {%- if c contains 'weill' or c contains 'medical' or c contains 'mri' or c contains 'radiation' or c contains 'trauma' or c contains 'clinical' or c contains 'aapm' or c contains 'cyberknife' or c contains 'linac' or c contains 'soft-neuro' -%}{%- assign theme = 'medical' -%}
  {%- elsif c contains 'amazon' or c contains 'robot' or c contains 'icra' or c contains 'iros' or c contains 'manipulation' or c contains 'humanoid' or c contains 'digit' or c contains 'roscon' or c contains 'youbot' -%}{%- assign theme = 'robotics' -%}
  {%- elsif c contains 'control' or c contains 'cdc' or c contains 'ifac' or c contains 'nonlinear' or c contains 'equilibrium' or c contains 'policy optimization' or c contains 'adaptive' or c contains 'h-infinity' or c contains 'continuum' -%}{%- assign theme = 'control' -%}
  {%- elsif c contains 'congratulation' or c contains 'defended' or c contains 'awarded' or c contains 'scholarship' or c contains 'joined' or c contains 'cheer' or c contains 'nsf' or c contains 'thesis' -%}{%- assign theme = 'award' -%}
  {%- elsif c contains 'talk' or c contains 'spoke' or c contains 'presented' or c contains 'slides' or c contains 'workshop' or c contains 'delivered' or c contains 'teaching' -%}{%- assign theme = 'talk' -%}
  {%- else -%}{%- assign theme = 'default' -%}
  {%- endif -%}
{%- endunless -%}
{%- case theme -%}
{%- when 'robotics' -%}{%- assign grad = 'linear-gradient(135deg,#16263d 0%,#1a6fa8 100%)' -%}
{%- when 'medical' -%}{%- assign grad = 'linear-gradient(135deg,#5e1722 0%,#c14b63 100%)' -%}
{%- when 'control' -%}{%- assign grad = 'linear-gradient(135deg,#2d2a6e 0%,#6a5acd 100%)' -%}
{%- when 'talk' -%}{%- assign grad = 'linear-gradient(135deg,#33415c 0%,#c98a3a 100%)' -%}
{%- when 'award' -%}{%- assign grad = 'linear-gradient(135deg,#6b5200 0%,#d4af37 100%)' -%}
{%- else -%}{%- assign grad = 'linear-gradient(135deg,#243b55 0%,#141e30 100%)' -%}
{%- endcase -%}
{%- assign clen = it.content | strip_html | size -%}
<div class="news-reel">
  {% if item.bg %}
  <div class="news-reel-bg news-reel-bg--photo" style="background-image: linear-gradient(135deg, rgba(0,0,0,0.25), rgba(0,0,0,0.3)), url({{ item.bg }});"></div>
  {% else %}
  <div class="news-reel-bg news-reel-bg--grad" style="background-image: {{ grad }};"></div>
  {% endif %}
  <div class="news-reel-overlay">
    <div class="news-reel-mask">
      {% if clen > 300 %}
      <div class="news-reel-scroll">
        <div style="padding-bottom:1.5rem;">
          <span class="news-reel-date">{{ it.date }}</span>
          <p class="news-reel-text">{{ it.content }}</p>
        </div>
        <div style="padding-bottom:1.5rem;">
          <span class="news-reel-date">{{ it.date }}</span>
          <p class="news-reel-text">{{ it.content }}</p>
        </div>
      </div>
      {% else %}
      <div>
        <span class="news-reel-date">{{ it.date }}</span>
        <p class="news-reel-text">{{ it.content }}</p>
      </div>
      {% endif %}
    </div>
  </div>
</div>
{% endunless %}
{% endfor %}
