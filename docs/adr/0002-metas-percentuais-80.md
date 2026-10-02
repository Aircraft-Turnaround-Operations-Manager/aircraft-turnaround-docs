---
id: adr-0002
titulo: "ADR-0002 — Metas percentuais do item 1: 80%"
tipo: decisao
decisao: D2
status: aceita
data: 2026-10-01
decisor: Rodrigo Alves
itens_template: [1, 3]
areas: [C]
fontes: [7, 15, 16, 18]
relacionados: [metricas-item-1, tolerancias-e-indicadores, adr-0001]
---
# ADR-0002 — Metas percentuais do item 1: 80%

- **Status:** aceita · **Data:** 01/10/2026 · **Decisor:** Rodrigo Alves · **Origem:** decisão D2 do [relatório de pesquisa](../../pesquisa/01-referencias-setor-e-similares.md) (seção 5)

## Contexto

O objetivo 1 tinha duas metas de 95%: atividades dentro das janelas planejadas (M3) e turnarounds prontos até o horário planejado (M2).

- **Não confirmado:** meta pública oficial de percentual para a precisão do TOBT.
- **[Fato]** Heathrow considera "verde" a pontualidade quando "at least 79% of flights operated within 3 or 15 minutes of the scheduled time" [7].
- **[Fato]** Na aderência ao slot ATFM, as unidades ATS reportam quando a não aderência chega a 20% das partidas reguladas [15]. **[Inferência]** Equivale a ~80% de aderência, mas é outra métrica, usada só como analogia.
- **[Fato]** Pontualidade de partida na Europa em 2023: 67,9% dentro de 15 min [16]. Precisão do TOBT "less than 60%" em grandes aeroportos (declarado pelo fornecedor) [18].

## Opções consideradas

- **(a)** Manter 95%, declarando que é meta interna mais exigente que o setor.
- **(b)** Adotar 80%, alinhado às referências de mercado mais próximas.

## Decisão

**(b) 80%** para M2 (turnarounds prontos para liberação até o TOBT planejado + 5 min) e para M3 (atividades iniciadas e concluídas dentro das janelas planejadas). Motivo do Rodrigo: seguir o padrão de mercado, sem inventar um padrão próprio.

## Consequências

- Objetivo 1 e meta-valor da Visão do Produto (item 3) usam 80%.
- O texto deve citar a origem do número ([7] e, como analogia, [15]).
- As demais metas (100% das tarefas com responsável, 5 s, 90% dos alertas críticos com ação em 2 min, 0 liberações com pendência) seguem como metas internas do projeto.

---

## Ligações

- **Pesquisa:** [metricas-item-1](../../pesquisa/impacto/metricas-item-1.md), [tolerancias-e-indicadores](../../pesquisa/topicos/tolerancias-e-indicadores.md)
- **Itens da especificação:** [Item 1 — 3 Objetivos](../../especificacao/01-3-objetivos.md), [Item 3 — Visão do Produto](../../especificacao/03-visao-do-produto.md)
- **Outras decisões:** [D1](0001-referencia-horario-tobt-mais-5-min.md)
- **Fontes citadas:** 7, 15, 16, 18 (em [fontes.md](../../pesquisa/fontes.md))
- **Índice das decisões:** [README.md](README.md) · **Contexto geral:** [CONTEXT.md](../../CONTEXT.md)
