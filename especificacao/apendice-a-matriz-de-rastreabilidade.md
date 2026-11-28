# APÊNDICE A — MATRIZ DE RASTREABILIDADE

A matriz cruza os requisitos funcionais (item 6) com os objetivos (item 1), os atores (item 5), as estórias de usuário (item 7), os casos de uso (itens 9 e 10) e os requisitos não funcionais (item 8). Ela mostra que todo requisito funcional atende a um objetivo e tem estória e caso de uso, e que todo requisito não funcional se aplica a requisitos funcionais definidos (ADR-0012). Ela também liga cada requisito funcional às tabelas do modelo de dados (item 12), cada caso de uso aos seus diagramas de sequência (item 14) e cada critério de aceite das estórias aos casos de teste que o verificam (item 15) (ADR-0021).

As tabelas abaixo são **geradas** pelo script `scripts/gerar_matriz_rastreabilidade.py` a partir dos arquivos de área. Não edite o trecho entre os marcadores: altere os requisitos, as estórias, os casos de uso, o modelo de dados, os diagramas de sequência ou os casos de teste e rode o script de novo.

<!-- matriz:inicio -->
### A.1 Requisitos funcionais × títulos, objetivos, atores, estórias, casos de uso, RNFs e tabelas

| RF | Título | Objetivo | Ator / usuário | Estória | Caso(s) de uso | RNFs aplicáveis | Tabelas (item 12) |
|---|---|---|---|---|---|---|---|
| RF-1 | Autenticar acesso do usuário | Obj. 2 | Usuário | US001 | UC01 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-10, RNF-19, RNF-20 | falha_login (Cadastro e Planejamento), sessao (Cadastro e Planejamento), usuario (Cadastro e Planejamento) |
| RF-2 | Gerenciar cadastro de usuários e perfis | Obj. 2 | Administrador do Sistema | US002 | UC02 | RNF-1, RNF-2, RNF-3, RNF-4, RNF-5, RNF-6, RNF-18, RNF-19, RNF-20 | equipe (Cadastro e Planejamento), tarefa (Execução em Solo), tarefa_plano (Cadastro e Planejamento), usuario (Cadastro e Planejamento), usuario_vinculado (Cadastro e Planejamento) |
| RF-3 | Abrir turnaround da aeronave | Obj. 1 e 2 | Coordenador de Turnaround | US003 | UC03 | RNF-1, RNF-2, RNF-3, RNF-4, RNF-5, RNF-6, RNF-18, RNF-19, RNF-20 | companhia (Cadastro e Planejamento), turnaround (Cadastro e Planejamento) |
| RF-4 | Criar modelo de tarefas | Obj. 2 | Coordenador de Turnaround | US004 | UC04, UC05, UC20, UC25 | RNF-1, RNF-2, RNF-3, RNF-4, RNF-5, RNF-6, RNF-18, RNF-19, RNF-20 | dependencia_tarefa_modelo (Cadastro e Planejamento), equipe (Cadastro e Planejamento), modelo_tarefa (Cadastro e Planejamento), tarefa_modelo (Cadastro e Planejamento) |
| RF-5 | Confirmar plano inicial do turnaround | Obj. 1 e 2 | Coordenador de Turnaround | US005 | UC05, UC06, UC24 | RNF-1, RNF-2, RNF-3, RNF-4, RNF-5, RNF-6, RNF-18, RNF-19, RNF-20 | dependencia_tarefa_plano (Cadastro e Planejamento), equipe (Cadastro e Planejamento), plano (Cadastro e Planejamento), politica_abastecimento (Cadastro e Planejamento), tarefa_plano (Cadastro e Planejamento), usuario (Cadastro e Planejamento) |
| RF-6 | Aplicar modelo de tarefas | Obj. 2 | Coordenador de Turnaround | US006 | UC06 | RNF-1, RNF-2, RNF-3, RNF-4, RNF-5, RNF-6, RNF-18, RNF-19, RNF-20 | modelo_tarefa (Cadastro e Planejamento), plano (Cadastro e Planejamento), politica_abastecimento (Cadastro e Planejamento), ponto_confirmacao_plano (Cadastro e Planejamento), tarefa_modelo (Cadastro e Planejamento), tarefa_plano (Cadastro e Planejamento), turnaround (Cadastro e Planejamento) |
| RF-7 | Configurar pontos de confirmação das tarefas | Obj. 2 | Coordenador de Turnaround | US007 | UC07, UC19 | RNF-1, RNF-2, RNF-3, RNF-4, RNF-5, RNF-6, RNF-18, RNF-19, RNF-20 | ponto_confirmacao_modelo (Cadastro e Planejamento), ponto_confirmacao_plano (Cadastro e Planejamento), tarefa_modelo (Cadastro e Planejamento) |
| RF-8 | Definir dependências entre tarefas | Obj. 1 e 2 | Coordenador de Turnaround | US008 | UC05, UC08, UC35 | RNF-1, RNF-2, RNF-3, RNF-4, RNF-5, RNF-6, RNF-18, RNF-19, RNF-20 | dependencia_tarefa_modelo (Cadastro e Planejamento), dependencia_tarefa_plano (Cadastro e Planejamento), tarefa_modelo (Cadastro e Planejamento) |
| RF-9 | Gerenciar cadastro de equipes e especialidades | Obj. 2 | Administrador do Sistema | US009 | UC09 | RNF-1, RNF-2, RNF-3, RNF-4, RNF-5, RNF-6, RNF-18, RNF-19, RNF-20 | equipe (Cadastro e Planejamento), tarefa (Execução em Solo), tarefa_plano (Cadastro e Planejamento) |
| RF-10 | Atualizar referências de previsão do turnaround | Obj. 1 e 3 | Coordenador de Turnaround | US010 | UC10 | RNF-1, RNF-2, RNF-3, RNF-4, RNF-5, RNF-6, RNF-18, RNF-19, RNF-20 | turnaround (Cadastro e Planejamento) |
| RF-11 | Configurar política de abastecimento | Obj. 1 e 2 | Coordenador de Turnaround | US011 | UC05, UC11 | RNF-1, RNF-2, RNF-3, RNF-4, RNF-5, RNF-6, RNF-18, RNF-19, RNF-20 | companhia (Cadastro e Planejamento), plano (Cadastro e Planejamento), politica_abastecimento (Cadastro e Planejamento) |
| RF-12 | Registrar chegada da aeronave à posição | Obj. 1 e 2 | Operador de Solo/Rampa | US012 | UC10, UC12 | RNF-1, RNF-2, RNF-3, RNF-4, RNF-5, RNF-6, RNF-9, RNF-11, RNF-13, RNF-19, RNF-20 | historico_estado_turnaround (Execução em Solo), marco (Execução em Solo), turnaround (Execução em Solo) |
| RF-13 | Corrigir horário de chegada à posição | Obj. 1 e 2 | Coordenador de Turnaround | US013 | UC12, UC13 | RNF-1, RNF-2, RNF-3, RNF-4, RNF-5, RNF-6, RNF-18, RNF-19, RNF-20 | correcao_aibt (Execução em Solo), marco (Execução em Solo) |
| RF-14 | Consultar lista de tarefas do operador | Obj. 2 | Operador de Solo/Rampa | US014 | UC14 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-7, RNF-9, RNF-10, RNF-11, RNF-13, RNF-20 | dependencia_tarefa (Execução em Solo), tarefa (Execução em Solo), turnaround (Execução em Solo) |
| RF-15 | Registrar início da tarefa | Obj. 1 e 2 | Operador de Solo/Rampa | US015 | UC15 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-7, RNF-8, RNF-9, RNF-20 | historico_estado_tarefa (Execução em Solo), registro_tarefa (Execução em Solo), tarefa (Execução em Solo) |
| RF-16 | Registrar conclusão da tarefa | Obj. 1 e 2 | Operador de Solo/Rampa | US016 | UC16, UC19 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-7, RNF-8, RNF-9, RNF-20 | historico_estado_tarefa (Execução em Solo), leitura_qr_code (Execução em Solo), ponto_confirmacao (Execução em Solo), registro_tarefa (Execução em Solo), tarefa (Execução em Solo) |
| RF-17 | Pausar e retomar execução da tarefa | Obj. 2 e 3 | Operador de Solo/Rampa | US017 | UC17 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-7, RNF-8, RNF-9, RNF-20, RNF-22 | codigo_atraso (Execução em Solo), historico_estado_tarefa (Execução em Solo), registro_tarefa (Execução em Solo), tabela_codigo_atraso (Execução em Solo), tarefa (Execução em Solo) |
| RF-18 | Marcar tarefa como "Não aplicável" | Obj. 2 e 3 | Operador de Solo/Rampa | US018 | UC18 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-7, RNF-8, RNF-9, RNF-20 | historico_estado_tarefa (Execução em Solo), registro_tarefa (Execução em Solo), tarefa (Execução em Solo) |
| RF-19 | Confirmar execução da tarefa por QR Code | Obj. 2 | Operador de Solo/Rampa | US019 | UC16, UC19 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-7, RNF-8, RNF-9, RNF-20 | leitura_qr_code (Execução em Solo), ponto_confirmacao (Execução em Solo), tarefa (Execução em Solo) |
| RF-20 | Registrar marcos do atendimento em solo | Obj. 1 | Motor de Eventos | US020 | UC18, UC20 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-19, RNF-20 | marco (Execução em Solo), registro_tarefa (Execução em Solo) |
| RF-21 | Propagar estado das tarefas e do turnaround | Obj. 2 | Motor de Eventos | US021 | UC15, UC17, UC18, UC21 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-11, RNF-13, RNF-19, RNF-20 | dependencia_tarefa (Execução em Solo), historico_estado_tarefa (Execução em Solo), historico_estado_turnaround (Execução em Solo), tarefa (Execução em Solo), turnaround (Execução em Solo) |
| RF-22 | Recalcular projeção de prontidão | Obj. 1 e 3 | Motor de Eventos | US022 | UC24 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-12, RNF-13, RNF-19, RNF-20 | dependencia_monitorada (Monitoramento), projecao (Monitoramento), tarefa_monitorada (Monitoramento), turnaround_monitorado (Monitoramento) |
| RF-23 | Calcular atraso e impacto das tarefas | Obj. 1 e 3 | Motor de Eventos | US023 | UC23, UC24 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-12, RNF-13, RNF-19, RNF-20 | dependencia_monitorada (Monitoramento), projecao_tarefa (Monitoramento), tarefa_monitorada (Monitoramento) |
| RF-24 | Identificar caminho crítico do turnaround | Obj. 3 | Motor de Eventos | US024 | UC23, UC24 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-12, RNF-13, RNF-16, RNF-17, RNF-19, RNF-20 | caminho_critico (Monitoramento), caminho_critico_tarefa (Monitoramento), dependencia_monitorada (Monitoramento), tarefa_monitorada (Monitoramento) |
| RF-25 | Acompanhar painel dos turnarounds | Obj. 2 e 3 | Coordenador de Turnaround | US025 | UC22 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-11, RNF-13, RNF-14, RNF-15, RNF-16, RNF-17, RNF-18, RNF-19, RNF-20, RNF-21 | alerta (Monitoramento), projecao (Monitoramento), turnaround_monitorado (Monitoramento) |
| RF-26 | Consultar linha do tempo do turnaround | Obj. 1 e 2 | Coordenador de Turnaround | US026 | UC23 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-11, RNF-13, RNF-14, RNF-15, RNF-16, RNF-17, RNF-18, RNF-19, RNF-20 | aviso_checagem (Monitoramento), caminho_critico (Monitoramento), projecao (Monitoramento), projecao_tarefa (Monitoramento), tarefa_monitorada (Monitoramento), turnaround_monitorado (Monitoramento) |
| RF-27 | Emitir alerta de tarefa pronta não iniciada | Obj. 2 e 3 | Motor de Eventos | US027 | UC25, UC31 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-12, RNF-13, RNF-15, RNF-19, RNF-20, RNF-21 | alerta (Monitoramento), tarefa_monitorada (Monitoramento) |
| RF-28 | Emitir alerta de projeção além de TOBT + 5 | Obj. 3 | Motor de Eventos | US028 | UC25 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-12, RNF-13, RNF-15, RNF-19, RNF-20, RNF-21 | alerta (Monitoramento), alerta_tarefa (Monitoramento), projecao (Monitoramento), turnaround_monitorado (Monitoramento) |
| RF-29 | Verificar viabilidade do turnaround | Obj. 3 | Motor de Eventos | US029 | UC24, UC25 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-12, RNF-13, RNF-15, RNF-19, RNF-20 | alerta (Monitoramento), turnaround_monitorado (Monitoramento) |
| RF-30 | Emitir alerta de embarque não iniciado | Obj. 3 | Motor de Eventos | US030 | UC25 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-12, RNF-13, RNF-15, RNF-19, RNF-20, RNF-21 | alerta (Monitoramento), alerta_tarefa (Monitoramento), tarefa_monitorada (Monitoramento), turnaround_monitorado (Monitoramento) |
| RF-31 | Emitir alerta de prontidão não registrada | Obj. 3 | Motor de Eventos | US031 | UC25 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-12, RNF-13, RNF-15, RNF-19, RNF-20, RNF-21 | alerta (Monitoramento), alerta_tarefa (Monitoramento), tarefa_monitorada (Monitoramento), turnaround_monitorado (Monitoramento) |
| RF-32 | Exibir aviso de checagem em TOBT − 15 | Obj. 2 | Motor de Eventos | US032 | UC27 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-13, RNF-19, RNF-20, RNF-21 | aviso_checagem (Monitoramento), projecao_tarefa (Monitoramento), tarefa_monitorada (Monitoramento), turnaround_monitorado (Monitoramento) |
| RF-33 | Consultar lista de alertas abertos | Obj. 3 | Coordenador de Turnaround | US033 | UC22, UC25, UC26, UC31 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-11, RNF-13, RNF-14, RNF-15, RNF-16, RNF-17, RNF-18, RNF-19, RNF-20 | alerta (Monitoramento) |
| RF-34 | Consultar indicadores de aderência | Obj. 1 e 3 | Coordenador de Turnaround | US034 | UC28 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-13, RNF-14, RNF-18, RNF-19, RNF-20, RNF-21 | alerta (Monitoramento), atualizacao_tobt_monitorada (Monitoramento), tarefa_monitorada (Monitoramento), turnaround_monitorado (Monitoramento) |
| RF-35 | Registrar checagem com as equipes | Obj. 2 | Coordenador de Turnaround | US035 | UC27 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-13, RNF-18, RNF-19, RNF-20 | aviso_checagem (Monitoramento) |
| RF-36 | Abrir exceção do turnaround com código de atraso | Obj. 3 | Coordenador de Turnaround | US036 | UC29 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-18, RNF-19, RNF-20, RNF-22, RNF-24 | codigo_atraso (Exceções e Liberação), codigo_atraso (Execução em Solo), excecao (Exceções e Liberação), historico_estado_turnaround (Execução em Solo), tabela_codigo_atraso (Exceções e Liberação), tabela_codigo_atraso (Execução em Solo), turnaround (Execução em Solo), turnaround_referencia (Exceções e Liberação) |
| RF-37 | Reatribuir tarefa a outro operador da mesma equipe | Obj. 2 e 3 | Coordenador de Turnaround | US037 | UC19, UC30 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-18, RNF-19, RNF-20, RNF-24 | reatribuicao (Exceções e Liberação), tarefa (Execução em Solo), turnaround_referencia (Exceções e Liberação), usuario (Cadastro e Planejamento) |
| RF-38 | Registrar ação tomada para cada alerta | Obj. 3 | Coordenador de Turnaround | US038 | UC31 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-15, RNF-18, RNF-19, RNF-20, RNF-21, RNF-24 | acao_alerta (Exceções e Liberação), alerta (Monitoramento), atualizacao_tobt (Exceções e Liberação), reatribuicao (Exceções e Liberação), replanejamento (Exceções e Liberação), turnaround_referencia (Exceções e Liberação) |
| RF-39 | Confirmar prontidão e liberar aeronave | Obj. 3 | Autoridade de Liberação | US039 | UC32 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-18, RNF-19, RNF-20, RNF-23, RNF-24 | excecao (Exceções e Liberação), historico_estado_turnaround (Execução em Solo), liberacao (Exceções e Liberação), tarefa (Execução em Solo), turnaround (Execução em Solo), turnaround_referencia (Exceções e Liberação) |
| RF-40 | Encerrar exceção do turnaround | Obj. 3 | Coordenador de Turnaround | US040 | UC28, UC29, UC33 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-18, RNF-19, RNF-20, RNF-23, RNF-24 | excecao (Exceções e Liberação), historico_estado_turnaround (Execução em Solo), turnaround (Execução em Solo), turnaround_referencia (Exceções e Liberação) |
| RF-41 | Atualizar o TOBT quando a projeção se afasta 5 minutos ou mais | Obj. 1 | Coordenador de Turnaround | US041 | UC34 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-18, RNF-19, RNF-20, RNF-21, RNF-24 | atualizacao_tobt (Exceções e Liberação), projecao (Monitoramento), solicitacao_atualizacao_tobt (Exceções e Liberação), turnaround_referencia (Exceções e Liberação) |
| RF-42 | Replanejar tarefas não iniciadas do turnaround | Obj. 1 e 3 | Coordenador de Turnaround | US042 | UC35 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-18, RNF-19, RNF-20, RNF-24 | dependencia_tarefa (Execução em Solo), historico_estado_tarefa (Execução em Solo), politica_abastecimento (Cadastro e Planejamento), replanejamento (Exceções e Liberação), tarefa (Execução em Solo), turnaround (Execução em Solo), turnaround_referencia (Exceções e Liberação), usuario (Cadastro e Planejamento) |
| RF-43 | Consultar operadores disponíveis da equipe | Obj. 2 | Coordenador de Turnaround | US043 | UC36 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-18, RNF-19, RNF-20, RNF-24 | equipe (Cadastro e Planejamento), registro_tarefa (Execução em Solo), tarefa (Execução em Solo), usuario (Cadastro e Planejamento) |
| RF-44 | Registrar saída da posição e encerrar turnaround | Obj. 3 | Operador de Solo/Rampa | US044 | UC37 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-9, RNF-19, RNF-20, RNF-23, RNF-24 | historico_estado_turnaround (Execução em Solo), marco (Execução em Solo), turnaround (Execução em Solo) |

