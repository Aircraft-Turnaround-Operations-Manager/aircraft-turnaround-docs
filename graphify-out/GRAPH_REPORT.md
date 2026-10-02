# Graph Report - aircraft-turnaround-docs  (2026-10-02)

## Corpus Check
- 69 files · ~33,767 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 243 nodes · 588 edges · 9 communities
- Extraction: 80% EXTRACTED · 20% INFERRED · 0% AMBIGUOUS · INFERRED: 117 edges (avg confidence: 0.87)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Objetivos, liberação e QR Code
- Similares, insumos e abastecimento
- Contexto: atores, estados e régua
- Metas, tolerâncias e aderência ao TOBT
- Regras para IAs e processo do RA1
- Fontes e referências da pesquisa
- Atores e nome do coordenador
- A-CDM: marcos e siglas
- Códigos de atraso (ANAC/IATA)

## God Nodes (most connected - your core abstractions)
1. `CONTEXT.md — Contexto do projeto` - 37 edges
2. `Pesquisa - mapa da base de conhecimento` - 32 edges
3. `Fontes da pesquisa` - 31 edges
4. `Aircraft Turnaround Orchestration System` - 18 edges
5. `Lacunas e diferencial possivel (3.4)` - 17 edges
6. `Tolerancias e indicadores de aderencia (P1.3)` - 17 edges
7. `Impacto por item do template (4.2)` - 15 edges
8. `Matriz comparativa (3.3)` - 15 edges
9. `ADR-0001 — TOBT planejado + 5 min` - 14 edges
10. `Marcos e horarios do A-CDM (P1.2)` - 14 edges

## Surprising Connections (you probably didn't know these)
- `Sinalizar conflitos com ADRs` --semantically_similar_to--> `Precedência: ADRs > pesquisa > rascunhos`  [INFERRED] [semantically similar]
  docs/agents/domain.md → CONTEXT.md
- `Orientacao ao plano (aderencia a janela planejada)` --semantically_similar_to--> `Princípio: previsibilidade, não velocidade`  [INFERRED] [semantically similar]
  especificacao/02-e-nao-e-faz-nao-faz.md → CONTEXT.md
- `Rótulos ra1 / item-NN / area-x / por-integrante` --semantically_similar_to--> `Vocabulário de triage (needs-triage, needs-info, ready-for-agent, ready-for-human, wontfix)`  [INFERRED] [semantically similar]
  entregas/ra1-tarefas.md → docs/agents/triage-labels.md
- `Item 3 Visao do Produto` --references--> `Aircraft Turnaround Orchestration System`  [INFERRED]
  especificacao/03-visao-do-produto.md → CONTEXT.md
- `Item 4 Mapeamento de Negocios (BPMN to-be)` --references--> `Aircraft Turnaround Orchestration System`  [INFERRED]
  especificacao/04-mapeamento-de-negocios.md → CONTEXT.md

