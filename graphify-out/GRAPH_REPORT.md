# Graph Report - aircraft-turnaround-docs  (2026-10-06)

## Corpus Check
- 72 files · ~62,585 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 397 nodes · 1358 edges · 11 communities
- Extraction: 76% EXTRACTED · 24% INFERRED · 0% AMBIGUOUS · INFERRED: 324 edges (avg confidence: 0.89)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Decisões (ADRs) e fontes da pesquisa
- Regras para IAs, CONTEXT e README
- Área B: RFs, estórias, objetivos e estados
- Escopo, liberação e previsibilidade
- QR Code e registro pelo operador
- Visão do Produto e similares
- BPMN: eventos, desvios e subprocessos
- ADR-0011, áreas e modelos dos itens 6, 7, 8 e 10
- BPMN: tarefas de solo em paralelo
- Metas, régua do TOBT e risco ao horário
- Atores (item 5) e ADR-0010

## God Nodes (most connected - your core abstractions)
1. `Fontes da pesquisa` - 60 edges
2. `CONTEXT.md — Contexto do projeto` - 46 edges
3. `Pesquisa - mapa da base de conhecimento` - 35 edges
4. `Operador de Solo/Rampa` - 34 edges
5. `Item 4 Mapeamento de Negocios (BPMN to-be)` - 29 edges
6. `Operador de Solo/Rampa (lane do BPMN)` - 29 edges
7. `D11 — Mínimo de 4 por integrante, sem máximo; IDs provisórios por área e renumeração única no início do T12` - 29 edges
8. `Diferencial-chave: grafo de tarefas com caminho crítico, bloqueio da liberação, registro pelo operador com QR Code, régua TOBT + 5 min` - 27 edges
9. `README.md — aircraft-turnaround-docs` - 27 edges
10. `ADR-0010 — Administrador do Sistema, ator abstrato Usuário e equipe do operador como dado` - 24 edges

## Surprising Connections (you probably didn't know these)
- `Subprocesso de evento: Checagem em TOBT − 15 min` --conceptually_related_to--> `Ramp checkpoints TOBT-15 and TOBT-3`  [INFERRED]
  especificacao/diagramas/04-bpmn-to-be.png → pesquisa/topicos/atividades-e-dependencias.md
- `Limpar a cabine (confirmação por QR Code)` --conceptually_related_to--> `Task confirmation by QR Code on operator phone`  [INFERRED]
  especificacao/diagramas/04-bpmn-to-be.png → pesquisa/topicos/atividades-e-dependencias.md
- `Confirmar a prontidão e liberar a aeronave (ARDT)` --conceptually_related_to--> `Aircraft Ready (ARDT, milestone 12)`  [INFERRED]
  especificacao/diagramas/04-bpmn-to-be.png → pesquisa/topicos/marcos-e-horarios.md
- `Motor de Eventos` --semantically_similar_to--> `A-CDM System / information platform`  [INFERRED] [semantically similar]
  CONTEXT.md → pesquisa/topicos/papeis-e-atores.md
- `Propagar estados e recalcular projeção, caminho crítico e aderência ao TOBT + 5 min` --conceptually_related_to--> `ADR-0001 — TOBT planejado + 5 min`  [INFERRED]
  especificacao/diagramas/04-bpmn-to-be.png → docs/adr/0001-referencia-horario-tobt-mais-5-min.md

