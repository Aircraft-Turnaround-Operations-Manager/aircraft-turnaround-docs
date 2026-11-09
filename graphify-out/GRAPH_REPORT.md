# Graph Report - aircraft-turnaround-docs  (2026-11-09)

## Corpus Check
- 9 files · ~670,708 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 760 nodes · 3886 edges · 30 communities (27 shown, 3 thin omitted)
- Extraction: 76% EXTRACTED · 24% INFERRED · 0% AMBIGUOUS · INFERRED: 914 edges (avg confidence: 0.88)
- Token cost: 166,893 input · 0 output

## Community Hubs (Navigation)
- Monitoramento: projeção, alertas, TOBT e objetivos 1 e 3
- Especificações por área, casos de uso, estórias e matriz
- Execução em solo: operador, estados e QR Code
- BPMN TO BE (item 4) e exportação dos diagramas
- Serviços sob demanda e replanejamento
- Autoridade de Liberação, estados do turnaround, prontidão (ARDT) e exceções
- Tarefas em solo no BPMN, abastecimento e paralelismo
- Item 11, marcos (RF-20) e checagem dos diagramas
- Mapa da pesquisa: tópicos de base e ADRs
- Pesquisa, fontes e problemas do setor
- Quadro É / Não é / Faz / Não faz
- Similares de mercado e diferencial
- CONTEXT, AGENTS, README e critérios de aceite
- Chegada à posição (AIBT, ADR-0013)
- Visão do Produto (item 3)
- Contrato entre os serviços: mensageria e envelope
- ADR-0015 e ADR-0016: quatro microsserviços
- Caminho crítico e previsibilidade
- Gerador do documento final (gerar_docx.py)
- A-CDM, IATA e siglas
- Regras de escrita: grafo, checagem cruzada e siglas
- RA2: itens 13 e 14 (classes e sequência)
- RA2: item 12 e decisões B1 a B8
- Assaia e capacidades observadas
- IATA, RNFs e ISO/IEC 25010
- RA2: ajustes do RA1 (T00, T01)
- RA2: fechamento (T16, T17)
- Site único em Angular

## God Nodes (most connected - your core abstractions)
1. `Coordenador de Turnaround` - 119 edges
2. `Fontes da pesquisa` - 83 edges
3. `EUROCONTROL Specification for A-CDM Ed. 1.0 (2025) [2]` - 78 edges
4. `Operador de Solo/Rampa` - 67 edges
5. `Serviços sob demanda no turnaround (limpeza com risco biológico, assistência extra, catering adicional)` - 62 edges
6. `Motor de Eventos` - 55 edges
7. `Estados do turnaround (Em solo ... Fora de bloco, Em exceção)` - 50 edges
8. `Item 4 Mapeamento de Negócios (BPMN TO BE em vistas)` - 49 edges
9. `Requisitos funcionais — acesso, cadastros, planejamento e chegada à posição (RF-1 a RF-13)` - 47 edges
10. `Objetivo 3: Antecipar desvios e assegurar liberacao segura` - 46 edges

## Surprising Connections (you probably didn't know these)
- `TOBT planejado (fixo, régua da meta)` --conceptually_related_to--> `Protótipo UC-A5 — confirmar plano inicial (tela de computador)`  [INFERRED]
  docs/adr/0003-atualizar-previsao-na-antecipacao.md → especificacao/10-especificacoes-de-caso-de-uso/prototipos/uc-a5-confirmar-plano.png
- `Turnaround critical path` --conceptually_related_to--> `Protótipo UC-C3 — recálculo e caminho crítico (tela de computador)`  [INFERRED]
  pesquisa/topicos/caminho-critico.md → especificacao/10-especificacoes-de-caso-de-uso/prototipos/uc-c3-recalculo-e-caminho-critico.png
- `Turnaround critical path` --conceptually_related_to--> `Subprocesso: Executar as tarefas em solo (início "Atendimento iniciado", fim "Tarefas em solo concluídas")`  [INFERRED]
  pesquisa/topicos/caminho-critico.md → especificacao/diagramas/04-bpmn-to-be.png
- `Turnaround critical path` --conceptually_related_to--> `Propagar estados e recalcular projeção, caminho crítico e aderência ao TOBT + 5 min`  [INFERRED]
  pesquisa/topicos/caminho-critico.md → especificacao/diagramas/04-bpmn-to-be.png
