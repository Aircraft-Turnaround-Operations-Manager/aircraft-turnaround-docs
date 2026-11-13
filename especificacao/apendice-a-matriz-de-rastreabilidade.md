# APÊNDICE A — MATRIZ DE RASTREABILIDADE

A matriz cruza os requisitos funcionais (item 6) com os objetivos (item 1), os atores (item 5), as estórias de usuário (item 7), os casos de uso (itens 9 e 10) e os requisitos não funcionais (item 8). Ela mostra que todo requisito funcional atende a um objetivo e tem estória e caso de uso, e que todo requisito não funcional se aplica a requisitos funcionais definidos (ADR-0012). Ela também liga cada requisito funcional às tabelas do modelo de dados (item 12), cada caso de uso aos seus diagramas de sequência (item 14) e cada critério de aceite das estórias aos casos de teste que o verificam (item 15).

As tabelas abaixo são **geradas** pelo script `scripts/gerar_matriz_rastreabilidade.py` a partir dos arquivos de área. Não edite o trecho entre os marcadores: altere os requisitos, as estórias, os casos de uso, o modelo de dados, os diagramas de sequência ou os casos de teste e rode o script de novo.

<!-- matriz:inicio -->
### A.1 Requisitos funcionais × títulos, objetivos, atores, estórias, casos de uso, RNFs e tabelas

