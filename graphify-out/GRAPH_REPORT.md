# Graph Report - aircraft-turnaround-docs  (2026-10-03)

## Corpus Check
- 70 files · ~37,898 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 305 nodes · 926 edges · 9 communities
- Extraction: 76% EXTRACTED · 24% INFERRED · 0% AMBIGUOUS · INFERRED: 221 edges (avg confidence: 0.88)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Visão do Produto, similares e fontes
- Decisões e pesquisa de similares
- Atores e produto
- Regras para IAs, README e siglas
- Régua do TOBT e fontes do A-CDM
- Áreas, estados da tarefa e códigos de atraso
- Metas, alertas e caminho crítico
- CONTEXT: marcos, estados e metas
- QR Code e registro pelo operador

## God Nodes (most connected - your core abstractions)
1. `Fontes da pesquisa` - 58 edges
2. `CONTEXT.md — Contexto do projeto` - 45 edges
3. `Pesquisa - mapa da base de conhecimento` - 35 edges
4. `Diferencial-chave: grafo de tarefas com caminho crítico, bloqueio da liberação, registro pelo operador com QR Code, régua TOBT + 5 min` - 27 edges
5. `README.md — aircraft-turnaround-docs` - 25 edges
6. `Quadro E - Nao E - Faz - Nao Faz` - 21 edges
7. `Aircraft Turnaround Orchestration System` - 20 edges
8. `ADR-0010 — Administrador do Sistema, ator abstrato Usuário e equipe do operador como dado` - 20 edges
9. `Coordenador de Turnaround` - 19 edges
10. `Lacunas e diferencial possivel (3.4)` - 17 edges

## Surprising Connections (you probably didn't know these)
- `Sinalizar conflitos com ADRs` --semantically_similar_to--> `Precedência: ADRs > pesquisa > rascunhos`  [INFERRED] [semantically similar]
  docs/agents/domain.md → CONTEXT.md
- `Motor de Eventos` --semantically_similar_to--> `A-CDM System / information platform`  [INFERRED] [semantically similar]
  CONTEXT.md → pesquisa/topicos/papeis-e-atores.md
- `Motor de Eventos — ator não humano (item 5)` --semantically_similar_to--> `Motor de Eventos`  [INFERRED] [semantically similar]
  especificacao/05-atores-usuarios.md → CONTEXT.md
- `Rótulos ra1 / item-NN / area-x / por-integrante` --semantically_similar_to--> `Vocabulário de triage (needs-triage, needs-info, ready-for-agent, ready-for-human, wontfix)`  [INFERRED] [semantically similar]
  entregas/ra1-tarefas.md → docs/agents/triage-labels.md
- `Não é ferramenta para encurtar o turnaround nem encaixar mais voos` --semantically_similar_to--> `Princípio: previsibilidade, não velocidade`  [INFERRED] [semantically similar]
  especificacao/02-e-nao-e-faz-nao-faz.md → CONTEXT.md

## Hyperedges (group relationships)
- **Cinco atores da Relação de Atores / Usuários (item 5)** — especificacao_05_atores_usuarios_operador_de_solo_rampa, especificacao_05_atores_usuarios_coordenador_de_turnaround, especificacao_05_atores_usuarios_autoridade_de_liberacao, especificacao_05_atores_usuarios_administrador_do_sistema, especificacao_05_atores_usuarios_motor_de_eventos [EXTRACTED 1.00]
- **Atores humanos generalizados pelo ator abstrato Usuário** — context_usuario_ator_abstrato, context_operador_de_solo_rampa, pesquisa_topicos_papeis_e_atores_coordenador_de_turnaround, context_autoridade_de_liberacao, context_administrador_do_sistema [EXTRACTED 1.00]
- **Atores do turnaround (Operador de Solo/Rampa, Coordenador de Turnaround, Autoridade de Liberação)** — context_operador_de_solo_rampa, pesquisa_topicos_papeis_e_atores_coordenador_de_turnaround, pesquisa_topicos_papeis_e_atores_autoridade_de_liberacao [EXTRACTED 1.00]
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

### Community 0 - "Visão do Produto, similares e fontes"
Cohesion: 0.08
Nodes (51): Categoria-segmento: software de gestão de turnaround / operações de solo, Diferencial-chave: grafo de tarefas com caminho crítico, bloqueio da liberação, registro pelo operador com QR Code, régua TOBT + 5 min, P2: TOBT pouco confiável (menos de 60% de acerto em 5 min), P4: monitoramento automático exige câmeras/sensores e não registra quem executou, Fontes da pesquisa, EUROCONTROL A-CDM Impact Assessment (2016) [14], ADB SAFEGATE - Apron Manager [49], ADB SAFEGATE - visual docking guidance press release [48] (+43 more)

### Community 1 - "Decisões e pesquisa de similares"
Cohesion: 0.09
Nodes (44): ADR-0003 — Atualizar previsão na antecipação, ADR-0005 — Abastecimento com passageiros configurável, EASA CAT.OP.MPA.195, ANAC RBAC 91.102(g), ADR-0006 — Códigos de atraso tabela ANAC, ADR-0007 — Dados do operador e QR Code, EUROCONTROL CODA Digest 2023 [16], IATA AHM 732 delay codes webinar [37] (+36 more)

### Community 2 - "Atores e produto"
Cohesion: 0.13
Nodes (34): Administrador do Sistema, Aircraft Turnaround Orchestration System, Autoridade de Liberação, Fora de escopo (voos, tripulação, financeiro, ATC), Motor de Eventos, Operador de Solo/Rampa, Usuário (ator abstrato), Aviso de antecipação >= 5 min (+26 more)

