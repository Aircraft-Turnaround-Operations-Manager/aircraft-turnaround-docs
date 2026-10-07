# Graph Report - aircraft-turnaround-docs  (2026-10-06)

## Corpus Check
- 72 files · ~62,920 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 406 nodes · 1467 edges · 11 communities
- Extraction: 74% EXTRACTED · 26% INFERRED · 0% AMBIGUOUS · INFERRED: 377 edges (avg confidence: 0.89)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Decisões (ADRs), siglas e fontes
- Área D: exceções, liberação e estados do turnaround
- Atores, áreas e regras de quantidade
- Regras para IAs, CONTEXT e README
- QR Code, Visão do Produto e similares
- Área B: RFs, estórias e estados da tarefa
- Abastecimento, antecipação e leitura do BPMN
- BPMN: tarefas de solo e encerramento
- BPMN: eventos, desvios e atualização da previsão
- Previsibilidade, metas e régua do TOBT
- Fora de escopo

## God Nodes (most connected - your core abstractions)
1. `Fontes da pesquisa` - 61 edges
2. `CONTEXT.md — Contexto do projeto` - 46 edges
3. `Pesquisa - mapa da base de conhecimento` - 35 edges
4. `Operador de Solo/Rampa` - 35 edges
5. `Operador de Solo/Rampa (lane do BPMN)` - 30 edges
6. `Item 4 Mapeamento de Negocios (BPMN to-be)` - 29 edges
7. `D11 — Mínimo de 4 por integrante, sem máximo; IDs provisórios por área e renumeração única no início do T12` - 29 edges
8. `README.md — aircraft-turnaround-docs` - 27 edges
9. `Coordenador de Turnaround` - 27 edges
10. `Diferencial-chave: grafo de tarefas com caminho crítico, bloqueio da liberação, registro pelo operador com QR Code, régua TOBT + 5 min` - 27 edges

## Surprising Connections (you probably didn't know these)
- `Gateway exclusivo (abastecimento): Abastecimento com passageiros permitido? (Sim → abastecer; Não → aguardar "Desembarque concluído")` --conceptually_related_to--> `Refuelling with passengers on board (configurable rule)`  [INFERRED]
  especificacao/diagramas/04-bpmn-to-be.png → pesquisa/topicos/atividades-e-dependencias.md
- `Gateway paralelo: abertura das tarefas em paralelo após o ACGT` --conceptually_related_to--> `Turnaround activities A1-A13 with dependencies`  [INFERRED]
  especificacao/diagramas/04-bpmn-to-be.png → pesquisa/topicos/atividades-e-dependencias.md
- `Subprocesso de evento: Checagem em TOBT − 15 min` --conceptually_related_to--> `Ramp checkpoints TOBT-15 and TOBT-3`  [INFERRED]
  especificacao/diagramas/04-bpmn-to-be.png → pesquisa/topicos/atividades-e-dependencias.md
- `Propagar estados e recalcular projeção, caminho crítico e aderência ao TOBT + 5 min` --conceptually_related_to--> `Turnaround critical path`  [INFERRED]
  especificacao/diagramas/04-bpmn-to-be.png → pesquisa/topicos/caminho-critico.md
- `Embarcar os passageiros (ASBT)` --conceptually_related_to--> `Boarding as critical activity`  [INFERRED]
  especificacao/diagramas/04-bpmn-to-be.png → pesquisa/topicos/caminho-critico.md

