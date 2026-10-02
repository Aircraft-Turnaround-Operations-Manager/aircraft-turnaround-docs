# Referências do Setor e Similares de Mercado

> **Aviso — versão consolidada congelada em 01/10/2026.** Este arquivo não é mais atualizado. A versão vigente está dividida por tema a partir do [mapa da pesquisa](README.md), e as decisões estão em [docs/adr/](../docs/adr/README.md). Em caso de diferença, valem as decisões e os arquivos vigentes.

> **Projeto:** TCC — Aircraft Turnaround Orchestration System (org. GitHub `Aircraft-Turnaround-Operations-Manager`)
> **Briefing de origem:** `pesquisa/00-briefing-pesquisa.md`
> **Elaborado por:** Claude (Cowork), para Rodrigo Alves (`rdsalvesPUC`), em 30/09/2026.
> **Data de acesso de todas as fontes:** 30/09/2026 (horário de Brasília), salvo indicação em contrário.
> **Status:** relatório de pesquisa. Não altera nenhum item da especificação; apenas recomenda.
> **Decisões:** as respostas do Rodrigo às decisões D1–D9 foram registradas na seção 5 em 01/10/2026.

**Convenções de leitura** (nota de cabeçalho):

- **[Fato]** = está na fonte citada entre colchetes (ex.: `[Fato][2]`). Citações literais ficam entre aspas, no idioma original.
- **[Inferência]** = conclusão deste relatório a partir das fontes; não está escrita na fonte.
- **(declarado pelo fornecedor)** = número ou capacidade anunciada por empresa em material próprio; não foi verificado de forma independente.
- **Não confirmado** = procurei e não encontrei fonte acessível que confirme.
- Os números entre colchetes remetem à seção 6 (Fontes).
- Siglas do setor ficam no original e são explicadas na primeira ocorrência. O glossário completo está na seção 2.2.

---

## 1. Resumo executivo

1. **[Fato]** O A-CDM (EUROCONTROL, ACI e IATA) organiza o turnaround em marcos com horários-alvo e responsáveis, com foco declarado em previsibilidade [1][2][4].
2. **[Inferência]** A referência de horário é o **TOBT** (prontidão), da companhia aérea e delegável ao *handling* ([Fato][2][5]).
3. **[Fato]** Seis aeroportos usam 5 min como janela de prontidão ou limiar de atualização do TOBT [7]–[12]; a EUROCONTROL alerta em TOBT + 5 [2]. **[Inferência]** Os 5 min do item 1 se confirmam, com referência no TOBT.
4. **Não confirmado:** meta pública de % para o TOBT. **[Inferência]** Os 95%, 5 s e 2 min do item 1 são metas internas, não do setor.
5. **[Inferência]** O princípio 1.2 está sustentado; encurtar o turnaround é decisão de programação (seção 2.4).
6. **[Fato]** Abastecer com passageiros é permitido sob condições pela EASA (Agência Europeia para a Segurança da Aviação) e pela ANAC (Agência Nacional de Aviação Civil) [26][27]. **[Inferência]** Essa dependência deve ser configurável.
7. **[Inferência]** Os 4 atores têm correspondência real; ajustar nome e descrição (seção 2.7.2).
8. **[Inferência]** Nenhum dos 5 similares documenta bloqueio de liberação com pendência nem caminho crítico explícito → diferencial sugerido DF1–DF4 (seção 3.4).
9. **[Inferência] O que muda na especificação:** usar "TOBT + 5 min" no item 1, declarar as metas internas, definir "risco" pelos gatilhos do A-CDM e adotar o vocabulário de marcos (seções 4 e 5).

---

## 2. Frente 1 — Padrões e práticas do setor

### 2.1 P1.1 — O que é o A-CDM, quem define e qual é o objetivo

- **[Fato][1]** A EUROCONTROL (organização europeia para a segurança da navegação aérea) define: "Airport CDM (A-CDM) aims to improve the efficiency and resilience of airport operations by optimising the use of resources and improving the predictability of air traffic." O conceito pede que "airport operators, aircraft operators, ground handlers and ATC" troquem informação "relevant accurate and timely", junto com o Network Manager europeu.
- **[Fato][1]** A página oficial informa que o A-CDM está "fully implemented in 34 airports across Europe" (ex.: Amsterdam, Frankfurt, London Heathrow, Paris CDG).
- **[Fato][1][2]** Documentos de referência atuais: o *Airport CDM Implementation Manual* (versão 5.0, 31/03/2017) e a *EUROCONTROL Specification for Airport Collaborative Decision Making (A-CDM)*, edição 1.0, de 30/01/2025.
- **[Fato][4]** O manual de implantação versão 5.0 é assinado em conjunto por ACI (Airports Council International), EUROCONTROL e IATA (International Air Transport Association).
- **[Fato][2]** A Especificação 2025 (seção 2.1) repete o objetivo de eficiência, resiliência e previsibilidade e descreve o objetivo dos processos de marcos como duplo: informar aos parceiros o ELDT (*Estimated Landing Time*, horário estimado de pouso) e informar "inconsistencies and updated predictions of Target Off-block, Start-up Approval and Take-Off Times" aos parceiros e ao Network Manager.
- **[Fato][5]** A IATA, nas suas recomendações de A-CDM (2018), escreve que o A-CDM melhora "flight predictability through real time data exchange" e que "Overall, A-CDM is about making more efficient use of existing capacity and resources".
- **[Fato][6]** O escritório Ásia-Pacífico da ICAO (Organização da Aviação Civil Internacional) publicou um FAQ de A-CDM (1ª ed., 02/07/2021) que cita como materiais-guia o Doc 9971 da ICAO, o manual da EUROCONTROL e recomendações de CANSO e IATA.
- **[Fato][57][58]** No Brasil, o Aeroporto de Guarulhos (GRU) foi anunciado como o primeiro aeroporto A-CDM do país em 05/11/2020, em projeto do DECEA (Departamento de Controle do Espaço Aéreo) com cooperação da EUROCONTROL. Em 2023, o DECEA apresentou o acompanhamento do A-CDM em GRU com participação de companhias aéreas e empresas de *ground handling* (atendimento em solo), com foco em "previsibilidade e pontualidade".
- **[Inferência]** O A-CDM é a referência mais forte para o vocabulário do nosso sistema: ele trata o turnaround como uma sequência de marcos com horários-alvo e responsáveis definidos. Ele **não** define como orquestrar as tarefas internas do turnaround (quem faz limpeza, em que ordem). Essa camada fica com o *ground handler* e é justamente onde o nosso produto atua.

### 2.2 P1.2 — Marcos (milestones) e horários do A-CDM ligados ao turnaround

#### 2.2.1 Os 16 marcos do A-CDM

**[Fato][2][3]** A Especificação 2025 numera 16 marcos (MST, *milestone*), mais três marcos de degelo (D1 a D3) que não entram no nosso escopo:

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

#### 2.2.2 Glossário de horários (sigla, nome, significado, quem atualiza)

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

#### 2.2.3 Correspondência com a máquina de estados do projeto

| Estado do turnaround (projeto) | Marco/horário A-CDM equivalente | Observação |
|---|---|---|
| Em solo | AIBT (marco 7) | [Inferência] Correspondência direta. |
| Operações em andamento | ACGT (marco 8) até AEGT | [Inferência] Correspondência direta. |
| Pronto para liberação | AEGT / ARDT (marco 12) | [Inferência] A condição de "pronto" do A-CDM ("ground handling is completed, all aircraft doors are closed and passenger bridges/gangways are removed, pushback truck available if required" [Fato][2], seção 5.1.11) pode virar a regra de transição deste estado. |
| Liberado | Sem equivalente direto | [Inferência] No A-CDM, depois do ARDT vêm ASRT e ASAT, que são atos do ATC. Como a integração com ATC está fora de escopo, "Liberado" precisa ser definido como um ato **interno** (liberação pela Autoridade de Liberação), e não como autorização de acionamento. Ver decisão D4. |
| Fora de bloco | AOBT (marco 15) | [Inferência] Correspondência direta. |
| Em exceção | Alertas do A-CDM (ex.: CDM07, CDM08) e códigos de atraso | [Inferência] O A-CDM não tem um "estado de exceção"; tem alertas. O estado lateral do projeto é uma extensão razoável. |

### 2.3 P1.3 — Indicadores e tolerâncias usados para medir aderência

#### 2.3.1 Regras e tolerâncias do TOBT, do TSAT e da prontidão

| # | Regra / tolerância | Valor exato | Fonte |
|---|---|---|---|
| T1 | Precisão exigida do TOBT (Heathrow) | "The TOBT must be maintained to an accuracy of +/- 5 minutes" | [Fato][7] seção 2.4.1 |
| T2 | Janela de tolerância do TOBT (Zurique) | "The TOBT has a tolerance window of +/– 5 minutes. The aircraft must be ready for push back and/or start up within this tolerance window." | [Fato][10] |
| T3 | Atualização obrigatória do TOBT (Dublin) | "All AO and HA at Dublin Airport must communicate any change to their TOBT of +/- 5 minutes or greater." (AO = companhia aérea; HA = *handling agent*) | [Fato][8] seção 4.8 |
| T4 | Atualização obrigatória do TOBT (Toronto) | "TOBT must be updated if it is different from the previous TOBT by 5 minutes or more." | [Fato][9] |
| T5 | Atualização obrigatória do TOBT (Incheon) | "If the prediction of departure readiness (new TOBT) differs more than 5 minutes (plus or minus) from the previous TOBT, AO or GHA shall update TOBT." (GHA = *ground handling agent*) | [Fato][12] seção 3.2.c |
| T6 | Atualização obrigatória do TOBT (Changi) | Atualizar o TOBT se a previsão diferir em 5 min ou mais, até o início do push-back. | [Fato][11] seção 3.5 |
| T7 | Modificações mínimas (Zurique) | "only modifications of 5 min. or more are permitted"; a última atualização deve ocorrer até 5 min antes do TOBT vigente. | [Fato][10] |
| T8 | Prontidão não registrada (Especificação EUROCONTROL) | "In case the Aircraft Ready status has not been recorded at TOBT +5 minutes at the latest, the TOBT Responsible Person (AO/GH) is informed that TOBT has passed". | [Fato][2] seção 5.1.11 |
| T9 | Recomendação da IATA | "Irrespective of the TSAT, the aircraft must be ready for departure at the TOBT +/- X minutes" (o valor X fica a cargo da regra local; no PDF o X aparece seguido de um número de nota). | [Fato][5]; leitura do "X" como parâmetro local = [Inferência] |
| T10 | Discrepância TOBT × EOBT | Alerta CDM08 quando TOBT e EOBT diferem 15 min ou mais; em Heathrow e Dublin, atraso ≥15 min exige mensagem DLA (atualização do plano de voo). | [Fato][3] seção 5.1.2; [7] seção 2.4.1; [8] seção 4.10 |
| T11 | Viabilidade do turnaround | Alertas CDM07/CDM07a quando EIBT + MTTT fica fora dos limites em relação ao EOBT/TOBT. Em Heathrow, no TOBT − 50 min, se "EIBT + the MTT exceeds the current TOBT", o voo é considerado "under stress". | [Fato][3] (seção não identificada na leitura); [7] seção 2.4.1 |
| T12 | Embarque não iniciado | "If the boarding has not commenced at a given time (local variable) prior to TOBT, an Alert Message is sent indicating that the TOBT might not be respected." | [Fato][2] seção 5.1.10 |
| T13 | Emissão do TSAT | Entre 40 e 30 min antes do TOBT (Especificação); TOBT − 40 em Dublin; TOBT − 30 em Heathrow. | [Fato][3] seção 5.1.9; [8] seção 4.14; [7] seção 2.4.2 |
| T14 | Janela de pedido de acionamento | Alerta se a autorização não for dada até TSAT + 5 min; TSAT removido se não houver pedido até TSAT + 10 min. Em Heathrow, "The compliance window within which the pilot calls for actual start request is +/- 5 minutes". | [Fato][3] seções 5.1.12 e 5.1.13; [7] seção 2.4.1 |
| T15 | Off-block após autorização | Alerta se o AOBT não for registrado até ASAT + 5 min. | [Fato][3] seção 5.1.14 |
| T16 | Convenção de tolerância | "5:59 is acceptable while 6:00 is not" (tolerâncias contadas em minutos completos). | [Fato][3] seção 1.4 |

