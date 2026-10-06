# Graph Report - aircraft-turnaround-docs  (2026-10-05)

## Corpus Check
- 72 files · ~58,894 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 377 nodes · 1204 edges · 9 communities (8 shown, 1 thin omitted)
- Extraction: 77% EXTRACTED · 23% INFERRED · 0% AMBIGUOUS · INFERRED: 279 edges (avg confidence: 0.89)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Decisões (ADRs) e fontes da pesquisa
- Contexto: atores, estados e produto
- QR Code, Visão do Produto e similares
- Regras para IAs, README e precedência
- ADR-0011, áreas e modelos dos itens 6, 7, 8 e 10
- Metas, régua do TOBT e risco ao horário
- BPMN: eventos, desvios e subprocessos
- BPMN: tarefas de solo em paralelo
- Abastecimento com passageiros

## God Nodes (most connected - your core abstractions)
1. `Fontes da pesquisa` - 60 edges
2. `CONTEXT.md — Contexto do projeto` - 46 edges
3. `Pesquisa - mapa da base de conhecimento` - 35 edges
4. `Item 4 Mapeamento de Negocios (BPMN to-be)` - 29 edges
5. `Operador de Solo/Rampa (lane do BPMN)` - 29 edges
6. `D11 — Mínimo de 4 por integrante, sem máximo; IDs provisórios por área e renumeração única no início do T12` - 29 edges
7. `Diferencial-chave: grafo de tarefas com caminho crítico, bloqueio da liberação, registro pelo operador com QR Code, régua TOBT + 5 min` - 27 edges
8. `README.md — aircraft-turnaround-docs` - 27 edges
9. `ADR-0010 — Administrador do Sistema, ator abstrato Usuário e equipe do operador como dado` - 23 edges
10. `Quadro E - Nao E - Faz - Nao Faz` - 21 edges

## Surprising Connections (you probably didn't know these)
- `Coordenador de Turnaround (lane do BPMN)` --conceptually_related_to--> `Coordenador de Turnaround`  [INFERRED]
  especificacao/diagramas/04-bpmn-to-be.png → pesquisa/topicos/papeis-e-atores.md
- `Motor de Eventos` --semantically_similar_to--> `A-CDM System / information platform`  [INFERRED] [semantically similar]
  CONTEXT.md → pesquisa/topicos/papeis-e-atores.md
- `Limpar a cabine (confirmação por QR Code)` --conceptually_related_to--> `Task confirmation by QR Code on operator phone`  [INFERRED]
  especificacao/diagramas/04-bpmn-to-be.png → pesquisa/topicos/atividades-e-dependencias.md
- `Tratar o alerta: redistribuir recursos, replanejar e registrar a causa (código ANAC)` --conceptually_related_to--> `ADR-0006 — Códigos de atraso tabela ANAC`  [INFERRED]
  especificacao/diagramas/04-bpmn-to-be.png → docs/adr/0006-codigos-de-atraso-tabela-anac.md
- `Limpar a cabine (confirmação por QR Code)` --conceptually_related_to--> `ADR-0007 — Dados do operador e QR Code`  [INFERRED]
  especificacao/diagramas/04-bpmn-to-be.png → docs/adr/0007-dados-do-operador-e-qr-code.md

## Hyperedges (group relationships)
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

## Communities (9 total, 1 thin omitted)

### Community 0 - "Decisões (ADRs) e fontes da pesquisa"
Cohesion: 0.08
Nodes (79): ADR-0001 — TOBT planejado + 5 min, ADR-0002 — Metas percentuais 80%, ADR-0003 — Atualizar previsão na antecipação, ADR-0004 — Quatro atores e Autoridade de Liberação, ADR-0005 — Abastecimento com passageiros configurável, ADR-0006 — Códigos de atraso tabela ANAC, ADR-0007 — Dados do operador e QR Code, ADR-0008 — Siglas A-CDM com nome em português (+71 more)

### Community 1 - "Contexto: atores, estados e produto"
Cohesion: 0.08
Nodes (60): CONTEXT.md — Contexto do projeto, Administrador do Sistema, AEGT — Fim real do atendimento em solo, Aircraft Turnaround Orchestration System, ARDT — Horário real de prontidão (Aircraft Ready), Autoridade de Liberação, Estados da tarefa, Estados do turnaround (+52 more)

### Community 2 - "QR Code, Visão do Produto e similares"
Cohesion: 0.06
Nodes (61): Diferencial DF5 (QR Code por assento/fileira/zona), Leitura de QR Code pelo celular, Caminho critico, Atualizacao por dispositivo movel / QR code, Categoria-segmento: software de gestão de turnaround / operações de solo, Diferencial-chave: grafo de tarefas com caminho crítico, bloqueio da liberação, registro pelo operador com QR Code, régua TOBT + 5 min, E4: andamento registrado pelo Operador de Solo/Rampa no celular, inclusive QR Code, sem infraestrutura no pátio, Item 3 Visao do Produto (+53 more)

### Community 3 - "Regras para IAs, README e precedência"
Cohesion: 0.10
Nodes (29): Formato de arquivo de pesquisa (YAML + seção Ligações), Domain Docs, Issue tracker: GitHub, GitHub Issues via gh CLI, Wayfinding (map issue + child tickets), Triage Labels, Vocabulário de triage (needs-triage, needs-info, ready-for-agent, ready-for-human, wontfix), Critérios de Aceite RA1 (+21 more)

