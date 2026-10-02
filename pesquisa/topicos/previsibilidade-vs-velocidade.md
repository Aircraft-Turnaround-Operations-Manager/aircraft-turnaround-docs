---
id: previsibilidade-vs-velocidade
titulo: "Previsibilidade × velocidade (P1.4)"
tipo: pesquisa-topico
secao_original: "2.4"
itens_template: [1, 2, 3]
areas: []
decisoes: [D3]
fontes: [1, 2, 5, 7, 13, 16, 20, 21, 22, 23, 25, 32, 42]
relacionados: [tolerancias-e-indicadores, metricas-item-1, caminho-critico]
status: vigente
atualizado: 2026-10-01
---
# Previsibilidade × velocidade (P1.4)

> Base de conhecimento do projeto · origem: seção 2.4 do [relatório consolidado](../01-referencias-setor-e-similares.md) (congelado em 01/10/2026) · fontes numeradas em [fontes.md](../fontes.md) · convenções [Fato]/[Inferência] e índices no [mapa da pesquisa](../README.md).

> **Decisões vigentes (prevalecem sobre o texto abaixo):** [D3 — Antecipação de 5 min ou mais exige atualizar a previsão](../../docs/adr/0003-atualizar-previsao-na-antecipacao.md).
>
> A recomendação "a antecipação vira informação" foi adotada (D3).


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

---

## Ligações

- **Decisões:** [D3](../../docs/adr/0003-atualizar-previsao-na-antecipacao.md)
- **Itens da especificação:** [Item 1 — 3 Objetivos](../../especificacao/01-3-objetivos.md), [Item 2 — É / Não é / Faz / Não faz](../../especificacao/02-e-nao-e-faz-nao-faz.md), [Item 3 — Visão do Produto](../../especificacao/03-visao-do-produto.md)
- **Relacionados:** [tolerancias-e-indicadores](tolerancias-e-indicadores.md), [metricas-item-1](../impacto/metricas-item-1.md), [caminho-critico](caminho-critico.md)
- **Fontes citadas:** 1, 2, 5, 7, 13, 16, 20, 21, 22, 23, 25, 32, 42 (em [fontes.md](../fontes.md))
- **Contexto geral:** [CONTEXT.md](../../CONTEXT.md) · [mapa da pesquisa](../README.md)
