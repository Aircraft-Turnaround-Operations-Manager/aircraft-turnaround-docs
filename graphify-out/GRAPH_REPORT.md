# Graph Report - aircraft-turnaround-docs-kb  (2026-10-02)

## Corpus Check
- Corpus is ~33,754 words - fits in a single context window. You may not need a graph.

## Summary
- 246 nodes · 579 edges · 9 communities (8 shown, 1 thin omitted)
- Extraction: 81% EXTRACTED · 19% INFERRED · 0% AMBIGUOUS · INFERRED: 110 edges (avg confidence: 0.87)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Objetivos e escopo do produto
- Fontes e referências da pesquisa
- ADRs, similares e insumos
- Contexto: atores, estados e régua
- Regras para IAs e processo do RA1
- Metas, tolerâncias e aderência ao TOBT
- A-CDM: marcos e siglas
- Códigos de atraso (ANAC/IATA)
- Abastecimento com passageiros

## God Nodes (most connected - your core abstractions)
1. `CONTEXT.md — Contexto do projeto` - 37 edges
2. `Pesquisa - mapa da base de conhecimento` - 32 edges
3. `Fontes da pesquisa` - 31 edges
4. `Lacunas e diferencial possivel (3.4)` - 17 edges
5. `Tolerancias e indicadores de aderencia (P1.3)` - 17 edges
6. `Impacto por item do template (4.2)` - 15 edges
7. `Matriz comparativa (3.3)` - 15 edges
8. `ADR-0001 — TOBT planejado + 5 min` - 14 edges
9. `Aircraft Turnaround Orchestration System` - 14 edges
10. `Quadro E - Nao E - Faz - Nao Faz` - 14 edges

## Surprising Connections (you probably didn't know these)
- `Sinalizar conflitos com ADRs` --semantically_similar_to--> `Precedência: ADRs > pesquisa > rascunhos`  [INFERRED] [semantically similar]
  docs/agents/domain.md → CONTEXT.md
- `Rótulos ra1 / item-NN / area-x / por-integrante` --semantically_similar_to--> `Vocabulário de triage (needs-triage, needs-info, ready-for-agent, ready-for-human, wontfix)`  [INFERRED] [semantically similar]
  entregas/ra1-tarefas.md → docs/agents/triage-labels.md
- `Turnaround state machine mapped to A-CDM milestones` --rationale_for--> `ADR-0004 — Quatro atores e Autoridade de Liberação`  [INFERRED]
  pesquisa/topicos/marcos-e-horarios.md → docs/adr/0004-quatro-atores-e-autoridade-de-liberacao.md
- `Refuelling with passengers on board (configurable rule)` --rationale_for--> `ADR-0005 — Abastecimento com passageiros configurável`  [INFERRED]
  pesquisa/topicos/atividades-e-dependencias.md → docs/adr/0005-abastecimento-com-passageiros-configuravel.md
- `ANAC delay code table (72 codes, 12 categories)` --rationale_for--> `ADR-0006 — Códigos de atraso tabela ANAC`  [INFERRED]
  pesquisa/topicos/codigos-de-atraso.md → docs/adr/0006-codigos-de-atraso-tabela-anac.md

