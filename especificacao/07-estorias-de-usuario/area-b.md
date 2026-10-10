## US-B1 – REQUISITO RF-B1: Consultar as tarefas da equipe atribuídas ao operador

**COMO:** Operador de Solo/Rampa
**POSSO:** consultar no celular a lista das tarefas da minha equipe atribuídas a mim, com o turnaround (aeronave e posição), o estado, a janela planejada de início e de fim e as tarefas predecessoras ainda não concluídas
**PARA:** saber o que devo executar, em qual aeronave e a partir de quando posso começar

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** estou autenticado com o perfil de operador e há tarefas da minha equipe atribuídas a mim em turnarounds abertos <br> **QUANDO:** abro a lista de tarefas <br> **ENTÃO:** o sistema exibe essas tarefas, cada uma com o turnaround (aeronave e posição), o estado e a janela planejada de início e de fim |
| 2 | **DADO QUE:** uma tarefa atribuída a mim está no estado "Aguardando" porque uma tarefa predecessora não foi concluída <br> **QUANDO:** abro essa tarefa na lista <br> **ENTÃO:** o sistema mostra o nome da predecessora pendente e não oferece a opção de registrar o início |
| 3 | **DADO QUE:** no mesmo turnaround existe uma tarefa de outra equipe, ou da minha equipe atribuída a outro operador <br> **QUANDO:** abro a lista de tarefas <br> **ENTÃO:** essa tarefa não aparece na minha lista |

## US-B2 – REQUISITO RF-B2: Iniciar tarefa

**COMO:** Operador de Solo/Rampa
**POSSO:** registrar o início de uma tarefa da minha equipe atribuída a mim
**PARA:** que o começo real da tarefa fique registrado com horário e chegue ao Coordenador de Turnaround e ao Motor de Eventos no momento em que acontece

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** uma tarefa atribuída a mim está no estado "Pronta" <br> **QUANDO:** registro o início da tarefa <br> **ENTÃO:** a tarefa passa para o estado "Em execução" e o sistema grava o meu usuário e o horário do registro |
| 2 | **DADO QUE:** uma tarefa atribuída a mim está no estado "Aguardando", "Em execução" ou "Concluída" <br> **QUANDO:** tento registrar o início da tarefa <br> **ENTÃO:** o sistema recusa o registro, informa que só uma tarefa no estado "Pronta" pode ser iniciada e a tarefa mantém o estado |

## US-B3 – REQUISITO RF-B3: Concluir tarefa

**COMO:** Operador de Solo/Rampa
**POSSO:** registrar a conclusão de uma tarefa da minha equipe atribuída a mim
**PARA:** que o fim real da tarefa fique registrado com horário e as tarefas que dependem dela possam começar

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** uma tarefa atribuída a mim está no estado "Em execução" <br> **QUANDO:** registro a conclusão da tarefa <br> **ENTÃO:** a tarefa passa para o estado "Concluída" e o sistema grava o meu usuário e o horário do registro |
| 2 | **DADO QUE:** uma tarefa atribuída a mim está no estado "Aguardando" ou "Pronta" <br> **QUANDO:** tento registrar a conclusão da tarefa <br> **ENTÃO:** o sistema recusa o registro, informa que a tarefa precisa ser iniciada antes e a tarefa mantém o estado |
| 3 | **DADO QUE:** uma tarefa de limpeza atribuída a mim está no estado "Em execução" e tem um QR Code por zona da cabine, com uma zona ainda não confirmada <br> **QUANDO:** tento registrar a conclusão da tarefa <br> **ENTÃO:** o sistema recusa o registro, mostra a zona que falta confirmar e a tarefa mantém o estado "Em execução" |

## US-B4 – REQUISITO RF-B4: Pausar e retomar tarefa

