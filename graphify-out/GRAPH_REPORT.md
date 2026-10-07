# Graph Report - aircraft-turnaround-docs  (2026-10-06)

## Corpus Check
- 72 files · ~71,368 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 418 nodes · 1622 edges · 10 communities
- Extraction: 74% EXTRACTED · 26% INFERRED · 0% AMBIGUOUS · INFERRED: 420 edges (avg confidence: 0.89)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Regras para IAs, README, plano e critérios
- Decisões (ADRs) e fontes da pesquisa
- Liberação, exceções e estados do turnaround
- Área B: RFs, estórias, casos de uso e estados da tarefa
- Visão do Produto, painel e redistribuição
- Risco ao horário, antecipação e alertas
- BPMN: tarefas de solo e abastecimento
- Similares de mercado
- Fora de escopo e leitura do BPMN
- Metas do item 1

## God Nodes (most connected - your core abstractions)
1. `Fontes da pesquisa` - 63 edges
2. `CONTEXT.md — Contexto do projeto` - 46 edges
3. `Operador de Solo/Rampa` - 41 edges
4. `Pesquisa - mapa da base de conhecimento` - 35 edges
5. `EUROCONTROL Specification for A-CDM Ed. 1.0 (2025) [2]` - 33 edges
6. `Operador de Solo/Rampa (lane do BPMN)` - 31 edges
7. `ADR-0010 — Administrador do Sistema, ator abstrato Usuário e equipe do operador como dado` - 29 edges
8. `D11 — Mínimo de 4 por integrante, sem máximo; IDs provisórios por área e renumeração única no início do T12` - 29 edges
9. `Item 4 Mapeamento de Negocios (BPMN to-be)` - 29 edges
10. `README.md — aircraft-turnaround-docs` - 28 edges

## Surprising Connections (you probably didn't know these)
- `Motor de Eventos` --semantically_similar_to--> `A-CDM System / information platform`  [INFERRED] [semantically similar]
  CONTEXT.md → pesquisa/topicos/papeis-e-atores.md
- `Propagar estados e recalcular projeção, caminho crítico e aderência ao TOBT + 5 min` --conceptually_related_to--> `ADR-0001 — TOBT planejado + 5 min`  [INFERRED]
  especificacao/diagramas/04-bpmn-to-be.png → docs/adr/0001-referencia-horario-tobt-mais-5-min.md
- `Tratar o alerta: redistribuir recursos, replanejar e registrar a causa (código ANAC)` --conceptually_related_to--> `ADR-0006 — Códigos de atraso tabela ANAC`  [INFERRED]
  especificacao/diagramas/04-bpmn-to-be.png → docs/adr/0006-codigos-de-atraso-tabela-anac.md
- `Autoridade de Liberação (item 5)` --semantically_similar_to--> `Autoridade de Liberação`  [INFERRED] [semantically similar]
  especificacao/05-atores-usuarios.md → CONTEXT.md
- `Verificar tarefas obrigatórias e exceções abertas (Pronto para liberação)` --conceptually_related_to--> `Estados do turnaround`  [INFERRED]
  especificacao/diagramas/04-bpmn-to-be.png → CONTEXT.md