**[Inferência]** O valor de **5 minutos** em torno do TOBT é consistente nas fontes consultadas, em dois papéis: como **janela de prontidão** (Heathrow T1, Zurique T2, janela do piloto em Dublin [8] seção 4.22.1, alerta da EUROCONTROL T8) e como **limiar de atualização** do TOBT (Dublin T3, Toronto T4, Incheon T5, Changi T6, Zurique T7). A IATA deixa o valor como parâmetro local (T9). Ela vale **nos dois sentidos** (±5): ficar pronto muito antes também é desvio de previsão e exige atualizar o TOBT. A regra de alerta da Especificação (T8), porém, é **unilateral** (TOBT + 5).

#### 2.3.2 Indicadores (KPIs) de aderência e pontualidade

| # | Indicador | Definição / valor | Fonte |
|---|---|---|---|
| K1 | Pilot Missed Calls (Heathrow) | "% of flights where the pilot called within +/- 5 minutes of the TOBT". | [Fato][7] seção 3.3.2.6 |
| K2 | Late Updaters (Heathrow) | "% of flights where an TOBT was updated within 10 minutes of the TOBT time". | [Fato][7] seção 3.3.2.6 |
| K3 | Predictability (Heathrow) | "% of flights with all new TOBT updates giving at least 10 minutes future notice". | [Fato][7] seção 3.3.2.6 |
| K4 | TOBT Quality (Heathrow) | "average of the three measures above". | [Fato][7] seção 3.3.2.6 |
| K5 | Pontualidade (Heathrow, faixas) | Verde: "at least 79% of flights operated within 3 or 15 minutes of the scheduled time"; âmbar: entre 59% e 79%; vermelho: menos de 59%. | [Fato][7] seções 3.3.2.2–3.3.2.3 |
| K6 | Indicadores monitorados (Incheon) | "Airport performance indicator (TOBT accuracy, TSAT compliance and departure punctuality, etc.) will be monitored." Sem meta numérica publicada. | [Fato][12] seção 2.3.d |
| K7 | On-time performance (padrão de mercado) | Partida pontual = "departs from the gate within 15 minutes of its scheduled departure time". | [Fato][17] |
| K8 | Aderência ao slot ATFM (Europa) | "The percentage of departures inside an ATFM slot tolerance window of [-5 minutes, +10 minutes]"; unidades ATS (serviços de tráfego aéreo) devem reportar quando a não aderência for igual ou maior que 20% das partidas reguladas. | [Fato][15] |
| K9 | Pontualidade europeia 2023 | "67.9% of flights departing within 15 minutes or earlier than their scheduled departure time". | [Fato][16] |

#### 2.3.3 Linha de base: quão preciso o TOBT costuma ser

- **[Fato][14]** Avaliação de impacto do A-CDM feita pela EUROCONTROL (publicada em 2016, quando 20 aeroportos tinham A-CDM completo): o desvio-padrão da precisão da decolagem caiu "from an average of 14 minutes to around 7 and 5 minutes at the sequencing and off-block milestones respectively"; ganho médio de aderência ao horário entre 0,5 e 2 min por voo.
- **[Fato][18]** (declarado pelo fornecedor Veovo, 2022) O TOBT de muitos grandes aeroportos é "less than 60% accurate to within 5 minutes".
- **[Fato][19]** (declarado pelo fornecedor Assaia) A imprecisão média do TOBT é "rather consistent at four to five minutes", e 68% dos voos têm imprecisão de ±11 min ou mais; em um aeroporto, 40% dos voos perderam a janela do TSAT.
- **Não confirmado:** meta percentual pública e oficial para precisão do TOBT (ex.: "X% dos voos dentro de ±5 min"). Os modelos de medição de TOBT/TSAT publicados pela ICAO (escritório WACAF, 2025) retornaram erro 403 e não foram lidos.

### 2.4 P1.4 — O setor valoriza mais a previsibilidade do que a velocidade?

**Evidências a favor do princípio 1.2 (previsibilidade e aderência ao plano):**

1. **[Fato][1][2]** O objetivo declarado do A-CDM inclui "improving the predictability of air traffic".
2. **[Fato][5]** A IATA: "Irrespective of the TSAT, the aircraft must be ready for departure at the TOBT +/- X minutes" e "A-CDM is about making more efficient use of existing capacity and resources". O alvo é ficar pronto **no** TOBT, não antes.
3. **[Fato][7]** Heathrow define o papel do *handling*: "Ground Handlers/Turnaround Managers: Work towards getting the aircraft ready to meet its TOBT, irrespective of the TSAT assigned, and update TOBT if required." O índice "TOBT Quality" mede **qualidade da previsão** (aviso com antecedência, atualizações tardias), não a duração do turnaround.
4. **[Fato][13]** O cartão de rampa dos aeroportos alemães (v3.1, dez/2023) manda comunicar ao responsável pelo TOBT qualquer desvio "regardless of whether the ground handling will end early or late". Terminar antes sem avisar também é falha de previsibilidade.
5. **[Fato][20]** Schultz (2018): "To provide a reliable time stamp for the TOBT, the critical path of the turnaround has to be under the control of the operational entities."
6. **[Fato][16][23]** Atrasos reacionários (efeito dominó entre voos) são 46% dos minutos de atraso na Europa em 2023 (CODA, *Central Office for Delay Analysis* da EUROCONTROL); Rodríguez-Sanz e Herrera de la Cruz (2020) registram que eles "usually represent 40%-45% of all generated delay minutes" e que folgas ("buffers", "fire break time") são usadas para conter a propagação.
7. **[Fato][25]** O projeto BPM da TU Dresden (com a EUROCONTROL) buscou estratégias de controle do turnaround para manter os horários-alvo acordados entre os parceiros, "particularly the planned pushback time".

**Evidências em outra direção (encurtar o turnaround como meta):**

1. **[Fato][32]** (fonte jornalística) Companhias de baixo custo como a Ryanair trabalham com turnaround-alvo de 25 min, porque "Aircraft on the ground aren't making airlines money".
2. **[Fato][21]** Płanda e Skorupski (2025) citam que "a reduction of one minute in the boarding time results in savings of USD 50 million per year" para grandes companhias.
3. **[Fato][22]** Kierzkowski et al. (2025) estudam o custo de reduzir o tempo do *ground handling*: "moderate time reductions are attainable at reasonable cost, whereas aggressive targets that lie below the structural minimum are infeasible".
4. **[Fato][42]** (declarado pelo fornecedor Assaia) Um estudo de caso anuncia redução da duração do turnaround de cerca de 40 para 35 min (mais de 12%) com alertas em tempo real.
5. **[Fato][20]** O próprio artigo de Schultz (2018) se chama *Fast Aircraft Turnaround Enabled by Reliable Passenger Boarding*: velocidade e confiabilidade aparecem juntas.

**Síntese [Inferência]:**

- O princípio 1.2 **está sustentado** para o nível operacional do dia: no A-CDM, a meta do *handling* é deixar a aeronave pronta **no TOBT, dentro de ±5 min**, e a qualidade é medida pela previsão, não pela rapidez.
- A busca por turnaround mais curto existe, mas é uma decisão **de programação** da companhia (quanto tempo de solo planejar, ou seja, o MTTT e o par SIBT/SOBT). Isso confirma a fronteira já decidida: reduzir o turnaround programado mexe na malha e fica fora do sistema.
- Ajuste fino recomendado: o sistema não deve "premiar" terminar antes, mas deve **exigir que a antecipação vire informação** (atualizar a previsão quando a diferença chegar a 5 min), porque isso é exigido pelas regras de TOBT (T3 a T7) e pelo cartão de rampa [13].

### 2.5 P1.5 — Atividades típicas, paralelismo e dependências

**[Fato][20][23]** A literatura descreve o turnaround como "five major tasks": "deboarding, catering, cleaning, fueling, and boarding", mais "the parallel processes of unloading and loading". **[Fato][22]** Kierzkowski et al. (2025) detalham 12 tarefas: calçar a aeronave, posicionar escada/ponte, desembarque, serviço de cabine, embarque, retirada da escada, descarregamento de bagagem, carregamento de bagagem, abastecimento, serviço de lavatório, reposição de água e retirada dos calços. **[Fato][31]** A SKYbrary lista entre os serviços de rampa: carregamento e descarregamento, abastecimento, "toilet and water servicing", limpeza, catering, documentação, degelo e push-back.

| # | Atividade | Executante típico | Começa depois de | Pode correr em paralelo com | Marco / observação | Fonte |
|---|---|---|---|---|---|---|
| A1 | Calçar a aeronave e posicionar ponte ou escada | Agente de rampa | Chegada à posição (AIBT) | — | "Ground handling begins with the locking of the aircraft's wheels and the placement of a passenger ramp" | [Fato][21][22] |
| A2 | Desembarque de passageiros | *Handling* de passageiros / tripulação | A1 | A3 e A7; A4 só sob regra especial (ver abaixo) | "passenger disembarkation and baggage unloading" podem ser simultâneos | [Fato][22] |
| A3 | Descarregamento de bagagem e carga | Equipe de carregamento (rampa) | A1 | A2, A4, A7 | Processo paralelo ao fluxo de passageiros | [Fato][20][22] |
| A4 | Abastecimento | Fornecedor de combustível | A1; com passageiros a bordo, só com procedimento aprovado | A3, A5, A6, A7 | Código de atraso 36 "FUELLING DEFUELLING, fuel supplier" | [Fato][16][26][27]; paralelismo = [Inferência] |
| A5 | Limpeza da cabine | Equipe de limpeza | Fim de A2 | A4, A6, A7, A3 | "aircraft cleaning can only take place after passengers have left" | [Fato][22] |
| A6 | Catering | Empresa de catering | Fim de A2 | A5, A4, A7 | "All passengers must disembark before catering teams board" (resumo do artigo) | [Fato][29] |
| A7 | Água potável e serviço de lavatório | Agente de rampa | A1 | Quase todas | Listado como tarefa própria | [Fato][22][31] (existência da tarefa); dependências = [Inferência] |
| A8 | Inspeção técnica de trânsito | Manutenção | A1 | Quase todas | Códigos 41–43 cobrem defeito e manutenção | [Fato][16][31] (existência da tarefa); dependências = [Inferência] |
| A9 | Embarque | *Handling* de passageiros | Fim de A5; fim de A4 se o operador não abastece com passageiros. Esperar também o fim de A6 = [Inferência] | A10 | Marco 11 (ASBT); alerta se não começar até TOBT − X (variável local) | [Fato][2][24][29] |
| A10 | Carregamento de bagagem e carga | Equipe de carregamento | Fim de A3 = [Inferência] | A9 | Descarregar e carregar são "parallel processes" ao fluxo de passageiros | [Fato][20] |
| A11 | Documentação de peso e balanceamento (loadsheet) | Controle de carga (*load control*) | Fim de A9 e A10 | — | "Final paperwork (weight/balance figures) requires complete passenger and baggage loading"; código 31 | [Fato][16][29] |
| A12 | Fechar portas e retirar ponte/escada | *Handling* / tripulação | Fim de A9, A10 e A11 | — | Condições do marco 12 "Aircraft Ready" | [Fato][2][29] |
| A13 | Push-back e retirada dos calços | Agente de rampa (trator) | A12 + autorização do ATC (fora de escopo) | — | Marco 15 (AOBT); código 39 cobre falta ou pane de trator | [Fato][2][16] |

