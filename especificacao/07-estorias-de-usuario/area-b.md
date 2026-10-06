## US005 – REQUISITO 5: Consultar as tarefas da equipe atribuídas ao operador

**COMO:** Operador de Solo/Rampa
**POSSO:** consultar no celular a lista das tarefas da minha equipe atribuídas a mim, com o turnaround (aeronave e posição), o estado, a janela planejada de início e de fim e as tarefas predecessoras ainda não concluídas
**PARA:** saber o que devo executar, em qual aeronave e a partir de quando posso começar

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** estou autenticado com o perfil de operador e há tarefas da minha equipe atribuídas a mim em turnarounds abertos <br> **QUANDO:** abro a lista de tarefas <br> **ENTÃO:** o sistema exibe essas tarefas, cada uma com o turnaround (aeronave e posição), o estado e a janela planejada de início e de fim |
| 2 | **DADO QUE:** uma tarefa atribuída a mim está no estado "Aguardando" porque uma tarefa predecessora não foi concluída <br> **QUANDO:** abro essa tarefa na lista <br> **ENTÃO:** o sistema mostra o nome da predecessora pendente e não oferece a opção de registrar o início |
| 3 | **DADO QUE:** no mesmo turnaround existe uma tarefa de outra equipe, ou da minha equipe atribuída a outro operador <br> **QUANDO:** abro a lista de tarefas <br> **ENTÃO:** essa tarefa não aparece na minha lista |

## US006 – REQUISITO 6: Registrar a execução da tarefa

**COMO:** Operador de Solo/Rampa
**POSSO:** registrar o início e a conclusão de uma tarefa da minha equipe atribuída a mim
**PARA:** que o andamento real fique registrado com horário e chegue ao Coordenador de Turnaround e ao Motor de Eventos no momento em que acontece

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** uma tarefa atribuída a mim está no estado "Pronta" <br> **QUANDO:** registro o início da tarefa <br> **ENTÃO:** a tarefa passa para o estado "Em execução" e o sistema grava o meu usuário e o horário do registro |
| 2 | **DADO QUE:** uma tarefa atribuída a mim está no estado "Em execução" <br> **QUANDO:** registro a conclusão da tarefa <br> **ENTÃO:** a tarefa passa para o estado "Concluída" e o sistema grava o meu usuário e o horário do registro |
| 3 | **DADO QUE:** uma tarefa atribuída a mim está no estado "Aguardando" ou "Pronta" <br> **QUANDO:** tento registrar a conclusão da tarefa <br> **ENTÃO:** o sistema recusa o registro, informa que a tarefa precisa ser iniciada antes e a tarefa mantém o estado |
| 4 | **DADO QUE:** nenhuma tarefa do turnaround foi iniciada <br> **QUANDO:** registro o início da primeira tarefa <br> **ENTÃO:** o sistema grava esse horário como início real do atendimento em solo (ACGT) [2] e o turnaround passa para o estado "Operações em andamento" |
| 5 | **DADO QUE:** todas as demais tarefas obrigatórias do turnaround estão no estado "Concluída" <br> **QUANDO:** registro a conclusão da última tarefa obrigatória <br> **ENTÃO:** o sistema grava esse horário como fim real do atendimento em solo (AEGT) [2] e o turnaround passa para o estado "Pronto para liberação" |
| 6 | **DADO QUE:** a tarefa de embarque atribuída a mim está no estado "Pronta" <br> **QUANDO:** registro o início da tarefa <br> **ENTÃO:** o sistema grava esse horário como início real do embarque (ASBT) [2] no turnaround |

## US007 – REQUISITO 7: Registrar desvio na execução da tarefa

**COMO:** Operador de Solo/Rampa
**POSSO:** pausar e retomar uma tarefa da minha equipe atribuída a mim, informando o motivo da pausa pelo código da tabela da Agência Nacional de Aviação Civil (ANAC), ou marcá-la como "Não aplicável" com justificativa
**PARA:** que o Coordenador de Turnaround saiba por que a tarefa parou ou não será feita e possa agir antes que o horário-alvo de prontidão (TOBT) [2] fique em risco

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** uma tarefa atribuída a mim está no estado "Em execução" <br> **QUANDO:** registro a pausa e escolho um código da tabela de códigos de atraso da ANAC [62] <br> **ENTÃO:** a tarefa passa para o estado "Pausada" e o sistema grava o código escolhido, o meu usuário e o horário do registro |
| 2 | **DADO QUE:** uma tarefa atribuída a mim está no estado "Em execução" <br> **QUANDO:** tento registrar a pausa sem escolher um código <br> **ENTÃO:** o sistema recusa o registro, pede o código do motivo e a tarefa mantém o estado "Em execução" |
| 3 | **DADO QUE:** uma tarefa atribuída a mim está no estado "Pausada" <br> **QUANDO:** registro a retomada da tarefa <br> **ENTÃO:** a tarefa volta para o estado "Em execução" e o sistema grava o meu usuário e o horário do registro |
| 4 | **DADO QUE:** uma tarefa atribuída a mim ainda não foi iniciada e o modelo de tarefas do turnaround permite marcá-la como "Não aplicável" <br> **QUANDO:** marco a tarefa como "Não aplicável" e escrevo a justificativa <br> **ENTÃO:** a tarefa passa para o estado "Não aplicável" e o sistema grava a justificativa, o meu usuário e o horário do registro |
| 5 | **DADO QUE:** uma tarefa atribuída a mim já foi iniciada, ou o modelo de tarefas não permite marcá-la como "Não aplicável" <br> **QUANDO:** tento marcar a tarefa como "Não aplicável" <br> **ENTÃO:** o sistema recusa o registro, informa o motivo da recusa e a tarefa mantém o estado |
| 6 | **DADO QUE:** uma tarefa atribuída a mim ainda não foi iniciada e o modelo de tarefas permite marcá-la como "Não aplicável" <br> **QUANDO:** tento marcar a tarefa como "Não aplicável" sem escrever a justificativa <br> **ENTÃO:** o sistema recusa o registro, pede a justificativa e a tarefa mantém o estado |

## US008 – REQUISITO 8: Confirmar a execução da tarefa por QR Code

**COMO:** Operador de Solo/Rampa
**POSSO:** ler com a câmera do celular os QR Codes fixados nos pontos da aeronave ligados a uma tarefa da minha equipe atribuída a mim, por exemplo as zonas, fileiras ou assentos da cabine na limpeza
**PARA:** comprovar, ponto a ponto, a execução da tarefa sem digitar nada

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** uma tarefa de limpeza atribuída a mim está no estado "Em execução" e tem um QR Code por zona da cabine <br> **QUANDO:** leio o QR Code de uma zona <br> **ENTÃO:** o sistema grava a leitura dessa zona com o meu usuário e o horário e mostra a zona como confirmada na tarefa |
| 2 | **DADO QUE:** um QR Code pertence a uma tarefa de outra equipe, ou da minha equipe atribuída a outro operador <br> **QUANDO:** leio esse QR Code <br> **ENTÃO:** o sistema recusa a leitura, informa que o QR Code não pertence a uma tarefa atribuída a mim e não grava nenhum registro |
| 3 | **DADO QUE:** um QR Code não corresponde a nenhum ponto cadastrado no turnaround <br> **QUANDO:** leio esse QR Code <br> **ENTÃO:** o sistema informa que o QR Code não foi reconhecido e não grava nenhum registro |

Fontes citadas: [2] e [62], conforme a numeração de `pesquisa/fontes.md`.