### Community 4 - "ADR-0011, áreas e modelos dos itens 6, 7, 8 e 10"
Cohesion: 0.12
Nodes (35): ADR-0011 — Mínimo de 4 por integrante, sem máximo; numeração provisória por área, IDs provisórios por área (RF-A1…, US-A1… com o número do RF, RNF-A1…, UC-A1…), Renumeração única no início do T12 (script, áreas A, B, C, D; correspondência em entregas/ra1-renumeracao.md), Metrica: 100% tarefas com responsavel, painel atualizado em ate 5 s, Objetivo 2: Sincronizar equipes, recursos e atividades paralelas, Painel operacional, Area A: Abertura e configuracao do turnaround, Area B: Execucao de tarefas pelo operador (+27 more)

### Community 5 - "Metas, régua do TOBT e risco ao horário"
Cohesion: 0.12
Nodes (29): Metas do item 1 (precisão, sincronização, desvios), MTTT — Tempo mínimo de turnaround, Risco ao horário (gatilhos A-CDM), TOBT — Horário-alvo de prontidão, Heathrow pontualidade "verde" (>=79%), IATA AHM 730, IATA AHM 732, ANAC Portaria nº 55/2026 (+21 more)

### Community 6 - "BPMN: eventos, desvios e subprocessos"
Cohesion: 0.15
Nodes (28): Evento de fim: Turnaround encerrado, Evento de início (mensagem): Voo previsto para a posição, Evento de início (mensagem, não interruptivo): Registro de andamento recebido (início, pausa, conclusão, não aplicável, QR Code), Evento de início (temporizador, não interruptivo): TOBT − 15 min, Gateway exclusivo: Há desvio? (Risco ao horário T8, T11, T12 / Antecipação ≥ 5 min / Não), Gateway exclusivo: Há tarefa obrigatória pendente ou exceção aberta? (Sim → tratar; Não → liberar), Gateway exclusivo: Turnaround viável? (Sim → aguarda AIBT; Não → ajustar o plano ou o TOBT), Coordenador de Turnaround (lane do BPMN) (+20 more)

### Community 7 - "BPMN: tarefas de solo em paralelo"
Cohesion: 0.19
Nodes (25): Evento de mensagem: Aeronave em posição (AIBT), Gateway exclusivo (abastecimento): Abastecimento com passageiros permitido? (Sim → abastecer; Não → aguardar "Desembarque concluído"), Gateway exclusivo (embarque): Abastecimento com passageiros permitido? (Sim → embarcar; Não → aguardar "Abastecimento concluído"), Gateway paralelo: abertura das tarefas em paralelo após o ACGT, Gateway paralelo: junção de embarque e carregamento de bagagem e carga, Gateway paralelo: junção final das tarefas de solo, Gateway paralelo: junção de limpeza e catering, Gateway paralelo: limpeza da cabine e catering após o desembarque (+17 more)

## Knowledge Gaps
- **11 isolated node(s):** `Item 11 Diagrama de Atividades`, `Amadeus (excluded candidate)`, `Cosmos (excluded candidate)`, `Heathrow pontualidade "verde" (>=79%)`, `Wayfinding (map issue + child tickets)` (+6 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 11 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Fontes da pesquisa` connect `QR Code, Visão do Produto e similares` to `Decisões (ADRs) e fontes da pesquisa`, `Contexto: atores, estados e produto`, `Regras para IAs, README e precedência`, `Metas, régua do TOBT e risco ao horário`?**
  _High betweenness centrality (0.226) - this node is a cross-community bridge._
- **Why does `CONTEXT.md — Contexto do projeto` connect `Contexto: atores, estados e produto` to `Decisões (ADRs) e fontes da pesquisa`, `QR Code, Visão do Produto e similares`, `Regras para IAs, README e precedência`, `ADR-0011, áreas e modelos dos itens 6, 7, 8 e 10`, `Metas, régua do TOBT e risco ao horário`?**
  _High betweenness centrality (0.168) - this node is a cross-community bridge._
- **Why does `Pesquisa - mapa da base de conhecimento` connect `Decisões (ADRs) e fontes da pesquisa` to `Contexto: atores, estados e produto`, `QR Code, Visão do Produto e similares`, `Regras para IAs, README e precedência`?**
  _High betweenness centrality (0.107) - this node is a cross-community bridge._
- **Are the 4 inferred relationships involving `Item 4 Mapeamento de Negocios (BPMN to-be)` (e.g. with `Aircraft Turnaround Orchestration System` and `Atividades, paralelismo e dependencias (P1.5)`) actually correct?**
  _`Item 4 Mapeamento de Negocios (BPMN to-be)` has 4 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `Operador de Solo/Rampa (lane do BPMN)` (e.g. with `Operador de Solo/Rampa` and `Operador de Solo/Rampa (item 5)`) actually correct?**
  _`Operador de Solo/Rampa (lane do BPMN)` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Item 11 Diagrama de Atividades`, `Amadeus (excluded candidate)`, `Cosmos (excluded candidate)` to the rest of the system?**
  _11 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Decisões (ADRs) e fontes da pesquisa` be split into smaller, more focused modules?**
  _Cohesion score 0.07530022719896137 - nodes in this community are weakly interconnected._