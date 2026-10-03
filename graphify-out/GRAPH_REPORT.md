# Graph Report - aircraft-turnaround-docs  (2026-10-03)

## Corpus Check
- 69 files · ~34,585 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 284 nodes · 773 edges · 10 communities (9 shown, 1 thin omitted)
- Extraction: 75% EXTRACTED · 25% INFERRED · 0% AMBIGUOUS · INFERRED: 193 edges (avg confidence: 0.88)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- ADRs, pesquisa e similares
- Visão do Produto e similares de mercado
- Produto, objetivos e áreas
- Contexto, A-CDM e regras para IAs
- Fontes: normas e estudos
- Atores, QR Code e nome do coordenador
- Previsibilidade, metas e códigos de atraso
- Processo do RA1 e issue tracker
- Desvios, caminho crítico e liberação
- Abastecimento com passageiros

## God Nodes (most connected - your core abstractions)
1. `Fontes da pesquisa` - 52 edges
2. `CONTEXT.md — Contexto do projeto` - 37 edges
3. `Pesquisa - mapa da base de conhecimento` - 32 edges
4. `Diferencial-chave: grafo de tarefas com caminho crítico, bloqueio da liberação, registro pelo operador com QR Code, régua TOBT + 5 min` - 27 edges
5. `Quadro E - Nao E - Faz - Nao Faz` - 21 edges
6. `Aircraft Turnaround Orchestration System` - 19 edges
7. `Lacunas e diferencial possivel (3.4)` - 17 edges
8. `Tolerancias e indicadores de aderencia (P1.3)` - 17 edges
9. `Item 3 Visao do Produto` - 17 edges
10. `Matriz comparativa (3.3)` - 15 edges

## Surprising Connections (you probably didn't know these)
- `Sinalizar conflitos com ADRs` --semantically_similar_to--> `Precedência: ADRs > pesquisa > rascunhos`  [INFERRED] [semantically similar]
  docs/agents/domain.md → CONTEXT.md
- `Não é ferramenta para encurtar o turnaround nem encaixar mais voos` --semantically_similar_to--> `Princípio: previsibilidade, não velocidade`  [INFERRED] [semantically similar]
  especificacao/02-e-nao-e-faz-nao-faz.md → CONTEXT.md
- `Orientacao ao plano (aderencia a janela planejada)` --semantically_similar_to--> `Princípio: previsibilidade, não velocidade`  [INFERRED] [semantically similar]
  especificacao/02-e-nao-e-faz-nao-faz.md → CONTEXT.md
- `Rótulos ra1 / item-NN / area-x / por-integrante` --semantically_similar_to--> `Vocabulário de triage (needs-triage, needs-info, ready-for-agent, ready-for-human, wontfix)`  [INFERRED] [semantically similar]
  entregas/ra1-tarefas.md → docs/agents/triage-labels.md
- `Fora de escopo: malha aerea, slots, ATC, escalas, financeiro, visao computacional/sensores` --conceptually_related_to--> `D7 — Dados do operador, inclusive QR Code pelo celular`  [INFERRED]
  especificacao/02-e-nao-e-faz-nao-faz.md → docs/adr/0007-dados-do-operador-e-qr-code.md

