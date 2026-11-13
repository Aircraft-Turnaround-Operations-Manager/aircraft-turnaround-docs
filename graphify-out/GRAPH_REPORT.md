# Graph Report - wt-blueprint  (2026-11-13)

## Corpus Check
- 51 files · ~709,100 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 1068 nodes · 2952 edges · 46 communities (42 shown, 4 thin omitted)
- Extraction: 82% EXTRACTED · 18% INFERRED · 0% AMBIGUOUS · INFERRED: 530 edges (avg confidence: 0.87)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Numeração provisória, TOBT e scripts
- Pesquisa, serviços sob demanda e regras de escrita
- Execução em solo: operador, QR Code e AIBT
- Autoridade de Liberação, prontidão e exceções
- Gerador do documento final (gerar_docx.py)
- Régua TOBT + 5 e metas de 80%
- BPMN TO BE (item 4) e diagramas
- RFs da área A e prioridade em sprints
- A-CDM e ADRs de base
- Matriz de rastreabilidade e item 12
- ADR-0015: divisão em microsserviços
- Atores e dados do operador (D4, D7)
- Motor de Eventos e alertas
- Códigos de atraso e mapa da pesquisa
- MTTT, antecipação e TOBT vigente
- Releases e CHANGELOG
- Serviço Exceções e Liberação (ADR-0020)
- RFs de exceção e liberação
- AGENTS.md e checagem cruzada
- Previsibilidade e objetivos do item 1
- Serviço Execução em Solo (ADR-0018)
- Siglas do A-CDM e risco ao horário
- ADR-0012: matriz de rastreabilidade
- Marcos do CONTEXT.md
- Projeção e caminho crítico
- Casos de teste e ADR-0022
- RA2: itens 12 e 13 e decisões B1 a B8
- ADR-0016: contrato entre os serviços
- Issues e pendências cruzadas
- Administrador e ator Usuário
- Painel e checagem em TOBT − 15
- Diagrama de casos de uso: Monitoramento
- Siglas e vocabulário (D8)
- Critérios de aceite do RA1
- Casos de uso: acesso e planejamento
- README e fluxo de branches
- Casos de uso: exceções e liberação
- Códigos de atraso da ANAC (D6)
- Consolidação em PDF (T13)
- Abastecimento com passageiros (D5)
- Indicadores de aderência
- Blueprint: aviso que encerra o alerta (RF-38)
- RA2: ajustes do RA1 (T00, T01)
- Site único em Angular

## God Nodes (most connected - your core abstractions)
1. `Coordenador de Turnaround` - 95 edges
2. `Fontes da pesquisa` - 79 edges
3. `Serviços sob demanda no turnaround (limpeza com risco biológico, assistência extra, catering adicional)` - 57 edges
4. `Operador de Solo/Rampa` - 51 edges
5. `Item 4 Mapeamento de Negócios (BPMN TO BE em vistas)` - 48 edges
6. `ADR-0015 Divisão em microsserviços` - 41 edges
7. `ADR-0007 — Dados do operador e QR Code` - 36 edges
8. `Subprocesso: Executar as tarefas em solo (início "Atendimento iniciado", fim "Tarefas em solo concluídas")` - 36 edges
9. `ADR-0001 — TOBT planejado + 5 min` - 34 edges
10. `Motor de Eventos` - 34 edges

## Surprising Connections (you probably didn't know these)
- `Protótipo UC-C5 — lista de alertas abertos (tela de computador)` --conceptually_related_to--> `Coordenador de Turnaround`  [INFERRED]
  especificacao/10-especificacoes-de-caso-de-uso/prototipos/uc-c5-lista-de-alertas.png → pesquisa/topicos/papeis-e-atores.md
- `Protótipo UC-D1 — abrir exceção (tela de computador)` --conceptually_related_to--> `Coordenador de Turnaround`  [INFERRED]
  especificacao/10-especificacoes-de-caso-de-uso/prototipos/uc-d1-abrir-excecao.png → pesquisa/topicos/papeis-e-atores.md
- `Protótipo UC-D2 — reatribuir tarefa (tela de computador)` --conceptually_related_to--> `Coordenador de Turnaround`  [INFERRED]
  especificacao/10-especificacoes-de-caso-de-uso/prototipos/uc-d2-reatribuir-tarefa.png → pesquisa/topicos/papeis-e-atores.md
- `Protótipo UC-D5 — encerrar exceção (tela de computador)` --conceptually_related_to--> `Coordenador de Turnaround`  [INFERRED]
  especificacao/10-especificacoes-de-caso-de-uso/prototipos/uc-d5-encerrar-excecao.png → pesquisa/topicos/papeis-e-atores.md
