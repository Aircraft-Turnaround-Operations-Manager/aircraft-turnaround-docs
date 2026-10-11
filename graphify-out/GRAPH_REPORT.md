# Graph Report - aircraft-turnaround-docs  (2026-10-10)

## Corpus Check
- 120 files · ~354,008 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 5 file(s) not represented in the graph (top: (none) 4, .bpmn 1)

## Summary
- 625 nodes · 3450 edges · 15 communities
- Extraction: 77% EXTRACTED · 23% INFERRED · 0% AMBIGUOUS · INFERRED: 804 edges (avg confidence: 0.89)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `d8cbc67d`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Área C: monitoramento, alertas, TOBT e objetivo 3
- CONTEXT, regras para IAs, critérios, ADRs e rastreabilidade
- Área B: operador, casos de uso, protótipos e RNFs
- Área A: acesso, planejamento, chegada e segurança
- Área D: estados, exceções e liberação
- Item 2 (É / Não é / Faz / Não faz) e atores do item 5
- BPMN do Motor de Eventos e checagem em TOBT − 15
- Visão do Produto e fontes da pesquisa
- Pesquisa do setor: tolerâncias, marcos e atividades
- BPMN: tarefas de solo e abastecimento
- Serviços sob demanda (pesquisa e ADR-0014)
- Similares de mercado, matriz comparativa e lacunas
- A-CDM e confiabilidade do TOBT
- BPMN TO BE e caminho crítico
- Atraso reacionário e códigos de atraso da IATA

## God Nodes (most connected - your core abstractions)
1. `Coordenador de Turnaround` - 121 edges
2. `Fontes da pesquisa` - 83 edges
3. `Operador de Solo/Rampa` - 76 edges
4. `Serviços sob demanda no turnaround (limpeza com risco biológico, assistência extra, catering adicional)` - 65 edges
5. `EUROCONTROL Specification for A-CDM Ed. 1.0 (2025) [2]` - 58 edges
6. `CONTEXT.md — Contexto do projeto` - 58 edges
7. `Motor de Eventos` - 53 edges
8. `Estados do turnaround` - 46 edges
9. `Objetivo 3: Antecipar desvios e assegurar liberacao segura` - 46 edges
10. `RNF-D1 — Disponibilidade de 99,5% ao mês, 24 h por dia, das funções dos RF-A1 a RF-A13, RF-B7, RF-B8, RF-C1 a RF-C14 e RF-D1 a RF-D9 (Confiabilidade: disponibilidade)` - 45 edges

## Surprising Connections (you probably didn't know these)
- `ATC — Controle de tráfego aéreo (fora de escopo)` --semantically_similar_to--> `Pool externo: Controle de tráfego aéreo (ATC) — fora do escopo`  [INFERRED] [semantically similar]
  CONTEXT.md → especificacao/diagramas/04-bpmn-to-be.png
- `Motor de Eventos` --conceptually_related_to--> `Protótipo UC-B8 — lista de tarefas com a sucessora liberada (celular)`  [INFERRED]
  CONTEXT.md → especificacao/10-especificacoes-de-caso-de-uso/prototipos/uc-b8-propagacao-de-estado.png
- `Motor de Eventos` --conceptually_related_to--> `Motor de Eventos (lane do BPMN)`  [INFERRED]
  CONTEXT.md → especificacao/diagramas/04-bpmn-to-be.png
- `Motor de Eventos` --semantically_similar_to--> `A-CDM System / information platform`  [INFERRED] [semantically similar]
  CONTEXT.md → pesquisa/topicos/papeis-e-atores.md
