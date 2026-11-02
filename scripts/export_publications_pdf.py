"""Export /pubs as a chronological, linked research timeline."""
from pathlib import Path
from html import escape
from urllib.parse import urljoin
import re
import calendar
import yaml
from bs4 import BeautifulSoup
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://scriptedonachip.com/'
OUTPUT = ROOT / 'downloads' / 'Lekan_Molu_Publications.pdf'
NAVY = colors.HexColor('#15354b')
TEAL = colors.HexColor('#087f8c')


def plain(value):
    return re.sub(r'\s+', ' ', BeautifulSoup(str(value or ''), 'html.parser').get_text()).strip()


def date_key(paper):
    value = str(paper.get('year', ''))
    year = re.search(r'\b(?:19|20)\d{2}\b', value)
    month = next((i for i, name in enumerate(calendar.month_name) if name and name.lower() in value.lower()), 0)
    return (int(year.group()) if year else 0, month)


def main():
    for suffix, filename in [('', 'DejaVuSans'), ('-Bold', 'DejaVuSans-Bold')]:
        pdfmetrics.registerFont(TTFont('DejaVu' + suffix, f'/usr/share/fonts/truetype/dejavu/{filename}.ttf'))
    pdfmetrics.registerFontFamily('DejaVu', normal='DejaVu', bold='DejaVu-Bold')
    styles = {
        'title': ParagraphStyle('title', fontName='DejaVu-Bold', fontSize=28, leading=34, textColor=NAVY, spaceAfter=16),
        'year': ParagraphStyle('year', fontName='DejaVu-Bold', fontSize=19, leading=25, textColor=TEAL, spaceBefore=15, spaceAfter=9, keepWithNext=True),
        'paper': ParagraphStyle('paper', fontName='DejaVu-Bold', fontSize=9.7, leading=13.4, textColor=NAVY, spaceAfter=5),
        'body': ParagraphStyle('body', fontName='DejaVu', fontSize=8.2, leading=11.8, textColor=colors.HexColor('#334857'), spaceAfter=4),
        'meta': ParagraphStyle('meta', fontName='DejaVu', fontSize=7.4, leading=10.5, textColor=colors.HexColor('#607582'), spaceAfter=2),
        'date': ParagraphStyle('date', fontName='DejaVu-Bold', fontSize=8, leading=12, textColor=TEAL),
    }
    papers = [p for g in yaml.safe_load((ROOT / '_data/papers.yaml').read_text())['publications'] for p in g['paperitems']
              if p.get('paper_status') in ('Accepted', 'Submitted', 'Technical Report', 'Accepted Abstract', 'Oral')]
    papers.sort(key=lambda p: (date_key(p)[0],
                              not (date_key(p)[0] == 2026 and p['title'] == 'A Generalized Nash Equilibrium-Seeking Scheme for Trauma Resuscitation'),
                              date_key(p)[1]), reverse=True)
    story = [Paragraph('Lekan Molu', styles['title'])]
    current_year = None
    for p in papers:
        year, month = date_key(p)
        if year != current_year:
            story.append(Paragraph(str(year), styles['year']))
            current_year = year
        title = escape(plain(p['title']))
        is_thesis = 'PhD Thesis' in str(p.get('venue', ''))
        location = None if is_thesis else p.get('location')
        if location and location != '#':
            title = f'<link href="{escape(urljoin(BASE, location), quote=True)}" color="#15354b">{title}</link>'
        block = [Paragraph(title, styles['paper'])]
        if p.get('authors'):
            authors = p['authors'] if isinstance(p['authors'], list) else [p['authors']]
            author_text = escape(plain(' '.join(authors))).replace('Lekan Molu', '<b>Lekan Molu</b>')
            block.append(Paragraph(author_text, styles['body']))
        block.append(Paragraph(escape(plain(p.get('venue'))), styles['body']))
        status = {'Accepted': 'Accepted / Published', 'Submitted': 'Under review', 'Accepted Abstract': 'Abstract', 'Oral': 'Oral presentation'}.get(p['paper_status'], p['paper_status'])
        meta = '' if p['title'].startswith('Beyond Sampling: Kolmogorov') else escape(status)
        # Keep the thesis as a citation without any clickable links.
        links = []
        if not is_thesis:
            for label, href in [('Paper', location), ('DOI', p.get('doi')), ('Video', p.get('video'))]:
                if href and href != '#':
                    links.append(f'<link href="{escape(urljoin(BASE, str(href)), quote=True)}" color="#087f8c">{label}</link>')
        if links:
            meta += '  ·  ' + ' / '.join(links)
        if meta:
            block.append(Paragraph(meta, styles['meta']))
        date_label = calendar.month_abbr[month].upper() if month else str(year)
        row = Table([[Paragraph(date_label, styles['date']), block]], colWidths=[47, A4[0] - 139])
        row.setStyle(TableStyle([
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('LINEBEFORE', (1, 0), (1, 0), 1.7, colors.HexColor('#91cbd0')),
            ('BACKGROUND', (1, 0), (1, 0), colors.HexColor('#f2f7f9')),
            ('LEFTPADDING', (0, 0), (0, 0), 0),
            ('LEFTPADDING', (1, 0), (1, 0), 13),
            ('RIGHTPADDING', (1, 0), (1, 0), 12),
            ('TOPPADDING', (0, 0), (-1, -1), 10),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
        ]))
        story.extend([row, Spacer(1, 8)])

    def footer(canvas, doc):
        canvas.setFillColor(TEAL)
        canvas.rect(0, A4[1] - 7, A4[0], 7, fill=1, stroke=0)
        canvas.setStrokeColor(colors.HexColor('#d8e3e8'))
        canvas.line(46, 39, A4[0] - 46, 39)
        canvas.setFont('DejaVu', 7)
        canvas.setFillColor(colors.HexColor('#607582'))
        canvas.drawString(46, 25, 'Lekan Molu')
        canvas.drawRightString(A4[0] - 46, 25, f'{doc.page:02d}')

    SimpleDocTemplate(str(OUTPUT), pagesize=A4, rightMargin=46, leftMargin=46, topMargin=35, bottomMargin=53,
                      title='Lekan Molu — Research Timeline', author='Lekan Molu').build(story, onFirstPage=footer, onLaterPages=footer)
    print(f'Exported {len(papers)} entries to {OUTPUT}')


if __name__ == '__main__':
    main()
