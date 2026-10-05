# Graph Report - aircraft-turnaround-docs  (2026-10-04)

## Corpus Check
- 71 files · ~57,499 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 371 nodes · 1156 edges · 9 communities
- Extraction: 76% EXTRACTED · 24% INFERRED · 0% AMBIGUOUS · INFERRED: 277 edges (avg confidence: 0.89)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Atores, estados e contexto do produto
- Decisões, fontes do A-CDM e QR Code
- Regras para IAs, CONTEXT e README
- Visão do Produto e similares
- Item 4: leitura do BPMN e abastecimento
- BPMN: eventos, desvios e subprocessos
- Escopo, QR Code e registro pelo operador
- BPMN: tarefas de solo em paralelo
- Previsibilidade, régua do TOBT e códigos de atraso

## God Nodes (most connected - your core abstractions)
1. `Fontes da pesquisa` - 60 edges
2. `CONTEXT.md — Contexto do projeto` - 45 edges
3. `Pesquisa - mapa da base de conhecimento` - 35 edges
4. `Item 4 Mapeamento de Negocios (BPMN to-be)` - 29 edges
5. `Operador de Solo/Rampa (lane do BPMN)` - 29 edges
6. `Diferencial-chave: grafo de tarefas com caminho crítico, bloqueio da liberação, registro pelo operador com QR Code, régua TOBT + 5 min` - 27 edges
7. `README.md — aircraft-turnaround-docs` - 25 edges
8. `ADR-0010 — Administrador do Sistema, ator abstrato Usuário e equipe do operador como dado` - 22 edges
9. `Quadro E - Nao E - Faz - Nao Faz` - 21 edges
10. `Aircraft Turnaround Orchestration System` - 21 edges

## Surprising Connections (you probably didn't know these)
- `Gateway exclusivo (abastecimento): Abastecimento com passageiros permitido? (Sim → abastecer; Não → aguardar "Desembarque concluído")` --conceptually_related_to--> `Refuelling with passengers on board (configurable rule)`  [INFERRED]
  especificacao/diagramas/04-bpmn-to-be.png → pesquisa/topicos/atividades-e-dependencias.md
- `Gateway paralelo: abertura das tarefas em paralelo após o ACGT` --conceptually_related_to--> `Turnaround activities A1-A13 with dependencies`  [INFERRED]
  especificacao/diagramas/04-bpmn-to-be.png → pesquisa/topicos/atividades-e-dependencias.md
- `Limpar a cabine (confirmação por QR Code)` --conceptually_related_to--> `Task confirmation by QR Code on operator phone`  [INFERRED]
  especificacao/diagramas/04-bpmn-to-be.png → pesquisa/topicos/atividades-e-dependencias.md
- `Propagar estados e recalcular projeção, caminho crítico e aderência ao TOBT + 5 min` --conceptually_related_to--> `Turnaround critical path`  [INFERRED]
  especificacao/diagramas/04-bpmn-to-be.png → pesquisa/topicos/caminho-critico.md
- `Embarcar os passageiros (ASBT)` --conceptually_related_to--> `Boarding as critical activity`  [INFERRED]
  especificacao/diagramas/04-bpmn-to-be.png → pesquisa/topicos/caminho-critico.md

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
- **Três camadas da base de conhecimento (decisões, pesquisa, resumo)** — docs_adr_readme, pesquisa_readme, context [EXTRACTED 1.00]
- **'Risco ao horario' trigger set (T8, T11, T12)** — pesquisa_impacto_impacto_por_item_risco_ao_horario, pesquisa_topicos_tolerancias_e_indicadores_tobt_mais_5_min, pesquisa_topicos_tolerancias_e_indicadores_t11_viabilidade_eibt_mttt, pesquisa_topicos_tolerancias_e_indicadores_t12_embarque_nao_iniciado [EXTRACTED 1.00]
- **Campos da Visão de Produto (cliente-alvo, categoria-segmento, benefício-chave, diferencial-chave, meta-valor)** — especificacao_03_visao_do_produto_cliente_alvo, especificacao_03_visao_do_produto_categoria_segmento, especificacao_03_visao_do_produto_beneficio_chave, especificacao_03_visao_do_produto_diferencial_chave, especificacao_03_visao_do_produto_meta_valor [EXTRACTED 1.00]
- **Problemas P1–P5 da Visão do Produto** — especificacao_03_visao_do_produto_p1, especificacao_03_visao_do_produto_p2, especificacao_03_visao_do_produto_p3, especificacao_03_visao_do_produto_p4, especificacao_03_visao_do_produto_p5 [EXTRACTED 1.00]
- **Governança de consistência documental** — context_precedencia_adr_pesquisa, docs_agents_domain_flag_adr_conflicts, entregas_ra1_criterios_de_aceite_k11_consistencia_context_adr, entregas_ra1_criterios_de_aceite_protocolo_execucao_verificacao [INFERRED 0.85]
- **Cadeia de rastreabilidade RF, US, RNF, UC por area** — especificacao_06_requisitos_funcionais_00_item_item, especificacao_07_estorias_de_usuario_00_item_item, especificacao_08_requisitos_nao_funcionais_00_item_item, especificacao_09_diagrama_geral_de_casos_de_uso_item, especificacao_10_especificacoes_de_caso_de_uso_00_item_item [INFERRED 0.85]

