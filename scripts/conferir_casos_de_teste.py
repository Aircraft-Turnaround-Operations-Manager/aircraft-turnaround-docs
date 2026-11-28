"""Confere a planilha de casos de teste do item 15 (especificacao/15-casos-de-teste/area-a.md a area-d.md).

O que confere (entregas/ra2-criterios-de-aceite.md, seção do item 15):
  C15.1  cabeçalho com as 9 colunas, nesta ordem, em toda tabela; toda linha com 9 células; ID no formato
         provisório da área (CT-A001…, ADR-0022) ou final (CT-001…), sem repetição; o caso de uso da linha é o da
         seção "## UCnn – <nome>", e o nome da seção é o do item 10
  C15.2  todo critério de aceite das estórias (USnnn-CAn, item 7) é citado por pelo menos um caso de teste, e todo
         caso de teste cita pelo menos um critério, todos existentes
  C15.3  para cada caso de uso com casos de teste, o fluxo básico (FPn) e cada fluxo alternativo e de exceção do
         item 10 (An.m, En.m) aparecem na coluna "Cenário" de pelo menos um caso de teste daquele caso de uso
  C15.5  os passos de cada caso de teste são numerados em sequência (1., 2., …)
Áreas ainda sem caso de teste aparecem como pendentes e, sem --completo, não contam como problema.

Uso: python scripts/conferir_casos_de_teste.py [--area c] [--completo]
  --area x     confere só a área x (C15.2 e C15.3 só para os critérios e casos de uso dela)
  --completo   exige as quatro áreas com casos de teste (consolidação da T15, #147)
Sai com código 1 se houver problema.
"""
import re, sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
ESP = RAIZ / 'especificacao'
AREAS = 'abcd'
COLUNAS = ['ID', 'Caso de uso', 'Cenário', 'Estória e critério de aceite', 'Caso de teste', 'Pré-condições',
           'Dados de entrada', 'Passos', 'Resultado esperado']
problemas = []


def erro(msg): problemas.append(msg)
def ler(p): return p.read_text(encoding='utf-8') if p.exists() else ''
def celulas(ln): return [c.strip() for c in ln.strip().strip('|').split('|')]


def item10():
    """{UCnn: (área, nome, [fluxos alternativos e de exceção])}"""
    ucs = {}
    for a in AREAS:
        partes = re.split(r'^## (UC\d+)\s*[–-]\s*(.+?)\s*$', ler(ESP / '10-especificacoes-de-caso-de-uso' / f'area-{a}.md'), flags=re.M)
        for i in range(1, len(partes), 3):
            ucs[partes[i]] = (a, partes[i + 1], re.findall(r'^### Fluxo (?:alternativo|de exceção) ([AE]\d+)', partes[i + 2], re.M))
    return ucs


def item7():
    """{USnnn-CAn: área}"""
    cas = {}
    for a in AREAS:
        partes = re.split(r'^## (US\d+)\b.*$', ler(ESP / '07-estorias-de-usuario' / f'area-{a}.md'), flags=re.M)
        for i in range(1, len(partes), 2):
            for n in re.findall(r'^\| (\d+) \| ', partes[i + 1], re.M): cas[f'{partes[i]}-CA{n}'] = a
    return cas


