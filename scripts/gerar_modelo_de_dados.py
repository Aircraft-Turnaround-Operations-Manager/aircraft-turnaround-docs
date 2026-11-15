"""Gera os diagramas do modelo de dados (item 12) a partir do Apêndice B e confere a coerência (C12.2, C12.10).

Uso, na raiz do repositório:
  python scripts/gerar_modelo_de_dados.py            gera especificacao/diagramas/12-modelo-de-dados-*.drawio e confere
  python scripts/gerar_modelo_de_dados.py --conferir só confere (os .drawio no disco × Apêndice B × item 12)
Depois de gerar, exporte cada .drawio com scripts/exportar_drawio.py.

O Apêndice B é a fonte: tabelas, campos, chaves e obrigatoriedade. Notação dos slides: caixa com o nome, a região da PK
separada por uma linha, a coluna PK/FK e os campos "nome: TIPO"; obrigatório em negrito; a seta aponta para a tabela
que tem a PK, com a cardinalidade nas duas pontas.

Diagrama por serviço: o Graphviz (dot, linhas ortogonais) põe as caixas e traça as linhas. Depois, as pontas que chegam
ao mesmo lado de uma caixa são separadas e cada cardinalidade vai para a posição livre mais perto da sua ponta. Como a
ordem de entrada muda o resultado do dot, o script testa TENTATIVAS ordens (sempre as mesmas) e fica com a de menos
problemas: linha dentro ou rente a caixa alheia, linhas coladas, rótulo tocando algo e cruzamentos (Drawio.medir).
Visão geral: os serviços lado a lado, com uma linha «identificador» tracejada de tabela para tabela entre serviços.
"""
import html, json, random, re, subprocess, sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
ESP = RAIZ / "especificacao"
DIAG = ESP / "diagramas"
SLUG = {"Cadastro e Planejamento": "cadastro", "Execução em Solo": "execucao",
        "Monitoramento": "monitoramento", "Exceções e Liberação": "excecoes"}
COR = {"cadastro": "#dae8fc", "execucao": "#d5e8d4", "monitoramento": "#fff2cc", "excecoes": "#f8cecc"}
LINHA, TOPO, LET, KCOL = 20, 26, 7.0, 44  # altura da linha, do título, largura média de letra, coluna PK/FK
TENTATIVAS = 24  # ordens de entrada testadas por diagrama de serviço
TENTATIVAS_GERAL = 120  # e na visão geral, que tem mais linhas entre grupos


def celulas(ln):
    return [c.strip() for c in ln.strip().strip("|").split("|")]


def ler_apendice():
    """{serviço: {tabela: {'tec': bool, 'campos': [(nome, tipo, chave, obrig, ref)], 'unicos': {campo}}}}"""
    m, svc, tab = {}, None, None
    for ln in (ESP / "apendice-b-dicionario-de-dados.md").read_text(encoding="utf-8").splitlines():
        if r := re.match(r"## B\.\d+ (.+)", ln):
            svc = r.group(1).strip(); m[svc] = {}
        elif r := re.match(r"### B\.\d+\.\d+ `(\w+)`( \(técnica\))?", ln):
            tab = m[svc][r.group(1)] = {"tec": bool(r.group(2)), "campos": [], "unicos": set()}
        elif tab is not None and ln.startswith("| `"):
            c = celulas(ln)
            ref = re.match(r"Identificador de `(\w+)`(?: \((.+?)\))?", c[4])
            ref = (ref.group(2) or svc, ref.group(1)) if ref else None
            tab["campos"].append((c[0].strip("`"), c[1].strip("`"), c[2].replace("—", ""), c[3] == "Sim", ref))
        elif tab is not None and (r := re.match(r"- UNIQUE \((\w+)\)$", ln)):
            tab["unicos"].add(r.group(1))
    return m