## Hyperedges (group relationships)
- **Cadeia RF → estória das ações de execução de tarefa do Operador de Solo/Rampa (RF-B2 a RF-B6, US-B2 a US-B6)** — especificacao_06_requisitos_funcionais_area_b_rf_b2, especificacao_06_requisitos_funcionais_area_b_rf_b3, especificacao_06_requisitos_funcionais_area_b_rf_b4, especificacao_06_requisitos_funcionais_area_b_rf_b5, especificacao_06_requisitos_funcionais_area_b_rf_b6, especificacao_07_estorias_de_usuario_area_b_us_b2, especificacao_07_estorias_de_usuario_area_b_us_b3, especificacao_07_estorias_de_usuario_area_b_us_b4, especificacao_07_estorias_de_usuario_area_b_us_b5, especificacao_07_estorias_de_usuario_area_b_us_b6 [EXTRACTED 1.00]
- **Casos de uso da área B (UC-B1 a UC-B8)** — especificacao_10_especificacoes_de_caso_de_uso_area_b_uc_b1, especificacao_10_especificacoes_de_caso_de_uso_area_b_uc_b2, especificacao_10_especificacoes_de_caso_de_uso_area_b_uc_b3, especificacao_10_especificacoes_de_caso_de_uso_area_b_uc_b4, especificacao_10_especificacoes_de_caso_de_uso_area_b_uc_b5, especificacao_10_especificacoes_de_caso_de_uso_area_b_uc_b6, especificacao_10_especificacoes_de_caso_de_uso_area_b_uc_b7, especificacao_10_especificacoes_de_caso_de_uso_area_b_uc_b8 [EXTRACTED 1.00]
- **«include»: UC-B2, UC-B3 e UC-B5 incluem UC-B7 (marcos) e UC-B8 (propagação), executados pelo Motor de Eventos** — especificacao_10_especificacoes_de_caso_de_uso_area_b_uc_b2, especificacao_10_especificacoes_de_caso_de_uso_area_b_uc_b3, especificacao_10_especificacoes_de_caso_de_uso_area_b_uc_b5, especificacao_10_especificacoes_de_caso_de_uso_area_b_uc_b7, especificacao_10_especificacoes_de_caso_de_uso_area_b_uc_b8, context_motor_de_eventos [EXTRACTED 1.00]
- **Requisitos funcionais da área B (RF-B1 a RF-B8)** — especificacao_06_requisitos_funcionais_area_b_rf_b1, especificacao_06_requisitos_funcionais_area_b_rf_b2, especificacao_06_requisitos_funcionais_area_b_rf_b3, especificacao_06_requisitos_funcionais_area_b_rf_b4, especificacao_06_requisitos_funcionais_area_b_rf_b5, especificacao_06_requisitos_funcionais_area_b_rf_b6, especificacao_06_requisitos_funcionais_area_b_rf_b7, especificacao_06_requisitos_funcionais_area_b_rf_b8 [EXTRACTED 1.00]
- **Requisitos não funcionais da área B (RNF-B1 a RNF-B4)** — especificacao_08_requisitos_nao_funcionais_area_b_rnf_b1, especificacao_08_requisitos_nao_funcionais_area_b_rnf_b2, especificacao_08_requisitos_nao_funcionais_area_b_rnf_b3, especificacao_08_requisitos_nao_funcionais_area_b_rnf_b4 [EXTRACTED 1.00]
- **Requisitos funcionais da área D (RF-D1 a RF-D9)** — especificacao_06_requisitos_funcionais_area_d_area_d, especificacao_06_requisitos_funcionais_area_d_rf_d1, especificacao_06_requisitos_funcionais_area_d_rf_d2, especificacao_06_requisitos_funcionais_area_d_rf_d3, especificacao_06_requisitos_funcionais_area_d_rf_d4, especificacao_06_requisitos_funcionais_area_d_rf_d5, especificacao_06_requisitos_funcionais_area_d_rf_d6, especificacao_06_requisitos_funcionais_area_d_rf_d7, especificacao_06_requisitos_funcionais_area_d_rf_d8, especificacao_06_requisitos_funcionais_area_d_rf_d9 [EXTRACTED 1.00]
- **Cinco atores da Relação de Atores / Usuários (item 5)** — especificacao_05_atores_usuarios_operador_de_solo_rampa, especificacao_05_atores_usuarios_coordenador_de_turnaround, especificacao_05_atores_usuarios_autoridade_de_liberacao, especificacao_05_atores_usuarios_administrador_do_sistema, especificacao_05_atores_usuarios_motor_de_eventos [EXTRACTED 1.00]
- **Atores humanos generalizados pelo ator abstrato Usuário** — context_usuario_ator_abstrato, context_operador_de_solo_rampa, pesquisa_topicos_papeis_e_atores_coordenador_de_turnaround, context_autoridade_de_liberacao, context_administrador_do_sistema [EXTRACTED 1.00]
- **Atores do turnaround (Operador de Solo/Rampa, Coordenador de Turnaround, Autoridade de Liberação)** — context_operador_de_solo_rampa, pesquisa_topicos_papeis_e_atores_coordenador_de_turnaround, pesquisa_topicos_papeis_e_atores_autoridade_de_liberacao [EXTRACTED 1.00]
- **Lanes do pool do turnaround (BPMN TO BE)** — especificacao_diagramas_04_bpmn_to_be_lane_coordenador_de_turnaround, especificacao_diagramas_04_bpmn_to_be_lane_operador_de_solo_rampa, especificacao_diagramas_04_bpmn_to_be_lane_motor_de_eventos, especificacao_diagramas_04_bpmn_to_be_lane_autoridade_de_liberacao [EXTRACTED 1.00]
- **Quatro subprocessos de evento do BPMN TO BE** — especificacao_diagramas_04_bpmn_to_be_subprocesso_monitoramento_a_cada_registro, especificacao_diagramas_04_bpmn_to_be_subprocesso_tratamento_de_alerta_de_risco, especificacao_diagramas_04_bpmn_to_be_subprocesso_atualizacao_da_previsao, especificacao_diagramas_04_bpmn_to_be_subprocesso_checagem_em_tobt_menos_15_min [EXTRACTED 1.00]
- **Ramos em paralelo após o início do atendimento em solo (ACGT)** — especificacao_diagramas_04_bpmn_to_be_tarefa_desembarcar_os_passageiros, especificacao_diagramas_04_bpmn_to_be_tarefa_descarregar_bagagem_e_carga, especificacao_diagramas_04_bpmn_to_be_tarefa_abastecer_a_aeronave, especificacao_diagramas_04_bpmn_to_be_tarefa_atender_agua_potavel_e_lavatorios, especificacao_diagramas_04_bpmn_to_be_tarefa_inspecao_tecnica_de_transito [EXTRACTED 1.00]
- **Régua de horário e metas (TOBT + 5 min, 80%, antecipação)** — docs_adr_0001_referencia_horario_tobt_mais_5_min_d1_tobt_mais_5_min, docs_adr_0002_metas_percentuais_80_d2_metas_80, docs_adr_0003_atualizar_previsao_na_antecipacao_d3_atualizar_previsao_antecipacao, context_tobt, context_metas_do_item_1 [EXTRACTED 1.00]
- **Five market similars compared in matrix 3.3** — pesquisa_similares_assaia_assaia_apronai_turnaroundcontrol, pesquisa_similares_inform_groundstar_inform_groundstar, pesquisa_similares_adb_safegate_adb_safegate_safedock_apron_manager, pesquisa_similares_veovo_veovo_acdm, pesquisa_similares_sita_sita_airport_management_cdm, pesquisa_similares_matriz_comparativa_capacidades_do_nucleo [EXTRACTED 1.00]
- **Project differentiators DF1-DF5** — pesquisa_similares_lacunas_e_diferencial_df1, pesquisa_similares_lacunas_e_diferencial_df2, pesquisa_similares_lacunas_e_diferencial_df3, pesquisa_similares_lacunas_e_diferencial_df4, pesquisa_similares_lacunas_e_diferencial_df5 [EXTRACTED 1.00]
- **Quatro atores operacionais do Aircraft Turnaround Orchestration System** — context_operador_de_solo_rampa, pesquisa_topicos_papeis_e_atores_coordenador_de_turnaround, context_autoridade_de_liberacao, context_motor_de_eventos [EXTRACTED 1.00]
- **Regra D11: mínimo sem máximo, IDs provisórios e renumeração no T12** — docs_adr_0011_minimo_por_integrante_e_numeracao_provisoria_d11_minimo_sem_maximo_numeracao_provisoria, docs_adr_0011_minimo_por_integrante_e_numeracao_provisoria_ids_provisorios_por_area, docs_adr_0011_minimo_por_integrante_e_numeracao_provisoria_renumeracao_unica_t12, entregas_ra1_criterios_de_aceite_x8_regra_4_por_integrante, entregas_ra1_tarefas_areas_funcionais_a_d, entregas_ra1_tarefas_t12_revisao_cruzada, readme_quantidade_e_numeracao [EXTRACTED 1.00]
- **Três camadas da base de conhecimento (decisões, pesquisa, resumo)** — docs_adr_readme, pesquisa_readme, context [EXTRACTED 1.00]
- **'Risco ao horario' trigger set (T8, T11, T12)** — pesquisa_impacto_impacto_por_item_risco_ao_horario, pesquisa_topicos_tolerancias_e_indicadores_tobt_mais_5_min, pesquisa_topicos_tolerancias_e_indicadores_t11_viabilidade_eibt_mttt, pesquisa_topicos_tolerancias_e_indicadores_t12_embarque_nao_iniciado [EXTRACTED 1.00]
- **Campos da Visão de Produto (cliente-alvo, categoria-segmento, benefício-chave, diferencial-chave, meta-valor)** — especificacao_03_visao_do_produto_cliente_alvo, especificacao_03_visao_do_produto_categoria_segmento, especificacao_03_visao_do_produto_beneficio_chave, especificacao_03_visao_do_produto_diferencial_chave, especificacao_03_visao_do_produto_meta_valor [EXTRACTED 1.00]
- **Problemas P1–P5 da Visão do Produto** — especificacao_03_visao_do_produto_p1, especificacao_03_visao_do_produto_p2, especificacao_03_visao_do_produto_p3, especificacao_03_visao_do_produto_p4, especificacao_03_visao_do_produto_p5 [EXTRACTED 1.00]
- **Cadeia RF → estória → caso de uso da conclusão de tarefa com marcos e propagação (RF/US/UC-B3, B7 e B8)** — especificacao_06_requisitos_funcionais_area_b_rf_b3, especificacao_07_estorias_de_usuario_area_b_us_b3, especificacao_10_especificacoes_de_caso_de_uso_area_b_uc_b3, especificacao_06_requisitos_funcionais_area_b_rf_b7, especificacao_07_estorias_de_usuario_area_b_us_b7, especificacao_10_especificacoes_de_caso_de_uso_area_b_uc_b7, especificacao_06_requisitos_funcionais_area_b_rf_b8, especificacao_07_estorias_de_usuario_area_b_us_b8, especificacao_10_especificacoes_de_caso_de_uso_area_b_uc_b8 [INFERRED 0.85]
- **Governança de consistência documental** — context_precedencia_adr_pesquisa, docs_agents_domain_flag_adr_conflicts, entregas_ra1_criterios_de_aceite_k11_consistencia_context_adr, entregas_ra1_criterios_de_aceite_protocolo_execucao_verificacao [INFERRED 0.85]
- **Cadeia de rastreabilidade RF, US, RNF, UC por area** — especificacao_06_requisitos_funcionais_00_item_item, especificacao_07_estorias_de_usuario_00_item_item, especificacao_08_requisitos_nao_funcionais_00_item_item, especificacao_09_diagrama_geral_de_casos_de_uso_item, especificacao_10_especificacoes_de_caso_de_uso_00_item_item [INFERRED 0.85]
- **Ciclo de vida da exceção e bloqueio da liberação (RF-D1, RF-D5, RF-D4)** — especificacao_06_requisitos_funcionais_area_d_rf_d1, especificacao_06_requisitos_funcionais_area_d_rf_d5, especificacao_06_requisitos_funcionais_area_d_rf_d4 [INFERRED 0.95]
- **Reatribuição de tarefa entre operadores da mesma equipe (RF-D2, RF-D8)** — especificacao_06_requisitos_funcionais_area_d_rf_d2, especificacao_06_requisitos_funcionais_area_d_rf_d8 [INFERRED 0.95]

