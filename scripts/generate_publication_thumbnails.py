#!/usr/bin/env python3
"""Regenerate the publication SVG schematics (requires PyYAML).

Run from any directory: python scripts/generate_publication_thumbnails.py
The two original ICRA/ICLR animations are maintained separately. These are
conceptual illustrations, not plots of measurements or simulated results.
"""
from html import escape
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets/thumbs'

# Related papers share a visual vocabulary, with paper-specific captions.
DESIGNS = {
    'icml26': ('reach', 'HJ–GAUSS', 'SAMPLE · PROPAGATE'),
    'infdiff': ('diffusion', 'DIFFUSION POLICY', 'DENOISE · CONTROL'),
    'gnep_socio': ('game', 'TEAM EQUILIBRIA', 'COORDINATE · RESPOND'),
    'cfree': ('map', 'COLLISION-FREE', 'MAP · PLAN · MOVE'),
    'levelsetpy': ('reach', 'LEVELSETPY', 'GRID · EVOLVE · SOLVE'),
    'toms_supp': ('reach', 'REACHABILITY', 'BENCHMARK · COMPARE'),
    'sorospt': ('soft', 'STRAIN CONTROL', 'FAST + SLOW DYNAMICS'),
    'levelsetpy_cdc': ('reach', 'HJ TOOLBOX', 'PROPAGATE · VERIFY'),
    'soropd': ('soft', 'COSSERAT RODS', 'STRUCTURE · CONTROL'),
    'vecnn': ('barrier', 'NEURAL BARRIERS', 'LEARN · VERIFY'),
    'pclast': ('latent', 'PLANNABLE LATENTS', 'ENCODE · PLAN'),
    'ifac': ('control', 'MIXED H₂ / H∞', 'EVALUATE · IMPROVE'),
    'h2hinf': ('control', 'ROBUST POLICIES', 'LEARN · ATTENUATE'),
    'lsd': ('latent', 'LATENT DYNAMICS', 'OBSERVE · DISCOVER'),
    'igl': ('feedback', 'GROUNDED LEARNING', 'ACT · OBSERVE · LEARN'),
    'icra20': ('patient', 'SOFT STABILIZATION', 'SENSE · COMPENSATE'),
    'medphys': ('beam', 'LEARNED BEAM ANGLES', 'PREDICT · SELECT'),
    'iccr19': ('beam', 'NEURAL BEAM PLANS', 'LEARN · ORIENT'),
    'phdthesis': ('patient', 'ROBOTIC THERAPY', 'POSITION · TREAT'),
    'airt2019': ('tree', 'GUIDED TREE SEARCH', 'SEARCH · SELECT'),
    'wafr': ('beam', 'DEEP BOO', 'IMITATE · PLAN'),
    'iros18': ('minimax', 'MINIMAX CONTROL', 'ACT · COUNTERACT'),
    'spie': ('patient', 'SOFT ROBOT DESIGN', 'ACTUATE · POSITION'),
    'iros17': ('patient', 'SOFT-NEUROADAPT', 'ADAPT · CORRECT'),
    'case2016': ('patient', 'VISION FEEDBACK', 'TRACK · CORRECT'),
    'case2015': ('patient', 'PATIENT POSITIONING', 'SENSE · REGULATE'),
    'springer2019': ('patient', 'MOTION COMPENSATION', 'TRACK · STABILIZE'),
    'zerosum': ('minimax', 'ZERO-SUM LEARNING', 'POLICY + ADVERSARY'),
    'ident': ('identify', 'DYNAMIC MODELS', 'OBSERVE · IDENTIFY'),
    'nerc_soropd': ('soft', 'LAGRANGIAN ROBOTS', 'MODEL · CONTROL'),
    'nerc_sorospt': ('soft', 'FAST–SLOW CONTROL', 'REGULATE · TRACK'),
    'pclast_nerc': ('latent', 'LATENT-SPACE PLANS', 'REPRESENT · PLAN'),
    'igl2_workshop': ('feedback', 'ACTION + FEEDBACK', 'INTERACT · LEARN'),
    'aapm21b': ('patient', 'MRI–LINAC ROBOT', 'CORRECT HEAD MOTION'),
    'aapm20_poster': ('patient', 'HEAD POSE CONTROL', 'TRACK · COMPENSATE'),
    'aapm20_workspace': ('map', 'MOTION PLANNING', 'SEARCH · POSITION'),
    'aapm20': ('patient', 'SOFT ACTUATORS', 'CLOSED-LOOP CONTROL'),
    'aapm19': ('beam', 'BEAM PREDICTION', 'LEARN · SELECT'),
    'aapm19az': ('tree', 'BEAM TREE SEARCH', 'EXPLORE · PLAN'),
    'aapm19myne': ('beam', 'BEAM POLICIES', 'EVALUATE · IMPROVE'),
    'iros18_workshop': ('minimax', 'DYNAMIC GAMES', 'MINIMAX · CONTROL'),
    'aapm2019': ('beam', 'LEARNED IMRT PLANS', 'LEARN · ORIENT'),
    'icra18': ('minimax', 'ADVERSARIAL CONTROL', 'PLAN · RESPOND'),
    'iros17_abstract': ('control', 'ROBUST POLICY SEARCH', 'GUIDE · OPTIMIZE'),
    'aapm15': ('patient', 'IMAGE-GUIDED ROBOT', 'SENSE · POSITION'),
}

