# Graph Report - aircraft-turnaround-docs  (2026-10-10)

## Corpus Check
- 99 files · ~219,665 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 5 file(s) not represented in the graph (top: (none) 4, .bpmn 1)

## Summary
- 537 nodes · 2505 edges · 9 communities
- Extraction: 75% EXTRACTED · 25% INFERRED · 0% AMBIGUOUS · INFERRED: 638 edges (avg confidence: 0.89)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `cf456ec5`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Fontes, pesquisa, serviços sob demanda e Visão do Produto
- CONTEXT, regras para IAs, plano, critérios e rastreabilidade
- Área B: operador, casos de uso, protótipos e RNFs
- Estados, liberação, chegada e saída (área D)
- Área D: casos de uso, replanejamento e TOBT
- Régua do TOBT, previsão e tolerâncias
- Área C, Motor de Eventos e objetivo 3
- BPMN: Motor de Eventos, monitoramento e checagem
- BPMN: tarefas de solo e abastecimento

## God Nodes (most connected - your core abstractions)
1. `Fontes da pesquisa` - 79 edges
2. `Operador de Solo/Rampa` - 67 edges
3. `Coordenador de Turnaround` - 65 edges
4. `Serviços sob demanda no turnaround (limpeza com risco biológico, assistência extra, catering adicional)` - 65 edges
5. `CONTEXT.md — Contexto do projeto` - 58 edges
6. `EUROCONTROL Specification for A-CDM Ed. 1.0 (2025) [2]` - 43 edges
7. `Objetivo 3: Antecipar desvios e assegurar liberacao segura` - 39 edges
8. `Pesquisa - mapa da base de conhecimento` - 38 edges
9. `Motor de Eventos` - 34 edges
10. `Estados do turnaround` - 33 edges

## Surprising Connections (you probably didn't know these)
- `Pool externo: Controle de tráfego aéreo (ATC) — fora do escopo` --semantically_similar_to--> `ATC — Controle de tráfego aéreo (fora de escopo)`  [INFERRED] [semantically similar]
  especificacao/diagramas/04-bpmn-to-be.png → CONTEXT.md
- `Turnaround critical path` --conceptually_related_to--> `Propagar estados e recalcular projeção, caminho crítico e aderência ao TOBT + 5 min`  [INFERRED]
  pesquisa/topicos/caminho-critico.md → especificacao/diagramas/04-bpmn-to-be.png
- `Boarding as critical activity` --conceptually_related_to--> `Embarcar os passageiros (ASBT)`  [INFERRED]
  pesquisa/topicos/caminho-critico.md → especificacao/diagramas/04-bpmn-to-be.png
- `A-CDM System / information platform` --semantically_similar_to--> `Motor de Eventos`  [INFERRED] [semantically similar]
  pesquisa/topicos/papeis-e-atores.md → CONTEXT.md
- `Tratar o alerta: redistribuir recursos, replanejar e registrar a causa (código ANAC)` --conceptually_related_to--> `ADR-0006 — Códigos de atraso tabela ANAC`  [INFERRED]
  especificacao/diagramas/04-bpmn-to-be.png → docs/adr/0006-codigos-de-atraso-tabela-anac.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Cadeia RF → estória das ações de execução de tarefa do Operador de Solo/Rampa (RF-B2 a RF-B6, US-B2 a US-B6)** — especificacao_06_requisitos_funcionais_area_b_rf_b2, especificacao_06_requisitos_funcionais_area_b_rf_b3, especificacao_06_requisitos_funcionais_area_b_rf_b4, especificacao_06_requisitos_funcionais_area_b_rf_b5, especificacao_06_requisitos_funcionais_area_b_rf_b6, especificacao_07_estorias_de_usuario_area_b_us_b2, especificacao_07_estorias_de_usuario_area_b_us_b3, especificacao_07_estorias_de_usuario_area_b_us_b4, especificacao_07_estorias_de_usuario_area_b_us_b5, especificacao_07_estorias_de_usuario_area_b_us_b6 [EXTRACTED 1.00]
