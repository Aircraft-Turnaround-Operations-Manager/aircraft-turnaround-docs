---
id: veovo
titulo: "Ficha — Veovo (A-CDM)"
tipo: similar-ficha
secao_original: "3.2"
itens_template: [3]
areas: []
decisoes: []
fontes: [18, 51, 52]
relacionados: [matriz-comparativa, lacunas-e-diferencial, similares]
status: vigente
atualizado: 2026-10-01
---
# Ficha 4 — Veovo (A-CDM)

> Base de conhecimento do projeto · origem: seção 3.2 do [relatório consolidado](../01-referencias-setor-e-similares.md) (congelado em 01/10/2026) · fontes numeradas em [fontes.md](../fontes.md) · convenções [Fato]/[Inferência] e índices no [mapa da pesquisa](../README.md).


| Campo | Registro |
|---|---|
| Produto e fornecedor | A-CDM, dentro da linha "Outstanding Operations" (com AODB e gestão de recursos). Veovo, parte do grupo Gentrack, sede em Auckland, **Nova Zelândia**. https://veovo.com/platform/acdm [Fato][51][52] |
| Público-alvo | Operadores de aeroporto [Fato][51]; "over 110 airports globally" (perfil do fornecedor) [Fato][52]. |
| Problema que resolve | Coordenar a operação com dados em tempo real e previsões, melhorando turnaround, congestionamento e pontualidade [Fato][51]; o fornecedor critica a dependência de TOBT estimado manualmente por "busy airline or ground staff" [Fato][18]. |
| Funcionalidades | "360 view of milestones" com marcos pré-partida e atualizações em tempo real; ícones dinâmicos de status do turn; previsão de in-block e off-block com aprendizado de máquina; sequenciamento pré-partida; portal web com acesso, visões e alertas configuráveis por papel e gestão de exceções [Fato][51]. |
| Como trata atrasos e exceções | Previsão de off-block por ML, alertas por papel e gestão de exceções [Fato][51]. |
| Fonte do dado operacional | AODB e histórico do aeroporto mais dados em tempo real [Fato][51]. Câmeras/sensores: não informado. |
| Métricas divulgadas — [Fato] (declarado pelo fornecedor) | "20% improvement" em previsões [51]; prever horários de bloco "to within one minute" [52]; até "90% accuracy" com ML contra menos de 60% do TOBT manual [18]. |
| Relação com A-CDM | É um produto de A-CDM (marcos e sequenciamento pré-partida) [Fato][51]. |
| O que vale incorporar [Inferência] | (1) Linha do tempo de marcos por turnaround; (2) ícones de status; (3) alertas e visões configuráveis por papel (casa com os perfis dos atores do projeto). |
| O que fica fora do nosso escopo [Inferência] | Sequenciamento pré-partida e TSAT (função de ATC/aeroporto; integração com ATC excluída); ML preditivo (pode ser evolução futura, não MVP). |

---

## Ligações

- **Itens da especificação:** [Item 3 — Visão do Produto](../../especificacao/03-visao-do-produto.md)
- **Relacionados:** [matriz-comparativa](matriz-comparativa.md), [lacunas-e-diferencial](lacunas-e-diferencial.md), [similares](README.md)
- **Fontes citadas:** 18, 51, 52 (em [fontes.md](../fontes.md))
- **Contexto geral:** [CONTEXT.md](../../CONTEXT.md) · [mapa da pesquisa](../README.md)