## Hyperedges (group relationships)
- **Cadeia RF → estória das ações de execução de tarefa do Operador de Solo/Rampa (RF-B2 a RF-B6, US-B2 a US-B6)** — especificacao_06_requisitos_funcionais_area_b_rf_b2, especificacao_06_requisitos_funcionais_area_b_rf_b3, especificacao_06_requisitos_funcionais_area_b_rf_b4, especificacao_06_requisitos_funcionais_area_b_rf_b5, especificacao_06_requisitos_funcionais_area_b_rf_b6, especificacao_07_estorias_de_usuario_area_b_us_b2, especificacao_07_estorias_de_usuario_area_b_us_b3, especificacao_07_estorias_de_usuario_area_b_us_b4, especificacao_07_estorias_de_usuario_area_b_us_b5, especificacao_07_estorias_de_usuario_area_b_us_b6 [EXTRACTED 1.00]
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
- **Governança de consistência documental** — context_precedencia_adr_pesquisa, docs_agents_domain_flag_adr_conflicts, entregas_ra1_criterios_de_aceite_k11_consistencia_context_adr, entregas_ra1_criterios_de_aceite_protocolo_execucao_verificacao [INFERRED 0.85]
- **Cadeia de rastreabilidade RF, US, RNF, UC por area** — especificacao_06_requisitos_funcionais_00_item_item, especificacao_07_estorias_de_usuario_00_item_item, especificacao_08_requisitos_nao_funcionais_00_item_item, especificacao_09_diagrama_geral_de_casos_de_uso_item, especificacao_10_especificacoes_de_caso_de_uso_00_item_item [INFERRED 0.85]
- **Ciclo de vida da exceção e bloqueio da liberação (RF-D1, RF-D5, RF-D4)** — especificacao_06_requisitos_funcionais_area_d_rf_d1, especificacao_06_requisitos_funcionais_area_d_rf_d5, especificacao_06_requisitos_funcionais_area_d_rf_d4 [INFERRED 0.95]
- **Reatribuição de tarefa entre operadores da mesma equipe (RF-D2, RF-D8)** — especificacao_06_requisitos_funcionais_area_d_rf_d2, especificacao_06_requisitos_funcionais_area_d_rf_d8 [INFERRED 0.95]

## Communities (11 total, 0 thin omitted)

### Community 0 - "Decisões (ADRs), siglas e fontes"
Cohesion: 0.09
Nodes (55): ADR-0001 — TOBT planejado + 5 min, ADR-0006 — Códigos de atraso tabela ANAC, ADR-0008 — Siglas A-CDM com nome em português, ADR-0009 — Nome Coordenador de Turnaround, Usar o vocabulário do glossário do CONTEXT.md, IATA AHM 732 delay codes webinar [37], Impacto por item do template (4.2), E / Nao e / Faz / Nao faz candidates (+47 more)

### Community 1 - "Área D: exceções, liberação e estados do turnaround"
Cohesion: 0.11
Nodes (49): ARDT — Horário real de prontidão (Aircraft Ready), Autoridade de Liberação, Estados do turnaround, ADR-0004 — Quatro atores e Autoridade de Liberação, IATA AHM 730, IATA AHM 732, ANAC Portaria nº 55/2026, Alerta de risco ao horario planejado (+41 more)

### Community 2 - "Atores, áreas e regras de quantidade"
Cohesion: 0.10
Nodes (43): Administrador do Sistema, Aircraft Turnaround Orchestration System, Usuário (ator abstrato), ADR-0010 — Administrador do Sistema, ator abstrato Usuário e equipe do operador como dado, ADR-0011 — Mínimo de 4 por integrante, sem máximo; numeração provisória por área, IDs provisórios por área (RF-A1…, US-A1… com o número do RF, RNF-A1…, UC-A1…), Renumeração única no início do T12 (script, áreas A, B, C, D; correspondência em entregas/ra1-renumeracao.md), K.1 — Atores com nomes idênticos (+35 more)

### Community 3 - "Regras para IAs, CONTEXT e README"
Cohesion: 0.10
Nodes (35): Formato de arquivo de pesquisa (YAML + seção Ligações), CONTEXT.md — Contexto do projeto, Metas do item 1 (precisão, sincronização, desvios), MTTT — Tempo mínimo de turnaround, Tabela "O que ler para cada item", Risco ao horário (gatilhos A-CDM), TOBT — Horário-alvo de prontidão, Índice de decisões (ADRs) (+27 more)