*Nota sobre a tabela:* nas colunas "Começa depois de" e "Pode correr em paralelo com", são [Fato] apenas as relações sustentadas pela citação da coluna "Marco / observação" ou pela fonte da linha (A1, A2 ∥ A3, A5 e A6 depois de A2, A9 depois de A5, A11, A12). As demais relações são [Inferência] a partir da descrição geral do processo.

**Restrições de segurança — abastecimento com passageiros a bordo:**

- **[Fato][26]** Regra europeia CAT.OP.MPA.195: "An aircraft shall not be refuelled/defuelled with Avgas or wide-cut type fuel when passengers are embarking, on board or disembarking." Para os demais combustíveis, "necessary precautions shall be taken and the aircraft shall be properly manned by qualified personnel ready to initiate and direct an evacuation."
- **[Fato][27]** Regra brasileira, RBAC 91 (Emenda 05, 01/04/2025), seção 91.102(g): o abastecimento com passageiros a bordo, embarcando ou desembarcando só é permitido se houver (1) procedimento aprovado e um tripulante de voo na cabine supervisionando; (2) no mínimo 50% dos comissários requeridos e/ou pessoas treinadas para dirigir evacuação, com meios de evacuação disponíveis; (3) motores desligados (exceto APU, a unidade auxiliar de energia); e (4) comunicação entre o pessoal de solo e a cabine dos pilotos. *Emendas posteriores à 05 não foram conferidas.*
- **[Fato][28]** A Airbus (briefing de 2007) lista precauções: sinal de "NO SMOKING" aceso, "FASTEN SEAT BELT" apagado, saídas de emergência desobstruídas e área sob as saídas livre de equipamentos.
- **[Fato][24]** Há modelos acadêmicos que adotam a regra mais restritiva: "The refuelling procedure cannot begin until the disembarking has ended, as well as boarding cannot begin until refuelling has finished".
- **[Inferência]** Abastecer com passageiros é **permitido sob condições**, e a escolha é de cada operador. Por isso, a dependência entre abastecimento, desembarque e embarque deve ser uma **regra configurável** do modelo de tarefas, não uma dependência fixa. Ela muda o caminho crítico (ver 2.6).

**Pontos de verificação usados na prática [Fato][13]:** o cartão de rampa dos aeroportos alemães manda, no **TOBT − 15 min**, conferir com tripulação, portão/embarque, carregamento, abastecimento, limpeza e catering se todos estão no prazo, e ajustar o TOBT se preciso; no **TOBT − 3 min**, conferir se a ponte ou escada foi removida e se todas as portas estão fechadas. **[Inferência]** Esses dois instantes são bons candidatos a eventos de temporizador no BPMN (item 4) e a regras do Motor de Eventos.

### 2.6 P1.6 — Caminho crítico no turnaround

- **[Fato][24]** Definição usada na literatura de turnaround: as atividades do caminho crítico são aquelas em que "any delay in them would increase the total time of the project". No modelo de Sanz de Vicente (2010), o caminho crítico passa por desembarque, limpeza, carregamento e embarque.
- **[Fato][20][21]** O embarque aparece como atividade crítica: "boarding is on the critical path of the aircraft 4D trajectory and not controlled by the operators" (Schultz, 2018); "Boarding is one of the most critical parts of the ground handling [...] as it lies on the critical path of the turnaround process" (Płanda e Skorupski, 2025).
- **[Fato][20]** Schultz liga caminho crítico e previsão: para um TOBT confiável, "the critical path of the turnaround has to be under the control of the operational entities"; e "The stochastic and passenger-controlled progress of aircraft boarding makes it difficult to reliably predict the turnaround time".
- **[Fato][22]** Kierzkowski et al. (2025), com o método PERT, encontram o caminho crítico "A, B, C, D, E, F, L" com 21,3 min, e observam que, nos cenários otimista e mais provável, "the longest activity is related to refuelling the aircraft". *A correspondência exata letra → atividade não foi confirmada na leitura.*
- **[Fato][45]** No mercado, o módulo TurnManager do INFORM GroundStar calcula "automatically" o impacto de uma irregularidade "on dependent processes and flight delays".
- **[Inferência]** Leitura para o projeto:
  - O caminho crítico típico é a cadeia de **passageiros e cabine**: desembarque → limpeza (e catering) → embarque → fechamento de portas. Bagagem, água/lavatório e inspeção costumam ter folga.
  - O abastecimento entra no caminho crítico quando o operador **não** permite abastecer com passageiros, porque passa a ficar entre desembarque e embarque.
  - O caminho crítico muda durante o turnaround: tarefa marcada "Não aplicável", tarefa atrasada ou regra de abastecimento alteram a cadeia mais longa. Por isso ele precisa ser **recalculado a cada evento**, e não fixado no planejamento.
  - O MTTT (tempo mínimo de turnaround) do A-CDM [4] é, na prática, a duração do caminho crítico nominal; é o parâmetro natural para a checagem de viabilidade EIBT + MTTT ≤ TOBT (T11).

### 2.7 P1.7 — Papéis reais e comparação com os 4 atores do projeto

#### 2.7.1 Papéis encontrados nas fontes

| Papel real | O que faz no turnaround | Fonte |
|---|---|---|
| Companhia aérea (*Aircraft Operator*, AO) | Dona do plano de voo; "responsible for the TOBT and any updates", podendo delegar ao *ground handler*. A IATA diz que o TOBT é "owned by the airline". | [Fato][2] seção 4.7; [5] |
| *Ground handler* (GH) / "TOBT Responsible Person" | Executa o atendimento em solo; assume o TOBT quando a companhia delega. | [Fato][2] seção 4.6; [13] |
| Turnaround Coordinator / Turnaround Manager / Dispatcher | "responsible for coordinating all functions around the aircraft to enable a safe, secure and on time departure, whilst following airline specific procedures" (Menzies). Em Heathrow, "Ground Handlers/Turnaround Managers" trabalham para cumprir o TOBT. | [Fato][30]; [7] seção 2.5; [29] |
| Equipes e prestadores de rampa | Carregamento, abastecimento, limpeza, catering, água/lavatório, push-back. Vários são empresas diferentes (os códigos IATA citam "fuel supplier" e "late delivery" de catering). | [Fato][13][16][31] |
| Controle de carga (*load control*) | Prepara a documentação de peso e balanceamento (código 31). | [Fato][16] |
| Tripulação / comandante | Reporta "pronto" e pede acionamento; em Dublin, "The Pilot shall ensure that the flight is ready to depart at TOBT (window of -/+5 minutes)". | [Fato][2] seção 5.1.11; [8] seção 4.22.1 |
| Operador do aeroporto / centro de operações (AOC/APOC) | "responsible for the operational management of the airport"; pode atualizar o status de pronto no A-CDM System; no estudo de caso da Assaia, um "AOC operative" recebe o alerta e liga para o *handling*. | [Fato][2] seções 4.2 e 5.1.11; [42] |
| Controle de tráfego aéreo (ATC) | Registra ARDT, emite TSAT e autoriza acionamento e push-back. | [Fato][2][3] |
| Network Manager | Gerenciamento de fluxo (ATFM) e CTOT. | [Fato][2] seção 4.8; [4] |
| Sistema A-CDM / plataforma de informação | Calcula horários (EIBT, TOBT inicial, TTOT) e envia alertas (CDM07, CDM08). No Brasil, o anúncio de GRU cita a ACISP (*Airport Collaborative Information Sharing Platform*). | [Fato][2][3][57] |

**Quem declara a aeronave pronta? [Fato][2][4]** No A-CDM, o marco "Aircraft Ready" (ARDT) é registrado pelo controlador "When the flight reports ready", ou pelas operações do aeroporto no A-CDM System. O *ground handler* marca o fim do atendimento (AEGT, que "can be equal to ARDT"). **[Inferência]** Não existe, nas fontes, um papel único chamado "autoridade de liberação": a prontidão resulta de três atos — o *handling* encerra o atendimento, a tripulação reporta pronto e o ATC autoriza o acionamento.

#### 2.7.2 Comparação com os atores do projeto

| Ator do projeto | Papel(éis) real(is) correspondente(s) | Aderência [Inferência] | Sugestão [Inferência] |
|---|---|---|---|
| Operador de Solo/Rampa | Equipes e prestadores de rampa (carregamento, abastecimento, limpeza, catering, água/lavatório, push-back) | Alta | Descrever como "executante de tarefas do turnaround, da própria empresa de *handling* ou de prestador contratado". Isso explica por que o sistema precisa de responsável por tarefa. |
| Coordenador/Supervisor de Turnaround | Turnaround Coordinator/Manager; também o "TOBT Responsible Person" quando a companhia delega | Alta | Usar **um único nome** em todos os itens (critério K.1). "Coordenador de Turnaround" é o termo mais próximo do setor. Incluir na descrição: manter atualizado o horário planejado de prontidão (TOBT). |
| Autoridade de Liberação | Sem papel único. O mais próximo é o representante da companhia aérea/comandante, que confirma a prontidão depois que o *handling* encerra o atendimento | Parcial | Manter o ator (separa quem executa de quem libera, o que sustenta a métrica "0 liberações com pendência"), mas descrevê-lo como "representante da companhia aérea que confirma a prontidão da aeronave (equivalente ao marco Aircraft Ready do A-CDM)", deixando claro que **não** é a autorização do ATC. Ver D4. |
| Motor de Eventos | Sistema A-CDM / plataforma de informação compartilhada | Alta | Descrever como "componente que recebe os registros, recalcula projeções e caminho crítico e emite alertas", citando o A-CDM System como analogia. |
| (sem ator) | ATC, Network Manager, AOC/APOC | — | ATC e Network Manager ficam fora (integração com ATC fora de escopo). O AOC pode, no máximo, aparecer como consumidor do painel; não é necessário como ator no MVP. |

### 2.8 P1.8 — Causas de atraso padronizadas e o que cabe ao turnaround

**[Fato][16]** O padrão de mercado são os códigos de atraso de dois dígitos da IATA (AHM 730), reproduzidos no anexo do relatório CODA da EUROCONTROL. A EUROCONTROL agrupa as causas em "Airline, Airport, ATFM, Weather, Other" e "Reactionary". **[Fato][1]** Em aeroportos A-CDM, "the target off-block time (TOBT) values reflect any delays that can be attributed to the aircraft operator (AO) or to the ground handling operations."

Códigos mais ligados ao turnaround (texto literal do anexo [16]):

