"""Apoio à checagem cruzada dos diagramas (AGENTS.md, regra 6): para cada marco do atendimento em solo, lista os RFs que o
definem (com o ator) e cada passo de diagrama que o cita (com a partição ou lane em que está).

Situação de cada passo: vazio (a partição é ator de um RF do marco), "dispara" (o Operador faz o registro de que o Motor de
Eventos deriva o marco, pelo RF), "grava" (o Motor de Eventos grava o que um ator registrou) ou "conferir" (ler o RF e o UC).
Uso: python scripts/marcos_nos_diagramas.py
"""
import html, re, xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent; E = ROOT / 'especificacao'
MARCOS = ['AIBT', 'ACGT', 'ASBT', 'AEGT', 'ARDT', 'AOBT']
M = '{http://www.omg.org/spec/BPMN/20100524/MODEL}'


def rfs():
    out = []
    for f in sorted((E / '06-requisitos-funcionais').glob('area-*.md')):
        for l in f.read_text(encoding='utf-8').splitlines():
            c = [x.strip() for x in l.strip().strip('|').split('|')]
            if len(c) >= 3 and re.fullmatch(r'RF-\d+', c[0]): out.append((c[0], c[1], c[2]))
    return out


def passos_bpmn(f):
    r = ET.parse(f).getroot(); lane = {}
    for ln in r.iter(M + 'lane'):
        for ref in ln.findall(M + 'flowNodeRef'): lane[ref.text] = ln.get('name')
    def anda(no, ln):
        for e in no:
            l2 = lane.get(e.get('id'), ln)
            if e.get('name') and not e.tag.endswith('sequenceFlow'): yield l2, e.get('name')
            yield from anda(e, l2)
    for p in r.iter(M + 'process'): yield from anda(p, None)


def passos_drawio(f):
    cel = list(ET.parse(f).getroot().iter('mxCell')); part = []
    geo = lambda c: [float(c.find('mxGeometry').get(k, 0)) for k in ('x', 'y', 'width', 'height')]
    for c in cel:
        if (c.get('style') or '').startswith('swimlane'): part.append((geo(c), html.unescape(c.get('value') or '')))
    for c in cel:
        if c.get('vertex') != '1' or (c.get('style') or '').startswith(('swimlane', 'text;')): continue
        x, y, w, h = geo(c); cx, cy = x + w / 2, y + h / 2
        nome = next((n for (px, py, pw, ph), n in part if px <= cx <= px + pw and py <= cy <= py + ph), None)
        txt = re.sub(r'\s+', ' ', html.unescape(re.sub(r'<br\s*/?>', ' ', c.get('value') or ''))).strip()
        if txt: yield nome, txt


def main():
    R = rfs(); passos = []
    for f in sorted((E / 'diagramas').glob('*.bpmn')): passos += [(f.name, p, t) for p, t in passos_bpmn(f)]
    for f in sorted((E / 'diagramas').glob('*.drawio')): passos += [(f.name, p, t) for p, t in passos_drawio(f)]
    for m in MARCOS:
        print(f'\n## {m}\n')
        defs = [(i, t, a) for i, t, a in R if re.search(rf'\b{m}\b', t)]
        atores = {a for _, _, a in defs}
        for i, t, a in defs:
            k = t.find(m); print(f'- {i} ({a}): …{t[max(0, k - 160):k + len(m) + 10]}…')
        print('\n| Diagrama | Partição/lane | Passo | |\n|---|---|---|---|')
        derivado = [i for i, t, a in defs if 'a partir dos registros dos operadores' in t]
        vistos = set()
        for arq, p, t in passos:
            if re.search(rf'\b{m}\b', t) and (arq, p, t) not in vistos:
                vistos.add((arq, p, t)); print(f'| {arq} | {p or "—"} | {t} | {situacao(p, t, atores, derivado)} |')


def situacao(p, t, atores, derivado):
    """'' quando a partição é ator de um RF do marco; 'dispara' quando o Operador faz o registro que o Motor de Eventos
    transforma no marco (RF que define o marco 'a partir dos registros dos operadores'); 'grava' quando o Motor de
    Eventos grava o que um ator registrou; 'conferir' nos demais casos e quando o Operador diz registrar um marco derivado."""
    if not p or p in atores: return ''
    if p == 'Operador de Solo/Rampa' and derivado:
        return 'conferir' if re.search(r'\bregistr', t, re.I) else f'dispara ({", ".join(derivado)})'
    if p == 'Motor de Eventos' and re.match(r'Gravar\b', t): return 'grava'
    return 'conferir'


if __name__ == '__main__':
    main()
