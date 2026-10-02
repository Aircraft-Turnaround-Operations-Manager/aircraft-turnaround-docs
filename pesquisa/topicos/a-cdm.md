---
id: a-cdm
titulo: "O que é o A-CDM (P1.1)"
tipo: pesquisa-topico
secao_original: "2.1"
itens_template: [1, 3]
areas: []
decisoes: [D8]
fontes: [1, 2, 4, 5, 6, 57, 58]
relacionados: [marcos-e-horarios, tolerancias-e-indicadores, referencias-iata]
status: vigente
atualizado: 2026-10-01
---
# O que é o A-CDM (P1.1)

> Base de conhecimento do projeto · origem: seção 2.1 do [relatório consolidado](../01-referencias-setor-e-similares.md) (congelado em 01/10/2026) · fontes numeradas em [fontes.md](../fontes.md) · convenções [Fato]/[Inferência] e índices no [mapa da pesquisa](../README.md).

> **Decisões vigentes (prevalecem sobre o texto abaixo):** [D8 — Siglas do A-CDM com nome em português](../../docs/adr/0008-siglas-a-cdm-com-nome-em-portugues.md).
>
> As siglas do A-CDM são usadas na especificação sempre com o nome em português na primeira ocorrência (D8).


- **[Fato][1]** A EUROCONTROL (organização europeia para a segurança da navegação aérea) define: "Airport CDM (A-CDM) aims to improve the efficiency and resilience of airport operations by optimising the use of resources and improving the predictability of air traffic." O conceito pede que "airport operators, aircraft operators, ground handlers and ATC" troquem informação "relevant accurate and timely", junto com o Network Manager europeu.
- **[Fato][1]** A página oficial informa que o A-CDM está "fully implemented in 34 airports across Europe" (ex.: Amsterdam, Frankfurt, London Heathrow, Paris CDG).
- **[Fato][1][2]** Documentos de referência atuais: o *Airport CDM Implementation Manual* (versão 5.0, 31/03/2017) e a *EUROCONTROL Specification for Airport Collaborative Decision Making (A-CDM)*, edição 1.0, de 30/01/2025.
- **[Fato][4]** O manual de implantação versão 5.0 é assinado em conjunto por ACI (Airports Council International), EUROCONTROL e IATA (International Air Transport Association).
- **[Fato][2]** A Especificação 2025 (seção 2.1) repete o objetivo de eficiência, resiliência e previsibilidade e descreve o objetivo dos processos de marcos como duplo: informar aos parceiros o ELDT (*Estimated Landing Time*, horário estimado de pouso) e informar "inconsistencies and updated predictions of Target Off-block, Start-up Approval and Take-Off Times" aos parceiros e ao Network Manager.
- **[Fato][5]** A IATA, nas suas recomendações de A-CDM (2018), escreve que o A-CDM melhora "flight predictability through real time data exchange" e que "Overall, A-CDM is about making more efficient use of existing capacity and resources".
- **[Fato][6]** O escritório Ásia-Pacífico da ICAO (Organização da Aviação Civil Internacional) publicou um FAQ de A-CDM (1ª ed., 02/07/2021) que cita como materiais-guia o Doc 9971 da ICAO, o manual da EUROCONTROL e recomendações de CANSO e IATA.
- **[Fato][57][58]** No Brasil, o Aeroporto de Guarulhos (GRU) foi anunciado como o primeiro aeroporto A-CDM do país em 05/11/2020, em projeto do DECEA (Departamento de Controle do Espaço Aéreo) com cooperação da EUROCONTROL. Em 2023, o DECEA apresentou o acompanhamento do A-CDM em GRU com participação de companhias aéreas e empresas de *ground handling* (atendimento em solo), com foco em "previsibilidade e pontualidade".
- **[Inferência]** O A-CDM é a referência mais forte para o vocabulário do nosso sistema: ele trata o turnaround como uma sequência de marcos com horários-alvo e responsáveis definidos. Ele **não** define como orquestrar as tarefas internas do turnaround (quem faz limpeza, em que ordem). Essa camada fica com o *ground handler* e é justamente onde o nosso produto atua.

---

## Ligações

- **Decisões:** [D8](../../docs/adr/0008-siglas-a-cdm-com-nome-em-portugues.md)
- **Itens da especificação:** [Item 1 — 3 Objetivos](../../especificacao/01-3-objetivos.md), [Item 3 — Visão do Produto](../../especificacao/03-visao-do-produto.md)
- **Relacionados:** [marcos-e-horarios](marcos-e-horarios.md), [tolerancias-e-indicadores](tolerancias-e-indicadores.md), [referencias-iata](referencias-iata.md)
- **Fontes citadas:** 1, 2, 4, 5, 6, 57, 58 (em [fontes.md](../fontes.md))
- **Contexto geral:** [CONTEXT.md](../../CONTEXT.md) · [mapa da pesquisa](../README.md)
