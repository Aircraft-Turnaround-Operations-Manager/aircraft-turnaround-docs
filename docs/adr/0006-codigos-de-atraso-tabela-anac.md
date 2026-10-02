---
id: adr-0006
titulo: "ADR-0006 — Códigos de atraso: tabela completa da ANAC (72 códigos)"
tipo: decisao
decisao: D6
status: aceita
data: 2026-10-01
decisor: Rodrigo Alves
itens_template: [2, 4, 6, 7, 10]
areas: [B, D]
fontes: [16, 37, 62]
relacionados: [codigos-de-atraso, referencias-iata, insumos-rfs, adr-0001]
---
# ADR-0006 — Códigos de atraso: tabela completa da ANAC (72 códigos)

- **Status:** aceita · **Data:** 01/10/2026 · **Decisor:** Rodrigo Alves · **Origem:** decisão D6 do [relatório de pesquisa](../../pesquisa/01-referencias-setor-e-similares.md) (seção 5)

## Contexto

- **[Fato][62]** A Portaria nº 55/SPO/SSA, de 06/08/2026 (DOU de 11/08/2026, vigência na data da publicação), altera a Portaria nº 791/SSO/2012, que trata do registro dos motivos de atraso e cancelamento de voos, e institui nova tabela: **72 códigos** em 12 categorias, só siglas de duas letras, descrições em português e coluna "DESCRIÇÃO PARA O INFOVOO/SRV". Leitura registrada em [Códigos de atraso](../../pesquisa/topicos/codigos-de-atraso.md).
- **[Inferência]** As siglas e as categorias são as mesmas da IATA AHM 730 (ex.: GC limpeza, GF combustível, GB catering, RA aeronave que chegou atrasada), comparando [62] com [16].
- **[Fato]** O AHM 732 existe como novo esquema da IATA [37]; a portaria de 2026 manteve as duas letras [62].

## Opções consideradas

- **(a)** Subconjunto dos códigos de dois dígitos da IATA AHM 730 (31–39 e alguns outros).
- **(b)** IATA AHM 732 (três letras).
- **(c)** Tabela completa da ANAC.

## Decisão

**(c) Tabela da ANAC, com os 72 códigos, sem recorte.** É ao mesmo tempo a norma brasileira e a taxonomia da IATA AHM 730.

## Consequências

- O sistema registra a causa de cada atraso ou exceção com a sigla e a descrição da ANAC.
- A tabela é carregada inteira, inclusive categorias que não são de solo (ex.: RA, atraso em cadeia, como causa de entrada).
- Item 2 ("Faz"), RFs das áreas B e D e casos de uso de exceção citam a tabela da ANAC.
- Ao implementar, versionar a tabela no repositório com referência à Portaria nº 55/2026.

---

## Ligações

- **Pesquisa:** [codigos-de-atraso](../../pesquisa/topicos/codigos-de-atraso.md), [referencias-iata](../../pesquisa/topicos/referencias-iata.md), [insumos-rfs](../../pesquisa/impacto/insumos-rfs.md)
- **Itens da especificação:** [Item 2 — É / Não é / Faz / Não faz](../../especificacao/02-e-nao-e-faz-nao-faz.md), [Item 4 — Mapeamento de Negócios (BPMN TO BE)](../../especificacao/04-mapeamento-de-negocios.md), [Item 6 — Requisitos Funcionais](../../especificacao/06-requisitos-funcionais/00-item.md), [Item 7 — Estórias de Usuário](../../especificacao/07-estorias-de-usuario/00-item.md), [Item 10 — Especificações de Caso de Uso](../../especificacao/10-especificacoes-de-caso-de-uso/00-item.md)
- **Outras decisões:** [D1](0001-referencia-horario-tobt-mais-5-min.md)
- **Fontes citadas:** 16, 37, 62 (em [fontes.md](../../pesquisa/fontes.md))
- **Índice das decisões:** [README.md](README.md) · **Contexto geral:** [CONTEXT.md](../../CONTEXT.md)
