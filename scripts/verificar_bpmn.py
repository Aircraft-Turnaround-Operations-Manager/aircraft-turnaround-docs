"""Confere a geometria das vistas BPMN exportadas por scripts/exportar_bpmn.mjs, medida no próprio bpmn-js.

Aponta: linha que não é ortogonal ou não encosta na origem/destino; linha sobre ou rente a forma que não é dela;
cruzamento de linhas; texto (medido linha a linha, como o bpmn-js desenha) sobre linha, forma, ícone, marcador
de subprocesso, faixa do nome de lane ou outro texto; formas sobrepostas; rótulo longe do seu elemento.

Uso: node scripts/exportar_bpmn.mjs <arquivo.bpmn>  e depois  python scripts/verificar_bpmn.py [início_do_nome_da_vista]
Sai com código 1 se encontrar problema ou cruzamento.
"""
import sys, json, glob, os, itertools, tempfile
so = sys.argv[1] if len(sys.argv) > 1 else ''
GEO = os.path.join(tempfile.gettempdir(), 'bpmn-geo')
FOLGA = 8        # distância mínima entre linha e forma/texto que não são dela
CONT = {'bpmn:Participant', 'bpmn:Lane'}

def inter(a, b, m=0):  # retângulos [x1,y1,x2,y2] se sobrepõem (com margem m)
    return a[0] - m < b[2] and b[0] - m < a[2] and a[1] - m < b[3] and b[1] - m < a[3]
def seg_rect(p, q, r, m=0):  # segmento ortogonal toca retângulo expandido por m
    x1, x2 = sorted((p[0], q[0])); y1, y2 = sorted((p[1], q[1]))
    return x1 < r[2] + m and x2 > r[0] - m and y1 < r[3] + m and y2 > r[1] - m
def cruza(a, b, c, d):  # cruzamento próprio de dois segmentos ortogonais (um H e um V)
    if a[1] == b[1] and c[0] == d[0]: h, v = (a, b), (c, d)
    elif a[0] == b[0] and c[1] == d[1]: h, v = (c, d), (a, b)
    else: return False
    hx1, hx2 = sorted((h[0][0], h[1][0])); vy1, vy2 = sorted((v[0][1], v[1][1]))
    return hx1 < v[0][0] < hx2 and vy1 < h[0][1] < vy2
def segs(e): return list(zip(e['wp'], e['wp'][1:]))
def dentro(r, b, m=1): return r[0] >= b[0] - m and r[1] >= b[1] - m and r[2] <= b[2] + m and r[3] <= b[3] + m