CSS = '''
    .flow { stroke-dasharray: 4 7; animation: flow 3s linear infinite; }
    .pulse { animation: pulse 4s ease-in-out infinite; }
    .late { animation-delay: -2s; }
    .ring { transform-origin: 100px 120px; animation: ring 6s ease-in-out infinite; }
    .turn { transform-origin: 100px 120px; animation: turn 16s linear infinite; }
    .bend { transform-origin: 100px 183px; animation: bend 7s ease-in-out infinite; }
    .correct { transform-origin: 100px 112px; animation: correct 6s ease-in-out infinite; }
    .travel { animation: travel 8s linear infinite; }
    .interpolate { animation: interpolate 7s ease-in-out infinite; }
    @keyframes flow { to { stroke-dashoffset: -44; } }
    @keyframes pulse { 0%, 100% { opacity: .35; } 50% { opacity: 1; } }
    @keyframes ring { 0%, 100% { transform: scale(.85); } 50% { transform: scale(1.08); } }
    @keyframes turn { to { transform: rotate(360deg); } }
    @keyframes bend { 0%, 100% { transform: rotate(-9deg); } 50% { transform: rotate(9deg); } }
    @keyframes correct { 0%, 100% { transform: translate(5px, -3px) rotate(4deg); } 40%, 70% { transform: none; } }
    @keyframes travel {
      0%, 100% { transform: translate(38px, 176px); }
      25% { transform: translate(38px, 74px); }
      50% { transform: translate(108px, 74px); }
      75% { transform: translate(162px, 176px); }
    }
    @keyframes interpolate {
      0%, 100% { transform: translate(50px, 165px); }
      33% { transform: translate(85px, 127px); }
      66% { transform: translate(140px, 90px); }
    }
    @media (prefers-reduced-motion: reduce) {
      * { animation: none !important; }
      .travel { transform: translate(38px, 125px); }
      .interpolate { transform: translate(85px, 127px); }
    }
'''


def path(d, color='#78b9ff', cls='', width=2, extra=''):
    return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{width}" class="{cls}" stroke-linecap="round" stroke-linejoin="round" {extra}/>'


def circle(x, y, r, color='#62dfc3', cls='', extra=''):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{color}" class="{cls}" {extra}/>'


def box(x, y, w, h, color='#78b9ff'):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="7" fill="#1c3046" stroke="{color}"/>'


def network(y=120):
    nodes = [(65,y-18), (65,y+18), (100,y-25), (100,y), (100,y+25), (135,y)]
    edges = ''.join(path(f'M{x} {a}L{z} {b}', '#48627c', width=1) for x,a in nodes[:2] for z,b in nodes[2:5])
    edges += ''.join(path(f'M{x} {a}L135 {y}', '#48627c', width=1) for x,a in nodes[2:5])
    return edges + ''.join(circle(x,a,4,'#b0a4ee','pulse' if i%2 else 'pulse late') for i,(x,a) in enumerate(nodes))