## Hyperedges (group relationships)
- **Quatro atores do Aircraft Turnaround Orchestration System** — context_operador_de_solo_rampa, context_coordenador_de_turnaround, context_autoridade_de_liberacao, context_motor_de_eventos [EXTRACTED 1.00]
- **Régua de horário e metas (TOBT + 5 min, 80%, antecipação)** — docs_adr_0001_referencia_horario_tobt_mais_5_min_d1_tobt_mais_5_min, docs_adr_0002_metas_percentuais_80_d2_metas_80, docs_adr_0003_atualizar_previsao_na_antecipacao_d3_atualizar_previsao_antecipacao, context_tobt, context_metas_do_item_1 [EXTRACTED 1.00]
- **Governança de consistência documental** — context_precedencia_adr_pesquisa, docs_agents_domain_flag_adr_conflicts, entregas_ra1_criterios_de_aceite_k11_consistencia_context_adr, entregas_ra1_criterios_de_aceite_protocolo_execucao_verificacao [INFERRED 0.85]
- **Tres objetivos do turnaround e suas metricas** — especificacao_01_3_objetivos_objetivo_1_precisao_temporal, especificacao_01_3_objetivos_objetivo_2_sincronizar_equipes, especificacao_01_3_objetivos_objetivo_3_desvios_e_liberacao_segura, especificacao_01_3_objetivos_metrica_95_atividades_na_janela, especificacao_01_3_objetivos_metrica_responsavel_e_painel_5s, especificacao_01_3_objetivos_metrica_alertas_e_zero_liberacoes_pendentes [EXTRACTED 1.00]
- **Areas A-D de entrega do produto** — especificacao_02_e_nao_e_faz_nao_faz_area_a, especificacao_02_e_nao_e_faz_nao_faz_area_b, especificacao_02_e_nao_e_faz_nao_faz_area_c, especificacao_02_e_nao_e_faz_nao_faz_area_d [EXTRACTED 1.00]
- **Cadeia de rastreabilidade RF, US, RNF, UC por area** — especificacao_06_requisitos_funcionais_00_item_item, especificacao_07_estorias_de_usuario_00_item_item, especificacao_08_requisitos_nao_funcionais_00_item_item, especificacao_09_diagrama_geral_de_casos_de_uso_item, especificacao_10_especificacoes_de_caso_de_uso_00_item_item [INFERRED 0.85]
- **'Risco ao horario' trigger set (T8, T11, T12)** — pesquisa_impacto_impacto_por_item_risco_ao_horario, pesquisa_topicos_tolerancias_e_indicadores_tobt_mais_5_min, pesquisa_topicos_tolerancias_e_indicadores_t11_viabilidade_eibt_mttt, pesquisa_topicos_tolerancias_e_indicadores_t12_embarque_nao_iniciado [EXTRACTED 1.00]
- **Five market similars compared in matrix 3.3** — pesquisa_similares_assaia_assaia_apronai_turnaroundcontrol, pesquisa_similares_inform_groundstar_inform_groundstar, pesquisa_similares_adb_safegate_adb_safegate_safedock_apron_manager, pesquisa_similares_veovo_veovo_acdm, pesquisa_similares_sita_sita_airport_management_cdm, pesquisa_similares_matriz_comparativa_capacidades_do_nucleo [EXTRACTED 1.00]
- **Project differentiators DF1-DF5** — pesquisa_similares_lacunas_e_diferencial_df1, pesquisa_similares_lacunas_e_diferencial_df2, pesquisa_similares_lacunas_e_diferencial_df3, pesquisa_similares_lacunas_e_diferencial_df4, pesquisa_similares_lacunas_e_diferencial_df5 [EXTRACTED 1.00]

## Communities (9 total, 1 thin omitted)

### Community 0 - "Objetivos e escopo do produto"
Cohesion: 0.07
Nodes (53): Aircraft Turnaround Orchestration System, Alerta de risco ao horario planejado, Caminho critico, Janela planejada, Liberacao da aeronave, Metrica: 95% das atividades na janela e 95% dos turnarounds prontos (tolerancia 5 min), Metrica: alertas em 5 s, 90% acoes em 2 min, 0 liberacoes com pendencia, Metrica: 100% tarefas com responsavel, painel atualizado em ate 5 s (+45 more)

### Community 1 - "Fontes e referências da pesquisa"
Cohesion: 0.08
Nodes (42): Fontes da pesquisa, EUROCONTROL A-CDM Impact Assessment (2016) [14], ANAC Portaria Regulatoria 55/SPO/SSA 2026 (72 delay codes) [62], ANAC RBAC 91 Emenda 05, 91.102(g) [27], Assaia case study - turnaround time reduction via alerts [42], Assaia - value of accurate off-block predictions [19], EUROCONTROL CODA Digest 2023 [16], EASA Part-CAT CAT.OP.MPA.195 [26] (+34 more)

### Community 2 - "ADRs, similares e insumos"
Cohesion: 0.15
Nodes (38): ADR-0004 — Quatro atores e Autoridade de Liberação, ADR-0005 — Abastecimento com passageiros configurável, ADR-0006 — Códigos de atraso tabela ANAC, ADR-0007 — Dados do operador e QR Code, ADR-0009 — Nome Coordenador de Turnaround, Índice de decisões (ADRs), Impacto por item do template (4.2), BPMN TO BE inputs (events, gateways, lanes) (+30 more)