tot = 0
for f in sorted(glob.glob(os.path.join(GEO, so + '*.json'))):
    vista = os.path.basename(f)[:-5]
    G = json.load(open(f, encoding='utf-8')); E = {g['id']: g for g in G}
    shapes = [g for g in G if g['b'] and not g['label']]
    conts = [g for g in shapes if g['tipo'] in CONT or (g['tipo'] == 'bpmn:SubProcess' and g['exp'])]
    nos = [g for g in shapes if g not in conts]
    edges = [g for g in G if g['wp']]
    labels = [g for g in G if g['label']]
    P = []
    anc = lambda i: [i] + (anc(E[i]['pai']) if i in E and E[i]['pai'] in E else [])
    # 1. linha ortogonal e encostada na origem e no destino
    for e in edges:
        for p, q in segs(e):
            if p[0] != q[0] and p[1] != q[1]: P.append(f'linha não ortogonal: {e["id"]}')
        if e['tipo'] == 'bpmn:SequenceFlow':
            for pt, k in ((e['wp'][0], 'de'), (e['wp'][-1], 'para')):
                b = E[e[k]]['b']
                if E[e[k]]['tipo'].endswith('Gateway'):
                    cx, cy, r = (b[0] + b[2]) / 2, (b[1] + b[3]) / 2, (b[2] - b[0]) / 2
                    if abs(abs(pt[0] - cx) + abs(pt[1] - cy) - r) > 1.5: P.append(f'linha não encosta no losango {e[k]}: {e["id"]}')
                    continue
                if not (dentro([pt[0], pt[1], pt[0], pt[1]], b, 1) and (abs(pt[0] - b[0]) < 1.5 or abs(pt[0] - b[2]) < 1.5 or abs(pt[1] - b[1]) < 1.5 or abs(pt[1] - b[3]) < 1.5)):
                    P.append(f'linha não encosta na borda de {e[k]}: {e["id"]}')
    # 2. linha passando sobre (ou rente a) forma que não é dela
    for e in edges:
        for n in nos:
            if n['id'] in (e['de'], e['para']): continue
            for p, q in segs(e):
                if seg_rect(p, q, n['b'], FOLGA if n['tipo'] != 'bpmn:SubProcess' else 0):
                    P.append(f'linha {e["id"]} passa sobre/rente a {n["id"]}'); break
        for c in conts:  # atravessa subprocesso aberto sem ser dele
            if c['tipo'] != 'bpmn:SubProcess' or c['id'] in (e['de'], e['para']) or c['id'] in anc(e['de']): continue
            if any(seg_rect(p, q, c['b']) for p, q in segs(e)): P.append(f'linha {e["id"]} atravessa o subprocesso {c["id"]}')
    # 3. cruzamentos de linhas
    cruz = []
    for a, b in itertools.combinations(edges, 2):
        if any(cruza(p, q, r, s) for p, q in segs(a) for r, s in segs(b)): cruz.append(f'{a["id"]} × {b["id"]}')
    # 4. textos: sobre linha, sobre forma, sobre outro texto; texto de tarefa fora da caixa ou sobre o ícone
    txt = [(g['id'], t['b'], t['t'], g) for g in G for t in g['textos'] if g['tipo'] not in CONT]
    for gid, b, t, g in txt:
        dono = g['dono'] or gid
        for e in edges:
            if any(seg_rect(p, q, b, 2) for p, q in segs(e)) and not (e['id'] == gid and not g['label']):
                if dono in (e['de'], e['para']) and not g['label']: continue
                P.append(f'texto "{t[:30]}" ({gid}) encosta na linha {e["id"]}')
        for n in nos:
            if n['id'] == dono or (not g['label'] and n['id'] == gid): continue
            if inter(b, n['b'], 2): P.append(f'texto "{t[:30]}" ({gid}) sobre a forma {n["id"]}')
        if not g['label'] and g['b'] and g['tipo'] not in ('bpmn:SubProcess',) and not dentro(b, g['b'], 0):
            P.append(f'texto sai da caixa: {gid} "{t[:30]}"')
        for ic in g['icones']:
            if not g['label'] and inter(b, ic, 1): P.append(f'texto encosta no ícone: {gid} "{t[:30]}"')
        if g['label'] and E[dono]['b'] and inter(b, E[dono]['b'], 2): P.append(f'rótulo encosta no próprio elemento: {dono} "{t[:30]}"')
        for c in conts:  # faixa do nome do pool ou da lane
            if c['tipo'] in CONT and inter(b, [c['b'][0], c['b'][1], c['b'][0] + 30, c['b'][3]], 2): P.append(f'texto "{t[:30]}" ({gid}) invade a faixa do nome de {c["id"]}')
        if not g['label'] and g['tipo'] == 'bpmn:SubProcess' and not g['exp']:  # recolhido: "+" embaixo e ícone do evento no canto
            x1, y1, x2, y2 = g['b']; cx = (x1 + x2) / 2
            for zona in ([cx - 9, y2 - 23, cx + 9, y2 - 5], [x1 + 2, y1 + 2, x1 + 26, y1 + 26]):
                if inter(b, zona, 1): P.append(f'texto encosta no marcador/ícone do subprocesso: {gid} "{t[:30]}"')
    for (i1, b1, t1, g1), (i2, b2, t2, g2) in itertools.combinations(txt, 2):
        if i1 != i2 and inter(b1, b2, 2): P.append(f'textos sobrepostos: {i1} "{t1[:20]}" × {i2} "{t2[:20]}"')
    # 5. formas sobrepostas e fora do contêiner
    for a, b in itertools.combinations(nos, 2):
        if inter(a['b'], b['b'], 6) and a['pai'] != b['id'] and b['pai'] != a['id']: P.append(f'formas muito próximas/sobrepostas: {a["id"]} × {b["id"]}')
    for n in nos + [c for c in conts if c['tipo'] == 'bpmn:SubProcess']:
        par = E.get(n['pai'])
        if par and par['b'] and par['tipo'] != 'bpmn:Participant' and not dentro(n['b'], par['b'], 0): P.append(f'{n["id"]} sai de {par["id"]}')
    # 6. rótulo longe do dono
    for l in labels:
        o = E[l['dono']]; ob = o['b'] or [min(p[0] for p in o['wp']), min(p[1] for p in o['wp']), max(p[0] for p in o['wp']), max(p[1] for p in o['wp'])]
        if not inter(l['b'], ob, 45): P.append(f'rótulo longe do dono: {l["dono"]}')
    P = sorted(set(P)); tot += len(P) + len(cruz)
    print(f'== {vista}: {len(P)} problemas, {len(cruz)} cruzamentos')
    for p in P: print('  ', p)
    for c in cruz: print('   cruza:', c)
print('TOTAL', tot)
sys.exit(1 if tot else 0)