- `MTTT — Tempo mínimo de turnaround` --conceptually_related_to--> `Verificar a viabilidade (EIBT + MTTT ≤ TOBT)`  [INFERRED]
  CONTEXT.md → especificacao/diagramas/04-bpmn-to-be.png

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Casos de uso da área A: UC-A1 a UC-A13** — especificacao_10_especificacoes_de_caso_de_uso_area_a_uc_a1, especificacao_10_especificacoes_de_caso_de_uso_area_a_uc_a2, especificacao_10_especificacoes_de_caso_de_uso_area_a_uc_a3, especificacao_10_especificacoes_de_caso_de_uso_area_a_uc_a4, especificacao_10_especificacoes_de_caso_de_uso_area_a_uc_a5, especificacao_10_especificacoes_de_caso_de_uso_area_a_uc_a6, especificacao_10_especificacoes_de_caso_de_uso_area_a_uc_a7, especificacao_10_especificacoes_de_caso_de_uso_area_a_uc_a8, especificacao_10_especificacoes_de_caso_de_uso_area_a_uc_a9, especificacao_10_especificacoes_de_caso_de_uso_area_a_uc_a10, especificacao_10_especificacoes_de_caso_de_uso_area_a_uc_a11, especificacao_10_especificacoes_de_caso_de_uso_area_a_uc_a12, especificacao_10_especificacoes_de_caso_de_uso_area_a_uc_a13 [EXTRACTED 1.00]
- **Estórias da área A: US-A1 a US-A13** — especificacao_07_estorias_de_usuario_area_a_us_a1, especificacao_07_estorias_de_usuario_area_a_us_a2, especificacao_07_estorias_de_usuario_area_a_us_a3, especificacao_07_estorias_de_usuario_area_a_us_a4, especificacao_07_estorias_de_usuario_area_a_us_a5, especificacao_07_estorias_de_usuario_area_a_us_a6, especificacao_07_estorias_de_usuario_area_a_us_a7, especificacao_07_estorias_de_usuario_area_a_us_a8, especificacao_07_estorias_de_usuario_area_a_us_a9, especificacao_07_estorias_de_usuario_area_a_us_a10, especificacao_07_estorias_de_usuario_area_a_us_a11, especificacao_07_estorias_de_usuario_area_a_us_a12, especificacao_07_estorias_de_usuario_area_a_us_a13, especificacao_07_estorias_de_usuario_area_a_area_a [EXTRACTED 1.00]
- **Protótipos de tela da área A** — especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_a1_autenticar_celular, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_a1_autenticar_web, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_a2_gerenciar_usuarios, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_a3_abrir_turnaround, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_a4_criar_modelo, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_a5_confirmar_plano, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_a6_aplicar_modelo, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_a7_pontos_de_confirmacao, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_a8_definir_dependencias, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_a9_gerenciar_equipes, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_a10_atualizar_previsao, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_a11_politica_de_abastecimento, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_a12_registrar_chegada, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_a13_corrigir_chegada [EXTRACTED 1.00]
- **Requisitos funcionais da área A (RF-A1 a RF-A13)** — especificacao_06_requisitos_funcionais_area_a_rf_a1, especificacao_06_requisitos_funcionais_area_a_rf_a2, especificacao_06_requisitos_funcionais_area_a_rf_a3, especificacao_06_requisitos_funcionais_area_a_rf_a4, especificacao_06_requisitos_funcionais_area_a_rf_a5, especificacao_06_requisitos_funcionais_area_a_rf_a6, especificacao_06_requisitos_funcionais_area_a_rf_a7, especificacao_06_requisitos_funcionais_area_a_rf_a8, especificacao_06_requisitos_funcionais_area_a_rf_a9, especificacao_06_requisitos_funcionais_area_a_rf_a10, especificacao_06_requisitos_funcionais_area_a_rf_a11, especificacao_06_requisitos_funcionais_area_a_rf_a12, especificacao_06_requisitos_funcionais_area_a_rf_a13 [EXTRACTED 1.00]
- **Requisitos não funcionais da área A (RNF-A1 a RNF-A6)** — especificacao_08_requisitos_nao_funcionais_area_a_rnf_a1, especificacao_08_requisitos_nao_funcionais_area_a_rnf_a2, especificacao_08_requisitos_nao_funcionais_area_a_rnf_a3, especificacao_08_requisitos_nao_funcionais_area_a_rnf_a4, especificacao_08_requisitos_nao_funcionais_area_a_rnf_a5, especificacao_08_requisitos_nao_funcionais_area_a_rnf_a6 [EXTRACTED 1.00]
- **Cadeia RF → estória das ações de execução de tarefa do Operador de Solo/Rampa (RF-B2 a RF-B6, US-B2 a US-B6)** — especificacao_06_requisitos_funcionais_area_b_rf_b2, especificacao_06_requisitos_funcionais_area_b_rf_b3, especificacao_06_requisitos_funcionais_area_b_rf_b4, especificacao_06_requisitos_funcionais_area_b_rf_b5, especificacao_06_requisitos_funcionais_area_b_rf_b6, especificacao_07_estorias_de_usuario_area_b_us_b2, especificacao_07_estorias_de_usuario_area_b_us_b3, especificacao_07_estorias_de_usuario_area_b_us_b4, especificacao_07_estorias_de_usuario_area_b_us_b5, especificacao_07_estorias_de_usuario_area_b_us_b6 [EXTRACTED 1.00]
- **Casos de uso da área B (UC-B1 a UC-B8)** — especificacao_10_especificacoes_de_caso_de_uso_area_b_uc_b1, especificacao_10_especificacoes_de_caso_de_uso_area_b_uc_b2, especificacao_10_especificacoes_de_caso_de_uso_area_b_uc_b3, especificacao_10_especificacoes_de_caso_de_uso_area_b_uc_b4, especificacao_10_especificacoes_de_caso_de_uso_area_b_uc_b5, especificacao_10_especificacoes_de_caso_de_uso_area_b_uc_b6, especificacao_10_especificacoes_de_caso_de_uso_area_b_uc_b7, especificacao_10_especificacoes_de_caso_de_uso_area_b_uc_b8 [EXTRACTED 1.00]
- **«include»: UC-B2, UC-B3 e UC-B5 incluem UC-B7 (marcos) e UC-B8 (propagação), executados pelo Motor de Eventos** — especificacao_10_especificacoes_de_caso_de_uso_area_b_uc_b2, especificacao_10_especificacoes_de_caso_de_uso_area_b_uc_b3, especificacao_10_especificacoes_de_caso_de_uso_area_b_uc_b5, especificacao_10_especificacoes_de_caso_de_uso_area_b_uc_b7, especificacao_10_especificacoes_de_caso_de_uso_area_b_uc_b8, context_motor_de_eventos [EXTRACTED 1.00]
- **Protótipos de tela da área B (UC-B1 a UC-B8)** — especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_b1_lista_de_tarefas, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_b1_detalhe_da_tarefa, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_b2_iniciar_tarefa, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_b3_concluir_tarefa, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_b4_pausar_tarefa, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_b4_retomar_tarefa, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_b5_nao_aplicavel, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_b6_leitura_qr_code, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_b6_pontos_da_tarefa, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_b7_marcos_do_turnaround, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_b8_propagacao_de_estado [EXTRACTED 1.00]
- **Requisitos funcionais da área B (RF-B1 a RF-B8)** — especificacao_06_requisitos_funcionais_area_b_rf_b1, especificacao_06_requisitos_funcionais_area_b_rf_b2, especificacao_06_requisitos_funcionais_area_b_rf_b3, especificacao_06_requisitos_funcionais_area_b_rf_b4, especificacao_06_requisitos_funcionais_area_b_rf_b5, especificacao_06_requisitos_funcionais_area_b_rf_b6, especificacao_06_requisitos_funcionais_area_b_rf_b7, especificacao_06_requisitos_funcionais_area_b_rf_b8 [EXTRACTED 1.00]
- **Requisitos não funcionais da área B (RNF-B1 a RNF-B4)** — especificacao_08_requisitos_nao_funcionais_area_b_rnf_b1, especificacao_08_requisitos_nao_funcionais_area_b_rnf_b2, especificacao_08_requisitos_nao_funcionais_area_b_rnf_b3, especificacao_08_requisitos_nao_funcionais_area_b_rnf_b4 [EXTRACTED 1.00]
- **Casos de uso da área C: UC-C1 a UC-C7** — especificacao_10_especificacoes_de_caso_de_uso_area_c_uc_c1, especificacao_10_especificacoes_de_caso_de_uso_area_c_uc_c2, especificacao_10_especificacoes_de_caso_de_uso_area_c_uc_c3, especificacao_10_especificacoes_de_caso_de_uso_area_c_uc_c4, especificacao_10_especificacoes_de_caso_de_uso_area_c_uc_c5, especificacao_10_especificacoes_de_caso_de_uso_area_c_uc_c6, especificacao_10_especificacoes_de_caso_de_uso_area_c_uc_c7 [EXTRACTED 1.00]
- **Estórias da área C: US-C1 a US-C14** — especificacao_07_estorias_de_usuario_area_c_us_c1, especificacao_07_estorias_de_usuario_area_c_us_c2, especificacao_07_estorias_de_usuario_area_c_us_c3, especificacao_07_estorias_de_usuario_area_c_us_c4, especificacao_07_estorias_de_usuario_area_c_us_c5, especificacao_07_estorias_de_usuario_area_c_us_c6, especificacao_07_estorias_de_usuario_area_c_us_c7, especificacao_07_estorias_de_usuario_area_c_us_c8, especificacao_07_estorias_de_usuario_area_c_us_c9, especificacao_07_estorias_de_usuario_area_c_us_c10, especificacao_07_estorias_de_usuario_area_c_us_c11, especificacao_07_estorias_de_usuario_area_c_us_c12, especificacao_07_estorias_de_usuario_area_c_us_c13, especificacao_07_estorias_de_usuario_area_c_us_c14, especificacao_07_estorias_de_usuario_area_c_area_c [EXTRACTED 1.00]
- **Protótipos de tela da área C** — especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_c1_painel_de_turnarounds, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_c2_linha_do_tempo, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_c3_recalculo_e_caminho_critico, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_c4_alerta_emitido, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_c5_lista_de_alertas, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_c6_checagem_tobt_15, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_c7_indicadores_de_aderencia, especificacao_10_especificacoes_de_caso_de_uso_area_c_area_c [EXTRACTED 1.00]
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

