---
id: tolerancias-e-indicadores
titulo: "Tolerâncias e indicadores de aderência (P1.3)"
tipo: pesquisa-topico
secao_original: "2.3"
itens_template: [1, 7, 8]
areas: [C, D]
decisoes: [D1, D2, D3]
fontes: [2, 3, 5, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19]
relacionados: [marcos-e-horarios, previsibilidade-vs-velocidade, metricas-item-1]
status: vigente
atualizado: 2026-10-01
---
# Tolerâncias e indicadores de aderência (P1.3)

> Base de conhecimento do projeto · origem: seção 2.3 do [relatório consolidado](../01-referencias-setor-e-similares.md) (congelado em 01/10/2026) · fontes numeradas em [fontes.md](../fontes.md) · convenções [Fato]/[Inferência] e índices no [mapa da pesquisa](../README.md).

> **Decisões vigentes (prevalecem sobre o texto abaixo):** [D1 — Referência de horário: TOBT planejado + 5 min, unilateral](../../docs/adr/0001-referencia-horario-tobt-mais-5-min.md); [D2 — Metas percentuais do item 1: 80%](../../docs/adr/0002-metas-percentuais-80.md); [D3 — Antecipação de 5 min ou mais exige atualizar a previsão](../../docs/adr/0003-atualizar-previsao-na-antecipacao.md).
>
> Régua do projeto: pronto até o TOBT planejado + 5 min, unilateral (D1). Metas percentuais do item 1: 80% (D2). Antecipação de 5 min ou mais gera pedido de atualização da previsão (D3). As regras T8, T11 e T12 definem os gatilhos de "risco ao horário".


## 2.3.1 Regras e tolerâncias do TOBT, do TSAT e da prontidão

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

## 2.3.2 Indicadores (KPIs) de aderência e pontualidade

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

## 2.3.3 Linha de base: quão preciso o TOBT costuma ser

- **[Fato][14]** Avaliação de impacto do A-CDM feita pela EUROCONTROL (publicada em 2016, quando 20 aeroportos tinham A-CDM completo): o desvio-padrão da precisão da decolagem caiu "from an average of 14 minutes to around 7 and 5 minutes at the sequencing and off-block milestones respectively"; ganho médio de aderência ao horário entre 0,5 e 2 min por voo.
- **[Fato][18]** (declarado pelo fornecedor Veovo, 2022) O TOBT de muitos grandes aeroportos é "less than 60% accurate to within 5 minutes".
- **[Fato][19]** (declarado pelo fornecedor Assaia) A imprecisão média do TOBT é "rather consistent at four to five minutes", e 68% dos voos têm imprecisão de ±11 min ou mais; em um aeroporto, 40% dos voos perderam a janela do TSAT.
- **Não confirmado:** meta percentual pública e oficial para precisão do TOBT (ex.: "X% dos voos dentro de ±5 min"). Os modelos de medição de TOBT/TSAT publicados pela ICAO (escritório WACAF, 2025) retornaram erro 403 e não foram lidos.

---

## Ligações

- **Decisões:** [D1](../../docs/adr/0001-referencia-horario-tobt-mais-5-min.md), [D2](../../docs/adr/0002-metas-percentuais-80.md), [D3](../../docs/adr/0003-atualizar-previsao-na-antecipacao.md)
- **Itens da especificação:** [Item 1 — 3 Objetivos](../../especificacao/01-3-objetivos.md), [Item 7 — Estórias de Usuário](../../especificacao/07-estorias-de-usuario/00-item.md), [Item 8 — Requisitos Não Funcionais](../../especificacao/08-requisitos-nao-funcionais/00-item.md)
- **Áreas do plano RA1:** [Área C — Monitoramento](../../especificacao/06-requisitos-funcionais/area-c.md), [Área D — Exceções e liberação](../../especificacao/06-requisitos-funcionais/area-d.md) (divisão em [entregas/ra1-tarefas.md](../../entregas/ra1-tarefas.md), tabela 1.2)
- **Relacionados:** [marcos-e-horarios](marcos-e-horarios.md), [previsibilidade-vs-velocidade](previsibilidade-vs-velocidade.md), [metricas-item-1](../impacto/metricas-item-1.md)
- **Fontes citadas:** 2, 3, 5, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19 (em [fontes.md](../fontes.md))
- **Contexto geral:** [CONTEXT.md](../../CONTEXT.md) · [mapa da pesquisa](../README.md)
