---
id: contexto
titulo: "Contexto do projeto — leia antes de qualquer tarefa"
tipo: contexto
status: vigente
atualizado: 2026-10-07
relacionados: [mapa-pesquisa, adr-indice, adr-0001, adr-0002, adr-0003, adr-0004, adr-0005, adr-0006, adr-0007, adr-0008, adr-0009, adr-0010, adr-0011, adr-0012]
---
# Contexto do projeto

> Leia este arquivo **antes de qualquer tarefa de documentação**. Ele resume o que está decidido e aponta onde está o detalhe. É curto de propósito: não leia a pesquisa inteira, abra só o que o seu item pede (tabela da seção 9).

## 1. Produto

- **Nome (sempre exatamente assim):** Aircraft Turnaround Orchestration System.
- **O que é:** sistema web que orquestra o turnaround de aeronaves, do in-block (chegada à posição) ao off-block (saída da posição): execução de tarefas em paralelo, propagação de estado, cálculo de atraso e caminho crítico, painel em tempo real, alertas e redistribuição de recursos.
- **Princípio:** o objetivo **não é encurtar o turnaround**, e sim garantir que ele aconteça **dentro do planejado** (previsibilidade). Terminar antes é aceitável, mas não é meta. Ver [previsibilidade × velocidade](pesquisa/topicos/previsibilidade-vs-velocidade.md).
- **Fora de escopo:** programação de voos e do turnaround programado, escala de tripulação, financeiro e integração real com o controle de tráfego aéreo (ATC).

## 2. Atores (nomes idênticos em todos os itens)

| Ator | Papel |
|---|---|
| **Operador de Solo/Rampa** | Executa as tarefas da **sua equipe ou especialidade** (abastecimento, limpeza, catering, rampa…), da própria empresa de *handling* ou de prestador contratado; a equipe é um dado do cadastro, não um ator separado; registra início, pausa, conclusão, "não aplicável" e leituras de QR Code. |
| **Coordenador de Turnaround** | Coordena o turnaround, mantém atualizado o horário-alvo de prontidão (TOBT), trata alertas e exceções e redistribui recursos. |
| **Autoridade de Liberação** | Representante da companhia aérea que confirma a prontidão da aeronave (equivalente ao marco *Aircraft Ready* do A-CDM). **Não** é a autorização do ATC. |
| **Administrador do Sistema** | Mantém usuários, perfis de acesso e equipes ou especialidades; não atua nos turnarounds. |
| **Motor de Eventos** | Ator não humano: recebe os registros, recalcula projeções e caminho crítico e emite alertas. |

Decisões: [ADR-0004](docs/adr/0004-quatro-atores-e-autoridade-de-liberacao.md), [ADR-0009](docs/adr/0009-nome-coordenador-de-turnaround.md), [ADR-0010](docs/adr/0010-administrador-usuario-e-equipe-do-operador.md).

**Ator abstrato Usuário:** generaliza os quatro atores humanos (casos de uso comuns, como autenticar-se); aparece só no diagrama de casos de uso (item 9). O Motor de Eventos não o especializa.

## 3. Estados

- **Turnaround:** Em solo → Operações em andamento → Pronto para liberação → Liberado → Fora de bloco; estado lateral **Em exceção**. "Liberado" é ato interno da Autoridade de Liberação.
- **Tarefa:** Aguardando → Pronta → Em execução → Concluída; ramos **Pausada** e **Não aplicável**.

## 4. Glossário mínimo (siglas do setor)

Regra ([ADR-0008](docs/adr/0008-siglas-a-cdm-com-nome-em-portugues.md)): **toda** sigla vem com o nome em português na primeira ocorrência de cada item da especificação, no formato "nome em português (SIGLA)". Vale para as siglas desta tabela, **inclusive a própria A-CDM**, e para as de órgãos e normas (por exemplo, "Agência Nacional de Aviação Civil (ANAC)" e "Associação Internacional de Transporte Aéreo (IATA)"). Vale também nas tabelas "Base" e nas regras de negócio, e não só no texto corrido. Depois da primeira ocorrência no item, use só a sigla. Glossário completo: [marcos e horários](pesquisa/topicos/marcos-e-horarios.md).