- `Turnaround critical path` --conceptually_related_to--> `Diagrama de atividades 11.4 — Eventos, alertas e intervenções (11-monitoramento.png)`  [INFERRED]
  pesquisa/topicos/caminho-critico.md → especificacao/diagramas/11-monitoramento.png

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Casos de uso da área A: UC01 a UC13** — especificacao_10_especificacoes_de_caso_de_uso_area_a_uc_a1, especificacao_10_especificacoes_de_caso_de_uso_area_a_uc_a2, especificacao_10_especificacoes_de_caso_de_uso_area_a_uc_a3, especificacao_10_especificacoes_de_caso_de_uso_area_a_uc_a4, especificacao_10_especificacoes_de_caso_de_uso_area_a_uc_a5, especificacao_10_especificacoes_de_caso_de_uso_area_a_uc_a6, especificacao_10_especificacoes_de_caso_de_uso_area_a_uc_a7, especificacao_10_especificacoes_de_caso_de_uso_area_a_uc_a8, especificacao_10_especificacoes_de_caso_de_uso_area_a_uc_a9, especificacao_10_especificacoes_de_caso_de_uso_area_a_uc_a10, especificacao_10_especificacoes_de_caso_de_uso_area_a_uc_a11, especificacao_10_especificacoes_de_caso_de_uso_area_a_uc_a12, especificacao_10_especificacoes_de_caso_de_uso_area_a_uc_a13 [EXTRACTED 1.00]
- **Estórias da área A: US001 a US013** — especificacao_07_estorias_de_usuario_area_a_us_a1, especificacao_07_estorias_de_usuario_area_a_us_a2, especificacao_07_estorias_de_usuario_area_a_us_a3, especificacao_07_estorias_de_usuario_area_a_us_a4, especificacao_07_estorias_de_usuario_area_a_us_a5, especificacao_07_estorias_de_usuario_area_a_us_a6, especificacao_07_estorias_de_usuario_area_a_us_a7, especificacao_07_estorias_de_usuario_area_a_us_a8, especificacao_07_estorias_de_usuario_area_a_us_a9, especificacao_07_estorias_de_usuario_area_a_us_a10, especificacao_07_estorias_de_usuario_area_a_us_a11, especificacao_07_estorias_de_usuario_area_a_us_a12, especificacao_07_estorias_de_usuario_area_a_us_a13, especificacao_07_estorias_de_usuario_area_a_area_a [EXTRACTED 1.00]
- **Protótipos de tela da área A** — especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_a1_autenticar_celular, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_a1_autenticar_web, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_a2_gerenciar_usuarios, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_a3_abrir_turnaround, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_a4_criar_modelo, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_a5_confirmar_plano, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_a6_aplicar_modelo, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_a7_pontos_de_confirmacao, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_a8_definir_dependencias, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_a9_gerenciar_equipes, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_a10_atualizar_previsao, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_a11_politica_de_abastecimento, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_a12_registrar_chegada, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_a13_corrigir_chegada [EXTRACTED 1.00]
- **Requisitos funcionais da área A (RF-1 a RF-13)** — especificacao_06_requisitos_funcionais_area_a_rf_a1, especificacao_06_requisitos_funcionais_area_a_rf_a2, especificacao_06_requisitos_funcionais_area_a_rf_a3, especificacao_06_requisitos_funcionais_area_a_rf_a4, especificacao_06_requisitos_funcionais_area_a_rf_a5, especificacao_06_requisitos_funcionais_area_a_rf_a6, especificacao_06_requisitos_funcionais_area_a_rf_a7, especificacao_06_requisitos_funcionais_area_a_rf_a8, especificacao_06_requisitos_funcionais_area_a_rf_a9, especificacao_06_requisitos_funcionais_area_a_rf_a10, especificacao_06_requisitos_funcionais_area_a_rf_a11, especificacao_06_requisitos_funcionais_area_a_rf_a12, especificacao_06_requisitos_funcionais_area_a_rf_a13 [EXTRACTED 1.00]
- **Requisitos não funcionais da área A (RNF-1 a RNF-6)** — especificacao_08_requisitos_nao_funcionais_area_a_rnf_a1, especificacao_08_requisitos_nao_funcionais_area_a_rnf_a2, especificacao_08_requisitos_nao_funcionais_area_a_rnf_a3, especificacao_08_requisitos_nao_funcionais_area_a_rnf_a4, especificacao_08_requisitos_nao_funcionais_area_a_rnf_a5, especificacao_08_requisitos_nao_funcionais_area_a_rnf_a6 [EXTRACTED 1.00]
- **Cadeia RF → estória das ações de execução de tarefa do Operador de Solo/Rampa (RF-15 a RF-19, US015 a US019)** — especificacao_06_requisitos_funcionais_area_b_rf_b2, especificacao_06_requisitos_funcionais_area_b_rf_b3, especificacao_06_requisitos_funcionais_area_b_rf_b4, especificacao_06_requisitos_funcionais_area_b_rf_b5, especificacao_06_requisitos_funcionais_area_b_rf_b6, especificacao_07_estorias_de_usuario_area_b_us_b2, especificacao_07_estorias_de_usuario_area_b_us_b3, especificacao_07_estorias_de_usuario_area_b_us_b4, especificacao_07_estorias_de_usuario_area_b_us_b5, especificacao_07_estorias_de_usuario_area_b_us_b6 [EXTRACTED 1.00]
- **Casos de uso da área B (UC14 a UC21)** — especificacao_10_especificacoes_de_caso_de_uso_area_b_uc_b1, especificacao_10_especificacoes_de_caso_de_uso_area_b_uc_b2, especificacao_10_especificacoes_de_caso_de_uso_area_b_uc_b3, especificacao_10_especificacoes_de_caso_de_uso_area_b_uc_b4, especificacao_10_especificacoes_de_caso_de_uso_area_b_uc_b5, especificacao_10_especificacoes_de_caso_de_uso_area_b_uc_b6, especificacao_10_especificacoes_de_caso_de_uso_area_b_uc_b7, especificacao_10_especificacoes_de_caso_de_uso_area_b_uc_b8 [EXTRACTED 1.00]
- **«include»: UC15, UC16 e UC18 incluem UC20 (marcos) e UC21 (propagação), executados pelo Motor de Eventos** — especificacao_10_especificacoes_de_caso_de_uso_area_b_uc_b2, especificacao_10_especificacoes_de_caso_de_uso_area_b_uc_b3, especificacao_10_especificacoes_de_caso_de_uso_area_b_uc_b5, especificacao_10_especificacoes_de_caso_de_uso_area_b_uc_b7, especificacao_10_especificacoes_de_caso_de_uso_area_b_uc_b8, context_motor_de_eventos [EXTRACTED 1.00]
- **Protótipos de tela da área B (UC14 a UC21)** — especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_b1_lista_de_tarefas, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_b1_detalhe_da_tarefa, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_b2_iniciar_tarefa, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_b3_concluir_tarefa, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_b4_pausar_tarefa, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_b4_retomar_tarefa, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_b5_nao_aplicavel, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_b6_leitura_qr_code, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_b6_pontos_da_tarefa, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_b7_marcos_do_turnaround, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_b8_propagacao_de_estado [EXTRACTED 1.00]
- **Requisitos funcionais da área B (RF-14 a RF-21)** — especificacao_06_requisitos_funcionais_area_b_rf_b1, especificacao_06_requisitos_funcionais_area_b_rf_b2, especificacao_06_requisitos_funcionais_area_b_rf_b3, especificacao_06_requisitos_funcionais_area_b_rf_b4, especificacao_06_requisitos_funcionais_area_b_rf_b5, especificacao_06_requisitos_funcionais_area_b_rf_b6, especificacao_06_requisitos_funcionais_area_b_rf_b7, especificacao_06_requisitos_funcionais_area_b_rf_b8 [EXTRACTED 1.00]
- **Requisitos não funcionais da área B (RNF-7 a RNF-10)** — especificacao_08_requisitos_nao_funcionais_area_b_rnf_b1, especificacao_08_requisitos_nao_funcionais_area_b_rnf_b2, especificacao_08_requisitos_nao_funcionais_area_b_rnf_b3, especificacao_08_requisitos_nao_funcionais_area_b_rnf_b4 [EXTRACTED 1.00]
- **Casos de uso da área C: UC22 a UC28** — especificacao_10_especificacoes_de_caso_de_uso_area_c_uc_c1, especificacao_10_especificacoes_de_caso_de_uso_area_c_uc_c2, especificacao_10_especificacoes_de_caso_de_uso_area_c_uc_c3, especificacao_10_especificacoes_de_caso_de_uso_area_c_uc_c4, especificacao_10_especificacoes_de_caso_de_uso_area_c_uc_c5, especificacao_10_especificacoes_de_caso_de_uso_area_c_uc_c6, especificacao_10_especificacoes_de_caso_de_uso_area_c_uc_c7 [EXTRACTED 1.00]
- **Estórias da área C: US022 a US035** — especificacao_07_estorias_de_usuario_area_c_us_c1, especificacao_07_estorias_de_usuario_area_c_us_c2, especificacao_07_estorias_de_usuario_area_c_us_c3, especificacao_07_estorias_de_usuario_area_c_us_c4, especificacao_07_estorias_de_usuario_area_c_us_c5, especificacao_07_estorias_de_usuario_area_c_us_c6, especificacao_07_estorias_de_usuario_area_c_us_c7, especificacao_07_estorias_de_usuario_area_c_us_c8, especificacao_07_estorias_de_usuario_area_c_us_c9, especificacao_07_estorias_de_usuario_area_c_us_c10, especificacao_07_estorias_de_usuario_area_c_us_c11, especificacao_07_estorias_de_usuario_area_c_us_c12, especificacao_07_estorias_de_usuario_area_c_us_c13, especificacao_07_estorias_de_usuario_area_c_us_c14, especificacao_07_estorias_de_usuario_area_c_area_c [EXTRACTED 1.00]
- **Protótipos de tela da área C** — especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_c1_painel_de_turnarounds, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_c2_linha_do_tempo_v2, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_c3_recalculo_e_caminho_critico, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_c4_alerta_emitido, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_c5_lista_de_alertas, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_c6_checagem_tobt_15, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_c7_indicadores_de_aderencia, especificacao_10_especificacoes_de_caso_de_uso_area_c_area_c [EXTRACTED 1.00]
- **Requisitos funcionais da área C (RF-22 a RF-35)** — especificacao_06_requisitos_funcionais_area_c_rf_c1, especificacao_06_requisitos_funcionais_area_c_rf_c2, especificacao_06_requisitos_funcionais_area_c_rf_c3, especificacao_06_requisitos_funcionais_area_c_rf_c4, especificacao_06_requisitos_funcionais_area_c_rf_c5, especificacao_06_requisitos_funcionais_area_c_rf_c6, especificacao_06_requisitos_funcionais_area_c_rf_c7, especificacao_06_requisitos_funcionais_area_c_rf_c8, especificacao_06_requisitos_funcionais_area_c_rf_c9, especificacao_06_requisitos_funcionais_area_c_rf_c10, especificacao_06_requisitos_funcionais_area_c_rf_c11, especificacao_06_requisitos_funcionais_area_c_rf_c12, especificacao_06_requisitos_funcionais_area_c_rf_c13, especificacao_06_requisitos_funcionais_area_c_rf_c14 [EXTRACTED 1.00]
- **Requisitos não funcionais da área C (RNF-11 a RNF-18)** — especificacao_08_requisitos_nao_funcionais_area_c_rnf_c1, especificacao_08_requisitos_nao_funcionais_area_c_rnf_c2, especificacao_08_requisitos_nao_funcionais_area_c_rnf_c3, especificacao_08_requisitos_nao_funcionais_area_c_rnf_c4, especificacao_08_requisitos_nao_funcionais_area_c_rnf_c5, especificacao_08_requisitos_nao_funcionais_area_c_rnf_c6, especificacao_08_requisitos_nao_funcionais_area_c_rnf_c7, especificacao_08_requisitos_nao_funcionais_area_c_rnf_c8 [EXTRACTED 1.00]
- **Casos de uso da área D: UC29 a UC37** — especificacao_10_especificacoes_de_caso_de_uso_area_d_uc_d1, especificacao_10_especificacoes_de_caso_de_uso_area_d_uc_d2, especificacao_10_especificacoes_de_caso_de_uso_area_d_uc_d3, especificacao_10_especificacoes_de_caso_de_uso_area_d_uc_d4, especificacao_10_especificacoes_de_caso_de_uso_area_d_uc_d5, especificacao_10_especificacoes_de_caso_de_uso_area_d_uc_d6, especificacao_10_especificacoes_de_caso_de_uso_area_d_uc_d7, especificacao_10_especificacoes_de_caso_de_uso_area_d_uc_d8, especificacao_10_especificacoes_de_caso_de_uso_area_d_uc_d9 [EXTRACTED 1.00]
- **Estórias da área D: US036 a US044** — especificacao_07_estorias_de_usuario_area_d_us_d1, especificacao_07_estorias_de_usuario_area_d_us_d2, especificacao_07_estorias_de_usuario_area_d_us_d3, especificacao_07_estorias_de_usuario_area_d_us_d4, especificacao_07_estorias_de_usuario_area_d_us_d5, especificacao_07_estorias_de_usuario_area_d_us_d6, especificacao_07_estorias_de_usuario_area_d_us_d7, especificacao_07_estorias_de_usuario_area_d_us_d8, especificacao_07_estorias_de_usuario_area_d_us_d9, especificacao_07_estorias_de_usuario_area_d_area_d [EXTRACTED 1.00]
- **Protótipos de tela da área D** — especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_d1_abrir_excecao, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_d2_reatribuir_tarefa, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_d3_registrar_acao_do_alerta, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_d4_confirmar_prontidao_v2, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_d5_encerrar_excecao, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_d6_atualizar_tobt, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_d7_acionar_servico_sob_demanda, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_d7_replanejar_tarefas, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_d8_operadores_disponiveis, especificacao_10_especificacoes_de_caso_de_uso_prototipos_uc_d9_registrar_saida_da_posicao [EXTRACTED 1.00]
- **Requisitos funcionais da área D (RF-36 a RF-44)** — especificacao_06_requisitos_funcionais_area_d_area_d, especificacao_06_requisitos_funcionais_area_d_rf_d1, especificacao_06_requisitos_funcionais_area_d_rf_d2, especificacao_06_requisitos_funcionais_area_d_rf_d3, especificacao_06_requisitos_funcionais_area_d_rf_d4, especificacao_06_requisitos_funcionais_area_d_rf_d5, especificacao_06_requisitos_funcionais_area_d_rf_d6, especificacao_06_requisitos_funcionais_area_d_rf_d7, especificacao_06_requisitos_funcionais_area_d_rf_d8, especificacao_06_requisitos_funcionais_area_d_rf_d9 [EXTRACTED 1.00]
- **Requisitos não funcionais da área D (RNF-19 a RNF-24)** — especificacao_08_requisitos_nao_funcionais_area_d_rnf_d1, especificacao_08_requisitos_nao_funcionais_area_d_rnf_d2, especificacao_08_requisitos_nao_funcionais_area_d_rnf_d3, especificacao_08_requisitos_nao_funcionais_area_d_rnf_d4, especificacao_08_requisitos_nao_funcionais_area_d_rnf_d5, especificacao_08_requisitos_nao_funcionais_area_d_rnf_d6 [EXTRACTED 1.00]
- **Cinco atores da Relação de Atores / Usuários (item 5)** — especificacao_05_atores_usuarios_operador_de_solo_rampa, especificacao_05_atores_usuarios_coordenador_de_turnaround, especificacao_05_atores_usuarios_autoridade_de_liberacao, especificacao_05_atores_usuarios_administrador_do_sistema, especificacao_05_atores_usuarios_motor_de_eventos [EXTRACTED 1.00]
- **Atores do turnaround (Operador de Solo/Rampa, Coordenador de Turnaround, Autoridade de Liberação)** — context_operador_de_solo_rampa, pesquisa_topicos_papeis_e_atores_coordenador_de_turnaround, pesquisa_topicos_papeis_e_atores_autoridade_de_liberacao [EXTRACTED 1.00]
- **Ferramentas do BPMN: package.json, exportar_bpmn.mjs e verificar_bpmn.py** — scripts_package_json, scripts_exportar_bpmn, scripts_verificar_bpmn [EXTRACTED 1.00]
- **Lanes do pool do turnaround (BPMN TO BE)** — especificacao_diagramas_04_bpmn_to_be_lane_coordenador_de_turnaround, especificacao_diagramas_04_bpmn_to_be_lane_operador_de_solo_rampa, especificacao_diagramas_04_bpmn_to_be_lane_motor_de_eventos, especificacao_diagramas_04_bpmn_to_be_lane_autoridade_de_liberacao [EXTRACTED 1.00]
- **Quatro subprocessos de evento do BPMN TO BE** — especificacao_diagramas_04_bpmn_to_be_subprocesso_monitoramento_a_cada_registro, especificacao_diagramas_04_bpmn_to_be_subprocesso_tratamento_de_alerta_de_risco, especificacao_diagramas_04_bpmn_to_be_subprocesso_atualizacao_da_previsao, especificacao_diagramas_04_bpmn_to_be_subprocesso_checagem_em_tobt_menos_15_min [EXTRACTED 1.00]
- **Ramos em paralelo do subprocesso "Executar as tarefas em solo" (após o ACGT)** — especificacao_diagramas_04_bpmn_to_be_tarefa_desembarcar_os_passageiros, especificacao_diagramas_04_bpmn_to_be_tarefa_descarregar_bagagem_e_carga, especificacao_diagramas_04_bpmn_to_be_tarefa_abastecer_a_aeronave, especificacao_diagramas_04_bpmn_to_be_tarefa_atender_agua_potavel_e_lavatorios, especificacao_diagramas_04_bpmn_to_be_tarefa_inspecao_tecnica_de_transito, especificacao_diagramas_04_bpmn_to_be_subprocesso_executar_as_tarefas_em_solo [EXTRACTED 1.00]
- **Vistas do mesmo modelo BPMN TO BE (processo principal, visão geral e vistas por subprocesso)** — especificacao_diagramas_04_bpmn_to_be, especificacao_diagramas_04_bpmn_to_be_geral, especificacao_diagramas_04_bpmn_to_be_tarefas_em_solo, especificacao_diagramas_04_bpmn_to_be_monitoramento, especificacao_diagramas_04_bpmn_to_be_alerta, especificacao_diagramas_04_bpmn_to_be_previsao, especificacao_diagramas_04_bpmn_to_be_tobt_15 [EXTRACTED 1.00]
- **Declaração de uso de IA: ferramentas, responsabilidade dos autores, repositório público e processo de revisão humana** — especificacao_00_declaracao_de_uso_de_ia, especificacao_00_declaracao_de_uso_de_ia_frase_obrigatoria, especificacao_00_declaracao_de_uso_de_ia_ferramentas_usadas, especificacao_00_declaracao_de_uso_de_ia_ia_como_ferramenta_nao_autora, especificacao_00_declaracao_de_uso_de_ia_repositorio_publico_github, especificacao_00_declaracao_de_uso_de_ia_processo_pr_e_revisao_humana, especificacao_00_declaracao_de_uso_de_ia_contagens [EXTRACTED 1.00]
- **Conjunto Execução em solo do item 9 (inclui UC12 da área A e UC37 da área D)** — especificacao_09_diagrama_geral_de_casos_de_uso_agrupamento_por_funcao, especificacao_10_especificacoes_de_caso_de_uso_area_a_uc_a12, especificacao_10_especificacoes_de_caso_de_uso_area_d_uc_d9, especificacao_10_especificacoes_de_caso_de_uso_area_b_area_b [EXTRACTED 1.00]
- **Quatro vistas do diagrama de atividades (11.1–11.4)** — especificacao_diagramas_11_atividades, especificacao_diagramas_11_atividades_paralelas, especificacao_diagramas_11_registro_tarefa, especificacao_diagramas_11_monitoramento [EXTRACTED 1.00]
- **Five market similars compared in matrix 3.3** — pesquisa_similares_assaia_assaia_apronai_turnaroundcontrol, pesquisa_similares_inform_groundstar_inform_groundstar, pesquisa_similares_adb_safegate_adb_safegate_safedock_apron_manager, pesquisa_similares_veovo_veovo_acdm, pesquisa_similares_sita_sita_airport_management_cdm, pesquisa_similares_matriz_comparativa_capacidades_do_nucleo [EXTRACTED 1.00]
- **Project differentiators DF1-DF5** — pesquisa_similares_lacunas_e_diferencial_df1, pesquisa_similares_lacunas_e_diferencial_df2, pesquisa_similares_lacunas_e_diferencial_df3, pesquisa_similares_lacunas_e_diferencial_df4, pesquisa_similares_lacunas_e_diferencial_df5 [EXTRACTED 1.00]
- **Quatro atores operacionais do Aircraft Turnaround Orchestration System** — context_operador_de_solo_rampa, pesquisa_topicos_papeis_e_atores_coordenador_de_turnaround, context_autoridade_de_liberacao, context_motor_de_eventos [EXTRACTED 1.00]
- **Rastreabilidade (ADR-0012): decisão, script, Apêndice A e critérios K.13, C08.6 e C10.10** — docs_adr_0012_matriz_de_rastreabilidade, docs_adr_0012_matriz_de_rastreabilidade_d12_matriz_apendice_sem_tabelas_base, scripts_gerar_matriz_rastreabilidade, especificacao_apendice_a_matriz_de_rastreabilidade, especificacao_apendice_a_matriz_de_rastreabilidade_matriz_de_rastreabilidade [EXTRACTED 1.00]
- **Regra D11: mínimo sem máximo, IDs provisórios e renumeração no T12** — docs_adr_0011_minimo_por_integrante_e_numeracao_provisoria_d11_minimo_sem_maximo_numeracao_provisoria, docs_adr_0011_minimo_por_integrante_e_numeracao_provisoria_ids_provisorios_por_area, docs_adr_0011_minimo_por_integrante_e_numeracao_provisoria_renumeracao_unica_t12, entregas_ra1_tarefas_areas_funcionais_a_d, entregas_ra1_tarefas_t12_revisao_cruzada [EXTRACTED 1.00]
- **'Risco ao horario' trigger set (T8, T11, T12)** — pesquisa_impacto_impacto_por_item_risco_ao_horario, pesquisa_topicos_tolerancias_e_indicadores_tobt_mais_5_min, pesquisa_topicos_tolerancias_e_indicadores_t11_viabilidade_eibt_mttt, pesquisa_topicos_tolerancias_e_indicadores_t12_embarque_nao_iniciado [EXTRACTED 1.00]
- **Campos da Visão de Produto (cliente-alvo, categoria-segmento, benefício-chave, diferencial-chave, meta-valor)** — especificacao_03_visao_do_produto_cliente_alvo, especificacao_03_visao_do_produto_categoria_segmento, especificacao_03_visao_do_produto_beneficio_chave, especificacao_03_visao_do_produto_diferencial_chave, especificacao_03_visao_do_produto_meta_valor [EXTRACTED 1.00]
- **Problemas P1–P5 da Visão do Produto** — especificacao_03_visao_do_produto_p1, especificacao_03_visao_do_produto_p2, especificacao_03_visao_do_produto_p3, especificacao_03_visao_do_produto_p4, especificacao_03_visao_do_produto_p5 [EXTRACTED 1.00]
- **Cadeia RF → estória → caso de uso da conclusão de tarefa com marcos e propagação (RF-16, RF-20 e RF-21; US016, US020 e US021; UC16, UC20 e UC21)** — especificacao_06_requisitos_funcionais_area_b_rf_b3, especificacao_07_estorias_de_usuario_area_b_us_b3, especificacao_10_especificacoes_de_caso_de_uso_area_b_uc_b3, especificacao_06_requisitos_funcionais_area_b_rf_b7, especificacao_07_estorias_de_usuario_area_b_us_b7, especificacao_10_especificacoes_de_caso_de_uso_area_b_uc_b7, especificacao_06_requisitos_funcionais_area_b_rf_b8, especificacao_07_estorias_de_usuario_area_b_us_b8, especificacao_10_especificacoes_de_caso_de_uso_area_b_uc_b8 [INFERRED 0.85]
- **Cadeia RF → estória → caso de uso do replanejamento e do serviço sob demanda (RF-42, US042, UC35)** — especificacao_06_requisitos_funcionais_area_d_rf_d7, especificacao_07_estorias_de_usuario_area_d_us_d7, especificacao_10_especificacoes_de_caso_de_uso_area_d_uc_d7 [INFERRED 0.85]
- **Relatórios de verificação do RA1 (item 10, T11, T12) e mapa de renumeração** — entregas_ra1_item_10_verificacao, entregas_ra1_t11_verificacao, entregas_ra1_t12_verificacao, entregas_ra1_renumeracao [INFERRED 0.85]
- **Serviços sob demanda: pesquisa, ADR-0014 (D14), catálogo, opção D-1 e RF-D7** — pesquisa_topicos_servicos_sob_demanda, docs_adr_0014_servicos_sob_demanda, docs_adr_0014_servicos_sob_demanda_d14_servicos_sob_demanda, docs_adr_0014_servicos_sob_demanda_catalogo_de_servicos_sob_demanda, pesquisa_topicos_servicos_sob_demanda_opcao_a1_catalogo_no_modelo, pesquisa_topicos_servicos_sob_demanda_opcao_d1_incluir_tarefa_no_plano_em_andamento, especificacao_06_requisitos_funcionais_area_d_rf_d7 [INFERRED 0.85]
- **Cadeia de rastreabilidade RF, US, RNF, UC por area** — especificacao_06_requisitos_funcionais_00_item_item, especificacao_07_estorias_de_usuario_00_item_item, especificacao_08_requisitos_nao_funcionais_00_item_item, especificacao_09_diagrama_geral_de_casos_de_uso_item, especificacao_10_especificacoes_de_caso_de_uso_00_item_item [INFERRED 0.85]
- **Ciclo de vida da exceção e bloqueio da liberação (RF-36, RF-40, RF-39)** — especificacao_06_requisitos_funcionais_area_d_rf_d1, especificacao_06_requisitos_funcionais_area_d_rf_d5, especificacao_06_requisitos_funcionais_area_d_rf_d4 [INFERRED 0.95]
- **Reatribuição de tarefa entre operadores da mesma equipe (RF-37, RF-43)** — especificacao_06_requisitos_funcionais_area_d_rf_d2, especificacao_06_requisitos_funcionais_area_d_rf_d8 [INFERRED 0.95]
- **Quatro microsserviços da ADR-0015** — docs_adr_0015_divisao_em_microsservicos_cadastro_e_planejamento, docs_adr_0015_divisao_em_microsservicos_execucao_em_solo, docs_adr_0015_divisao_em_microsservicos_monitoramento, docs_adr_0015_divisao_em_microsservicos_excecoes_e_liberacao [EXTRACTED 1.00]
- **Marcos A-CDM gravados pela Execução em Solo** — docs_adr_0015_divisao_em_microsservicos_execucao_em_solo, context_aibt, context_acgt, context_asbt, context_aegt, context_aobt [EXTRACTED 1.00]
- **Cadeia de modelagem do RA2 (T00 -> T12 -> T13 -> T14)** — entregas_ra2_tarefas_t00_titulo_aro_e_troca_de_area, entregas_ra2_tarefas_t12_modelo_de_dados, entregas_ra2_tarefas_t13_diagrama_de_classes, entregas_ra2_tarefas_t14_diagramas_de_sequencia, entregas_ra2_tarefas_cadeia_mais_longa [EXTRACTED 1.00]