## Communities (9 total, 0 thin omitted)

### Community 0 - "Atores, estados e contexto do produto"
Cohesion: 0.07
Nodes (72): Administrador do Sistema, AEGT — Fim real do atendimento em solo, Aircraft Turnaround Orchestration System, ARDT — Horário real de prontidão (Aircraft Ready), Autoridade de Liberação, Estados da tarefa, Estados do turnaround, Motor de Eventos (+64 more)

### Community 1 - "Decisões, fontes do A-CDM e QR Code"
Cohesion: 0.08
Nodes (61): ADR-0006 — Códigos de atraso tabela ANAC, ADR-0007 — Dados do operador e QR Code, Confirmação da limpeza da cabine por leitura de QR Code no celular do operador, Dublin Airport A-CDM Operational Procedures [8], EUROCONTROL A-CDM Specification draft (2024) [3], GE Aerospace - Airport Cleanliness app (QR) [63], Miratag - Aircraft Cabin Cleaning Checklist [64], Impacto por item do template (4.2) (+53 more)

### Community 2 - "Regras para IAs, CONTEXT e README"
Cohesion: 0.09
Nodes (43): Formato de arquivo de pesquisa (YAML + seção Ligações), CONTEXT.md — Contexto do projeto, Metas do item 1 (precisão, sincronização, desvios), MTTT — Tempo mínimo de turnaround, Tabela "O que ler para cada item", Risco ao horário (gatilhos A-CDM), ADR-0001 — TOBT planejado + 5 min, ADR-0002 — Metas percentuais 80% (+35 more)

### Community 3 - "Visão do Produto e similares"
Cohesion: 0.10
Nodes (37): Categoria-segmento: software de gestão de turnaround / operações de solo, Diferencial-chave: grafo de tarefas com caminho crítico, bloqueio da liberação, registro pelo operador com QR Code, régua TOBT + 5 min, P2: TOBT pouco confiável (menos de 60% de acerto em 5 min), P3: atividades paralelas sem visão compartilhada; coordenação por rádio falha, P4: monitoramento automático exige câmeras/sensores e não registra quem executou, Fontes da pesquisa, EUROCONTROL A-CDM Impact Assessment (2016) [14], ADB SAFEGATE - Apron Manager [49] (+29 more)

### Community 4 - "Item 4: leitura do BPMN e abastecimento"
Cohesion: 0.12
Nodes (32): ADR-0005 — Abastecimento com passageiros configurável, EASA CAT.OP.MPA.195, ANAC RBAC 91.102(g), Fluxo de trabalho 1.3: diagramas em Mermaid/PlantUML, exceto o BPMN do item 4 em BPMN 2.0 (.bpmn), Leitura do diagrama: caminho principal (abertura, viabilidade, AIBT, ACGT, tarefas em paralelo, ASBT, loadsheet, AEGT, ARDT, AOBT), Leitura do diagrama: eventos e mensagens (chegada, autorização do ATC, sinais de desembarque/abastecimento concluído, temporizador TOBT − 15 min), Leitura do diagrama: gateways com condição (viável?; abastecimento com passageiros permitido?; pendência ou exceção?; há desvio?), Item 4 Mapeamento de Negocios (BPMN to-be) (+24 more)

### Community 5 - "BPMN: eventos, desvios e subprocessos"
Cohesion: 0.13
Nodes (32): Evento de mensagem: Autorização de acionamento e push-back recebida (do ATC), Evento de fim: Turnaround encerrado, Evento de início (mensagem): Voo previsto para a posição, Evento de início (mensagem, não interruptivo): Registro de andamento recebido (início, pausa, conclusão, não aplicável, QR Code), Evento de início (temporizador, não interruptivo): TOBT − 15 min, Gateway exclusivo: Há desvio? (Risco ao horário T8, T11, T12 / Antecipação ≥ 5 min / Não), Gateway exclusivo: Há tarefa obrigatória pendente ou exceção aberta? (Sim → tratar; Não → liberar), Gateway exclusivo: Turnaround viável? (Sim → aguarda AIBT; Não → ajustar o plano ou o TOBT) (+24 more)