### A.2 Objetivos × requisitos funcionais

| Objetivo | RFs que o atendem |
|---|---|
| Objetivo 1 | RF-3, RF-5, RF-8, RF-10, RF-11, RF-12, RF-13, RF-15, RF-16, RF-20, RF-22, RF-23, RF-26, RF-34, RF-41, RF-42 |
| Objetivo 2 | RF-1, RF-2, RF-3, RF-4, RF-5, RF-6, RF-7, RF-8, RF-9, RF-11, RF-12, RF-13, RF-14, RF-15, RF-16, RF-17, RF-18, RF-19, RF-21, RF-25, RF-26, RF-27, RF-32, RF-35, RF-37, RF-43 |
| Objetivo 3 | RF-10, RF-17, RF-18, RF-22, RF-23, RF-24, RF-25, RF-27, RF-28, RF-29, RF-30, RF-31, RF-33, RF-34, RF-36, RF-37, RF-38, RF-39, RF-40, RF-42, RF-44 |

### A.3 Requisitos não funcionais × requisitos funcionais

| RNF | Característica ISO/IEC 25010 | RFs cobertos |
|---|---|---|
| RNF-1 | Segurança (confidencialidade e integridade) | todos os RFs |
| RNF-2 | Segurança (responsabilização e integridade) | todos os RFs |
| RNF-3 | Segurança (confidencialidade e autenticidade) | todos os RFs |
| RNF-4 | Compatibilidade (interoperabilidade) | RF-2, RF-3, RF-4, RF-5, RF-6, RF-7, RF-8, RF-9, RF-10, RF-11, RF-12, RF-13 |
| RNF-5 | Segurança (autenticidade e confidencialidade) | todos os RFs |
| RNF-6 | Segurança (confidencialidade e responsabilização) | todos os RFs |
| RNF-7 | Confiabilidade (disponibilidade) | RF-14, RF-15, RF-16, RF-17, RF-18, RF-19 |
| RNF-8 | Confiabilidade (tolerância a falhas) | RF-15, RF-16, RF-17, RF-18, RF-19 |
| RNF-9 | Portabilidade (adaptabilidade) | RF-12, RF-14, RF-15, RF-16, RF-17, RF-18, RF-19, RF-44 |
| RNF-10 | Portabilidade (instalabilidade) | RF-1, RF-14 |
| RNF-11 | Eficiência de desempenho (comportamento no tempo) | RF-12, RF-14, RF-21, RF-25, RF-26, RF-33 |
| RNF-12 | Eficiência de desempenho (comportamento no tempo) | RF-22, RF-23, RF-24, RF-27, RF-28, RF-29, RF-30, RF-31 |
| RNF-13 | Eficiência de desempenho (capacidade) | RF-12, RF-14, RF-21, RF-22, RF-23, RF-24, RF-25, RF-26, RF-27, RF-28, RF-29, RF-30, RF-31, RF-32, RF-33, RF-34, RF-35 |
| RNF-14 | Eficiência de desempenho (comportamento no tempo) | RF-25, RF-26, RF-33, RF-34 |
| RNF-15 | Usabilidade (operabilidade) | RF-25, RF-26, RF-27, RF-28, RF-29, RF-30, RF-31, RF-33, RF-38 |
| RNF-16 | Usabilidade (apreensibilidade) | RF-24, RF-25, RF-26, RF-33 |
| RNF-17 | Usabilidade (acessibilidade) | RF-24, RF-25, RF-26, RF-33 |
| RNF-18 | Usabilidade (operabilidade) | RF-2, RF-3, RF-4, RF-5, RF-6, RF-7, RF-8, RF-9, RF-10, RF-11, RF-13, RF-25, RF-26, RF-33, RF-34, RF-35, RF-36, RF-37, RF-38, RF-39, RF-40, RF-41, RF-42, RF-43 |
| RNF-19 | Confiabilidade (disponibilidade) | RF-1, RF-2, RF-3, RF-4, RF-5, RF-6, RF-7, RF-8, RF-9, RF-10, RF-11, RF-12, RF-13, RF-20, RF-21, RF-22, RF-23, RF-24, RF-25, RF-26, RF-27, RF-28, RF-29, RF-30, RF-31, RF-32, RF-33, RF-34, RF-35, RF-36, RF-37, RF-38, RF-39, RF-40, RF-41, RF-42, RF-43, RF-44 |
| RNF-20 | Confiabilidade (recuperabilidade) | todos os RFs |
| RNF-21 | Manutenibilidade (modificabilidade) | RF-25, RF-27, RF-28, RF-30, RF-31, RF-32, RF-34, RF-38, RF-41 |
| RNF-22 | Manutenibilidade (modificabilidade) | RF-17, RF-36 |
| RNF-23 | Manutenibilidade (testabilidade) | RF-39, RF-40, RF-44 |
| RNF-24 | Manutenibilidade (analisabilidade) | RF-36, RF-37, RF-38, RF-39, RF-40, RF-41, RF-42, RF-43, RF-44 |