| Código | Descrição IATA (original) | Responsabilidade do turnaround? [Inferência] |
|---|---|---|
| 15 (PH) | BOARDING, discrepancies and paging, missing checked-in passenger | Sim (embarque) |
| 17 (PC) | CATERING ORDER, late or incorrect order given to supplier | Parcial (pedido é da companhia) |
| 18 (PB) | BAGGAGE PROCESSING, sorting etc. | Parcial (antes da rampa) |
| 19 (PW) | REDUCED MOBILITY, boarding deboarding of passengers with reduced mobility | Sim |
| 31 (GD) | AIRCRAFT DOCUMENTATION LATE INACCURATE, weight and balance | Sim (*load control*) |
| 32 (GL) | LOADING UNLOADING, bulky, special load, cabin load, lack of loading staff | Sim |
| 33 (GE) | LOADING EQUIPMENT, lack of or breakdown, lack of staff | Sim (recurso) |
| 34 (GS) | SERVICING EQUIPMENT, lack of or breakdown, lack of staff, e.g. steps | Sim (recurso) |
| 35 (GC) | AIRCRAFT CLEANING | Sim |
| 36 (GF) | FUELLING DEFUELLING, fuel supplier | Sim |
| 37 (GB) | CATERING, late delivery or loading | Sim |
| 38 (GU) | ULD, lack of or serviceability (ULD = *unit load device*, contêiner/palete de carga) | Sim |
| 39 (GT) | TECHNICAL EQUIPMENT, lack of or breakdown, lack of staff, e.g. pushback | Sim (recurso) |
| 41 (TD) | AIRCRAFT DEFECTS | Parcial (manutenção) |
| 42 (TM) | SCHEDULED MAINTENANCE, late release | Parcial (manutenção) |
| 43 (TN) | NON-SCHEDULED MAINTENANCE, special checks and or additional works beyond normal maintenance schedule | Parcial (manutenção) |
| 52 (DG) | DAMAGE DURING GROUND OPERATIONS, collisions, loading off-loading damage | Sim (exceção de segurança) |
| 63 (FT) | LATE CREW BOARDING OR DEPARTURE PROCEDURES, other than connection and standby (flight deck or entire crew) | Não (tripulação) |
| 66 (FL) | LATE CABIN CREW BOARDING OR DEPARTURE PROCEDURES, other than connection and standby | Não (tripulação) |
| 75 (WI) | DE-ICING OF AIRCRAFT, removal of ice and or snow, frost prevention excluding unserviceability of equipment | Parcial (degelo fora do MVP) |
| 77 (WG) | GROUND HANDLING IMPAIRED BY ADVERSE WEATHER CONDITIONS | Parcial |
| 87 (AF) | AIRPORT FACILITIES, parking stands, ramp congestion, lighting, buildings | Não (aeroporto) |
| 93 (RA) | AIRCRAFT ROTATION, late arrival of aircraft from another flight | Não — atraso reacionário que **chega** ao turnaround |

- **[Fato][37]** A IATA tem um novo esquema de códigos, o **AHM 732**, divulgado em webinar próprio. **[Fato][38]** (fonte de fornecedor, blog Cosmos, 22/07/2025) O AHM 732 troca os dois dígitos por três letras — processo, motivo e parte envolvida (*stakeholder*) — e, segundo o blog, os códigos AHM 730/731 valem "until the 43rd edition", com o AHM 732 virando padrão a partir da 44ª edição. *O cronograma não foi confirmado em documento oficial da IATA.*
- **[Inferência]** Para o MVP, os códigos de dois dígitos do grupo 31–39 (mais 15, 19 e 52) cobrem as causas atribuíveis ao turnaround e têm texto público verificável. O código 93 é útil como causa **de entrada** (aeronave chegou atrasada), que o sistema registra mas não trata.

### 2.9 P1.9 — Referências da IATA sobre ground handling

| Referência | O que cobre (segundo a própria IATA) | Fonte |
|---|---|---|
| AHM — Airport Handling Manual | "The AHM contains all the industry-approved policies and standards to support safe and efficient ground operations above and below the wing." Orientado a política ("what to do"). A página lista 11 capítulos, entre eles manuseio de aeronave e carregamento, controle de carga, controle de movimento de aeronaves, acordos de *ground handling*, especificações de equipamentos de apoio e programa de treinamento. A página apresenta a 47ª edição (2027). | [Fato][33][35] |
| IGOM — IATA Ground Operations Manual | "standardizes ground handling processes and procedures to reduce the complexity between working with multiple airlines, airports and ground service providers". Orientado a procedimento ("how to do"). Seis capítulos; o capítulo 4 é "Aircraft turnaround" (chegada, portas, partida, reboque). Complementar ao AHM e referência para auditorias ISAGO. A página apresenta a 15ª edição (2027). | [Fato][33][34] |
| ISAGO — IATA Safety Audit for Ground Operations | "global safety oversight program" para prestadores de *ground handling* (GHSP), com auditorias na sede e nas estações, verificando conformidade com IGOM, AHM e o manual de carga (ICHM); registro e acreditação valem 24 meses. | [Fato][36] |
| AHM 730/731 e AHM 732 | Códigos de atraso (ver 2.8). | [Fato][16][37] |
| BRM — Baggage Reference Manual | Boas práticas de bagagem. | [Fato][33] |

- **Não confirmado:** o conteúdo integral do AHM e do IGOM (são publicações pagas; só os sumários públicos foram lidos) e o número exato do capítulo do *Standard Ground Handling Agreement* (SGHA). A página do AHM só confirma que existe um capítulo de "Ground handling agreements".
- **[Inferência]** Para a especificação, o IGOM é a melhor referência a citar no item 3 (padronização de procedimentos de turnaround) e o ISAGO no item 8 (auditoria e rastreabilidade), sem afirmar conteúdo que não foi lido.

---

## 3. Frente 2 — Similares de mercado

### 3.1 Seleção

Foram analisados **5 produtos**, cobrindo os três tipos pedidos no briefing (a classificação por tipo é [Inferência] a partir das fichas):

| Tipo | Produtos |
|---|---|
| Gestão e orquestração de *ground handling* | INFORM GroundStar |
| Monitoramento por visão computacional ou sensores | Assaia (ApronAI / TurnaroundControl); ADB SAFEGATE (Safedock + Apron Manager) |
| Plataforma de operações aeroportuárias / A-CDM | Veovo (A-CDM); SITA (Airport Management + Collaborative Decision Making) |

Candidatos verificados e **não** incluídos:

- **Amadeus:** a única fonte encontrada sobre o escopo de turnaround foi uma folha de vendas do AODB (*Airport Operational Database*, base de dados operacional do aeroporto) de 2014 [Fato][59]; sem fonte atual, o escopo não foi confirmado.
- **Cosmos (Cosmos Solutions GmbH):** a página do produto descreve gestão de SLA (acordo de nível de serviço), qualidade e atrasos entre companhias, aeroportos e prestadores [Fato][60], não orquestração de tarefas do turnaround. Foi usada só como fonte secundária sobre códigos de atraso.

**Lembrete:** tudo o que vem de site de fornecedor é **declarado pelo fornecedor**. "Não informado" significa que a fonte pública lida não diz; não significa que o produto não tenha.

### 3.2 Fichas de análise

#### Ficha 1 — Assaia (ApronAI e TurnaroundControl)

| Campo | Registro |
|---|---|
| Produto e fornecedor | ApronAI e TurnaroundControl (também ResourceManager, SafetyControl, EmissionsControl). Assaia International AG, Zurique, **Suíça**, com escritórios na Alemanha e nos EUA. https://www.assaia.com [Fato][39] |
| Público-alvo | "Airports, airlines, ground handlers" [Fato][39]; o TurnaroundControl cita companhias aéreas, *ground handlers*, "departure coordinators" e "gate managers", com clientes como United e Alaska Airlines [Fato][40]. |
| Problema que resolve | "Optimize aircraft turnarounds with AI & computer vision." [Fato][39] |
| Funcionalidades | Câmeras no pátio geram "accurate timestamps for turnaround events" em tempo real [Fato][41]; painel com widgets coloridos por atividade em vários portões e vídeo ao vivo; *watchlist* de turnarounds; alertas com "Airline-specific business logic"; previsão de off-block (POBT) e de prontidão (PRDT); fila de partida; mapa multi-aeroporto; integra progresso do embarque e leitura de bagagem [Fato][40]; auditoria de SLA e detecção de violações de segurança [Fato][39]. |
| Como trata atrasos e exceções | Notificações instantâneas, com foco em "handling exceptions, rather than multitasking" [Fato][40]. Exemplo real de regra: alerta quando a "cleaning team has not been detected on the aircraft stand within 3 minutes after passenger offboarding has ended"; o alerta vai para um "AOC operative who then calls the respective ground handler service provider" [Fato][42]. |
| Fonte do dado operacional | Câmeras e visão computacional [Fato][39][41], mais integrações (embarque, bagagem) [Fato][40]. |
| Métricas divulgadas — [Fato] (declarado pelo fornecedor) | +17% de pontualidade, −5 min de atraso em solo, −50% de comportamento inseguro; 2.895.340 turnarounds monitorados em 31 aeroportos [39]; Alaska −3,9 min e United −2 min de atraso médio em solo [40]; turnaround de ~40 para ~35 min (>12%) em um aeroporto médio [42]. |
| Relação com A-CDM | Declara melhorar o A-CDM "through more accurate predictive off block time (POBT)" [Fato][39]; compara o TOBT manual com o POBT [Fato][19]. |
| O que vale incorporar [Inferência] | (1) Regra de alerta por dependência: "sucessora não iniciada X min após o fim da predecessora"; (2) *watchlist* de turnarounds em risco; (3) status por cor por atividade; (4) projeção de prontidão (equivalente ao PRDT) recalculada a cada evento. |
| O que fica fora do nosso escopo [Inferência] | Visão computacional e câmeras (exige infraestrutura; o MVP usa registro do operador); monitoramento de emissões; detecção de segurança por vídeo. |

#### Ficha 2 — INFORM GroundStar

| Campo | Registro |
|---|---|
| Produto e fornecedor | GroundStar (módulos citados: Planning/RealTime Staff & Equipment, Planning/RealTime Stands & Terminals, WorkforcePlus, TurnManager, TeamWork, myStaff, entre outros). INFORM GmbH, **Alemanha**. https://www.inform-software.com/en/software/groundstar [Fato][43][45][47] |
| Público-alvo | "airports, airlines, and ground handlers" [Fato][43]; para turnaround: "Airline turnaround managers", empresas de *ground handling* e gestores de linha de frente [Fato][44]. |
| Problema que resolve | Controle de pessoal, equipamentos, posições e terminais com "Digital Decision Making based on Artificial Intelligence and Operations Research" [Fato][43]. |
| Funcionalidades | Planejamento e despacho em tempo real de pessoal e equipamentos, com "Management by Exception" e integração móvel [Fato][45]; TurnManager — "Process Irregularities at a Glance" — detecta irregularidades do *handling* e calcula automaticamente o impacto "on dependent processes and flight delays" [Fato][45]; "Reliable target off-block time calculation", previsão de efeito dominó e identificação de gargalos [Fato][44]; GS TeamWork: visão por tarefa de voos, alocação de pessoal e capacidade, em app web "mobile-first" para gestores de linha de frente [Fato][46]; cenários "what-if" [Fato][47]. |
| Como trata atrasos e exceções | TurnManager calcula o impacto nos processos dependentes [Fato][45]; TeamWork avisa os funcionários sobre "delays or changes that may affect them" e aponta "overlapping deployment times or agents who have not been informed"; o gestor ajusta manualmente ou aceita a recomendação do sistema [Fato][46]. |
| Fonte do dado operacional | Programação de voos e atividades operacionais [Fato][44] e apps móveis dos funcionários [Fato][43][46]. Integração com AODB/A-CDM: não informado. |
| Métricas divulgadas — [Fato] (declarado pelo fornecedor) | "more than 200 installations worldwide" desde os anos 1990 [47]; nenhum ganho numérico nas páginas lidas. |
| Relação com A-CDM | Calcula TOBT ("Reliable target off-block time calculation") [Fato][44]. Se envia o TOBT ao A-CDM do aeroporto: não informado. |
| O que vale incorporar [Inferência] | (1) Propagação automática do impacto de um atraso para as tarefas dependentes; (2) gestão por exceção; (3) app para quem executa e para o gestor de linha de frente; (4) redistribuição feita pelo gestor, com sugestão do sistema. |
| O que fica fora do nosso escopo [Inferência] | Escala e jornada de trabalho (WorkforcePlus), planejamento sazonal de posições e terminais e modelagem de custos: são escala/planejamento e financeiro, que o projeto excluiu. |

#### Ficha 3 — ADB SAFEGATE (Safedock + Apron Manager / Intelligent AiPRON)

