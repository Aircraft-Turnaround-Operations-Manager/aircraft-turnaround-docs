---
id: adr-0011
titulo: "ADR-0011 — Mínimo de 4 por integrante, sem máximo; numeração provisória por área"
tipo: decisao
decisao: D11
status: aceita
data: 2026-10-05
decisor: Rodrigo Alves
itens_template: [6, 7, 8, 9, 10]
areas: [A, B, C, D]
fontes: []
relacionados: [insumos-rfs, insumos-rnfs, adr-0010]
---
# ADR-0011 — Mínimo de 4 por integrante, sem máximo; numeração provisória por área

- **Status:** aceita · **Data:** 05/10/2026 · **Decisor:** Rodrigo Alves

## Contexto

- A rubrica pede, nos itens que dependem da quantidade de integrantes (6, 7, 8 e 10), **no mínimo** 4 itens por integrante (critério X.8). Com 4 integrantes, o mínimo é 16. Não há máximo.
- O plano do RA1 fixou a numeração por área (A = RF-1 a RF-4, B = RF-5 a RF-8, C = RF-9 a RF-12, D = RF-13 a RF-16, e o mesmo para estórias, casos de uso e RNFs). Na prática, isso transformou o mínimo em máximo: quem quisesse um quinto RF quebraria a numeração das outras áreas.
- O critério C06.2 exige RF-n **sequencial e sem lacunas** no documento final, então reservar faixas maiores com buracos não resolve.

## Opções consideradas

- **(a)** Manter a numeração fixa e limitar cada área a 4 itens.
- **(b)** Reservar faixas maiores por área (ex.: A = RF-1 a RF-10), aceitando lacunas.
- **(c)** Numeração **provisória por área** durante a escrita e **renumeração sequencial única** antes da revisão final.

## Decisão

**(c)**:

1. **Mínimo de 4 por integrante, sem máximo,** nos itens 6, 7, 8 e 10. Cada área escreve quantos RFs e RNFs o sistema precisar.
2. **IDs provisórios por área** enquanto os itens são escritos:

   | Item | Formato provisório | Exemplo |
   |---|---|---|
   | 6 — RFs | `RF-<área><n>` | RF-A1, RF-A2, …, RF-D5 |
   | 7 — Estórias | `US-<área><n>`, com o mesmo número do RF | US-D5 ↔ RF-D5 |
   | 8 — RNFs | `RNF-<área><n>` | RNF-B1 |
   | 9 e 10 — Casos de uso | `UC-<área><n>` | UC-C2 |

3. **Renumeração única,** feita por script no início da revisão cruzada (T12), depois que todas as áreas estiverem na `main`: áreas na ordem A, B, C, D e, dentro de cada área, na ordem do arquivo. RF-A1… vira RF-1…RF-n; cada estória recebe o número do seu RF (US001…); RNF-1…RNF-n; UC01…UCnn. A tabela de correspondência (provisório → final) fica registrada em `entregas/ra1-renumeracao.md`.
4. **Casos de uso:** o mínimo continua sendo 4 especificações por integrante (C10.1). Um RF extra pode ser coberto por um caso de uso já existente, por `include` ou `extend` (K.3), sem exigir especificação nova.

## Consequências

- Cada RF a mais exige uma estória com pelo menos 2 critérios de aceite (K.2); o caso de uso pode ser novo ou um já existente (K.3).
- README, `entregas/ra1-tarefas.md`, critérios e os arquivos de área passam a falar em "mínimo 4" e a usar os IDs provisórios.
- Os títulos das issues que citam faixas fixas (ex.: "RF-13 a RF-16") passam a citar a área e o mínimo.
- Até a renumeração, referências cruzadas (estória → RF, caso de uso → RF) usam sempre os IDs provisórios.

---

## Ligações

- **Pesquisa:** [insumos-rfs](../../pesquisa/impacto/insumos-rfs.md), [insumos-rnfs](../../pesquisa/impacto/insumos-rnfs.md)
- **Itens da especificação:** [Item 6 — Requisitos Funcionais](../../especificacao/06-requisitos-funcionais/00-item.md), [Item 7 — Estórias de Usuário](../../especificacao/07-estorias-de-usuario/00-item.md), [Item 8 — Requisitos Não Funcionais](../../especificacao/08-requisitos-nao-funcionais/00-item.md), [Item 9 — Diagrama Geral de Casos de Uso](../../especificacao/09-diagrama-geral-de-casos-de-uso.md), [Item 10 — Especificações de Caso de Uso](../../especificacao/10-especificacoes-de-caso-de-uso/00-item.md)
- **Plano e critérios:** [ra1-tarefas](../../entregas/ra1-tarefas.md), [ra1-criterios-de-aceite](../../entregas/ra1-criterios-de-aceite.md)
- **Outras decisões:** [D10](0010-administrador-usuario-e-equipe-do-operador.md)
- **Índice das decisões:** [README.md](README.md) · **Contexto geral:** [CONTEXT.md](../../CONTEXT.md)
