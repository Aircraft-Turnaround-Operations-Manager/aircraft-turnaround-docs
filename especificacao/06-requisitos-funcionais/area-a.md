**Horários usados nos requisitos** [2][4]:

- Horário programado de chegada à posição (SIBT): chegada prevista na programação do voo.
- Horário programado de saída da posição (SOBT): saída prevista na programação do voo.
- Horário estimado de chegada à posição (EIBT): previsão atual de chegada.
- Horário-alvo de prontidão (TOBT): referência para a aeronave estar pronta.
- Horário real de chegada à posição (AIBT): chegada que de fato ocorreu.
- Tempo mínimo de turnaround (MTTT): tempo mínimo previsto para o atendimento em solo.

Os horários incluem data e fuso. MTTT e durações das tarefas usam minutos positivos. O TOBT planejado é a referência inicial; o vigente é a previsão mais recente (ADR-0003).

| # | REQUISITO FUNCIONAL | ATOR / USUÁRIO | OBJETIVO | SPRINT |
|---|---|---|---|---|
| RF-A1 | O sistema deve permitir ao Usuário entrar com credenciais válidas e acessar as funções do seu perfil. Credenciais inválidas ou cadastro desativado impedem o acesso. | Usuário | Obj. 2 | |
| RF-A2 | O sistema deve permitir ao Administrador do Sistema cadastrar, editar e desativar usuários. O cadastro exige nome, identificador de acesso único, perfil e senha inicial protegida (RNF-A3); operadores também precisam de equipe ativa. Desativar bloqueia o acesso e preserva o histórico. | Administrador do Sistema | Obj. 2 | |
| RF-A3 | O sistema deve permitir ao Coordenador de Turnaround abrir um turnaround com voos de chegada e partida, companhia, aeronave, posição, SIBT, SOBT, EIBT, TOBT e MTTT [2][4]. O TOBT planejado fica fixo e o vigente começa igual a ele (ADR-0003). Abrir o cadastro não registra chegada real nem inicia tarefas. | Coordenador de Turnaround | Obj. 1 e 2 | |
| RF-A4 | O sistema deve permitir ao Coordenador de Turnaround criar modelos de tarefas por tipo de aeronave e serviço. Cada tarefa tem nome, tipo de atividade, equipe ativa, duração positiva, obrigatoriedade e permissão de "Não aplicável". Embarque, desembarque e abastecimento são identificados pelo tipo; serviços com embarque de passageiros exigem uma única tarefa de embarque [22][45]. | Coordenador de Turnaround | Obj. 2 | |
| RF-A5 | O sistema deve permitir ao Coordenador de Turnaround confirmar o plano inicial com responsável, início, fim e obrigatoriedade de cada tarefa. Todas as tarefas precisam de operador ativo da equipe correta, fim após o início e dependências válidas (RF-A8). O plano inicial só pode ser confirmado ou editado antes de qualquer tarefa começar. | Coordenador de Turnaround | Obj. 1 e 2 | |
| RF-A6 | O sistema deve permitir ao Coordenador de Turnaround aplicar um modelo compatível com a aeronave e o serviço. A cópia mantém todas as tarefas, configurações, dependências e pontos, com identificadores próprios e sem alterar o modelo. Só é permitida antes da confirmação do plano e do início das tarefas; substituir uma cópia exige confirmação. A cópia respeita RF-A11, sem atribuir operadores nem iniciar tarefas. | Coordenador de Turnaround | Obj. 2 | |
| RF-A7 | O sistema deve permitir ao Coordenador de Turnaround definir pontos de confirmação por código de resposta rápida (QR Code) nas tarefas do modelo. Cada ponto exige nome e identificador únicos na tarefa e é copiado ao aplicar o modelo (RF-A6). A leitura e a validação da conclusão pertencem à área B (ADR-0007). | Coordenador de Turnaround | Obj. 2 | |
| RF-A8 | O sistema deve permitir ao Coordenador de Turnaround definir quais tarefas precisam terminar antes de outras, no mesmo modelo ou plano inicial. O sistema recusa referências inválidas e ciclos e respeita RF-A11. O início planejado da sucessora deve ser igual ou posterior ao fim planejado das predecessoras; tarefas independentes podem ocorrer em paralelo com operadores distintos. No plano inicial, só há edição antes do início das tarefas. | Coordenador de Turnaround | Obj. 1 e 2 | |
| RF-A9 | O sistema deve permitir ao Administrador do Sistema cadastrar, editar e desativar equipes ou especialidades com nome e identificador único. Desativar exige ausência de usuários ativos vinculados e de tarefas pendentes em turnarounds não encerrados. A equipe desativada não aceita novos vínculos, mas mantém o histórico. | Administrador do Sistema | Obj. 2 | |
| RF-A10 | O sistema deve permitir ao Coordenador de Turnaround atualizar EIBT e MTTT até a confirmação da chegada. A alteração mantém o TOBT planejado e o vigente, registra valores anteriores e novos e fornece os dados ao Motor de Eventos para a checagem de viabilidade da área C [3][7]. | Coordenador de Turnaround | Obj. 1 e 3 | |
| RF-A11 | O sistema deve permitir ao Coordenador de Turnaround configurar, por companhia, a permissão de abastecimento com passageiros, desabilitada por padrão (ADR-0005) [24][26][27]. Sem permissão, o plano exige desembarque, depois abastecimento e depois embarque. A configuração é copiada ao turnaround e não muda após o início das tarefas. | Coordenador de Turnaround | Obj. 1 e 2 | |
| RF-A12 | O sistema deve permitir ao Operador de Solo/Rampa com tarefa atribuída nesse turnaround informar o horário real de chegada (AIBT) [2][4]. O envio fica pendente, sem registrar a chegada oficial nem entrar em "Em solo". Horário futuro, chegada já confirmada ou outro envio pendente impedem novo registro. | Operador de Solo/Rampa | Obj. 1 e 2 | |
| RF-A13 | O sistema deve permitir ao Coordenador de Turnaround confirmar ou recusar uma chegada pendente. Confirmar exige plano confirmado, usa como AIBT o horário informado pelo operador e coloca o turnaround em "Em solo", acionando a área B [2][4]. Recusar exige motivo e permite correção e novo envio. Cada registro recebe apenas uma decisão. | Coordenador de Turnaround | Obj. 1 e 2 | |

**Regras comuns:** mudanças registram autor e horário conforme RNF-A2. Usuário representa os quatro perfis humanos: Operador de Solo/Rampa, Coordenador de Turnaround, Autoridade de Liberação e Administrador do Sistema; não é um quinto perfil (ADR-0010). O sistema não altera a programação dos voos. Replanejamento durante a operação pertence à área D; a SPRINT será definida pelo grupo no T06.

**Chegada (#59):** operador registra e coordenador confirma é a proposta escolhida pelo autor, a revisar em equipe. Pendente, Confirmado e Recusado são situações do registro, não estados do turnaround. Horário real, envio e decisão ficam separados; só a confirmação grava o AIBT oficial.

**Abastecimento:** a permissão representa a política autorizada da companhia, não uma autorização regulatória do sistema. Ela permite paralelismo sem remover outras dependências; mudanças gerais não alteram turnarounds já iniciados.

Fontes citadas: [2], [3], [4], [7], [22], [24], [26], [27] e [45], conforme `pesquisa/fontes.md`. Validações, unicidade do embarque e congelamento da configuração são regras internas propostas.