## Communities (15 total, 0 thin omitted)

### Community 0 - "Área C: monitoramento, alertas, TOBT e objetivo 3"
Cohesion: 0.09
Nodes (103): Metas do item 1 (precisão, sincronização, desvios), Motor de Eventos, MTTT — Tempo mínimo de turnaround, Risco ao horário (gatilhos A-CDM), TOBT — Horário-alvo de prontidão, ADR-0001 — TOBT planejado + 5 min, Heathrow pontualidade "verde" (>=79%), ADR-0003 — Atualizar previsão na antecipação (+95 more)

### Community 1 - "CONTEXT, regras para IAs, critérios, ADRs e rastreabilidade"
Cohesion: 0.07
Nodes (74): Formato de arquivo de pesquisa (YAML + seção Ligações), AGENTS.md regra 8 — registrar a suposição sobre outra área em vez de inventar o requisito, AGENTS.md regra 9 — toda sigla com o nome em português na primeira ocorrência de cada item (inclusive A-CDM, ANAC, ISO/IEC), CONTEXT.md — Contexto do projeto, A-CDM — Tomada de decisão colaborativa em aeroportos, Aircraft Turnaround Orchestration System, IATA — Associação Internacional de Transporte Aéreo, Tabela "O que ler para cada item" (+66 more)