def ler_item12():
    """{(serviço, tabela)} da tabela 'Serviço | Tabela | RFs atendidos'."""
    out, dentro = set(), False
    for ln in (ESP / "12-modelo-de-dados.md").read_text(encoding="utf-8").splitlines():
        c = celulas(ln) if ln.startswith("|") else []
        if c[:3] == ["Serviço", "Tabela", "RFs atendidos"]: dentro = True
        elif not c: dentro = False
        elif dentro and not re.fullmatch(r":?-+:?", c[0]): out.add((c[0], c[1].strip("`")))
    return out


def fks(svc, m, t):
    """Ligações dentro do serviço: [(tabela PK, [campos FK], obrigatória, única)]; PK composta junta os campos."""
    tab, grupos = m[svc][t], {}
    for nome, _, ch, ob, ref in tab["campos"]:
        if "FK" not in ch or not ref or ref[0] != svc: continue
        alvo = ref[1]
        pk = [c for c in m[svc][alvo]["campos"] if "PK" in c[2]]
        chave = alvo if len(pk) > 1 else f"{alvo}:{nome}"
        grupos.setdefault(chave, (alvo, [], []))[1].append(nome); grupos[chave][2].append(ob)
    return [(alvo, cs, all(o), len(cs) == 1 and cs[0] in tab["unicos"]) for alvo, cs, o in grupos.values()]


def largura(t, campos):
    return int(max([len(t) * 7.5 + 30] + [len(f"{n}: {ti}") * LET + KCOL + 16 for n, ti, *_ in campos]))


def dot_layout(nos, arestas, rank="RL", grupos=None):
    """nos {id: (w, h)}, na ordem dada; arestas [(origem, destino)]; grupos {nome: [ids]} viram molduras (clusters).
    Devolve as posições, os pontos das linhas e as molduras {nome: (x, y, w, h)}."""
    sep = "nodesep=0.5; ranksep=2.2;" if grupos else "nodesep=0.7; ranksep=0.9;"  # vão largo entre serviços
    g = [f'digraph G {{ rankdir={rank}; splines=ortho; {sep} node [shape=box, fixedsize=true];']
    no = lambda i: f'"{i}" [width={nos[i][0] / 72:.3f}, height={nos[i][1] / 72:.3f}];'
    for k, (nome, ids) in enumerate((grupos or {}).items()):
        g += [f'subgraph "cluster_{k}" {{ label="{nome}"; margin=30; fontsize=16;'] + [no(i) for i in ids] + ["}"]
    dentro = {i for ids in (grupos or {}).values() for i in ids}
    g += [no(i) for i in nos if i not in dentro]
    g += [f'"{a}" -> "{b}";' for a, b in arestas]
    g.append("}")
    r = subprocess.run(["dot", "-Tjson"], input="\n".join(g), capture_output=True, text=True, encoding="utf-8", check=True)
    j = json.loads(r.stdout)
    alt = float(j["bb"].split(",")[3])
    pos = {o["name"]: tuple(float(v) for v in o["pos"].split(",")) for o in j.get("objects", []) if "pos" in o}
    pos = {k: (x, alt - y) for k, (x, y) in pos.items()}
    molduras = {o["label"]: [float(v) for v in o["bb"].split(",")] for o in j.get("objects", []) if "nodes" in o and "bb" in o}
    molduras = {k: (x0, alt - y1, x1 - x0, y1 - y0) for k, (x0, y0, x1, y1) in molduras.items()}
    linhas = []
    for e in j.get("edges", []):
        fim = [p[2:] for p in e["pos"].split() if p.startswith("e,")]
        partes = [p for p in e["pos"].split() if not p.startswith(("e,", "s,"))]
        pts = [(float(x), alt - float(y)) for x, y in (p.split(",") for p in partes)]
        meio = []
        for p in pts[1:-1]:
            if not meio or meio[-1] != p: meio.append(p)
        xy = lambda q: (float(q.split(",")[0]), alt - float(q.split(",")[1]))
        linhas.append((pts[0], xy(fim[0]) if fim else pts[-1], meio))
    return pos, linhas, molduras


