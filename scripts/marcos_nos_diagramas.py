"""Apoio à checagem cruzada dos diagramas (AGENTS.md, regra 6): para cada marco do atendimento em solo, lista os RFs que o
definem (com o ator) e cada passo de diagrama (.bpmn, .drawio e os diagramas de sequência 14-sequencia-*.puml) que o cita,
com a partição ou lane em que está. Inclui o TOBT, que não é marco real, mas é sigla dos passos (Y.8). No diagrama de
sequência, a partição é o ator que envia a mensagem ou, nos demais passos, o último ator que enviou uma (ver passos_puml).

Situação de cada passo: vazio (a partição é ator de um RF que grava, corrige ou usa o marco), "cita" (a partição é ator só
de um RF que consulta, verifica ou alerta sobre o marco, e o passo não o grava), "exibe" (passo de diagrama de sequência que
só mostra, devolve, lê ou menciona o dado, sem gravar), "dispara" (o Operador faz o registro de que o Motor de Eventos deriva o marco, pelo RF), "grava" (o
Motor de Eventos grava o que um ator registrou) ou "conferir" (ler o RF e o UC).
Uso: python scripts/marcos_nos_diagramas.py
"""
import html, re, xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent; E = ROOT / 'especificacao'
MARCOS = ['AIBT', 'ACGT', 'ASBT', 'AEGT', 'ARDT', 'AOBT', 'TOBT']  # TOBT: horário-alvo, não marco real, mas sigla dos passos (Y.8)
M = '{http://www.omg.org/spec/BPMN/20100524/MODEL}'
SO_CITA = r'(Consultar|Acompanhar|Exibir|Verificar|Recalcular|Emitir)\b'  # título do RF que só lê o marco ou alerta sobre ele: seu ator não conta como ator do marco


def rfs():
    out = []
    for f in sorted((E / '06-requisitos-funcionais').glob('area-*.md')):
        for l in f.read_text(encoding='utf-8').splitlines():
            c = [x.strip() for x in l.strip().strip('|').split('|')]
            if len(c) >= 6 and re.fullmatch(r'RF-\d+', c[0]): out.append((c[0], c[2], c[3], c[1]))  # # | TÍTULO | REQUISITO | ATOR | ...
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


DECL = re.compile(r'(actor|participant|boundary|control|entity|database|queue|collections)\s+"([^"]+)"\s+as\s+(\w+)')
MSG = re.compile(r'(\w+)\s*<?(-+)>{1,2}\s*(\w+)\s*:\s*(.+)')
NOTA = re.compile(r'(?:ref over|note\s+(?:over|(?:left|right|top|bottom)\s+of))\s+([\w\s,]+?)\s*(?::\s*(.*))?$')
BLOCO = re.compile(r'(==|alt\b|else\b|critical\b|group\b|opt\b|loop\b|break\b)\s*')
txt = lambda s: s.replace(r'\n', ' ')
# Registro original do marco (tabela marco) e do TOBT (turnaround_referencia); escrever em outra tabela é cópia (item 12)
ORIGINAL = r'«create» Marco|\b(INSERT|UPDATE)\s+(marco|turnaround_referencia)\b'


def passos_puml(f):
    """Diagrama de sequência: cada mensagem, nota, ref, condição de bloco ou divisória é um passo, com a partição e quem faz
    o passo, pelo tipo dos participantes declarados. Mensagem enviada por um ator: a partição é esse ator, e o passo é dele
    ('ator'). Resposta (seta tracejada), mensagem enviada por uma tela (boundary) ou nota presa a uma tela: 'exibe' (mostra
    ou devolve o dado, não grava marco). Ref ou nota que cobre um ator: 'ator'. Condição de bloco e divisória: 'rotulo'
    (nomeia o trecho; os passos de dentro é que são conferidos). Chamadas,
    refs e notas só entre participantes internos: 'sistema'. Fora da mensagem do ator, a partição é o último ator que enviou
    uma mensagem (o dono do fluxo em curso; antes da primeira, o primeiro ator declarado). Limite: seta invertida (A <- B) é
    lida como enviada por A; os diagramas não a usam."""
    tipo = {}; atores = {}; nota = None; inicia = None
    for l in f.read_text(encoding='utf-8').splitlines():
        s = l.strip(); inicia = inicia or next(iter(atores.values()), None)
        if nota is not None:
            if re.match(r'end ?(note|ref)', s): yield inicia, ' '.join(nota[1]), nota[0]; nota = None
            else: nota[1].append(s)
            continue
        if not s or s.startswith(("'", '!', '@')): continue
        if d := DECL.match(s):
            tipo[d[3]] = d[1]
            if d[1] == 'actor': atores[d[3]] = txt(d[2])
            continue
        if mm := MSG.match(s):
            de = tipo.get(mm[1]); inicia = atores.get(mm[1], inicia)
            q ='ator' if de == 'actor' else 'exibe' if mm[2] == '--' or de == 'boundary' else 'sistema'
            yield atores.get(mm[1], inicia), txt(mm[4]), q; continue
        if n := NOTA.match(s):
            sobre = [tipo.get(x.strip()) for x in n[1].split(',')]
            q = 'ator' if 'actor' in sobre else 'exibe' if s.startswith('note') and 'boundary' in sobre else 'sistema'
            if n[2] is None: nota = (q, [])
            else: yield inicia, txt(n[2]), q
            continue
        if b := BLOCO.match(s): yield inicia, txt(s[b.end():].rstrip('= ')), 'rotulo'


