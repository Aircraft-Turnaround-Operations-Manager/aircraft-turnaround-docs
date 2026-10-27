"""Confere a geometria de um diagrama de atividades feito no draw.io (item 11), sobre o SVG exportado.

O texto e as linhas são medidos no Chrome (scripts/medir_svg.mjs), como de fato aparecem na imagem. Aponta: linha que
não é ortogonal; linha sobre ou rente a forma que não é dela; trechos de linhas diferentes sobrepostos; cruzamentos;
texto sobre linha, sobre forma, sobre outro texto ou cruzando a divisa entre partições; texto que sai da caixa.

Uso: python scripts/exportar_drawio.py <arquivo.drawio>  e depois  python scripts/verificar_drawio.py <arquivo.drawio> [...]
Sai com código 1 se encontrar problema ou cruzamento.
"""
import sys, json, re, itertools, subprocess, tempfile, xml.etree.ElementTree as ET
from pathlib import Path


def tipo(st):
    if st.startswith('swimlane'): return 'particao'
    if st.startswith('text;'): return 'titulo'
    if 'shape=note' in st: return 'nota'
    if 'rhombus' in st: return 'dec'
    if 'ellipse' in st: return 'no'
    if 'rounded=0' in st: return 'barra'
    return 'acao'


def inter(a, b, m=0): return a[0] - m < b[2] and b[0] - m < a[2] and a[1] - m < b[3] and b[1] - m < a[3]


def seg_rect(p, q, r, m=0):
    x1, x2 = sorted((p[0], q[0])); y1, y2 = sorted((p[1], q[1]))
    return x1 < r[2] + m and x2 > r[0] - m and y1 < r[3] + m and y2 > r[1] - m


def cruza(a, b, c, d):  # cruzamento próprio entre um trecho horizontal e um vertical
    if abs(a[1] - b[1]) < .5 and abs(c[0] - d[0]) < .5: h, v = (a, b), (c, d)
    elif abs(a[0] - b[0]) < .5 and abs(c[1] - d[1]) < .5: h, v = (c, d), (a, b)
    else: return False
    hx1, hx2 = sorted((h[0][0], h[1][0])); vy1, vy2 = sorted((v[0][1], v[1][1]))
    return hx1 + .5 < v[0][0] < hx2 - .5 and vy1 + .5 < h[0][1] < vy2 - .5


def sobrepoe(a, b, c, d):  # trechos colineares de linhas diferentes que se sobrepõem
    if abs(a[1] - b[1]) < .5 and abs(c[1] - d[1]) < .5 and abs(a[1] - c[1]) < 2:
        return min(max(a[0], b[0]), max(c[0], d[0])) - max(min(a[0], b[0]), min(c[0], d[0])) > 2
    if abs(a[0] - b[0]) < .5 and abs(c[0] - d[0]) < .5 and abs(a[0] - c[0]) < 2:
        return min(max(a[1], b[1]), max(c[1], d[1])) - max(min(a[1], b[1]), min(c[1], d[1])) > 2
    return False