class Drawio:
    def __init__(self):
        self.cells, self.n, self.geo, self.arestas, self.tabelas, self.ruins_rot, self.acabado = [], 1, {}, [], set(), 0, False
        self.espalhar_pontas = True
        self.molduras = []  # bordas dos serviços na visão geral: linha correndo sobre elas confunde a leitura

    def id(self):
        self.n += 1; return f"c{self.n}"

    def cell(self, value, style, x, y, w, h, parent="1", vertex=True, extra=""):
        i = self.id()
        tipo = 'vertex="1"' if vertex else 'edge="1"'
        if parent == "1": self.geo[i] = (x, y, w, h)
        self.cells.append(f'<mxCell id="{i}" value="{html.escape(value, quote=True).replace(chr(10), "&#10;")}" style="{style}" {tipo} parent="{parent}" {extra}>'
                          f'<mxGeometry x="{x:.0f}" y="{y:.0f}" width="{w:.0f}" height="{h:.0f}" as="geometry"/></mxCell>')
        return i

    def edge(self, src, dst, style, linha, rotulos=()):
        """Guarda a linha como o Graphviz a traçou: ponto de saída, dobras e ponto de chegada."""
        ini, fim, pontos = linha
        self.arestas.append({"id": self.id(), "src": src, "dst": dst, "style": style, "rot": rotulos,
                             "p": [ini, *pontos, fim] if src != dst else self.laco(src)})

    def laco(self, no):
        """Relação da tabela com ela mesma: um laço curto em cima da caixa, com as duas pontas separadas."""
        x, y, w, h = self.geo[no]
        return [(x + 0.55 * w, y), (x + 0.55 * w, y - 28), (x + 0.85 * w, y - 28), (x + 0.85 * w, y)]

    # ---- geometria das linhas -------------------------------------------------------------------------------
    def caixas(self, menos=()):
        return [g for i, g in self.geo.items() if i not in menos and i in self.tabelas]

    @staticmethod
    def corta(a, b, g, m=3):
        """O segmento a-b (horizontal ou vertical) passa por dentro do retângulo g (com margem m)?"""
        x, y, w, h = g
        x1, x2 = sorted((a[0], b[0])); y1, y2 = sorted((a[1], b[1]))
        return x1 < x + w - m and x2 > x + m and y1 < y + h - m and y2 > y + m

    @staticmethod
    def colados(s1, s2):
        """Dois segmentos paralelos a menos de 10 px um do outro, com trecho em comum."""
        (a, b), (c, d) = s1, s2
        for i in (0, 1):  # i = 0: verticais (x igual); i = 1: horizontais (y igual)
            j = 1 - i
            if a[i] == b[i] and c[i] == d[i] and abs(a[i] - c[i]) < 10:
                if min(max(a[j], b[j]), max(c[j], d[j])) - max(min(a[j], b[j]), min(c[j], d[j])) > 2: return True
        return False

    def livre(self, pts, e):
        segs = list(zip(pts, pts[1:]))
        if any(self.corta(a, b, g) for a, b in segs for g in self.caixas((e["src"], e["dst"]))): return False
        for o in self.arestas:
            if o is e: continue
            if any(self.colados(s1, s2) for s1 in zip(o["p"], o["p"][1:]) for s2 in segs): return False
        return True

    @staticmethod
    def limpar(pts):
        out = []
        for q in pts:
            q = (round(q[0]), round(q[1]))
            if out and out[-1] == q: continue
            if len(out) >= 2 and (out[-2][0] == out[-1][0] == q[0] or out[-2][1] == out[-1][1] == q[1]):
                out[-1] = q; continue
            out.append(q)
        return out

    def lado(self, no, q):
        x, y, w, h = self.geo[no]
        d = {"t": abs(q[1] - y), "b": abs(q[1] - y - h), "l": abs(q[0] - x), "r": abs(q[0] - x - w)}
        return min(d, key=d.get)

    def espalhar(self):
        """Pontas no mesmo lado da mesma caixa ficam separadas. A linha desliza junto com a dobra vizinha; se isso a
        fizer passar por uma caixa ou colar em outra linha, ela faz um degrau curto perto da caixa."""
        for e in self.arestas: e["p"] = self.limpar(e["p"])
        grupos = {}
        for e in self.arestas:
            if not e["p"]: continue
            for k, no in ((0, e["src"]), (-1, e["dst"])):
                grupos.setdefault((no, self.lado(no, e["p"][k])), []).append((e, k))
        for (no, lado), membros in grupos.items():
            if len(membros) < 2: continue
            x, y, w, h = self.geo[no]; horiz = lado in "tb"
            ao = (lambda q: q[0]) if horiz else (lambda q: q[1])
            membros.sort(key=lambda ek: (ao(ek[0]["p"][1 if ek[1] == 0 else -2]), ao(ek[0]["p"][ek[1]])))
            ini, tam = (x, w) if horiz else (y, h)
            passo = min(40, (tam - 24) / len(membros))
            centro = sum(ao(ek[0]["p"][ek[1]]) for ek in membros) / len(membros)
            c0 = min(max(centro - passo * (len(membros) - 1) / 2, ini + 12), ini + tam - 12 - passo * (len(membros) - 1))
            fora = {"t": (0, -1), "b": (0, 1), "l": (-1, 0), "r": (1, 0)}[lado]
            for n, (e, k) in enumerate(membros):
                novo = c0 + n * passo
                p = list(e["p"]); ponta = p[k]
                if abs(ao(ponta) - novo) < 1: continue
                mover = (lambda q: (novo, q[1])) if horiz else (lambda q: (q[0], novo))
                if len(p) > 2:
                    j = 1 if k == 0 else -2
                    t = list(p); t[k] = mover(p[k]); t[j] = mover(p[j])
                    if self.livre(t, e): e["p"] = self.limpar(t); continue
                for dist in (18, 26, 34, 42, 50):  # degrau perto da caixa
                    a1 = (ponta[0] + fora[0] * dist, ponta[1] + fora[1] * dist)
                    degrau = [mover(ponta), mover(a1), a1]
                    t = degrau + p[1:] if k == 0 else p[:-1] + degrau[::-1]
                    if self.livre(t, e): e["p"] = self.limpar(t); break

    def rotulos(self):
        """Cada cardinalidade vai para a posição mais perto da sua ponta que não toca linha, caixa nem outro rótulo."""
        segs = [(a, b) for e in self.arestas for a, b in zip(e["p"], e["p"][1:])]
        donos = [e["id"] for e in self.arestas for _ in zip(e["p"], e["p"][1:])]
        postos = []
        for e in self.arestas:
            for txt, ponta in e["rot"]:
                rw, rh = 8 * len(txt) + 6, 15
                if not e["p"]:  # laço na própria tabela
                    x, y, w, h = self.geo[e["src"]]
                    cand = [(x + w + 34, y + h / 2 - 14 + (ponta > 0) * 26), (x + w + 34, y + h / 2 + 30 * ponta)]
                else:
                    a = e["p"][0] if ponta < 0 else e["p"][-1]; b = e["p"][1] if ponta < 0 else e["p"][-2]
                    dx, dy = (b[0] > a[0]) - (b[0] < a[0]), (b[1] > a[1]) - (b[1] < a[1])
                    cand = []
                    for t in (12, 22, 34, 48, 64, 82, 104):
                        for s_ in (1, -1, 2.2, -2.2):
                            cand.append((a[0] + dx * (t + (rw / 2 if dx else 0)) + dy * s_ * (rw / 2 + 4),
                                         a[1] + dy * (t + (rh / 2 if dy else 0)) - dx * s_ * (rh / 2 + 3)))
                def custo(c):
                    r = (c[0] - rw / 2, c[1] - rh / 2, rw, rh)
                    k = sum(self.corta(a, b, r, -3) for a, b in segs)
                    k += sum(self.corta((r[0], r[1]), (r[0] + rw, r[1] + rh), g, -2) for g in self.caixas())
                    k += sum(abs(c[0] - q[0]) < (rw + q[2]) / 2 + 2 and abs(c[1] - q[1]) < (rh + q[3]) / 2 + 2 for q in postos)
                    return k
                def perto(c):  # linha de outra relação a menos de 9 px: o rótulo pareceria ser dela
                    r = (c[0] - rw / 2, c[1] - rh / 2, rw, rh)
                    return sum(self.corta(a, b, r, -9) for (a, b), o in zip(segs, donos) if o != e["id"])
                melhor = min(cand, key=lambda c: (custo(c), perto(c), cand.index(c)))
                self.ruins_rot += custo(melhor) > 0
                postos.append((*melhor, rw, rh))
                self.cells.append(f'<mxCell id="{self.id()}" value="{html.escape(txt)}" style="text;html=0;align=center;'
                                  f'verticalAlign=middle;resizable=0;fontSize=12;fontStyle=1;" vertex="1" parent="1">'
                                  f'<mxGeometry x="{melhor[0] - rw / 2:.0f}" y="{melhor[1] - rh / 2:.0f}" width="{rw}" '
                                  f'height="{rh}" as="geometry"/></mxCell>')

    def desenhar_arestas(self):
        def rel(q, g):
            x, y, w, h = g
            return min(max((q[0] - x) / w, 0), 1), min(max((q[1] - y) / h, 0), 1)
        for e in self.arestas:
            style = e["style"]
            if e["p"]:
                (ex, ey), (nx, ny) = rel(e["p"][0], self.geo[e["src"]]), rel(e["p"][-1], self.geo[e["dst"]])
                style = style.replace("edgeStyle=orthogonalEdgeStyle;", "edgeStyle=none;") + (
                    f"exitX={ex:.4f};exitY={ey:.4f};exitPerimeter=0;entryX={nx:.4f};entryY={ny:.4f};entryPerimeter=0;")
            pts = "".join(f'<mxPoint x="{x:.0f}" y="{y:.0f}"/>' for x, y in e["p"][1:-1])
            self.cells.append(f'<mxCell id="{e["id"]}" value="" style="{style}" edge="1" parent="1" source="{e["src"]}" '
                              f'target="{e["dst"]}"><mxGeometry relative="1" as="geometry"><Array as="points">{pts}</Array>'
                              f'</mxGeometry></mxCell>')

    def medir(self):
        """O que restou: linhas que passam por caixa, pares de linhas coladas e rótulos que tocam algo."""
        cx = sum(any(self.corta(a, b, g) for a, b in zip(e["p"], e["p"][1:]) for g in self.caixas((e["src"], e["dst"])))
                 for e in self.arestas)
        segs = [(id(e), s_) for e in self.arestas for s_ in zip(e["p"], e["p"][1:])]
        col = sum(self.colados(s1, s2) for i, (e1, s1) in enumerate(segs) for e2, s2 in segs[i + 1:] if e1 != e2)
        cruz = 0
        for i, (e1, (a, b)) in enumerate(segs):
            for e2, (c, d) in segs[i + 1:]:
                if e1 == e2: continue
                h, v = ((a, b), (c, d)) if a[1] == b[1] else ((c, d), (a, b))
                if h[0][1] == h[1][1] and v[0][0] == v[1][0] and \
                        min(h[0][0], h[1][0]) < v[0][0] < max(h[0][0], h[1][0]) and \
                        min(v[0][1], v[1][1]) < h[0][1] < max(v[0][1], v[1][1]):
                    cruz += 1
        # linha que encosta (a menos de 8 px) numa caixa que não é dela: parece ligada a ela
        rente = sum(any(self.corta(a, b, g, -8) for a, b in zip(e["p"], e["p"][1:])
                        for g in self.caixas((e["src"], e["dst"]))) for e in self.arestas) - cx
        for x, y, w, h in self.molduras:
            lados = [((x, y), (x + w, y)), ((x, y + h), (x + w, y + h)), ((x, y), (x, y + h)), ((x + w, y), (x + w, y + h))]
            rente += sum(self.colados(l, sg) for l in lados for _, sg in segs)
        return {"linha_em_caixa": cx, "linha_rente_a_caixa": rente, "trechos_colados": col,
                "rotulos_tocando": self.ruins_rot, "cruzamentos": cruz}

    def nota(self):
        m = self.medir()
        return (m["linha_em_caixa"] * 100 + (m["trechos_colados"] + m["rotulos_tocando"] + m["linha_rente_a_caixa"]) * 20
                + m["cruzamentos"])

    def acabar(self):
        if not self.acabado:
            if self.espalhar_pontas: self.espalhar()
            self.desenhar_arestas(); self.rotulos(); self.acabado = True
        return self

    def salvar(self, arq, nome):
        self.acabar()
        corpo = "".join(self.cells)
        arq.write_text(f'<mxfile host="gerar_modelo_de_dados.py"><diagram id="d" name="{nome}"><mxGraphModel grid="0" '
                       f'page="0" math="0" shadow="0"><root><mxCell id="0"/><mxCell id="1" parent="0"/>{corpo}</root>'
                       f'</mxGraphModel></diagram></mxfile>\n', encoding="utf-8")


