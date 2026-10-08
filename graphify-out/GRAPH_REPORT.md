# Graph Report - aircraft-turnaround-docs  (2026-10-07)

## Corpus Check
- 75 files · ~73,743 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 5 file(s) not represented in the graph (top: (none) 4, .bpmn 1)

## Summary
- 440 nodes · 1753 edges · 9 communities
- Extraction: 74% EXTRACTED · 26% INFERRED · 0% AMBIGUOUS · INFERRED: 449 edges (avg confidence: 0.89)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `b71e4a26`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Regras para IAs, README, plano, critérios e rastreabilidade
- Pesquisa do setor, decisões e marcos do A-CDM
- Área B: RFs, estórias, casos de uso e RNFs
- Visão do Produto, similares e fontes
- Área D: exceções, liberação, RNFs e objetivo 3
- BPMN: Motor de Eventos, monitoramento e alertas
- BPMN: tarefas de solo e abastecimento
- Atores do item 5 e fora de escopo
- Confirmação por QR Code

## God Nodes (most connected - your core abstractions)
1. `Fontes da pesquisa` - 62 edges
2. `CONTEXT.md — Contexto do projeto` - 52 edges
3. `Operador de Solo/Rampa` - 42 edges
4. `Pesquisa - mapa da base de conhecimento` - 35 edges
5. `Operador de Solo/Rampa (lane do BPMN)` - 31 edges
6. `ADR-0012 — Matriz de rastreabilidade como apêndice gerado; sem tabelas de base nos arquivos de área` - 31 edges
7. `D11 — Mínimo de 4 por integrante, sem máximo; IDs provisórios por área e renumeração única no início do T12` - 30 edges
8. `EUROCONTROL Specification for A-CDM Ed. 1.0 (2025) [2]` - 30 edges
9. `Item 4 Mapeamento de Negocios (BPMN to-be)` - 29 edges
10. `README.md — aircraft-turnaround-docs` - 29 edges

## Surprising Connections (you probably didn't know these)
- `Pool externo: Controle de tráfego aéreo (ATC) — fora do escopo` --semantically_similar_to--> `ATC — Controle de tráfego aéreo (fora de escopo)`  [INFERRED] [semantically similar]
  especificacao/diagramas/04-bpmn-to-be.png → CONTEXT.md
- `Sinalizar conflitos com ADRs` --semantically_similar_to--> `Precedência: ADRs > pesquisa > rascunhos`  [INFERRED] [semantically similar]
  docs/agents/domain.md → CONTEXT.md
- `Refuelling with passengers on board (configurable rule)` --conceptually_related_to--> `Gateway exclusivo (abastecimento): Abastecimento com passageiros permitido? (Sim → abastecer; Não → aguardar "Desembarque concluído")`  [INFERRED]
  pesquisa/topicos/atividades-e-dependencias.md → especificacao/diagramas/04-bpmn-to-be.png
- `Turnaround activities A1-A13 with dependencies` --conceptually_related_to--> `Gateway paralelo: abertura das tarefas em paralelo após o ACGT`  [INFERRED]
  pesquisa/topicos/atividades-e-dependencias.md → especificacao/diagramas/04-bpmn-to-be.png