- `Coordenador de Turnaround` --conceptually_related_to--> `Protótipo UC-A8 — definir dependências entre tarefas (tela de computador)`  [INFERRED]
  pesquisa/topicos/papeis-e-atores.md → especificacao/10-especificacoes-de-caso-de-uso/prototipos/uc-a8-definir-dependencias.png

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Requisitos não funcionais da área A (RNF-1 a RNF-6)** — especificacao_08_requisitos_nao_funcionais_area_a_rnf_a1, especificacao_08_requisitos_nao_funcionais_area_a_rnf_a2, especificacao_08_requisitos_nao_funcionais_area_a_rnf_a3, especificacao_08_requisitos_nao_funcionais_area_a_rnf_a4, especificacao_08_requisitos_nao_funcionais_area_a_rnf_a5, especificacao_08_requisitos_nao_funcionais_area_a_rnf_a6 [EXTRACTED 1.00]
- **Requisitos não funcionais da área B (RNF-7 a RNF-10)** — especificacao_08_requisitos_nao_funcionais_area_b_rnf_b1, especificacao_08_requisitos_nao_funcionais_area_b_rnf_b2, especificacao_08_requisitos_nao_funcionais_area_b_rnf_b3, especificacao_08_requisitos_nao_funcionais_area_b_rnf_b4 [EXTRACTED 1.00]
- **Requisitos não funcionais da área C (RNF-11 a RNF-18)** — especificacao_08_requisitos_nao_funcionais_area_c_rnf_c1, especificacao_08_requisitos_nao_funcionais_area_c_rnf_c2, especificacao_08_requisitos_nao_funcionais_area_c_rnf_c3, especificacao_08_requisitos_nao_funcionais_area_c_rnf_c4, especificacao_08_requisitos_nao_funcionais_area_c_rnf_c5, especificacao_08_requisitos_nao_funcionais_area_c_rnf_c6, especificacao_08_requisitos_nao_funcionais_area_c_rnf_c7, especificacao_08_requisitos_nao_funcionais_area_c_rnf_c8 [EXTRACTED 1.00]
- **Requisitos não funcionais da área D (RNF-19 a RNF-24)** — especificacao_08_requisitos_nao_funcionais_area_d_rnf_d1, especificacao_08_requisitos_nao_funcionais_area_d_rnf_d2, especificacao_08_requisitos_nao_funcionais_area_d_rnf_d3, especificacao_08_requisitos_nao_funcionais_area_d_rnf_d4, especificacao_08_requisitos_nao_funcionais_area_d_rnf_d5, especificacao_08_requisitos_nao_funcionais_area_d_rnf_d6 [EXTRACTED 1.00]
- **Cinco atores da Relação de Atores / Usuários (item 5)** — especificacao_05_atores_usuarios_operador_de_solo_rampa, especificacao_05_atores_usuarios_coordenador_de_turnaround, especificacao_05_atores_usuarios_autoridade_de_liberacao, especificacao_05_atores_usuarios_administrador_do_sistema, especificacao_05_atores_usuarios_motor_de_eventos [EXTRACTED 1.00]
- **Atores do turnaround (Operador de Solo/Rampa, Coordenador de Turnaround, Autoridade de Liberação)** — ator_operador_de_solo_rampa, pesquisa_topicos_papeis_e_atores_coordenador_de_turnaround, pesquisa_topicos_papeis_e_atores_autoridade_de_liberacao [EXTRACTED 1.00]
- **Ferramentas do BPMN: package.json, exportar_bpmn.mjs e verificar_bpmn.py** — scripts_package_json, scripts_exportar_bpmn, scripts_verificar_bpmn [EXTRACTED 1.00]
- **Lanes do pool do turnaround (BPMN TO BE)** — especificacao_diagramas_04_bpmn_to_be_lane_coordenador_de_turnaround, especificacao_diagramas_04_bpmn_to_be_lane_operador_de_solo_rampa, especificacao_diagramas_04_bpmn_to_be_lane_motor_de_eventos, especificacao_diagramas_04_bpmn_to_be_lane_autoridade_de_liberacao [EXTRACTED 1.00]
- **Quatro subprocessos de evento do BPMN TO BE** — especificacao_diagramas_04_bpmn_to_be_subprocesso_monitoramento_a_cada_registro, especificacao_diagramas_04_bpmn_to_be_subprocesso_tratamento_de_alerta_de_risco, especificacao_diagramas_04_bpmn_to_be_subprocesso_atualizacao_da_previsao, especificacao_diagramas_04_bpmn_to_be_subprocesso_checagem_em_tobt_menos_15_min [EXTRACTED 1.00]
- **Ramos em paralelo do subprocesso "Executar as tarefas em solo" (após o ACGT)** — especificacao_diagramas_04_bpmn_to_be_tarefa_desembarcar_os_passageiros, especificacao_diagramas_04_bpmn_to_be_tarefa_descarregar_bagagem_e_carga, especificacao_diagramas_04_bpmn_to_be_tarefa_abastecer_a_aeronave, especificacao_diagramas_04_bpmn_to_be_tarefa_atender_agua_potavel_e_lavatorios, especificacao_diagramas_04_bpmn_to_be_tarefa_inspecao_tecnica_de_transito, especificacao_diagramas_04_bpmn_to_be_subprocesso_executar_as_tarefas_em_solo [EXTRACTED 1.00]
- **Vistas do mesmo modelo BPMN TO BE (processo principal, visão geral e vistas por subprocesso)** — especificacao_diagramas_04_bpmn_to_be, especificacao_diagramas_04_bpmn_to_be_geral, especificacao_diagramas_04_bpmn_to_be_tarefas_em_solo, especificacao_diagramas_04_bpmn_to_be_monitoramento, especificacao_diagramas_04_bpmn_to_be_alerta, especificacao_diagramas_04_bpmn_to_be_previsao, especificacao_diagramas_04_bpmn_to_be_tobt_15 [EXTRACTED 1.00]
- **Cadeia de modelagem do RA2 (T00 -> T12 -> T13 -> T14)** — entregas_ra2_tarefas_t00_titulo_aro_e_troca_de_area, entregas_ra2_tarefas_t12_modelo_de_dados, entregas_ra2_tarefas_t13_diagrama_de_classes, entregas_ra2_tarefas_t14_diagramas_de_sequencia, entregas_ra2_tarefas_cadeia_mais_longa [EXTRACTED 1.00]
- **Declaração de uso de IA: ferramentas, responsabilidade dos autores, repositório público e processo de revisão humana** — especificacao_00_declaracao_de_uso_de_ia, especificacao_00_declaracao_de_uso_de_ia_frase_obrigatoria, especificacao_00_declaracao_de_uso_de_ia_ferramentas_usadas, especificacao_00_declaracao_de_uso_de_ia_ia_como_ferramenta_nao_autora, especificacao_00_declaracao_de_uso_de_ia_repositorio_publico_github, especificacao_00_declaracao_de_uso_de_ia_processo_pr_e_revisao_humana, especificacao_00_declaracao_de_uso_de_ia_contagens [EXTRACTED 1.00]
- **Conjunto Execução em solo do item 9 (inclui UC12 da área A e UC37 da área D)** — especificacao_09_diagrama_geral_de_casos_de_uso_agrupamento_por_funcao [EXTRACTED 1.00]
- **Quatro vistas do diagrama de atividades (11.1–11.4)** — especificacao_diagramas_11_atividades, especificacao_diagramas_11_atividades_paralelas, especificacao_diagramas_11_registro_tarefa, especificacao_diagramas_11_monitoramento [EXTRACTED 1.00]
- **Five market similars compared in matrix 3.3** — pesquisa_similares_assaia_assaia_apronai_turnaroundcontrol, pesquisa_similares_inform_groundstar_inform_groundstar, pesquisa_similares_adb_safegate_adb_safegate_safedock_apron_manager, pesquisa_similares_veovo_veovo_acdm, pesquisa_similares_sita_sita_airport_management_cdm, pesquisa_similares_matriz_comparativa_capacidades_do_nucleo [EXTRACTED 1.00]
- **Project differentiators DF1-DF5** — pesquisa_similares_lacunas_e_diferencial_df1, pesquisa_similares_lacunas_e_diferencial_df2, pesquisa_similares_lacunas_e_diferencial_df3, pesquisa_similares_lacunas_e_diferencial_df4, pesquisa_similares_lacunas_e_diferencial_df5 [EXTRACTED 1.00]
- **Quatro atores operacionais do Aircraft Turnaround Orchestration System** — ator_operador_de_solo_rampa, pesquisa_topicos_papeis_e_atores_coordenador_de_turnaround, context_autoridade_de_liberacao, context_motor_de_eventos [EXTRACTED 1.00]
- **'Risco ao horario' trigger set (T8, T11, T12)** — pesquisa_impacto_impacto_por_item_risco_ao_horario, pesquisa_topicos_tolerancias_e_indicadores_tobt_mais_5_min, pesquisa_topicos_tolerancias_e_indicadores_t11_viabilidade_eibt_mttt, pesquisa_topicos_tolerancias_e_indicadores_t12_embarque_nao_iniciado [EXTRACTED 1.00]
- **Campos da Visão de Produto (cliente-alvo, categoria-segmento, benefício-chave, diferencial-chave, meta-valor)** — especificacao_03_visao_do_produto_cliente_alvo, especificacao_03_visao_do_produto_categoria_segmento, especificacao_03_visao_do_produto_beneficio_chave, especificacao_03_visao_do_produto_diferencial_chave, especificacao_03_visao_do_produto_meta_valor [EXTRACTED 1.00]
- **Problemas P1–P5 da Visão do Produto** — especificacao_03_visao_do_produto_p1, especificacao_03_visao_do_produto_p2, especificacao_03_visao_do_produto_p3, especificacao_03_visao_do_produto_p4, especificacao_03_visao_do_produto_p5 [EXTRACTED 1.00]
- **Relatórios de verificação do RA1 (item 10, T11, T12) e mapa de renumeração** — entregas_ra1_item_10_verificacao, entregas_ra1_t11_verificacao, entregas_ra1_t12_verificacao, entregas_ra1_renumeracao [INFERRED 0.85]
- **Serviços sob demanda: pesquisa, ADR-0014 (D14), catálogo, opção D-1 e RF-D7** — pesquisa_topicos_servicos_sob_demanda, docs_adr_0014_servicos_sob_demanda, docs_adr_0014_servicos_sob_demanda_d14_servicos_sob_demanda, docs_adr_0014_servicos_sob_demanda_catalogo_de_servicos_sob_demanda, pesquisa_topicos_servicos_sob_demanda_opcao_a1_catalogo_no_modelo, pesquisa_topicos_servicos_sob_demanda_opcao_d1_incluir_tarefa_no_plano_em_andamento [INFERRED 0.85]
- **Registros de tarefa incluem propagação de estado** — especificacao_diagramas_09_casos_de_uso_uc12, especificacao_diagramas_09_casos_de_uso_uc15, especificacao_diagramas_09_casos_de_uso_uc16, especificacao_diagramas_09_casos_de_uso_uc18, especificacao_diagramas_09_casos_de_uso_uc21 [EXTRACTED 1.00]
- **Extensões de Registrar ação para o alerta** — especificacao_diagramas_09_casos_de_uso_uc29, especificacao_diagramas_09_casos_de_uso_uc30, especificacao_diagramas_09_casos_de_uso_uc34, especificacao_diagramas_09_casos_de_uso_uc35, especificacao_diagramas_09_casos_de_uso_uc31 [EXTRACTED 1.00]
- **Motor de Eventos recalcula e alerta** — context_motor_de_eventos, especificacao_diagramas_09_casos_de_uso_uc24, especificacao_diagramas_09_casos_de_uso_uc25 [INFERRED 0.85]
- **Fluxo de confirmação de prontidão (ARDT)** — especificacao_diagramas_14_sequencia_uc32_liberacaoservice, especificacao_diagramas_14_sequencia_uc32_excecaorepository, especificacao_diagramas_14_sequencia_uc32_turnaroundcontroller, especificacao_diagramas_14_sequencia_uc32_liberacaorepository [EXTRACTED 1.00]
- **Quatro microsserviços da ADR-0015** — docs_adr_0015_divisao_em_microsservicos_cadastro_e_planejamento, docs_adr_0015_divisao_em_microsservicos_execucao_em_solo, docs_adr_0015_divisao_em_microsservicos_monitoramento, docs_adr_0015_divisao_em_microsservicos_excecoes_e_liberacao [EXTRACTED 1.00]
- **Cinco conflitos da primeira divisão** — pesquisa_topicos_service_blueprint_conflito_chegada, pesquisa_topicos_service_blueprint_conflito_reatribuir_replanejar, pesquisa_topicos_service_blueprint_conflito_excecao, pesquisa_topicos_service_blueprint_conflito_liberacao, pesquisa_topicos_service_blueprint_conflito_saida [EXTRACTED 1.00]
- **Matriz de rastreabilidade e numeração provisória** — docs_adr_0011_minimo_por_integrante_e_numeracao_provisoria, docs_adr_0012_matriz_de_rastreabilidade, docs_adr_0021_matriz_de_rastreabilidade_estendida, docs_adr_0022_ids_provisorios_dos_casos_de_teste [INFERRED 0.85]
- **Ciclo de vida da tarefa (início, pausa, conclusão, N/A, QR, propagação)** — especificacao_06_requisitos_funcionais_area_b_rf_15, especificacao_06_requisitos_funcionais_area_b_rf_16, especificacao_06_requisitos_funcionais_area_b_rf_17, especificacao_06_requisitos_funcionais_area_b_rf_18, especificacao_06_requisitos_funcionais_area_b_rf_19, especificacao_06_requisitos_funcionais_area_b_rf_21 [EXTRACTED 1.00]
- **Alertas de risco ao horário e seu tratamento** — especificacao_06_requisitos_funcionais_area_c_rf_27, especificacao_06_requisitos_funcionais_area_c_rf_28, especificacao_06_requisitos_funcionais_area_c_rf_29, especificacao_06_requisitos_funcionais_area_c_rf_30, especificacao_06_requisitos_funcionais_area_c_rf_31, especificacao_06_requisitos_funcionais_area_c_rf_33, especificacao_06_requisitos_funcionais_area_d_rf_38 [EXTRACTED 1.00]
- **Planejamento do turnaround (modelo, plano, dependências, abastecimento, replanejamento)** — especificacao_06_requisitos_funcionais_area_a_rf_4, especificacao_06_requisitos_funcionais_area_a_rf_5, especificacao_06_requisitos_funcionais_area_a_rf_6, especificacao_06_requisitos_funcionais_area_a_rf_7, especificacao_06_requisitos_funcionais_area_a_rf_8, especificacao_06_requisitos_funcionais_area_a_rf_11, especificacao_06_requisitos_funcionais_area_d_rf_42 [EXTRACTED 1.00]
- **Ciclo de vida da tarefa do operador** — especificacao_07_estorias_de_usuario_area_b_us015, especificacao_07_estorias_de_usuario_area_b_us016, especificacao_07_estorias_de_usuario_area_b_us017, especificacao_07_estorias_de_usuario_area_b_us018, especificacao_07_estorias_de_usuario_area_b_us019 [INFERRED 0.85]
- **Alertas de risco ao horário (A-CDM)** — especificacao_07_estorias_de_usuario_area_c_us028, especificacao_07_estorias_de_usuario_area_c_us029, especificacao_07_estorias_de_usuario_area_c_us030, especificacao_07_estorias_de_usuario_area_c_us031 [INFERRED 0.85]
- **Exceção e liberação do turnaround** — especificacao_07_estorias_de_usuario_area_d_us036, especificacao_07_estorias_de_usuario_area_d_us039, especificacao_07_estorias_de_usuario_area_d_us040 [INFERRED 0.85]
- **Registro de tarefa incluindo marcos e propagação** — especificacao_10_especificacoes_de_caso_de_uso_area_b_uc15, especificacao_10_especificacoes_de_caso_de_uso_area_b_uc16, especificacao_10_especificacoes_de_caso_de_uso_area_b_uc18, especificacao_10_especificacoes_de_caso_de_uso_area_b_uc20, especificacao_10_especificacoes_de_caso_de_uso_area_b_uc21 [EXTRACTED 1.00]
- **Ações que encerram um alerta (UC31)** — especificacao_10_especificacoes_de_caso_de_uso_area_d_uc31, especificacao_10_especificacoes_de_caso_de_uso_area_d_uc29, especificacao_10_especificacoes_de_caso_de_uso_area_d_uc30, especificacao_10_especificacoes_de_caso_de_uso_area_d_uc34, especificacao_10_especificacoes_de_caso_de_uso_area_d_uc35 [EXTRACTED 1.00]
- **Gatilhos de alerta de risco ao horário** — especificacao_10_especificacoes_de_caso_de_uso_area_c_tarefa_pronta_nao_iniciada, especificacao_10_especificacoes_de_caso_de_uso_area_c_projecao_alem_de_tobt_mais_5, especificacao_10_especificacoes_de_caso_de_uso_area_c_viabilidade, especificacao_10_especificacoes_de_caso_de_uso_area_c_embarque_nao_iniciado, especificacao_10_especificacoes_de_caso_de_uso_area_c_prontidao_nao_registrada [EXTRACTED 1.00]
- **Matrix columns blocked by unwritten items 12, 14, 15** — especificacao_apendice_a_matriz_de_rastreabilidade_a1, especificacao_apendice_a_matriz_de_rastreabilidade_a4, especificacao_apendice_a_matriz_de_rastreabilidade_a5, especificacao_apendice_a_matriz_de_rastreabilidade_a6, especificacao_12_modelo_de_dados [INFERRED 0.85]
- **Item 12 data model deliverables (model, dictionary, matrix column)** — especificacao_12_modelo_de_dados, especificacao_apendice_b_dicionario_de_dados, especificacao_apendice_a_matriz_de_rastreabilidade_a1 [EXTRACTED 1.00]
- **Fluxo de planejamento testado: modelo → aplicar → dependências → plano** — especificacao_15_casos_de_teste_area_a_uc04, especificacao_15_casos_de_teste_area_a_uc06, especificacao_15_casos_de_teste_area_a_uc08, especificacao_15_casos_de_teste_area_a_uc05 [INFERRED 0.85]