| RF | Título | Objetivo | Ator / usuário | Estória | Caso(s) de uso | RNFs aplicáveis | Tabelas (item 12) |
|---|---|---|---|---|---|---|---|
| RF-1 | Autenticar acesso do usuário | Obj. 2 | Usuário | US001 | UC01 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-10, RNF-19, RNF-20 | — |
| RF-2 | Gerenciar cadastro de usuários e perfis | Obj. 2 | Administrador do Sistema | US002 | UC02 | RNF-1, RNF-2, RNF-3, RNF-4, RNF-5, RNF-6, RNF-18, RNF-19, RNF-20 | — |
| RF-3 | Abrir turnaround da aeronave | Obj. 1 e 2 | Coordenador de Turnaround | US003 | UC03 | RNF-1, RNF-2, RNF-3, RNF-4, RNF-5, RNF-6, RNF-18, RNF-19, RNF-20 | — |
| RF-4 | Criar modelo de tarefas | Obj. 2 | Coordenador de Turnaround | US004 | UC04, UC05 | RNF-1, RNF-2, RNF-3, RNF-4, RNF-5, RNF-6, RNF-18, RNF-19, RNF-20 | — |
| RF-5 | Confirmar plano inicial do turnaround | Obj. 1 e 2 | Coordenador de Turnaround | US005 | UC05, UC06 | RNF-1, RNF-2, RNF-3, RNF-4, RNF-5, RNF-6, RNF-18, RNF-19, RNF-20 | — |
| RF-6 | Aplicar modelo de tarefas | Obj. 2 | Coordenador de Turnaround | US006 | UC06 | RNF-1, RNF-2, RNF-3, RNF-4, RNF-5, RNF-6, RNF-18, RNF-19, RNF-20 | — |
| RF-7 | Configurar pontos de confirmação das tarefas | Obj. 2 | Coordenador de Turnaround | US007 | UC07 | RNF-1, RNF-2, RNF-3, RNF-4, RNF-5, RNF-6, RNF-18, RNF-19, RNF-20 | — |
| RF-8 | Definir dependências entre tarefas | Obj. 1 e 2 | Coordenador de Turnaround | US008 | UC05, UC08 | RNF-1, RNF-2, RNF-3, RNF-4, RNF-5, RNF-6, RNF-18, RNF-19, RNF-20 | — |
| RF-9 | Gerenciar cadastro de equipes e especialidades | Obj. 2 | Administrador do Sistema | US009 | UC09 | RNF-1, RNF-2, RNF-3, RNF-4, RNF-5, RNF-6, RNF-18, RNF-19, RNF-20 | — |
| RF-10 | Atualizar referências de previsão do turnaround | Obj. 1 e 3 | Coordenador de Turnaround | US010 | UC10 | RNF-1, RNF-2, RNF-3, RNF-4, RNF-5, RNF-6, RNF-18, RNF-19, RNF-20 | — |
| RF-11 | Configurar política de abastecimento | Obj. 1 e 2 | Coordenador de Turnaround | US011 | UC05, UC11 | RNF-1, RNF-2, RNF-3, RNF-4, RNF-5, RNF-6, RNF-18, RNF-19, RNF-20 | — |
| RF-12 | Registrar chegada da aeronave à posição | Obj. 1 e 2 | Operador de Solo/Rampa | US012 | UC10, UC12 | RNF-1, RNF-2, RNF-3, RNF-4, RNF-5, RNF-6, RNF-9, RNF-11, RNF-19, RNF-20 | — |
| RF-13 | Corrigir horário de chegada à posição | Obj. 1 e 2 | Coordenador de Turnaround | US013 | UC12, UC13 | RNF-1, RNF-2, RNF-3, RNF-4, RNF-5, RNF-6, RNF-18, RNF-19, RNF-20 | — |
| RF-14 | Consultar lista de tarefas do operador | Obj. 2 | Operador de Solo/Rampa | US014 | UC14 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-7, RNF-9, RNF-10, RNF-11, RNF-20 | — |
| RF-15 | Registrar início da tarefa | Obj. 1 e 2 | Operador de Solo/Rampa | US015 | UC15 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-7, RNF-8, RNF-9, RNF-20 | — |
| RF-16 | Registrar conclusão da tarefa | Obj. 1 e 2 | Operador de Solo/Rampa | US016 | UC16, UC19 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-7, RNF-8, RNF-9, RNF-20 | — |
| RF-17 | Pausar e retomar execução da tarefa | Obj. 2 e 3 | Operador de Solo/Rampa | US017 | UC17 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-7, RNF-8, RNF-9, RNF-20, RNF-22 | — |
| RF-18 | Marcar tarefa como "Não aplicável" | Obj. 2 e 3 | Operador de Solo/Rampa | US018 | UC18 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-7, RNF-8, RNF-9, RNF-20 | — |
| RF-19 | Confirmar execução da tarefa por QR Code | Obj. 2 | Operador de Solo/Rampa | US019 | UC16, UC19 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-7, RNF-8, RNF-9, RNF-20 | — |
| RF-20 | Registrar marcos do atendimento em solo | Obj. 1 | Motor de Eventos | US020 | UC18, UC20 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-19, RNF-20 | — |
| RF-21 | Propagar estado das tarefas e do turnaround | Obj. 2 | Motor de Eventos | US021 | UC15, UC17, UC18, UC21 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-11, RNF-19, RNF-20 | — |
| RF-22 | Recalcular projeção de prontidão | Obj. 1 e 3 | Motor de Eventos | US022 | UC24 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-12, RNF-13, RNF-19, RNF-20 | — |
| RF-23 | Calcular atraso e impacto das tarefas | Obj. 1 e 3 | Motor de Eventos | US023 | UC23, UC24 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-12, RNF-13, RNF-19, RNF-20 | — |
| RF-24 | Identificar caminho crítico do turnaround | Obj. 3 | Motor de Eventos | US024 | UC23, UC24 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-12, RNF-13, RNF-16, RNF-17, RNF-19, RNF-20 | — |
| RF-25 | Acompanhar painel dos turnarounds | Obj. 2 e 3 | Coordenador de Turnaround | US025 | UC22 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-11, RNF-13, RNF-14, RNF-15, RNF-16, RNF-17, RNF-18, RNF-19, RNF-20, RNF-21 | — |
| RF-26 | Consultar linha do tempo do turnaround | Obj. 1 e 2 | Coordenador de Turnaround | US026 | UC23 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-11, RNF-13, RNF-14, RNF-15, RNF-16, RNF-17, RNF-18, RNF-19, RNF-20 | — |
| RF-27 | Emitir alerta de tarefa pronta não iniciada | Obj. 2 e 3 | Motor de Eventos | US027 | UC25, UC31 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-12, RNF-13, RNF-15, RNF-19, RNF-20, RNF-21 | — |
| RF-28 | Emitir alerta de projeção além de TOBT + 5 | Obj. 3 | Motor de Eventos | US028 | UC25 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-12, RNF-13, RNF-15, RNF-19, RNF-20, RNF-21 | — |
| RF-29 | Verificar viabilidade do turnaround | Obj. 3 | Motor de Eventos | US029 | UC24, UC25 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-12, RNF-13, RNF-15, RNF-19, RNF-20 | — |
| RF-30 | Emitir alerta de embarque não iniciado | Obj. 3 | Motor de Eventos | US030 | UC25 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-12, RNF-13, RNF-15, RNF-19, RNF-20, RNF-21 | — |
| RF-31 | Emitir alerta de prontidão não registrada | Obj. 3 | Motor de Eventos | US031 | UC25 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-12, RNF-13, RNF-15, RNF-19, RNF-20, RNF-21 | — |
| RF-32 | Exibir aviso de checagem em TOBT − 15 | Obj. 2 | Motor de Eventos | US032 | UC27 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-13, RNF-19, RNF-20, RNF-21 | — |
| RF-33 | Consultar lista de alertas abertos | Obj. 3 | Coordenador de Turnaround | US033 | UC22, UC25, UC26, UC31 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-11, RNF-13, RNF-14, RNF-15, RNF-16, RNF-17, RNF-18, RNF-19, RNF-20 | — |
| RF-34 | Consultar indicadores de aderência | Obj. 1 e 3 | Coordenador de Turnaround | US034 | UC28 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-13, RNF-14, RNF-18, RNF-19, RNF-20, RNF-21 | — |
| RF-35 | Registrar checagem com as equipes | Obj. 2 | Coordenador de Turnaround | US035 | UC27 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-13, RNF-18, RNF-19, RNF-20 | — |
| RF-36 | Abrir exceção do turnaround com código de atraso | Obj. 3 | Coordenador de Turnaround | US036 | UC29 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-18, RNF-19, RNF-20, RNF-22, RNF-24 | — |
| RF-37 | Reatribuir tarefa a outro operador da mesma equipe | Obj. 2 e 3 | Coordenador de Turnaround | US037 | UC30 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-18, RNF-19, RNF-20, RNF-24 | — |
| RF-38 | Registrar ação tomada para cada alerta | Obj. 3 | Coordenador de Turnaround | US038 | UC31 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-15, RNF-18, RNF-19, RNF-20, RNF-21, RNF-24 | — |
| RF-39 | Confirmar prontidão e liberar aeronave | Obj. 3 | Autoridade de Liberação | US039 | UC32 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-18, RNF-19, RNF-20, RNF-23, RNF-24 | — |
| RF-40 | Encerrar exceção do turnaround | Obj. 3 | Coordenador de Turnaround | US040 | UC33 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-18, RNF-19, RNF-20, RNF-23, RNF-24 | — |
| RF-41 | Atualizar o TOBT quando a projeção se afasta 5 minutos ou mais | Obj. 1 | Coordenador de Turnaround | US041 | UC34 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-18, RNF-19, RNF-20, RNF-21, RNF-24 | — |
| RF-42 | Replanejar tarefas não iniciadas do turnaround | Obj. 1 e 3 | Coordenador de Turnaround | US042 | UC35 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-18, RNF-19, RNF-20, RNF-24 | — |
| RF-43 | Consultar operadores disponíveis da equipe | Obj. 2 | Coordenador de Turnaround | US043 | UC36 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-18, RNF-19, RNF-20, RNF-24 | — |
| RF-44 | Registrar saída da posição e encerrar turnaround | Obj. 3 | Operador de Solo/Rampa | US044 | UC37 | RNF-1, RNF-2, RNF-3, RNF-5, RNF-6, RNF-9, RNF-19, RNF-20, RNF-23, RNF-24 | — |

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
| RNF-13 | Eficiência de desempenho (capacidade) | RF-22, RF-23, RF-24, RF-25, RF-26, RF-27, RF-28, RF-29, RF-30, RF-31, RF-32, RF-33, RF-34, RF-35 |
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
| UC12 | — |
| UC13 | — |
| UC14 | — |
| UC15 | — |
| UC16 | — |
| UC17 | — |
| UC18 | — |
| UC19 | — |
| UC20 | — |
| UC21 | — |
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
| UC37 | — |

