# Verificação do item 10 — issue #11

Base da revisão: `main` em `4c8b136` (diagrama integrado pela PR #106). A verificação cobre as especificações consolidadas e suas ligações com RFs, estórias, RNFs, diagrama e ADRs. O fechamento administrativo depende da aprovação por outro integrante e do merge da PR desta tarefa, conforme o README e a definição de pronto da issue #11.

## Evidência por critério

Os caminhos abaixo são relativos à raiz do repositório. As quatro áreas ficam em `especificacao/10-especificacoes-de-caso-de-uso/area-{a,b,c,d}.md`.

| ID | Status | Evidência |
|---|---|---|
| C10.1 | Atendido | 37 especificações contadas: A13, B8, C7, D9; mínimo total 16 e mínimo por área 4. |
| C10.2 | Atendido | 37/37 contêm nome, atores, descrição, pré-condições, pós-condições, regras, protótipos e três tipos de fluxo: dez campos. |
| C10.3 | Atendido | 42 PNGs referenciados e inspecionados visualmente: A14, B11, C7, D10; todos os 37 casos possuem protótipo de alta fidelidade. |
| C10.4 | Atendido | 37 fluxos básicos com passos consecutivos e resultado definido; UC-B8 A8 completa a propagação após replanejamento. |
| C10.5 | Atendido | 119 fluxos alternativos, pelo menos um em cada UC; variações de seleção, desistência e eventos do Motor de Eventos. |
| C10.6 | Atendido | 122 fluxos de exceção, pelo menos um em cada UC; UC-D7 E7 cobre referências inválidas sem alterar o plano. |
| C10.7 | Atendido | Passagem textual de todos os UCs: entradas, validações, estados, horários, registros e resultados observáveis. UC-B7 E1 preserva horário da ação e só grava marco aplicável. |
| C10.8 | Atendido | 37 nomes, 39 associações de atores, 10 include e 8 extend correspondem à fonte `especificacao/diagramas/09-casos-de-uso.puml` e ao diagrama integrado. A autenticação generaliza os quatro perfis humanos. |
| C10.9 | Atendido | RFs e estórias das quatro áreas revisados; corrigidos propagação, projeção pré-chegada, fontes do TOBT vigente, duplicação de alertas, cobertura dos alertas tratados e validação de dependências. US-A13 critério 6 cobre correção em Liberado sem recálculo. |
| C10.10 | Atendido | 37/37 citam os RFs atendidos nas regras ou nos fluxos; cobertura dos 44 RFs. |
| X.8 | Atendido | A13/B8/C7/D9, todos ≥4. |
| X.9 | Atendido | Campo PRODUTO do `00-item.md`: Aircraft Turnaround Orchestration System. |
| K.1 | Atendido no escopo | Atores do item 10 correspondem ao item 5 e ao diagrama integrado; a conferência global das raias do item 11 pertence à revisão final. |
| K.2 | Atendido | 44 RFs e 44 estórias; exatamente uma estória por RF e nenhum ID inexistente. Apêndice A, seção A.1. |
| K.3 | Atendido | Todos os 44 RFs cobertos pelos 37 casos do diagrama; requisitos relacionados da área C agrupados. Apêndice A, seção A.1. |
| K.4 | Atendido | Correspondência integral entre os 37 títulos e a fonte PlantUML do item 9. |
| K.5 | Atendido | Critérios de aceite cruzados com regras e fluxos; US-A13 contempla Liberado conforme RF-A13 e ADR-0013. |
| K.6 | Atendido | Objetivos 1–3 cobertos pelos RFs na seção A.2 da matriz e refletidos nas expectativas da Visão; os UCs preservam metas de 80%, atualização em 5 s e ação em 2 min para 90% dos alertas críticos. |
| K.7 | Atendido | Item 2 cruzado com os UCs: programação recebida como entrada, ATC externo, liberação humana, sem faturamento nem escala de pessoal. |
| K.9 | Atendido | Contagem real: 44 RFs, 44 estórias, 24 RNFs, 37 UCs; todas as estórias têm pelo menos dois critérios. |
| K.11 | Atendido no item 10 | Conferência contra CONTEXT e ADRs; siglas expandidas no início do item e fontes numéricas. Preservados TOBT planejado/vigente, chegada direta, código ANAC por sigla, abastecimento por companhia, serviços sob demanda e liberação interna. |
| K.12 | Atendido | Consulta `gh issue list --state open --label pendencia-cruzada --json number,title` retornou `[]`; dependências #8/#10 e tarefas das áreas #27–#30 fechadas. |

## Verificação executada

- Comandos de contagem reproduzíveis: `rg -c "^## UC-" especificacao/10-especificacoes-de-caso-de-uso -g "area-*.md"`, `rg -c "^### Fluxo alternativo" especificacao/10-especificacoes-de-caso-de-uso -g "area-*.md"` e `rg -c "^### Fluxo de exceção" especificacao/10-especificacoes-de-caso-de-uso -g "area-*.md"`.
- Contagem dos cabeçalhos `## UC-` por área, dos sete campos em tabela e das seções de fluxo; validação dos números consecutivos dos fluxos básicos.
- Conferência de existência das 42 imagens referenciadas e inspeção visual individual.
- Comparação de títulos, atores e relacionamentos das tabelas de cada área com a fonte PlantUML integrada; inspeção do diagrama na revisão da base.
- Leitura dos RFs, estórias e ADRs ligados pelo grafo. O grafo informa `built_at_commit=d8cbc67`, anterior ao diagrama integrado; as decisões foram tomadas pelos Markdown atuais.
- `python scripts/gerar_matriz_rastreabilidade.py`: **44 RFs, 24 RNFs, 44 estórias, 37 casos de uso, 0 lacunas**. Nova execução produz conteúdo idêntico ao Apêndice A versionado.
- Auditoria de links locais e referências: nenhum link quebrado, nenhum ID desconhecido, nenhuma duplicidade de estória; mínimo de dois critérios em cada estória.
- `git diff --check`: sem erro.
- Segunda passagem por revisores independentes: área A (13 UCs/14 imagens), B (8/11), C (7/7), D (9/10); achados devolvidos à escrita e conferidos depois das correções.

## Limites desta consolidação

IDs por área permanecem provisórios, conforme ADR-0011. Renumeração, atualização dos diagramas com os IDs finais e regeneração definitiva da matriz (K.13) pertencem à issue #13. Diagramas de atividades pertencem à #12. Capa, sumário, paginação e legibilidade no PDF final pertencem às #13/#14; este relatório não certifica esses critérios globais.

As barras dos protótipos podem usar a marca visual abreviada. Isso não altera o nome canônico nos campos PRODUTO. As versões v2 dos protótipos UC-C2 e UC-D4 corrigem, respectivamente, código ANAC/atraso/legenda dos marcos e correspondência entre o resumo de tarefas e a tarefa não aplicável. Os originais permanecem preservados, mas as especificações referenciam as versões corrigidas.