- **Casos de uso da área B (UC-B1 a UC-B8)** — especificacao_10_especificacoes_de_caso_de_uso_area_b_uc_b1, especificacao_10_especificacoes_de_caso_de_uso_area_b_uc_b2, especificacao_10_especificacoes_de_caso_de_uso_area_b_uc_b3, especificacao_10_especificacoes_de_caso_de_uso_area_b_uc_b4, especificacao_10_especificacoes_de_caso_de_uso_area_b_uc_b5, especificacao_10_especificacoes_de_caso_de_uso_area_b_uc_b6, especificacao_10_especificacoes_de_caso_de_uso_area_b_uc_b7, especificacao_10_especificacoes_de_caso_de_uso_area_b_uc_b8 [EXTRACTED 1.00]
- **«include»: UC-B2, UC-B3 e UC-B5 incluem UC-B7 (marcos) e UC-B8 (propagação), executados pelo Motor de Eventos** — especificacao_10_especificacoes_de_caso_de_uso_area_b_uc_b2, especificacao_10_especificacoes_de_caso_de_uso_area_b_uc_b3, especificacao_10_especificacoes_de_caso_de_uso_area_b_uc_b5, especificacao_10_especificacoes_de_caso_de_uso_area_b_uc_b7, especificacao_10_especificacoes_de_caso_de_uso_area_b_uc_b8, context_motor_de_eventos [EXTRACTED 1.00]
- **Protótipos de tela da área B (UC-B1 a UC-B8)** — especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_b1_lista_de_tarefas, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_b1_detalhe_da_tarefa, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_b2_iniciar_tarefa, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_b3_concluir_tarefa, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_b4_pausar_tarefa, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_b4_retomar_tarefa, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_b5_nao_aplicavel, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_b6_leitura_qr_code, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_b6_pontos_da_tarefa, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_b7_marcos_do_turnaround, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_b8_propagacao_de_estado [EXTRACTED 1.00]
- **Requisitos funcionais da área B (RF-B1 a RF-B8)** — especificacao_06_requisitos_funcionais_area_b_rf_b1, especificacao_06_requisitos_funcionais_area_b_rf_b2, especificacao_06_requisitos_funcionais_area_b_rf_b3, especificacao_06_requisitos_funcionais_area_b_rf_b4, especificacao_06_requisitos_funcionais_area_b_rf_b5, especificacao_06_requisitos_funcionais_area_b_rf_b6, especificacao_06_requisitos_funcionais_area_b_rf_b7, especificacao_06_requisitos_funcionais_area_b_rf_b8 [EXTRACTED 1.00]
- **Requisitos não funcionais da área B (RNF-B1 a RNF-B4)** — especificacao_08_requisitos_nao_funcionais_area_b_rnf_b1, especificacao_08_requisitos_nao_funcionais_area_b_rnf_b2, especificacao_08_requisitos_nao_funcionais_area_b_rnf_b3, especificacao_08_requisitos_nao_funcionais_area_b_rnf_b4 [EXTRACTED 1.00]
- **Requisitos funcionais da área C (RF-C1 a RF-C14)** — especificacao_06_requisitos_funcionais_area_c_rf_c1, especificacao_06_requisitos_funcionais_area_c_rf_c2, especificacao_06_requisitos_funcionais_area_c_rf_c3, especificacao_06_requisitos_funcionais_area_c_rf_c4, especificacao_06_requisitos_funcionais_area_c_rf_c5, especificacao_06_requisitos_funcionais_area_c_rf_c6, especificacao_06_requisitos_funcionais_area_c_rf_c7, especificacao_06_requisitos_funcionais_area_c_rf_c8, especificacao_06_requisitos_funcionais_area_c_rf_c9, especificacao_06_requisitos_funcionais_area_c_rf_c10, especificacao_06_requisitos_funcionais_area_c_rf_c11, especificacao_06_requisitos_funcionais_area_c_rf_c12, especificacao_06_requisitos_funcionais_area_c_rf_c13, especificacao_06_requisitos_funcionais_area_c_rf_c14 [EXTRACTED 1.00]
- **Requisitos não funcionais da área C (RNF-C1 a RNF-C8)** — especificacao_08_requisitos_nao_funcionais_area_c_rnf_c1, especificacao_08_requisitos_nao_funcionais_area_c_rnf_c2, especificacao_08_requisitos_nao_funcionais_area_c_rnf_c3, especificacao_08_requisitos_nao_funcionais_area_c_rnf_c4, especificacao_08_requisitos_nao_funcionais_area_c_rnf_c5, especificacao_08_requisitos_nao_funcionais_area_c_rnf_c6, especificacao_08_requisitos_nao_funcionais_area_c_rnf_c7, especificacao_08_requisitos_nao_funcionais_area_c_rnf_c8 [EXTRACTED 1.00]
- **Casos de uso da área D: UC-D1 a UC-D9** — especificacao_10_especificacoes_de_caso_de_uso_area_d_uc_d1, especificacao_10_especificacoes_de_caso_de_uso_area_d_uc_d2, especificacao_10_especificacoes_de_caso_de_uso_area_d_uc_d3, especificacao_10_especificacoes_de_caso_de_uso_area_d_uc_d4, especificacao_10_especificacoes_de_caso_de_uso_area_d_uc_d5, especificacao_10_especificacoes_de_caso_de_uso_area_d_uc_d6, especificacao_10_especificacoes_de_caso_de_uso_area_d_uc_d7, especificacao_10_especificacoes_de_caso_de_uso_area_d_uc_d8, especificacao_10_especificacoes_de_caso_de_uso_area_d_uc_d9 [EXTRACTED 1.00]
- **Estórias da área D: US-D1 a US-D9** — especificacao_07_estorias_de_usuario_area_d_us_d1, especificacao_07_estorias_de_usuario_area_d_us_d2, especificacao_07_estorias_de_usuario_area_d_us_d3, especificacao_07_estorias_de_usuario_area_d_us_d4, especificacao_07_estorias_de_usuario_area_d_us_d5, especificacao_07_estorias_de_usuario_area_d_us_d6, especificacao_07_estorias_de_usuario_area_d_us_d7, especificacao_07_estorias_de_usuario_area_d_us_d8, especificacao_07_estorias_de_usuario_area_d_us_d9, especificacao_07_estorias_de_usuario_area_d_area_d [EXTRACTED 1.00]
- **Protótipos de tela da área D** — especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_d1_abrir_excecao, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_d2_reatribuir_tarefa, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_d3_registrar_acao_do_alerta, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_d4_confirmar_prontidao, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_d5_encerrar_excecao, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_d6_atualizar_tobt, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_d7_acionar_servico_sob_demanda, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_d7_replanejar_tarefas, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_d8_operadores_disponiveis, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_d9_registrar_saida_da_posicao [EXTRACTED 1.00]
- **Requisitos funcionais da área D (RF-D1 a RF-D9)** — especificacao_06_requisitos_funcionais_area_d_area_d, especificacao_06_requisitos_funcionais_area_d_rf_d1, especificacao_06_requisitos_funcionais_area_d_rf_d2, especificacao_06_requisitos_funcionais_area_d_rf_d3, especificacao_06_requisitos_funcionais_area_d_rf_d4, especificacao_06_requisitos_funcionais_area_d_rf_d5, especificacao_06_requisitos_funcionais_area_d_rf_d6, especificacao_06_requisitos_funcionais_area_d_rf_d7, especificacao_06_requisitos_funcionais_area_d_rf_d8, especificacao_06_requisitos_funcionais_area_d_rf_d9 [EXTRACTED 1.00]
- **Requisitos não funcionais da área D (RNF-D1 a RNF-D6)** — especificacao_08_requisitos_nao_funcionais_area_d_rnf_d1, especificacao_08_requisitos_nao_funcionais_area_d_rnf_d2, especificacao_08_requisitos_nao_funcionais_area_d_rnf_d3, especificacao_08_requisitos_nao_funcionais_area_d_rnf_d4, especificacao_08_requisitos_nao_funcionais_area_d_rnf_d5, especificacao_08_requisitos_nao_funcionais_area_d_rnf_d6 [EXTRACTED 1.00]
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
- **Rastreabilidade (ADR-0012): decisão, script, Apêndice A e critérios K.13, C08.6 e C10.10** — docs_adr_0012_matriz_de_rastreabilidade, docs_adr_0012_matriz_de_rastreabilidade_d12_matriz_apendice_sem_tabelas_base, scripts_gerar_matriz_rastreabilidade, especificacao_apendice_a_matriz_de_rastreabilidade, especificacao_apendice_a_matriz_de_rastreabilidade_matriz_de_rastreabilidade, entregas_ra1_criterios_de_aceite_k13_matriz_regerada_sem_lacunas, entregas_ra1_criterios_de_aceite_c08_6_rnf_cita_os_rfs, entregas_ra1_criterios_de_aceite_c10_10_caso_de_uso_cita_os_rfs [EXTRACTED 1.00]
- **Regra D11: mínimo sem máximo, IDs provisórios e renumeração no T12** — docs_adr_0011_minimo_por_integrante_e_numeracao_provisoria_d11_minimo_sem_maximo_numeracao_provisoria, docs_adr_0011_minimo_por_integrante_e_numeracao_provisoria_ids_provisorios_por_area, docs_adr_0011_minimo_por_integrante_e_numeracao_provisoria_renumeracao_unica_t12, entregas_ra1_criterios_de_aceite_x8_regra_4_por_integrante, entregas_ra1_tarefas_areas_funcionais_a_d, entregas_ra1_tarefas_t12_revisao_cruzada, readme_quantidade_e_numeracao [EXTRACTED 1.00]
- **Três camadas da base de conhecimento (decisões, pesquisa, resumo)** — docs_adr_readme, pesquisa_readme, context [EXTRACTED 1.00]
- **'Risco ao horario' trigger set (T8, T11, T12)** — pesquisa_impacto_impacto_por_item_risco_ao_horario, pesquisa_topicos_tolerancias_e_indicadores_tobt_mais_5_min, pesquisa_topicos_tolerancias_e_indicadores_t11_viabilidade_eibt_mttt, pesquisa_topicos_tolerancias_e_indicadores_t12_embarque_nao_iniciado [EXTRACTED 1.00]
- **Campos da Visão de Produto (cliente-alvo, categoria-segmento, benefício-chave, diferencial-chave, meta-valor)** — especificacao_03_visao_do_produto_cliente_alvo, especificacao_03_visao_do_produto_categoria_segmento, especificacao_03_visao_do_produto_beneficio_chave, especificacao_03_visao_do_produto_diferencial_chave, especificacao_03_visao_do_produto_meta_valor [EXTRACTED 1.00]
- **Problemas P1–P5 da Visão do Produto** — especificacao_03_visao_do_produto_p1, especificacao_03_visao_do_produto_p2, especificacao_03_visao_do_produto_p3, especificacao_03_visao_do_produto_p4, especificacao_03_visao_do_produto_p5 [EXTRACTED 1.00]
- **Cadeia RF → estória → caso de uso da conclusão de tarefa com marcos e propagação (RF/US/UC-B3, B7 e B8)** — especificacao_06_requisitos_funcionais_area_b_rf_b3, especificacao_07_estorias_de_usuario_area_b_us_b3, especificacao_10_especificacoes_de_caso_de_uso_area_b_uc_b3, especificacao_06_requisitos_funcionais_area_b_rf_b7, especificacao_07_estorias_de_usuario_area_b_us_b7, especificacao_10_especificacoes_de_caso_de_uso_area_b_uc_b7, especificacao_06_requisitos_funcionais_area_b_rf_b8, especificacao_07_estorias_de_usuario_area_b_us_b8, especificacao_10_especificacoes_de_caso_de_uso_area_b_uc_b8 [INFERRED 0.85]
- **Cadeia RF → estória → caso de uso do replanejamento e do serviço sob demanda (RF-D7, US-D7, UC-D7)** — especificacao_06_requisitos_funcionais_area_d_rf_d7, especificacao_07_estorias_de_usuario_area_d_us_d7, especificacao_10_especificacoes_de_caso_de_uso_area_d_uc_d7 [INFERRED 0.85]
- **Governança de consistência documental** — context_precedencia_adr_pesquisa, docs_agents_domain_flag_adr_conflicts, entregas_ra1_criterios_de_aceite_k11_consistencia_context_adr, entregas_ra1_criterios_de_aceite_protocolo_execucao_verificacao [INFERRED 0.85]
- **Serviços sob demanda: pesquisa, ADR-0014 (D14), catálogo, opção D-1 e RF-D7** — pesquisa_topicos_servicos_sob_demanda, docs_adr_0014_servicos_sob_demanda, docs_adr_0014_servicos_sob_demanda_d14_servicos_sob_demanda, docs_adr_0014_servicos_sob_demanda_catalogo_de_servicos_sob_demanda, pesquisa_topicos_servicos_sob_demanda_opcao_a1_catalogo_no_modelo, pesquisa_topicos_servicos_sob_demanda_opcao_d1_incluir_tarefa_no_plano_em_andamento, especificacao_06_requisitos_funcionais_area_d_rf_d7 [INFERRED 0.85]
- **Cadeia de rastreabilidade RF, US, RNF, UC por area** — especificacao_06_requisitos_funcionais_00_item_item, especificacao_07_estorias_de_usuario_00_item_item, especificacao_08_requisitos_nao_funcionais_00_item_item, especificacao_09_diagrama_geral_de_casos_de_uso_item, especificacao_10_especificacoes_de_caso_de_uso_00_item_item [INFERRED 0.85]
- **Ciclo de vida da exceção e bloqueio da liberação (RF-D1, RF-D5, RF-D4)** — especificacao_06_requisitos_funcionais_area_d_rf_d1, especificacao_06_requisitos_funcionais_area_d_rf_d5, especificacao_06_requisitos_funcionais_area_d_rf_d4 [INFERRED 0.95]
- **Reatribuição de tarefa entre operadores da mesma equipe (RF-D2, RF-D8)** — especificacao_06_requisitos_funcionais_area_d_rf_d2, especificacao_06_requisitos_funcionais_area_d_rf_d8 [INFERRED 0.95]

