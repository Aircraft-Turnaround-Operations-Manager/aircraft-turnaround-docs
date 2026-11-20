---
id: adr-0022
titulo: "ADR-0022 — IDs provisórios dos casos de teste por área e renumeração única na consolidação"
tipo: decisao
decisao: D22
status: aceita
data: 2026-11-13
decisor: Rodrigo Alves
itens_template: [15]
areas: [A, B, C, D]
fontes: []
relacionados: [adr-0011, adr-0021]
---
# ADR-0022 — IDs provisórios dos casos de teste por área e renumeração única na consolidação

- **Status:** aceita · **Data:** 13/11/2026 · **Decisor:** Rodrigo Alves · **Complementa:** [ADR-0011](0011-minimo-por-integrante-e-numeracao-provisoria.md) (a mesma regra de IDs provisórios por área, agora para os casos de teste do item 15)

## Contexto

- O critério C15.1 de `entregas/ra2-criterios-de-aceite.md` pede o ID do caso de teste no formato `CT-nnn`.
- As quatro áreas escrevem os casos de teste em paralelo, cada uma no seu `area-x.md` do item 15. Com uma numeração única desde o início, cada área precisaria saber quantos casos de teste as outras já escreveram, e um caso de teste a mais numa área empurraria a numeração das outras. É o mesmo problema que a ADR-0011 resolveu para os RFs, as estórias, os RNFs e os casos de uso no RA1.
- As áreas A (PR #176), B (PR #166) e C (PR #174) já escreveram os seus casos de teste com o prefixo da área: `CT-A001`, `CT-B001`, `CT-C001`. Nenhuma decisão cobria isso ([issue #180](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/issues/180)).

## Opções consideradas

- **(a)** Numeração única desde o início, com faixas reservadas por área. Cria buracos ou limita a quantidade, como a ADR-0011 mostrou.
- **(b)** Manter o prefixo da área no documento final e mudar o texto do C15.1.
- **(c)** IDs provisórios por área durante a escrita e renumeração única, por script, na consolidação.

## Decisão

**(c)**:

1. **Durante a escrita,** cada área numera os seus casos de teste com o prefixo da área e três dígitos, numa sequência própria: `CT-A001`, `CT-A002`…; `CT-B001`…; `CT-C001`…; `CT-D001`…. Uma área não precisa saber quantos casos de teste as outras têm, e nenhuma sobrescreve a sequência da outra.
2. **Na consolidação,** depois que as quatro áreas estiverem na `main` e antes da revisão cruzada (tarefa T16, [issue #156](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/issues/156)), um script renumera todos os casos de teste numa sequência única, `CT-001` em diante, sem lacunas, como pede o C15.1.
3. **Ordem da renumeração:** a ordem em que os casos de teste aparecem no documento, isto é, por caso de uso (UC01 a UC37) e, dentro de cada caso de uso, na ordem da planilha. O gerador do documento já põe o item 15 em ordem de caso de uso, e o UC37, que é da área B, vem depois do UC36; renumerar pela ordem das áreas deixaria os números fora de ordem no PDF.
4. **O script troca o ID em todo lugar que o cita** e grava a tabela de correspondência (provisório → final) em `entregas/ra2-renumeracao.md`, como `entregas/ra1-renumeracao.md` fez no RA1.

## Consequências

- Até a renumeração, toda referência a um caso de teste usa o ID provisório. A matriz de rastreabilidade aceita os dois formatos (ADR-0021).
- A tarefa T16 começa pela renumeração, e a matriz é gerada de novo logo depois.
- A área D usa `CT-D001` em diante.

---

## Ligações

- **Decisão complementada:** [ADR-0011](0011-minimo-por-integrante-e-numeracao-provisoria.md) · **Matriz estendida:** [ADR-0021](0021-matriz-de-rastreabilidade-estendida.md)
- **Item da especificação:** [Item 15](../../especificacao/15-casos-de-teste/00-item.md)
- **Critérios:** [ra2-criterios-de-aceite](../../entregas/ra2-criterios-de-aceite.md) · **Renumeração do RA1:** [ra1-renumeracao](../../entregas/ra1-renumeracao.md)
- **Índice das decisões:** [README.md](README.md) · **Contexto geral:** [CONTEXT.md](../../CONTEXT.md)
