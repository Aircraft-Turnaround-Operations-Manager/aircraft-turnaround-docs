---
id: metricas-item-1
titulo: "Métricas do item 1 (seção 4.1)"
tipo: impacto
secao_original: "4.1"
itens_template: [1]
areas: []
decisoes: [D1, D2]
fontes: [2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 15, 16, 18, 40, 42, 51, 54]
relacionados: [tolerancias-e-indicadores, previsibilidade-vs-velocidade, impacto-por-item]
status: vigente
atualizado: 2026-10-01
---
# Métricas do item 1 (seção 4.1)

> Base de conhecimento do projeto · origem: seção 4.1 do [relatório consolidado](../01-referencias-setor-e-similares.md) (congelado em 01/10/2026) · fontes numeradas em [fontes.md](../fontes.md) · convenções [Fato]/[Inferência] e índices no [mapa da pesquisa](../README.md).

> **Decisões vigentes (prevalecem sobre o texto abaixo):** [D1 — Referência de horário: TOBT planejado + 5 min, unilateral](../../docs/adr/0001-referencia-horario-tobt-mais-5-min.md); [D2 — Metas percentuais do item 1: 80%](../../docs/adr/0002-metas-percentuais-80.md).
>
> M1: referência no TOBT planejado, unilateral (D1). M2 e M3: meta de 80% (D2). As demais metas (M4–M9) seguem como estão.


