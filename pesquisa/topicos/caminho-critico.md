---
id: caminho-critico
titulo: "Caminho crítico do turnaround (P1.6)"
tipo: pesquisa-topico
secao_original: "2.6"
itens_template: [4, 6, 10, 11]
areas: [C]
decisoes: [D5]
fontes: [4, 20, 21, 22, 24, 45]
relacionados: [atividades-e-dependencias, previsibilidade-vs-velocidade, lacunas-e-diferencial]
status: vigente
atualizado: 2026-10-01
---
# Caminho crítico do turnaround (P1.6)

> Base de conhecimento do projeto · origem: seção 2.6 do [relatório consolidado](../01-referencias-setor-e-similares.md) (congelado em 01/10/2026) · fontes numeradas em [fontes.md](../fontes.md) · convenções [Fato]/[Inferência] e índices no [mapa da pesquisa](../README.md).

> **Decisões vigentes (prevalecem sobre o texto abaixo):** [D5 — Abastecimento com passageiros a bordo: regra configurável por operador](../../docs/adr/0005-abastecimento-com-passageiros-configuravel.md).
>
> Como o abastecimento com passageiros é regra configurável (D5), o caminho crítico depende dessa configuração e precisa ser recalculado a cada evento.


- **[Fato][24]** Definição usada na literatura de turnaround: as atividades do caminho crítico são aquelas em que "any delay in them would increase the total time of the project". No modelo de Sanz de Vicente (2010), o caminho crítico passa por desembarque, limpeza, carregamento e embarque.
- **[Fato][20][21]** O embarque aparece como atividade crítica: "boarding is on the critical path of the aircraft 4D trajectory and not controlled by the operators" (Schultz, 2018); "Boarding is one of the most critical parts of the ground handling [...] as it lies on the critical path of the turnaround process" (Płanda e Skorupski, 2025).
- **[Fato][20]** Schultz liga caminho crítico e previsão: para um TOBT confiável, "the critical path of the turnaround has to be under the control of the operational entities"; e "The stochastic and passenger-controlled progress of aircraft boarding makes it difficult to reliably predict the turnaround time".
- **[Fato][22]** Kierzkowski et al. (2025), com o método PERT, encontram o caminho crítico "A, B, C, D, E, F, L" com 21,3 min, e observam que, nos cenários otimista e mais provável, "the longest activity is related to refuelling the aircraft". *A correspondência exata letra → atividade não foi confirmada na leitura.*
- **[Fato][45]** No mercado, o módulo TurnManager do INFORM GroundStar calcula "automatically" o impacto de uma irregularidade "on dependent processes and flight delays".
- **[Inferência]** Leitura para o projeto:
  - O caminho crítico típico é a cadeia de **passageiros e cabine**: desembarque → limpeza (e catering) → embarque → fechamento de portas. Bagagem, água/lavatório e inspeção costumam ter folga.
  - O abastecimento entra no caminho crítico quando o operador **não** permite abastecer com passageiros, porque passa a ficar entre desembarque e embarque.
  - O caminho crítico muda durante o turnaround: tarefa marcada "Não aplicável", tarefa atrasada ou regra de abastecimento alteram a cadeia mais longa. Por isso ele precisa ser **recalculado a cada evento**, e não fixado no planejamento.
  - O MTTT (tempo mínimo de turnaround) do A-CDM [4] é, na prática, a duração do caminho crítico nominal; é o parâmetro natural para a checagem de viabilidade EIBT + MTTT ≤ TOBT (T11).

---

## Ligações

- **Decisões:** [D5](../../docs/adr/0005-abastecimento-com-passageiros-configuravel.md)
- **Itens da especificação:** [Item 4 — Mapeamento de Negócios (BPMN TO BE)](../../especificacao/04-mapeamento-de-negocios.md), [Item 6 — Requisitos Funcionais](../../especificacao/06-requisitos-funcionais/00-item.md), [Item 10 — Especificações de Caso de Uso](../../especificacao/10-especificacoes-de-caso-de-uso/00-item.md), [Item 11 — Diagrama de Atividades](../../especificacao/11-diagrama-de-atividades.md)
- **Áreas do plano RA1:** [Área C — Monitoramento](../../especificacao/06-requisitos-funcionais/area-c.md) (divisão em [entregas/ra1-tarefas.md](../../entregas/ra1-tarefas.md), tabela 1.2)
- **Relacionados:** [atividades-e-dependencias](atividades-e-dependencias.md), [previsibilidade-vs-velocidade](previsibilidade-vs-velocidade.md), [lacunas-e-diferencial](../similares/lacunas-e-diferencial.md)
- **Fontes citadas:** 4, 20, 21, 22, 24, 45 (em [fontes.md](../fontes.md))
- **Contexto geral:** [CONTEXT.md](../../CONTEXT.md) · [mapa da pesquisa](../README.md)