## Communities (46 total, 4 thin omitted)

### Community 0 - "Numeração provisória, TOBT e scripts"
Cohesion: 0.05
Nodes (69): TOBT — horário-alvo de prontidão, Verificação do item 10 — issue #11 (C10.1–C10.10, X.8, X.9, K.1–K.12), Item 10: 37 especificações (A13, B8, C7, D9), 42 protótipos, 119 fluxos alternativos e 122 de exceção, Item 10 × diagrama do item 9: 37 nomes, 39 associações de atores, 10 include e 8 extend, Matriz regenerada: 44 RFs, 24 RNFs, 44 estórias, 37 casos de uso, 0 lacunas, Renumeração definitiva — ADR-0011 (tabela de IDs provisórios × finais), Mapa de renumeração: 44 RF → RF-1…RF-44, 44 US → US001…US044, 24 RNF → RNF-1…RNF-24, 37 UC → UC01…UC37, na ordem A, B, C, D, C11.1–C11.7 atendidos (fluxo principal, alternativos, guardas, fork/join, partições, notação, legibilidade) (+61 more)

### Community 1 - "Pesquisa, serviços sob demanda e regras de escrita"
Cohesion: 0.05
Nodes (86): Regras para quem escreve, Categoria-segmento: software de gestão de turnaround / operações de solo, Diferencial-chave: grafo de tarefas com caminho crítico, bloqueio da liberação, registro pelo operador com QR Code, régua TOBT + 5 min, E4: andamento registrado pelo Operador de Solo/Rampa no celular, inclusive QR Code, sem infraestrutura no pátio, P2: TOBT pouco confiável (menos de 60% de acerto em 5 min), P3: atividades paralelas sem visão compartilhada; coordenação por rádio falha, P4: monitoramento automático exige câmeras/sensores e não registra quem executou, Fontes da pesquisa (+78 more)