### A.4 Casos de uso × diagramas de sequência (item 14)

| Caso de uso | Diagrama(s) de sequência |
|---|---|
| UC01 | — |
| UC02 | — |
| UC03 | — |
| UC04 | — |
| UC05 | — |
| UC06 | — |
| UC07 | — |
| UC08 | — |
| UC09 | — |
| UC10 | — |
| UC11 | — |
| UC12 | 14-sequencia-uc12.png |
| UC13 | 14-sequencia-uc13.png |
| UC14 | 14-sequencia-uc14.png |
| UC15 | 14-sequencia-uc15.png |
| UC16 | 14-sequencia-uc16.png |
| UC17 | 14-sequencia-uc17.png, 14-sequencia-uc17_001.png |
| UC18 | 14-sequencia-uc18.png |
| UC19 | 14-sequencia-uc19.png |
| UC20 | 14-sequencia-uc20.png |
| UC21 | 14-sequencia-uc21.png, 14-sequencia-uc21_001.png |
| UC22 | — |
| UC23 | — |
| UC24 | — |
| UC25 | — |
| UC26 | — |
| UC27 | — |
| UC28 | — |
| UC29 | — |
| UC30 | — |
| UC31 | — |
| UC32 | — |
| UC33 | — |
| UC34 | — |
| UC35 | — |
| UC36 | — |
| UC37 | 14-sequencia-uc37.png |