### Community 2 - "Área B: operador, casos de uso, protótipos e RNFs"
Cohesion: 0.11
Nodes (78): AEGT — Fim real do atendimento em solo, Estados da tarefa, Operador de Solo/Rampa, ADR-0007 — Dados do operador e QR Code, Diferencial DF5 (QR Code por assento/fileira/zona), Leitura de QR Code pelo celular, ADR-0013 — Chegada à posição registrada direto pelo operador, sem confirmação, Recusas do registro do AIBT (operador sem tarefa atribuída, horário futuro, chegada já registrada, plano inicial não confirmado) (+70 more)

### Community 3 - "Área A: acesso, planejamento, chegada e segurança"
Cohesion: 0.11
Nodes (75): Administrador do Sistema, Usuário (ator abstrato), ADR-0005 — Abastecimento com passageiros configurável, EASA CAT.OP.MPA.195, ANAC RBAC 91.102(g), Correção do AIBT pelo Coordenador de Turnaround (motivo, valor anterior e novo, autor e horário; até "Fora de bloco"; dispara o recálculo da projeção), ADR-0014 — Serviços sob demanda: catálogo no modelo de tarefas, acionado pelo Coordenador de Turnaround, Catálogo de serviços sob demanda no modelo de tarefas (tarefas "sob demanda" com tipo de atividade, equipe e duração planejada; fora do plano até serem acionadas) (+67 more)