### Community 2 - "Execução em solo: operador, QR Code e AIBT"
Cohesion: 0.05
Nodes (61): Operador de Solo/Rampa, Diferencial DF5 (QR Code por assento/fileira/zona), Leitura de QR Code pelo celular, Recusas do registro do AIBT (operador sem tarefa atribuída, horário futuro, chegada já registrada, plano inicial não confirmado), Padrão Ação-Resultado-Objeto (ARO) dos títulos, 06 Requisitos funcionais – area-b, Estórias de usuário – área B, US012 – Registrar chegada da aeronave à posição (+53 more)

### Community 3 - "Autoridade de Liberação, prontidão e exceções"
Cohesion: 0.08
Nodes (65): AEGT — fim real do atendimento em solo, ARDT — horário real de prontidão, Autoridade de Liberação, Diagrama de atividades: 17 decisões binárias, 1 seleção com 4 guardas, 2 laços, 4 partições, 4 nós iniciais e 7 finais, Correções da revisão independente: eventos condicionais no BPMN, propagação após replanejamento, loadsheet após embarque e bagagem, norma ISO/IEC no item 8, Protótipo UC-D4 — confirmar a prontidão (tela de computador), Protótipo UC32 — confirmar a prontidão, versão 2 (tela de computador), Protótipo UC-D9 — registrar a saída da posição (celular) (+57 more)