### A.5 Critérios de aceite × casos de teste (item 15)

| Critério de aceite | Casos de teste |
|---|---|
| US001-CA1 | CT-A001, CT-A002, CT-A003, CT-A004 |
| US001-CA2 | CT-A005, CT-A006, CT-A007, CT-A008, CT-A009, CT-A010 |
| US001-CA3 | CT-A011 |
| US002-CA1 | CT-A012, CT-A024 |
| US002-CA2 | CT-A013 |
| US002-CA3 | CT-A019, CT-A021, CT-A022, CT-A023 |
| US002-CA4 | CT-A014, CT-A015 |
| US002-CA5 | CT-A016 |
| US002-CA6 | CT-A017, CT-A018 |
| US002-CA7 | CT-A020, CT-A021 |
| US003-CA1 | CT-A025, CT-A028 |
| US003-CA2 | CT-A026, CT-A027, CT-A029, CT-A033 |
| US003-CA3 | CT-A030, CT-A031 |
| US003-CA4 | CT-A032 |
| US004-CA1 | CT-A034, CT-A036, CT-A042 |
| US004-CA2 | CT-A034 |
| US004-CA3 | CT-A037, CT-A038, CT-A041 |
| US004-CA4 | CT-A035 |
| US004-CA5 | CT-A039, CT-A040 |
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
| US009-CA3 | CT-A085 |
| US009-CA4 | CT-A086, CT-A087, CT-A088, CT-A089, CT-A090 |
| US010-CA1 | CT-A092, CT-A098 |
| US010-CA2 | CT-A093 |
| US010-CA3 | CT-A094, CT-A095, CT-A096, CT-A097 |
| US011-CA1 | CT-A062, CT-A099, CT-A103 |
| US011-CA2 | CT-A100, CT-A104, CT-A105 |
| US011-CA3 | CT-A101, CT-A102, CT-A106 |
| US011-CA4 | CT-A049, CT-A079 |
| US012-CA1 | — |
| US012-CA2 | — |
| US012-CA3 | — |
| US012-CA4 | — |
| US012-CA5 | — |
| US012-CA6 | — |
| US013-CA1 | — |
| US013-CA2 | — |
| US013-CA3 | — |
| US013-CA4 | — |
| US013-CA5 | — |
| US013-CA6 | — |
| US014-CA1 | — |
| US014-CA2 | — |
| US014-CA3 | — |
| US015-CA1 | — |
| US015-CA2 | — |
| US016-CA1 | — |
| US016-CA2 | — |
| US016-CA3 | — |
| US017-CA1 | — |
| US017-CA2 | — |
| US017-CA3 | — |
| US017-CA4 | — |
| US017-CA5 | — |
| US018-CA1 | — |
| US018-CA2 | — |
| US018-CA3 | — |
| US019-CA1 | — |
| US019-CA2 | — |
| US019-CA3 | — |
| US019-CA4 | — |
| US020-CA1 | — |
| US020-CA2 | — |
| US020-CA3 | — |
| US020-CA4 | — |
| US020-CA5 | — |
| US021-CA1 | — |
| US021-CA2 | — |
| US021-CA3 | — |
| US021-CA4 | — |
| US021-CA5 | — |
| US021-CA6 | — |
| US021-CA7 | — |
| US022-CA1 | — |
| US022-CA2 | — |
| US022-CA3 | — |
| US022-CA4 | — |
| US022-CA5 | — |
| US023-CA1 | — |
| US023-CA2 | — |
| US023-CA3 | — |
| US023-CA4 | — |
| US024-CA1 | — |
| US024-CA2 | — |
| US024-CA3 | — |
| US025-CA1 | — |
| US025-CA2 | — |
| US025-CA3 | — |
| US025-CA4 | — |
| US026-CA1 | — |
| US026-CA2 | — |
| US026-CA3 | — |
| US026-CA4 | — |
| US027-CA1 | — |
| US027-CA2 | — |
| US027-CA3 | — |
| US028-CA1 | — |
| US028-CA2 | — |
| US028-CA3 | — |
| US028-CA4 | — |
| US029-CA1 | — |
| US029-CA2 | — |
| US029-CA3 | — |
| US030-CA1 | — |
| US030-CA2 | — |
| US030-CA3 | — |
| US031-CA1 | — |
| US031-CA2 | — |
| US031-CA3 | — |
| US032-CA1 | — |
| US032-CA2 | — |
| US032-CA3 | — |
| US032-CA4 | — |
| US033-CA1 | — |
| US033-CA2 | — |
| US033-CA3 | — |
| US033-CA4 | — |
| US034-CA1 | — |
| US034-CA2 | — |
| US034-CA3 | — |
| US034-CA4 | — |
| US034-CA5 | — |
| US035-CA1 | — |
| US035-CA2 | — |
| US035-CA3 | — |
| US036-CA1 | — |
| US036-CA2 | — |
| US036-CA3 | — |
| US037-CA1 | — |
| US037-CA2 | — |
| US037-CA3 | — |
| US037-CA4 | — |
| US038-CA1 | — |
| US038-CA2 | — |
| US038-CA3 | — |
| US039-CA1 | — |
| US039-CA2 | — |
| US039-CA3 | — |
| US039-CA4 | — |
| US040-CA1 | — |
| US040-CA2 | — |
| US040-CA3 | — |
| US040-CA4 | — |
| US040-CA5 | — |
| US041-CA1 | — |
| US041-CA2 | — |
| US041-CA3 | — |
| US041-CA4 | — |
| US042-CA1 | — |
| US042-CA2 | — |
| US042-CA3 | — |
| US042-CA4 | — |
| US042-CA5 | — |
| US042-CA6 | — |
| US043-CA1 | — |
| US043-CA2 | — |
| US043-CA3 | — |
| US044-CA1 | — |
| US044-CA2 | — |
| US044-CA3 | — |

