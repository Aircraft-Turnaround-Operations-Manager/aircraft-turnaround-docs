---
id: adr-0008
titulo: "ADR-0008 — Siglas do A-CDM com nome em português"
tipo: decisao
decisao: D8
status: aceita
data: 2026-10-01
decisor: Rodrigo Alves
itens_template: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
areas: [A, B, C, D]
fontes: [2, 4]
relacionados: [marcos-e-horarios, a-cdm]
---
# ADR-0008 — Siglas do A-CDM com nome em português

- **Status:** aceita · **Data:** 01/10/2026 · **Decisor:** Rodrigo Alves · **Origem:** decisão D8 do [relatório de pesquisa](../../pesquisa/01-referencias-setor-e-similares.md) (seção 5)

## Contexto

- **[Fato]** O A-CDM define marcos e horários com siglas próprias (AIBT, ACGT, ASBT, AEGT, ARDT, AOBT, TOBT, TSAT, MTTT, EIBT) [2][4].
- **[Inferência]** Um vocabulário comum evita que cada área do plano RA1 invente nomes diferentes para o mesmo evento e mostra embasamento no setor.

## Opções consideradas

- **(a)** Usar as siglas do A-CDM com o nome em português.
- **(b)** Usar só nomes em português.

## Decisão

**(a).** As siglas são usadas com o nome em português na primeira ocorrência de cada item da especificação.

**Complemento (07/10/2026).** A regra vale para **toda** sigla usada na especificação, e não só para as de marcos e horários: inclui a própria A-CDM e as de órgãos e normas (por exemplo, ANAC, IATA e ISO/IEC). O formato é "nome em português (SIGLA)", também nas regras de negócio; depois da primeira ocorrência no item, usa-se só a sigla.

## Consequências

- Glossário curto no [CONTEXT.md](../../CONTEXT.md); glossário completo em [Marcos e horários](../../pesquisa/topicos/marcos-e-horarios.md).
- Não criar siglas novas; se faltar um termo, usar o nome em português.

---

## Ligações

- **Pesquisa:** [marcos-e-horarios](../../pesquisa/topicos/marcos-e-horarios.md), [a-cdm](../../pesquisa/topicos/a-cdm.md)
- **Itens da especificação:** [Item 1 — 3 Objetivos](../../especificacao/01-3-objetivos.md), [Item 2 — É / Não é / Faz / Não faz](../../especificacao/02-e-nao-e-faz-nao-faz.md), [Item 3 — Visão do Produto](../../especificacao/03-visao-do-produto.md), [Item 4 — Mapeamento de Negócios (BPMN TO BE)](../../especificacao/04-mapeamento-de-negocios.md), [Item 5 — Atores / Usuários](../../especificacao/05-atores-usuarios.md), [Item 6 — Requisitos Funcionais](../../especificacao/06-requisitos-funcionais/00-item.md), [Item 7 — Estórias de Usuário](../../especificacao/07-estorias-de-usuario/00-item.md), [Item 8 — Requisitos Não Funcionais](../../especificacao/08-requisitos-nao-funcionais/00-item.md), [Item 9 — Diagrama Geral de Casos de Uso](../../especificacao/09-diagrama-geral-de-casos-de-uso.md), [Item 10 — Especificações de Caso de Uso](../../especificacao/10-especificacoes-de-caso-de-uso/00-item.md), [Item 11 — Diagrama de Atividades](../../especificacao/11-diagrama-de-atividades.md)
- **Fontes citadas:** 2, 4 (em [fontes.md](../../pesquisa/fontes.md))
- **Índice das decisões:** [README.md](README.md) · **Contexto geral:** [CONTEXT.md](../../CONTEXT.md)