## Communities (9 total, 0 thin omitted)

### Community 0 - "Fontes, pesquisa, serviços sob demanda e Visão do Produto"
Cohesion: 0.05
Nodes (113): ADR-0005 — Abastecimento com passageiros configurável, ADR-0014 — Serviços sob demanda: catálogo no modelo de tarefas, acionado pelo Coordenador de Turnaround, Catálogo de serviços sob demanda no modelo de tarefas (tarefas "sob demanda" com tipo de atividade, equipe e duração planejada; fora do plano até serem acionadas), Benefício-chave: aeronave pronta para liberação no TOBT, desvios tratados durante a operação, Categoria-segmento: software de gestão de turnaround / operações de solo, Diferencial-chave: grafo de tarefas com caminho crítico, bloqueio da liberação, registro pelo operador com QR Code, régua TOBT + 5 min, E2: turnaround dentro do planejado, medido pela régua TOBT planejado + 5 min, Item 3 Visao do Produto (+105 more)

### Community 1 - "CONTEXT, regras para IAs, plano, critérios e rastreabilidade"
Cohesion: 0.07
Nodes (76): Formato de arquivo de pesquisa (YAML + seção Ligações), AGENTS.md regra 8 — registrar a suposição sobre outra área em vez de inventar o requisito, AGENTS.md regra 9 — toda sigla com o nome em português na primeira ocorrência de cada item (inclusive A-CDM, ANAC, ISO/IEC), CONTEXT.md — Contexto do projeto, A-CDM — Tomada de decisão colaborativa em aeroportos, Administrador do Sistema, Aircraft Turnaround Orchestration System, IATA — Associação Internacional de Transporte Aéreo (+68 more)