| Sigla | Nome em português | Estado ou uso no projeto |
|---|---|---|
| A-CDM | Tomada de decisão colaborativa em aeroportos | Padrão de referência do setor para marcos, horários e alertas |
| IATA | Associação Internacional de Transporte Aéreo | Fonte de recomendações do setor (ex.: A-CDM, códigos de atraso) |
| ATC | Controle de tráfego aéreo | Fora de escopo; emite TSAT e autoriza acionamento e push-back |
| SIBT / SOBT | Horário programado de chegada / de saída da posição | Referência da programação (fora de escopo alterar) |
| EIBT | Horário estimado de chegada à posição | Planejamento do turnaround |
| AIBT | Horário real de chegada à posição (in-block) | Entrada em **Em solo** |
| ACGT | Início real do atendimento em solo | Entrada em **Operações em andamento** |
| ASBT | Início real do embarque | Marco de tarefa; alerta se não começar até TOBT − X |
| AEGT | Fim real do atendimento em solo | Entrada em **Pronto para liberação** |
| ARDT | Horário real de prontidão (*Aircraft Ready*) | Confirmação pela Autoridade de Liberação |
| AOBT | Horário real de saída da posição (off-block) | Entrada em **Fora de bloco** |
| TOBT | Horário-alvo de prontidão | **Régua de aderência do projeto** |
| TSAT | Horário-alvo de autorização de acionamento | Emitido pelo ATC — fora de escopo |
| MTTT | Tempo mínimo de turnaround | Parâmetro; checagem EIBT + MTTT ≤ TOBT |

## 5. Decisões vigentes

| | Decisão | ADR |
|---|---|---|
| D1 | Régua: pronto até o **TOBT planejado + 5 min**, unilateral | [0001](docs/adr/0001-referencia-horario-tobt-mais-5-min.md) |
| D2 | Metas percentuais do item 1: **80%** | [0002](docs/adr/0002-metas-percentuais-80.md) |
| D3 | Antecipação de 5 min ou mais → pedir atualização da previsão | [0003](docs/adr/0003-atualizar-previsao-na-antecipacao.md) |
| D4 | 4 atores operacionais; Autoridade de Liberação = representante da companhia (complementada pela D10) | [0004](docs/adr/0004-quatro-atores-e-autoridade-de-liberacao.md) |
| D5 | Abastecimento com passageiros a bordo: regra configurável por operador | [0005](docs/adr/0005-abastecimento-com-passageiros-configuravel.md) |
| D6 | Códigos de atraso: tabela completa da **ANAC** (72 códigos) | [0006](docs/adr/0006-codigos-de-atraso-tabela-anac.md) |
| D7 | Dados do operador, **inclusive QR Code pelo celular**; sem sensores da aeronave nem câmeras fixas | [0007](docs/adr/0007-dados-do-operador-e-qr-code.md) |
| D8 | Siglas do A-CDM com nome em português | [0008](docs/adr/0008-siglas-a-cdm-com-nome-em-portugues.md) |
| D9 | Nome único: **Coordenador de Turnaround** | [0009](docs/adr/0009-nome-coordenador-de-turnaround.md) |
| D10 | **Administrador do Sistema** como ator; ator abstrato **Usuário**; equipe do operador como dado | [0010](docs/adr/0010-administrador-usuario-e-equipe-do-operador.md) |
| D11 | **Mínimo de 4 por integrante, sem máximo**; IDs provisórios por área (RF-A1, US-A1, RNF-A1, UC-A1) e renumeração sequencial única no início do T12 | [0011](docs/adr/0011-minimo-por-integrante-e-numeracao-provisoria.md) |
| D12 | **Matriz de rastreabilidade** como Apêndice A, gerada por script; cada RNF cita os RFs a que se aplica; tabelas "Base" só no repositório, fora do PDF | [0012](docs/adr/0012-matriz-de-rastreabilidade.md) |

## 6. Metas do item 1 (vigentes)

1. **Precisão temporal:** ≥ **80%** das atividades iniciadas e concluídas dentro das janelas planejadas; ≥ **80%** dos turnarounds prontos para liberação até o **TOBT planejado**, com tolerância máxima de **5 min**.
2. **Sincronização:** 100% das tarefas com responsável antes do início; nenhuma conclusão sem registro de início; mudança de estado no painel em até 5 s.
3. **Desvios e liberação:** alerta em até 5 s para 100% das atualizações com risco ao horário; ≥ 90% dos alertas críticos com ação registrada em até 2 min; 0 liberações com tarefa obrigatória pendente ou exceção não resolvida.

Os 5 min têm referência direta no setor (tolerância em torno do TOBT). Os 80% seguem as referências de mercado mais próximas (pontualidade "verde" de Heathrow; a aderência ao slot ATFM só como analogia), e não há meta pública oficial de % para o TOBT ([ADR-0002](docs/adr/0002-metas-percentuais-80.md)). 5 s, 100%, 90% em 2 min e 0 liberações são metas internas do projeto. Detalhe: [métricas do item 1](pesquisa/impacto/metricas-item-1.md). "Risco ao horário" = gatilhos do A-CDM: EIBT + MTTT além do TOBT; embarque não iniciado até TOBT − X; prontidão não registrada em TOBT + 5 ([tolerâncias](pesquisa/topicos/tolerancias-e-indicadores.md)).