def caixa(d, t, campos, x, y, w, cor):
    """Tabela na notação dos slides: título, região da PK, coluna PK/FK e campos (obrigatório em negrito)."""
    h = TOPO + LINHA * len(campos) + 6
    sw = d.cell(t, f"swimlane;html=0;fontStyle=1;fontSize=13;startSize={TOPO};fillColor={cor};collapsible=0;"
                   "rounded=0;horizontal=1;swimlaneLine=1;", x, y, w, h)
    npk = sum("PK" in c[2] for c in campos)
    for i, (nome, tipo, ch, ob, _) in enumerate(campos):
        yy = TOPO + 3 + i * LINHA
        base = "text;html=0;fontSize=12;verticalAlign=middle;spacingLeft=6;resizable=0;"
        d.cell(ch.replace(" ", ""), base + "align=center;fontStyle=1;", 0, yy, KCOL, LINHA, sw)
        d.cell(f"{nome}: {tipo}", base + f"align=left;fontStyle={1 if ob else 0};", KCOL, yy, w - KCOL, LINHA, sw)
    d.cell("", "line;strokeWidth=1;html=0;", 0, TOPO + 3 + npk * LINHA - 1, w, 2, sw)
    d.cell("", "line;direction=south;strokeWidth=1;html=0;", KCOL - 1, TOPO, 2, h - TOPO, sw)
    return sw, h