### Community 4 - "QR Code, Visão do Produto e similares"
Cohesion: 0.10
Nodes (44): ADR-0007 — Dados do operador e QR Code, Diferencial DF5 (QR Code por assento/fileira/zona), Leitura de QR Code pelo celular, Atualizacao por dispositivo movel / QR code, Categoria-segmento: software de gestão de turnaround / operações de solo, Diferencial-chave: grafo de tarefas com caminho crítico, bloqueio da liberação, registro pelo operador com QR Code, régua TOBT + 5 min, E4: andamento registrado pelo Operador de Solo/Rampa no celular, inclusive QR Code, sem infraestrutura no pátio, Item 3 Visao do Produto (+36 more)

### Community 5 - "Área B: RFs, estórias e estados da tarefa"
Cohesion: 0.17
Nodes (35): AEGT — Fim real do atendimento em solo, Estados da tarefa, Motor de Eventos, Operador de Solo/Rampa, Metrica: 100% tarefas com responsavel, painel atualizado em ate 5 s, Objetivo 2: Sincronizar equipes, recursos e atividades paralelas, Painel operacional, Area B: Execucao de tarefas pelo operador (+27 more)

### Community 6 - "Abastecimento, antecipação e leitura do BPMN"
Cohesion: 0.13
Nodes (33): ADR-0003 — Atualizar previsão na antecipação, ADR-0005 — Abastecimento com passageiros configurável, EASA CAT.OP.MPA.195, ANAC RBAC 91.102(g), Fluxo de trabalho 1.3: diagramas em Mermaid/PlantUML, exceto o BPMN do item 4 em BPMN 2.0 (.bpmn), Leitura do diagrama: caminho principal (abertura, viabilidade, AIBT, ACGT, tarefas em paralelo, ASBT, loadsheet, AEGT, ARDT, AOBT), Leitura do diagrama: eventos e mensagens (chegada, autorização do ATC, sinais de desembarque/abastecimento concluído, temporizador TOBT − 15 min), Leitura do diagrama: gateways com condição (viável?; abastecimento com passageiros permitido?; pendência ou exceção?; há desvio?) (+25 more)

### Community 7 - "BPMN: tarefas de solo e encerramento"
Cohesion: 0.15
Nodes (30): RF-D9 — Registrar o AOBT de um turnaround "Liberado" e encerrá-lo em "Fora de bloco", mantendo o histórico, Evento de mensagem: Aeronave em posição (AIBT), Evento de mensagem: Autorização de acionamento e push-back recebida (do ATC), Evento de fim: Turnaround encerrado, Gateway exclusivo (abastecimento): Abastecimento com passageiros permitido? (Sim → abastecer; Não → aguardar "Desembarque concluído"), Gateway exclusivo (embarque): Abastecimento com passageiros permitido? (Sim → embarcar; Não → aguardar "Abastecimento concluído"), Gateway paralelo: abertura das tarefas em paralelo após o ACGT, Gateway paralelo: junção de embarque e carregamento de bagagem e carga (+22 more)

### Community 8 - "BPMN: eventos, desvios e atualização da previsão"
Cohesion: 0.15
Nodes (27): Aviso de antecipação >= 5 min, RF-D6 — Solicitar a atualização do TOBT quando a projeção de prontidão se afastar 5 min ou mais, para mais ou para menos, Evento de início (mensagem): Voo previsto para a posição, Evento de início (mensagem, não interruptivo): Registro de andamento recebido (início, pausa, conclusão, não aplicável, QR Code), Evento de início (temporizador, não interruptivo): TOBT − 15 min, Gateway exclusivo: Há desvio? (Risco ao horário T8, T11, T12 / Antecipação ≥ 5 min / Não), Gateway exclusivo: Há tarefa obrigatória pendente ou exceção aberta? (Sim → tratar; Não → liberar), Gateway exclusivo: Turnaround viável? (Sim → aguarda AIBT; Não → ajustar o plano ou o TOBT) (+19 more)