## Hyperedges (group relationships)
- **Atores do turnaround (operador, Coordenador, autoridade)** — especificacao_02_e_nao_e_faz_nao_faz_operador_de_solo, pesquisa_topicos_papeis_e_atores_coordenador_de_turnaround, pesquisa_topicos_papeis_e_atores_autoridade_de_liberacao [EXTRACTED 1.00]
- **Régua de horário e metas (TOBT + 5 min, 80%, antecipação)** — docs_adr_0001_referencia_horario_tobt_mais_5_min_d1_tobt_mais_5_min, docs_adr_0002_metas_percentuais_80_d2_metas_80, docs_adr_0003_atualizar_previsao_na_antecipacao_d3_atualizar_previsao_antecipacao, context_tobt, context_metas_do_item_1 [EXTRACTED 1.00]
- **Five market similars compared in matrix 3.3** — pesquisa_similares_assaia_assaia_apronai_turnaroundcontrol, pesquisa_similares_inform_groundstar_inform_groundstar, pesquisa_similares_adb_safegate_adb_safegate_safedock_apron_manager, pesquisa_similares_veovo_veovo_acdm, pesquisa_similares_sita_sita_airport_management_cdm, pesquisa_similares_matriz_comparativa_capacidades_do_nucleo [EXTRACTED 1.00]
- **Project differentiators DF1-DF5** — pesquisa_similares_lacunas_e_diferencial_df1, pesquisa_similares_lacunas_e_diferencial_df2, pesquisa_similares_lacunas_e_diferencial_df3, pesquisa_similares_lacunas_e_diferencial_df4, pesquisa_similares_lacunas_e_diferencial_df5 [EXTRACTED 1.00]
- **Quatro atores do Aircraft Turnaround Orchestration System** — context_operador_de_solo_rampa, context_coordenador_de_turnaround, context_autoridade_de_liberacao, context_motor_de_eventos [EXTRACTED 1.00]
- **'Risco ao horario' trigger set (T8, T11, T12)** — pesquisa_impacto_impacto_por_item_risco_ao_horario, pesquisa_topicos_tolerancias_e_indicadores_tobt_mais_5_min, pesquisa_topicos_tolerancias_e_indicadores_t11_viabilidade_eibt_mttt, pesquisa_topicos_tolerancias_e_indicadores_t12_embarque_nao_iniciado [EXTRACTED 1.00]
- **Liberacao segura da aeronave** — especificacao_01_3_objetivos_liberacao_da_aeronave, especificacao_02_e_nao_e_faz_nao_faz_bloqueio_de_liberacao_com_pendencia, pesquisa_topicos_papeis_e_atores_autoridade_de_liberacao, especificacao_01_3_objetivos_metrica_alertas_e_zero_liberacoes_pendentes [INFERRED 0.85]
- **Monitoramento de risco (projecao, caminho critico, painel, alertas)** — especificacao_01_3_objetivos_projecao_de_conclusao, especificacao_01_3_objetivos_caminho_critico, especificacao_01_3_objetivos_painel_operacional, especificacao_01_3_objetivos_alerta_de_risco, especificacao_02_e_nao_e_faz_nao_faz_area_c [INFERRED 0.85]
- **Governança de consistência documental** — context_precedencia_adr_pesquisa, docs_agents_domain_flag_adr_conflicts, entregas_ra1_criterios_de_aceite_k11_consistencia_context_adr, entregas_ra1_criterios_de_aceite_protocolo_execucao_verificacao [INFERRED 0.85]
- **Cadeia de rastreabilidade RF, US, RNF, UC por area** — especificacao_06_requisitos_funcionais_00_item_item, especificacao_07_estorias_de_usuario_00_item_item, especificacao_08_requisitos_nao_funcionais_00_item_item, especificacao_09_diagrama_geral_de_casos_de_uso_item, especificacao_10_especificacoes_de_caso_de_uso_00_item_item [INFERRED 0.85]

## Communities (9 total, 0 thin omitted)

### Community 0 - "Objetivos, liberação e QR Code"
Cohesion: 0.08
Nodes (41): Diferencial DF5 (QR Code por assento/fileira/zona), Leitura de QR Code pelo celular, Alerta de risco ao horario planejado, Caminho critico, Liberacao da aeronave, Metrica: alertas em 5 s, 90% acoes em 2 min, 0 liberacoes com pendencia, Metrica: 100% tarefas com responsavel, painel atualizado em ate 5 s, Objetivo 2: Sincronizar equipes, recursos e atividades paralelas (+33 more)

### Community 1 - "Similares, insumos e abastecimento"
Cohesion: 0.13
Nodes (35): ADR-0005 — Abastecimento com passageiros configurável, EASA CAT.OP.MPA.195, ANAC RBAC 91.102(g), ADR-0007 — Dados do operador e QR Code, Assaia case study - turnaround time reduction via alerts [42], INFORM GroundStar demo clips [45], Insumos para os RFs, por area (4.3), Observed capabilities by area A-D (RF inputs) (+27 more)

### Community 2 - "Contexto: atores, estados e régua"
Cohesion: 0.12
Nodes (28): CONTEXT.md — Contexto do projeto, A-CDM (Airport Collaborative Decision Making), AEGT — Fim real do atendimento em solo, Aircraft Turnaround Orchestration System, ARDT — Horário real de prontidão (Aircraft Ready), Autoridade de Liberação, Coordenador de Turnaround, Estados da tarefa (+20 more)

### Community 3 - "Metas, tolerâncias e aderência ao TOBT"
Cohesion: 0.13
Nodes (28): ADR-0001 — TOBT planejado + 5 min, ADR-0002 — Metas percentuais 80%, ADR-0003 — Atualizar previsão na antecipação, Dublin Airport A-CDM Operational Procedures [8], EUROCONTROL A-CDM Specification draft (2024) [3], Heathrow AOP2 user manual [7], IATA A-CDM Recommendations (2018) [5], German airports A-CDM Ramp Reference Card v3.1 [13] (+20 more)

### Community 4 - "Regras para IAs e processo do RA1"
Cohesion: 0.09
Nodes (21): Formato de arquivo de pesquisa (YAML + seção Ligações), Domain Docs, Usar o vocabulário do glossário do CONTEXT.md, Issue tracker: GitHub, GitHub Issues via gh CLI, Wayfinding (map issue + child tickets), Triage Labels, Vocabulário de triage (needs-triage, needs-info, ready-for-agent, ready-for-human, wontfix) (+13 more)

