---
layout: default
title: Lekan Molu
---
<script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script>

<!-- ═══════════════════════════════════════════════
     HERO BANNER
═══════════════════════════════════════════════ -->
<div class="hero-section" style="margin: -28px -20px 28px; padding: 52px 0 40px; position: relative; overflow: hidden;">
  <canvas id="robo-canvas" style="position:absolute;top:0;left:0;width:100%;height:100%;z-index:0;opacity:0.38;pointer-events:none;"></canvas>
  <div class="hero-inner" style="position:relative;z-index:1;">
    <div class="hero-photo">
      <a href="/downloads/me-rodlab.jpg">
        <img src="/downloads/me-rodlab.jpg" alt="Lekan Molu">
      </a>
    </div>
    <div class="hero-text">
      <h1>Lekan Molu</h1>
      <p class="hero-subtitle">
        Researcher, roboticist, engineer --- in that order.
      </p>
      <div class="research-chips">
        <span class="chip">AI</span>
        <span class="chip">Robotics</span>
        <span class="chip">Control</span>
      </div>
      <div class="hero-links">
<!--         <a href="https://scholar.google.com/citations?user=JeUaqqEAAAAJ" target="_blank">
          <i class="ai ai-google-scholar"></i> Scholar
        </a> -->
        <a href="https://github.com/robotsorcerer" target="_blank">
          <i class="fa fa-github"></i> GitHub
        </a>
        <a href="https://www.linkedin.com/in/robotsorcerer" target="_blank">
          <i class="fa fa-linkedin"></i> LinkedIn
        </a>
        <a href="/pubs.html">
          <i class="fa fa-book"></i> Publications
        </a>
        <a href="mailto:lekanmolu@scriptedonachip.com">
          <i class="fa fa-envelope"></i> Email
        </a>
      </div>
    </div>
  </div>
</div>

{% include cv.md %}

<br>
<p style="color:#888;font-size:.8rem;">This web presence was last updated on {{ "now" | date: "%a, %b %d, %Y" }}.</p>