- `Ramp checkpoints TOBT-15 and TOBT-3` --conceptually_related_to--> `Subprocesso de evento: Checagem em TOBT − 15 min`  [INFERRED]
  pesquisa/topicos/atividades-e-dependencias.md → especificacao/diagramas/04-bpmn-to-be.png

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Cadeia RF → estória das ações de execução de tarefa do Operador de Solo/Rampa (RF-B2 a RF-B6, US-B2 a US-B6)** — especificacao_06_requisitos_funcionais_area_b_rf_b2, especificacao_06_requisitos_funcionais_area_b_rf_b3, especificacao_06_requisitos_funcionais_area_b_rf_b4, especificacao_06_requisitos_funcionais_area_b_rf_b5, especificacao_06_requisitos_funcionais_area_b_rf_b6, especificacao_07_estorias_de_usuario_area_b_us_b2, especificacao_07_estorias_de_usuario_area_b_us_b3, especificacao_07_estorias_de_usuario_area_b_us_b4, especificacao_07_estorias_de_usuario_area_b_us_b5, especificacao_07_estorias_de_usuario_area_b_us_b6 [EXTRACTED 1.00]
- **Casos de uso da área B (UC-B1 a UC-B8)** — especificacao_10_especificacoes_de_caso_de_uso_area_b_uc_b1, especificacao_10_especificacoes_de_caso_de_uso_area_b_uc_b2, especificacao_10_especificacoes_de_caso_de_uso_area_b_uc_b3, especificacao_10_especificacoes_de_caso_de_uso_area_b_uc_b4, especificacao_10_especificacoes_de_caso_de_uso_area_b_uc_b5, especificacao_10_especificacoes_de_caso_de_uso_area_b_uc_b6, especificacao_10_especificacoes_de_caso_de_uso_area_b_uc_b7, especificacao_10_especificacoes_de_caso_de_uso_area_b_uc_b8 [EXTRACTED 1.00]
- **«include»: UC-B2, UC-B3 e UC-B5 incluem UC-B7 (marcos) e UC-B8 (propagação), executados pelo Motor de Eventos** — especificacao_10_especificacoes_de_caso_de_uso_area_b_uc_b2, especificacao_10_especificacoes_de_caso_de_uso_area_b_uc_b3, especificacao_10_especificacoes_de_caso_de_uso_area_b_uc_b5, especificacao_10_especificacoes_de_caso_de_uso_area_b_uc_b7, especificacao_10_especificacoes_de_caso_de_uso_area_b_uc_b8, context_motor_de_eventos [EXTRACTED 1.00]
- **Requisitos funcionais da área B (RF-B1 a RF-B8)** — especificacao_06_requisitos_funcionais_area_b_rf_b1, especificacao_06_requisitos_funcionais_area_b_rf_b2, especificacao_06_requisitos_funcionais_area_b_rf_b3, especificacao_06_requisitos_funcionais_area_b_rf_b4, especificacao_06_requisitos_funcionais_area_b_rf_b5, especificacao_06_requisitos_funcionais_area_b_rf_b6, especificacao_06_requisitos_funcionais_area_b_rf_b7, especificacao_06_requisitos_funcionais_area_b_rf_b8 [EXTRACTED 1.00]
- **Requisitos não funcionais da área B (RNF-B1 a RNF-B4)** — especificacao_08_requisitos_nao_funcionais_area_b_rnf_b1, especificacao_08_requisitos_nao_funcionais_area_b_rnf_b2, especificacao_08_requisitos_nao_funcionais_area_b_rnf_b3, especificacao_08_requisitos_nao_funcionais_area_b_rnf_b4 [EXTRACTED 1.00]
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
- **Governança de consistência documental** — context_precedencia_adr_pesquisa, docs_agents_domain_flag_adr_conflicts, entregas_ra1_criterios_de_aceite_k11_consistencia_context_adr, entregas_ra1_criterios_de_aceite_protocolo_execucao_verificacao [INFERRED 0.85]
- **Cadeia de rastreabilidade RF, US, RNF, UC por area** — especificacao_06_requisitos_funcionais_00_item_item, especificacao_07_estorias_de_usuario_00_item_item, especificacao_08_requisitos_nao_funcionais_00_item_item, especificacao_09_diagrama_geral_de_casos_de_uso_item, especificacao_10_especificacoes_de_caso_de_uso_00_item_item [INFERRED 0.85]
- **Ciclo de vida da exceção e bloqueio da liberação (RF-D1, RF-D5, RF-D4)** — especificacao_06_requisitos_funcionais_area_d_rf_d1, especificacao_06_requisitos_funcionais_area_d_rf_d5, especificacao_06_requisitos_funcionais_area_d_rf_d4 [INFERRED 0.95]
- **Reatribuição de tarefa entre operadores da mesma equipe (RF-D2, RF-D8)** — especificacao_06_requisitos_funcionais_area_d_rf_d2, especificacao_06_requisitos_funcionais_area_d_rf_d8 [INFERRED 0.95]

## Communities (9 total, 0 thin omitted)