## Hyperedges (group relationships)
- **Atores do turnaround (Operador de Solo/Rampa, Coordenador de Turnaround, Autoridade de Liberação)** — context_operador_de_solo_rampa, pesquisa_topicos_papeis_e_atores_coordenador_de_turnaround, pesquisa_topicos_papeis_e_atores_autoridade_de_liberacao [EXTRACTED 1.00]
- **Régua de horário e metas (TOBT + 5 min, 80%, antecipação)** — docs_adr_0001_referencia_horario_tobt_mais_5_min_d1_tobt_mais_5_min, docs_adr_0002_metas_percentuais_80_d2_metas_80, docs_adr_0003_atualizar_previsao_na_antecipacao_d3_atualizar_previsao_antecipacao, context_tobt, context_metas_do_item_1 [EXTRACTED 1.00]
- **Five market similars compared in matrix 3.3** — pesquisa_similares_assaia_assaia_apronai_turnaroundcontrol, pesquisa_similares_inform_groundstar_inform_groundstar, pesquisa_similares_adb_safegate_adb_safegate_safedock_apron_manager, pesquisa_similares_veovo_veovo_acdm, pesquisa_similares_sita_sita_airport_management_cdm, pesquisa_similares_matriz_comparativa_capacidades_do_nucleo [EXTRACTED 1.00]
- **Project differentiators DF1-DF5** — pesquisa_similares_lacunas_e_diferencial_df1, pesquisa_similares_lacunas_e_diferencial_df2, pesquisa_similares_lacunas_e_diferencial_df3, pesquisa_similares_lacunas_e_diferencial_df4, pesquisa_similares_lacunas_e_diferencial_df5 [EXTRACTED 1.00]
- **Quatro atores do Aircraft Turnaround Orchestration System** — context_operador_de_solo_rampa, context_coordenador_de_turnaround, context_autoridade_de_liberacao, context_motor_de_eventos [EXTRACTED 1.00]
- **'Risco ao horario' trigger set (T8, T11, T12)** — pesquisa_impacto_impacto_por_item_risco_ao_horario, pesquisa_topicos_tolerancias_e_indicadores_tobt_mais_5_min, pesquisa_topicos_tolerancias_e_indicadores_t11_viabilidade_eibt_mttt, pesquisa_topicos_tolerancias_e_indicadores_t12_embarque_nao_iniciado [EXTRACTED 1.00]
- **Campos da Visão de Produto (cliente-alvo, categoria-segmento, benefício-chave, diferencial-chave, meta-valor)** — especificacao_03_visao_do_produto_cliente_alvo, especificacao_03_visao_do_produto_categoria_segmento, especificacao_03_visao_do_produto_beneficio_chave, especificacao_03_visao_do_produto_diferencial_chave, especificacao_03_visao_do_produto_meta_valor [EXTRACTED 1.00]
- **Problemas P1–P5 da Visão do Produto** — especificacao_03_visao_do_produto_p1, especificacao_03_visao_do_produto_p2, especificacao_03_visao_do_produto_p3, especificacao_03_visao_do_produto_p4, especificacao_03_visao_do_produto_p5 [EXTRACTED 1.00]
- **Governança de consistência documental** — context_precedencia_adr_pesquisa, docs_agents_domain_flag_adr_conflicts, entregas_ra1_criterios_de_aceite_k11_consistencia_context_adr, entregas_ra1_criterios_de_aceite_protocolo_execucao_verificacao [INFERRED 0.85]
- **Cadeia de rastreabilidade RF, US, RNF, UC por area** — especificacao_06_requisitos_funcionais_00_item_item, especificacao_07_estorias_de_usuario_00_item_item, especificacao_08_requisitos_nao_funcionais_00_item_item, especificacao_09_diagrama_geral_de_casos_de_uso_item, especificacao_10_especificacoes_de_caso_de_uso_00_item_item [INFERRED 0.85]

## Communities (10 total, 1 thin omitted)

### Community 0 - "ADRs, pesquisa e similares"
Cohesion: 0.09
Nodes (61): ADR-0001 — TOBT planejado + 5 min, ADR-0002 — Metas percentuais 80%, ADR-0003 — Atualizar previsão na antecipação, ADR-0004 — Quatro atores e Autoridade de Liberação, ADR-0005 — Abastecimento com passageiros configurável, ADR-0006 — Códigos de atraso tabela ANAC, ADR-0007 — Dados do operador e QR Code, ADR-0008 — Siglas A-CDM com nome em português (+53 more)

### Community 1 - "Visão do Produto e similares de mercado"
Cohesion: 0.08
Nodes (48): Categoria-segmento: software de gestão de turnaround / operações de solo, Diferencial-chave: grafo de tarefas com caminho crítico, bloqueio da liberação, registro pelo operador com QR Code, régua TOBT + 5 min, Item 3 Visao do Produto, P1: desvios percebidos tarde e propagados (atraso reacionário 46%, 67,9% das partidas em até 15 min), P2: TOBT pouco confiável (menos de 60% de acerto em 5 min), P4: monitoramento automático exige câmeras/sensores e não registra quem executou, P5: sem garantia formal de ausência de pendência na liberação (Aircraft Ready), Fontes da pesquisa (+40 more)

### Community 2 - "Produto, objetivos e áreas"
Cohesion: 0.11
Nodes (36): Aircraft Turnaround Orchestration System, Estados da tarefa, Metrica: 100% tarefas com responsavel, painel atualizado em ate 5 s, Objetivo 2: Sincronizar equipes, recursos e atividades paralelas, Painel operacional, Quadro 3 Objetivos, Area A: Abertura e configuracao do turnaround, Area B: Execucao de tarefas pelo operador (+28 more)

### Community 3 - "Contexto, A-CDM e regras para IAs"
Cohesion: 0.12
Nodes (25): Formato de arquivo de pesquisa (YAML + seção Ligações), CONTEXT.md — Contexto do projeto, A-CDM (Airport Collaborative Decision Making), AEGT — Fim real do atendimento em solo, ARDT — Horário real de prontidão (Aircraft Ready), Autoridade de Liberação, Coordenador de Turnaround, Estados do turnaround (+17 more)

### Community 4 - "Fontes: normas e estudos"
Cohesion: 0.11
Nodes (26): ANAC RBAC 91 Emenda 05, 91.102(g) [27], Dublin Airport A-CDM Operational Procedures [8], EASA Part-CAT CAT.OP.MPA.195 [26], IATA A-CDM Recommendations (2018) [5], Kierzkowski et al. 2025 - PERT-COST ground handling [22], Planda & Skorupski 2025 - Aircraft Boarding Under Disturbances [21], Sanz de Vicente 2010 - Ground Handling Simulation with CAST [24], Schultz 2018 - Fast Aircraft Turnaround Enabled by Reliable Passenger Boarding [20] (+18 more)

