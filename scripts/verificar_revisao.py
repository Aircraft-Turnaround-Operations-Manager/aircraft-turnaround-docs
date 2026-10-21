"""Valida IDs finais, referências, contagens e geração da matriz após T12."""
from pathlib import Path
import re,json,runpy,contextlib,io
import xml.etree.ElementTree as ET,html
from unittest.mock import patch
ROOT=Path(__file__).resolve().parent.parent;E=ROOT/'especificacao'
patterns={'RF':('06-requisitos-funcionais',r'^\| (RF-\d+) \|'),'US':('07-estorias-de-usuario',r'^## (US\d+)\b'),'RNF':('08-requisitos-nao-funcionais',r'^\| (RNF-\d+) \|'),'UC':('10-especificacoes-de-caso-de-uso',r'^## (UC\d+)\b')}
expected={'RF':44,'US':44,'RNF':24,'UC':37};defs={};areas={};errors=[]
for kind,(folder,pattern) in patterns.items():
 allids=[];areas[kind]={}
 for area in 'abcd':
  s=(E/folder/f'area-{area}.md').read_text(encoding='utf-8');ids=re.findall(pattern,s,re.M);areas[kind][area.upper()]=len(ids);allids+=ids
  if kind=='US':
   for part in re.split(r'^## US\d+.*$',s,flags=re.M)[1:]:
    criteria=re.findall(r'^\| \d+ \| (.+)$',part,re.M)
    if len(criteria)<2 or any(not all(x in t for x in ['DADO QUE','QUANDO','ENTÃO']) for t in criteria):errors.append('Estória sem dois critérios completos')
 defs[kind]=set(allids)
 if len(allids)!=expected[kind] or len(set(allids))!=len(allids):errors.append(f'{kind}: contagem/duplicação')
 seq=[int(re.search(r'\d+',x)[0]) for x in allids]
 if seq!=list(range(1,expected[kind]+1)):errors.append(f'{kind}: sequência')
for p in list(E.rglob('*.md'))+list(E.rglob('*.puml'))+list(E.rglob('*.drawio')):
 s=p.read_text(encoding='utf-8')
 if re.search(r'\b(?:RNF|RF|UC|US)-[A-D]\d+',s):errors.append(f'ID provisório: {p}')
 for ref in re.findall(r'\b(?:RNF-\d+|RF-\d+|UC\d+|US\d+)\b',s):
  kind=re.match('[A-Z]+',ref)[0]
  if ref not in defs[kind]:errors.append(f'{p}: {ref} desconhecido')
 for target in re.findall(r'\]\(([^)]+)\)',s):
  if ':' not in target and not (p.parent/target.split('#')[0]).exists():errors.append(f'Link ausente: {p}/{target}')
text='\n'.join((E/'07-estorias-de-usuario'/f'area-{a}.md').read_text(encoding='utf-8') for a in 'abcd')
pairs=re.findall(r'^## US(\d+)\s*[–-]\s*REQUISITO RF-(\d+)',text,re.M)
if len(pairs)!=44 or any(int(a)!=int(b) for a,b in pairs):errors.append('RF/US não bijetivos')
ucnames={m[1]:m[2] for a in 'abcd' for m in re.finditer(r'^## (UC\d+)\s*[–-]\s*(.*)',(E/'10-especificacoes-de-caso-de-uso'/f'area-{a}.md').read_text(encoding='utf-8'),re.M)}
# item 9: o diagrama de casos de uso é o .drawio (nomes, setas e ligações de cada linha)
cells=list(ET.parse(E/'diagramas/09-casos-de-uso.drawio').getroot().iter('mxCell'));norm=lambda x:re.sub(r'\s+',' ',x.replace('“','"').replace('”','"')).strip()
ucd={c.get('id').upper():re.split(r'<br\s*/?>',html.unescape(c.get('value') or '')) for c in cells if re.fullmatch(r'uc\d+',c.get('id') or '')}
for cid,parts in ucd.items():
 if norm(parts[0])!=cid or norm(' '.join(parts[1:]))!=norm(ucnames.get(cid,'')):errors.append(f'Nome diagrama: {cid}')
if len(ucd)!=37:errors.append('Contagem diagrama')
edges=[c for c in cells if c.get('edge')=='1']
if any(not c.get('source') or not c.get('target') for c in edges):errors.append('Diagrama: linha sem ligação')
if sum(c.get('value')=='«include»' for c in edges)!=10 or sum(c.get('value')=='«extend»' for c in edges)!=8:errors.append('Diagrama: include/extend')
capture={}
def save(p,s,*a,**k):capture[str(p)]=s;return len(s)
log=io.StringIO()
with patch.object(Path,'write_text',save),contextlib.redirect_stdout(log):runpy.run_path(str(ROOT/'scripts/gerar_matriz_rastreabilidade.py'))
matrix=E/'apendice-a-matriz-de-rastreabilidade.md'
if capture[str(matrix)].replace('\r\n','\n')!=matrix.read_text(encoding='utf-8').replace('\r\n','\n'):errors.append('Matriz desatualizada')
if '0 lacunas' not in log.getvalue():errors.append('Lacunas matriz')
result={'contagens':expected,'por_area':areas,'matriz':log.getvalue().strip(),'erros':errors}
print(json.dumps(result,ensure_ascii=False,indent=2));raise SystemExit(bool(errors))