### Community 5 - "Fontes e referências da pesquisa"
Cohesion: 0.15
Nodes (21): Fontes da pesquisa, EUROCONTROL A-CDM Impact Assessment (2016) [14], ANAC RBAC 91 Emenda 05, 91.102(g) [27], Assaia - value of accurate off-block predictions [19], EUROCONTROL CODA Digest 2023 [16], EASA Part-CAT CAT.OP.MPA.195 [26], GE Aerospace - Airport Cleanliness app (QR) [63], Kierzkowski et al. 2025 - PERT-COST ground handling [22] (+13 more)

### Community 6 - "Atores e nome do coordenador"
Cohesion: 0.19
Nodes (18): ADR-0004 — Quatro atores e Autoridade de Liberação, ADR-0009 — Nome Coordenador de Turnaround, Índice de decisões (ADRs), K.1 — Atores com nomes idênticos, Operador de solo, Orquestracao operacional em tempo real, Replanejamento e redistribuicao de recursos, Item 5 Relacao de Atores/Usuarios (+10 more)

### Community 7 - "A-CDM: marcos e siglas"
Cohesion: 0.18
Nodes (16): ADR-0008 — Siglas A-CDM com nome em português, Airport CDM Implementation Manual v5.0 (ACI/EUROCONTROL/IATA) [4], EUROCONTROL A-CDM concept page [1], EUROCONTROL Specification for A-CDM Ed. 1.0 (2025) [2], M9: zero releases with pending task or open exception, DF2 release blocked with pending task or open exception, O que e o A-CDM (P1.1), A-CDM (Airport Collaborative Decision Making) (+8 more)

### Community 8 - "Códigos de atraso (ANAC/IATA)"
Cohesion: 0.18
Nodes (15): ADR-0006 — Códigos de atraso tabela ANAC, IATA AHM 730, IATA AHM 732, ANAC Portaria nº 55/2026, ANAC Portaria Regulatoria 55/SPO/SSA 2026 (72 delay codes) [62], IATA AHM 732 delay codes webinar [37], E / Nao e / Faz / Nao faz candidates, Codigos de atraso (P1.8) (+7 more)

## Knowledge Gaps
- **19 isolated node(s):** `Item 3 Visao do Produto`, `Item 4 Mapeamento de Negocios (BPMN to-be)`, `Item 11 Diagrama de Atividades`, `Amadeus (excluded candidate)`, `Cosmos (excluded candidate)` (+14 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 21 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `CONTEXT.md — Contexto do projeto` connect `Contexto: atores, estados e régua` to `Similares, insumos e abastecimento`, `Metas, tolerâncias e aderência ao TOBT`, `Regras para IAs e processo do RA1`, `Fontes e referências da pesquisa`, `Atores e nome do coordenador`, `A-CDM: marcos e siglas`, `Códigos de atraso (ANAC/IATA)`?**
  _High betweenness centrality (0.417) - this node is a cross-community bridge._
- **Why does `Fontes da pesquisa` connect `Fontes e referências da pesquisa` to `Similares, insumos e abastecimento`, `Contexto: atores, estados e régua`, `Metas, tolerâncias e aderência ao TOBT`, `Regras para IAs e processo do RA1`, `Atores e nome do coordenador`, `A-CDM: marcos e siglas`, `Códigos de atraso (ANAC/IATA)`?**
  _High betweenness centrality (0.220) - this node is a cross-community bridge._
- **Why does `Pesquisa - mapa da base de conhecimento` connect `Similares, insumos e abastecimento` to `Contexto: atores, estados e régua`, `Metas, tolerâncias e aderência ao TOBT`, `Fontes e referências da pesquisa`, `Atores e nome do coordenador`, `A-CDM: marcos e siglas`, `Códigos de atraso (ANAC/IATA)`?**
  _High betweenness centrality (0.208) - this node is a cross-community bridge._
- **Are the 9 inferred relationships involving `Aircraft Turnaround Orchestration System` (e.g. with `Item 3 Visao do Produto` and `Item 4 Mapeamento de Negocios (BPMN to-be)`) actually correct?**
  _`Aircraft Turnaround Orchestration System` has 9 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Item 3 Visao do Produto`, `Item 4 Mapeamento de Negocios (BPMN to-be)`, `Item 11 Diagrama de Atividades` to the rest of the system?**
  _19 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Objetivos, liberação e QR Code` be split into smaller, more focused modules?**
  _Cohesion score 0.08456659619450317 - nodes in this community are weakly interconnected._
- **Should `Similares, insumos e abastecimento` be split into smaller, more focused modules?**
  _Cohesion score 0.12698412698412698 - nodes in this community are weakly interconnected._