### Community 3 - "Contexto: atores, estados e régua"
Cohesion: 0.13
Nodes (23): CONTEXT.md — Contexto do projeto, A-CDM (Airport Collaborative Decision Making), AEGT — Fim real do atendimento em solo, Aircraft Turnaround Orchestration System, ARDT — Horário real de prontidão (Aircraft Ready), Autoridade de Liberação, Coordenador de Turnaround, Estados da tarefa (+15 more)

### Community 4 - "Regras para IAs e processo do RA1"
Cohesion: 0.09
Nodes (21): Formato de arquivo de pesquisa (YAML + seção Ligações), Domain Docs, Usar o vocabulário do glossário do CONTEXT.md, Issue tracker: GitHub, GitHub Issues via gh CLI, Wayfinding (map issue + child tickets), Triage Labels, Vocabulário de triage (needs-triage, needs-info, ready-for-agent, ready-for-human, wontfix) (+13 more)

### Community 5 - "Metas, tolerâncias e aderência ao TOBT"
Cohesion: 0.15
Nodes (26): ADR-0001 — TOBT planejado + 5 min, ADR-0002 — Metas percentuais 80%, ADR-0003 — Atualizar previsão na antecipação, Dublin Airport A-CDM Operational Procedures [8], EUROCONTROL A-CDM Specification draft (2024) [3], Heathrow AOP2 user manual [7], German airports A-CDM Ramp Reference Card v3.1 [13], SES Performance ATFM slot adherence [15] (+18 more)

### Community 6 - "A-CDM: marcos e siglas"
Cohesion: 0.16
Nodes (17): ADR-0008 — Siglas A-CDM com nome em português, Airport CDM Implementation Manual v5.0 (ACI/EUROCONTROL/IATA) [4], EUROCONTROL A-CDM concept page [1], EUROCONTROL Specification for A-CDM Ed. 1.0 (2025) [2], IATA A-CDM Recommendations (2018) [5], M9: zero releases with pending task or open exception, DF2 release blocked with pending task or open exception, O que e o A-CDM (P1.1) (+9 more)

### Community 7 - "Códigos de atraso (ANAC/IATA)"
Cohesion: 0.67
Nodes (3): IATA AHM 730, IATA AHM 732, ANAC Portaria nº 55/2026

## Knowledge Gaps
- **22 isolated node(s):** `Estados da tarefa`, `Tabela "O que ler para cada item"`, `ANAC RBAC 91.102(g)`, `EASA CAT.OP.MPA.195`, `IATA AHM 732` (+17 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 24 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `CONTEXT.md — Contexto do projeto` connect `Contexto: atores, estados e régua` to `Fontes e referências da pesquisa`, `ADRs, similares e insumos`, `Regras para IAs e processo do RA1`, `Metas, tolerâncias e aderência ao TOBT`, `A-CDM: marcos e siglas`?**
  _High betweenness centrality (0.204) - this node is a cross-community bridge._
- **Why does `Pesquisa - mapa da base de conhecimento` connect `ADRs, similares e insumos` to `Fontes e referências da pesquisa`, `Contexto: atores, estados e régua`, `Metas, tolerâncias e aderência ao TOBT`, `A-CDM: marcos e siglas`?**
  _High betweenness centrality (0.156) - this node is a cross-community bridge._
- **Why does `Fontes da pesquisa` connect `Fontes e referências da pesquisa` to `ADRs, similares e insumos`, `Contexto: atores, estados e régua`, `Regras para IAs e processo do RA1`, `Metas, tolerâncias e aderência ao TOBT`, `A-CDM: marcos e siglas`?**
  _High betweenness centrality (0.155) - this node is a cross-community bridge._
- **What connects `Estados da tarefa`, `Tabela "O que ler para cada item"`, `ANAC RBAC 91.102(g)` to the rest of the system?**
  _22 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Objetivos e escopo do produto` be split into smaller, more focused modules?**
  _Cohesion score 0.07017543859649122 - nodes in this community are weakly interconnected._
- **Should `Fontes e referências da pesquisa` be split into smaller, more focused modules?**
  _Cohesion score 0.07665505226480836 - nodes in this community are weakly interconnected._
- **Should `ADRs, similares e insumos` be split into smaller, more focused modules?**
  _Cohesion score 0.14509246088193456 - nodes in this community are weakly interconnected._