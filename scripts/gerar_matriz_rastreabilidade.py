"""Gera a matriz de rastreabilidade (ADR-0012 e ADR-0021) a partir dos arquivos de área.

Uso, na raiz do repositório:  python scripts/gerar_matriz_rastreabilidade.py
Lê os itens 6, 7, 8 e 10 (area-a.md … area-d.md) e, no RA2 (decisão B5, ADR-0021), a tabela
"Serviço | Tabela | RFs atendidos" do item 12, as legendas "Diagrama de Sequência do UCnn" do
item 14 e a coluna "Estória e critério de aceite" (USnnn-CAn) da planilha do item 15. Reescreve o
trecho entre os marcadores de especificacao/apendice-a-matriz-de-rastreabilidade.md.
As lacunas de um item do RA2 só entram na lista depois que o item tem conteúdo.
Funciona com os IDs provisórios (RF-A1…) e com os finais (RF-1…).
"""
import re, sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
ESP = RAIZ / "especificacao"
DESTINO = ESP / "apendice-a-matriz-de-rastreabilidade.md"
INI, FIM = "<!-- matriz:inicio -->", "<!-- matriz:fim -->"
AREAS = "abcd"
ID = r"(?:[A-D]\d+|\d+)"


def ler(p):
    return p.read_text(encoding="utf-8").replace("\r\n", "\n") if p.exists() else ""


def chave(x):  # ordena RF-A1 < RF-A2 < RF-B1 … ou RF-1 < RF-2 …
    m = re.match(r"[A-Z]+-?([A-D]?)(\d+)", x)
    return (m.group(1), int(m.group(2))) if m else ("", 0)


def refs(texto, prefixo="RF"):
    """IDs citados no texto, expandindo faixas 'RF-B1 a RF-B6'."""
    achados = set()
    for a, b in re.findall(rf"\b{prefixo}-({ID})\s+a\s+{prefixo}-({ID})\b", texto):
        ma, mb = re.match(r"([A-D]?)(\d+)", a), re.match(r"([A-D]?)(\d+)", b)
        if ma.group(1) == mb.group(1):
            for n in range(int(ma.group(2)), int(mb.group(2)) + 1):
                achados.add(f"{prefixo}-{ma.group(1)}{n}")
    achados |= {f"{prefixo}-{x}" for x in re.findall(rf"\b{prefixo}-({ID})\b", texto)}
    return achados


def celulas(linha):
    return [c.strip() for c in linha.strip().strip("|").split("|")]