### A.5 Critérios de aceite × casos de teste (item 15)

| Critério de aceite | Casos de teste |
|---|---|
| US001-CA1 | CT-A001, CT-A002, CT-A003, CT-A004 |
| US001-CA2 | CT-A005, CT-A006, CT-A007, CT-A008, CT-A009, CT-A010 |
| US001-CA3 | CT-A011 |
| US001-CA4 | CT-A107 |
| US002-CA1 | CT-A012, CT-A024 |
| US002-CA2 | CT-A013 |
| US002-CA3 | CT-A019, CT-A021, CT-A022, CT-A023 |
| US002-CA4 | CT-A014, CT-A015 |
| US002-CA5 | CT-A016 |
| US002-CA6 | CT-A017, CT-A018, CT-A108 |
| US002-CA7 | CT-A020, CT-A021 |
| US002-CA8 | CT-A109 |
| US003-CA1 | CT-A025, CT-A028 |
| US003-CA2 | CT-A026, CT-A027, CT-A029, CT-A033 |
| US003-CA3 | CT-A030, CT-A031 |
| US003-CA4 | CT-A032 |
| US004-CA1 | CT-A034, CT-A036, CT-A042 |
| US004-CA2 | CT-A034 |
| US004-CA3 | CT-A037, CT-A038, CT-A041, CT-A111 |
| US004-CA4 | CT-A035 |
| US004-CA5 | CT-A039, CT-A040 |
| US004-CA6 | CT-A111 |
| US005-CA1 | CT-A043, CT-A044, CT-A051, CT-A054 |
| US005-CA2 | CT-A045, CT-A046 |
| US005-CA3 | CT-A047, CT-A048, CT-A049, CT-A053, CT-A080 |
| US005-CA4 | CT-A050 |
| US005-CA5 | CT-A052 |
| US006-CA1 | CT-A055 |
| US006-CA2 | CT-A058, CT-A063 |
| US006-CA3 | CT-A059, CT-A060, CT-A061, CT-A062, CT-A064 |
| US006-CA4 | CT-A056 |
| US006-CA5 | CT-A057 |
| US007-CA1 | CT-A065, CT-A066, CT-A072, CT-A073 |
| US007-CA2 | CT-A067 |
| US007-CA3 | CT-A066, CT-A068, CT-A069, CT-A070 |
| US007-CA4 | CT-A056, CT-A071 |
| US008-CA1 | CT-A074, CT-A082 |
| US008-CA2 | CT-A044, CT-A075 |
| US008-CA3 | CT-A076, CT-A077, CT-A078, CT-A079 |
| US008-CA4 | CT-A081 |
| US009-CA1 | CT-A083, CT-A091 |
| US009-CA2 | CT-A084 |
| US009-CA3 | CT-A085, CT-A110 |
| US009-CA4 | CT-A086, CT-A087, CT-A088, CT-A089, CT-A090 |
| US010-CA1 | CT-A092, CT-A098 |
| US010-CA2 | CT-A093 |
| US010-CA3 | CT-A094, CT-A095, CT-A096, CT-A097 |
| US011-CA1 | CT-A062, CT-A099, CT-A103 |
| US011-CA2 | CT-A100, CT-A104, CT-A105 |
| US011-CA3 | CT-A101, CT-A102, CT-A106 |
| US011-CA4 | CT-A049, CT-A079 |
| US012-CA1 | CT-B001, CT-B003, CT-B012 |
| US012-CA2 | CT-B006, CT-B007, CT-B011 |
| US012-CA3 | CT-B004, CT-B005 |
| US012-CA4 | CT-B002 |
| US012-CA5 | CT-B008, CT-B010 |
| US012-CA6 | CT-B009 |
| US013-CA1 | CT-B013, CT-B015, CT-B022, CT-B023 |
| US013-CA2 | CT-B018, CT-B019 |
| US013-CA3 | CT-B016, CT-B017 |
| US013-CA4 | CT-B020, CT-B021 |
| US013-CA5 | CT-B013 |
| US013-CA6 | CT-B014 |
| US014-CA1 | CT-B024, CT-B027, CT-B029, CT-B030, CT-B031 |
| US014-CA2 | CT-B026 |
| US014-CA3 | CT-B025, CT-B028, CT-B032, CT-B039, CT-B041, CT-B052 |
| US015-CA1 | CT-B033, CT-B034, CT-B035, CT-B036, CT-B039, CT-B040, CT-B041, CT-B042 |
| US015-CA2 | CT-B037, CT-B038 |
| US016-CA1 | CT-B043, CT-B044, CT-B045, CT-B046, CT-B047, CT-B049, CT-B050, CT-B052, CT-B053 |
| US016-CA2 | CT-B048 |
| US016-CA3 | CT-B045, CT-B051 |
| US017-CA1 | CT-B054, CT-B057, CT-B058, CT-B061, CT-B063 |
| US017-CA2 | CT-B056 |
| US017-CA3 | CT-B059 |
| US017-CA4 | CT-B060 |
| US017-CA5 | CT-B055, CT-B062 |
| US018-CA1 | CT-B064, CT-B065, CT-B066, CT-B067, CT-B071 |
| US018-CA2 | CT-B069, CT-B070, CT-B116 |
| US018-CA3 | CT-B068 |
| US019-CA1 | CT-B072, CT-B073, CT-B074, CT-B081, CT-B112 |
| US019-CA2 | CT-B075, CT-B076, CT-B077, CT-B079, CT-B080 |
| US019-CA3 | CT-B078 |
| US019-CA4 | CT-B082, CT-B110, CT-B111 |
| US020-CA1 | CT-B035, CT-B083, CT-B089, CT-B090, CT-B113 |
| US020-CA2 | CT-B036, CT-B084 |
| US020-CA3 | CT-B047, CT-B086, CT-B088, CT-B114, CT-B115 |
| US020-CA4 | CT-B085 |
| US020-CA5 | CT-B067, CT-B087 |
| US021-CA1 | CT-B035, CT-B092, CT-B101 |
| US021-CA2 | CT-B046, CT-B091, CT-B096, CT-B097, CT-B100, CT-B102 |
| US021-CA3 | CT-B093 |
| US021-CA4 | CT-B066, CT-B094 |
| US021-CA5 | CT-B047, CT-B095 |
| US021-CA6 | CT-B098 |
| US021-CA7 | CT-B099 |
| US021-CA8 | CT-B117 |
| US021-CA9 | CT-B119 |
| US021-CA10 | CT-B118 |
| US022-CA1 | CT-C004, CT-C023, CT-C033, CT-C034, CT-C035, CT-C037, CT-C038 |
| US022-CA2 | CT-C030 |
| US022-CA3 | CT-C032 |
| US022-CA4 | CT-C036 |
| US022-CA5 | CT-C029 |
| US023-CA1 | CT-C024 |
| US023-CA2 | CT-C025, CT-C031 |
| US023-CA3 | CT-C027 |
| US023-CA4 | CT-C028 |
| US024-CA1 | CT-C026 |
| US024-CA2 | CT-C018, CT-C030, CT-C031 |
| US024-CA3 | CT-C032 |
| US025-CA1 | CT-C001, CT-C002, CT-C003, CT-C004, CT-C009, CT-C011 |
| US025-CA2 | CT-C007, CT-C010 |
| US025-CA3 | CT-C008 |
| US025-CA4 | CT-C012 |
| US026-CA1 | CT-C005, CT-C013, CT-C017, CT-C018, CT-C022 |
| US026-CA2 | CT-C014, CT-C019 |
| US026-CA3 | CT-C015 |
| US026-CA4 | CT-C016, CT-C020, CT-C021 |
| US027-CA1 | CT-C050, CT-C051, CT-C059 |
| US027-CA2 | CT-C052 |
| US027-CA3 | CT-C053 |
| US027-CA4 | CT-C089 |
| US028-CA1 | CT-C045 |
| US028-CA2 | CT-C046 |
| US028-CA3 | CT-C047, CT-C048 |
| US028-CA4 | CT-C049 |
| US029-CA1 | CT-C039, CT-C041, CT-C043, CT-C060 |
| US029-CA2 | CT-C040, CT-C042 |
| US029-CA3 | CT-C044 |
| US030-CA1 | CT-C054 |
| US030-CA2 | CT-C055 |
| US030-CA3 | CT-C056 |
| US030-CA4 | CT-C090 |
| US030-CA5 | CT-C095 |
| US030-CA6 | CT-C096 |
| US031-CA1 | CT-C057 |
| US031-CA2 | CT-C057 |
| US031-CA3 | CT-C058 |
| US031-CA4 | CT-C090 |
| US032-CA1 | CT-C071, CT-C077 |
| US032-CA2 | CT-C076 |
| US032-CA3 | CT-C072 |
| US032-CA4 | CT-C078 |
| US032-CA5 | CT-C091 |
| US032-CA6 | CT-C092 |
| US033-CA1 | CT-C006, CT-C061, CT-C063, CT-C065, CT-C066, CT-C068, CT-C070 |
| US033-CA2 | CT-C050, CT-C051, CT-C062 |
| US033-CA3 | CT-C064, CT-C069 |
| US033-CA4 | CT-C067 |
| US034-CA1 | CT-C080, CT-C083, CT-C084, CT-C086, CT-C088, CT-C093 |
| US034-CA2 | CT-C081 |
| US034-CA3 | CT-C082, CT-C093 |
| US034-CA4 | CT-C085 |
| US034-CA5 | CT-C087 |
| US035-CA1 | CT-C073, CT-C075 |
| US035-CA2 | CT-C079 |
| US035-CA3 | CT-C074 |
| US036-CA1 | CT-D001, CT-D005, CT-D006, CT-D021 |
| US036-CA2 | CT-D002, CT-D003 |
| US036-CA3 | CT-D004 |
| US037-CA1 | CT-D008, CT-D009, CT-D010, CT-D011, CT-D015 |
| US037-CA2 | CT-D012 |
| US037-CA3 | CT-D013, CT-D014, CT-D025, CT-D071 |
| US037-CA4 | CT-D017 |
| US038-CA1 | CT-D005, CT-D009, CT-D018, CT-D019, CT-D020, CT-D021, CT-D026, CT-D047, CT-D056 |
| US038-CA2 | CT-D023, CT-D024, CT-D025 |
| US038-CA3 | CT-C094, CT-D022 |
| US039-CA1 | CT-D007, CT-D028, CT-D034, CT-D051 |
| US039-CA2 | CT-D030, CT-D032 |
| US039-CA3 | CT-D029, CT-D033 |
| US039-CA4 | CT-D027, CT-D031 |
| US040-CA1 | CT-D035, CT-D041 |
| US040-CA2 | CT-D036 |
| US040-CA3 | CT-D039, CT-D040 |
| US040-CA4 | CT-D037 |
| US040-CA5 | CT-D038 |
| US041-CA1 | CT-D042, CT-D048 |
| US041-CA2 | CT-D044, CT-D050, CT-D051 |
| US041-CA3 | CT-D020, CT-D043, CT-D045, CT-D047, CT-D049 |
| US041-CA4 | CT-D046, CT-D050 |
| US042-CA1 | CT-D052, CT-D056, CT-D057, CT-D059 |
| US042-CA2 | CT-D058 |
| US042-CA3 | CT-D053, CT-D054 |
| US042-CA4 | CT-D055, CT-D062, CT-D063, CT-D064 |
| US042-CA5 | CT-D060 |
| US042-CA6 | CT-D061 |
| US043-CA1 | CT-D065, CT-D069, CT-D071 |
| US043-CA2 | CT-D066 |
| US043-CA3 | CT-D016, CT-D068, CT-D070 |
| US043-CA4 | CT-D067 |
| US044-CA1 | CT-B103, CT-B104, CT-B109 |
| US044-CA2 | CT-B106 |
| US044-CA3 | CT-B105, CT-B107, CT-B108 |

