---
id: adr-0021
titulo: "ADR-0021 — Matriz de rastreabilidade estendida aos itens 12, 14 e 15"
tipo: decisao
decisao: D21
status: aceita
data: 2026-11-13
decisor: Rodrigo Alves
itens_template: [12, 14, 15]
areas: [A, B, C, D]
fontes: []
relacionados: [adr-0012, adr-0022]
---
# ADR-0021 — Matriz de rastreabilidade estendida aos itens 12, 14 e 15

- **Status:** aceita · **Data:** 13/11/2026 · **Decisor:** Rodrigo Alves · **Complementa:** [ADR-0012](0012-matriz-de-rastreabilidade.md) (a matriz continua sendo o Apêndice A, gerado por script, sem tabelas "Base" nos arquivos de área)

## Contexto

- A [ADR-0012](0012-matriz-de-rastreabilidade.md) criou a matriz de rastreabilidade do RA1, que cruza os itens 1, 5, 6, 7, 8 e 10.
- O RA2 acrescenta o modelo de dados (item 12), os diagramas de sequência (item 14) e os casos de teste (item 15). A decisão B5 de `entregas/ra2-criterios-de-aceite.md` pede que a matriz ligue também esses itens: RF → tabelas; caso de uso → diagrama de sequência; critério de aceite → casos de teste. Os critérios C12.2, C14.1, C15.2, K.2, K.5 e K.12 dependem dessas ligações.
- A extensão foi feita na tarefa T03 ([issue #142](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/issues/142), PR #171) e escrita, por engano, como uma seção nova dentro da ADR-0012. Uma ADR aceita não muda de conteúdo: decisão nova vira ADR nova, que complementa ou substitui a anterior. Esta ADR registra a extensão, e a ADR-0012 voltou ao texto original.

## Opções consideradas

- **(a)** Manter a matriz só com os itens do RA1 e conferir os itens 12, 14 e 15 por outro script.
- **(b)** Estender a matriz do Apêndice A com os itens 12, 14 e 15, no mesmo script.

## Decisão

**(b)**, com o script `scripts/gerar_matriz_rastreabilidade.py`:

1. **RF → tabelas:** a tabela A.1 ganha a coluna "Tabelas (item 12)", lida da tabela `Serviço | Tabela | RFs atendidos` do item 12 (C12.2).
2. **Caso de uso → diagrama de sequência:** tabela A.4, lida das legendas "Diagrama de Sequência do UCnn – <nome>" do item 14 (C14.1). Um diagrama pode ter partes, cada uma com a legenda seguida de "(parte n: …)".
3. **Critério de aceite → casos de teste:** tabela A.5, lida da coluna "Estória e critério de aceite" da planilha do item 15, em que o critério é escrito como `USnnn-CAn`, com n igual ao número da linha do critério na estória do item 7 (C15.2). O ID do caso de teste segue a [ADR-0022](0022-ids-provisorios-dos-casos-de-teste.md).
4. **Lacunas** (A.6): tabela sem RF; caso de uso sem diagrama ou com nome diferente do item 10; critério de aceite sem caso de teste; caso de teste sem critério ou com critério inexistente. As lacunas de um item só entram na lista depois que o item tem conteúdo, para que a matriz possa ser gerada durante o trabalho. Na entrega, a lista tem de dizer "Nenhuma." (K.12).
5. O formato que cada item precisa seguir para o script ler fica no comentário do `00-item.md` do item (ou no arquivo do item 12).

## Consequências

- Cada PR que muda os itens 12, 14 ou 15 roda o script de novo, como já acontece com os itens 6 a 10.
- `scripts/verificar_revisao.py` exige "0 lacunas" e, por isso, falha enquanto os itens 12 a 15 estiverem incompletos. A falha mostra o que falta, e na entrega a verificação tem de passar.
- A seção de lacunas passou de A.4 para A.6, porque as tabelas A.4 e A.5 são novas.

---

## Ligações

- **Decisão complementada:** [ADR-0012](0012-matriz-de-rastreabilidade.md) · **IDs dos casos de teste:** [ADR-0022](0022-ids-provisorios-dos-casos-de-teste.md)
- **Itens da especificação:** [Item 12](../../especificacao/12-modelo-de-dados.md), [Item 14](../../especificacao/14-diagramas-de-sequencia/00-item.md), [Item 15](../../especificacao/15-casos-de-teste/00-item.md), [Apêndice A](../../especificacao/apendice-a-matriz-de-rastreabilidade.md)
- **Critérios:** [ra2-criterios-de-aceite](../../entregas/ra2-criterios-de-aceite.md)
- **Índice das decisões:** [README.md](README.md) · **Contexto geral:** [CONTEXT.md](../../CONTEXT.md)