rfs, rnfs, us_de, ucs, nome_uc = {}, {}, {}, {}, {}
cas, seq, cts, tabs = [], {}, {}, {}  # RA2: critérios de aceite, diagramas de sequência, casos de teste, tabelas
for a in AREAS:
    for ln in ler(ESP / "06-requisitos-funcionais" / f"area-{a}.md").splitlines():
        c = celulas(ln) if ln.startswith("| RF-") else []
        if len(c) >= 6 and re.fullmatch(rf"RF-{ID}", c[0]) and c[2]:  # # | TÍTULO | REQUISITO FUNCIONAL | ATOR | OBJETIVO | SPRINT
            rfs[c[0]] = {"tit": c[1], "ator": c[3], "obj": c[4]}
    for ln in ler(ESP / "08-requisitos-nao-funcionais" / f"area-{a}.md").splitlines():
        c = celulas(ln) if ln.startswith("| RNF-") else []
        if len(c) >= 3 and re.fullmatch(rf"RNF-{ID}", c[0]) and c[1]:
            todos = re.search(r"todos os RFs", c[1], re.I)
            rnfs[c[0]] = {"car": c[2], "rfs": "todos" if todos else refs(c[1])}
    est = ler(ESP / "07-estorias-de-usuario" / f"area-{a}.md")
    for m in re.finditer(rf"^## (US-?{ID})\s*[–-]\s*REQUISITO (RF-{ID})", est, re.M):
        us_de.setdefault(m.group(2), []).append(m.group(1))
    partes = re.split(r"^## (US\d+)\b.*$", est, flags=re.M)
    for i in range(1, len(partes), 2):  # critério de aceite USnnn-CAn = linha n da tabela da estória
        cas += [f"{partes[i]}-CA{n}" for n in re.findall(r"^\| (\d+) \| ", partes[i + 1], re.M)]
    txt = ler(ESP / "10-especificacoes-de-caso-de-uso" / f"area-{a}.md")
    nome_uc.update(re.findall(r"^## (UC\d+)\s*[–-]\s*(.+?)\s*$", txt, re.M))
    partes = re.split(rf"^## (UC-?{ID})\b.*$", txt, flags=re.M)
    for i in range(1, len(partes), 2):
        ucs[partes[i]] = refs(partes[i + 1])
    figs = ler(ESP / "14-diagramas-de-sequencia" / f"area-{a}.md")
    for m in re.finditer(r"!\[Diagrama de Sequência do (UC\d+) [–-] (.*?)(?: \(parte [^)]*\))?\]\(([^)]+)\)", figs):
        seq.setdefault(m.group(1), []).append((m.group(2).strip(), Path(m.group(3)).name))
    for ln in ler(ESP / "15-casos-de-teste" / f"area-{a}.md").splitlines():
        c = celulas(ln) if ln.startswith("| CT-") else []
        if len(c) >= 4:  # ID | Caso de uso | Cenário | Estória e critério de aceite | …
            cts[c[0]] = re.findall(r"US\d+-CA\d+", c[3])

em_tab = False
for ln in ler(ESP / "12-modelo-de-dados.md").splitlines():  # | Serviço | Tabela | RFs atendidos |
    c = celulas(ln) if ln.startswith("|") else []
    if c[:3] == ["Serviço", "Tabela", "RFs atendidos"]:
        em_tab = True
    elif not c:
        em_tab = False
    elif em_tab and len(c) >= 3 and not re.fullmatch(r":?-+:?", c[0]):
        tabs[c[1].strip("`")] = refs(c[2])

uc_de, rnf_de, tab_de, ct_de = {}, {}, {}, {}
for uc, rr in ucs.items():
    for r in rr:
        uc_de.setdefault(r, []).append(uc)
for rnf, d in rnfs.items():
    for r in (rfs if d["rfs"] == "todos" else d["rfs"]):
        rnf_de.setdefault(r, []).append(rnf)
for t, rr in tabs.items():
    for r in rr:
        tab_de.setdefault(r, []).append(t)
for ct, cc in cts.items():
    for x in cc:
        ct_de.setdefault(x, []).append(ct)

j = lambda xs: ", ".join(sorted(xs, key=chave)) if xs else "—"
num_ct = lambda x: (re.sub(r"\d+$", "", x), int(re.search(r"\d+$", x).group()))  # CT-001 ou CT-B001
out = []
out.append("### A.1 Requisitos funcionais × títulos, objetivos, atores, estórias, casos de uso, RNFs e tabelas\n")
out.append("| RF | Título | Objetivo | Ator / usuário | Estória | Caso(s) de uso | RNFs aplicáveis | Tabelas (item 12) |")
out.append("|---|---|---|---|---|---|---|---|")
for r in sorted(rfs, key=chave):
    d = rfs[r]
    tb = ", ".join(sorted(tab_de.get(r, []))) or "—"
    out.append(f"| {r} | {d['tit']} | {d['obj'] or '—'} | {d['ator']} | {j(us_de.get(r))} | {j(uc_de.get(r))} | {j(rnf_de.get(r))} | {tb} |")
out.append("\n### A.2 Objetivos × requisitos funcionais\n")
out.append("| Objetivo | RFs que o atendem |")
out.append("|---|---|")
for o in ("1", "2", "3"):
    lst = [r for r, d in rfs.items() if re.search(rf"\b{o}\b", d["obj"])]
    out.append(f"| Objetivo {o} | {j(lst)} |")