def planilha(a, ucs):
    """Lista de casos de teste da área: dicionários com id, uc, cenario, cas, passos e o local."""
    arq = ESP / '15-casos-de-teste' / f'area-{a}.md'
    cts, secao, cab_ok = [], None, False
    for n, ln in enumerate(ler(arq).splitlines(), 1):
        m = re.match(r'^## (UC\d+)\s*[–-]\s*(.+?)\s*$', ln)
        if m:
            secao, cab_ok = m.group(1), False
            if secao not in ucs: erro(f'{arq.name}:{n}: {secao} não existe no item 10')
            elif m.group(2) != ucs[secao][1]: erro(f'{arq.name}:{n}: nome da seção diferente do item 10: "{m.group(2)}" × "{ucs[secao][1]}"')
            continue
        if ln.startswith('## '): secao = None; continue
        if not ln.startswith('|') or not secao: continue
        c = celulas(ln)
        if c[0] == 'ID':
            cab_ok = c == COLUNAS
            if not cab_ok: erro(f'{arq.name}:{n}: cabeçalho diferente das 9 colunas do C15.1')
            continue
        if re.fullmatch(r':?-+:?', c[0]): continue
        local = f'{arq.name}:{n}'
        if not cab_ok: erro(f'{local}: linha sem o cabeçalho do C15.1 antes')
        if len(c) != 9: erro(f'{local}: {len(c)} células (C15.1 pede 9)'); continue
        if not re.fullmatch(rf'CT-(?:{a.upper()}\d{{3}}|\d{{3}})', c[0]): erro(f'{local}: ID fora do formato: {c[0]}')
        if c[1] != secao: erro(f'{local}: {c[0]} diz {c[1]} na seção do {secao}')
        cts.append({'id': c[0], 'uc': secao, 'cenario': c[2], 'cas': re.findall(r'US\d+-CA\d+', c[3]),
                    'passos': c[7], 'local': local})
    return cts


def main():
    so = sys.argv[sys.argv.index('--area') + 1].lower() if '--area' in sys.argv else None
    completo = '--completo' in sys.argv
    ucs, cas = item10(), item7()
    areas = [so] if so else list(AREAS)
    todos, pendentes = [], []
    for a in areas:
        cts = planilha(a, ucs)
        if not cts: pendentes.append(a.upper()); continue
        todos += cts
    vistos = {}
    for ct in todos:  # C15.1: ID único
        if ct['id'] in vistos: erro(f"{ct['local']}: {ct['id']} repetido (também em {vistos[ct['id']]})")
        vistos.setdefault(ct['id'], ct['local'])
    # C15.2
    citados = {x for ct in todos for x in ct['cas']}
    for ct in todos:
        if not ct['cas']: erro(f"{ct['local']}: {ct['id']} sem critério de aceite (C15.2)")
        for x in ct['cas']:
            if x not in cas: erro(f"{ct['local']}: {ct['id']} cita critério inexistente {x} (C15.2)")
    areas_com = {a for a in areas if a.upper() not in pendentes}
    sem = [x for x, a in cas.items() if a in areas_com and x not in citados]
    for x in sem: erro(f'{x} sem caso de teste (C15.2)')
    # C15.3
    fluxos = faltam = 0
    for u, (a, nome, fl) in sorted(ucs.items()):
        if a not in areas_com: continue
        cen = ' '.join(ct['cenario'] for ct in todos if ct['uc'] == u)
        if not cen: erro(f'{u} sem caso de teste (C15.3)'); continue
        if not re.search(r'\bFP\d', cen): erro(f'{u}: fluxo básico sem caso de teste (C15.3)')
        for f in fl:
            fluxos += 1
            if not re.search(rf'\b{f}\.\d', cen): faltam += 1; erro(f'{u}: fluxo {f} sem caso de teste (C15.3)')
    # C15.5
    for ct in todos:
        nums = [int(x) for x in re.findall(r'(?:^|<br>)\s*(\d+)\.\s', ct['passos'])]
        if not nums or nums != list(range(1, len(nums) + 1)):
            erro(f"{ct['local']}: {ct['id']} com passos sem numeração em sequência (C15.5)")
    if completo:
        for a in pendentes: erro(f'área {a} sem casos de teste (--completo)')
    total_cas = sum(1 for a in cas.values() if a in areas_com)
    print(f'{len(todos)} casos de teste nas áreas {", ".join(sorted(x.upper() for x in areas_com)) or "—"}; '
          f'{total_cas - len(sem)} de {total_cas} critérios cobertos; {fluxos - faltam} de {fluxos} fluxos alternativos '
          f'e de exceção cobertos' + (f'; áreas sem casos de teste: {", ".join(pendentes)}' if pendentes else ''))
    for p in problemas: print('-', p)
    print(f'{len(problemas)} problema(s)')
    sys.exit(1 if problemas else 0)


if __name__ == '__main__':
    main()