### Community 2 - "Área B: operador, casos de uso, protótipos e RNFs"
Cohesion: 0.10
Nodes (74): Estados da tarefa, Operador de Solo/Rampa, EASA CAT.OP.MPA.195, ANAC RBAC 91.102(g), ADR-0006 — Códigos de atraso tabela ANAC, IATA AHM 730, IATA AHM 732, ANAC Portaria nº 55/2026 (+66 more)

### Community 3 - "Estados, liberação, chegada e saída (área D)"
Cohesion: 0.07
Nodes (64): AEGT — Fim real do atendimento em solo, ARDT — Horário real de prontidão (Aircraft Ready), ATC — Controle de tráfego aéreo (fora de escopo), Autoridade de Liberação, Estados do turnaround, Fora de escopo (voos, tripulação, financeiro, ATC), MTTT — Tempo mínimo de turnaround, TSAT — Horário-alvo de autorização de acionamento (+56 more)

### Community 4 - "Área D: casos de uso, replanejamento e TOBT"
Cohesion: 0.15
Nodes (41): Metas do item 1 (precisão, sincronização, desvios), Risco ao horário (gatilhos A-CDM), TOBT — Horário-alvo de prontidão, Heathrow pontualidade "verde" (>=79%), Correção do AIBT pelo Coordenador de Turnaround (motivo, valor anterior e novo, autor e horário; até "Fora de bloco"; dispara o recálculo da projeção), O atraso causado por serviço sob demanda conta na meta de 80% do objetivo 1 (ADR-0001 e ADR-0002 não mudam), Janela planejada, Metrica: 80% das atividades na janela e 80% dos turnarounds prontos ate o TOBT planejado (tolerancia 5 min) (+33 more)