## Communities (10 total, 0 thin omitted)

### Community 0 - "Regras para IAs, README, plano e critérios"
Cohesion: 0.07
Nodes (66): Formato de arquivo de pesquisa (YAML + seção Ligações), AGENTS.md regra 8 — registrar a suposição sobre outra área em vez de inventar o requisito, CONTEXT.md — Contexto do projeto, Administrador do Sistema, Aircraft Turnaround Orchestration System, Tabela "O que ler para cada item", Usuário (ator abstrato), ADR-0004 — Quatro atores e Autoridade de Liberação (+58 more)

### Community 1 - "Decisões (ADRs) e fontes da pesquisa"
Cohesion: 0.08
Nodes (70): ADR-0001 — TOBT planejado + 5 min, ADR-0002 — Metas percentuais 80%, ADR-0003 — Atualizar previsão na antecipação, ADR-0005 — Abastecimento com passageiros configurável, ADR-0006 — Códigos de atraso tabela ANAC, Fluxo de trabalho 1.3: diagramas em Mermaid/PlantUML, exceto o BPMN do item 4 em BPMN 2.0 (.bpmn), Leitura do diagrama: caminho principal (abertura, viabilidade, AIBT, ACGT, tarefas em paralelo, ASBT, loadsheet, AEGT, ARDT, AOBT), Leitura do diagrama: eventos e mensagens (chegada, autorização do ATC, sinais de desembarque/abastecimento concluído, temporizador TOBT − 15 min) (+62 more)