### Community 6 - "Escopo, QR Code e registro pelo operador"
Cohesion: 0.12
Nodes (27): Fora de escopo (voos, tripulação, financeiro, ATC), TSAT — Horário-alvo de autorização de acionamento, Diferencial DF5 (QR Code por assento/fileira/zona), Leitura de QR Code pelo celular, Fora de escopo: malha aerea, slots, ATC, escalas, financeiro, visao computacional/sensores, Atualizacao por dispositivo movel / QR code, Não define o turnaround programado nem o MTTT (dados de entrada), Não é A-CDM completo, sequenciador de partidas (TSAT) nem AODB (+19 more)

### Community 7 - "BPMN: tarefas de solo em paralelo"
Cohesion: 0.19
Nodes (25): Evento de mensagem: Aeronave em posição (AIBT), Gateway exclusivo (abastecimento): Abastecimento com passageiros permitido? (Sim → abastecer; Não → aguardar "Desembarque concluído"), Gateway exclusivo (embarque): Abastecimento com passageiros permitido? (Sim → embarcar; Não → aguardar "Abastecimento concluído"), Gateway paralelo: abertura das tarefas em paralelo após o ACGT, Gateway paralelo: junção de embarque e carregamento de bagagem e carga, Gateway paralelo: junção final das tarefas de solo, Gateway paralelo: junção de limpeza e catering, Gateway paralelo: limpeza da cabine e catering após o desembarque (+17 more)

### Community 8 - "Previsibilidade, régua do TOBT e códigos de atraso"
Cohesion: 0.17
Nodes (14): TOBT — Horário-alvo de prontidão, Aviso de antecipação >= 5 min, IATA AHM 730, IATA AHM 732, ANAC Portaria nº 55/2026, Janela planejada, Metrica: 80% das atividades na janela e 80% dos turnarounds prontos ate o TOBT planejado (tolerancia 5 min), Objetivo 1: Assegurar a precisao temporal do turnaround (+6 more)

## Knowledge Gaps
- **11 isolated node(s):** `EASA CAT.OP.MPA.195`, `ANAC RBAC 91.102(g)`, `Amadeus (excluded candidate)`, `Cosmos (excluded candidate)`, `Item 11 Diagrama de Atividades` (+6 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 11 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Fontes da pesquisa` connect `Visão do Produto e similares` to `Atores, estados e contexto do produto`, `Decisões, fontes do A-CDM e QR Code`, `Regras para IAs, CONTEXT e README`, `Item 4: leitura do BPMN e abastecimento`, `Escopo, QR Code e registro pelo operador`, `Previsibilidade, régua do TOBT e códigos de atraso`?**
  _High betweenness centrality (0.230) - this node is a cross-community bridge._
- **Why does `CONTEXT.md — Contexto do projeto` connect `Regras para IAs, CONTEXT e README` to `Atores, estados e contexto do produto`, `Decisões, fontes do A-CDM e QR Code`, `Visão do Produto e similares`, `Item 4: leitura do BPMN e abastecimento`, `Escopo, QR Code e registro pelo operador`, `Previsibilidade, régua do TOBT e códigos de atraso`?**
  _High betweenness centrality (0.174) - this node is a cross-community bridge._
- **Why does `Pesquisa - mapa da base de conhecimento` connect `Decisões, fontes do A-CDM e QR Code` to `Atores, estados e contexto do produto`, `Regras para IAs, CONTEXT e README`, `Visão do Produto e similares`, `Item 4: leitura do BPMN e abastecimento`?**
  _High betweenness centrality (0.109) - this node is a cross-community bridge._
- **Are the 4 inferred relationships involving `Item 4 Mapeamento de Negocios (BPMN to-be)` (e.g. with `Aircraft Turnaround Orchestration System` and `Atividades, paralelismo e dependencias (P1.5)`) actually correct?**
  _`Item 4 Mapeamento de Negocios (BPMN to-be)` has 4 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `Operador de Solo/Rampa (lane do BPMN)` (e.g. with `Operador de Solo/Rampa` and `Operador de Solo/Rampa (item 5)`) actually correct?**
  _`Operador de Solo/Rampa (lane do BPMN)` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `EASA CAT.OP.MPA.195`, `ANAC RBAC 91.102(g)`, `Amadeus (excluded candidate)` to the rest of the system?**
  _11 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Atores, estados e contexto do produto` be split into smaller, more focused modules?**
  _Cohesion score 0.06621226874391431 - nodes in this community are weakly interconnected._