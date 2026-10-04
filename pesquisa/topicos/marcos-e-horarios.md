---
id: marcos-e-horarios
titulo: "Marcos e horários do A-CDM (P1.2)"
tipo: pesquisa-topico
secao_original: "2.2"
itens_template: [4, 5, 6, 9, 11]
areas: [A, B, C, D]
decisoes: [D1, D4, D8]
fontes: [2, 3, 4, 7, 8]
relacionados: [a-cdm, tolerancias-e-indicadores, papeis-e-atores, atividades-e-dependencias]
status: vigente
atualizado: 2026-10-01
---
# Marcos e horários do A-CDM (P1.2)

> Base de conhecimento do projeto · origem: seção 2.2 do [relatório consolidado](../01-referencias-setor-e-similares.md) (congelado em 01/10/2026) · fontes numeradas em [fontes.md](../fontes.md) · convenções [Fato]/[Inferência] e índices no [mapa da pesquisa](../README.md).

> **Decisões vigentes (prevalecem sobre o texto abaixo):** [D1 — Referência de horário: TOBT planejado + 5 min, unilateral](../../docs/adr/0001-referencia-horario-tobt-mais-5-min.md); [D4 — Quatro atores; Autoridade de Liberação é o representante da companhia](../../docs/adr/0004-quatro-atores-e-autoridade-de-liberacao.md); [D8 — Siglas do A-CDM com nome em português](../../docs/adr/0008-siglas-a-cdm-com-nome-em-portugues.md).
>
> O horário de referência do projeto é o TOBT planejado (D1). O estado "Liberado" é um ato interno da Autoridade de Liberação, não a autorização de acionamento do ATC (D4).


## 2.2.1 Os 16 marcos do A-CDM

**[Fato][2][3]** A Especificação 2025 numera 16 marcos (MST, *milestone*), mais três marcos de degelo (numerados D1 a D3 pela EUROCONTROL; não confundir com as decisões D1–D10 do projeto) que não entram no nosso escopo:

| Nº | Marco (original) | Horário registrado | Fonte |
|---|---|---|---|
| 1 | ATC Flight Plan Activated | — | [2] |
| 2 | EOBT − 2 hrs | — | [2] |
| 3 | Take Off from Outstation | ATOT da origem | [2] |
| 4 | Local Radar Update | — | [2] |
| 5 | Final Approach | — | [2] |
| 6 | Landed | ALDT | [2] |
| 7 | In-blocks | AIBT | [2] |
| 8 | Ground Handling Started | ACGT | [2] |
| 9 | TOBT Manual Input / Update | TOBT | [2] |
| 10 | TSAT Issued | TSAT | [2] |
| 11 | Boarding Started | ASBT | [2] |
| 12 | Aircraft Ready | ARDT | [2] |
| 13 | Start-up Requested | ASRT | [2] |
| 14 | Start-up Approved | ASAT | [2] |
| 15 | Off-Block | AOBT | [2] |
| 16 | Take Off | ATOT | [2] |

**[Inferência]** Os marcos 7 a 15 cobrem exatamente o intervalo do nosso produto (do in-block ao off-block). Os marcos 1 a 6 e 16 são de tráfego aéreo e ficam fora do escopo, mas os horários deles (ELDT, EIBT) alimentam o planejamento do turnaround.

## 2.2.2 Glossário de horários (sigla, nome, significado, quem atualiza)