### Community 4 - "Área D: estados, exceções e liberação"
Cohesion: 0.10
Nodes (67): ARDT — Horário real de prontidão (Aircraft Ready), ATC — Controle de tráfego aéreo (fora de escopo), Autoridade de Liberação, Estados do turnaround, IATA AHM 730, IATA AHM 732, ANAC Portaria nº 55/2026, Alerta de risco ao horario planejado (+59 more)

### Community 5 - "Item 2 (É / Não é / Faz / Não faz) e atores do item 5"
Cohesion: 0.11
Nodes (25): Fora de escopo (voos, tripulação, financeiro, ATC), TSAT — Horário-alvo de autorização de acionamento, Metrica: 100% tarefas com responsavel, painel atualizado em ate 5 s, Painel operacional, Instrumento de apoio à decisão do Coordenador de Turnaround e da Autoridade de Liberação, Registro da causa de atraso/exceção com código da tabela da ANAC, Fora de escopo: malha aerea, slots, ATC, escalas, financeiro, visao computacional/sensores, Não define o turnaround programado nem o MTTT (dados de entrada) (+17 more)

### Community 6 - "BPMN do Motor de Eventos e checagem em TOBT − 15"
Cohesion: 0.18
Nodes (28): Leitura do diagrama: eventos e mensagens (chegada, autorização do ATC, sinais de desembarque/abastecimento concluído, temporizador TOBT − 15 min), RF-C11 — Exibir o aviso de checagem em TOBT − 15 min com as tarefas obrigatórias não concluídas e as equipes responsáveis, RF-C14 — Registrar a checagem com as equipes de um aviso de TOBT − 15 aberto e encerrar o aviso, US-C11 — Exibir o aviso de checagem em TOBT − 15 (4 critérios de aceite), US-C14 — Registrar a checagem com as equipes (3 critérios de aceite), UC-C6 — Registrar a checagem com as equipes em TOBT − 15, Protótipo UC-C6 — checagem em TOBT − 15 (tela de computador), Evento de início (mensagem): Voo previsto para a posição (+20 more)

### Community 7 - "Visão do Produto e fontes da pesquisa"
Cohesion: 0.16
Nodes (26): Benefício-chave: aeronave pronta para liberação no TOBT, desvios tratados durante a operação, Categoria-segmento: software de gestão de turnaround / operações de solo, Diferencial-chave: grafo de tarefas com caminho crítico, bloqueio da liberação, registro pelo operador com QR Code, régua TOBT + 5 min, E2: turnaround dentro do planejado, medido pela régua TOBT planejado + 5 min, Item 3 Visao do Produto, P3: atividades paralelas sem visão compartilhada; coordenação por rádio falha, P4: monitoramento automático exige câmeras/sensores e não registra quem executou, Fontes da pesquisa (+18 more)

### Community 8 - "Pesquisa do setor: tolerâncias, marcos e atividades"
Cohesion: 0.16
Nodes (25): IATA AHM 732 delay codes webinar [37], SES Performance ATFM slot adherence [15], Insumos para os RFs, por area (4.3), Insumos para os RNFs (4.4), RNF requirements mapped to ISO/IEC 25010, Metricas do item 1 (4.1), M9: zero releases with pending task or open exception, 80% target for M2 and M3 (+17 more)