### A.6 Lacunas encontradas

- UC01 sem diagrama de sequência (item 14)
- UC02 sem diagrama de sequência (item 14)
- UC03 sem diagrama de sequência (item 14)
- UC04 sem diagrama de sequência (item 14)
- UC05 sem diagrama de sequência (item 14)
- UC06 sem diagrama de sequência (item 14)
- UC07 sem diagrama de sequência (item 14)
- UC08 sem diagrama de sequência (item 14)
- UC09 sem diagrama de sequência (item 14)
- UC10 sem diagrama de sequência (item 14)
- UC11 sem diagrama de sequência (item 14)
- UC22 sem diagrama de sequência (item 14)
- UC23 sem diagrama de sequência (item 14)
- UC24 sem diagrama de sequência (item 14)
- UC25 sem diagrama de sequência (item 14)
- UC26 sem diagrama de sequência (item 14)
- UC27 sem diagrama de sequência (item 14)
- UC28 sem diagrama de sequência (item 14)
- UC29 sem diagrama de sequência (item 14)
- UC30 sem diagrama de sequência (item 14)
- UC31 sem diagrama de sequência (item 14)
- UC32 sem diagrama de sequência (item 14)
- UC33 sem diagrama de sequência (item 14)
- UC34 sem diagrama de sequência (item 14)
- UC35 sem diagrama de sequência (item 14)
- UC36 sem diagrama de sequência (item 14)
<!-- matriz:fim -->
