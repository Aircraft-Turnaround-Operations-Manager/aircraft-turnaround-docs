"""Gera a matriz de rastreabilidade (ADR-0012) a partir dos arquivos de área.

Uso, na raiz do repositório:  python scripts/gerar_matriz_rastreabilidade.py
Lê os itens 6, 7, 8 e 10 (area-a.md … area-d.md) e reescreve o trecho entre os
marcadores de especificacao/apendice-a-matriz-de-rastreabilidade.md.
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


rfs, rnfs, us_de, ucs = {}, {}, {}, {}
for a in AREAS:
    for ln in ler(ESP / "06-requisitos-funcionais" / f"area-{a}.md").splitlines():
        c = celulas(ln) if ln.startswith("| RF-") else []
        if len(c) >= 4 and re.fullmatch(rf"RF-{ID}", c[0]) and c[1]:
            rfs[c[0]] = {"ator": c[2], "obj": c[3] if len(c) > 3 else ""}
    for ln in ler(ESP / "08-requisitos-nao-funcionais" / f"area-{a}.md").splitlines():
        c = celulas(ln) if ln.startswith("| RNF-") else []
        if len(c) >= 3 and re.fullmatch(rf"RNF-{ID}", c[0]) and c[1]:
            todos = re.search(r"todos os RFs", c[1], re.I)
            rnfs[c[0]] = {"car": c[2], "rfs": "todos" if todos else refs(c[1])}
    for m in re.finditer(rf"^## (US-?{ID})\s*[–-]\s*REQUISITO (RF-{ID})", ler(ESP / "07-estorias-de-usuario" / f"area-{a}.md"), re.M):
        us_de.setdefault(m.group(2), []).append(m.group(1))
    txt = ler(ESP / "10-especificacoes-de-caso-de-uso" / f"area-{a}.md")
    partes = re.split(rf"^## (UC-?{ID})\b.*$", txt, flags=re.M)
    for i in range(1, len(partes), 2):
        ucs[partes[i]] = refs(partes[i + 1])

uc_de = {}
for uc, rr in ucs.items():
    for r in rr:
        uc_de.setdefault(r, []).append(uc)
rnf_de = {}
for rnf, d in rnfs.items():
    for r in (rfs if d["rfs"] == "todos" else d["rfs"]):
        rnf_de.setdefault(r, []).append(rnf)

j = lambda xs: ", ".join(sorted(xs, key=chave)) if xs else "—"
out = []
out.append("### A.1 Requisitos funcionais × objetivos, atores, estórias, casos de uso e RNFs\n")
out.append("| RF | Objetivo | Ator / usuário | Estória | Caso(s) de uso | RNFs aplicáveis |")
out.append("|---|---|---|---|---|---|")
for r in sorted(rfs, key=chave):
    d = rfs[r]
    out.append(f"| {r} | {d['obj'] or '—'} | {d['ator']} | {j(us_de.get(r))} | {j(uc_de.get(r))} | {j(rnf_de.get(r))} |")
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
lac = []
lac += [f"{r} sem estória (K.2)" for r in sorted(rfs, key=chave) if r not in us_de]
lac += [f"{r} sem caso de uso (K.3)" for r in sorted(rfs, key=chave) if r not in uc_de]
lac += [f"{n} sem RF associado" for n, d in sorted(rnfs.items(), key=lambda x: chave(x[0])) if d["rfs"] != "todos" and not (d["rfs"] & set(rfs))]
lac += [f"{u} sem RF citado" for u, rr in sorted(ucs.items(), key=lambda x: chave(x[0])) if not rr]
lac += [f"{u} sem RF correspondente" for r, us in us_de.items() if r not in rfs for u in us]
out.append("\n### A.4 Lacunas encontradas\n")
out += [f"- {x}" for x in lac] or ["- Nenhuma."]
corpo = "\n".join(out)

doc = ler(DESTINO)
if INI not in doc or FIM not in doc:
    sys.exit(f"Marcadores {INI} / {FIM} não encontrados em {DESTINO}")
novo = doc.split(INI)[0] + INI + "\n" + corpo + "\n" + FIM + doc.split(FIM, 1)[1]
DESTINO.write_text(novo.replace("\n", "\r\n") if "\r\n" in DESTINO.read_bytes().decode("utf-8") else novo, encoding="utf-8", newline="")
print(f"{len(rfs)} RFs, {len(rnfs)} RNFs, {sum(map(len, us_de.values()))} estórias, {len(ucs)} casos de uso, {len(lac)} lacunas")