| Campo | Registro |
|---|---|
| Produto e fornecedor | Safedock (A-VDGS, sistema avançado de guiagem visual de estacionamento), Apron Manager e a plataforma "Intelligent AiPRON". ADB SAFEGATE, sede em Machelen, **Bélgica** [Fato][61]. https://adbsafegate.com/what-we-do/apron/ [Fato][48][49][50] |
| Público-alvo | "airports, airlines, and ANSPs" (provedores de serviços de navegação aérea), em "over 3,000 airports in over 175 countries" [Fato][50]; no Apron Manager: centro de controle de operações do aeroporto (AOCC), controladores, pessoal de pátio, equipes de solo, tripulações e companhias [Fato][49]. |
| Problema que resolve | Gerir as atividades do pátio "from landing to takeoff" com automação e dados [Fato][50]. |
| Funcionalidades | Safedock guia a parada da aeronave [Fato][50]; recurso "Turn manager" que acompanha a atividade do turn e mede atrasos, prevê atrasos para atualizar o TOBT e fornece dados para marcos do CDM [Fato][48]; Apron Manager: alertas "before an aircraft arrives", monitoramento de equipamentos de solo e da posição, envio automático dos horários de block IN e OUT ao banco de voos, painel de KPIs por portão, suporte a A-CDM e acesso móvel [Fato][49]. *A página do Apron Manager traz no título extraído o nome "CORTEX Apron Manager".* |
| Como trata atrasos e exceções | Previsão de atraso → atualização do TOBT [Fato][48]; alertas antecipados [Fato][49]; análise de dados para "mitigate irregularities and create recommendations" [Fato][50]. |
| Fonte do dado operacional | Sensores do Safedock, câmeras, AODB e rastreamento de superfície (A-SMGCS e ADS-B, vigilância por transmissão automática de posição) [Fato][49]. |
| Métricas divulgadas — [Fato] (declarado pelo fornecedor) | previsão de "more than 8,000 Safedock systems" instalados até o fim de 2017 e "some 15 million aircraft dockings per year" [48]; turnarounds "faster, safer and more predictable" [49]. |
| Relação com A-CDM | Alimenta marcos do CDM e o TOBT; envia AIBT/AOBT automaticamente [Fato][48][49]. |
| O que vale incorporar [Inferência] | (1) Tratar o in-block e o off-block como **eventos** que disparam transições de estado (no MVP, registrados pelo operador ou simulados); (2) alerta **antes** da chegada quando o turnaround planejado não cabe (ligado à checagem EIBT + MTTT); (3) KPIs por posição. |
| O que fica fora do nosso escopo [Inferência] | Hardware de guiagem e sensores, A-SMGCS e integração física com o pátio. |

#### Ficha 4 — Veovo (A-CDM)

| Campo | Registro |
|---|---|
| Produto e fornecedor | A-CDM, dentro da linha "Outstanding Operations" (com AODB e gestão de recursos). Veovo, parte do grupo Gentrack, sede em Auckland, **Nova Zelândia**. https://veovo.com/platform/acdm [Fato][51][52] |
| Público-alvo | Operadores de aeroporto [Fato][51]; "over 110 airports globally" (perfil do fornecedor) [Fato][52]. |
| Problema que resolve | Coordenar a operação com dados em tempo real e previsões, melhorando turnaround, congestionamento e pontualidade [Fato][51]; o fornecedor critica a dependência de TOBT estimado manualmente por "busy airline or ground staff" [Fato][18]. |
| Funcionalidades | "360 view of milestones" com marcos pré-partida e atualizações em tempo real; ícones dinâmicos de status do turn; previsão de in-block e off-block com aprendizado de máquina; sequenciamento pré-partida; portal web com acesso, visões e alertas configuráveis por papel e gestão de exceções [Fato][51]. |
| Como trata atrasos e exceções | Previsão de off-block por ML, alertas por papel e gestão de exceções [Fato][51]. |
| Fonte do dado operacional | AODB e histórico do aeroporto mais dados em tempo real [Fato][51]. Câmeras/sensores: não informado. |
| Métricas divulgadas — [Fato] (declarado pelo fornecedor) | "20% improvement" em previsões [51]; prever horários de bloco "to within one minute" [52]; até "90% accuracy" com ML contra menos de 60% do TOBT manual [18]. |
| Relação com A-CDM | É um produto de A-CDM (marcos e sequenciamento pré-partida) [Fato][51]. |
| O que vale incorporar [Inferência] | (1) Linha do tempo de marcos por turnaround; (2) ícones de status; (3) alertas e visões configuráveis por papel (casa com os 4 atores). |
| O que fica fora do nosso escopo [Inferência] | Sequenciamento pré-partida e TSAT (função de ATC/aeroporto; integração com ATC excluída); ML preditivo (pode ser evolução futura, não MVP). |

#### Ficha 5 — SITA (Airport Management e Collaborative Decision Making)

| Campo | Registro |
|---|---|
| Produto e fornecedor | SITA Airport Management (Operations Manager, Fixed Resource Manager, Mobile Resource Manager) e SITA Collaborative Decision Making. SITA, Genebra, **Suíça**; empresa "100% owned by industry partners" (cerca de 400 membros). https://www.sita.aero/solutions/sita-at-airports/sita-operations-at-airports/sita-airport-management/ [Fato][53][54][56] |
| Público-alvo | Aeroportos e todos os parceiros do CDM; "Trusted by 190+ airports worldwide" [Fato][53][54]. |
| Problema que resolve | "a single source of data in real time across your operations" para gerir voos, recursos fixos e móveis e decisão colaborativa [Fato][54]. |
| Funcionalidades | Operations Manager com KPIs configuráveis e alertas; Mobile Resource Manager para recursos móveis do *ground handling*, com menção a "turnaround management"; sequenciamento pré-partida e Departure Manager no CDM [Fato][53][54]. |
| Como trata atrasos e exceções | "Act on alert capability", KPIs em tempo real, planejamento por cenários [Fato][54]; suporte a condições adversas e recuperação [Fato][53]. |
| Fonte do dado operacional | Não informado em detalhe; a página descreve "a single source of data in real time across your operations" [Fato][54]. |
| Métricas divulgadas — [Fato] (declarado pelo fornecedor) | Em El Dorado (Bogotá), primeiro A-CDM da América Latina (22/05/2025): diferença média entre partida planejada e real caiu "from 14 minutes to 5–7 minutes"; −2.000 min de atraso/ano; −26.300 min de táxi; 360.000 kg de combustível/ano; +3,5% de capacidade do ATC [55]. |
| Relação com A-CDM | Fornece o sistema A-CDM (sequenciador pré-partida, AMS — *Airport Management System* — e Operations Manager) [Fato][55]. |
| O que vale incorporar [Inferência] | (1) "Alerta → ação registrada" como fluxo explícito (casa com a métrica do objetivo 3); (2) KPIs configuráveis no painel; (3) caso latino-americano útil para o item 3. |
| O que fica fora do nosso escopo [Inferência] | Sequenciamento pré-partida e Departure Manager (ATC), gestão de recursos fixos (posições e portões) e cobrança. |

### 3.3 Matriz comparativa — produtos × núcleo do nosso produto

Legenda: ✔ = documentado na fonte · parcial = documentado em parte · ✘ = a fonte indica que não faz · n.i. = não informado nas fontes lidas. Todas as células são [Fato] no sentido de **declarações do fornecedor** na fonte indicada; a escolha entre ✔ e parcial é [Inferência].

| Capacidade do núcleo | Assaia | INFORM GroundStar | ADB SAFEGATE | Veovo | SITA |
|---|---|---|---|---|---|
| Orquestração do turnaround (plano de tarefas por turnaround, com responsável) | parcial — monitora, não atribui tarefas [40] | ✔ — alocação de tarefas e TurnManager [45][46] | parcial — acompanha a atividade do turn [48] | parcial — marcos do turn [51] | parcial — "turnaround management" no Mobile Resource Manager, sem detalhe [54] |
| Tarefas paralelas com dependências | parcial — regra "limpeza após desembarque" [42] | ✔ — impacto em "dependent processes" [45] | n.i. | n.i. | n.i. |
| Estados de tarefa / do turnaround | ✔ — status por atividade [40] | parcial — visão por tarefa [46] | parcial — block in/out e status do turn [49] | parcial — ícones de status [51] | n.i. |
| Cálculo de atraso / projeção de prontidão | ✔ — POBT e PRDT [40] | ✔ — TOBT e efeito dominó [44] | ✔ — prevê atraso e atualiza TOBT [48] | ✔ — previsão de off-block [51] | parcial — previsões de turnaround citadas em caso [55] |
| Caminho crítico explícito | n.i. | parcial — calcula impacto em dependentes, sem nomear caminho crítico [45] | n.i. | n.i. | n.i. |
| Painel em tempo real | ✔ [40] | ✔ [44] | ✔ [49] | ✔ [51] | ✔ [54] |
| Alertas | ✔ [40][42] | ✔ [46] | ✔ [49] | ✔ [51] | ✔ [54] |
| Redistribuição de recursos pelo supervisor | n.i. — há produto "ResourceManager", sem detalhe [39] | ✔ — despacho em tempo real e TeamWork [45][46] | n.i. | parcial — gestão de recursos na plataforma [52] | ✔ — Mobile Resource Manager [54] |
| Liberação com bloqueio por pendência | n.i. | n.i. | n.i. | n.i. | n.i. |
| Entrada de dados pelo operador (app/web) | n.i. — dados principais vêm de câmeras [41] | ✔ — apps móveis [43][46] | parcial — acesso móvel; dados principais vêm de sensores [49] | parcial — portal web por papel [51] | n.i. |
| Integração com A-CDM | ✔ [39] | parcial — calcula TOBT [44] | ✔ [48][49] | ✔ [51] | ✔ [55] |

### 3.4 Lacunas e diferencial possível

**Lacunas observadas [Inferência]** (com base na matriz 3.3):

1. Nenhuma das cinco fontes públicas documenta um **bloqueio formal da liberação** enquanto houver tarefa obrigatória pendente ou exceção aberta.
2. Só o INFORM documenta propagação para processos dependentes, e nenhum produto documenta **caminho crítico explícito** mostrado por turnaround.
3. Os produtos de visão computacional e sensores (Assaia, ADB SAFEGATE) exigem câmeras ou sensores instalados no pátio. Os de plataforma A-CDM (Veovo, SITA) focam no aeroporto e no sequenciamento de partidas, não em quem executa cada tarefa.
4. O mais próximo do nosso núcleo é o INFORM GroundStar (TurnManager + TeamWork), que vem junto com planejamento, escala e custos (fora do nosso escopo).

**Diferencial possível, em linguagem verificável (insumo para o critério C03.4) [Inferência]:**

- **DF1.** Cada turnaround é um grafo de tarefas com dependências e estados; a cada registro, o sistema recalcula o caminho crítico e a projeção de prontidão e os mostra no painel em até X segundos. *Verificável por teste de aceitação.*
- **DF2.** A transição para "Liberado" é bloqueada enquanto houver tarefa obrigatória pendente ou exceção aberta. *Verificável por teste e pela métrica "0 liberações com pendência".*
- **DF3.** Funciona apenas com registro do operador (web/app), sem câmeras, sensores ou integração com ATC. *Verificável pela lista de requisitos de implantação.*
- **DF4.** Mede a aderência com a mesma régua do setor: prontidão até TOBT + 5 min (T8, [2]). *Verificável pelo cálculo da métrica.*

Para a redação final, recomenda-se escrever "não documentado nas fontes públicas dos similares analisados", e não "único no mercado".

---

## 4. Frente 3 — Impacto na especificação

Recomendações apenas. Nenhum item da especificação foi alterado.

### 4.1 Métricas do item 1 — confirmação ou correção, uma a uma

