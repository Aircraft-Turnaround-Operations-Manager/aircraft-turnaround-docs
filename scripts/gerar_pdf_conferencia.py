"""Gera PDF de conferência da revisão; a entrega final é a tarefa #14.
Use o Python do runtime Codex com reportlab instalado.
"""
from pathlib import Path
import re,html
from reportlab.platypus import *
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
ROOT=Path(__file__).resolve().parent.parent
OUT=ROOT/'output/pdf/ra1-conferencia.pdf';OUT.parent.mkdir(parents=True,exist_ok=True)
styles=getSampleStyleSheet()
for s in styles.byName.values():s.textColor=colors.black
styles.add(ParagraphStyle('Cell',fontName='Helvetica',fontSize=9,leading=12,spaceAfter=2,wordWrap='CJK'))
styles['Normal'].fontSize=10;styles['Normal'].leading=14
styles['Heading1'].fontSize=14;styles['Heading1'].leading=18
styles['Heading2'].fontSize=12;styles['Heading2'].leading=16
class SmartBreak(ActionFlowable):
 def apply(self,doc):
  pending=getattr(doc,"_nextPageTemplateIndex",None)
  changing=pending is not None and doc.pageTemplates[pending].id!=doc.pageTemplate.id
  if not doc.frame._atTop or changing:doc.handle_pageBreak()

class Doc(BaseDocTemplate):
 def afterFlowable(self,f):
  if isinstance(f,Paragraph) and f.style.name=='Heading1':
   text=f.getPlainText();key='h'+str(self.seq.nextf('heading'));self.canv.bookmarkPage(key);self.notify('TOCEntry',(0,text,self.page,key))
doc=Doc(str(OUT),pagesize=A4,leftMargin=48,rightMargin=48,topMargin=48,bottomMargin=48,title='Aircraft Turnaround Orchestration System — Especificação do Projeto',author='Eduardo Fabri; João Pedro Cardoso de Liz; Rodrigo Alves; João Vitor Correa Oliveira')
def footer(c,d):
 c.setFont('Helvetica',9);c.drawRightString(d.pagesize[0]-48,25,str(d.page))
doc.addPageTemplates(PageTemplate(id='portrait',frames=[Frame(48,48,A4[0]-96,A4[1]-96,id='normal')],onPage=footer,pagesize=A4))
story=[];figserial=0

def fmt(s):
 s=re.sub(r'\[([^]]+)\]\([^)]+\)',r'\1',s);s=s.replace('`','');s=html.escape(s)
 s=re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',s);s=re.sub(r'\*([^*]+)\*',r'<i>\1</i>',s);s=s.replace('&lt;br&gt;','<br/>').replace('&lt;br/&gt;','<br/>');return s

def cell(s,p,width):
 parts=[];last=0
 for m in re.finditer(r'!\[([^]]*)\]\(([^)]+)\)',s):
  if s[last:m.start()].strip():parts.append(Paragraph(fmt(s[last:m.start()]),styles['Cell']))
  imagepath=p.parent/m[2];im=Image(str(imagepath));factor=min(width/im.imageWidth,230/im.imageHeight);im.drawWidth=im.imageWidth*factor;im.drawHeight=im.imageHeight*factor;parts.append(im);last=m.end()
 if s[last:].strip():parts.append(Paragraph(fmt(s[last:]),styles['Cell']))
 return parts or [Paragraph('',styles['Cell'])]

def figure(path,label):
 global figserial
 figserial+=1;im=Image(str(path));w=im.imageWidth*.75;h=im.imageHeight*.75
 # Folha de diagrama mantém fonte nativa legível, sem comprimir um mapa grande em A4.
 scale=min(1,2600/max(w,h));w*=scale;h*=scale;size=(max(A4[0],w+108),max(A4[1],h+180));name='figure'+str(figserial)
 doc.addPageTemplates(PageTemplate(id=name,frames=[Frame(48,48,size[0]-96,size[1]-96,id=name)],onPage=footer,pagesize=size))
 story.extend([NextPageTemplate(name),SmartBreak(),Paragraph(fmt(label),styles['Heading2'])]);im.drawWidth=w;im.drawHeight=h;story.extend([im,NextPageTemplate('portrait'),SmartBreak()])