### Community 9 - "BPMN: tarefas de solo e abastecimento"
Cohesion: 0.19
Nodes (24): Evento de mensagem: Aeronave em posição (AIBT), Gateway exclusivo (abastecimento): Abastecimento com passageiros permitido? (Sim → abastecer; Não → aguardar "Desembarque concluído"), Gateway exclusivo (embarque): Abastecimento com passageiros permitido? (Sim → embarcar; Não → aguardar "Abastecimento concluído"), Gateway paralelo: abertura das tarefas em paralelo após o ACGT, Gateway paralelo: junção de embarque e carregamento de bagagem e carga, Gateway paralelo: junção final das tarefas de solo, Gateway paralelo: junção de limpeza e catering, Gateway paralelo: limpeza da cabine e catering após o desembarque (+16 more)

### Community 10 - "Serviços sob demanda (pesquisa e ADR-0014)"
Cohesion: 0.19
Nodes (22): ANAC — Resolução nº 280/2013 (assistência especial ao PNAE) [78], ANVISA — RDC nº 1.038/2026 (segurança sanitária em aeroportos e aeronaves) [76], EPG — Ground Handling System [97], Genève Aéroport — A-CDM Procedures LSGG [92], Hamburg Airport — Quality Charter, assistência a PRM (2008) [82], Airport Authority Hong Kong — A-CDM Operations Guidelines v2.0 (2018) [93], IATA — AHM e SGHA, apresentação ao MLIT do Japão (2025) [68], IATA — Aircraft Cleaning and Disinfection During and Post Pandemic, ed. 2 (2021) [73] (+14 more)

### Community 11 - "Similares de mercado, matriz comparativa e lacunas"
Cohesion: 0.24
Nodes (17): Ficha - ADB SAFEGATE, ADB SAFEGATE Safedock + Apron Manager, Ficha - Assaia, Assaia ApronAI / TurnaroundControl, Ficha - INFORM GroundStar, Lacunas e diferencial possivel (3.4), Observed gaps in similar products, Matriz comparativa (3.3) (+9 more)

### Community 12 - "A-CDM e confiabilidade do TOBT"
Cohesion: 0.21
Nodes (12): Cliente-alvo: empresas de handling e companhias aéreas (responsáveis pelo TOBT), P2: TOBT pouco confiável (menos de 60% de acerto em 5 min), EUROCONTROL A-CDM Impact Assessment (2016) [14], Assaia - value of accurate off-block predictions [19], EUROCONTROL A-CDM concept page [1], IATA A-CDM Recommendations (2018) [5], Veovo - The trouble with TOBT [18], A-CDM (Airport Collaborative Decision Making) (+4 more)

### Community 13 - "BPMN TO BE e caminho crítico"
Cohesion: 0.32
Nodes (12): Leitura do diagrama: caminho principal (abertura, viabilidade, AIBT, ACGT, tarefas em paralelo, ASBT, loadsheet, AEGT, ARDT, AOBT), Item 4 Mapeamento de Negocios (BPMN to-be), Leitura do diagrama: pool e lanes (uma lane por ator; ATC como pool externo fechado), Leitura do diagrama: subprocessos de evento (monitoramento, tratamento de alerta, atualização da previsão, checagem em TOBT − 15 min), Diagrama BPMN TO BE do turnaround (04-bpmn-to-be.png), Kierzkowski et al. 2025 - PERT-COST ground handling [22], Planda & Skorupski 2025 - Aircraft Boarding Under Disturbances [21], Schultz 2018 - Fast Aircraft Turnaround Enabled by Reliable Passenger Boarding [20] (+4 more)