### Community 3 - "Regras para IAs, README e siglas"
Cohesion: 0.10
Nodes (30): Formato de arquivo de pesquisa (YAML + seção Ligações), ADR-0008 — Siglas A-CDM com nome em português, Índice de decisões (ADRs), Domain Docs, Usar o vocabulário do glossário do CONTEXT.md, Issue tracker: GitHub, GitHub Issues via gh CLI, Wayfinding (map issue + child tickets) (+22 more)

### Community 4 - "Régua do TOBT e fontes do A-CDM"
Cohesion: 0.12
Nodes (33): ADR-0001 — TOBT planejado + 5 min, ADR-0002 — Metas percentuais 80%, Motor de Eventos — ator não humano (item 5), Airport CDM Implementation Manual v5.0 (ACI/EUROCONTROL/IATA) [4], Dublin Airport A-CDM Operational Procedures [8], EUROCONTROL A-CDM Specification draft (2024) [3], Heathrow AOP2 user manual [7], SES Performance ATFM slot adherence [15] (+25 more)

### Community 5 - "Áreas, estados da tarefa e códigos de atraso"
Cohesion: 0.11
Nodes (29): Estados da tarefa, IATA AHM 730, IATA AHM 732, ANAC Portaria nº 55/2026, Area A: Abertura e configuracao do turnaround, Area B: Execucao de tarefas pelo operador, Area D: Replanejamento e liberacao, Registro da causa de atraso/exceção com código da tabela da ANAC (+21 more)

### Community 6 - "Metas, alertas e caminho crítico"
Cohesion: 0.14
Nodes (30): Heathrow pontualidade "verde" (>=79%), Alerta de risco ao horario planejado, Caminho critico, Janela planejada, Liberacao da aeronave, Metrica: 80% das atividades na janela e 80% dos turnarounds prontos ate o TOBT planejado (tolerancia 5 min), Metrica: alertas em 5 s, 90% acoes em 2 min, 0 liberacoes com pendencia, Metrica: 100% tarefas com responsavel, painel atualizado em ate 5 s (+22 more)

### Community 7 - "CONTEXT: marcos, estados e metas"
Cohesion: 0.19
Nodes (22): CONTEXT.md — Contexto do projeto, AEGT — Fim real do atendimento em solo, ARDT — Horário real de prontidão (Aircraft Ready), Estados do turnaround, Metas do item 1 (precisão, sincronização, desvios), MTTT — Tempo mínimo de turnaround, Tabela "O que ler para cada item", Risco ao horário (gatilhos A-CDM) (+14 more)

### Community 8 - "QR Code e registro pelo operador"
Cohesion: 0.60
Nodes (4): Diferencial DF5 (QR Code por assento/fileira/zona), Leitura de QR Code pelo celular, Atualizacao por dispositivo movel / QR code, E4: andamento registrado pelo Operador de Solo/Rampa no celular, inclusive QR Code, sem infraestrutura no pátio

## Knowledge Gaps
- **12 isolated node(s):** `Amadeus (excluded candidate)`, `Cosmos (excluded candidate)`, `GRU first A-CDM airport in Brazil (2020)`, `Item 4 Mapeamento de Negocios (BPMN to-be)`, `Item 11 Diagrama de Atividades` (+7 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 12 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Fontes da pesquisa` connect `Visão do Produto, similares e fontes` to `Decisões e pesquisa de similares`, `Atores e produto`, `Regras para IAs, README e siglas`, `Régua do TOBT e fontes do A-CDM`, `Metas, alertas e caminho crítico`, `CONTEXT: marcos, estados e metas`?**
  _High betweenness centrality (0.295) - this node is a cross-community bridge._
- **Why does `CONTEXT.md — Contexto do projeto` connect `CONTEXT: marcos, estados e metas` to `Visão do Produto, similares e fontes`, `Decisões e pesquisa de similares`, `Atores e produto`, `Regras para IAs, README e siglas`, `Régua do TOBT e fontes do A-CDM`, `Áreas, estados da tarefa e códigos de atraso`?**
  _High betweenness centrality (0.189) - this node is a cross-community bridge._
- **Why does `Pesquisa - mapa da base de conhecimento` connect `Decisões e pesquisa de similares` to `Visão do Produto, similares e fontes`, `Atores e produto`, `Regras para IAs, README e siglas`, `Régua do TOBT e fontes do A-CDM`, `CONTEXT: marcos, estados e metas`?**
  _High betweenness centrality (0.146) - this node is a cross-community bridge._
- **Are the 8 inferred relationships involving `Diferencial-chave: grafo de tarefas com caminho crítico, bloqueio da liberação, registro pelo operador com QR Code, régua TOBT + 5 min` (e.g. with `D1 — Régua TOBT planejado + 5 min, unilateral` and `D7 — Dados do operador, inclusive QR Code pelo celular`) actually correct?**
  _`Diferencial-chave: grafo de tarefas com caminho crítico, bloqueio da liberação, registro pelo operador com QR Code, régua TOBT + 5 min` has 8 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Amadeus (excluded candidate)`, `Cosmos (excluded candidate)`, `GRU first A-CDM airport in Brazil (2020)` to the rest of the system?**
  _12 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Visão do Produto, similares e fontes` be split into smaller, more focused modules?**
  _Cohesion score 0.07607843137254902 - nodes in this community are weakly interconnected._
- **Should `Decisões e pesquisa de similares` be split into smaller, more focused modules?**
  _Cohesion score 0.09494949494949495 - nodes in this community are weakly interconnected._