def diagrama_servico(svc, m, semente=0):
    tabs = m[svc]; nos, arestas, info = {}, [], []
    for t, d in tabs.items():
        nos[t] = (largura(t, d["campos"]), TOPO + LINHA * len(d["campos"]) + 6)
        for alvo, cs, ob, unico in fks(svc, m, t):
            arestas.append((t, alvo)); info.append((cs, ob, unico))
    tec = [t for t, d in tabs.items() if d["tec"]]
    ordem = [t for t in nos if t not in tec]
    if semente:
        r = random.Random(semente); r.shuffle(ordem)
        juntos = list(zip(arestas, info)); r.shuffle(juntos); arestas, info = map(list, zip(*juntos))
    pos, linhas, _ = dot_layout({t: nos[t] for t in ordem}, arestas)
    base = max(cy + nos[t][1] / 2 for t, (cx, cy) in pos.items()) + 90
    x, alto = 40, max(nos[t][1] for t in tec)
    for t in tec:
        pos[t] = (x + nos[t][0] / 2, base + 40 + nos[t][1] / 2); x += nos[t][0] + 50
    d, ids = Drawio(), {}
    d.cell("Tabelas técnicas, sem FK (ADR-0016, ADR-0018, ADR-0020; seção 12.6)", "rounded=0;html=0;fillColor=none;"
           "dashed=1;verticalAlign=top;align=left;spacingLeft=8;fontSize=13;fontStyle=2;strokeColor=#666666;",
           10, base, x - 20, alto + 60)
    cor = COR[SLUG[svc]]
    for t, (cx, cy) in pos.items():
        w, h = nos[t]
        ids[t], _ = caixa(d, t, tabs[t]["campos"], cx - w / 2, cy - h / 2, w, "#eeeeee" if t in tec else cor)
        d.tabelas.add(ids[t])
    for (a, b), (cs, ob, unico), pts in zip(arestas, info, linhas):
        ponta_pk = "1" if ob else "0..1"
        ponta_fk = "0..1" if unico else "n"
        estilo = ("edgeStyle=orthogonalEdgeStyle;rounded=0;html=0;endArrow=open;endSize=10;strokeWidth=1.3;"
                  + ("" if a != b else "loop=1;"))
        d.edge(ids[a], ids[b], estilo, pts, [(ponta_fk, -1), (ponta_pk, 1)])
    return d