## Communities (30 total, 3 thin omitted)

### Community 0 - "Monitoramento: projeção, alertas, TOBT e objetivos 1 e 3"
Cohesion: 0.10
Nodes (101): ASBT (Início real do embarque), Metas do item 1 (80%, TOBT + 5 min, 5 s, 0 liberações indevidas), Motor de Eventos, MTTT (Tempo mínimo de turnaround), TOBT (Horário-alvo de prontidão), ADR-0001 — TOBT planejado + 5 min, Heathrow pontualidade "verde" (>=79%), ADR-0003 — Atualizar previsão na antecipação (+93 more)

### Community 1 - "Especificações por área, casos de uso, estórias e matriz"
Cohesion: 0.09
Nodes (92): A-CDM (Tomada de decisão colaborativa em aeroportos), Aircraft Turnaround Orchestration System, ADR-0010 — Administrador do Sistema, ator abstrato Usuário e equipe do operador como dado, ADR-0011 — Mínimo de 4 por integrante, sem máximo; numeração provisória por área, IDs provisórios por área (RF-A1…, US-A1… com o número do RF, RNF-A1…, UC-A1…), Renumeração única no início do T12 (script, áreas A, B, C, D; correspondência em entregas/ra1-renumeracao.md), ADR-0012 — Matriz de rastreabilidade como apêndice gerado; sem tabelas de base nos arquivos de área, Regras para o cruzamento: a estória traz o RF no título; o caso de uso cita os RFs que atende; o RNF cita os RFs a que se aplica (ID, faixa ou "todos os RFs") (+84 more)