**COMO:** Operador de Solo/Rampa
**POSSO:** pausar uma tarefa da minha equipe atribuída a mim, com justificativa e, quando houver impedimento, com o código do motivo da tabela da Agência Nacional de Aviação Civil (ANAC), e retomá-la depois
**PARA:** que o Coordenador de Turnaround saiba por que a tarefa parou e possa agir antes que o horário-alvo de prontidão (TOBT) [2] fique em risco

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** uma tarefa atribuída a mim está no estado "Em execução" <br> **QUANDO:** registro a pausa e escrevo a justificativa, sem indicar impedimento <br> **ENTÃO:** a tarefa passa para o estado "Pausada" e o sistema grava a justificativa, o meu usuário e o horário do registro |
| 2 | **DADO QUE:** uma tarefa atribuída a mim está no estado "Em execução" e há um impedimento <br> **QUANDO:** registro a pausa, escrevo a justificativa e escolho um código da tabela de códigos de atraso da ANAC [62] <br> **ENTÃO:** a tarefa passa para o estado "Pausada" e o sistema grava a justificativa, o código escolhido, o meu usuário e o horário do registro |
| 3 | **DADO QUE:** uma tarefa atribuída a mim está no estado "Em execução" <br> **QUANDO:** tento registrar a pausa sem escrever a justificativa <br> **ENTÃO:** o sistema recusa o registro, pede a justificativa e a tarefa mantém o estado "Em execução" |
| 4 | **DADO QUE:** uma tarefa atribuída a mim está no estado "Em execução" <br> **QUANDO:** registro a pausa, escrevo a justificativa, indico que há impedimento e não escolho o código da ANAC <br> **ENTÃO:** o sistema recusa o registro, pede o código do impedimento e a tarefa mantém o estado "Em execução" |
| 5 | **DADO QUE:** uma tarefa atribuída a mim está no estado "Pausada" <br> **QUANDO:** registro a retomada da tarefa <br> **ENTÃO:** a tarefa volta para o estado "Em execução" e o sistema grava o meu usuário e o horário do registro |

## US-B5 – REQUISITO RF-B5: Marcar tarefa como "Não aplicável"

**COMO:** Operador de Solo/Rampa
**POSSO:** marcar uma tarefa da minha equipe atribuída a mim como "Não aplicável", com justificativa
**PARA:** que o Coordenador de Turnaround saiba por que a tarefa não será feita e as tarefas que dependem dela não fiquem esperando

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** uma tarefa atribuída a mim ainda não foi iniciada e o modelo de tarefas do turnaround permite marcá-la como "Não aplicável" <br> **QUANDO:** marco a tarefa como "Não aplicável" e escrevo a justificativa <br> **ENTÃO:** a tarefa passa para o estado "Não aplicável" e o sistema grava a justificativa, o meu usuário e o horário do registro |
| 2 | **DADO QUE:** uma tarefa atribuída a mim já foi iniciada, ou o modelo de tarefas não permite marcá-la como "Não aplicável" <br> **QUANDO:** tento marcar a tarefa como "Não aplicável" <br> **ENTÃO:** o sistema recusa o registro, informa o motivo da recusa e a tarefa mantém o estado |
| 3 | **DADO QUE:** uma tarefa atribuída a mim ainda não foi iniciada e o modelo de tarefas permite marcá-la como "Não aplicável" <br> **QUANDO:** tento marcar a tarefa como "Não aplicável" sem escrever a justificativa <br> **ENTÃO:** o sistema recusa o registro, pede a justificativa e a tarefa mantém o estado |

## US-B6 – REQUISITO RF-B6: Confirmar a execução da tarefa por QR Code

**COMO:** Operador de Solo/Rampa
**POSSO:** ler com a câmera do celular os QR Codes fixados nos pontos da aeronave ligados a uma tarefa da minha equipe atribuída a mim, por exemplo as zonas, fileiras ou assentos da cabine na limpeza
**PARA:** comprovar, ponto a ponto, a execução da tarefa sem digitar nada

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** uma tarefa de limpeza atribuída a mim está no estado "Em execução" e tem um QR Code por zona da cabine <br> **QUANDO:** leio o QR Code de uma zona <br> **ENTÃO:** o sistema grava a leitura dessa zona com o meu usuário e o horário e mostra a zona como confirmada na tarefa |
| 2 | **DADO QUE:** um QR Code pertence a uma tarefa de outra equipe, ou da minha equipe atribuída a outro operador <br> **QUANDO:** leio esse QR Code <br> **ENTÃO:** o sistema recusa a leitura, informa que o QR Code não pertence a uma tarefa atribuída a mim e não grava nenhum registro |
| 3 | **DADO QUE:** um QR Code não corresponde a nenhum ponto cadastrado no turnaround <br> **QUANDO:** leio esse QR Code <br> **ENTÃO:** o sistema informa que o QR Code não foi reconhecido e não grava nenhum registro |
| 4 | **DADO QUE:** uma tarefa de limpeza atribuída a mim está no estado "Pronta" ou "Pausada" <br> **QUANDO:** leio o QR Code de uma zona dessa tarefa <br> **ENTÃO:** o sistema recusa a leitura, informa que a tarefa precisa estar em execução e não grava nenhum registro |

## US-B7 – REQUISITO RF-B7: Registrar os marcos do atendimento em solo

