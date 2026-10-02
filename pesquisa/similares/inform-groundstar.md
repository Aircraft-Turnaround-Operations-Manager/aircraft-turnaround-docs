---
id: inform-groundstar
titulo: "Ficha — INFORM GroundStar"
tipo: similar-ficha
secao_original: "3.2"
itens_template: [3]
areas: []
decisoes: []
fontes: [43, 44, 45, 46, 47]
relacionados: [matriz-comparativa, lacunas-e-diferencial, similares]
status: vigente
atualizado: 2026-10-01
---
# Ficha 2 — INFORM GroundStar

> Base de conhecimento do projeto · origem: seção 3.2 do [relatório consolidado](../01-referencias-setor-e-similares.md) (congelado em 01/10/2026) · fontes numeradas em [fontes.md](../fontes.md) · convenções [Fato]/[Inferência] e índices no [mapa da pesquisa](../README.md).


| Campo | Registro |
|---|---|
| Produto e fornecedor | GroundStar (módulos citados: Planning/RealTime Staff & Equipment, Planning/RealTime Stands & Terminals, WorkforcePlus, TurnManager, TeamWork, myStaff, entre outros). INFORM GmbH, **Alemanha**. https://www.inform-software.com/en/software/groundstar [Fato][43][45][47] |
| Público-alvo | "airports, airlines, and ground handlers" [Fato][43]; para turnaround: "Airline turnaround managers", empresas de *ground handling* e gestores de linha de frente [Fato][44]. |
| Problema que resolve | Controle de pessoal, equipamentos, posições e terminais com "Digital Decision Making based on Artificial Intelligence and Operations Research" [Fato][43]. |
| Funcionalidades | Planejamento e despacho em tempo real de pessoal e equipamentos, com "Management by Exception" e integração móvel [Fato][45]; TurnManager — "Process Irregularities at a Glance" — detecta irregularidades do *handling* e calcula automaticamente o impacto "on dependent processes and flight delays" [Fato][45]; "Reliable target off-block time calculation", previsão de efeito dominó e identificação de gargalos [Fato][44]; GS TeamWork: visão por tarefa de voos, alocação de pessoal e capacidade, em app web "mobile-first" para gestores de linha de frente [Fato][46]; cenários "what-if" [Fato][47]. |
| Como trata atrasos e exceções | TurnManager calcula o impacto nos processos dependentes [Fato][45]; TeamWork avisa os funcionários sobre "delays or changes that may affect them" e aponta "overlapping deployment times or agents who have not been informed"; o gestor ajusta manualmente ou aceita a recomendação do sistema [Fato][46]. |
| Fonte do dado operacional | Programação de voos e atividades operacionais [Fato][44] e apps móveis dos funcionários [Fato][43][46]. Integração com AODB/A-CDM: não informado. |
| Métricas divulgadas — [Fato] (declarado pelo fornecedor) | "more than 200 installations worldwide" desde os anos 1990 [47]; nenhum ganho numérico nas páginas lidas. |
| Relação com A-CDM | Calcula TOBT ("Reliable target off-block time calculation") [Fato][44]. Se envia o TOBT ao A-CDM do aeroporto: não informado. |
| O que vale incorporar [Inferência] | (1) Propagação automática do impacto de um atraso para as tarefas dependentes; (2) gestão por exceção; (3) app para quem executa e para o gestor de linha de frente; (4) redistribuição feita pelo gestor, com sugestão do sistema. |
| O que fica fora do nosso escopo [Inferência] | Escala e jornada de trabalho (WorkforcePlus), planejamento sazonal de posições e terminais e modelagem de custos: são escala/planejamento e financeiro, que o projeto excluiu. |

---

## Ligações

- **Itens da especificação:** [Item 3 — Visão do Produto](../../especificacao/03-visao-do-produto.md)
- **Relacionados:** [matriz-comparativa](matriz-comparativa.md), [lacunas-e-diferencial](lacunas-e-diferencial.md), [similares](README.md)
- **Fontes citadas:** 43, 44, 45, 46, 47 (em [fontes.md](../fontes.md))
- **Contexto geral:** [CONTEXT.md](../../CONTEXT.md) · [mapa da pesquisa](../README.md)