def visao_geral(m, semente=0):
    """Os serviços lado a lado, cada um com as suas tabelas de negócio em coluna, e uma linha tracejada «identificador»
    da tabela que guarda o identificador até a tabela dona, em outro serviço. As FKs de dentro de cada serviço estão
    nos diagramas por serviço. A nota fica embaixo, para o diagrama não ficar largo."""
    nos, arestas, grupos = {}, [], {}
    for svc, tabs in m.items():
        grupos[svc] = [f"{svc}.{t}" for t, d in tabs.items() if not d["tec"]]
        for i in grupos[svc]: nos[i] = (len(i.split(".", 1)[1]) * 7.5 + 30, 32)
        for t, d in tabs.items():
            vistos = set()
            for *_, ref in d["campos"]:
                if not d["tec"] and ref and ref[0] != svc and ref[1] != "usuario" and ref not in vistos:
                    vistos.add(ref); arestas.append((f"{svc}.{t}", f"{ref[0]}.{ref[1]}"))
    if semente:
        r = random.Random(semente)
        for ids in grupos.values(): r.shuffle(ids)
        r.shuffle(arestas)
    pos, linhas, molduras = dot_layout(nos, arestas, rank="LR", grupos=grupos)
    d, ids = Drawio(), {}
    d.molduras = list(molduras.values())
    for nome, (x, y, w, h) in molduras.items():
        d.cell(f"«serviço» {nome}", f"rounded=0;html=0;fillColor={COR[SLUG[nome]]};opacity=60;verticalAlign=top;align=left;"
                                    "spacingLeft=8;fontSize=15;fontStyle=1;", x, y, w, h)
    for i, (cx, cy) in pos.items():
        w, h = nos[i]
        ids[i] = d.cell(i.split(".", 1)[1], "rounded=0;html=0;fillColor=#ffffff;fontSize=12;", cx - w / 2, cy - h / 2, w, h)
        d.tabelas.add(ids[i])
    for (a, b), pts in zip(arestas, linhas):
        d.edge(ids[a], ids[b], "edgeStyle=orthogonalEdgeStyle;rounded=0;html=0;endArrow=open;endSize=8;dashed=1;"
                               "strokeColor=#555555;", pts)
    nota = ["Visão geral: as tabelas de negócio de cada serviço; as chaves estrangeiras dentro",
            "de cada serviço estão nos diagramas por serviço.",
            "Linha tracejada: dependência «identificador». A tabela guarda o identificador",
            "do dono, que está em outro serviço, sem FK (ADR-0015).",
            "Autor, responsável e operador apontam para usuario (Cadastro e Planejamento)",
            "em todos os serviços; essas linhas não são desenhadas.",
            "Tabelas técnicas: ver a seção 12.6."]
    y0 = max(y + h for x, y, w, h in molduras.values()) + 30
    d.cell(chr(10).join(nota), "shape=note;html=0;whiteSpace=nowrap;align=left;spacingLeft=8;fontSize=12;size=14;",
           min(x for x, y, w, h in molduras.values()), y0, 560, 20 * len(nota) + 20)
    return d


