"""Confere a coluna SPRINT do item 6 contra as dependências entre os RFs (critério C00.10, issue #140).

Um RF depende de outro quando usa dados ou comportamento que só o outro produz. Gatilhos a mais
(recalcular também quando outro RF acontece) não contam: são ligados na sprint do RF que dispara.
Uso: python scripts/verificar_sprints.py
"""
import glob
import sys

# RF: RFs de que ele depende, conforme o texto do RF no item 6
DEP = {
    1: [2], 2: [1, 5, 9, 37], 3: [1], 4: [9], 5: [2, 3, 4, 6, 8, 9, 11], 6: [3, 4, 7, 8, 11], 7: [4], 8: [4, 11],
    9: [1, 5], 10: [3, 12], 11: [1],
    12: [5, 21], 13: [12], 14: [5, 21], 15: [5, 21], 16: [15, 19], 17: [15], 18: [4, 5], 19: [7, 15],
    20: [4, 15, 16, 18], 21: [5, 8, 12, 15, 16, 18], 44: [39],
    22: [5, 13, 15, 16, 17, 21], 23: [22], 24: [22], 25: [3, 22, 33], 26: [17, 18, 20, 23, 24, 39, 44],
    27: [21], 28: [22, 24], 29: [3, 10], 30: [3, 20], 31: [3, 21, 39], 32: [3, 5, 21],
    33: [24, 27, 28, 29, 30, 31], 34: [15, 16, 21, 33, 38, 41, 44], 35: [32],
    36: [5, 21], 37: [21, 43], 38: [33, 36, 37, 41, 42], 39: [21, 36, 40], 40: [21, 36], 41: [22],
    42: [4, 8, 11, 21], 43: [2, 9, 16, 21],
}
# Dependências desenvolvidas com dados simulados no formato do contrato combinado na sprint 2,
# justificadas no texto do item 6 e mostradas no quadro de sprints do RA2
SIMULADO = {
    (2, 5), (2, 37), (9, 5),  # recusa da desativação com tarefa pendente
    (12, 5), (14, 5), (15, 5), (18, 4), (18, 5), (19, 7), (21, 5), (21, 8), (36, 5),  # plano e modelo
    (22, 5), (22, 13), (22, 17),  # projeção antes do plano, da correção da chegada e da pausa
    (29, 10),  # viabilidade antes da atualização de EIBT e MTTT
}
SERVICO = {'a': 'Cadastro e Planejamento', 'b': 'Execução em Solo', 'c': 'Monitoramento', 'd': 'Exceções e Liberação'}

sprint, servico = {}, {}
for f in sorted(glob.glob('especificacao/06-requisitos-funcionais/area-*.md')):
    for l in open(f, encoding='utf-8'):
        if l.startswith('| RF-'):
            c = [x.strip() for x in l.strip().strip('|').split('|')]
            n = int(c[0][3:])
            sprint[n], servico[n] = int(c[5]), SERVICO[f[-4]]

erros = []
if sorted(sprint) != list(range(1, 45)): erros.append('faltam RFs na tabela')
if sorted(DEP) != list(range(1, 45)): erros.append('faltam RFs no mapa de dependências')
for n, ds in DEP.items():
    for d in ds:
        if sprint.get(d, 0) > sprint.get(n, 0) and (n, d) not in SIMULADO:
            erros.append(f'RF-{n} (sprint {sprint.get(n)}) depende do RF-{d} (sprint {sprint.get(d)})')
for n, d in SIMULADO:
    if sprint[d] <= sprint[n]: erros.append(f'RF-{n}: simulação desnecessária, o RF-{d} já vem antes')

for s in range(1, 9):
    por = {}
    for n in sorted(k for k in sprint if sprint[k] == s): por.setdefault(servico[n], []).append(f'RF-{n}')
    print(f'Sprint {s}: ' + ('; '.join(f'{k}: {", ".join(v)}' for k, v in por.items()) or '(sem RF)'))
print(f'{sum(len(v) for v in DEP.values())} dependências, {len(SIMULADO)} com dados simulados, {len(erros)} erros')
for n, d in sorted(SIMULADO): print(f'  simulada: RF-{n} (sprint {sprint[n]}) usa o RF-{d} (sprint {sprint[d]})')
for e in erros: print('ERRO:', e)
sys.exit(1 if erros else 0)