| # | Métrica atual (seção 1.3 do briefing) | Veredito | Fonte e justificativa | Recomendação |
|---|---|---|---|---|
| M1 | Tolerância máxima de **5 min** para o turnaround ficar pronto até o horário planejado | **Confirmada, com ajuste de referência** | [Fato] O valor de 5 min em torno do TOBT aparece como janela de prontidão em [2] (alerta em TOBT + 5), [7] (± 5), [10] (± 5) e [8] (janela do piloto, seção 4.22.1), e como limiar de atualização em [8], [9], [11], [12]; a IATA deixa o valor como parâmetro local X [5]. [Inferência] No setor, o "horário planejado" é o **TOBT** (prontidão), não o SOBT (horário programado de saída). | **Decidido (D1).** Escrever "pronto para liberação até o TOBT planejado + 5 min". Manter **unilateral** (só o atraso conta), em linha com o alerta T8 da Especificação [2] e com o princípio 1.2. Ver [D1](../../docs/adr/0001-referencia-horario-tobt-mais-5-min.md). |
| M2 | **≥95%** dos turnarounds prontos para liberação até o horário planejado, com tolerância máxima de 5 min | **Não sustentada por fonte** (nem confirmada, nem refutada) | **Não confirmado:** não foi encontrada meta pública de % para precisão do TOBT. [Fato] Referências próximas: faixa verde de pontualidade em Heathrow ≥79% [7]; aderência ao slot ATFM (gerenciamento de fluxo de tráfego aéreo), com obrigação de reporte quando a não aderência chega a 20% [15] — [Inferência] equivale a ~80% de aderência, mas é outra métrica (slot CTOT na janela −5/+10 min) e um gatilho de reporte, não uma meta; pontualidade D15 (partida em até 15 min do horário) europeia de 67,9% em 2023 [16]; precisão do TOBT "less than 60%" em grandes aeroportos (declarado pelo fornecedor) [18]. | **Decidido (D2): 80%**, seguindo as referências de mercado mais próximas ([7]; [15] só como analogia). Ver [D2](../../docs/adr/0002-metas-percentuais-80.md). |
| M3 | **≥95%** das atividades iniciadas e concluídas dentro das janelas planejadas | **Não sustentada por fonte** | [Fato] O A-CDM mede marcos do turnaround (ACGT, ASBT, ARDT), não janelas por atividade [2]. A única regra por atividade encontrada é o alerta de embarque não iniciado até TOBT − X (variável local) [2]. | **Decidido (D2): 80%.** Definir no texto o que é "janela planejada" (início e fim previstos ± tolerância); sugestão: a mesma tolerância de 5 min. |
| M4 | **100%** das tarefas com responsável antes do início | **Coerente com o setor; valor é regra de projeto** | [Fato] O A-CDM exige um responsável identificado pelo TOBT ("TOBT Responsible Person") [2]; Dublin exige "One party is responsible for the TOBT on operational day / shift" [8]. Não há norma para responsável por tarefa. | [Inferência] Como 100% é garantido por validação, funciona melhor como **regra de negócio/RF** (o sistema não deixa iniciar tarefa sem responsável). Pode continuar no objetivo, já que é verificável. |
| M5 | **Nenhuma** conclusão sem registro de início | **Não confirmado em fonte setorial; regra de projeto** | [Inferência] Decorre da máquina de estados da tarefa (Em execução → Concluída). Análogo no setor: a sequência de marcos ACGT → AEGT [Fato][4]. | Mesma observação de M4. |
| M6 | Mudança de estado visível no painel em até **5 s** | **Não sustentada por fonte setorial** | [Fato] As regras do A-CDM trabalham em minutos (ex.: "5:59 is acceptable while 6:00 is not" [3]); os fornecedores falam em "real time" sem número [40][51][54]. | Manter como meta de engenharia, mas escrever como RNF mensurável (ex.: "em até 5 s no percentil 95") e classificá-la na ISO/IEC 25010 (eficiência de desempenho). |
| M7 | Alerta em até **5 s** para 100% das atualizações com risco ao horário | **Prazo não sustentado; gatilhos sustentados** | [Fato] As condições de alerta do setor existem e podem definir o que é "risco": EIBT + MTTT além do TOBT (CDM07) [3][7]; embarque não iniciado até TOBT − X [2]; prontidão não registrada em TOBT + 5 [2]. O prazo de 5 s não tem fonte. | Manter 5 s como meta interna e **listar os gatilhos** de risco a partir das regras T8, T11 e T12. |
| M8 | **≥90%** dos alertas críticos com ação registrada em até **2 min** | **Não sustentada por fonte** | [Fato] Há o fluxo "alerta → ação" no setor (operador do AOC recebe o alerta e liga para o prestador [42]; "Act on alert capability" [54]), mas sem prazo publicado. | Manter como meta interna. [Inferência] 2 min é coerente porque deixa margem dentro da tolerância de 5 min do TOBT. |
| M9 | **0** liberações com tarefa obrigatória pendente ou exceção não resolvida | **Coerente; regra de projeto ancorada na definição de Aircraft Ready** | [Fato] A definição do marco "Aircraft Ready" exige "ground handling is completed, all aircraft doors are closed and passenger bridges/gangways are removed, pushback truck available if required" [2]. [Inferência] A meta zero e a parte "exceção não resolvida" são do projeto. | Manter. Usar essa definição como regra de transição para "Pronto para liberação". |

**Princípio 1.2 [Inferência]:** sustentado pelas fontes ([Previsibilidade × velocidade](../topicos/previsibilidade-vs-velocidade.md)). A evidência contrária (encurtar o turnaround) se refere ao turnaround **programado**, que é decisão de malha e fica fora do sistema.

---

## Ligações

- **Decisões:** [D1](../../docs/adr/0001-referencia-horario-tobt-mais-5-min.md), [D2](../../docs/adr/0002-metas-percentuais-80.md)
- **Itens da especificação:** [Item 1 — 3 Objetivos](../../especificacao/01-3-objetivos.md)
- **Relacionados:** [tolerancias-e-indicadores](../topicos/tolerancias-e-indicadores.md), [previsibilidade-vs-velocidade](../topicos/previsibilidade-vs-velocidade.md), [impacto-por-item](impacto-por-item.md)
- **Fontes citadas:** 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 15, 16, 18, 40, 42, 51, 54 (em [fontes.md](../fontes.md))
- **Contexto geral:** [CONTEXT.md](../../CONTEXT.md) · [mapa da pesquisa](../README.md)
