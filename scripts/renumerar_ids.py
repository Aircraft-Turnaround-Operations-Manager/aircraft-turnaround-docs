"""Aplica a renumeração única da ADR-0011 aos textos/fontes da especificação.
Uso: python scripts/renumerar_ids.py. Falha se a base não estiver toda provisória.
Preserva históricos, pesquisa, ADRs, imagens e nomes de arquivos.
"""
import re
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
ESP=ROOT/'especificacao'
paths={'RF':'06-requisitos-funcionais','US':'07-estorias-de-usuario','RNF':'08-requisitos-nao-funcionais','UC':'10-especificacoes-de-caso-de-uso'}
mapping={};rows=[]
for prefix,folder in paths.items():
 serial=0
 for area in 'abcd':
  text=(ESP/folder/f'area-{area}.md').read_text(encoding='utf-8')
  pattern=rf'^\| ({prefix}-[A-D]\d+) \|' if prefix in ('RF','RNF') else rf'^## ({prefix}-[A-D]\d+)\b'
  ids=re.findall(pattern,text,re.M)
  if not ids: raise SystemExit(f'Base não provisória: {prefix}/{area}; nenhuma alteração feita.')
  for old in ids:
   serial+=1
   new=f'{prefix}-{serial}' if prefix in ('RF','RNF') else f'{prefix}{serial:02d}' if prefix=='UC' else f'US{serial:03d}'
   mapping[old]=new;rows.append((prefix,area.upper(),old,new))
pattern=re.compile(r'\b(?:RNF|RF|US|UC)-[A-D]\d+\b')
files=list(ESP.rglob('*.md'))+list(ESP.rglob('*.puml'))+list(ESP.rglob('*.bpmn'))
# Validação antes da primeira escrita.
for p in files:
 unknown=set(pattern.findall(p.read_text(encoding='utf-8')))-mapping.keys()
 if unknown:raise SystemExit(f'ID sem definição em {p}: {unknown}')
for p in files:
 old=p.read_text(encoding='utf-8');new=pattern.sub(lambda m:mapping[m[0]],old)
 if new!=old:p.write_text(new,encoding='utf-8')
lines=['# Renumeração definitiva — ADR-0011','', 'Base: main `6d68a03`, após integração das quatro áreas e diagramas. Ordem A, B, C, D, preservando a ordem de definição em cada arquivo. Históricos de revisão, pesquisa e ADRs conservam os IDs anteriores; a tabela permite consultá-los.','', '| Tipo | Área | Provisório | Final |','|---|---|---|---|']
lines += [f'| {kind} | {a} | {old} | {new} |' for kind,a,old,new in rows]
(ROOT/'entregas/ra1-renumeracao.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
print({kind:sum(1 for x in rows if x[0]==kind) for kind in paths})