### Community 9 - "Previsibilidade, metas e régua do TOBT"
Cohesion: 0.19
Nodes (13): ADR-0002 — Metas percentuais 80%, Heathrow pontualidade "verde" (>=79%), Janela planejada, Metrica: 80% das atividades na janela e 80% dos turnarounds prontos ate o TOBT planejado (tolerancia 5 min), Objetivo 1: Assegurar a precisao temporal do turnaround, Quadro 3 Objetivos, Benefício-chave: aeronave pronta para liberação no TOBT, desvios tratados durante a operação, E2: turnaround dentro do planejado, medido pela régua TOBT planejado + 5 min (+5 more)

### Community 10 - "Fora de escopo"
Cohesion: 0.21
Nodes (13): Fora de escopo (voos, tripulação, financeiro, ATC), TSAT — Horário-alvo de autorização de acionamento, Fora de escopo: malha aerea, slots, ATC, escalas, financeiro, visao computacional/sensores, Não define o turnaround programado nem o MTTT (dados de entrada), Não é A-CDM completo, sequenciador de partidas (TSAT) nem AODB, Cliente-alvo: empresas de handling e companhias aéreas (responsáveis pelo TOBT), Pool externo: Controle de tráfego aéreo (ATC) — fora do escopo, Airport CDM Implementation Manual v5.0 (ACI/EUROCONTROL/IATA) [4] (+5 more)

## Knowledge Gaps
- **10 isolated node(s):** `EASA CAT.OP.MPA.195`, `ANAC RBAC 91.102(g)`, `Wayfinding (map issue + child tickets)`, `Dependências e ordem de execução dos itens`, `IATA AHM 732` (+5 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 10 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Fontes da pesquisa` connect `QR Code, Visão do Produto e similares` to `Decisões (ADRs), siglas e fontes`, `Área D: exceções, liberação e estados do turnaround`, `Atores, áreas e regras de quantidade`, `Regras para IAs, CONTEXT e README`, `Área B: RFs, estórias e estados da tarefa`, `Abastecimento, antecipação e leitura do BPMN`, `BPMN: eventos, desvios e atualização da previsão`, `Previsibilidade, metas e régua do TOBT`, `Fora de escopo`?**
  _High betweenness centrality (0.197) - this node is a cross-community bridge._
- **Why does `CONTEXT.md — Contexto do projeto` connect `Regras para IAs, CONTEXT e README` to `Decisões (ADRs), siglas e fontes`, `Área D: exceções, liberação e estados do turnaround`, `Atores, áreas e regras de quantidade`, `QR Code, Visão do Produto e similares`, `Área B: RFs, estórias e estados da tarefa`, `Abastecimento, antecipação e leitura do BPMN`, `Previsibilidade, metas e régua do TOBT`, `Fora de escopo`?**
  _High betweenness centrality (0.142) - this node is a cross-community bridge._
- **Why does `Operador de Solo/Rampa (lane do BPMN)` connect `BPMN: tarefas de solo e encerramento` to `BPMN: eventos, desvios e atualização da previsão`, `Atores, áreas e regras de quantidade`, `Área B: RFs, estórias e estados da tarefa`?**
  _High betweenness centrality (0.092) - this node is a cross-community bridge._
- **Are the 8 inferred relationships involving `Operador de Solo/Rampa` (e.g. with `Equipe ou especialidade do operador como dado do cadastro (não um ator por especialidade)` and `Leitura de QR Code pelo celular`) actually correct?**
  _`Operador de Solo/Rampa` has 8 INFERRED edges - model-reasoned connections that need verification._
- **Are the 3 inferred relationships involving `Operador de Solo/Rampa (lane do BPMN)` (e.g. with `RF-D9 — Registrar o AOBT de um turnaround "Liberado" e encerrá-lo em "Fora de bloco", mantendo o histórico` and `Operador de Solo/Rampa`) actually correct?**
  _`Operador de Solo/Rampa (lane do BPMN)` has 3 INFERRED edges - model-reasoned connections that need verification._
- **What connects `EASA CAT.OP.MPA.195`, `ANAC RBAC 91.102(g)`, `Wayfinding (map issue + child tickets)` to the rest of the system?**
  _10 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Decisões (ADRs), siglas e fontes` be split into smaller, more focused modules?**
  _Cohesion score 0.08766233766233766 - nodes in this community are weakly interconnected._