def md(p,case=False,skiptitle=False,text_override=None):
 text=text_override if text_override is not None else p.read_text(encoding='utf-8');text=re.sub(r'<!--.*?-->','',text,flags=re.S);text=re.sub(r'^---\n.*?\n---\n','',text,flags=re.S)
 if case:text=text[text.index('\n## UC')+1:]
 lines=text.splitlines();i=0
 while i<len(lines):
  line=lines[i].strip();i+=1
  if not line or line=='---':continue
  if line.startswith('|'):
   rows=[line]
   while i<len(lines) and lines[i].strip().startswith('|'):rows.append(lines[i].strip());i+=1
   rows=[x for x in rows if not re.fullmatch(r'\|[\s|:\-]+',x)]
   data=[[x.strip() for x in row.strip('|').split('|')] for row in rows];cols=len(data[0]);width=A4[0]-108
   ratios=([.08,.53,.17,.12,.10] if cols==5 else [.08,.62,.30] if cols==3 else [.08,.25,.35,.32] if cols==4 else [.5,.5] if cols==2 else [1/cols]*cols)
   if cols==2 and data[0][0]=='Campo':ratios=[.24,.76]
   if cols==3 and data[0][0]=='Motor de Eventos':ratios=[.34,.33,.33]
   widths=[width*x for x in ratios];tab=LongTable([[cell(x,p,widths[j]-12) for j,x in enumerate(row)] for row in data],colWidths=widths,repeatRows=1,splitInRow=1 if cols==2 and data[0][0]=='Campo' else 0,hAlign='LEFT')
   tab.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('GRID',(0,0),(-1,-1),.3,colors.black),('BACKGROUND',(0,0),(-1,0),colors.HexColor('#eeeeee')),('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5)]));story.append(tab);continue
  if line.startswith('#'):
   level=len(line)-len(line.lstrip('#'));title=line[level:].strip()
   if skiptitle and level==1:continue
   if case and level==2:story.append(SmartBreak())
   story.append(Paragraph(fmt(title),styles['Heading1' if level==1 else 'Heading2' if level==2 else 'Heading3']));continue
  if line.startswith('!['):
   m=re.match(r'!\[([^]]*)\]\(([^)]+)\)',line)
   if m:figure(p.parent/m[2],m[1]);continue
  story.append(Paragraph(fmt(line.lstrip('- ').lstrip('> ')),styles['Normal']));story.append(Spacer(1,5))

story.extend([Spacer(1,75),Paragraph('EDUARDO FABRI<br/>JOÃO PEDRO CARDOSO DE LIZ<br/>RODRIGO ALVES<br/>JOÃO VITOR CORREA OLIVEIRA',styles['Normal']),Spacer(1,150),Paragraph('ESPECIFICAÇÃO DO PROJETO',styles['Title']),Paragraph('Aircraft Turnaround Orchestration System',styles['Title']),Spacer(1,100),Paragraph('2026',styles['Normal']),SmartBreak()])
story.extend([Paragraph('Declaração de uso de inteligência artificial',styles['Heading2']),Paragraph('Durante a preparação desta especificação de projeto, os autores usaram Claude Code 2.1.296 e Codex (GPT-6) para pesquisar referências, estruturar requisitos e estórias, preparar protótipos e diagramas, consolidar a documentação e verificar sua consistência. Após usar essas ferramentas, os autores revisaram e editaram o conteúdo conforme necessário e assumem total responsabilidade pelo conteúdo.',styles['Normal']),SmartBreak(),Paragraph('SUMÁRIO',styles['Title'])])
toc=TableOfContents();toc.levelStyles=[ParagraphStyle('toc',fontName='Helvetica',fontSize=10,leading=17)];story.extend([toc,SmartBreak()])
for n in range(1,12):
 matches=sorted((ROOT/'especificacao').glob(f'{n:02d}-*'));p=next(x for x in matches if x.is_dir() or x.suffix=='.md')
 if p.is_dir():
  md(p/'00-item.md')
  if n in (6,8):
   texts=[(p/f'area-{a}.md').read_text(encoding='utf-8') for a in 'abcd']
   header=texts[0].splitlines()[:2]
   rows=[ln for t in texts for ln in t.splitlines() if re.match(r'^\| (?:RF|RNF)-\d+ \|',ln)]
   notes=list(dict.fromkeys(ln for t in texts for ln in t.splitlines() if ln and not ln.startswith('|')))
   md(p/'area-a.md',text_override='\n'.join(header+rows+['']+notes))
  else:
   for area in 'abcd':md(p/f'area-{area}.md',case=n==10)
 else:md(p)
 story.append(SmartBreak())
md(ROOT/'especificacao/apendice-a-matriz-de-rastreabilidade.md')
story.append(SmartBreak());md(ROOT/'pesquisa/fontes.md')
doc.multiBuild(story)
print(OUT)