### Community 5 - "Régua do TOBT, previsão e tolerâncias"
Cohesion: 0.12
Nodes (42): ADR-0001 — TOBT planejado + 5 min, ADR-0002 — Metas percentuais 80%, ADR-0003 — Atualizar previsão na antecipação, Aviso de antecipação >= 5 min, TOBT planejado (fixo, régua da meta), TOBT vigente (última previsão informada), ADR-0004 — Quatro atores e Autoridade de Liberação, ADR-0009 — Nome Coordenador de Turnaround (+34 more)

### Community 6 - "Área C, Motor de Eventos e objetivo 3"
Cohesion: 0.22
Nodes (38): Motor de Eventos, Alerta de risco ao horario planejado, Caminho critico, Objetivo 3: Antecipar desvios e assegurar liberacao segura, Projecao de conclusao, Area C: Projecao, caminho critico, painel e alertas, E1: desvios detectados durante a operação (projeção e caminho crítico recalculados, alerta ao Coordenador de Turnaround), Leitura do diagrama: subprocessos de evento (monitoramento, tratamento de alerta, atualização da previsão, checagem em TOBT − 15 min) (+30 more)

### Community 7 - "BPMN: Motor de Eventos, monitoramento e checagem"
Cohesion: 0.12
Nodes (34): Fluxo de trabalho 1.3: diagramas em Mermaid/PlantUML, exceto o BPMN do item 4 em BPMN 2.0 (.bpmn), Leitura do diagrama: eventos e mensagens (chegada, autorização do ATC, sinais de desembarque/abastecimento concluído, temporizador TOBT − 15 min), RF-C11 — Exibir o aviso de checagem em TOBT − 15 min com as tarefas obrigatórias não concluídas e as equipes responsáveis, RF-C14 — Registrar a checagem com as equipes de um aviso de TOBT − 15 aberto e encerrar o aviso, Diagrama BPMN TO BE do turnaround (04-bpmn-to-be.png), Evento de início (mensagem): Voo previsto para a posição, Evento de início (mensagem, não interruptivo): Registro de andamento recebido (início, pausa, conclusão, não aplicável, QR Code), Evento de início (temporizador, não interruptivo): TOBT − 15 min (+26 more)