out.append("\n### A.3 Requisitos não funcionais × requisitos funcionais\n")
out.append("| RNF | Característica ISO/IEC 25010 | RFs cobertos |")
out.append("|---|---|---|")
for n in sorted(rnfs, key=chave):
    d = rnfs[n]
    out.append(f"| {n} | {d['car']} | {'todos os RFs' if d['rfs'] == 'todos' else j(d['rfs'] & set(rfs))} |")
out.append("\n### A.4 Casos de uso × diagramas de sequência (item 14)\n")
out.append("| Caso de uso | Diagrama(s) de sequência |")
out.append("|---|---|")
for u in sorted(ucs, key=chave):
    out.append(f"| {u} | {', '.join(f for _, f in seq.get(u, [])) or '—'} |")
out.append("\n### A.5 Critérios de aceite × casos de teste (item 15)\n")
out.append("| Critério de aceite | Casos de teste |")
out.append("|---|---|")
for x in sorted(cas, key=lambda x: tuple(map(int, re.findall(r"\d+", x)))):
    out.append(f"| {x} | {', '.join(sorted(ct_de.get(x, []), key=num_ct)) or '—'} |")
lac = []
lac += [f"{r} sem estória (K.2)" for r in sorted(rfs, key=chave) if r not in us_de]
lac += [f"{r} sem caso de uso (K.3)" for r in sorted(rfs, key=chave) if r not in uc_de]
lac += [f"{n} sem RF associado" for n, d in sorted(rnfs.items(), key=lambda x: chave(x[0])) if d["rfs"] != "todos" and not (d["rfs"] & set(rfs))]
lac += [f"{u} sem RF citado" for u, rr in sorted(ucs.items(), key=lambda x: chave(x[0])) if not rr]
lac += [f"{u} sem RF correspondente" for r, us in us_de.items() if r not in rfs for u in us]
n_ra1 = len(lac)
if tabs:  # item 12 começado
    lac += [f"Tabela {t} sem RF (item 12)" for t, rr in sorted(tabs.items()) if not rr & set(rfs)]
if seq:  # item 14 começado
    lac += [f"{u} sem diagrama de sequência (item 14)" for u in sorted(ucs, key=chave) if u not in seq]
    lac += [f"{u}: nome no diagrama de sequência diferente do item 10" for u, dd in sorted(seq.items()) if any(n != nome_uc.get(u) for n, _ in dd)]
if cts:  # item 15 começado
    lac += [f"{x} sem caso de teste (item 15)" for x in cas if x not in ct_de]
    lac += [f"{ct} aponta para critério inexistente: {x}" for ct, cc in sorted(cts.items(), key=lambda x: num_ct(x[0])) for x in cc if x not in cas]
    lac += [f"{ct} sem critério de aceite" for ct, cc in sorted(cts.items(), key=lambda x: num_ct(x[0])) if not cc]
out.append("\n### A.6 Lacunas encontradas\n")
out += [f"- {x}" for x in lac] or ["- Nenhuma."]
corpo = "\n".join(out)

doc = ler(DESTINO)
if INI not in doc or FIM not in doc:
    sys.exit(f"Marcadores {INI} / {FIM} não encontrados em {DESTINO}")
novo = doc.split(INI)[0] + INI + "\n" + corpo + "\n" + FIM + doc.split(FIM, 1)[1]
DESTINO.write_text(novo.replace("\n", "\r\n") if "\r\n" in DESTINO.read_bytes().decode("utf-8") else novo, encoding="utf-8", newline="")
print(f"{len(rfs)} RFs, {len(rnfs)} RNFs, {sum(map(len, us_de.values()))} estórias, {len(ucs)} casos de uso, "
      f"{len(cas)} critérios de aceite, {len(tabs)} tabelas, {len(seq)} casos de uso com diagrama de sequência, "
      f"{len(cts)} casos de teste, {len(lac)} lacunas ({len(lac) - n_ra1} dos itens 12 a 15)")