### A.6 Lacunas encontradas

- US012-CA1 sem caso de teste (item 15)
- US012-CA2 sem caso de teste (item 15)
- US012-CA3 sem caso de teste (item 15)
- US012-CA4 sem caso de teste (item 15)
- US012-CA5 sem caso de teste (item 15)
- US012-CA6 sem caso de teste (item 15)
- US013-CA1 sem caso de teste (item 15)
- US013-CA2 sem caso de teste (item 15)
- US013-CA3 sem caso de teste (item 15)
- US013-CA4 sem caso de teste (item 15)
- US013-CA5 sem caso de teste (item 15)
- US013-CA6 sem caso de teste (item 15)
- US014-CA1 sem caso de teste (item 15)
- US014-CA2 sem caso de teste (item 15)
- US014-CA3 sem caso de teste (item 15)
- US015-CA1 sem caso de teste (item 15)
- US015-CA2 sem caso de teste (item 15)
- US016-CA1 sem caso de teste (item 15)
- US016-CA2 sem caso de teste (item 15)
- US016-CA3 sem caso de teste (item 15)
- US017-CA1 sem caso de teste (item 15)
- US017-CA2 sem caso de teste (item 15)
- US017-CA3 sem caso de teste (item 15)
- US017-CA4 sem caso de teste (item 15)
- US017-CA5 sem caso de teste (item 15)
- US018-CA1 sem caso de teste (item 15)
- US018-CA2 sem caso de teste (item 15)
- US018-CA3 sem caso de teste (item 15)
- US019-CA1 sem caso de teste (item 15)
- US019-CA2 sem caso de teste (item 15)
- US019-CA3 sem caso de teste (item 15)
- US019-CA4 sem caso de teste (item 15)
- US020-CA1 sem caso de teste (item 15)
- US020-CA2 sem caso de teste (item 15)
- US020-CA3 sem caso de teste (item 15)
- US020-CA4 sem caso de teste (item 15)
- US020-CA5 sem caso de teste (item 15)
- US021-CA1 sem caso de teste (item 15)
- US021-CA2 sem caso de teste (item 15)
- US021-CA3 sem caso de teste (item 15)
- US021-CA4 sem caso de teste (item 15)
- US021-CA5 sem caso de teste (item 15)
- US021-CA6 sem caso de teste (item 15)
- US021-CA7 sem caso de teste (item 15)
- US044-CA1 sem caso de teste (item 15)
- US044-CA2 sem caso de teste (item 15)
- US044-CA3 sem caso de teste (item 15)
- US022-CA1 sem caso de teste (item 15)
- US022-CA2 sem caso de teste (item 15)
- US022-CA3 sem caso de teste (item 15)
- US022-CA4 sem caso de teste (item 15)
- US022-CA5 sem caso de teste (item 15)
- US023-CA1 sem caso de teste (item 15)
- US023-CA2 sem caso de teste (item 15)
- US023-CA3 sem caso de teste (item 15)
- US023-CA4 sem caso de teste (item 15)
- US024-CA1 sem caso de teste (item 15)
- US024-CA2 sem caso de teste (item 15)
- US024-CA3 sem caso de teste (item 15)
- US025-CA1 sem caso de teste (item 15)
- US025-CA2 sem caso de teste (item 15)
- US025-CA3 sem caso de teste (item 15)
- US025-CA4 sem caso de teste (item 15)
- US026-CA1 sem caso de teste (item 15)
- US026-CA2 sem caso de teste (item 15)
- US026-CA3 sem caso de teste (item 15)
- US026-CA4 sem caso de teste (item 15)
- US027-CA1 sem caso de teste (item 15)
- US027-CA2 sem caso de teste (item 15)
- US027-CA3 sem caso de teste (item 15)
- US028-CA1 sem caso de teste (item 15)
- US028-CA2 sem caso de teste (item 15)
- US028-CA3 sem caso de teste (item 15)
- US028-CA4 sem caso de teste (item 15)
- US029-CA1 sem caso de teste (item 15)
- US029-CA2 sem caso de teste (item 15)
- US029-CA3 sem caso de teste (item 15)
- US030-CA1 sem caso de teste (item 15)
- US030-CA2 sem caso de teste (item 15)
- US030-CA3 sem caso de teste (item 15)
- US031-CA1 sem caso de teste (item 15)
- US031-CA2 sem caso de teste (item 15)
- US031-CA3 sem caso de teste (item 15)
- US032-CA1 sem caso de teste (item 15)
- US032-CA2 sem caso de teste (item 15)
- US032-CA3 sem caso de teste (item 15)
- US032-CA4 sem caso de teste (item 15)
- US033-CA1 sem caso de teste (item 15)
- US033-CA2 sem caso de teste (item 15)
- US033-CA3 sem caso de teste (item 15)
- US033-CA4 sem caso de teste (item 15)
- US034-CA1 sem caso de teste (item 15)
- US034-CA2 sem caso de teste (item 15)
- US034-CA3 sem caso de teste (item 15)
- US034-CA4 sem caso de teste (item 15)
- US034-CA5 sem caso de teste (item 15)
- US035-CA1 sem caso de teste (item 15)
- US035-CA2 sem caso de teste (item 15)
- US035-CA3 sem caso de teste (item 15)
- US036-CA1 sem caso de teste (item 15)
- US036-CA2 sem caso de teste (item 15)
- US036-CA3 sem caso de teste (item 15)
- US037-CA1 sem caso de teste (item 15)
- US037-CA2 sem caso de teste (item 15)
- US037-CA3 sem caso de teste (item 15)
- US037-CA4 sem caso de teste (item 15)
- US038-CA1 sem caso de teste (item 15)
- US038-CA2 sem caso de teste (item 15)
- US038-CA3 sem caso de teste (item 15)
- US039-CA1 sem caso de teste (item 15)
- US039-CA2 sem caso de teste (item 15)
- US039-CA3 sem caso de teste (item 15)
- US039-CA4 sem caso de teste (item 15)
- US040-CA1 sem caso de teste (item 15)
- US040-CA2 sem caso de teste (item 15)
- US040-CA3 sem caso de teste (item 15)
- US040-CA4 sem caso de teste (item 15)
- US040-CA5 sem caso de teste (item 15)
- US041-CA1 sem caso de teste (item 15)
- US041-CA2 sem caso de teste (item 15)
- US041-CA3 sem caso de teste (item 15)
- US041-CA4 sem caso de teste (item 15)
- US042-CA1 sem caso de teste (item 15)
- US042-CA2 sem caso de teste (item 15)
- US042-CA3 sem caso de teste (item 15)
- US042-CA4 sem caso de teste (item 15)
- US042-CA5 sem caso de teste (item 15)
- US042-CA6 sem caso de teste (item 15)
- US043-CA1 sem caso de teste (item 15)
- US043-CA2 sem caso de teste (item 15)
- US043-CA3 sem caso de teste (item 15)
<!-- matriz:fim -->
