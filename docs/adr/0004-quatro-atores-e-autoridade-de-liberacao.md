---
id: adr-0004
titulo: "ADR-0004 — Quatro atores; Autoridade de Liberação é o representante da companhia"
tipo: decisao
decisao: D4
status: aceita
data: 2026-10-01
decisor: Rodrigo Alves
itens_template: [2, 4, 5, 6, 9, 10, 11]
areas: [D]
fontes: [2, 4]
relacionados: [papeis-e-atores, marcos-e-horarios, adr-0009, adr-0010]
---
# ADR-0004 — Quatro atores; Autoridade de Liberação é o representante da companhia

- **Status:** aceita, complementada por [ADR-0010](0010-administrador-usuario-e-equipe-do-operador.md) (Administrador do Sistema, ator abstrato Usuário e equipe do operador como dado) · **Data:** 01/10/2026 · **Decisor:** Rodrigo Alves · **Origem:** decisão D4 do [relatório de pesquisa](../../pesquisa/01-referencias-setor-e-similares.md) (seção 5)

## Contexto

- **[Fato][2][4]** No A-CDM, o *ground handler* marca o fim do atendimento (AEGT), o controlador registra o ARDT "When the flight reports ready" e o ATC autoriza o acionamento.
- **[Inferência]** Não existe nas fontes um papel único de "autoridade de liberação": a prontidão resulta desses três atos.
- **Escopo do projeto:** a integração real com o controle de tráfego aéreo está fora do escopo.
- **[Inferência]** Separar quem executa de quem libera sustenta a métrica "0 liberações com pendência".

## Opções consideradas

- **(a)** Manter 4 atores, com a liberação como ato interno da companhia aérea, sem ATC.
- **(b)** Fundir a Autoridade de Liberação com o Coordenador.

## Decisão

**(a).** Os atores são: **Operador de Solo/Rampa**, **Coordenador de Turnaround** ([ADR-0009](0009-nome-coordenador-de-turnaround.md)), **Autoridade de Liberação** — representante da companhia aérea que confirma a prontidão da aeronave, equivalente ao marco *Aircraft Ready* do A-CDM — e **Motor de Eventos** (ator não humano).

## Consequências

- O estado "Liberado" é um ato interno da Autoridade de Liberação, e não a autorização de acionamento ou push-back do ATC.
- O "Não faz" (item 2) diz que o sistema não emite autorizações de controle de tráfego aéreo.
- Lanes do BPMN (item 4), atores do item 5, diagrama de casos de uso (item 9) e raias do diagrama de atividades (item 11) usam exatamente esses nomes.

---

## Ligações

- **Pesquisa:** [papeis-e-atores](../../pesquisa/topicos/papeis-e-atores.md), [marcos-e-horarios](../../pesquisa/topicos/marcos-e-horarios.md)
- **Itens da especificação:** [Item 2 — É / Não é / Faz / Não faz](../../especificacao/02-e-nao-e-faz-nao-faz.md), [Item 4 — Mapeamento de Negócios (BPMN TO BE)](../../especificacao/04-mapeamento-de-negocios.md), [Item 5 — Atores / Usuários](../../especificacao/05-atores-usuarios.md), [Item 6 — Requisitos Funcionais](../../especificacao/06-requisitos-funcionais/00-item.md), [Item 9 — Diagrama Geral de Casos de Uso](../../especificacao/09-diagrama-geral-de-casos-de-uso.md), [Item 10 — Especificações de Caso de Uso](../../especificacao/10-especificacoes-de-caso-de-uso/00-item.md), [Item 11 — Diagrama de Atividades](../../especificacao/11-diagrama-de-atividades.md)
- **Outras decisões:** [D9](0009-nome-coordenador-de-turnaround.md)
- **Fontes citadas:** 2, 4 (em [fontes.md](../../pesquisa/fontes.md))
- **Índice das decisões:** [README.md](README.md) · **Contexto geral:** [CONTEXT.md](../../CONTEXT.md)
