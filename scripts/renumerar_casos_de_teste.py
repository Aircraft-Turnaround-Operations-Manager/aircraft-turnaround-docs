"""Renumeração única dos casos de teste do item 15 (ADR-0022, pontos 2 a 4).

Troca os IDs provisórios por área (CT-A001, CT-B001, CT-C001, CT-D001…) por uma sequência única CT-001…, sem
lacunas, na ordem em que os casos de teste aparecem no documento: por caso de uso (UC01 a UC37, como o gerador põe o
item 15) e, dentro de cada caso de uso, na ordem da planilha. O UC37, da área B, vem depois do UC36.
Troca o ID em todo arquivo .md e .puml de especificacao/ (planilhas, matriz e qualquer citação), fora dos comentários HTML, e grava a
correspondência em entregas/ra2-renumeracao.md. Não mexe no CHANGELOG, na pesquisa nem nas ADRs, que guardam o
histórico com os IDs provisórios; a tabela de correspondência permite consultá-los.

Uso: python scripts/renumerar_casos_de_teste.py [--conferir]
  --conferir  mostra o que seria feito e confere a base, sem gravar nada
Falha, sem gravar nada, se alguma das quatro áreas não tiver casos de teste, se algum ID já for final, se houver ID
repetido ou se algum arquivo citar um ID provisório que não está em nenhuma planilha. Depois de rodar, gere a matriz
de novo (python scripts/gerar_matriz_rastreabilidade.py) e confira (python scripts/conferir_casos_de_teste.py --completo).
"""
import re, subprocess, sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
ESP = RAIZ / 'especificacao'
DESTINO = RAIZ / 'entregas' / 'ra2-renumeracao.md'
AREAS = 'abcd'
PROVISORIO = re.compile(r'\bCT-[A-D]\d{3}\b')
COMENTARIO = re.compile(r'(<!--.*?-->)', re.S)  # comentários HTML (instruções de formato) ficam como estão


def ler(p): return p.read_text(encoding='utf-8') if p.exists() else ''


def fora_de_comentario(texto, fn):
    """Aplica fn só aos trechos fora dos comentários HTML."""
    return ''.join(t if COMENTARIO.fullmatch(t) else fn(t) for t in COMENTARIO.split(texto))


def casos_por_uc():
    """[(UCnn, área, CT-X000)] na ordem das planilhas."""
    out = []
    for a in AREAS:
        uc = None
        for ln in ler(ESP / '15-casos-de-teste' / f'area-{a}.md').splitlines():
            m = re.match(r'^## (UC\d+)\b', ln)
            if m: uc = m.group(1); continue
            m = re.match(r'^\| (CT-[^ |]+) \|', ln)
            if m and uc: out.append((uc, a.upper(), m.group(1)))
    return out


def main():
    conferir = '--conferir' in sys.argv
    casos = casos_por_uc()
    falhas = []
    vazias = [a.upper() for a in AREAS if not any(c[1] == a.upper() for c in casos)]
    if vazias: falhas.append(f'áreas sem casos de teste: {", ".join(vazias)} (a ADR-0022 renumera só com as quatro na main)')
    finais = [c[2] for c in casos if not PROVISORIO.fullmatch(c[2])]
    if finais: falhas.append(f'IDs que não são provisórios: {", ".join(finais[:5])}{"…" if len(finais) > 5 else ""}')
    ids = [c[2] for c in casos]
    rep = sorted({x for x in ids if ids.count(x) > 1})
    if rep: falhas.append(f'IDs repetidos: {", ".join(rep)}')
    # ordem do documento: caso de uso e, dentro dele, a ordem da planilha (sorted é estável)
    ordem = sorted(casos, key=lambda c: int(c[0][2:]))
    largura = max(3, len(str(len(ordem))))
    mapa = {c[2]: f'CT-{n:0{largura}d}' for n, c in enumerate(ordem, 1)}
    arquivos = sorted(list(ESP.rglob('*.md')) + list(ESP.rglob('*.puml')))
    for p in arquivos:
        orfaos = set(PROVISORIO.findall(COMENTARIO.sub('', ler(p)))) - mapa.keys()
        if orfaos: falhas.append(f'{p.relative_to(RAIZ)} cita ID sem caso de teste: {", ".join(sorted(orfaos))}')
    print(f'{len(ordem)} casos de teste: ' + ', '.join(f'{a} {sum(1 for c in casos if c[1] == a)}' for a in 'ABCD')
          + (f'; {ordem[0][2]} → {mapa[ordem[0][2]]} … {ordem[-1][2]} → {mapa[ordem[-1][2]]}' if ordem else ''))
    if falhas:
        for f in falhas: print('-', f)
        sys.exit('Nada foi gravado.' if not conferir else 1)
    alterados = []
    for p in arquivos:
        velho = ler(p); novo = fora_de_comentario(velho, lambda t: PROVISORIO.sub(lambda m: mapa[m[0]], t))
        if novo != velho: alterados.append(p.relative_to(RAIZ)); conferir or p.write_text(novo, encoding='utf-8')
    if conferir:
        print('Arquivos que mudariam:', ', '.join(map(str, alterados)) or 'nenhum'); return
    base = subprocess.run(['git', 'rev-parse', '--short', 'HEAD'], cwd=RAIZ, capture_output=True, text=True).stdout.strip() or '?'
    linhas = ['# Renumeração definitiva dos casos de teste — ADR-0022', '',
              f'Base: main `{base}`, com as quatro áreas do item 15 integradas. Ordem do documento: por caso de uso (UC01 a UC37) e, '
              'dentro de cada caso de uso, na ordem da planilha. O CHANGELOG, a pesquisa e as ADRs conservam os IDs provisórios; '
              'esta tabela permite consultá-los.', '', '| Caso de uso | Área | Provisório | Final |', '|---|---|---|---|']
    linhas += [f'| {uc} | {a} | {ct} | {mapa[ct]} |' for uc, a, ct in ordem]
    DESTINO.write_text('\n'.join(linhas) + '\n', encoding='utf-8')
    print('Renumerados', len(mapa), 'casos de teste em', len(alterados), 'arquivo(s); correspondência em', DESTINO.relative_to(RAIZ))


if __name__ == '__main__':
    main()