<script>
(function(){
  var canvas = document.getElementById('robo-canvas');
  if (!canvas) return;
  var ctx = canvas.getContext('2d');

  function resize() {
    canvas.width  = canvas.offsetWidth  || canvas.parentElement.offsetWidth;
    canvas.height = canvas.offsetHeight || canvas.parentElement.offsetHeight;
  }
  resize();
  window.addEventListener('resize', resize);

  var W = function(){ return canvas.width; };
  var H = function(){ return canvas.height; };

  /* ── Neural Network ── */
  var NN = {
    layers: [4, 6, 5, 3],
    pulses: [],
    tick: 0,
    nodes: function(){
      var all = [], lp = this.layers;
      lp.forEach(function(n, li){
        var x = W() * 0.08 + li * (W() * 0.18);
        for (var i = 0; i < n; i++){
          var y = H()*0.5 + (i - (n-1)/2) * Math.min(38, H()/lp.length);
          all.push({x:x, y:y, li:li, ni:i});
        }
      });
      return all;
    },
    update: function(){
      this.tick++;
      if (this.tick % 18 === 0){
        var li = Math.floor(Math.random()*(this.layers.length-1));
        this.pulses.push({li:li, ni:Math.floor(Math.random()*this.layers[li]),
          ni2:Math.floor(Math.random()*this.layers[li+1]), p:0,
          col:'rgba(160,216,255,'+(0.6+Math.random()*0.4)+')'});
      }
      this.pulses = this.pulses.filter(function(p){ return p.p < 1; });
      this.pulses.forEach(function(p){ p.p += 0.022; });
    },
    draw: function(){
      var nodes = this.nodes();
      var map = {};
      nodes.forEach(function(n){ map[n.li+','+n.ni] = n; });
      // Edges
      for (var li=0; li<this.layers.length-1; li++){
        for (var ni=0; ni<this.layers[li]; ni++){
          for (var ni2=0; ni2<this.layers[li+1]; ni2++){
            var a = map[li+','+ni], b = map[(li+1)+','+ni2];
            ctx.beginPath(); ctx.moveTo(a.x,a.y); ctx.lineTo(b.x,b.y);
            ctx.strokeStyle='rgba(77,184,255,0.18)'; ctx.lineWidth=0.7; ctx.stroke();
          }
        }
      }
      // Pulses
      this.pulses.forEach(function(p){
        var a=map[p.li+','+p.ni], b=map[(p.li+1)+','+p.ni2];
        if(!a||!b) return;
        var px=a.x+(b.x-a.x)*p.p, py=a.y+(b.y-a.y)*p.p;
        ctx.shadowBlur=10; ctx.shadowColor='#a0d8ff';
        ctx.beginPath(); ctx.arc(px,py,3,0,Math.PI*2);
        ctx.fillStyle=p.col; ctx.fill();
        ctx.shadowBlur=0;
      });
      // Nodes
      nodes.forEach(function(n){
        ctx.shadowBlur=7; ctx.shadowColor='#4db8ff';
        ctx.beginPath(); ctx.arc(n.x,n.y,5,0,Math.PI*2);
        ctx.fillStyle='rgba(77,184,255,0.85)'; ctx.fill();
        ctx.shadowBlur=0;
        ctx.strokeStyle='rgba(200,235,255,0.5)'; ctx.lineWidth=1; ctx.stroke();
      });
    }
  };

  /* ── 2-DOF Robot Arm ── */
  var Arm = {
    tick: 0,
    draw: function(){
      this.tick++;
      var t = this.tick * 0.016;
      var bx = W()*0.73, by = H()*0.68;
      var l1 = Math.min(65, H()*0.22), l2 = Math.min(48, H()*0.17);
      var th1 = -Math.PI/3 + Math.sin(t)*0.75;
      var th2 = Math.PI/4 + Math.cos(t*1.35)*0.9;
      var j1x = bx + l1*Math.cos(th1), j1y = by + l1*Math.sin(th1);
      var j2x = j1x + l2*Math.cos(th1+th2), j2y = j1y + l2*Math.sin(th1+th2);
      // Base mount
      ctx.beginPath(); ctx.arc(bx,by,9,0,Math.PI*2);
      ctx.fillStyle='rgba(126,200,227,0.7)'; ctx.fill();
      // Link 1
      ctx.shadowBlur=6; ctx.shadowColor='#7ec8e3';
      ctx.beginPath(); ctx.moveTo(bx,by); ctx.lineTo(j1x,j1y);
      ctx.strokeStyle='rgba(126,200,227,0.8)'; ctx.lineWidth=7; ctx.lineCap='round'; ctx.stroke();
      // Joint
      ctx.beginPath(); ctx.arc(j1x,j1y,6,0,Math.PI*2);
      ctx.fillStyle='rgba(43,168,176,0.9)'; ctx.fill();
      // Link 2
      ctx.beginPath(); ctx.moveTo(j1x,j1y); ctx.lineTo(j2x,j2y);
      ctx.strokeStyle='rgba(126,200,227,0.75)'; ctx.lineWidth=5; ctx.stroke();
      // End-effector (gripper)
      var ga = th1+th2+t*0.3;
      [1,-1].forEach(function(s){
        var gx=j2x+Math.cos(ga+Math.PI/2)*s*5, gy=j2y+Math.sin(ga+Math.PI/2)*s*5;
        ctx.beginPath(); ctx.moveTo(j2x,j2y); ctx.lineTo(gx+Math.cos(ga)*8, gy+Math.sin(ga)*8);
        ctx.strokeStyle='rgba(220,240,255,0.8)'; ctx.lineWidth=3; ctx.stroke();
      });
      ctx.beginPath(); ctx.arc(j2x,j2y,4,0,Math.PI*2);
      ctx.fillStyle='rgba(255,255,255,0.9)'; ctx.fill(); ctx.shadowBlur=0;
    }
  };

  /* ── Mobile Robots ── */
  function MobileRobot(pathFn, speed, col, sz){
    this.pathFn=pathFn; this.speed=speed; this.col=col; this.sz=sz||11;
    this.t=Math.random()*Math.PI*2; this.trail=[];
  }
  MobileRobot.prototype.update = function(){
    this.t += this.speed;
    var pos = this.pathFn(this.t);
    this.trail.push({x:pos.x, y:pos.y});
    if(this.trail.length > 45) this.trail.shift();
  };
  MobileRobot.prototype.draw = function(){
    // Trail
    for(var i=1; i<this.trail.length; i++){
      var a=(i/this.trail.length)*0.25;
      ctx.beginPath(); ctx.moveTo(this.trail[i-1].x,this.trail[i-1].y);
      ctx.lineTo(this.trail[i].x,this.trail[i].y);
      ctx.strokeStyle='rgba(43,168,176,'+a+')'; ctx.lineWidth=1.5; ctx.stroke();
    }
    var pos=this.pathFn(this.t);
    var prev=this.trail.length>1?this.trail[this.trail.length-2]:{x:pos.x-1,y:pos.y};
    var angle=Math.atan2(pos.y-prev.y, pos.x-prev.x);
    ctx.shadowBlur=9; ctx.shadowColor=this.col;
    ctx.beginPath(); ctx.arc(pos.x,pos.y,this.sz,0,Math.PI*2);
    ctx.fillStyle=this.col; ctx.fill(); ctx.shadowBlur=0;
    // Wheels
    [1,-1].forEach(function(s){
      var wx=pos.x+Math.cos(angle+Math.PI/2)*s*(this.sz*0.85);
      var wy=pos.y+Math.sin(angle+Math.PI/2)*s*(this.sz*0.85);
      ctx.beginPath(); ctx.arc(wx,wy,2.5,0,Math.PI*2);
      ctx.fillStyle='rgba(220,233,245,0.7)'; ctx.fill();
    }.bind(this));
    // Sensor blip
    ctx.beginPath(); ctx.arc(pos.x+Math.cos(angle)*this.sz,pos.y+Math.sin(angle)*this.sz,2,0,Math.PI*2);
    ctx.fillStyle='rgba(255,255,255,0.6)'; ctx.fill();
  };

  var robots = [
    new MobileRobot(function(t){
      return {x: W()*0.79+Math.cos(t*0.85)*W()*0.09, y: H()*0.28+Math.sin(t*0.85)*H()*0.13};
    }, 0.022, 'rgba(43,168,176,0.88)'),
    new MobileRobot(function(t){
      return {x: W()*0.86+Math.cos(t+Math.PI)*W()*0.05, y: H()*0.52+Math.sin(t*1.5)*H()*0.09};
    }, 0.028, 'rgba(77,184,255,0.8)', 8)
  ];

  /* ── Floating math / data particles ── */
  var SYMS = ['0','1','∇','∂','λ','σ','∫','θ','Σ','δ','u','x','ẋ'];
  function Particle(){
    this.reset = function(){
      this.x=Math.random()*W(); this.y=H()+8;
      this.vx=(Math.random()-0.5)*0.4; this.vy=-0.25-Math.random()*0.4;
      this.alpha=0.08+Math.random()*0.18; this.fs=8+Math.floor(Math.random()*7);
      this.ch=SYMS[Math.floor(Math.random()*SYMS.length)];
    };
    this.reset();
    this.y=Math.random()*H(); // scatter initial positions
  }
  Particle.prototype.update=function(){
    this.x+=this.vx; this.y+=this.vy;
    if(this.y<-12||this.x<-20||this.x>W()+20) this.reset();
  };
  Particle.prototype.draw=function(){
    ctx.font=this.fs+'px monospace';
    ctx.fillStyle='rgba(200,228,248,'+this.alpha+')';
    ctx.fillText(this.ch,this.x,this.y);
  };
  var particles=[];
  for(var i=0;i<28;i++) particles.push(new Particle());

  /* ── Faint grid ── */
  function drawGrid(){
    ctx.strokeStyle='rgba(255,255,255,0.04)'; ctx.lineWidth=1;
    var step=40;
    for(var x=0;x<W();x+=step){ ctx.beginPath();ctx.moveTo(x,0);ctx.lineTo(x,H());ctx.stroke(); }
    for(var y=0;y<H();y+=step){ ctx.beginPath();ctx.moveTo(0,y);ctx.lineTo(W(),y);ctx.stroke(); }
  }

  /* ── Control-loop arc (right side) ── */
  var clTick=0;
  function drawControlLoop(){
    clTick++;
    var cx=W()*0.62, cy=H()*0.5, rx=W()*0.055, ry=H()*0.22;
    // dashed ellipse representing feedback loop
    ctx.setLineDash([4,4]);
    ctx.beginPath(); ctx.ellipse(cx,cy,rx,ry,0,0,Math.PI*2);
    ctx.strokeStyle='rgba(200,228,248,0.18)'; ctx.lineWidth=1.2; ctx.stroke();
    ctx.setLineDash([]);
    // Animated arrow tip along the ellipse
    var ang = (clTick*0.025) % (Math.PI*2);
    var ax=cx+rx*Math.cos(ang), ay=cy+ry*Math.sin(ang);
    ctx.beginPath(); ctx.arc(ax,ay,3.5,0,Math.PI*2);
    ctx.fillStyle='rgba(160,216,255,0.7)'; ctx.fill();
    // Label
    ctx.font='9px Inter,sans-serif';
    ctx.fillStyle='rgba(200,228,248,0.3)';
    ctx.fillText('control loop', cx-22, cy+ry+12);
  }

  /* ── Main loop ── */
  function frame(){
    ctx.clearRect(0,0,W(),H());
    drawGrid();
    particles.forEach(function(p){ p.update(); p.draw(); });
    NN.update(); NN.draw();
    drawControlLoop();
    robots.forEach(function(r){ r.update(); r.draw(); });
    Arm.draw();
    requestAnimationFrame(frame);
  }
  frame();
})();
</script>