| # | Métrica atual (seção 1.3 do briefing) | Veredito | Fonte e justificativa | Recomendação |
|---|---|---|---|---|
| M1 | Tolerância máxima de **5 min** para o turnaround ficar pronto até o horário planejado | **Confirmada, com ajuste de referência** | [Fato] O valor de 5 min em torno do TOBT aparece como janela de prontidão em [2] (alerta em TOBT + 5), [7] (± 5), [10] (± 5) e [8] (janela do piloto, seção 4.22.1), e como limiar de atualização em [8], [9], [11], [12]; a IATA deixa o valor como parâmetro local X [5]. [Inferência] No setor, o "horário planejado" é o **TOBT** (prontidão), não o SOBT (horário programado de saída). | Escrever "pronto para liberação até o TOBT planejado + 5 min". Manter **unilateral** (só o atraso conta), em linha com o alerta T8 da Especificação [2] e com o princípio 1.2. Ver D1. |
| M2 | **≥95%** dos turnarounds prontos para liberação até o horário planejado, com tolerância máxima de 5 min | **Não sustentada por fonte** (nem confirmada, nem refutada) | **Não confirmado:** não foi encontrada meta pública de % para precisão do TOBT. [Fato] Referências próximas: faixa verde de pontualidade em Heathrow ≥79% [7]; aderência ao slot ATFM (gerenciamento de fluxo de tráfego aéreo), com obrigação de reporte quando a não aderência chega a 20% [15] — [Inferência] equivale a ~80% de aderência, mas é outra métrica (slot CTOT na janela −5/+10 min) e um gatilho de reporte, não uma meta; pontualidade D15 (partida em até 15 min do horário) europeia de 67,9% em 2023 [16]; precisão do TOBT "less than 60%" em grandes aeroportos (declarado pelo fornecedor) [18]. | Manter 95% **apenas** se o texto disser que é meta interna do produto, mais exigente que as referências do setor; ou adotar 80% usando [15] só como analogia (é outra métrica). Ver D2. |
| M3 | **≥95%** das atividades iniciadas e concluídas dentro das janelas planejadas | **Não sustentada por fonte** | [Fato] O A-CDM mede marcos do turnaround (ACGT, ASBT, ARDT), não janelas por atividade [2]. A única regra por atividade encontrada é o alerta de embarque não iniciado até TOBT − X (variável local) [2]. | Manter como meta interna, mas definir no texto o que é "janela planejada" (início e fim previstos ± tolerância). Sugestão: usar a mesma tolerância de 5 min por coerência. |
| M4 | **100%** das tarefas com responsável antes do início | **Coerente com o setor; valor é regra de projeto** | [Fato] O A-CDM exige um responsável identificado pelo TOBT ("TOBT Responsible Person") [2]; Dublin exige "One party is responsible for the TOBT on operational day / shift" [8]. Não há norma para responsável por tarefa. | [Inferência] Como 100% é garantido por validação, funciona melhor como **regra de negócio/RF** (o sistema não deixa iniciar tarefa sem responsável). Pode continuar no objetivo, já que é verificável. |
| M5 | **Nenhuma** conclusão sem registro de início | **Não confirmado em fonte setorial; regra de projeto** | [Inferência] Decorre da máquina de estados da tarefa (Em execução → Concluída). Análogo no setor: a sequência de marcos ACGT → AEGT [Fato][4]. | Mesma observação de M4. |
| M6 | Mudança de estado visível no painel em até **5 s** | **Não sustentada por fonte setorial** | [Fato] As regras do A-CDM trabalham em minutos (ex.: "5:59 is acceptable while 6:00 is not" [3]); os fornecedores falam em "real time" sem número [40][51][54]. | Manter como meta de engenharia, mas escrever como RNF mensurável (ex.: "em até 5 s no percentil 95") e classificá-la na ISO/IEC 25010 (eficiência de desempenho). |
| M7 | Alerta em até **5 s** para 100% das atualizações com risco ao horário | **Prazo não sustentado; gatilhos sustentados** | [Fato] As condições de alerta do setor existem e podem definir o que é "risco": EIBT + MTTT além do TOBT (CDM07) [3][7]; embarque não iniciado até TOBT − X [2]; prontidão não registrada em TOBT + 5 [2]. O prazo de 5 s não tem fonte. | Manter 5 s como meta interna e **listar os gatilhos** de risco a partir das regras T8, T11 e T12. |
| M8 | **≥90%** dos alertas críticos com ação registrada em até **2 min** | **Não sustentada por fonte** | [Fato] Há o fluxo "alerta → ação" no setor (operador do AOC recebe o alerta e liga para o prestador [42]; "Act on alert capability" [54]), mas sem prazo publicado. | Manter como meta interna. [Inferência] 2 min é coerente porque deixa margem dentro da tolerância de 5 min do TOBT. |
| M9 | **0** liberações com tarefa obrigatória pendente ou exceção não resolvida | **Coerente; regra de projeto ancorada na definição de Aircraft Ready** | [Fato] A definição do marco "Aircraft Ready" exige "ground handling is completed, all aircraft doors are closed and passenger bridges/gangways are removed, pushback truck available if required" [2]. [Inferência] A meta zero e a parte "exceção não resolvida" são do projeto. | Manter. Usar essa definição como regra de transição para "Pronto para liberação". |

**Princípio 1.2 [Inferência]:** sustentado pelas fontes (seção 2.4). A evidência contrária (encurtar o turnaround) se refere ao turnaround **programado**, que é decisão de malha e fica fora do sistema.

### 4.2 Tabela de impacto por item do template

Nesta tabela, [n] indica a base de cada trecho. O texto é [Inferência] (candidatos e recomendações), exceto números e citações, que são [Fato] da fonte indicada.

| Item do template | O que a pesquisa entrega (recomendações) | Fontes |
|---|---|---|
| **1 — 3 Objetivos** | (a) Trocar "horário planejado" por "TOBT planejado" e explicitar tolerância **+5 min** (M1). (b) Declarar 95% e 2 min como metas internas ou rebaixar para 80% usando [15] só como analogia, pois é outra métrica (M2, M3, M8). (c) Definir "risco ao horário" pelos gatilhos do A-CDM: EIBT + MTTT > TOBT; embarque não iniciado até TOBT − X; prontidão não registrada em TOBT + 5 (M7). (d) Objetivo 2: M4 e M5 podem ficar, mas são regras de negócio; considerar trocar uma delas por uma métrica de resultado. (e) Princípio 1.2 sustentado; escrever "não é meta encurtar o turnaround programado". | [2][3][5][7][8][10][15][16][18] |
| **2 — É / Não é / Faz / Não faz** | **Candidatos — É:** coordenador do turnaround orientado a marcos e tarefas; fonte única de status compartilhada pelos atores [1]; orientado a exceção [40][45]; auditável (todo registro com autor e horário). **Não é:** sistema A-CDM completo nem sequenciador de partidas (TSAT) [2]; AODB; sistema de escala de pessoal [45]; sistema de visão computacional ou sensores [41][49]; ferramenta para encurtar o turnaround programado (seção 2.4). **Faz:** registra marcos do turnaround (in-block, início do atendimento, início do embarque, fim do atendimento, pronto, off-block) [2]; calcula projeção de prontidão e caminho crítico; alerta pelos gatilhos T8, T11 e T12; registra causa de atraso com código IATA [16]; permite redistribuição de equipe pelo coordenador; impede liberação com pendência [2]. **Não faz:** emitir TSAT ou autorização de acionamento/push-back (ATC); alterar plano de voo ou enviar DLA [7][8]; programar voos nem definir MTTT/turnaround programado; escala de tripulação; faturamento, SLA financeiro ou cobrança [54][60]; detecção automática por câmeras/sensores no MVP. | [1][2][7][8][16][40][41][45][49][54][60] |
| **3 — Visão do Produto** | **Candidatos — Problemas (com fonte):** atraso reacionário = 46% dos minutos de atraso na Europa em 2023 [16]; só 67,9% das partidas europeias dentro de 15 min [16]; em aeroportos CDM, o desvio-padrão da precisão da decolagem cai de ~14 min para ~7 e ~5 min nos marcos de sequenciamento e off-block, ou seja, a imprecisão residual continua relevante [14]; embarque estocástico no caminho crítico dificulta prever o turnaround [20]. Como ilustração (declarado pelo fornecedor): TOBT com menos de 60% de acerto dentro de 5 min em grandes aeroportos e estimado manualmente por equipe ocupada [18]; imprecisão média do TOBT de 4–5 min [19]. **Cliente-alvo:** *ground handler* e companhia aérea, que são os responsáveis pelo TOBT [2][5]; secundário: centro de operações do aeroporto [2]. **Categoria-segmento:** software de gestão de operações de solo / turnaround management (mesma categoria de INFORM, Assaia, ADB SAFEGATE) [39][44][49]. **Benefício-chave:** aeronave pronta no TOBT, com desvio detectado cedo. **Diferencial-chave:** DF1 a DF4 (seção 3.4). **Meta-valor:** derivar das métricas M1, M2 e M9. Contexto Brasil: GRU é o primeiro aeroporto A-CDM do país (2020) [57]. | [2][5][16][18][19][20][39][44][49][57] |
| **4 — BPMN TO BE** | **Início:** evento de mensagem "aeronave em posição" (AIBT) [2]. **Sequência:** início do atendimento (ACGT) → gateway paralelo com desembarque ∥ descarregamento ∥ água/lavatório ∥ abastecimento (condicional) ∥ inspeção → limpeza ∥ catering (após desembarque) → embarque ∥ carregamento → loadsheet → portas fechadas/ponte retirada → "Pronto para liberação" → liberação → off-block (AOBT) [2][20][22][29]. **Gateways com condição:** "tarefa aplicável?" (Não aplicável); "operador permite abastecer com passageiros?" [26][27]; "projeção > TOBT + 5?"; "há pendência obrigatória ou exceção aberta?". **Eventos:** temporizador TOBT − 15 (checagem com todas as equipes) e TOBT − 3 (portas e ponte) [13]; temporizador "embarque não iniciado até TOBT − X" [2]; temporizador TOBT + 5 sem prontidão [2]; evento de borda "atraso registrado" → subprocesso de exceção com código de atraso [16]; evento "atualizar TOBT" quando o desvio chega a 5 min [9][10]. **Lanes:** Operador de Solo/Rampa, Coordenador de Turnaround, Autoridade de Liberação e Motor de Eventos. ATC, se aparecer, como pool externo (caixa-preta) só para indicar a fronteira. | [2][9][10][13][16][20][22][26][27][29] |
| **5 — Atores** | Os 4 atores correspondem a papéis reais (seção 2.7.2). Ajustes: usar um nome único para o coordenador ("Coordenador de Turnaround") [30]; descrever o Operador como executante da própria empresa ou de prestador [16]; redescrever a Autoridade de Liberação como quem confirma a prontidão em nome da companhia, deixando claro que não é o ATC [2]; descrever o Motor de Eventos por analogia com o A-CDM System [2][3]. | [2][3][16][30] |
| **6 — RFs (insumo)** | Ver 4.3, agrupado pelas áreas A a D. | — |
| **8 — RNFs (insumo)** | Ver 4.4. | — |

### 4.3 Insumo para RFs (item 6), por área do plano

Capacidades observadas no setor e nos similares. **Não** são RFs redigidos. Na coluna Fonte, **[Fato]** = a capacidade aparece descrita na fonte (declarado pelo fornecedor, quando a fonte é de empresa); **[Inferência] (base: [n])** = proposta deste relatório apoiada na fonte; **[Inferência]** sozinho = sem fonte direta.