def diagram(kind):
    if kind == 'reach':
        grid = ''.join(path(f'M{x} 52V190M30 {x+25}H170','#26364a',width=.7) for x in range(30,171,20))
        contours = ''.join(f'<ellipse cx="100" cy="120" rx="{r}" ry="{r*.72}" fill="none" stroke="{c}" stroke-width="1.7"/>' for r,c in [(65,'#48627c'),(48,'#78b9ff'),(30,'#62dfc3')])
        dots = ''.join(circle(x,y,2,'#f7c977','pulse' if i%2 else 'pulse late') for i,(x,y) in enumerate([(62,104),(82,136),(116,101),(138,128),(103,158),(92,80)]))
        return grid + '<g class="ring">'+contours+'</g>' + dots + circle(100,120,4)
    if kind == 'diffusion':
        noisy = path('M32 78l12-18 8 27 9-21 12 13 8-16 10 27 11-28 10 19 10-13 8 20 12-25 9 13 13-6','#b0a4ee','pulse',2)
        smooth = path('M32 174C58 174 61 140 84 145S122 181 168 150','#62dfc3',width=3)
        return noisy + path('M100 94v38m-5-6 5 6 5-6','#8aa4bc','flow') + smooth + path('M32 174C58 174 61 140 84 145S122 181 168 150','#f7c977','flow',3)
    if kind in ('game','feedback'):
        coords = [(100,65),(153,153),(47,153)]
        s = path('M100 65L153 153H47Z','#48627c',width=2)
        s += path('M100 65L153 153H47Z','#78b9ff','flow')
        for (x,y),c in zip(coords,['#b0a4ee','#62dfc3','#78b9ff']):
            s += circle(x,y,17,'#1c3046',extra=f'stroke="{c}"') + circle(x,y,5,c,'pulse')
        s += circle(100,122,17,'#173d3a',extra='stroke="#62dfc3"')
        return s + (path('M92 122h16m-8-8v16','#62dfc3',width=3) if kind=='game' else path('M92 122l6 6 11-12','#62dfc3',width=2))
    if kind == 'map':
        s = box(63,102,35,42,'#48627c') + box(130,63,30,47,'#48627c')
        s += path('M38 176V74H108L162 176Z','#48627c') + path('M38 176V74H108L162 176Z','#62dfc3','flow')
        return s + '<g class="travel">'+circle(0,0,14,'#62dfc3',extra='fill-opacity=".12" stroke="#62dfc3" stroke-opacity=".5"')+circle(0,0,5)+'</g>'
    if kind == 'soft':
        curve = 'M100 183C69 153 130 129 109 105S79 76 106 56'
        s = path('M70 187h60','#8aa4bc',width=5) + path(curve,'#39516a',width=15)
        s += '<g class="bend">' + path(curve,'#62dfc3',width=13) + path(curve,'#101e30','flow',3)
        s += circle(106,56,7,'#f7c977') + '</g>'
        return s + path('M145 80v75m-4-6 4 6 4-6','#78b9ff',width=1.5)
    if kind == 'barrier':
        s = path('M40 180C27 116 43 62 105 63S178 140 153 181Z','#62dfc3',width=2,extra='style="fill:#62dfc3;fill-opacity:.05"')
        s += network() + '<g class="turn">'+circle(100,49,5,'#f7c977')+'</g>'
        return s + path('M89 172l7 7 15-17','#62dfc3','pulse',3)
    if kind == 'latent':
        s = ''.join(path(f'M{x} 180L{x+40} 65','#39516a',width=1) for x in (35,65,95,125))
        s += ''.join(path(f'M{35+i*10} {180-i*29}H{125+i*10}','#39516a',width=1) for i in range(5))
        s += path('M50 165L85 127 140 90','#62dfc3',width=2.5)
        s += ''.join(circle(x,y,6,'#101e30',extra='stroke="#78b9ff" stroke-width="2"') for x,y in [(50,165),(85,127),(140,90)])
        return s + '<g class="interpolate">'+circle(0,0,4,'#f7c977')+'</g>'
    if kind == 'control':
        s = box(35,77,53,42) + box(112,77,53,42,'#62dfc3')
        s += path('M88 98h24m26 21v49H61v-49','#48627c') + path('M88 98h24m26 21v49H61v-49','#62dfc3','flow')
        s += path('M43 101l7-10 8 16 8-16 8 10','#78b9ff')
        s += path('M122 99h10l6-10 8 18 8-8','#62dfc3')
        return s + path('M94 58l6 17 6-17','#f7c977','pulse')
    if kind == 'beam':
        s = circle(100,120,65,'none',extra='stroke="#39516a" stroke-width="2" stroke-dasharray="3 5"')
        s += '<ellipse cx="100" cy="120" rx="33" ry="43" fill="#1c3046" stroke="#48627c"/>'
        s += '<g class="turn">' + path('M100 55v65l56 32M100 120l-56 32','#62dfc3',width=2)
        s += circle(100,55,7,'#78b9ff') + circle(156,152,5,'#b0a4ee') + circle(44,152,5,'#b0a4ee') + '</g>'
        return s + circle(100,120,11,'#f7c977','pulse') + circle(100,120,4,'#101e30')
    if kind == 'patient':
        s = '<path d="M42 169V87a58 47 0 0 1 116 0v82" fill="none" stroke="#39516a" stroke-width="12"/>'
        s += '<g class="correct"><ellipse cx="100" cy="110" rx="24" ry="30" fill="#1c3046" stroke="#78b9ff" stroke-width="2"/>'
        s += path('M93 115q7 6 14 0','#78b9ff',width=1.5) + circle(92,104,2,'#78b9ff') + circle(108,104,2,'#78b9ff') + '</g>'
        s += path('M60 151H140M48 180H152','#8aa4bc',width=4)
        s += path('M70 176v-20m30 20v-20m30 20v-20','#62dfc3','pulse',8)
        return s + path('M100 68v12m0 61v11m-38-42h12m52 0h12','#f7c977',width=1.5)
    if kind == 'minimax':
        s = ''.join(f'<ellipse cx="100" cy="121" rx="{r}" ry="{r*.6}" fill="none" stroke="#39516a"/>' for r in (24,45,67))
        s += path('M35 79Q100 40 165 79M35 162Q100 199 165 162','#48627c')
        s += path('M35 79Q100 40 165 79','#78b9ff','flow') + path('M165 162Q100 199 35 162','#f7c977','flow')
        return s + circle(65,92,7,'#78b9ff','pulse') + circle(135,150,7,'#f7c977','pulse late') + circle(100,121,5)
    if kind == 'identify':
        s = path('M35 65q10-20 20 0t20 0t20 0t20 0t20 0t20 0','#b0a4ee','flow')
        s += network(125) + path('M100 80v14m0 62v13','#8aa4bc','flow')
        return s + path('M35 185q10-20 20 0t20 0t20 0t20 0t20 0t20 0','#62dfc3',width=2.5)
    if kind == 'tree':
        s = path('M100 60L65 105 40 155m25-50 25 50m10-95 35 45-25 50m25-50 25 50','#48627c')
        s += path('M100 60L135 105 110 155','#62dfc3','flow',3)
        for x,y in [(100,60),(65,105),(135,105),(40,155),(90,155),(110,155),(160,155)]:
            s += circle(x,y,6,'#78b9ff' if x!=110 else '#f7c977','pulse' if x==110 else '')
        return s + path('M45 185H155','#39516a')
    raise ValueError(kind)


def main():
    papers = yaml.safe_load((ROOT / '_data/papers.yaml').read_text())
    titles = {Path(p['thumbnail']).stem: p['title'] for group in papers['publications']
              for p in group['paperitems'] if p.get('thumbnail')}
    for stem, (kind, heading, footer) in DESIGNS.items():
        title = titles[stem]
        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="200" height="240" viewBox="0 0 200 240" role="img" aria-labelledby="title desc">
  <title id="title">{escape(title)}</title>
  <desc id="desc">Animated conceptual illustration: {escape(heading.lower())}. Schematic only; not experimental data.</desc>
  <style>{CSS}  </style>
  <path fill="#101e30" d="M0 0h200v240H0z"/>
  <g font-family="Arial, sans-serif" text-anchor="middle">
    <text x="100" y="27" fill="#c1d3e5" font-size="10" letter-spacing="1">{escape(heading)}</text>
    <text x="100" y="222" fill="#8aa4bc" font-size="9" letter-spacing=".8">{escape(footer)}</text>
  </g>
  {diagram(kind)}
</svg>
'''
        (OUT / f'{stem}.svg').write_text(svg)
    print(f'Generated {len(DESIGNS)} publication thumbnails.')


if __name__ == '__main__':
    main()