### Community 4 - "Gerador do documento final (gerar_docx.py)"
Cohesion: 0.05
Nodes (20): exportar_drawio.py — exporta um .drawio para PNG e SVG com o draw.io desktop, com texto SVG real e só as cores do tema claro, drawio_exe() — localiza o draw.io desktop (variável DRAWIO, PATH ou caminhos padrão), main() — exporta PNG (escala 2) e SVG com borda 20, remove light-dark() do SVG (fica a cor do tema claro) e conta foreignObject, textos e cores light-dark, texto_simples() — copia o diagrama trocando rótulos HTML por texto simples, comando(), main(), blocos(), carregar() (+12 more)

### Community 5 - "Régua TOBT + 5 e metas de 80%"
Cohesion: 0.07
Nodes (56): Heathrow pontualidade "verde" (>=79%), O atraso causado por serviço sob demanda conta na meta de 80% do objetivo 1 (ADR-0001 e ADR-0002 não mudam), Alerta de risco ao horario planejado, Caminho critico, Janela planejada, Liberacao da aeronave, Metrica: 80% das atividades na janela e 80% dos turnarounds prontos ate o TOBT planejado (tolerancia 5 min), Metrica: alertas em 5 s, 90% acoes em 2 min, 0 liberacoes com pendencia (+48 more)

### Community 6 - "BPMN TO BE (item 4) e diagramas"
Cohesion: 0.08
Nodes (62): Leitura do diagrama: eventos e mensagens (chegada, autorização do ATC, marcos e eventos condicionais de desembarque/abastecimento concluído, temporizador TOBT − 15 min), Fontes editáveis do BPMN: 04-bpmn-to-be.bpmn (processo principal + vistas por subprocesso) e 04-bpmn-to-be-geral.bpmn (visão geral), Leitura do diagrama: pool e lanes (Coordenador de Turnaround, Motor de Eventos, Operador de Solo/Rampa, Autoridade de Liberação; ATC como pool externo fechado), Vistas do mesmo modelo BPMN: visão geral com tudo aberto + processo principal e uma vista por subprocesso (prioridade de leitura na tela), Protótipo UC-C6 — checagem em TOBT − 15 (tela de computador), Diagrama BPMN TO BE do turnaround — processo principal (04-bpmn-to-be.png), Diagrama BPMN TO BE — vista do subprocesso de evento Tratamento de alerta de risco (04-bpmn-to-be-alerta.png), Evento de fim: Turnaround encerrado (+54 more)

### Community 7 - "RFs da área A e prioridade em sprints"
Cohesion: 0.07
Nodes (47): 6 Relação de requisitos funcionais, Dados simulados no formato do contrato entre serviços, 06 Requisitos funcionais – area-a, Estórias de usuário – área A, US001 – Autenticar acesso do usuário, US002 – Gerenciar cadastro de usuários e perfis, US003 – Abrir turnaround da aeronave, US004 – Criar modelo de tarefas (+39 more)