### Community 8 - "BPMN: tarefas de solo e abastecimento"
Cohesion: 0.20
Nodes (23): Gateway exclusivo (abastecimento): Abastecimento com passageiros permitido? (Sim → abastecer; Não → aguardar "Desembarque concluído"), Gateway exclusivo (embarque): Abastecimento com passageiros permitido? (Sim → embarcar; Não → aguardar "Abastecimento concluído"), Gateway paralelo: abertura das tarefas em paralelo após o ACGT, Gateway paralelo: junção de embarque e carregamento de bagagem e carga, Gateway paralelo: junção final das tarefas de solo, Gateway paralelo: junção de limpeza e catering, Gateway paralelo: limpeza da cabine e catering após o desembarque, Operador de Solo/Rampa (lane do BPMN) (+15 more)

## Knowledge Gaps
- **9 isolated node(s):** `Amadeus (excluded candidate)`, `Cosmos (excluded candidate)`, `Heathrow pontualidade "verde" (>=79%)`, `Wayfinding (map issue + child tickets)`, `Item 11 Diagrama de Atividades` (+4 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 9 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Fontes da pesquisa` connect `Fontes, pesquisa, serviços sob demanda e Visão do Produto` to `CONTEXT, regras para IAs, plano, critérios e rastreabilidade`, `Área B: operador, casos de uso, protótipos e RNFs`, `Estados, liberação, chegada e saída (área D)`, `Área D: casos de uso, replanejamento e TOBT`, `Régua do TOBT, previsão e tolerâncias`, `Área C, Motor de Eventos e objetivo 3`, `BPMN: Motor de Eventos, monitoramento e checagem`?**
  _High betweenness centrality (0.166) - this node is a cross-community bridge._
- **Why does `CONTEXT.md — Contexto do projeto` connect `CONTEXT, regras para IAs, plano, critérios e rastreabilidade` to `Fontes, pesquisa, serviços sob demanda e Visão do Produto`, `Área B: operador, casos de uso, protótipos e RNFs`, `Estados, liberação, chegada e saída (área D)`, `Área D: casos de uso, replanejamento e TOBT`, `Régua do TOBT, previsão e tolerâncias`, `Área C, Motor de Eventos e objetivo 3`?**
  _High betweenness centrality (0.118) - this node is a cross-community bridge._
- **Why does `Serviços sob demanda no turnaround (limpeza com risco biológico, assistência extra, catering adicional)` connect `Fontes, pesquisa, serviços sob demanda e Visão do Produto` to `CONTEXT, regras para IAs, plano, critérios e rastreabilidade`, `Área B: operador, casos de uso, protótipos e RNFs`, `Área D: casos de uso, replanejamento e TOBT`, `Régua do TOBT, previsão e tolerâncias`, `Área C, Motor de Eventos e objetivo 3`?**
  _High betweenness centrality (0.099) - this node is a cross-community bridge._
- **Are the 25 inferred relationships involving `Operador de Solo/Rampa` (e.g. with `UC-D2 — Reatribuir tarefa` and `UC-D7 — Replanejar tarefas ainda não iniciadas`) actually correct?**
  _`Operador de Solo/Rampa` has 25 INFERRED edges - model-reasoned connections that need verification._
- **Are the 14 inferred relationships involving `Coordenador de Turnaround` (e.g. with `Cliente-alvo: empresas de handling e companhias aéreas (responsáveis pelo TOBT)` and `E1: desvios detectados durante a operação (projeção e caminho crítico recalculados, alerta ao Coordenador de Turnaround)`) actually correct?**
  _`Coordenador de Turnaround` has 14 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Amadeus (excluded candidate)`, `Cosmos (excluded candidate)`, `Heathrow pontualidade "verde" (>=79%)` to the rest of the system?**
  _9 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Fontes, pesquisa, serviços sob demanda e Visão do Produto` be split into smaller, more focused modules?**
  _Cohesion score 0.05030274802049371 - nodes in this community are weakly interconnected._