### Community 2 - "Liberação, exceções e estados do turnaround"
Cohesion: 0.08
Nodes (57): AEGT — Fim real do atendimento em solo, ARDT — Horário real de prontidão (Aircraft Ready), Autoridade de Liberação, Estados do turnaround, TOBT — Horário-alvo de prontidão, TSAT — Horário-alvo de autorização de acionamento, IATA AHM 730, IATA AHM 732 (+49 more)

### Community 3 - "Área B: RFs, estórias, casos de uso e estados da tarefa"
Cohesion: 0.15
Nodes (50): Estados da tarefa, Motor de Eventos, Operador de Solo/Rampa, EASA CAT.OP.MPA.195, ANAC RBAC 91.102(g), ADR-0007 — Dados do operador e QR Code, Diferencial DF5 (QR Code por assento/fileira/zona), Leitura de QR Code pelo celular (+42 more)

### Community 4 - "Visão do Produto, painel e redistribuição"
Cohesion: 0.08
Nodes (50): Metrica: 100% tarefas com responsavel, painel atualizado em ate 5 s, Painel operacional, Replanejamento e redistribuicao de recursos, Benefício-chave: aeronave pronta para liberação no TOBT, desvios tratados durante a operação, Categoria-segmento: software de gestão de turnaround / operações de solo, Diferencial-chave: grafo de tarefas com caminho crítico, bloqueio da liberação, registro pelo operador com QR Code, régua TOBT + 5 min, E2: turnaround dentro do planejado, medido pela régua TOBT planejado + 5 min, E3: visão única de tarefas, responsáveis, dependências e estados, painel em até 5 s (+42 more)