### Community 8 - "A-CDM e ADRs de base"
Cohesion: 0.16
Nodes (31): A-CDM — Tomada de decisão colaborativa em aeroportos, ADR-0005 — Abastecimento com passageiros configurável, ADR-0014 — Serviços sob demanda: catálogo no modelo de tarefas, acionado pelo Coordenador de Turnaround, T11 — Verificação do diagrama de atividades (#12), com anexo técnico das vistas, Item 11 de entrega só com título, subtítulos e imagens; explicações em anexo técnico interno, Leitura do diagrama: caminho principal (abertura, viabilidade, AIBT, posicionar ponte ou escada e iniciar o atendimento, subprocesso "Executar as tarefas em solo", fechamento de portas, verificação de pendências, ARDT, AOBT), Leitura do diagrama: gateways com condição (viável?; abastecimento com passageiros permitido?; pendência ou exceção?; há desvio?), Item 4 Mapeamento de Negócios (BPMN TO BE em vistas) (+23 more)

### Community 9 - "Matriz de rastreabilidade e item 12"
Cohesion: 0.11
Nodes (31): 06 Requisitos funcionais – area-c, 06 Requisitos funcionais – area-d, Item 12 - Modelo de Dados, A.1 RF x titulos, objetivos, atores, estorias, UCs, RNFs e tabelas, A.6 Lacunas encontradas, Lacuna US012: 6 CAs sem caso de teste, Lacuna US013: 6 CAs sem caso de teste, Lacuna US022: 5 CAs sem caso de teste (+23 more)

### Community 10 - "ADR-0015: divisão em microsserviços"
Cohesion: 0.11
Nodes (20): Metas do item 1 (80%, 5 s, 90% em 2 min, 0 liberações), ADR-0015 Divisão em microsserviços, Serviço Monitoramento (RF-22 a RF-35), Sem chave estrangeira entre serviços, Painéis: WebSocket para mudanças e GraphQL para consulta, 14 Diagramas de Sequência, Diagramas de Sequência – Área A (UC01–UC11, stub), Diagramas de Sequência – Área B (UC12–UC21, UC37, stub) (+12 more)

### Community 11 - "Atores e dados do operador (D4, D7)"
Cohesion: 0.19
Nodes (16): ADR-0004 — Quatro atores e Autoridade de Liberação, ADR-0007 — Dados do operador e QR Code, ADR-0009 — Nome Coordenador de Turnaround, ADR-0010 — Administrador do Sistema, ator abstrato Usuário e equipe do operador como dado, ADR-0011 Mínimo por integrante e numeração provisória, RF extra coberto por UC existente via include/extend, ADR-0013 — Chegada à posição registrada direto pelo operador, sem confirmação, Índice das ADRs (+8 more)

### Community 12 - "Motor de Eventos e alertas"
Cohesion: 0.18
Nodes (8): Motor de Eventos, US028 – Emitir alerta de projeção além de TOBT + 5, US029 – Verificar viabilidade do turnaround, US030 – Emitir alerta de embarque não iniciado, US031 – Emitir alerta de prontidão não registrada, UC25 – Emitir alertas de risco ao horário, UC26 – Consultar lista de alertas abertos, UC31 – Registrar ação tomada para o alerta

### Community 13 - "Códigos de atraso e mapa da pesquisa"
Cohesion: 0.15
Nodes (20): ADR-0006 — Códigos de atraso tabela ANAC, EUROCONTROL CODA Digest 2023 [16], E / Nao e / Faz / Nao faz candidates, Insumos para os RFs, por area (4.3), Mapa da pesquisa, Como usar o mapa da pesquisa, Convenções [Fato]/[Inferência]/declarado pelo fornecedor, Diagrama arquivos × decisões (+12 more)

### Community 14 - "MTTT, antecipação e TOBT vigente"
Cohesion: 0.17
Nodes (18): MTTT — tempo mínimo de turnaround, Aviso de antecipação >= 5 min, TOBT planejado (fixo, régua da meta), TOBT vigente (última previsão informada), Correção do AIBT pelo Coordenador de Turnaround (motivo, valor anterior e novo, autor e horário; até "Fora de bloco"; dispara o recálculo da projeção), Catálogo de serviços sob demanda no modelo de tarefas (tarefas "sob demanda" com tipo de atividade, equipe e duração planejada; fora do plano até serem acionadas), Protótipo UC-A10 — atualizar referências de previsão (tela de computador), Protótipo UC-A13 — corrigir chegada à posição (tela de computador) (+10 more)

### Community 15 - "Releases e CHANGELOG"
Cohesion: 0.13
Nodes (17): Release workflow (release.yml), Anexo do PDF entregas/raN-especificacao-de-projeto.pdf do commit da tag, Criar ou atualizar a release (gh release), Notas extraídas da seção ## [X.Y.Z] do CHANGELOG da main, Gatilho por tag vX.Y.Z e workflow_dispatch, Categorias Adicionado/Alterado/Removido/Corrigido, PlantUML para diagramas de sequência (decisão B3), Formato Keep a Changelog 1.1.0 (+9 more)

### Community 16 - "Serviço Exceções e Liberação (ADR-0020)"
Cohesion: 0.11
Nodes (16): Serviço Exceções e Liberação (RF-36 a RF-43), Tabela de avisos processados (idempotência), ADR-0020 Tecnologia de Exceções e Liberação, ASP.NET Core 10, Cobertura em página HTML (coverlet, ReportGenerator, v8), Códigos de atraso ANAC versionados (RNF-22), C# 14 com .NET 10 (LTS), Fila durável excecoes-e-liberacao (+8 more)

### Community 17 - "RFs de exceção e liberação"
Cohesion: 0.16
Nodes (14): Estórias de usuário – área D, US036 – Abrir exceção do turnaround com código de atraso, US038 – Registrar ação tomada para cada alerta, US039 – Confirmar prontidão e liberar aeronave, US040 – Encerrar exceção do turnaround, US041 – Atualizar o TOBT quando a projeção se afasta 5 minutos ou mais, US042 – Replanejar tarefas não iniciadas do turnaround, US043 – Consultar operadores disponíveis da equipe (+6 more)

### Community 18 - "AGENTS.md e checagem cruzada"
Cohesion: 0.13
Nodes (7): Checagem cruzada de diagramas contra RF e UC, Issue tracker: GitHub Issues via gh, Rótulos de triagem (needs-triage, ready-for-agent…), ACGT e AEGT gravados pelo Motor de Eventos (RF-20), Regras gerais Y.1 a Y.8, Quebra de tarefas do RA2, Grafo de conhecimento graphify-out/

### Community 19 - "Previsibilidade e objetivos do item 1"
Cohesion: 0.18
Nodes (17): Princípio: dentro do planejado, não encurtar, ADR-0001 — TOBT planejado + 5 min, ADR-0002 — Metas percentuais 80%, ADR-0003 — Atualizar previsão na antecipação, Quadro 3 Objetivos, UC34 – Atualizar TOBT, Insumos para os RNFs (4.4), Minute precision and rounding rule (5:59 vs 6:00) (+9 more)

### Community 20 - "Serviço Execução em Solo (ADR-0018)"
Cohesion: 0.12
Nodes (16): Camadas Controller → Service → Repository, Serviço Execução em Solo (RF-12 a RF-21, RF-44), ADR-0018 Tecnologia da Execução em Solo, Verificação de saúde /actuator/health (RNF-7, RNF-19), Envelope dos avisos (id, tipo, versao, ocorridoEm, turnaroundId, autorId, origem, causaId, dados), Fila durável execucao-em-solo, Flyway e JUnit 5 + Testcontainers, Java 25 (LTS) (+8 more)

### Community 21 - "Siglas do A-CDM e risco ao horário"
Cohesion: 0.25
Nodes (16): ADR-0008 — Siglas A-CDM com nome em português, Dublin Airport A-CDM Operational Procedures [8], 'Risco ao horario' defined by A-CDM triggers (T8, T11, T12), Observed capabilities by area A-D (RF inputs), O que e o A-CDM (P1.1), Marcos e horarios do A-CDM (P1.2), A-CDM time glossary (SIBT, EIBT, ACGT, ARDT, AOBT...), MTTT (Minimum Turn-round Time) (+8 more)

### Community 22 - "ADR-0012: matriz de rastreabilidade"
Cohesion: 0.19
Nodes (11): ADR-0012 de volta ao texto original, ADR-0012 Matriz de rastreabilidade, Apêndice A — Matriz de rastreabilidade, Lista de lacunas da matriz (vazia no K.13), Cada RNF cita os RFs a que se aplica, ADR-0021 Matriz de rastreabilidade estendida, Critério de aceite USnnn-CAn → casos de teste (A.5, C15.2), Lacunas A.6 (Nenhuma. na entrega, K.12) (+3 more)

### Community 23 - "Marcos do CONTEXT.md"
Cohesion: 0.19
Nodes (13): ACGT — início real do atendimento em solo, AOBT — horário real de saída da posição, ASBT — início real do embarque, ATC — Controle de tráfego aéreo, EIBT — horário estimado de chegada à posição, Estados da tarefa (Aguardando → Pronta → Em execução → Concluída; Pausada, Não aplicável), Estados do turnaround (Em solo → … → Fora de bloco; Em exceção), Fora de escopo: programação de voos, tripulação, financeiro, ATC real (+5 more)

### Community 24 - "Projeção e caminho crítico"
Cohesion: 0.22
Nodes (9): US022 – Recalcular projeção de prontidão, US023 – Calcular atraso e impacto das tarefas, US024 – Identificar caminho crítico do turnaround, US026 – Consultar linha do tempo do turnaround, Item 10 – Especificações de caso de uso, Especificações de caso de uso – área C (Monitoramento), UC22 – Acompanhar painel dos turnarounds, UC23 – Consultar linha do tempo do turnaround (+1 more)

### Community 25 - "Casos de teste e ADR-0022"
Cohesion: 0.17
Nodes (11): Item 15 área A: 106 casos de teste CT-A001 a CT-A106, Seção [Não publicado], ADR-0022 IDs provisórios dos casos de teste, Tabela de correspondência em entregas/ra2-renumeracao.md, 15 Casos de teste – 00-item, IDs provisórios CT-A001…CT-D001 e renumeração CT-001, Planilha de casos de teste (colunas C15.1), 15 Casos de teste – area-b (+3 more)

### Community 26 - "RA2: itens 12 e 13 e decisões B1 a B8"
Cohesion: 0.17
Nodes (12): Convenção de nomes em português (PascalCase, camelCase, snake_case), Decisões do RA2 B1 a B8, B6: dicionário de dados no Apêndice B, Item 12 - Modelo de dados (C12.1 a C12.10), Item 13 - Diagrama de classes (C13.1 a C13.10), Item 14 - Diagramas de sequência, 37 (C14.1 a C14.8), B5: matriz de rastreabilidade estendida aos itens 12 a 15, T02 Testar a ferramenta dos diagramas de sequência (+4 more)

### Community 27 - "ADR-0016: contrato entre os serviços"
Cohesion: 0.17
Nodes (12): AIBT — horário real de chegada à posição, Serviço Cadastro e Planejamento (RF-1 a RF-11), ADR-0016 Contrato comum entre os serviços (D16), Porta de entrada única (Spring Cloud Gateway), Envelope comum dos avisos (id, tipo, versao, causaId, dados), Horários ISO 8601 em UTC (Z), Login próprio no Cadastro (token emitido pelo Cadastro), RabbitMQ (filas duráveis, uma por serviço) (+4 more)

### Community 28 - "Issues e pendências cruzadas"
Cohesion: 0.22
Nodes (10): Issue tracker: GitHub, GitHub Issues via gh CLI, Wayfinding (map issue + child tickets), Triage Labels, Vocabulário de triage (needs-triage, needs-info, ready-for-agent, ready-for-human, wontfix), Quebra de Tarefas RA1, Fluxo de trabalho 1.3: cada diagrama com a fonte editável versionada junto da imagem; BPMN do item 4 em BPMN 2.0 (.bpmn), Fluxo de trabalho 1.3: casos de uso (item 9) e atividades (item 11) feitos no draw.io (.drawio) para controlar a posição de cada elemento; entregues em PlantUML no RA1 e refeitos depois da entrega (+2 more)

### Community 29 - "Administrador e ator Usuário"
Cohesion: 0.20
Nodes (10): Administrador do Sistema, Usuário, Usuário (ator abstrato), RNF-18 — Telas de computador do Coordenador de Turnaround, da Autoridade de Liberação e do Administrador do Sistema sem rolagem horizontal de 1366 a 1920 pixels no Chrome e no Edge; 10 turnarounds visíveis em 1920 × 1080 (Usabilidade: operabilidade), Protótipo UC-A2 — gerenciar usuários e perfis de acesso (tela de computador), Protótipo UC-A9 — gerenciar equipes e especialidades (tela de computador), Protótipo UC-D8 — operadores disponíveis da equipe (tela de computador), UC01 Autenticar acesso do usuário (+2 more)

### Community 30 - "Painel e checagem em TOBT − 15"
Cohesion: 0.22
Nodes (8): Estórias de usuário – área C, US025 – Acompanhar painel dos turnarounds, US027 – Emitir alerta de tarefa pronta não iniciada, US032 – Exibir aviso de checagem em TOBT − 15, US033 – Consultar lista de alertas abertos, US034 – Consultar indicadores de aderência, US035 – Registrar checagem com as equipes, UC27 – Registrar checagem com as equipes em TOBT − 15

### Community 31 - "Diagrama de casos de uso: Monitoramento"
Cohesion: 0.24
Nodes (10): Aircraft Turnaround Orchestration System, Diagrama de casos de uso (item 9), Monitoramento, UC22 Acompanhar painel dos turnarounds, UC23 Consultar linha do tempo do turnaround, UC24 Recalcular projeção, atraso e caminho crítico, UC25 Emitir alertas de risco ao horário, UC26 Consultar lista de alertas abertos (+2 more)

### Community 32 - "Siglas e vocabulário (D8)"
Cohesion: 0.22
Nodes (8): Domain Docs, Usar o vocabulário do glossário do CONTEXT.md, Cliente-alvo: empresas de handling e companhias aéreas (responsáveis pelo TOBT), EUROCONTROL A-CDM concept page [1], IATA A-CDM Recommendations (2018) [5], A-CDM (Airport Collaborative Decision Making), GRU first A-CDM airport in Brazil (2020), 16 A-CDM milestones

### Community 33 - "Critérios de aceite do RA1"
Cohesion: 0.22
Nodes (9): Checklist de consistência cruzada K.1 a K.13 (RA1), Critérios por item C01.1 a C11.7 e pesos da rubrica, Critérios de aceite do RA1 (itens 1 a 11), Regra dos 4 por integrante (mínimo 16), Regras gerais X.1 a X.10, Checklist de consistência cruzada K.1 a K.12 (RA2), Critérios de aceite do RA2 (itens 12 a 15), T16 Revisão cruzada e verificação independente (+1 more)

### Community 34 - "Casos de uso: acesso e planejamento"
Cohesion: 0.27
Nodes (10): Acesso e planejamento, UC03 Abrir turnaround da aeronave, UC04 Criar modelo de tarefas, UC05 Confirmar plano inicial do turnaround, UC06 Aplicar modelo de tarefas, UC07 Configurar pontos de confirmação das tarefas, UC08 Definir dependências entre tarefas, UC10 Atualizar referências de previsão do turnaround (+2 more)

### Community 35 - "README e fluxo de branches"
Cohesion: 0.20
Nodes (10): README do repositório, Atualizar grafo só a partir da main via PR, Branches ra1/<tarefa> e PR obrigatório, Definição de pronto de uma tarefa, Ferramentas de diagrama: BPMN 2.0, draw.io, PlantUML, Integrantes e áreas A–D, Itens por integrante editam só o area-x.md, Prazos RA1 10/10/2026 e RA2 28/11/2026 (+2 more)

### Community 36 - "Casos de uso: exceções e liberação"
Cohesion: 0.36
Nodes (9): Exceções e liberação, UC29 Abrir exceção do turnaround, UC30 Reatribuir tarefa, UC31 Registrar ação tomada para o alerta, UC32 Confirmar prontidão e liberar aeronave, UC33 Encerrar exceção do turnaround, UC34 Atualizar TOBT, UC35 Replanejar tarefas não iniciadas do turnaround (+1 more)

### Community 37 - "Códigos de atraso da ANAC (D6)"
Cohesion: 0.29
Nodes (7): IATA AHM 730, IATA AHM 732, ANAC Portaria nº 55/2026, Protótipo UC-B4 — formulário de pausa com código da ANAC (celular), Protótipo UC-B4 — tarefa pausada com a opção "Retomar" (celular), Protótipo UC-D1 — abrir exceção (tela de computador), Protótipo UC-D5 — encerrar exceção (tela de computador)

### Community 38 - "Consolidação em PDF (T13)"
Cohesion: 0.32
Nodes (5): T13 — Consolidar em PDF e enviar no Canvas, Declaração de uso de inteligência artificial (abertura da especificação), Contagens até 10/10/2026: 73 pull requests, 36 tarefas, mais de 180 commits; 44 RFs, 44 estórias de usuário, 24 RNFs e 37 casos de uso; 103 fontes, Ferramentas de IA usadas: Claude Opus 5.5 (Anthropic), ChatGPT e Codex (OpenAI), Repositório público de documentação no GitHub (Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs)

### Community 39 - "Abastecimento com passageiros (D5)"
Cohesion: 0.40
Nodes (5): EASA CAT.OP.MPA.195, ANAC RBAC 91.102(g), Protótipo UC-A11 — configurar política de abastecimento (tela de computador), Protótipo UC-A6 — aplicar modelo de tarefas (tela de computador), Protótipo UC-A8 — definir dependências entre tarefas (tela de computador)

### Community 41 - "Blueprint: aviso que encerra o alerta (RF-38)"
Cohesion: 0.50
Nodes (3): Aviso da ação registrada encerra o alerta no Monitoramento (RF-38), Aviso (evento), Caso não desenhado: encerramento do alerta pelo RF-38

### Community 42 - "RA2: ajustes do RA1 (T00, T01)"
Cohesion: 0.67
Nodes (3): Ajustes do RA1: título ARO dos RFs (C00.1 a C00.10), T00 Título ARO dos RFs e troca de área, T01 Sprints do item 6 pelas dependências entre RFs

## Ambiguous Edges - Review These
- `Item 8 Relação de Requisitos Não-Funcionais (RNF-1 a RNF-24, classificados pela ISO/IEC 25010:2011)` → `A.3 RNFs x RFs`  [AMBIGUOUS]
  especificacao/apendice-a-matriz-de-rastreabilidade.md · relation: references
- `UC27 Registrar checagem com as equipes em TOBT − 15` → `Motor de Eventos`  [AMBIGUOUS]
  especificacao/diagramas/09-casos-de-uso.png · relation: calls
- `UC34 Atualizar TOBT` → `Motor de Eventos`  [AMBIGUOUS]
  especificacao/diagramas/09-casos-de-uso.png · relation: calls
- `A.4 Casos de uso x diagramas de sequencia (item 14)` → `14 Diagramas de Sequência`  [AMBIGUOUS]
  especificacao/apendice-a-matriz-de-rastreabilidade.md · relation: references
- `A.5 Criterios de aceite x casos de teste (item 15)` → `15 Casos de teste – 00-item`  [AMBIGUOUS]
  especificacao/apendice-a-matriz-de-rastreabilidade.md · relation: references

## Knowledge Gaps
- **109 isolated node(s):** `Heathrow pontualidade "verde" (>=79%)`, `Doc — documento com entradas do sumário a cada título de nível 1`, `Wayfinding (map issue + child tickets)`, `Item 10: 37 especificações (A13, B8, C7, D9), 42 protótipos, 119 fluxos alternativos e 122 de exceção`, `Agrupamento por função no diagrama do item 9 (retângulos cinza só organizam a leitura; não são subsistemas)` (+104 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 168 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **4 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `Item 8 Relação de Requisitos Não-Funcionais (RNF-1 a RNF-24, classificados pela ISO/IEC 25010:2011)` and `A.3 RNFs x RFs`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._
- **What is the exact relationship between `UC27 Registrar checagem com as equipes em TOBT − 15` and `Motor de Eventos`?**
  _Edge tagged AMBIGUOUS (relation: calls) - confidence is low._
- **What is the exact relationship between `UC34 Atualizar TOBT` and `Motor de Eventos`?**
  _Edge tagged AMBIGUOUS (relation: calls) - confidence is low._
- **What is the exact relationship between `A.4 Casos de uso x diagramas de sequencia (item 14)` and `14 Diagramas de Sequência`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._
- **What is the exact relationship between `A.5 Criterios de aceite x casos de teste (item 15)` and `15 Casos de teste – 00-item`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._
- **Why does `Coordenador de Turnaround` connect `MTTT, antecipação e TOBT vigente` to `Numeração provisória, TOBT e scripts`, `Pesquisa, serviços sob demanda e regras de escrita`, `Execução em solo: operador, QR Code e AIBT`, `Régua TOBT + 5 e metas de 80%`, `BPMN TO BE (item 4) e diagramas`, `RFs da área A e prioridade em sprints`, `A-CDM e ADRs de base`, `Atores e dados do operador (D4, D7)`, `Motor de Eventos e alertas`, `RFs de exceção e liberação`, `Marcos do CONTEXT.md`, `Projeção e caminho crítico`, `Administrador e ator Usuário`, `Painel e checagem em TOBT − 15`, `Diagrama de casos de uso: Monitoramento`, `Siglas e vocabulário (D8)`, `Casos de uso: acesso e planejamento`, `Casos de uso: exceções e liberação`, `Códigos de atraso da ANAC (D6)`, `Abastecimento com passageiros (D5)`, `Indicadores de aderência`?**
  _High betweenness centrality (0.120) - this node is a cross-community bridge._
- **Why does `Fontes da pesquisa` connect `Pesquisa, serviços sob demanda e regras de escrita` to `Numeração provisória, TOBT e scripts`, `Siglas e vocabulário (D8)`, `Gerador do documento final (gerar_docx.py)`, `Régua TOBT + 5 e metas de 80%`, `Consolidação em PDF (T13)`, `BPMN TO BE (item 4) e diagramas`, `A-CDM e ADRs de base`, `Atores e dados do operador (D4, D7)`, `Códigos de atraso e mapa da pesquisa`, `MTTT, antecipação e TOBT vigente`, `AGENTS.md e checagem cruzada`, `Siglas do A-CDM e risco ao horário`?**
  _High betweenness centrality (0.118) - this node is a cross-community bridge._