### Community 2 - "Execução em solo: operador, estados e QR Code"
Cohesion: 0.09
Nodes (79): Administrador do Sistema, Estados da tarefa (Aguardando ... Concluída, Pausada, Não aplicável), Operador de Solo/Rampa, Usuário (ator abstrato), ADR-0007 — Dados do operador e QR Code, Diferencial DF5 (QR Code por assento/fileira/zona), Leitura de QR Code pelo celular, Objetivo 2: Sincronizar equipes, recursos e atividades paralelas (+71 more)

### Community 3 - "BPMN TO BE (item 4) e exportação dos diagramas"
Cohesion: 0.10
Nodes (57): Fluxo de trabalho 1.3: cada diagrama com a fonte editável versionada junto da imagem; BPMN do item 4 em BPMN 2.0 (.bpmn), Leitura do diagrama: caminho principal (abertura, viabilidade, AIBT, posicionar ponte ou escada e iniciar o atendimento, subprocesso "Executar as tarefas em solo", fechamento de portas, verificação de pendências, ARDT, AOBT), Leitura do diagrama: eventos e mensagens (chegada, autorização do ATC, marcos e eventos condicionais de desembarque/abastecimento concluído, temporizador TOBT − 15 min), Fontes editáveis do BPMN: 04-bpmn-to-be.bpmn (processo principal + vistas por subprocesso) e 04-bpmn-to-be-geral.bpmn (visão geral), Item 4 Mapeamento de Negócios (BPMN TO BE em vistas), Leitura do diagrama: subprocessos de evento (monitoramento a cada registro, tratamento de alerta de risco, atualização da previsão, checagem em TOBT − 15 min), em paralelo ao caminho principal, Leitura do diagrama: subprocesso "Executar as tarefas em solo" com as tarefas em paralelo conforme as dependências [20][22][29], Vistas do mesmo modelo BPMN: visão geral com tudo aberto + processo principal e uma vista por subprocesso (prioridade de leitura na tela) (+49 more)