### Community 0 - "Regras para IAs, README, plano, critérios e rastreabilidade"
Cohesion: 0.07
Nodes (77): Formato de arquivo de pesquisa (YAML + seção Ligações), AGENTS.md regra 8 — registrar a suposição sobre outra área em vez de inventar o requisito, AGENTS.md regra 9 — toda sigla com o nome em português na primeira ocorrência de cada item (inclusive A-CDM, ANAC, ISO/IEC), CONTEXT.md — Contexto do projeto, A-CDM — Tomada de decisão colaborativa em aeroportos, Aircraft Turnaround Orchestration System, IATA — Associação Internacional de Transporte Aéreo, MTTT — Tempo mínimo de turnaround (+69 more)

### Community 1 - "Pesquisa do setor, decisões e marcos do A-CDM"
Cohesion: 0.08
Nodes (71): ADR-0001 — TOBT planejado + 5 min, ADR-0002 — Metas percentuais 80%, ADR-0003 — Atualizar previsão na antecipação, ADR-0004 — Quatro atores e Autoridade de Liberação, ADR-0005 — Abastecimento com passageiros configurável, ADR-0006 — Códigos de atraso tabela ANAC, ADR-0009 — Nome Coordenador de Turnaround, Fluxo de trabalho 1.3: diagramas em Mermaid/PlantUML, exceto o BPMN do item 4 em BPMN 2.0 (.bpmn) (+63 more)

### Community 2 - "Área B: RFs, estórias, casos de uso e RNFs"
Cohesion: 0.10
Nodes (65): AEGT — Fim real do atendimento em solo, Estados da tarefa, Estados do turnaround, Motor de Eventos, Operador de Solo/Rampa, EASA CAT.OP.MPA.195, ANAC RBAC 91.102(g), IATA AHM 730 (+57 more)

### Community 3 - "Visão do Produto, similares e fontes"
Cohesion: 0.07
Nodes (61): Categoria-segmento: software de gestão de turnaround / operações de solo, Diferencial-chave: grafo de tarefas com caminho crítico, bloqueio da liberação, registro pelo operador com QR Code, régua TOBT + 5 min, Item 3 Visao do Produto, P1: desvios percebidos tarde e propagados (atraso reacionário 46%, 67,9% das partidas em até 15 min), P2: TOBT pouco confiável (menos de 60% de acerto em 5 min), P3: atividades paralelas sem visão compartilhada; coordenação por rádio falha, P4: monitoramento automático exige câmeras/sensores e não registra quem executou, Fontes da pesquisa (+53 more)

### Community 4 - "Área D: exceções, liberação, RNFs e objetivo 3"
Cohesion: 0.12
Nodes (50): ARDT — Horário real de prontidão (Aircraft Ready), Autoridade de Liberação, Metas do item 1 (precisão, sincronização, desvios), TOBT — Horário-alvo de prontidão, Heathrow pontualidade "verde" (>=79%), Aviso de antecipação >= 5 min, Alerta de risco ao horario planejado, Caminho critico (+42 more)

### Community 5 - "BPMN: Motor de Eventos, monitoramento e alertas"
Cohesion: 0.16
Nodes (27): Evento de fim: Turnaround encerrado, Evento de início (mensagem): Voo previsto para a posição, Evento de início (mensagem, não interruptivo): Registro de andamento recebido (início, pausa, conclusão, não aplicável, QR Code), Evento de início (temporizador, não interruptivo): TOBT − 15 min, Gateway exclusivo: Há desvio? (Risco ao horário T8, T11, T12 / Antecipação ≥ 5 min / Não), Gateway exclusivo: Há tarefa obrigatória pendente ou exceção aberta? (Sim → tratar; Não → liberar), Gateway exclusivo: Turnaround viável? (Sim → aguarda AIBT; Não → ajustar o plano ou o TOBT), Coordenador de Turnaround (lane do BPMN) (+19 more)

### Community 6 - "BPMN: tarefas de solo e abastecimento"
Cohesion: 0.19
Nodes (24): Evento de mensagem: Aeronave em posição (AIBT), Gateway exclusivo (abastecimento): Abastecimento com passageiros permitido? (Sim → abastecer; Não → aguardar "Desembarque concluído"), Gateway exclusivo (embarque): Abastecimento com passageiros permitido? (Sim → embarcar; Não → aguardar "Abastecimento concluído"), Gateway paralelo: abertura das tarefas em paralelo após o ACGT, Gateway paralelo: junção de embarque e carregamento de bagagem e carga, Gateway paralelo: junção final das tarefas de solo, Gateway paralelo: junção de limpeza e catering, Gateway paralelo: limpeza da cabine e catering após o desembarque (+16 more)

