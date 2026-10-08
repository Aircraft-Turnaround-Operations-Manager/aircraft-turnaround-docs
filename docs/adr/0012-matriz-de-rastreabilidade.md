---
id: adr-0012
titulo: "ADR-0012 — Matriz de rastreabilidade como apêndice gerado; sem tabelas de base nos arquivos de área"
tipo: decisao
decisao: D12
status: aceita
data: 2026-10-07
decisor: Rodrigo Alves
itens_template: [6, 7, 8, 10]
areas: [A, B, C, D]
fontes: []
relacionados: [adr-0011]
---
# ADR-0012 — Matriz de rastreabilidade como apêndice gerado; sem tabelas de base nos arquivos de área

- **Status:** aceita · **Data:** 07/10/2026 · **Decisor:** Rodrigo Alves

## Contexto

- As áreas B e D passaram a pôr, abaixo das tabelas de RFs e RNFs, uma tabela "Base" com a origem de cada requisito ([Fato]/[Inferência] e fontes). O template dos itens 6 e 8 só tem a tabela principal, e nenhuma regra dizia se essa tabela iria para o PDF (critério X.1).
- O cruzamento entre objetivos, RFs, estórias, casos de uso e RNFs é exigido pelos critérios C06.5, K.2, K.3 e K.6, mas não aparecia em lugar nenhum do documento. A ferramenta própria para isso é a **matriz de rastreabilidade**.

## Opções consideradas

- **(a)** Levar as tabelas "Base" para o PDF, abaixo de cada tabela.
- **(b)** Manter as tabelas "Base" só no repositório e incluir no documento uma matriz de rastreabilidade.
- **(c)** Remover as tabelas "Base" e usar a matriz de rastreabilidade como única forma de relacionar os artefatos.

## Decisão

**(c)** (corrigida em 07/10/2026: a primeira redação registrou a opção (b) por engano):

1. O documento ganha o **Apêndice A — Matriz de rastreabilidade** (`especificacao/apendice-a-matriz-de-rastreabilidade.md`), depois da seção 11. É apêndice, e não seção 12, porque as seções 12 a 15 do template são as da entrega do RA2 (modelo de dados, classes, sequência e casos de teste).
2. A matriz é **gerada por script** (`scripts/gerar_matriz_rastreabilidade.py`) a partir dos arquivos de área dos itens 6, 7, 8 e 10, para não divergir do texto. Ela traz: RF × objetivo, ator, estória, caso(s) de uso e RNFs; objetivo × RFs; RNF × RFs; e a lista de lacunas.
3. Para o cruzamento funcionar:
   - cada estória mantém no título o RF correspondente (`US-Xn – REQUISITO RF-Xn`);
   - cada caso de uso cita os RFs que atende (em regras de negócio ou fluxos);
   - **cada RNF cita os RFs a que se aplica** (por ID, por faixa como "RF-B1 a RF-B6" ou com "todos os RFs").
4. As tabelas "Base" **não existem mais**: foram removidas dos arquivos de área e não devem ser criadas nos próximos. A relação entre os artefatos é mostrada só pela matriz. As citações [n] dentro do texto dos requisitos ficam, com a linha "Fontes citadas" abaixo da tabela quando houver citação.

## Consequências

- No T12, depois da renumeração (ADR-0011), o script é rodado de novo e a lista de lacunas tem de ficar vazia (critério K.13).
- No T13, a consolidação inclui o Apêndice A.
- RNF que não cite nenhum RF aparece como lacuna; o dono da área ajusta o texto.

---

## Ligações

- **Itens da especificação:** [Item 6](../../especificacao/06-requisitos-funcionais/00-item.md), [Item 7](../../especificacao/07-estorias-de-usuario/00-item.md), [Item 8](../../especificacao/08-requisitos-nao-funcionais/00-item.md), [Item 10](../../especificacao/10-especificacoes-de-caso-de-uso/00-item.md), [Apêndice A](../../especificacao/apendice-a-matriz-de-rastreabilidade.md)
- **Plano e critérios:** [ra1-tarefas](../../entregas/ra1-tarefas.md), [ra1-criterios-de-aceite](../../entregas/ra1-criterios-de-aceite.md)
- **Outras decisões:** [D11](0011-minimo-por-integrante-e-numeracao-provisoria.md)
- **Índice das decisões:** [README.md](README.md) · **Contexto geral:** [CONTEXT.md](../../CONTEXT.md)