| Área | Capacidade observada | Fonte |
|---|---|---|
| **A** — Acesso e planejamento | Perfis de acesso e visões configuráveis por papel | [Fato][51] |
| A | Abrir o turnaround a partir do par chegada/partida, com horários de referência (SIBT/SOBT, EIBT, TOBT) | [Inferência] (base: [2][4]) |
| A | Calcular o TOBT inicial como o mais tarde entre EIBT + MTTT e EOBT | [Fato][3] |
| A | Modelo (template) de tarefas por tipo de aeronave/serviço, com dependências e marcação de "Não aplicável" | [Inferência] (base: [22][45]) |
| A | Regra configurável "abastecimento com passageiros a bordo permitido?" | [Inferência] (base: [26][27]) |
| A | Checagem de viabilidade na abertura: EIBT + MTTT > TOBT → turnaround "sob estresse" | [Fato][3][7] |
| **B** — Execução em solo | Operador consulta as próprias tarefas em app/web | [Fato][43][46] |
| B | Iniciar, pausar e concluir tarefa com horário registrado | [Inferência] (base: registro de horários dos marcos [2] e status por atividade [40]; pausa não descrita nas fontes) |
| B | Registrar marcos: início do atendimento (ACGT), início do embarque (ASBT), fim do atendimento (AEGT) | [Fato][2][4] |
| B | Marcar tarefa "Não aplicável" com justificativa | [Inferência] |
| B | Registrar impedimento com código de atraso IATA (grupo 31–39) | [Inferência] (base: [16]) |
| **C** — Monitoramento | Painel multi-turnaround com status por cor e *watchlist* | [Fato][40][51] |
| C | Linha do tempo de marcos por turnaround | [Fato][51] |
| C | Projeção de prontidão recalculada a cada evento e comparada ao TOBT | [Fato][40][44][48] |
| C | Cálculo do impacto de um atraso nos processos dependentes | [Fato][45] |
| C | Caminho crítico destacado por turnaround — conceito da literatura [20][24]; **não** documentado nos similares (seção 3.4) | [Inferência] |
| C | Alerta: sucessora não iniciada X min após o fim da predecessora | [Fato][42] (regra observada: limpeza não iniciada 3 min após o desembarque) |
| C | Alerta: embarque não iniciado até TOBT − X | [Fato][2] |
| C | Alerta: prontidão não registrada em TOBT + 5 | [Fato][2] |
| C | Indicadores no estilo "TOBT Quality": antecedência das atualizações, atualizações tardias | [Fato][7] |
| **D** — Exceções e liberação | Abrir exceção com código de atraso | [Inferência] (base: [16][38]) |
| D | Redistribuir equipe/recurso entre tarefas e turnarounds, com sugestão do sistema | [Fato][45][46][54] |
| D | Exigir atualização do TOBT quando a projeção se afasta 5 min ou mais (para mais **ou** para menos) | [Fato][8][9][10][13] |
| D | Registrar a ação tomada para cada alerta crítico ("alerta → ação") | [Inferência] (base: [42][54]) |
| D | Liberação só com as condições do marco "Aircraft Ready" atendidas e sem exceção aberta | [Inferência] (base: definição de Aircraft Ready [2]; "sem exceção aberta" é regra do projeto) |
| D | Registrar off-block (AOBT) e encerrar o turnaround | [Fato][2] |

### 4.4 Insumo para RNFs (item 8)

| Exigência | Origem | Característica ISO/IEC 25010 sugerida [Inferência] |
|---|---|---|
| Atualização "em tempo real" do painel e dos alertas; meta numérica a definir (ex.: ≤5 s p95) | [Fato] fornecedores falam em "real time" [40][51][54]; número = meta interna | Eficiência de desempenho (comportamento no tempo) |
| Horários registrados com precisão de minuto, no mínimo, e regra de arredondamento explícita | [Fato] "5:59 is acceptable while 6:00 is not" [3] | Adequação funcional (correção) |
| Trilha de auditoria de toda mudança de estado (quem, quando, o quê) | [Fato] marcos registrados com responsável [2]; auditorias ISAGO [36] | Segurança (responsabilização / não repúdio) |
| Acesso por papel; proteção de dados pessoais de funcionários (LGPD — Lei Geral de Proteção de Dados Pessoais) | [Fato] visões e acessos por papel [51]; LGPD = exigência legal brasileira [Inferência] | Segurança (confidencialidade) |
| Uso em dispositivo móvel no pátio | [Fato] apps móveis para quem executa [43][46]; checagens no pátio em TOBT − 15 e TOBT − 3 [13] | Usabilidade / Portabilidade |
| Disponibilidade durante toda a janela de operação do aeroporto | [Fato] suporte 24/7 citado pela SITA [53]; valor a definir | Confiabilidade (disponibilidade) |
| Interface de dados padronizada para troca com terceiros | [Fato] a IATA recomenda "a common API" para acesso a dados de A-CDM [5] | Compatibilidade (interoperabilidade) |
| Continuar registrando com conexão instável no pátio | [Inferência] sem fonte; risco típico de uso móvel em área aberta | Confiabilidade (tolerância a falhas) |
| Regras de tolerância e gatilhos de alerta parametrizáveis (variáveis locais) | [Fato] vários valores são "local variable" no A-CDM [2] | Manutenibilidade (modificabilidade) |

---

## 5. Decisões recomendadas

Nenhuma decisão abaixo bloqueia a entrega deste relatório. Cada uma traz a minha recomendação e, na última coluna, a decisão do Rodrigo (01/10/2026).

**A coluna "Decisão" prevalece sobre as recomendações das seções 1 a 4 quando houver diferença.** Em especial:

- **D2** troca a meta de 95% por **80%** em M2 e M3 (seção 4.1).
- **D6** troca o subconjunto de códigos 31–39 (seções 2.8 e 4.3) pela **tabela completa da ANAC, com 72 códigos**.
- **D7** inclui a leitura de QR Code pela câmera do celular no "Faz" e restringe o "Não faz" a sensores da aeronave e câmeras fixas no pátio (seções 3.4 e 4.2).

| # | Decisão para o Rodrigo | Opções | Recomendação [Inferência] | Decisão (01/10/2026) |
|---|---|---|---|---|
| D1 | Qual é o "horário planejado" das métricas do objetivo 1? | (a) TOBT planejado; (b) SOBT (horário programado de saída) | **(a) TOBT + 5 min, unilateral.** É a régua do setor para prontidão (T1–T9) e o alerta da Especificação EUROCONTROL é em TOBT + 5 [2]. O SOBT mistura o turnaround com atrasos de chegada e de ATC. | **Aprovada:** TOBT planejado + 5 min, unilateral. |
| D2 | O que fazer com os 95% (M2 e M3)? | (a) Manter, declarando que é meta interna mais exigente que o setor; (b) baixar para 80%, usando a regra de aderência ao slot ATFM [15] só como analogia (é outra métrica) | **(a)**, com uma frase de justificativa citando as referências de M2. Num ambiente controlado de TCC, 95% é atingível; o importante é não apresentar 95% como padrão do setor. | **80%** para os turnarounds prontos para liberação (M2) e para as atividades dentro das janelas planejadas (M3), seguindo as referências de mercado [7][15]. |
| D3 | Terminar antes do previsto deve gerar algum evento? | (a) Não; (b) sim, pedir atualização da previsão quando a antecipação chegar a 5 min | **(b).** Não é meta (princípio 1.2), mas as regras do TOBT pedem atualização nos dois sentidos [8][9][10] e o cartão de rampa alemão manda avisar "regardless of whether the ground handling will end early or late" [13]. | **(b)**, seguindo o padrão de mercado: pedir atualização da previsão quando a antecipação chegar a 5 min [8][9][10][13]. |
| D4 | O que significa o estado "Liberado" e quem é a Autoridade de Liberação? | (a) Liberação interna pela companhia (sem ATC); (b) fundir com o Coordenador | **(a).** Manter 4 atores, redescrever a Autoridade de Liberação como representante da companhia aérea que confirma a prontidão e escrever no "Não faz" que o sistema não emite autorização de acionamento/push-back (ATC). | **(a)**: 4 atores; a Autoridade de Liberação é o representante da companhia aérea que confirma a prontidão; não é a autorização do ATC. |
| D5 | Abastecimento com passageiros a bordo | (a) Dependência fixa (sempre sequencial); (b) regra configurável por operador | **(b).** É permitido sob condições pela EASA [26] e pela ANAC (RBAC 91.102(g)) [27]; o padrão pode ser "não permitido", que é o caso mais conservador [24]. | **(b)**: regra configurável por operador; abastecer com passageiros a bordo é permitido sob condições [26][27]. |
| D6 | Qual tabela de códigos de atraso usar? | (a) Dois dígitos AHM 730 (31–39 e alguns outros); (b) AHM 732 (três letras) | **(a) no MVP**, porque o texto é público e verificável [16]; citar o AHM 732 como evolução [37]. | **Tabela da ANAC** (Portaria nº 791/SSO/2012, alterada pela Portaria nº 55/2026): siglas de duas letras, as mesmas da IATA AHM 730, com os **72 códigos completos**, sem recorte, e descrições em português [62]. O AHM 732 não foi adotado pela ANAC. |
| D7 | Fonte do dado no MVP | (a) Só registro manual do operador; (b) prever integração com sensores | **(a)**, e escrever no "Não faz" que o MVP não captura eventos por câmera ou sensor. É também parte do diferencial DF3. | **(a) ampliada:** dados registrados pelo operador, **inclusive leitura de QR Code pela câmera do celular** (ex.: confirmação da limpeza por assento, fileira ou zona, a ser simulada na apresentação do TCC). Ficam fora: sensores da própria aeronave e câmeras fixas no pátio. Leitura de QR Code por assento ligada ao andamento do turnaround não foi encontrada nas fontes consultadas [42][63][64] → possível diferencial **DF5**. |
| D8 | Usar as siglas do A-CDM na especificação? | (a) Sim, com nome em português; (b) só nomes em português | **(a).** Um glossário curto (AIBT, ACGT, TOBT, ARDT, AOBT, MTTT) dá vocabulário comum aos RFs das quatro áreas e mostra embasamento no setor. | **(a)**: aprovada. |
| D9 | Nome do coordenador | "Coordenador/Supervisor de Turnaround" ou um nome só | **"Coordenador de Turnaround"** em todos os itens, por causa do critério K.1 (nomes idênticos). | **Aprovada:** "Coordenador de Turnaround" em todos os itens. |

---

## 6. Fontes

Fontes 1 a 61 acessadas em 30/09/2026; fontes 62 a 64 acessadas em 01/10/2026.