### Community 5 - "Risco ao horário, antecipação e alertas"
Cohesion: 0.14
Nodes (31): MTTT — Tempo mínimo de turnaround, Risco ao horário (gatilhos A-CDM), Aviso de antecipação >= 5 min, RF-D3 — Registrar a ação tomada para cada alerta (reatribuir, replanejar, atualizar a previsão ou abrir exceção), encerrando o alerta, RF-D6 — Solicitar a atualização do TOBT quando a projeção de prontidão se afastar 5 min ou mais, para mais ou para menos, Evento de início (mensagem): Voo previsto para a posição, Evento de início (mensagem, não interruptivo): Registro de andamento recebido (início, pausa, conclusão, não aplicável, QR Code), Evento de início (temporizador, não interruptivo): TOBT − 15 min (+23 more)

### Community 6 - "BPMN: tarefas de solo e abastecimento"
Cohesion: 0.20
Nodes (24): Gateway exclusivo (abastecimento): Abastecimento com passageiros permitido? (Sim → abastecer; Não → aguardar "Desembarque concluído"), Gateway exclusivo (embarque): Abastecimento com passageiros permitido? (Sim → embarcar; Não → aguardar "Abastecimento concluído"), Gateway paralelo: abertura das tarefas em paralelo após o ACGT, Gateway paralelo: junção de embarque e carregamento de bagagem e carga, Gateway paralelo: junção final das tarefas de solo, Gateway paralelo: junção de limpeza e catering, Gateway paralelo: limpeza da cabine e catering após o desembarque, Operador de Solo/Rampa (lane do BPMN) (+16 more)