### Community 4 - "Serviços sob demanda e replanejamento"
Cohesion: 0.13
Nodes (51): ADR-0014 — Serviços sob demanda: catálogo no modelo de tarefas, acionado pelo Coordenador de Turnaround, Catálogo de serviços sob demanda no modelo de tarefas (tarefas "sob demanda" com tipo de atividade, equipe e duração planejada; fora do plano até serem acionadas), Caminho critico, RF-4 — Criar modelos de tarefas por tipo de aeronave e serviço, com catálogo de tarefas "sob demanda" fora do plano até serem acionadas, RF-5 — Confirmar o plano inicial com responsável, início, fim e obrigatoriedade de cada tarefa (só antes de qualquer tarefa começar), RF-6 — Aplicar ao turnaround um modelo de tarefas compatível com a aeronave e o serviço (cópia das tarefas, do catálogo sob demanda, das dependências e dos pontos), RF-8 — Definir as dependências entre tarefas do modelo ou do plano inicial (recusa referências inválidas e ciclos), RF-42 — Replanejar: alterar a janela planejada ou as dependências das tarefas não iniciadas e acionar serviço sob demanda do catálogo, com recálculo da projeção de prontidão e do caminho crítico (+43 more)

### Community 5 - "Autoridade de Liberação, estados do turnaround, prontidão (ARDT) e exceções"
Cohesion: 0.13
Nodes (42): ARDT (Horário real de prontidão), Autoridade de Liberação, Estados do turnaround (Em solo ... Fora de bloco, Em exceção), ADR-0006 — Códigos de atraso tabela ANAC, IATA AHM 730, IATA AHM 732, ANAC Portaria nº 55/2026, RF-36 — Abrir exceção em um turnaround (tarefa afetada, código de atraso da ANAC, descrição), levando-o a "Em exceção" (+34 more)