## 7. Regras para quem escreve (pessoas e IAs)

1. **Precedência:** decisões ([docs/adr/](docs/adr/README.md)) > pesquisa vigente ([pesquisa/](pesquisa/README.md)) > rascunhos e textos antigos. O [relatório consolidado](pesquisa/01-referencias-setor-e-similares.md) está congelado.
2. **Não contradiga uma decisão.** Se algo pedir uma mudança de decisão, registre a dúvida para o grupo em vez de mudar o texto.
3. **Cite a fonte** ao usar número ou sigla do setor, pelo número de [pesquisa/fontes.md](pesquisa/fontes.md).
4. **Separe fato de inferência** quando o texto não for óbvio.
5. **Use os nomes exatos** do produto, dos atores e dos estados.

## 8. Onde fica cada coisa

- **Mapa da pesquisa** (índices por item e por área, diagrama): [pesquisa/README.md](pesquisa/README.md)
- **Decisões:** [docs/adr/README.md](docs/adr/README.md)
- **Fontes:** [pesquisa/fontes.md](pesquisa/fontes.md)
- **Plano e critérios do RA1:** [entregas/ra1-tarefas.md](entregas/ra1-tarefas.md), [entregas/ra1-criterios-de-aceite.md](entregas/ra1-criterios-de-aceite.md)
- **Grafo** (quando existir): `graphify-out/GRAPH_REPORT.md` e `graphify-out/graph.html`. Use para achar o que ler; decida pelos arquivos.

## 9. O que ler para cada item

D8 (siglas) e D9 (nome do coordenador) valem para **todos** os itens. A coluna "Decisões" mostra as demais, conforme o campo `itens_template` de cada ADR.

| Item | Leia | Decisões |
|---|---|---|
| 1 — 3 Objetivos | [métricas do item 1](pesquisa/impacto/metricas-item-1.md), [tolerâncias](pesquisa/topicos/tolerancias-e-indicadores.md), [previsibilidade](pesquisa/topicos/previsibilidade-vs-velocidade.md) | D1, D2, D3 |
| 2 — É / Não é / Faz / Não faz | [impacto por item](pesquisa/impacto/impacto-por-item.md), [lacunas e diferencial](pesquisa/similares/lacunas-e-diferencial.md) | D4, D6, D7 |
| 3 — Visão do Produto | [impacto por item](pesquisa/impacto/impacto-por-item.md), [similares](pesquisa/similares/README.md), [matriz](pesquisa/similares/matriz-comparativa.md), [lacunas e diferencial](pesquisa/similares/lacunas-e-diferencial.md) | D2, D7 |
| 4 — BPMN TO BE | [atividades e dependências](pesquisa/topicos/atividades-e-dependencias.md), [caminho crítico](pesquisa/topicos/caminho-critico.md), [marcos](pesquisa/topicos/marcos-e-horarios.md) | D4, D5, D6, D7 |
| 5 — Atores | [papéis e atores](pesquisa/topicos/papeis-e-atores.md) | D4, D10 |
| 6 — RFs | [insumos para RFs](pesquisa/impacto/insumos-rfs.md) (linha da sua área) | D1, D3, D4, D5, D6, D7, D10, D11, D12 |
| 7 — Estórias | [tolerâncias](pesquisa/topicos/tolerancias-e-indicadores.md) (regras T8, T11, T12), [insumos para RFs](pesquisa/impacto/insumos-rfs.md) | D1, D3, D6, D7, D11, D12 |
| 8 — RNFs | [insumos para RNFs](pesquisa/impacto/insumos-rnfs.md) | D1, D11, D12 |
| 9 — Casos de uso | [papéis e atores](pesquisa/topicos/papeis-e-atores.md), [insumos para RFs](pesquisa/impacto/insumos-rfs.md) | D4, D10, D11 |
| 10 — Especificações de caso de uso | [atividades](pesquisa/topicos/atividades-e-dependencias.md), [caminho crítico](pesquisa/topicos/caminho-critico.md), [códigos de atraso](pesquisa/topicos/codigos-de-atraso.md) | D1, D3, D4, D5, D6, D7, D10, D11, D12 |
| 11 — Diagrama de atividades | [atividades](pesquisa/topicos/atividades-e-dependencias.md), [caminho crítico](pesquisa/topicos/caminho-critico.md), [papéis](pesquisa/topicos/papeis-e-atores.md) | D4, D5 |