## Hyperedges (group relationships)
- **Cadeia RF → estória das ações de execução de tarefa do Operador de Solo/Rampa (RF-B2 a RF-B6, US-B2 a US-B6)** — especificacao_06_requisitos_funcionais_area_b_rf_b2, especificacao_06_requisitos_funcionais_area_b_rf_b3, especificacao_06_requisitos_funcionais_area_b_rf_b4, especificacao_06_requisitos_funcionais_area_b_rf_b5, especificacao_06_requisitos_funcionais_area_b_rf_b6, especificacao_07_estorias_de_usuario_area_b_us_b2, especificacao_07_estorias_de_usuario_area_b_us_b3, especificacao_07_estorias_de_usuario_area_b_us_b4, especificacao_07_estorias_de_usuario_area_b_us_b5, especificacao_07_estorias_de_usuario_area_b_us_b6 [EXTRACTED 1.00]
- **Requisitos funcionais da área B (RF-B1 a RF-B8)** — especificacao_06_requisitos_funcionais_area_b_rf_b1, especificacao_06_requisitos_funcionais_area_b_rf_b2, especificacao_06_requisitos_funcionais_area_b_rf_b3, especificacao_06_requisitos_funcionais_area_b_rf_b4, especificacao_06_requisitos_funcionais_area_b_rf_b5, especificacao_06_requisitos_funcionais_area_b_rf_b6, especificacao_06_requisitos_funcionais_area_b_rf_b7, especificacao_06_requisitos_funcionais_area_b_rf_b8 [EXTRACTED 1.00]
- **Requisitos não funcionais da área B (RNF-B1 a RNF-B4)** — especificacao_08_requisitos_nao_funcionais_area_b_rnf_b1, especificacao_08_requisitos_nao_funcionais_area_b_rnf_b2, especificacao_08_requisitos_nao_funcionais_area_b_rnf_b3, especificacao_08_requisitos_nao_funcionais_area_b_rnf_b4 [EXTRACTED 1.00]
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
- **Governança de consistência documental** — context_precedencia_adr_pesquisa, docs_agents_domain_flag_adr_conflicts, entregas_ra1_criterios_de_aceite_k11_consistencia_context_adr, entregas_ra1_criterios_de_aceite_protocolo_execucao_verificacao [INFERRED 0.85]
- **Cadeia de rastreabilidade RF, US, RNF, UC por area** — especificacao_06_requisitos_funcionais_00_item_item, especificacao_07_estorias_de_usuario_00_item_item, especificacao_08_requisitos_nao_funcionais_00_item_item, especificacao_09_diagrama_geral_de_casos_de_uso_item, especificacao_10_especificacoes_de_caso_de_uso_00_item_item [INFERRED 0.85]

## Communities (11 total, 0 thin omitted)

### Community 0 - "Decisões (ADRs) e fontes da pesquisa"
Cohesion: 0.09
Nodes (64): ADR-0001 — TOBT planejado + 5 min, ADR-0002 — Metas percentuais 80%, ADR-0003 — Atualizar previsão na antecipação, ADR-0004 — Quatro atores e Autoridade de Liberação, ADR-0005 — Abastecimento com passageiros configurável, EASA CAT.OP.MPA.195, ANAC RBAC 91.102(g), ADR-0006 — Códigos de atraso tabela ANAC (+56 more)

### Community 1 - "Regras para IAs, CONTEXT e README"
Cohesion: 0.10
Nodes (34): Formato de arquivo de pesquisa (YAML + seção Ligações), CONTEXT.md — Contexto do projeto, Administrador do Sistema, Tabela "O que ler para cada item", Usuário (ator abstrato), Domain Docs, Issue tracker: GitHub, GitHub Issues via gh CLI (+26 more)

### Community 2 - "Área B: RFs, estórias, objetivos e estados"
Cohesion: 0.13
Nodes (42): AEGT — Fim real do atendimento em solo, Estados da tarefa, Estados do turnaround, Motor de Eventos, Operador de Solo/Rampa, IATA AHM 730, IATA AHM 732, ANAC Portaria nº 55/2026 (+34 more)

### Community 3 - "Escopo, liberação e previsibilidade"
Cohesion: 0.08
Nodes (39): ARDT — Horário real de prontidão (Aircraft Ready), Autoridade de Liberação, Fora de escopo (voos, tripulação, financeiro, ATC), TSAT — Horário-alvo de autorização de acionamento, Aviso de antecipação >= 5 min, Usar o vocabulário do glossário do CONTEXT.md, Alerta de risco ao horario planejado, Liberacao da aeronave (+31 more)