### Community 7 - "Similares de mercado"
Cohesion: 0.24
Nodes (17): Ficha - ADB SAFEGATE, ADB SAFEGATE Safedock + Apron Manager, Ficha - Assaia, Ficha - INFORM GroundStar, INFORM GroundStar (TurnManager, TeamWork), Lacunas e diferencial possivel (3.4), Observed gaps in similar products, Matriz comparativa (3.3) (+9 more)

### Community 8 - "Fora de escopo e leitura do BPMN"
Cohesion: 0.25
Nodes (14): Fora de escopo (voos, tripulação, financeiro, ATC), Fora de escopo: malha aerea, slots, ATC, escalas, financeiro, visao computacional/sensores, Não define o turnaround programado nem o MTTT (dados de entrada), Leitura do diagrama: pool e lanes (uma lane por ator; ATC como pool externo fechado), Administrador do Sistema (item 5), Autoridade de Liberação (item 5), Coordenador de Turnaround (item 5), Fora do sistema: ATC, tripulação e centro de operações do aeroporto não são atores (+6 more)

### Community 9 - "Metas do item 1"
Cohesion: 0.33
Nodes (10): Metas do item 1 (precisão, sincronização, desvios), Heathrow pontualidade "verde" (>=79%), Janela planejada, Metrica: 80% das atividades na janela e 80% dos turnarounds prontos ate o TOBT planejado (tolerancia 5 min), Objetivo 1: Assegurar a precisao temporal do turnaround, Quadro 3 Objetivos, Meta-valor: 80% dos turnarounds prontos até TOBT planejado + 5 min, 80% das atividades na janela, 0 liberações com pendência, Heathrow AOP2 user manual [7] (+2 more)

## Knowledge Gaps
- **9 isolated node(s):** `Amadeus (excluded candidate)`, `Cosmos (excluded candidate)`, `IATA AHM 732`, `GRU first A-CDM airport in Brazil (2020)`, `Item 11 Diagrama de Atividades` (+4 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 9 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Fontes da pesquisa` connect `Visão do Produto, painel e redistribuição` to `Regras para IAs, README, plano e critérios`, `Decisões (ADRs) e fontes da pesquisa`, `Liberação, exceções e estados do turnaround`, `Área B: RFs, estórias, casos de uso e estados da tarefa`, `Risco ao horário, antecipação e alertas`, `Fora de escopo e leitura do BPMN`, `Metas do item 1`?**
  _High betweenness centrality (0.200) - this node is a cross-community bridge._
- **Why does `CONTEXT.md — Contexto do projeto` connect `Regras para IAs, README, plano e critérios` to `Decisões (ADRs) e fontes da pesquisa`, `Liberação, exceções e estados do turnaround`, `Área B: RFs, estórias, casos de uso e estados da tarefa`, `Visão do Produto, painel e redistribuição`, `Risco ao horário, antecipação e alertas`, `Fora de escopo e leitura do BPMN`, `Metas do item 1`?**
  _High betweenness centrality (0.127) - this node is a cross-community bridge._
- **Why does `Pesquisa - mapa da base de conhecimento` connect `Decisões (ADRs) e fontes da pesquisa` to `Regras para IAs, README, plano e critérios`, `Liberação, exceções e estados do turnaround`, `Área B: RFs, estórias, casos de uso e estados da tarefa`, `Visão do Produto, painel e redistribuição`, `Similares de mercado`?**
  _High betweenness centrality (0.085) - this node is a cross-community bridge._
- **Are the 8 inferred relationships involving `Operador de Solo/Rampa` (e.g. with `Equipe ou especialidade do operador como dado do cadastro (não um ator por especialidade)` and `Leitura de QR Code pelo celular`) actually correct?**
  _`Operador de Solo/Rampa` has 8 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Amadeus (excluded candidate)`, `Cosmos (excluded candidate)`, `IATA AHM 732` to the rest of the system?**
  _9 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Regras para IAs, README, plano e critérios` be split into smaller, more focused modules?**
  _Cohesion score 0.06962025316455696 - nodes in this community are weakly interconnected._
- **Should `Decisões (ADRs) e fontes da pesquisa` be split into smaller, more focused modules?**
  _Cohesion score 0.0782608695652174 - nodes in this community are weakly interconnected._