### Community 5 - "Atores, QR Code e nome do coordenador"
Cohesion: 0.14
Nodes (20): Operador de Solo/Rampa, Diferencial DF5 (QR Code por assento/fileira/zona), Leitura de QR Code pelo celular, K.1 — Atores com nomes idênticos, Instrumento de apoio à decisão do Coordenador de Turnaround e da Autoridade de Liberação, Registro da causa de atraso/exceção com código da tabela da ANAC, Atualizacao por dispositivo movel / QR code, Não é registro posterior da operação (+12 more)

### Community 6 - "Previsibilidade, metas e códigos de atraso"
Cohesion: 0.16
Nodes (14): Heathrow pontualidade "verde" (>=79%), IATA AHM 730, IATA AHM 732, ANAC Portaria nº 55/2026, Janela planejada, Metrica: 80% das atividades na janela e 80% dos turnarounds prontos ate o TOBT planejado (tolerancia 5 min), Objetivo 1: Assegurar a precisao temporal do turnaround, Benefício-chave: aeronave pronta para liberação no TOBT, desvios tratados durante a operação (+6 more)

### Community 7 - "Processo do RA1 e issue tracker"
Cohesion: 0.13
Nodes (18): Issue tracker: GitHub, GitHub Issues via gh CLI, Wayfinding (map issue + child tickets), Triage Labels, Vocabulário de triage (needs-triage, needs-info, ready-for-agent, ready-for-human, wontfix), Critérios de Aceite RA1, Dependências e ordem de execução dos itens, K.11 — Nenhum item contradiz CONTEXT.md nem D1–D9 (+10 more)

### Community 8 - "Desvios, caminho crítico e liberação"
Cohesion: 0.28
Nodes (13): Alerta de risco ao horario planejado, Caminho critico, Liberacao da aeronave, Metrica: alertas em 5 s, 90% acoes em 2 min, 0 liberacoes com pendencia, Objetivo 3: Antecipar desvios e assegurar liberacao segura, Projecao de conclusao, Bloqueio de liberacao com tarefa obrigatoria pendente ou excecao, E1: desvios detectados durante a operação (projeção e caminho crítico recalculados, alerta ao Coordenador de Turnaround) (+5 more)

## Knowledge Gaps
- **18 isolated node(s):** `Diferencial DF5 (QR Code por assento/fileira/zona)`, `EASA CAT.OP.MPA.195`, `ANAC RBAC 91.102(g)`, `Amadeus (excluded candidate)`, `Cosmos (excluded candidate)` (+13 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 19 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Fontes da pesquisa` connect `Visão do Produto e similares de mercado` to `ADRs, pesquisa e similares`, `Contexto, A-CDM e regras para IAs`, `Fontes: normas e estudos`, `Atores, QR Code e nome do coordenador`, `Previsibilidade, metas e códigos de atraso`, `Processo do RA1 e issue tracker`, `Desvios, caminho crítico e liberação`?**
  _High betweenness centrality (0.318) - this node is a cross-community bridge._
- **Why does `CONTEXT.md — Contexto do projeto` connect `Contexto, A-CDM e regras para IAs` to `ADRs, pesquisa e similares`, `Visão do Produto e similares de mercado`, `Produto, objetivos e áreas`, `Atores, QR Code e nome do coordenador`, `Previsibilidade, metas e códigos de atraso`, `Processo do RA1 e issue tracker`?**
  _High betweenness centrality (0.250) - this node is a cross-community bridge._
- **Why does `Pesquisa - mapa da base de conhecimento` connect `ADRs, pesquisa e similares` to `Visão do Produto e similares de mercado`, `Contexto, A-CDM e regras para IAs`?**
  _High betweenness centrality (0.158) - this node is a cross-community bridge._
- **Are the 8 inferred relationships involving `Diferencial-chave: grafo de tarefas com caminho crítico, bloqueio da liberação, registro pelo operador com QR Code, régua TOBT + 5 min` (e.g. with `D1 — Régua TOBT planejado + 5 min, unilateral` and `D7 — Dados do operador, inclusive QR Code pelo celular`) actually correct?**
  _`Diferencial-chave: grafo de tarefas com caminho crítico, bloqueio da liberação, registro pelo operador com QR Code, régua TOBT + 5 min` has 8 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Diferencial DF5 (QR Code por assento/fileira/zona)`, `EASA CAT.OP.MPA.195`, `ANAC RBAC 91.102(g)` to the rest of the system?**
  _18 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `ADRs, pesquisa e similares` be split into smaller, more focused modules?**
  _Cohesion score 0.09398907103825137 - nodes in this community are weakly interconnected._
- **Should `Visão do Produto e similares de mercado` be split into smaller, more focused modules?**
  _Cohesion score 0.07801418439716312 - nodes in this community are weakly interconnected._