def ler_drawio(arq):
    """{tabela: [(nome, tipo, obrigatório)]} de um diagrama por serviço."""
    txt, out, pais = arq.read_text(encoding="utf-8"), {}, {}
    for c in re.finditer(r'<mxCell id="(\w+)" value="([^"]*)" style="([^"]*)" vertex="1" parent="(\w+)"', txt):
        i, v, st, p = c.groups()
        v = html.unescape(v)
        if st.startswith("swimlane"): pais[i] = v; out[v] = []
        elif p in pais and ": " in v:
            n, t = v.split(": ", 1); out[pais[p]].append((n, t, "fontStyle=1" in st))
    return out


def conferir(m):
    erros = []
    neg = {(s, t) for s, ts in m.items() for t, d in ts.items() if not d["tec"]}
    i12 = ler_item12()
    erros += [f"item 12 sem a tabela {t} ({s})" for s, t in sorted(neg - i12)]
    erros += [f"item 12 cita {t} ({s}), que não está no Apêndice B" for s, t in sorted(i12 - neg)]
    for svc, tabs in m.items():
        for t, d in tabs.items():
            if not any("PK" in c[2] for c in d["campos"]): erros.append(f"{svc}.{t} sem PK")
            for n, _, ch, _, ref in d["campos"]:
                if ref and ref[1] not in m.get(ref[0], {}): erros.append(f"{svc}.{t}.{n} aponta para {ref} inexistente")
                if ref and "FK" in ch and ref[0] != svc: erros.append(f"{svc}.{t}.{n}: FK entre serviços")
        arq = DIAG / f"12-modelo-de-dados-{SLUG[svc]}.drawio"
        if not arq.exists(): erros.append(f"falta {arq.name}"); continue
        dg = ler_drawio(arq)
        ap = {t: [(n, ti, ob) for n, ti, _, ob, _ in d["campos"]] for t, d in tabs.items()}
        erros += [f"{arq.name}: {t} diferente do Apêndice B" for t in sorted(set(ap) | set(dg)) if ap.get(t) != dg.get(t)]
    return erros


def main():
    m = ler_apendice()
    if "--conferir" not in sys.argv:
        for svc in m:
            arq = DIAG / f"12-modelo-de-dados-{SLUG[svc]}.drawio"
            # várias ordens de entrada no Graphviz; fica a disposição com menos problemas (sempre a mesma)
            d = min((diagrama_servico(svc, m, k).acabar() for k in range(TENTATIVAS)), key=lambda x: x.nota())
            d.salvar(arq, f"Modelo de dados — {svc}"); print("gerado", arq.name, d.medir())
        d = min((visao_geral(m, k).acabar() for k in range(TENTATIVAS_GERAL)), key=lambda x: x.nota())
        d.salvar(DIAG / "12-modelo-de-dados-visao-geral.drawio", "Modelo de dados — visão geral")
        print("gerado 12-modelo-de-dados-visao-geral.drawio", d.medir())
    erros = conferir(m)
    n = sum(len(ts) for ts in m.values()); tec = sum(d["tec"] for ts in m.values() for d in ts.values())
    print(f"{n - tec} tabelas de negócio + {tec} técnicas; {len(erros)} problema(s)")
    for e in erros: print("-", e)
    sys.exit(1 if erros else 0)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
