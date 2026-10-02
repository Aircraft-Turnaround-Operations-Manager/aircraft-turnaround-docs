---
id: adr-0007
titulo: "ADR-0007 — Dados registrados pelo operador, inclusive QR Code lido pelo celular"
tipo: decisao
decisao: D7
status: aceita
data: 2026-10-01
decisor: Rodrigo Alves
itens_template: [2, 3, 4, 6, 7, 10]
areas: [B]
fontes: [42, 63, 64]
relacionados: [atividades-e-dependencias, lacunas-e-diferencial, impacto-por-item, adr-0004]
---
# ADR-0007 — Dados registrados pelo operador, inclusive QR Code lido pelo celular

- **Status:** aceita · **Data:** 01/10/2026 · **Decisor:** Rodrigo Alves · **Origem:** decisão D7 do [relatório de pesquisa](../../pesquisa/01-referencias-setor-e-similares.md) (seção 5)

## Contexto

A recomendação inicial era um MVP sem câmeras nem sensores. O Rodrigo quer capturar eventos pela câmera do celular lendo QR Code — por exemplo, o operador de limpeza bipa os assentos limpos e o sistema recebe o registro —, simulado na apresentação do TCC. Sensores nativos da aeronave não entram.

- **[Fato]** Há leitura de QR Code para comprovar limpeza em aeroporto (piloto em Albany, 2020, para banheiros e totens) [63] e checklist digital de limpeza de cabine por zona [64]. Leitura registrada em [Atividades e dependências](../../pesquisa/topicos/atividades-e-dependencias.md).
- **[Fato]** A Assaia alerta quando a equipe de limpeza não é detectada pela câmera de pátio até 3 min depois do fim do desembarque [42].
- **[Inferência]** Leitura de QR Code por assento ligada ao andamento do turnaround não foi encontrada nas fontes consultadas.

## Opções consideradas

- **(a)** Só registro manual do operador.
- **(b)** Integração com sensores.
- **(c)** Registro pelo operador, inclusive leitura de QR Code pela câmera do celular.

## Decisão

**(c), "(a) ampliada".** Os dados vêm do operador, inclusive por leitura de QR Code pela câmera do celular. Ficam fora: sensores da própria aeronave e câmeras fixas no pátio.

## Consequências

- "Faz" (item 2): confirmar tarefas por QR Code (ex.: limpeza por assento, fileira ou zona). "Não faz": captura por sensores da aeronave ou por câmeras fixas no pátio.
- Diferencial **DF5** na Visão do Produto (item 3), escrito como "não encontrado nas fontes consultadas".
- RF na área B e caso de uso com protótipo de tela da leitura.
- **[Inferência]** Bipar assento por assento pode atrasar a limpeza: prever leitura por fileira ou zona, com assento como opção. Etiquetas dentro da cabine dependem da companhia; na apresentação, QR Codes impressos resolvem.

---

## Ligações

- **Pesquisa:** [atividades-e-dependencias](../../pesquisa/topicos/atividades-e-dependencias.md), [lacunas-e-diferencial](../../pesquisa/similares/lacunas-e-diferencial.md), [impacto-por-item](../../pesquisa/impacto/impacto-por-item.md)
- **Itens da especificação:** [Item 2 — É / Não é / Faz / Não faz](../../especificacao/02-e-nao-e-faz-nao-faz.md), [Item 3 — Visão do Produto](../../especificacao/03-visao-do-produto.md), [Item 4 — Mapeamento de Negócios (BPMN TO BE)](../../especificacao/04-mapeamento-de-negocios.md), [Item 6 — Requisitos Funcionais](../../especificacao/06-requisitos-funcionais/00-item.md), [Item 7 — Estórias de Usuário](../../especificacao/07-estorias-de-usuario/00-item.md), [Item 10 — Especificações de Caso de Uso](../../especificacao/10-especificacoes-de-caso-de-uso/00-item.md)
- **Outras decisões:** [D4](0004-quatro-atores-e-autoridade-de-liberacao.md)
- **Fontes citadas:** 42, 63, 64 (em [fontes.md](../../pesquisa/fontes.md))
- **Índice das decisões:** [README.md](README.md) · **Contexto geral:** [CONTEXT.md](../../CONTEXT.md)