### Community 4 - "QR Code e registro pelo operador"
Cohesion: 0.12
Nodes (36): ADR-0007 — Dados do operador e QR Code, Diferencial DF5 (QR Code por assento/fileira/zona), Leitura de QR Code pelo celular, Atualizacao por dispositivo movel / QR code, E4: andamento registrado pelo Operador de Solo/Rampa no celular, inclusive QR Code, sem infraestrutura no pátio, Confirmação da limpeza da cabine por leitura de QR Code no celular do operador, RF-B6 — Confirmar a execução ponto a ponto por leitura de QR Code no celular (só "Em execução"), Assaia case study - turnaround time reduction via alerts [42] (+28 more)

### Community 5 - "Visão do Produto e similares"
Cohesion: 0.10
Nodes (37): Caminho critico, Categoria-segmento: software de gestão de turnaround / operações de solo, Diferencial-chave: grafo de tarefas com caminho crítico, bloqueio da liberação, registro pelo operador com QR Code, régua TOBT + 5 min, Item 3 Visao do Produto, P1: desvios percebidos tarde e propagados (atraso reacionário 46%, 67,9% das partidas em até 15 min), P2: TOBT pouco confiável (menos de 60% de acerto em 5 min), P3: atividades paralelas sem visão compartilhada; coordenação por rádio falha, P4: monitoramento automático exige câmeras/sensores e não registra quem executou (+29 more)

### Community 6 - "BPMN: eventos, desvios e subprocessos"
Cohesion: 0.13
Nodes (32): Evento de mensagem: Autorização de acionamento e push-back recebida (do ATC), Evento de fim: Turnaround encerrado, Evento de início (mensagem): Voo previsto para a posição, Evento de início (mensagem, não interruptivo): Registro de andamento recebido (início, pausa, conclusão, não aplicável, QR Code), Evento de início (temporizador, não interruptivo): TOBT − 15 min, Gateway exclusivo: Há desvio? (Risco ao horário T8, T11, T12 / Antecipação ≥ 5 min / Não), Gateway exclusivo: Há tarefa obrigatória pendente ou exceção aberta? (Sim → tratar; Não → liberar), Gateway exclusivo: Turnaround viável? (Sim → aguarda AIBT; Não → ajustar o plano ou o TOBT) (+24 more)

### Community 7 - "ADR-0011, áreas e modelos dos itens 6, 7, 8 e 10"
Cohesion: 0.16
Nodes (29): Aircraft Turnaround Orchestration System, ADR-0011 — Mínimo de 4 por integrante, sem máximo; numeração provisória por área, IDs provisórios por área (RF-A1…, US-A1… com o número do RF, RNF-A1…, UC-A1…), Renumeração única no início do T12 (script, áreas A, B, C, D; correspondência em entregas/ra1-renumeracao.md), Area A: Abertura e configuracao do turnaround, Area C: Projecao, caminho critico, painel e alertas, Item 6 Requisitos Funcionais, Area A - Requisitos funcionais (RF-A1…, mínimo 4) (+21 more)

### Community 8 - "BPMN: tarefas de solo em paralelo"
Cohesion: 0.19
Nodes (25): Evento de mensagem: Aeronave em posição (AIBT), Gateway exclusivo (abastecimento): Abastecimento com passageiros permitido? (Sim → abastecer; Não → aguardar "Desembarque concluído"), Gateway exclusivo (embarque): Abastecimento com passageiros permitido? (Sim → embarcar; Não → aguardar "Abastecimento concluído"), Gateway paralelo: abertura das tarefas em paralelo após o ACGT, Gateway paralelo: junção de embarque e carregamento de bagagem e carga, Gateway paralelo: junção final das tarefas de solo, Gateway paralelo: junção de limpeza e catering, Gateway paralelo: limpeza da cabine e catering após o desembarque (+17 more)