### Community 7 - "Atores do item 5 e fora de escopo"
Cohesion: 0.18
Nodes (19): Administrador do Sistema, ATC — Controle de tráfego aéreo (fora de escopo), Fora de escopo (voos, tripulação, financeiro, ATC), TSAT — Horário-alvo de autorização de acionamento, Usuário (ator abstrato), K.1 — Atores com nomes idênticos, Leitura do diagrama: pool e lanes (uma lane por ator; ATC como pool externo fechado), Administrador do Sistema (item 5) (+11 more)

### Community 8 - "Confirmação por QR Code"
Cohesion: 0.30
Nodes (16): ADR-0007 — Dados do operador e QR Code, Diferencial DF5 (QR Code por assento/fileira/zona), Leitura de QR Code pelo celular, Atualizacao por dispositivo movel / QR code, E4: andamento registrado pelo Operador de Solo/Rampa no celular, inclusive QR Code, sem infraestrutura no pátio, Confirmação da limpeza da cabine por leitura de QR Code no celular do operador, RF-B6 — Confirmar a execução ponto a ponto por leitura de QR Code no celular (só "Em execução"), RNF-B3 — Telas do operador, com leitura de QR Code, em Chrome/Android 10+ e Safari/iOS 16+, 360 a 430 px (Portabilidade: adaptabilidade) (+8 more)

## Knowledge Gaps
- **9 isolated node(s):** `Wayfinding (map issue + child tickets)`, `Item 11 Diagrama de Atividades`, `IATA AHM 732`, `GRU first A-CDM airport in Brazil (2020)`, `EASA CAT.OP.MPA.195` (+4 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 9 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Fontes da pesquisa` connect `Visão do Produto, similares e fontes` to `Regras para IAs, README, plano, critérios e rastreabilidade`, `Pesquisa do setor, decisões e marcos do A-CDM`, `Área B: RFs, estórias, casos de uso e RNFs`, `Atores do item 5 e fora de escopo`, `Confirmação por QR Code`?**
  _High betweenness centrality (0.190) - this node is a cross-community bridge._
- **Why does `CONTEXT.md — Contexto do projeto` connect `Regras para IAs, README, plano, critérios e rastreabilidade` to `Pesquisa do setor, decisões e marcos do A-CDM`, `Área B: RFs, estórias, casos de uso e RNFs`, `Visão do Produto, similares e fontes`, `Área D: exceções, liberação, RNFs e objetivo 3`, `Atores do item 5 e fora de escopo`, `Confirmação por QR Code`?**
  _High betweenness centrality (0.155) - this node is a cross-community bridge._
- **Why does `Pesquisa - mapa da base de conhecimento` connect `Pesquisa do setor, decisões e marcos do A-CDM` to `Regras para IAs, README, plano, critérios e rastreabilidade`, `Confirmação por QR Code`, `Visão do Produto, similares e fontes`, `Atores do item 5 e fora de escopo`?**
  _High betweenness centrality (0.080) - this node is a cross-community bridge._
- **Are the 8 inferred relationships involving `Operador de Solo/Rampa` (e.g. with `K.1 — Atores com nomes idênticos` and `Leitura de QR Code pelo celular`) actually correct?**
  _`Operador de Solo/Rampa` has 8 INFERRED edges - model-reasoned connections that need verification._
- **Are the 4 inferred relationships involving `Operador de Solo/Rampa (lane do BPMN)` (e.g. with `Operador de Solo/Rampa` and `Operador de Solo/Rampa (item 5)`) actually correct?**
  _`Operador de Solo/Rampa (lane do BPMN)` has 4 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Wayfinding (map issue + child tickets)`, `Item 11 Diagrama de Atividades`, `IATA AHM 732` to the rest of the system?**
  _9 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Regras para IAs, README, plano, critérios e rastreabilidade` be split into smaller, more focused modules?**
  _Cohesion score 0.06895745675549322 - nodes in this community are weakly interconnected._