### Community 14 - "Atraso reacionário e códigos de atraso da IATA"
Cohesion: 0.40
Nodes (5): P1: desvios percebidos tarde e propagados (atraso reacionário 46%, 67,9% das partidas em até 15 min), EUROCONTROL CODA Digest 2023 [16], Rodriguez-Sanz & Herrera 2020 - Turnaround time allocation RL [23], IATA AHM 730 two-digit delay codes, Reactionary delay (46% of EU delay minutes 2023)

## Knowledge Gaps
- **9 isolated node(s):** `Heathrow pontualidade "verde" (>=79%)`, `Wayfinding (map issue + child tickets)`, `Dependências e ordem de execução dos itens`, `Item 11 Diagrama de Atividades`, `Amadeus (excluded candidate)` (+4 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 9 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Fontes da pesquisa` connect `Visão do Produto e fontes da pesquisa` to `Área C: monitoramento, alertas, TOBT e objetivo 3`, `CONTEXT, regras para IAs, critérios, ADRs e rastreabilidade`, `Área B: operador, casos de uso, protótipos e RNFs`, `Área A: acesso, planejamento, chegada e segurança`, `Área D: estados, exceções e liberação`, `Item 2 (É / Não é / Faz / Não faz) e atores do item 5`, `BPMN do Motor de Eventos e checagem em TOBT − 15`, `Pesquisa do setor: tolerâncias, marcos e atividades`, `Serviços sob demanda (pesquisa e ADR-0014)`, `A-CDM e confiabilidade do TOBT`, `BPMN TO BE e caminho crítico`, `Atraso reacionário e códigos de atraso da IATA`?**
  _High betweenness centrality (0.146) - this node is a cross-community bridge._
- **Why does `Coordenador de Turnaround` connect `Área A: acesso, planejamento, chegada e segurança` to `Área C: monitoramento, alertas, TOBT e objetivo 3`, `CONTEXT, regras para IAs, critérios, ADRs e rastreabilidade`, `Área B: operador, casos de uso, protótipos e RNFs`, `Área D: estados, exceções e liberação`, `Item 2 (É / Não é / Faz / Não faz) e atores do item 5`, `BPMN do Motor de Eventos e checagem em TOBT − 15`, `A-CDM e confiabilidade do TOBT`?**
  _High betweenness centrality (0.114) - this node is a cross-community bridge._
- **Why does `CONTEXT.md — Contexto do projeto` connect `CONTEXT, regras para IAs, critérios, ADRs e rastreabilidade` to `Área C: monitoramento, alertas, TOBT e objetivo 3`, `Área B: operador, casos de uso, protótipos e RNFs`, `Área A: acesso, planejamento, chegada e segurança`, `Área D: estados, exceções e liberação`, `Item 2 (É / Não é / Faz / Não faz) e atores do item 5`, `Visão do Produto e fontes da pesquisa`, `Pesquisa do setor: tolerâncias, marcos e atividades`, `Serviços sob demanda (pesquisa e ADR-0014)`, `A-CDM e confiabilidade do TOBT`?**
  _High betweenness centrality (0.096) - this node is a cross-community bridge._
- **Are the 30 inferred relationships involving `Coordenador de Turnaround` (e.g. with `ADR-0009 — Nome Coordenador de Turnaround` and `Cliente-alvo: empresas de handling e companhias aéreas (responsáveis pelo TOBT)`) actually correct?**
  _`Coordenador de Turnaround` has 30 INFERRED edges - model-reasoned connections that need verification._
- **Are the 27 inferred relationships involving `Operador de Solo/Rampa` (e.g. with `Leitura de QR Code pelo celular` and `Equipe ou especialidade do operador como dado do cadastro (não um ator por especialidade)`) actually correct?**
  _`Operador de Solo/Rampa` has 27 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Heathrow pontualidade "verde" (>=79%)`, `Wayfinding (map issue + child tickets)`, `Dependências e ordem de execução dos itens` to the rest of the system?**
  _9 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Área C: monitoramento, alertas, TOBT e objetivo 3` be split into smaller, more focused modules?**
  _Cohesion score 0.09415992812219227 - nodes in this community are weakly interconnected._