### Community 6 - "Tarefas em solo no BPMN, abastecimento e paralelismo"
Cohesion: 0.16
Nodes (42): ADR-0005 — Abastecimento com passageiros configurável, EASA CAT.OP.MPA.195, ANAC RBAC 91.102(g), Correções da revisão independente: eventos condicionais no BPMN, propagação após replanejamento, loadsheet após embarque e bagagem, norma ISO/IEC no item 8, Leitura do diagrama: gateways com condição (viável?; abastecimento com passageiros permitido?; pendência ou exceção?; há desvio?), RF-11 — Configurar, por companhia, a permissão de abastecimento com passageiros (desabilitada por padrão), US011 — Configurar política de abastecimento (4 critérios de aceite), UC11 — Configurar política de abastecimento (+34 more)

### Community 7 - "Item 11, marcos (RF-20) e checagem dos diagramas"
Cohesion: 0.11
Nodes (41): AEGT (Fim real do atendimento em solo), T11 — Verificação do diagrama de atividades (#12), com anexo técnico das vistas, Diagrama de atividades: 17 decisões binárias, 1 seleção com 4 guardas, 2 laços, 4 partições, 4 nós iniciais e 7 finais, C11.1–C11.7 atendidos (fluxo principal, alternativos, guardas, fork/join, partições, notação, legibilidade), Item 11 de entrega só com título, subtítulos e imagens; explicações em anexo técnico interno, Fluxo de trabalho 1.3: casos de uso (item 9) e atividades (item 11) feitos no draw.io (.drawio) para controlar a posição de cada elemento; entregues em PlantUML no RA1 e refeitos depois da entrega, RF-20 — Registrar os marcos do atendimento em solo (ACGT, ASBT, AEGT) a partir dos registros dos operadores; AEGT = horário do registro que leva a última tarefa obrigatória pendente a "Concluída" ou "Não aplicável", US020 — Registrar os marcos do atendimento em solo (5 critérios de aceite) (+33 more)

### Community 8 - "Mapa da pesquisa: tópicos de base e ADRs"
Cohesion: 0.16
Nodes (28): ADR-0002 — Metas percentuais 80%, ADR-0004 — Quatro atores e Autoridade de Liberação, ADR-0008 — Siglas A-CDM com nome em português, ADR-0009 — Nome Coordenador de Turnaround, Impacto por item do template (4.2), BPMN TO BE inputs (events, gateways, lanes), E / Nao e / Faz / Nao faz candidates, 'Risco ao horario' defined by A-CDM triggers (T8, T11, T12) (+20 more)

### Community 9 - "Pesquisa, fontes e problemas do setor"
Cohesion: 0.15
Nodes (25): Categoria-segmento: software de gestão de turnaround / operações de solo, Diferencial-chave: grafo de tarefas com caminho crítico, bloqueio da liberação, registro pelo operador com QR Code, régua TOBT + 5 min, P3: atividades paralelas sem visão compartilhada; coordenação por rádio falha, P4: monitoramento automático exige câmeras/sensores e não registra quem executou, Fontes da pesquisa, ADB SAFEGATE - Apron Manager [49], ADB SAFEGATE - visual docking guidance press release [48], ADB SAFEGATE - Intelligent apron management [50] (+17 more)

### Community 10 - "Quadro É / Não é / Faz / Não faz"
Cohesion: 0.17
Nodes (15): Instrumento de apoio à decisão do Coordenador de Turnaround e da Autoridade de Liberação, Area B: Execucao de tarefas pelo operador, Area D: Replanejamento e liberacao, Bloqueio de liberacao com tarefa obrigatoria pendente ou excecao, Registro da causa de atraso/exceção com código da tabela da ANAC, Fora de escopo: malha aerea, slots, ATC, escalas, financeiro, visao computacional/sensores, Marcos do turnaround: in-block, início do atendimento, início do embarque, fim do atendimento, pronto para liberação, off-block, Não define o turnaround programado nem o MTTT (dados de entrada) (+7 more)

### Community 11 - "Similares de mercado e diferencial"
Cohesion: 0.24
Nodes (17): Ficha - ADB SAFEGATE, ADB SAFEGATE Safedock + Apron Manager, Ficha - Assaia, Ficha - INFORM GroundStar, INFORM GroundStar (TurnManager, TeamWork), Lacunas e diferencial possivel (3.4), Observed gaps in similar products, Matriz comparativa (3.3) (+9 more)

### Community 12 - "CONTEXT, AGENTS, README e critérios de aceite"
Cohesion: 0.22
Nodes (13): AGENTS.md - regras para assistentes de IA, Pendência cruzada entre áreas (rótulo pendencia-cruzada), CONTEXT.md - contexto do projeto, O que ler para cada item (tabela da seção 9), Checklist de consistência cruzada K.1 a K.13 (RA1), Critérios por item C01.1 a C11.7 e pesos da rubrica, Critérios de aceite do RA1 (itens 1 a 11), Critérios de aceite do RA2 (itens 12 a 15) (+5 more)

### Community 13 - "Chegada à posição (AIBT, ADR-0013)"
Cohesion: 0.42
Nodes (12): ADR-0013 — Chegada à posição registrada direto pelo operador, sem confirmação, Correção do AIBT pelo Coordenador de Turnaround (motivo, valor anterior e novo, autor e horário; até "Fora de bloco"; dispara o recálculo da projeção), Recusas do registro do AIBT (operador sem tarefa atribuída, horário futuro, chegada já registrada, plano inicial não confirmado), RF-12 — Registrar o AIBT e levar o turnaround a "Em solo" (sem confirmação), RF-13 — Corrigir o AIBT registrado, com motivo, enquanto o turnaround não estiver "Fora de bloco"; recalcula a projeção enquanto não estiver "Liberado", US012 — Registrar chegada à posição (6 critérios de aceite), US013 — Corrigir chegada à posição (6 critérios de aceite), UC12 — Registrar chegada à posição (+4 more)

### Community 14 - "Visão do Produto (item 3)"
Cohesion: 0.24
Nodes (13): Benefício-chave: aeronave pronta para liberação no TOBT, desvios tratados durante a operação, E1: desvios detectados durante a operação (projeção e caminho crítico recalculados, alerta ao Coordenador de Turnaround), E2: turnaround dentro do planejado, medido pela régua TOBT planejado + 5 min, E5: liberação bloqueada com tarefa obrigatória pendente ou exceção aberta; decisão registrada, Item 3 Visao do Produto, P1: desvios percebidos tarde e propagados (atraso reacionário 46%, 67,9% das partidas em até 15 min), P2: TOBT pouco confiável (menos de 60% de acerto em 5 min), P5: sem garantia formal de ausência de pendência na liberação (Aircraft Ready) (+5 more)

### Community 15 - "Contrato entre os serviços: mensageria e envelope"
Cohesion: 0.17
Nodes (11): AIBT (Horário real de chegada à posição), AOBT (Horário real de saída da posição), Aviso (evento) pela mensageria, Serviço Exceções e Liberação (RF-36 a RF-43), Serviço Execução em Solo (RF-12 a RF-21 e RF-44), Fluxo de liberação entre serviços (ARDT gravado com resposta positiva), Envelope comum dos avisos (id, tipo, versao, causaId, dados), Horários ISO 8601 em UTC (Z) (+3 more)

### Community 16 - "ADR-0015 e ADR-0016: quatro microsserviços"
Cohesion: 0.24
Nodes (12): Decisões vigentes D1 a D16, ADR-0015 Quatro microsserviços (D15), Serviço Cadastro e Planejamento (RF-1 a RF-11), Serviço Monitoramento (RF-22 a RF-35), Pedido (comando) com resposta em chamada direta, ADR-0016 Contrato comum entre os serviços (D16), Porta de entrada única (Spring Cloud Gateway), Login próprio no Cadastro (token emitido pelo Cadastro) (+4 more)

### Community 17 - "Caminho crítico e previsibilidade"
Cohesion: 0.21
Nodes (12): Protótipo UC-C2 — linha do tempo do turnaround (tela de computador), Protótipo UC23 — linha do tempo do turnaround, versão 2 (tela de computador), Planda & Skorupski 2025 - Aircraft Boarding Under Disturbances [21], Rodriguez-Sanz & Herrera 2020 - Turnaround time allocation RL [23], DF1 task graph with recalculated critical path and readiness projection, Caminho critico do turnaround (P1.6), Turnaround critical path, Boarding as critical activity (+4 more)

### Community 18 - "Gerador do documento final (gerar_docx.py)"
Cohesion: 0.38
Nodes (12): gerar_docx.py — monta o .docx final a partir do template do professor e dos Markdown de especificacao/, blocos() — converte Markdown em blocos (títulos, parágrafos, listas, imagens, tabelas), com caminhos de imagem resolvidos a partir do .md de origem, carregar() — carrega os arquivos de um item e aplica a regra do item, estorias() — item 7: cada estória vira uma tabela no formato do template, fontes_unidas() — junta as linhas "Fontes citadas" das áreas, larguras() — largura das colunas pelo conteúdo, como a tabela automática do HTML (palavra mais longa como mínimo, sobra para quem tem mais texto), ler() — lê o Markdown sem comentários HTML, main() — fluxo principal de gerar_docx.py (+4 more)

### Community 19 - "A-CDM, IATA e siglas"
Cohesion: 0.22
Nodes (8): Domain Docs, Usar o vocabulário do glossário do CONTEXT.md, Cliente-alvo: empresas de handling e companhias aéreas (responsáveis pelo TOBT), EUROCONTROL A-CDM concept page [1], IATA A-CDM Recommendations (2018) [5], A-CDM (Airport Collaborative Decision Making), GRU first A-CDM airport in Brazil (2020), 16 A-CDM milestones

### Community 20 - "Regras de escrita: grafo, checagem cruzada e siglas"
Cohesion: 0.25
Nodes (5): scripts/marcos_nos_diagramas.py, Regra dos 4 por integrante (mínimo 16), Regras gerais X.1 a X.10, Regras gerais Y.1 a Y.8, Grafo de conhecimento (graphify-out)

### Community 21 - "RA2: itens 13 e 14 (classes e sequência)"
Cohesion: 0.25
Nodes (8): ACGT (Início real do atendimento em solo), Camadas de referência Controller -> Service -> Repository, Convenção de nomes em português (PascalCase, camelCase, snake_case), Item 13 - Diagrama de classes (C13.1 a C13.10), Item 14 - Diagramas de sequência, 37 (C14.1 a C14.8), T02 Testar a ferramenta dos diagramas de sequência, T13 Diagrama de classes, T14 Diagramas de sequência (tarefa-mãe, 4 sub-issues)

### Community 22 - "RA2: item 12 e decisões B1 a B8"
Cohesion: 0.33
Nodes (6): Decisões do RA2 B1 a B8, B6: dicionário de dados no Apêndice B, Item 12 - Modelo de dados (C12.1 a C12.10), B5: matriz de rastreabilidade estendida aos itens 12 a 15, T03 Preparar estrutura, gerador e matriz, T12 Modelo de dados

### Community 23 - "Assaia e capacidades observadas"
Cohesion: 0.38
Nodes (7): Assaia case study - turnaround time reduction via alerts [42], Assaia - value of accurate off-block predictions [19], Observed capabilities by area A-D (RF inputs), Dependency alert: successor not started X min after predecessor, Assaia ApronAI / TurnaroundControl, Predicted off-block/ready time (POBT/PRDT), TurnManager impact propagation to dependent processes

### Community 24 - "IATA, RNFs e ISO/IEC 25010"
Cohesion: 0.48
Nodes (7): Insumos para os RNFs (4.4), Minute precision and rounding rule (5:59 vs 6:00), RNF requirements mapped to ISO/IEC 25010, Referencias da IATA sobre ground handling (P1.9), IATA Airport Handling Manual (AHM), IATA Ground Operations Manual (IGOM), ISAGO safety audit

### Community 25 - "RA2: ajustes do RA1 (T00, T01)"
Cohesion: 0.67
Nodes (4): Troca de área: RF-12, RF-13, RF-44 para a área B, Ajustes do RA1: título ARO dos RFs (C00.1 a C00.10), T00 Título ARO dos RFs e troca de área, T01 Sprints do item 6 pelas dependências entre RFs

### Community 26 - "RA2: fechamento (T16, T17)"
Cohesion: 0.67
Nodes (3): Checklist de consistência cruzada K.1 a K.12 (RA2), T16 Revisão cruzada e verificação independente, T17 Consolidar em PDF e enviar no Canvas

## Knowledge Gaps
- **31 isolated node(s):** `Heathrow pontualidade "verde" (>=79%)`, `Amadeus (excluded candidate)`, `Cosmos (excluded candidate)`, `Doc — documento com entradas do sumário a cada título de nível 1`, `Item 10: 37 especificações (A13, B8, C7, D9), 42 protótipos, 119 fluxos alternativos e 122 de exceção` (+26 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 36 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **3 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Fontes da pesquisa` connect `Pesquisa, fontes e problemas do setor` to `Monitoramento: projeção, alertas, TOBT e objetivos 1 e 3`, `Especificações por área, casos de uso, estórias e matriz`, `Execução em solo: operador, estados e QR Code`, `BPMN TO BE (item 4) e exportação dos diagramas`, `Serviços sob demanda e replanejamento`, `Autoridade de Liberação, estados do turnaround, prontidão (ARDT) e exceções`, `Tarefas em solo no BPMN, abastecimento e paralelismo`, `Item 11, marcos (RF-20) e checagem dos diagramas`, `Mapa da pesquisa: tópicos de base e ADRs`, `Quadro É / Não é / Faz / Não faz`, `Chegada à posição (AIBT, ADR-0013)`, `Visão do Produto (item 3)`, `Caminho crítico e previsibilidade`, `Gerador do documento final (gerar_docx.py)`, `A-CDM, IATA e siglas`, `Assaia e capacidades observadas`?**
  _High betweenness centrality (0.117) - this node is a cross-community bridge._
- **Why does `Coordenador de Turnaround` connect `Monitoramento: projeção, alertas, TOBT e objetivos 1 e 3` to `Especificações por área, casos de uso, estórias e matriz`, `Execução em solo: operador, estados e QR Code`, `BPMN TO BE (item 4) e exportação dos diagramas`, `Serviços sob demanda e replanejamento`, `Autoridade de Liberação, estados do turnaround, prontidão (ARDT) e exceções`, `Tarefas em solo no BPMN, abastecimento e paralelismo`, `Mapa da pesquisa: tópicos de base e ADRs`, `Pesquisa, fontes e problemas do setor`, `Quadro É / Não é / Faz / Não faz`, `Chegada à posição (AIBT, ADR-0013)`, `Visão do Produto (item 3)`, `Caminho crítico e previsibilidade`, `A-CDM, IATA e siglas`?**
  _High betweenness centrality (0.078) - this node is a cross-community bridge._
- **Why does `Item 4 Mapeamento de Negócios (BPMN TO BE em vistas)` connect `BPMN TO BE (item 4) e exportação dos diagramas` to `Monitoramento: projeção, alertas, TOBT e objetivos 1 e 3`, `Especificações por área, casos de uso, estórias e matriz`, `Execução em solo: operador, estados e QR Code`, `Serviços sob demanda e replanejamento`, `Autoridade de Liberação, estados do turnaround, prontidão (ARDT) e exceções`, `Tarefas em solo no BPMN, abastecimento e paralelismo`, `Item 11, marcos (RF-20) e checagem dos diagramas`, `Mapa da pesquisa: tópicos de base e ADRs`, `Pesquisa, fontes e problemas do setor`, `Chegada à posição (AIBT, ADR-0013)`, `Caminho crítico e previsibilidade`, `Gerador do documento final (gerar_docx.py)`?**
  _High betweenness centrality (0.069) - this node is a cross-community bridge._
- **Are the 30 inferred relationships involving `Coordenador de Turnaround` (e.g. with `Cliente-alvo: empresas de handling e companhias aéreas (responsáveis pelo TOBT)` and `E1: desvios detectados durante a operação (projeção e caminho crítico recalculados, alerta ao Coordenador de Turnaround)`) actually correct?**
  _`Coordenador de Turnaround` has 30 INFERRED edges - model-reasoned connections that need verification._
- **Are the 25 inferred relationships involving `Operador de Solo/Rampa` (e.g. with `Item 5 Relacao de Atores/Usuarios` and `Operador de Solo/Rampa (item 5)`) actually correct?**
  _`Operador de Solo/Rampa` has 25 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Heathrow pontualidade "verde" (>=79%)`, `Amadeus (excluded candidate)`, `Cosmos (excluded candidate)` to the rest of the system?**
  _31 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Monitoramento: projeção, alertas, TOBT e objetivos 1 e 3` be split into smaller, more focused modules?**
  _Cohesion score 0.09764749813293502 - nodes in this community are weakly interconnected._