1. EUROCONTROL. *Airport collaborative decision-making (A-CDM)* (página do conceito). https://www.eurocontrol.int/concept/airport-collaborative-decision-making
2. EUROCONTROL. *EUROCONTROL Specification for Airport Collaborative Decision Making (A-CDM)*, Edição 1.0, 30/01/2025. https://www.eurocontrol.int/sites/default/files/2025-01/eurocontrol-specification-for-acdm.pdf
3. EUROCONTROL. *EUROCONTROL Specification for A-CDM* — versão de rascunho da Edição 1.0 (arquivo de 07/2024). https://www.eurocontrol.int/sites/default/files/2024-07/eurocontrol-draft-specification-acdm-ed1-0.pdf
4. ACI, EUROCONTROL e IATA. *Airport CDM Implementation Manual*, versão 5.0, 31/03/2017 — anexo "Acronyms and Definitions" (cópia hospedada por PASSUR). https://pitm.passur.com/help_files/airport-cdm-manual-2017%2010.15.19.pdf — página oficial do manual: https://www.eurocontrol.int/publication/airport-collaborative-decision-making-cdm-implementation-manual
5. IATA. *Airport – Collaborative Decision Making (A-CDM): IATA Recommendations*, 2018. https://www.iata.org/contentassets/5c1a116a6120415f87f3dadfa38859d2/iata-acdm-recommendations-v1.pdf
6. ICAO (Escritório Ásia-Pacífico). *A-CDM Frequently Asked Questions*, 1ª ed., 02/07/2021. https://www.icao.int/sites/default/files/APAC/Documents/FAQ-A-CDM.pdf
7. Heathrow Airport. *AOP2 user manual — Day to day operations*, versão 1.2, out/2018. https://www.heathrow.com/content/dam/heathrow/web/common/documents/company/team-heathrow/airside/aop/AOP2-daily-activities.pdf
8. Dublin Airport. *Airport Collaborative Decision Making — Operational Procedures*. https://www.dublinairport.com/docs/default-source/about-a-cdm/acdm-dub-operational-procedures.pdf?sfvrsn=a6f8c98e_2
9. Toronto Pearson. *A-CDM — Key Concepts*. https://www.torontopearson.com/en/operators-at-pearson/getting-started/a-cdm/key-concepts
10. Flughafen Zürich. *A-CDM Info* (folheto; data AIRAC de implantação 25/04/2019). https://media.flughafen-zuerich.ch/-/jssmedia/airport/portal/dokumente/business/airlines-and-handling/flight-operations/a-cdm/a-cdm_info_flyer_en.pdf?vs=1&rev=a3560a74e2d24b7fbb52a71de850db65
11. CAAS (Autoridade de Aviação Civil de Singapura). *AIP Supplement 83/16* — A-CDM em Changi. https://www.caas.gov.sg/docs/default-source/pdf/aipsup83-16.pdf
12. KOCA (Coreia do Sul). *AIP Supplement KR-eSUP-2025-33* — A-CDM Fase 2 em Incheon. https://aim.koca.go.kr/eaipPub/Package/2022-06-30/html/eSUP/KR-eSUP-2025-33-en-GB.pdf
13. Aeroportos alemães (publicado pelo Aeroporto de Munique). *Airport CDM: Ramp Reference Card*, versão 3.1, dez/2023. https://www.munich-airport.com/_b/0000000000000021443546bb6579b19f/ramp-reference-card-acdm-ger-version-3_1-en.pdf
14. ATC Network. *A-CDM Impact Assessment report published – A-CDM family increases to 20* (notícia sobre relatório da EUROCONTROL), 2016. https://www.atc-network.com/atc-news/eurocontrol/a-cdm-impact-assessment-report-published-a-cdm-family-increases-to-20
15. SES Performance (EUROCONTROL/Comissão Europeia). *ATFM slot adherence — metadata*. https://www.sesperformance.eu/dataportal/metadata/atfm-slot-adherence/
16. EUROCONTROL. *All-Causes Delays to Air Transport in Europe — Annual 2023 (CODA Digest)*. https://www.eurocontrol.int/sites/default/files/2024-12/eurocontrol-coda-digest-annual-report-2023.pdf
17. Cirium. *On-Time Performance FAQ*. https://www.cirium.com/resources/on-time-performance/on-time-performance-faq/
18. Veovo. *The trouble with TOBT… and how machine learning can improve it*, 05/04/2022. https://veovo.com/insights/articles/tobt-and-machine-learning
19. Assaia. *The value of accurate off-block time predictions*. https://www.assaia.com/resources/the-value-of-accurate-off-block-time-predictions
20. SCHULTZ, M. Fast Aircraft Turnaround Enabled by Reliable Passenger Boarding. *Aerospace*, v. 5, n. 1, art. 8, 2018. https://www.mdpi.com/2226-4310/5/1/8/htm
21. PŁANDA, B.; SKORUPSKI, J. Model for Evaluation of Aircraft Boarding Under Disturbances. *Aerospace*, v. 12, n. 5, art. 403, 2025. https://www.mdpi.com/2226-4310/12/5/403/htm
22. KIERZKOWSKI, A. et al. Modelling the Sustainable Development of the Ground Handling Process Using the PERT-COST Method. *Sustainability*, v. 17, n. 24, art. 11278, 2025. https://www.mdpi.com/2071-1050/17/24/11278
23. RODRÍGUEZ-SANZ, Á.; HERRERA DE LA CRUZ, J. A Novel Approach for Turnaround Time Allocation Based on Reinforcement Learning. *ICAS 2020*. https://www.icas.org/icas_archive/ICAS2020/data/papers/ICAS2020_1015_paper.pdf
24. SANZ DE VICENTE, S. *Ground Handling Simulation with CAST*. Master Thesis, HAW Hamburg, 2010. https://www.fzt.haw-hamburg.de/pers/Scholz/arbeiten/TextSanz.pdf
25. TU Dresden. *BPM: Dynamische Prozessoptimierung… (ground handling management)* (página de projeto). https://tu-dresden.de/bu/verkehr/ila/ifl/forschung/airport-operations/abgeschlossen/dynamische-prozessoptimierung
26. EASA / União Europeia. *Annex IV — Commercial Air Transport Operations [Part-CAT]*, CAT.OP.MPA.195 (cópia na biblioteca SKYbrary). https://skybrary.aero/sites/default/files/bookshelf/2159.pdf
27. ANAC. *RBAC nº 91, Emenda nº 05* (01/04/2025), seção 91.102(g). https://pergamum.anac.gov.br/pergamum/vinculos/RBAC91EMD05_01_ABR_2025.pdf
28. Airbus Customer Services. *Flight Operations Briefing Notes — Ground Handling: Refueling with Passengers on Board*, ago/2007 (cópia SKYbrary). https://skybrary.aero/sites/default/files/bookshelf/170.pdf
29. WIGNALL, A. *How it works: the aircraft turnaround*. AeroTime, 27/11/2022. https://www.aerotime.aero/articles/32767-how-it-works-the-aircraft-turnaround
30. Menzies Aviation. *Turnaround Coordinator* (descrição de vaga). https://careers.jmenzies.com/aviation/talentpool/turnaround-coordinator/64/description/
31. SKYbrary. *Ground Handling*. https://skybrary.aero/articles/ground-handling
32. Simple Flying. *How Ryanair Manages Super Tight Turn Arounds* (data não informada). https://simpleflying.com/ryanair-25-minute-turnaround/
33. IATA. *Ground Operations Manuals*. https://www.iata.org/en/publications/manuals/ground-operations/
34. IATA. *IATA Ground Operations Manual (IGOM)*. https://www.iata.org/en/publications/manuals/iata-ground-operations-manual
35. IATA. *Airport Handling Manual (AHM)*. https://www.iata.org/en/publications/manuals/airport-handling-manual/
36. IATA. *IATA Safety Audit for Ground Operations (ISAGO)*. https://www.iata.org/en/programs/ops-infra/ground-operations/isago/
37. IATA. *On Demand Webinar: New IATA delay codes AHM 732: How to improve performance analysis*. https://www.iata.org/en/publications/newsletters/iata-knowledge-hub/on-demand-webinarnew-iata-delay-codes-ahm-732-how-to-improve-performance-analysis/
38. Cosmos. *Triple-A Delay Coding: What AHM 732 Means for You and Your Station*, 22/07/2025 (blog de fornecedor). https://usecosmos.com/blog/triple-a-delay-coding
39. Assaia. Página institucional. https://www.assaia.com
40. Assaia. *TurnaroundControl*. https://www.assaia.com/solutions/turnaroundcontrol
41. Assaia. *ApronAI*. https://www.assaia.com/solutions/apron-ai
42. Assaia. *Turnaround Time Reduction Through Real Time Alerts* (estudo de caso). https://www.assaia.com/resources/turnaround-time-reduction-through-real-time-alerts-case-study
43. INFORM. *GroundStar*. https://www.inform-software.com/en/software/groundstar
44. INFORM. *Aircraft Turnaround Management*. https://www.inform-software.com/en/solutions/aviation-ground-operations/aircraft-turnaround-management
45. INFORM. *Dive into the functional capabilities of GroundStar* (demo clips). https://www.inform-software.com/en/lp/groundstar-demo-clips
46. Airport Improvement. *INFORM's GroundStar (GS) TeamWork: More Efficiency with Decentralized Task Allocation*, 19/06/2025. https://airportimprovement.com/article/informs-groundstar-gs-teamwork-more-efficiency-with-decentralized-task-allocation/
47. Ground Handling International. *GroundStar: Optimal solution for all – INFORM* (entrevista, data não informada). https://www.groundhandlinginternational.com/content/interviews/groundstar-optimal-solution-for-all-inform
48. ADB SAFEGATE. *ADB SAFEGATE enhances visual docking guidance system…* (comunicado), 09/10/2017. https://adbsafegate.com/news-events/press-releases/adb-safegate-enhances-visual-docking-guidance-system/
49. ADB SAFEGATE. *Apron Manager* (página de produto). https://adbsafegate.com/products/apron/apron-management-system/aipron-manager/
50. ADB SAFEGATE. *Intelligent apron management for safer, faster aircraft turns*. https://adbsafegate.com/what-we-do/apron/
51. Veovo. *A-CDM*. https://veovo.com/platform/acdm
52. Airport Suppliers. *Veovo* (perfil do fornecedor). https://www.airport-suppliers.com/supplier/veovo/
53. SITA. *Collaborative Decision Making*. https://www.sita.aero/solutions/sita-at-airports/sita-operations-at-airports/sita-airport-management/sita-collaborative-decision-making/
54. SITA. *SITA Airport Management*. https://www.sita.aero/solutions/sita-at-airports/sita-operations-at-airports/sita-airport-management/
55. SITA. *El Dorado becomes first airport in Latin America to implement A-CDM system*, 22/05/2025. https://www.sita.aero/pressroom/news-releases/el-dorado-becomes-first-airport-in-latin-america-to-implement-a-cdm-system/
56. Wikipedia. *SITA (business services company)*. https://en.wikipedia.org/wiki/SITA_(business_services_company)
57. Força Aérea (revista). *GRU é o primeiro aeroporto A-CDM do Brasil*, 05/11/2020. https://forcaaerea.com.br/gru-e-o-primeiro-aeroporto-a-cdm-do-brasil/
58. AEROIN. *DECEA destaca avanços operacionais no Aeroporto de Guarulhos (SP) com a tecnologia A-CDM*, 09/09/2023. https://aeroin.net/decea-destaca-avancos-operacionais-no-aeroporto-de-guarulhos-sp-com-a-tecnologia-a-cdm/
59. Amadeus. *Amadeus AODB* (folha de vendas), 2014. https://amadeus.com/documents/en/ground-handlers/sales-sheet/amadeus-aodb.pdf
60. Cosmos Solutions GmbH. Página institucional. https://usecosmos.com
61. Wikipedia. *ADB Safegate*. https://en.wikipedia.org/wiki/ADB_Safegate
62. ANAC. *Portaria Regulatória nº 55/SPO/SSA*, de 06/08/2026 (DOU 11/08/2026), que altera a Portaria nº 791/SSO/2012 e institui a nova tabela de códigos de motivos de atraso e cancelamento (72 códigos, 12 categorias). https://www.anac.gov.br/assuntos/legislacao/legislacao-1/portaria-regulatoria/2026/portaria-regulatoria-55
63. GE Aerospace. *Airport Cleanliness: There's An App For That*, nov/2020. https://www.geaerospace.com/news/articles/technology/airport-cleanliness-theres-app
64. Miratag. *Aircraft Cabin Cleaning Checklist* (modelo de checklist digital). https://miratag.com/en/checklist-templates/aviation-cabin-cleaning-checklist

### 6.1 Fontes procuradas e não lidas (respeitando bloqueios)

| Fonte | Motivo | Alternativa usada |
|---|---|---|
| ICAO WACAF — *TOBT and TSAT Performance Measurement Template* e *A-CDM Performance Metrics Template* (2025) | Erro 403 | Indicadores de Heathrow [7] e SES [15] |
| ResearchGate — Fricke e Schultz, *Delay Impacts onto Turnaround Performance* | Erro 429 | Schultz [20], Rodríguez-Sanz [23], TU Dresden [25] |
| Airbus e Boeing — gráficos de turnaround dos manuais de planejamento aeroportuário (A320 AC, 737 MAX ACAPS) | Leitura truncada; seção do gráfico não veio | Literatura acadêmica [20][22][24] |
| UK CAA — AMC1 CAT.OP.MPA.195 | Página exige JavaScript | Texto da regra via SKYbrary [26] |
| DECEA — notícias sobre A-CDM em GRU | Página dinâmica sem o texto da notícia | [57][58] |
| Airservices Australia — FAQ de A-CDM | Erro 500 | Outros procedimentos de aeroportos [7]–[12] |
| Blog da ADB SAFEGATE (AiPRON 360) | Subdomínio desativado | Páginas de produto [49][50] |