| Sigla | Nome original | Significado | Quem atualiza / origem | Fonte |
|---|---|---|---|---|
| SIBT | Scheduled In-Block Time | Horário **programado** de chegada à primeira posição de estacionamento. | Programação da companhia aérea. | [Fato][4] |
| ELDT | Estimated Landing Time | Horário **estimado** de pouso. | Dados de fluxo do Network Manager (mensagens FUM — *Flight Update Message* — e serviços B2B, *business-to-business*, do Network Manager) ou sistemas de chegada. | [Fato][3][4] |
| EXIT | Estimated Taxi-In Time | Tempo estimado de táxi entre o pouso e a posição. | Parâmetro do A-CDM System (aeroporto). | [Fato][4] |
| EIBT | Estimated In-Block Time | Horário estimado de chegada à posição. **EIBT = ELDT + EXIT**. | Calculado pelo A-CDM System. | [Fato][3][4] |
| ALDT | Actual Landing Time | Horário **real** do pouso (marco 6). | Controle de tráfego aéreo (ATC). | [Fato][3][4] |
| AIBT | Actual In-Block Time | Horário real de chegada à posição (marco 7). Equivale ao ATA (*actual time of arrival*) da companhia. | Sistemas do ATC/aeroporto ou do *handling*, conforme a implantação local. | [Fato][2][4] |
| ACGT | Actual Commencement of Ground Handling Time | Início real do atendimento em solo (marco 8); "can be equal to AIBT". | *Ground handler*. | [Fato][2][4] |
| MTTT | Minimum Turn-round Time | "The minimum turn-round time agreed with an AO/GH for a specified flight or aircraft type". | Parâmetro acordado entre companhia (AO) e *ground handler* (GH). | [Fato][4] |
| SOBT | Scheduled Off-Block Time | Horário programado de saída da posição. | Programação da companhia. | [Fato][4] |
| EOBT | Estimated Off-Block Time | Horário estimado de início do movimento de partida, do plano de voo ATC. | Companhia aérea (dona do plano de voo). | [Fato][2][4] |
| TOBT | Target Off-Block Time | "The time that an Aircraft Operator or Ground Handler estimates that an aircraft will be ready" (portas fechadas, ponte removida, trator de push-back disponível, pronta para acionar). Marco 9. | Companhia aérea, que pode delegar ao *ground handler* ("TOBT Responsible Person"). O valor inicial pode ser calculado automaticamente: EIBT + MTTT ou EOBT, o que for mais tarde. | [Fato][2][3][4][8] |
| TSAT | Target Start-up Approval Time | Horário em que a aeronave pode esperar a autorização de acionamento/push-back, considerando TOBT, CTOT e tráfego. Marco 10. | ATC / sequenciador pré-partida. Emitido entre 40 e 30 min antes do TOBT. | [Fato][3][4][7] |
| ASBT | Actual Start Boarding Time | Início real do embarque ("passengers entering the bridge or bus"). Marco 11. | Companhia/*handling* (parceiro responsável). | [Fato][2][4] |
| AEGT | Actual End of Ground Handling Time | Fim real do atendimento em solo; "can be equal to ARDT". | *Ground handler*. | [Fato][4] |
| ARDT | Actual Ready Time | Aeronave pronta para acionar/push-back "immediately after clearance delivery". Marco 12. | O controlador (ATCO) registra quando o voo reporta "pronto"; alternativamente, as operações do aeroporto atualizam no A-CDM System. | [Fato][2][4] |
| ASRT | Actual Start-up Request Time | Horário em que o piloto pede o acionamento. Marco 13. | ATC registra. | [Fato][3][4] |
| ASAT | Actual Start-up Approval Time | Horário em que a aeronave recebe a autorização de acionamento. Marco 14. | ATC. | [Fato][3][4] |
| AOBT | Actual Off-Block Time | Horário real de push-back / saída da posição (marco 15). Equivale ao ATD (*actual time of departure*) da companhia. | ATC, A-SMGCS (sistema avançado de guiagem e controle de movimento de superfície) ou sistema de docking. | [Fato][3][4] |
| EXOT | Estimated Taxi-Out Time | Tempo estimado de táxi da posição até a decolagem. | Parâmetro do A-CDM System. | [Fato][4] |
| TTOT | Target Take-Off Time | Decolagem-alvo: TOBT/TSAT + EXOT. | Calculado pelo A-CDM System. | [Fato][3][4] |
| CTOT | Calculated Take-Off Time | Slot de decolagem do gerenciamento de fluxo (ATFM). | Unidade central de gerenciamento de fluxo (Network Manager). | [Fato][4] |
| ATOT | Actual Take-Off Time | Decolagem real (marco 16). | ATC. | [Fato][4] |

## 2.2.3 Correspondência com a máquina de estados do projeto

| Estado do turnaround (projeto) | Marco/horário A-CDM equivalente | Observação |
|---|---|---|
| Em solo | AIBT (marco 7) | [Inferência] Correspondência direta. |
| Operações em andamento | ACGT (marco 8) até AEGT | [Inferência] Correspondência direta. |
| Pronto para liberação | AEGT / ARDT (marco 12) | [Inferência] A condição de "pronto" do A-CDM ("ground handling is completed, all aircraft doors are closed and passenger bridges/gangways are removed, pushback truck available if required" [Fato][2], seção 5.1.11) pode virar a regra de transição deste estado. |
| Liberado | Sem equivalente direto | [Inferência] No A-CDM, depois do ARDT vêm ASRT e ASAT, que são atos do ATC. Como a integração com ATC está fora de escopo, "Liberado" precisa ser definido como um ato **interno** (liberação pela Autoridade de Liberação), e não como autorização de acionamento. Ver decisão [D4](../../docs/adr/0004-quatro-atores-e-autoridade-de-liberacao.md). |
| Fora de bloco | AOBT (marco 15) | [Inferência] Correspondência direta. |
| Em exceção | Alertas do A-CDM (ex.: CDM07, CDM08) e códigos de atraso | [Inferência] O A-CDM não tem um "estado de exceção"; tem alertas. O estado lateral do projeto é uma extensão razoável. |

---

## Ligações

- **Decisões:** [D1](../../docs/adr/0001-referencia-horario-tobt-mais-5-min.md), [D4](../../docs/adr/0004-quatro-atores-e-autoridade-de-liberacao.md), [D8](../../docs/adr/0008-siglas-a-cdm-com-nome-em-portugues.md)
- **Itens da especificação:** [Item 4 — Mapeamento de Negócios (BPMN TO BE)](../../especificacao/04-mapeamento-de-negocios.md), [Item 5 — Atores / Usuários](../../especificacao/05-atores-usuarios.md), [Item 6 — Requisitos Funcionais](../../especificacao/06-requisitos-funcionais/00-item.md), [Item 9 — Diagrama Geral de Casos de Uso](../../especificacao/09-diagrama-geral-de-casos-de-uso.md), [Item 11 — Diagrama de Atividades](../../especificacao/11-diagrama-de-atividades.md)
- **Áreas do plano RA1:** [Área A — Acesso e planejamento](../../especificacao/06-requisitos-funcionais/area-a.md), [Área B — Execução em solo](../../especificacao/06-requisitos-funcionais/area-b.md), [Área C — Monitoramento](../../especificacao/06-requisitos-funcionais/area-c.md), [Área D — Exceções e liberação](../../especificacao/06-requisitos-funcionais/area-d.md) (divisão em [entregas/ra1-tarefas.md](../../entregas/ra1-tarefas.md), tabela 1.2)
- **Relacionados:** [a-cdm](a-cdm.md), [tolerancias-e-indicadores](tolerancias-e-indicadores.md), [papeis-e-atores](papeis-e-atores.md), [atividades-e-dependencias](atividades-e-dependencias.md)
- **Fontes citadas:** 2, 3, 4, 7, 8 (em [fontes.md](../fontes.md))
- **Contexto geral:** [CONTEXT.md](../../CONTEXT.md) · [mapa da pesquisa](../README.md)