def verificar(arq):
    med = Path(tempfile.gettempdir()) / (Path(arq).stem + '.medida.json')
    subprocess.run(['node', str(Path(__file__).with_name('medir_svg.mjs')), str(Path(arq).with_suffix('.svg')), str(med)], check=True)
    M = json.load(open(med, encoding='utf-8'))
    cel = {c.get('id'): c for c in ET.parse(arq).getroot().iter('mxCell')}
    V = {}
    for i, c in cel.items():
        g = c.find('mxGeometry')
        if c.get('vertex') == '1' and g is not None:
            x, y, w, h = (float(g.get(k, 0)) for k in ('x', 'y', 'width', 'height'))
            V[i] = dict(t=tipo(c.get('style') or ''), b=[x, y, x + w, y + h])
    parts = [i for i, v in V.items() if v['t'] == 'particao']
    # deslocamento SVG -> drawio, pelo canto superior esquerdo da primeira partição
    p0 = min(parts, key=lambda i: V[i]['b'][0])
    mx = re.match(r'M ([\d.]+) ([\d.]+) L ([\d.]+) ([\d.]+)', M[p0]['linhas'][0])
    dx, dy = float(mx.group(3)) - V[p0]['b'][0], float(mx.group(4)) - V[p0]['b'][1]

    def pontos(d):
        n = [float(v) for v in re.findall(r'-?[\d.]+', d)]; return [(n[k] - dx, n[k + 1] - dy) for k in range(0, len(n), 2)]
    E = {i: dict(de=c.get('source'), para=c.get('target'), pts=pontos(M[i]['linhas'][0])) for i, c in cel.items() if c.get('edge') == '1'}
    T = [(i, t['t'], [t['b'][0] - dx, t['b'][1] - dy, t['b'][2] - dx, t['b'][3] - dy])
         for i, m in M.items() for t in m['textos'] if i in cel and i not in parts]
    segs = lambda e: list(zip(e['pts'], e['pts'][1:]))
    nos = {i: v for i, v in V.items() if v['t'] not in ('particao', 'titulo')}
    P = []
    for i, e in E.items():
        for p, q in segs(e):
            if abs(p[0] - q[0]) > .5 and abs(p[1] - q[1]) > .5: P.append(f'linha não ortogonal: {i}')
        for n, v in nos.items():
            if n not in (e['de'], e['para']) and any(seg_rect(p, q, v['b'], 4 if v['t'] == 'barra' else 8) for p, q in segs(e)):
                P.append(f'linha {i} passa sobre/rente a {n}')
    cruz = [f'{a} × {b}' for a, b in itertools.combinations(E, 2) if any(cruza(p, q, r, s) for p, q in segs(E[a]) for r, s in segs(E[b]))]
    for a, b in itertools.combinations(E, 2):
        if any(sobrepoe(p, q, r, s) for p, q in segs(E[a]) for r, s in segs(E[b])): P.append(f'linhas sobrepostas: {a} e {b}')
    divisas = sorted({V[i]['b'][0] for i in parts} | {V[i]['b'][2] for i in parts})
    for i, t, b in T:
        for j, e in E.items():
            if any(seg_rect(p, q, b, 2) for p, q in segs(e)): P.append(f'texto "{t}" ({i}) encosta na linha {j}')
        for n, v in nos.items():
            if not (n == i and v['t'] in ('acao', 'nota')) and inter(b, v['b'], 2): P.append(f'texto "{t}" ({i}) sobre a forma {n}')
        if i in nos and nos[i]['t'] in ('acao', 'nota'):
            x1, y1, x2, y2 = nos[i]['b']
            if not (b[0] >= x1 + 4 and b[2] <= x2 - 4 and b[1] >= y1 + 2 and b[3] <= y2 - 2): P.append(f'texto sai da caixa ou encosta na borda: {i} "{t}"')
        if V.get(i, {}).get('t') != 'titulo':
            for x in divisas:
                if b[0] - 2 < x < b[2] + 2: P.append(f'texto "{t}" ({i}) cruza a divisa de partição x={x:g}')
    for (i1, t1, b1), (i2, t2, b2) in itertools.combinations(T, 2):
        if i1 != i2 and inter(b1, b2, 2): P.append(f'textos sobrepostos: {i1} "{t1}" × {i2} "{t2}"')
    for a, b in itertools.combinations(nos, 2):
        if inter(nos[a]['b'], nos[b]['b'], 10): P.append(f'formas muito próximas: {a} × {b}')
    P = sorted(set(P))
    print(f'{arq}: {len(P)} problemas, {len(cruz)} cruzamentos')
    for p in P: print('  ', p)
    for c in cruz: print('   cruza:', c)
    return not (P or cruz)


if __name__ == '__main__':
    ok = [verificar(a) for a in sys.argv[1:]]
    sys.exit(0 if all(ok) else 1)
