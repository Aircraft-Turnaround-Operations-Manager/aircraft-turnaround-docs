"""Confere os diagramas de sequência do item 14 (especificacao/14-diagramas-de-sequencia/area-a.md a area-d.md).

O que confere (entregas/ra2-criterios-de-aceite.md, seção do item 14):
  C14.1  todo caso de uso do item 10 tem pelo menos uma figura, com a legenda "Diagrama de Sequência do UCnn – <nome>"
         e o mesmo nome do item 10 (a parte de um diagrama dividido leva "(parte n: ...)" depois do nome); a seção
         "## UCnn – <nome>" usa o mesmo nome; total de 37
  C14.4  cada fluxo alternativo e de exceção do item 10 (An, En) aparece na fonte .puml do caso de uso ou na lista de
         fluxos agrupados do arquivo da área (linha "- UCnn: ...")
  C14.8  toda figura tem a .png, a .svg e a fonte editável .puml de mesmo nome (Y.6, Y.7), e nenhuma .svg tem
         <foreignObject> (texto como texto SVG, para o PDF)
O C13.8 (métodos que existem no item 13) é conferido por python scripts/conferir_classes.py --sequencia.
Áreas ainda sem diagrama aparecem como pendentes e, sem --completo, não contam como problema.

Uso: python scripts/conferir_sequencia.py [--area c] [--completo]
Sai com código 1 se houver problema.
"""
import re, sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
ESP = RAIZ / 'especificacao'
DIR14 = ESP / '14-diagramas-de-sequencia'
AREAS = 'abcd'
problemas = []


def erro(msg): problemas.append(msg)
def ler(p): return p.read_text(encoding='utf-8') if p.exists() else ''


def item10():
    """{UCnn: (área, nome, [fluxos alternativos e de exceção])}"""
    ucs = {}
    for a in AREAS:
        partes = re.split(r'^## (UC\d+)\s*[–-]\s*(.+?)\s*$', ler(ESP / '10-especificacoes-de-caso-de-uso' / f'area-{a}.md'), flags=re.M)
        for i in range(1, len(partes), 3):
            ucs[partes[i]] = (a, partes[i + 1], re.findall(r'^### Fluxo (?:alternativo|de exceção) ([AE]\d+)', partes[i + 2], re.M))
    return ucs


def main():
    so = sys.argv[sys.argv.index('--area') + 1].lower() if '--area' in sys.argv else None
    completo = '--completo' in sys.argv
    ucs = item10()
    areas = [so] if so else list(AREAS)
    figuras, pendentes, fluxos, faltam = {}, [], 0, 0
    for a in areas:
        arq = DIR14 / f'area-{a}.md'
        txt = ler(arq)
        figs = re.findall(r'!\[Diagrama de Sequência do (UC\d+) [–-] (.*?)(?: \(parte ([^)]*)\))?\]\(([^)]+)\)', txt)
        if not figs: pendentes.append(a.upper()); continue
        for n, ln in enumerate(txt.splitlines(), 1):
            m = re.match(r'^## (UC\d+)\s*[–-]\s*(.+?)\s*$', ln)
            if m and m.group(1) in ucs and m.group(2) != ucs[m.group(1)][1]:
                erro(f'{arq.name}:{n}: nome da seção diferente do item 10: "{m.group(2)}" × "{ucs[m.group(1)][1]}" (C14.1)')
        for uc, nome, parte, caminho in figs:
            figuras.setdefault(uc, []).append((a, nome, parte, caminho))
            if uc not in ucs: erro(f'{arq.name}: {uc} não existe no item 10'); continue
            if ucs[uc][0] != a: erro(f'{arq.name}: {uc} é da área {ucs[uc][0].upper()} (item 10)')
            if nome != ucs[uc][1]: erro(f'{arq.name}: legenda do {uc} com nome diferente do item 10: "{nome}" × "{ucs[uc][1]}" (C14.1)')
            png = (arq.parent / caminho).resolve()
            base = re.sub(r'_\d{3}$', '', png.stem)
            for p in (png, png.with_suffix('.svg'), png.with_name(base + '.puml')):
                if not p.exists(): erro(f'{arq.name}: falta {p.relative_to(RAIZ)} (C14.8)')
            svg = png.with_suffix('.svg')
            if svg.exists() and 'foreignObject' in ler(svg): erro(f'{svg.relative_to(RAIZ)} tem <foreignObject> (C14.8)')
        agrupados = {uc: ' '.join(re.findall(rf'^- {uc}\b.*$', txt, re.M)) for uc in {f[0] for f in figs}}
        for uc in sorted({f[0] for f in figs}):
            if uc not in ucs: continue
            fontes = {re.sub(r'_\d{3}$', '', Path(c).stem) for u, _, _, c in figuras[uc]}
            pasta = (arq.parent / figuras[uc][0][3]).resolve().parent
            puml = ' '.join(ler(pasta / f'{f}.puml') for f in fontes)
            for f in ucs[uc][2]:
                fluxos += 1
                if not re.search(rf'\b{f}\b', puml) and not re.search(rf'\b{f}\b', agrupados.get(uc, '')):
                    faltam += 1; erro(f'{uc}: fluxo {f} não aparece no diagrama nem na lista de agrupados (C14.4)')
    areas_com = {a for a in areas if a.upper() not in pendentes}
    esperados = [u for u, (a, _, _) in sorted(ucs.items()) if a in areas_com]
    for u in esperados:
        if u not in figuras: erro(f'{u} sem diagrama de sequência (C14.1)')
    for a in (pendentes if completo else []): erro(f'área {a} sem diagramas (--completo)')
    if completo and len(figuras) != len(ucs): erro(f'{len(figuras)} casos de uso com diagrama, e o item 10 tem {len(ucs)} (C14.1)')
    nfig = sum(len(v) for v in figuras.values())
    print(f'{len([u for u in esperados if u in figuras])} de {len(ucs)} casos de uso com diagrama ({nfig} figuras) nas áreas '
          f'{", ".join(sorted(x.upper() for x in areas_com)) or "—"}; {fluxos - faltam} de {fluxos} fluxos alternativos e de exceção '
          'no diagrama ou agrupados' + (f'; áreas sem diagramas: {", ".join(pendentes)}' if pendentes else ''))
    for p in problemas: print('-', p)
    print(f'{len(problemas)} problema(s)')
    sys.exit(1 if problemas else 0)


if __name__ == '__main__':
    main()