**COMO:** Motor de Eventos
**POSSO:** registrar os horários dos marcos do atendimento em solo a partir dos registros feitos pelos operadores
**PARA:** que o Coordenador de Turnaround acompanhe os marcos reais do turnaround sem que ninguém precise digitá-los

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** nenhuma tarefa do turnaround foi iniciada <br> **QUANDO:** o Operador de Solo/Rampa registra o início da primeira tarefa <br> **ENTÃO:** o sistema grava o horário desse registro como início real do atendimento em solo (ACGT) [2] no turnaround |
| 2 | **DADO QUE:** a tarefa de embarque está no estado "Pronta" <br> **QUANDO:** o Operador de Solo/Rampa registra o início dessa tarefa <br> **ENTÃO:** o sistema grava o horário desse registro como início real do embarque (ASBT) [2] no turnaround |
| 3 | **DADO QUE:** todas as demais tarefas obrigatórias do turnaround estão nos estados "Concluída" ou "Não aplicável" <br> **QUANDO:** o Operador de Solo/Rampa registra a conclusão da última tarefa obrigatória <br> **ENTÃO:** o sistema grava o horário desse registro como fim real do atendimento em solo (AEGT) [2] no turnaround |
| 4 | **DADO QUE:** o ACGT do turnaround já foi gravado <br> **QUANDO:** o Operador de Solo/Rampa registra o início de outra tarefa que não é a de embarque <br> **ENTÃO:** o sistema mantém o ACGT gravado e não grava nenhum outro marco |
| 5 | **DADO QUE:** todas as demais tarefas obrigatórias do turnaround estão nos estados "Concluída" ou "Não aplicável" e a última tarefa obrigatória pendente ainda não foi iniciada <br> **QUANDO:** o Operador de Solo/Rampa marca essa tarefa como "Não aplicável" <br> **ENTÃO:** o sistema grava o horário dessa marcação como AEGT no turnaround |

## US-B8 – REQUISITO RF-B8: Propagar o estado das tarefas e do turnaround

**COMO:** Motor de Eventos
**POSSO:** propagar o estado das tarefas e do turnaround a cada registro feito pelos operadores
**PARA:** que cada Operador de Solo/Rampa veja a sua tarefa liberada para início assim que as predecessoras terminam, e que o turnaround mude de estado sem depender de um registro manual

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** o turnaround está no estado "Em solo" e nenhuma tarefa foi iniciada <br> **QUANDO:** o Operador de Solo/Rampa registra o início da primeira tarefa <br> **ENTÃO:** o turnaround passa para o estado "Operações em andamento" e o sistema grava o horário da mudança e o registro que a causou |
| 2 | **DADO QUE:** a tarefa de limpeza da cabine está no estado "Aguardando" e tem como única predecessora o desembarque, no estado "Em execução" <br> **QUANDO:** o Operador de Solo/Rampa registra a conclusão do desembarque <br> **ENTÃO:** a limpeza da cabine passa para o estado "Pronta" e o sistema grava o horário da mudança e o registro que a causou |
| 3 | **DADO QUE:** uma tarefa no estado "Aguardando" tem duas predecessoras, uma no estado "Em execução" e outra no estado "Pronta" <br> **QUANDO:** o Operador de Solo/Rampa registra a conclusão da predecessora que estava "Em execução" <br> **ENTÃO:** a tarefa continua no estado "Aguardando", porque ainda há predecessora pendente |
| 4 | **DADO QUE:** uma tarefa no estado "Aguardando" tem duas predecessoras, uma no estado "Concluída" e outra ainda não iniciada <br> **QUANDO:** o Operador de Solo/Rampa marca a predecessora não iniciada como "Não aplicável" <br> **ENTÃO:** a tarefa passa para o estado "Pronta" |
| 5 | **DADO QUE:** o turnaround está no estado "Operações em andamento" e só uma tarefa obrigatória não está nos estados "Concluída" ou "Não aplicável" <br> **QUANDO:** o Operador de Solo/Rampa registra a conclusão dessa tarefa <br> **ENTÃO:** o turnaround passa para o estado "Pronto para liberação" e o sistema grava o horário da mudança e o registro que a causou |
| 6 | **DADO QUE:** o turnaround foi aberto e a tarefa de calçar a aeronave, que não tem predecessora, está no estado "Aguardando" <br> **QUANDO:** o turnaround entra no estado "Em solo", com o registro do horário real de chegada à posição (AIBT) [2] <br> **ENTÃO:** a tarefa de calçar a aeronave passa para o estado "Pronta" e o sistema grava o horário da mudança e o registro que a causou |
| 7 | **DADO QUE:** o embarque está no estado "Pronta" <br> **QUANDO:** o Coordenador de Turnaround inclui no plano uma limpeza profunda de assento, ainda não iniciada, como predecessora do embarque <br> **ENTÃO:** o embarque volta para o estado "Aguardando" e o sistema grava o horário da mudança e a inclusão como causa |

Fontes citadas: [2] e [62], conforme a numeração de `pesquisa/fontes.md`.
