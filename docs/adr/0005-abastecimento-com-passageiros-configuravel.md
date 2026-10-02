---
id: adr-0005
titulo: "ADR-0005 — Abastecimento com passageiros a bordo: regra configurável por operador"
tipo: decisao
decisao: D5
status: aceita
data: 2026-10-01
decisor: Rodrigo Alves
itens_template: [4, 6, 10, 11]
areas: [A, B]
fontes: [24, 26, 27, 28]
relacionados: [atividades-e-dependencias, caminho-critico]
---
# ADR-0005 — Abastecimento com passageiros a bordo: regra configurável por operador

- **Status:** aceita · **Data:** 01/10/2026 · **Decisor:** Rodrigo Alves · **Origem:** decisão D5 do [relatório de pesquisa](../../pesquisa/01-referencias-setor-e-similares.md) (seção 5)

## Contexto

- **[Fato]** EASA, CAT.OP.MPA.195: proibido abastecer com Avgas ou combustível *wide-cut* com passageiros embarcando, a bordo ou desembarcando; para os demais, "necessary precautions shall be taken" [26].
- **[Fato][27]** ANAC, RBAC 91 (Emenda 05), seção 91.102(g): o abastecimento com passageiros a bordo, embarcando ou desembarcando só é permitido se houver (1) procedimento aprovado e um tripulante de voo na cabine de pilotagem supervisionando; (2) no mínimo 50% do número de comissários requeridos e/ou pessoas adequadamente treinadas para dirigir uma evacuação de emergência, com os meios de evacuação disponíveis; (3) motores desligados (exceto APU, a unidade auxiliar de energia); e (4) comunicação entre o pessoal de solo e o tripulante na cabine dos pilotos.
- **[Fato]** A Airbus lista precauções de cabine e de solo [28]; há modelos acadêmicos que adotam a regra sequencial [24].

## Opções consideradas

- **(a)** Dependência fixa: abastecimento sempre entre desembarque e embarque.
- **(b)** Regra configurável por operador.

## Decisão

**(b).** Como é permitido sob condições, o sistema deixa o abastecimento correr em paralelo com o fluxo de passageiros quando o operador habilita a regra.

## Consequências

- O modelo de tarefas tem a regra "abastecimento com passageiros a bordo permitido?" por operador (área A). **Valor padrão sugerido: "não permitido"**, o caso mais conservador [24]; o operador habilita quando cumprir as condições do RBAC 91.102(g).
- Sem a regra, o abastecimento fica entre desembarque e embarque e pode entrar no caminho crítico [24]; o caminho crítico é recalculado conforme a regra.
- BPMN (item 4) e diagrama de atividades (item 11) mostram o gateway; casos de uso (item 10) trazem a regra de negócio com as condições do RBAC 91.102(g).

---

## Ligações

- **Pesquisa:** [atividades-e-dependencias](../../pesquisa/topicos/atividades-e-dependencias.md), [caminho-critico](../../pesquisa/topicos/caminho-critico.md)
- **Itens da especificação:** [Item 4 — Mapeamento de Negócios (BPMN TO BE)](../../especificacao/04-mapeamento-de-negocios.md), [Item 6 — Requisitos Funcionais](../../especificacao/06-requisitos-funcionais/00-item.md), [Item 10 — Especificações de Caso de Uso](../../especificacao/10-especificacoes-de-caso-de-uso/00-item.md), [Item 11 — Diagrama de Atividades](../../especificacao/11-diagrama-de-atividades.md)
- **Fontes citadas:** 24, 26, 27, 28 (em [fontes.md](../../pesquisa/fontes.md))
- **Índice das decisões:** [README.md](README.md) · **Contexto geral:** [CONTEXT.md](../../CONTEXT.md)