def escreve(t):
    """O passo diz gravar ou registrar (gravar, «create», INSERT, UPDATE, registrar), sem contar o registro de auditoria,
    que só cita o marco como causa ou gatilho."""
    return bool(re.search(r'\bgrav|«create»|\bINSERT\b|\bUPDATE\b|\bregistra(r|ndo)?\b|atualizar|corrigir', t, re.I)
                and not re.search(r'auditoria|registrar\w*\(objeto', t))


def main():
    R = rfs(); passos = []
    for f in sorted((E / 'diagramas').glob('*.bpmn')): passos += [(f.name, p, t, 'ator') for p, t in passos_bpmn(f)]
    for f in sorted((E / 'diagramas').glob('*.drawio')): passos += [(f.name, p, t, 'ator') for p, t in passos_drawio(f)]
    for f in sorted((E / 'diagramas').glob('14-sequencia-*.puml')): passos += [(f.name, *x) for x in passos_puml(f)]
    for m in MARCOS:
        print(f'\n## {m}\n')
        defs = [(i, t, a) for i, t, a, _ in R if re.search(rf'\b{m}\b', t)]
        atores = {a for i, t, a, tit in R if re.search(rf'\b{m}\b', t) and not re.match(SO_CITA, tit)}
        cita = {}
        for i, t, a, tit in R:
            if re.search(rf'\b{m}\b', t) and re.match(SO_CITA, tit): cita.setdefault(a, []).append(i)
        for i, t, a in defs:
            k = t.find(m); print(f'- {i} ({a}): …{t[max(0, k - 160):k + len(m) + 10]}…')
        print('\n| Diagrama | Partição/lane | Passo | |\n|---|---|---|---|')
        derivado = [i for i, t, a in defs if 'a partir dos registros dos operadores' in t]
        vistos = set()
        for arq, p, t, q in passos:
            if re.search(rf'(?<![a-z]){m}(?![a-z])', t, re.I) and (arq, p, t) not in vistos:  # também tobt_vigente, aibt
                vistos.add((arq, p, t)); print(f'| {arq} | {p or "—"} | {t.replace("|", chr(92) + "|")} | {situacao(p, t, atores, derivado, q, cita)} |')


def situacao(p, t, atores, derivado, quem='ator', cita={}):
    """'' quando a partição é ator de um RF que grava, corrige ou usa o marco (o RF que só o consulta, verifica ou alerta
    sobre ele, SO_CITA, não conta); 'exibe' quando o passo do diagrama de sequência só mostra ou devolve o dado (uma
    resposta que diga gravar o marco também cai aqui, mas a gravação em si é uma chamada e continua conferida), ou quando
    o passo do sistema não escreve (escreve()); 'dispara' quando o Operador faz o registro que o Motor de Eventos transforma
    no marco (RF que define o marco 'a partir dos registros dos operadores'), ou quando o sistema deriva esse marco no
    diagrama de sequência que o Operador inicia; 'grava' quando o Motor de Eventos grava o que um ator registrou ("Gravar…"
    no item 4 e no 11, ou passo do sistema que escreve no diagrama de sequência); 'cita' quando a partição é ator só de um
    RF de SO_CITA e o passo não escreve; 'rótulo' na condição de bloco e na divisória do diagrama de sequência; 'copia'
    quando o sistema escreve fora do registro original do marco (ORIGINAL), como a cópia de um marco já registrado em
    outro serviço; 'conferir' nos demais casos (por exemplo, o sistema cria o marco no fluxo de um ator que não o grava) e
    quando o próprio Operador diz registrar um marco derivado (o teste da palavra vale só para o passo do ator)."""
    if not p or p in atores: return ''
    if quem == 'rotulo': return 'rótulo'
    if quem == 'exibe': return 'exibe'
    if p == 'Operador de Solo/Rampa' and derivado:
        return 'conferir' if quem == 'ator' and re.search(r'\bregistr', t, re.I) else f'dispara ({", ".join(derivado)})'
    if p == 'Motor de Eventos' and (re.match(r'Gravar\b', t) or quem == 'sistema' and escreve(t)): return 'grava'
    if p in cita and not escreve(t): return f'cita ({", ".join(cita[p])})'
    if quem == 'sistema':
        if not escreve(t): return 'exibe'
        if not re.search(ORIGINAL, t): return 'copia'
    return 'conferir'


if __name__ == '__main__':
    main()