### Community 9 - "Metas, régua do TOBT e risco ao horário"
Cohesion: 0.15
Nodes (20): Metas do item 1 (precisão, sincronização, desvios), MTTT — Tempo mínimo de turnaround, Risco ao horário (gatilhos A-CDM), TOBT — Horário-alvo de prontidão, Heathrow pontualidade "verde" (>=79%), Janela planejada, Metrica: 80% das atividades na janela e 80% dos turnarounds prontos ate o TOBT planejado (tolerancia 5 min), Benefício-chave: aeronave pronta para liberação no TOBT, desvios tratados durante a operação (+12 more)

### Community 10 - "Atores (item 5) e ADR-0010"
Cohesion: 0.44
Nodes (10): ADR-0010 — Administrador do Sistema, ator abstrato Usuário e equipe do operador como dado, Leitura do diagrama: pool e lanes (uma lane por ator; ATC como pool externo fechado), Administrador do Sistema (item 5), Autoridade de Liberação (item 5), Coordenador de Turnaround (item 5), Fora do sistema: ATC, tripulação e centro de operações do aeroporto não são atores, Item 5 Relacao de Atores/Usuarios, Motor de Eventos — ator não humano (item 5) (+2 more)

## Knowledge Gaps
- **10 isolated node(s):** `Amadeus (excluded candidate)`, `Cosmos (excluded candidate)`, `GRU first A-CDM airport in Brazil (2020)`, `Item 11 Diagrama de Atividades`, `Wayfinding (map issue + child tickets)` (+5 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 10 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Fontes da pesquisa` connect `Visão do Produto e similares` to `Decisões (ADRs) e fontes da pesquisa`, `Regras para IAs, CONTEXT e README`, `Área B: RFs, estórias, objetivos e estados`, `Escopo, liberação e previsibilidade`, `QR Code e registro pelo operador`, `Metas, régua do TOBT e risco ao horário`, `Atores (item 5) e ADR-0010`?**
  _High betweenness centrality (0.202) - this node is a cross-community bridge._
- **Why does `CONTEXT.md — Contexto do projeto` connect `Regras para IAs, CONTEXT e README` to `Decisões (ADRs) e fontes da pesquisa`, `Área B: RFs, estórias, objetivos e estados`, `Escopo, liberação e previsibilidade`, `QR Code e registro pelo operador`, `Visão do Produto e similares`, `ADR-0011, áreas e modelos dos itens 6, 7, 8 e 10`, `Metas, régua do TOBT e risco ao horário`, `Atores (item 5) e ADR-0010`?**
  _High betweenness centrality (0.155) - this node is a cross-community bridge._
- **Why does `Operador de Solo/Rampa (lane do BPMN)` connect `BPMN: tarefas de solo em paralelo` to `Área B: RFs, estórias, objetivos e estados`, `Atores (item 5) e ADR-0010`, `BPMN: eventos, desvios e subprocessos`?**
  _High betweenness centrality (0.096) - this node is a cross-community bridge._
- **Are the 8 inferred relationships involving `Operador de Solo/Rampa` (e.g. with `Equipe ou especialidade do operador como dado do cadastro (não um ator por especialidade)` and `Leitura de QR Code pelo celular`) actually correct?**
  _`Operador de Solo/Rampa` has 8 INFERRED edges - model-reasoned connections that need verification._
- **Are the 4 inferred relationships involving `Item 4 Mapeamento de Negocios (BPMN to-be)` (e.g. with `Aircraft Turnaround Orchestration System` and `Atividades, paralelismo e dependencias (P1.5)`) actually correct?**
  _`Item 4 Mapeamento de Negocios (BPMN to-be)` has 4 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Amadeus (excluded candidate)`, `Cosmos (excluded candidate)`, `GRU first A-CDM airport in Brazil (2020)` to the rest of the system?**
  _10 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Decisões (ADRs) e fontes da pesquisa` be split into smaller, more focused modules?**
  _Cohesion score 0.08846153846153847 - nodes in this community are weakly interconnected._