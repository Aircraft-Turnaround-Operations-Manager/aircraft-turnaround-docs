---
id: matriz-comparativa
titulo: "Matriz comparativa (seção 3.3)"
tipo: similar-matriz
secao_original: "3.3"
itens_template: [3, 6]
areas: []
decisoes: [D9]
fontes: [39, 40, 41, 42, 43, 44, 45, 46, 48, 49, 51, 52, 54, 55]
relacionados: [similares, lacunas-e-diferencial]
status: vigente
atualizado: 2026-10-01
---
# Matriz comparativa (seção 3.3)

> Base de conhecimento do projeto · origem: seção 3.3 do [relatório consolidado](../01-referencias-setor-e-similares.md) (congelado em 01/10/2026) · fontes numeradas em [fontes.md](../fontes.md) · convenções [Fato]/[Inferência] e índices no [mapa da pesquisa](../README.md).

> **Decisões vigentes (prevalecem sobre o texto abaixo):** [D9 — Nome único: Coordenador de Turnaround](../../docs/adr/0009-nome-coordenador-de-turnaround.md).
>
> Linha de redistribuição com o nome vigente do ator (D9).


Legenda: ✔ = documentado na fonte · parcial = documentado em parte · ✘ = a fonte indica que não faz · n.i. = não informado nas fontes lidas. Todas as células são [Fato] no sentido de **declarações do fornecedor** na fonte indicada; a escolha entre ✔ e parcial é [Inferência].

| Capacidade do núcleo | Assaia | INFORM GroundStar | ADB SAFEGATE | Veovo | SITA |
|---|---|---|---|---|---|
| Orquestração do turnaround (plano de tarefas por turnaround, com responsável) | parcial — monitora, não atribui tarefas [40] | ✔ — alocação de tarefas e TurnManager [45][46] | parcial — acompanha a atividade do turn [48] | parcial — marcos do turn [51] | parcial — "turnaround management" no Mobile Resource Manager, sem detalhe [54] |
| Tarefas paralelas com dependências | parcial — regra "limpeza após desembarque" [42] | ✔ — impacto em "dependent processes" [45] | n.i. | n.i. | n.i. |
| Estados de tarefa / do turnaround | ✔ — status por atividade [40] | parcial — visão por tarefa [46] | parcial — block in/out e status do turn [49] | parcial — ícones de status [51] | n.i. |
| Cálculo de atraso / projeção de prontidão | ✔ — POBT e PRDT [40] | ✔ — TOBT e efeito dominó [44] | ✔ — prevê atraso e atualiza TOBT [48] | ✔ — previsão de off-block [51] | parcial — previsões de turnaround citadas em caso [55] |
| Caminho crítico explícito | n.i. | parcial — calcula impacto em dependentes, sem nomear caminho crítico [45] | n.i. | n.i. | n.i. |
| Painel em tempo real | ✔ [40] | ✔ [44] | ✔ [49] | ✔ [51] | ✔ [54] |
| Alertas | ✔ [40][42] | ✔ [46] | ✔ [49] | ✔ [51] | ✔ [54] |
| Redistribuição de recursos pelo Coordenador de Turnaround | n.i. — há produto "ResourceManager", sem detalhe [39] | ✔ — despacho em tempo real e TeamWork [45][46] | n.i. | parcial — gestão de recursos na plataforma [52] | ✔ — Mobile Resource Manager [54] |
| Liberação com bloqueio por pendência | n.i. | n.i. | n.i. | n.i. | n.i. |
| Entrada de dados pelo operador (app/web) | n.i. — dados principais vêm de câmeras [41] | ✔ — apps móveis [43][46] | parcial — acesso móvel; dados principais vêm de sensores [49] | parcial — portal web por papel [51] | n.i. |
| Integração com A-CDM | ✔ [39] | parcial — calcula TOBT [44] | ✔ [48][49] | ✔ [51] | ✔ [55] |

---

## Ligações

- **Decisões:** [D9](../../docs/adr/0009-nome-coordenador-de-turnaround.md)
- **Itens da especificação:** [Item 3 — Visão do Produto](../../especificacao/03-visao-do-produto.md), [Item 6 — Requisitos Funcionais](../../especificacao/06-requisitos-funcionais/00-item.md)
- **Relacionados:** [similares](README.md), [lacunas-e-diferencial](lacunas-e-diferencial.md)
- **Fontes citadas:** 39, 40, 41, 42, 43, 44, 45, 46, 48, 49, 51, 52, 54, 55 (em [fontes.md](../fontes.md))
- **Contexto geral:** [CONTEXT.md](../../CONTEXT.md) · [mapa da pesquisa](../README.md)
