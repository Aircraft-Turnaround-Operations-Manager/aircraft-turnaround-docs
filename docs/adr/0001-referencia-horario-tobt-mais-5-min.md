---
id: adr-0001
titulo: "ADR-0001 — Referência de horário: TOBT planejado + 5 min, unilateral"
tipo: decisao
decisao: D1
status: aceita
data: 2026-10-01
decisor: Rodrigo Alves
itens_template: [1, 6, 7, 8, 10]
areas: [C]
fontes: [2, 3, 4, 7, 8, 9, 10, 11, 12, 62]
relacionados: [tolerancias-e-indicadores, metricas-item-1, marcos-e-horarios, adr-0002, adr-0003]
---
# ADR-0001 — Referência de horário: TOBT planejado + 5 min, unilateral

- **Status:** aceita · **Data:** 01/10/2026 · **Decisor:** Rodrigo Alves · **Origem:** decisão D1 do [relatório de pesquisa](../../pesquisa/01-referencias-setor-e-similares.md) (seção 5)

## Contexto

O objetivo 1 media "turnarounds prontos para liberação até o horário planejado, com tolerância máxima de 5 minutos", sem dizer qual horário.

- **[Fato]** No A-CDM, a prontidão é medida contra o **TOBT** (*Target Off-Block Time*, horário-alvo em que a aeronave fica pronta), mantido pela companhia aérea ou pelo *ground handler* [2][4].
- **[Fato]** A Especificação da EUROCONTROL avisa o responsável quando a prontidão não foi registrada até **TOBT + 5 min** [2].
- **[Fato]** Seis aeroportos usam 5 min como janela de prontidão ou limiar de atualização do TOBT [7]–[12].
- **[Inferência]** O SOBT mistura o turnaround com atrasos de chegada e de ATC, que o sistema não controla.

## Opções consideradas

- **(a)** TOBT planejado (horário-alvo de prontidão).
- **(b)** SOBT (horário programado de saída).

## Decisão

**(a) TOBT planejado + 5 min, unilateral.** Só o atraso conta: ficar pronto antes não é desvio negativo (ver [ADR-0003](0003-atualizar-previsao-na-antecipacao.md) para o tratamento da antecipação).

## Consequências

- O objetivo 1 passa a dizer "prontos para liberação até o horário-alvo de prontidão planejado (TOBT), com tolerância máxima de 5 minutos".
- O turnaround guarda o TOBT planejado, e o estado "Pronto para liberação" é comparado a ele.
- O Motor de Eventos alerta quando a prontidão não foi registrada até TOBT + 5 min.
- RNF de precisão de horário: minuto completo, com a convenção "5:59 is acceptable while 6:00 is not" [3].
- **[Fato][62]** Para a ANAC, "O registro dos motivos e tempos de atraso deve utilizar como referência o horário de partida previsto do voo" (Portaria nº 55/2026, art. 2º, § 3º; leitura registrada em [Códigos de atraso](../../pesquisa/topicos/codigos-de-atraso.md)). As duas réguas convivem: o TOBT mede a prontidão do turnaround; o código da ANAC explica o atraso do voo.

---

## Ligações

- **Pesquisa:** [tolerancias-e-indicadores](../../pesquisa/topicos/tolerancias-e-indicadores.md), [metricas-item-1](../../pesquisa/impacto/metricas-item-1.md), [marcos-e-horarios](../../pesquisa/topicos/marcos-e-horarios.md)
- **Itens da especificação:** [Item 1 — 3 Objetivos](../../especificacao/01-3-objetivos.md), [Item 6 — Requisitos Funcionais](../../especificacao/06-requisitos-funcionais/00-item.md), [Item 7 — Estórias de Usuário](../../especificacao/07-estorias-de-usuario/00-item.md), [Item 8 — Requisitos Não Funcionais](../../especificacao/08-requisitos-nao-funcionais/00-item.md), [Item 10 — Especificações de Caso de Uso](../../especificacao/10-especificacoes-de-caso-de-uso/00-item.md)
- **Outras decisões:** [D2](0002-metas-percentuais-80.md), [D3](0003-atualizar-previsao-na-antecipacao.md)
- **Fontes citadas:** 2, 3, 4, 7, 8, 9, 10, 11, 12, 62 (em [fontes.md](../../pesquisa/fontes.md))
- **Índice das decisões:** [README.md](README.md) · **Contexto geral:** [CONTEXT.md](../../CONTEXT.md)
