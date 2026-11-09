## US012 – REQUISITO RF-12: Registrar chegada da aeronave à posição

**COMO:** Operador de Solo/Rampa com tarefa atribuída no turnaround

**POSSO:** registrar o horário real de chegada à posição (AIBT) da aeronave [2][4]

**PARA:** colocar o turnaround em "Em solo" e liberar as tarefas sem predecessora pelo RF-21 (ADR-0013)

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** tenho tarefa atribuída nesse turnaround, o plano inicial está confirmado e não há chegada registrada <br> **QUANDO:** registro o horário real com data e fuso, sem horário futuro <br> **ENTÃO:** o AIBT é gravado com auditoria, o turnaround entra em "Em solo" e dispara a propagação do RF-21, sem confirmação do Coordenador de Turnaround nem início automático das tarefas |
| 2 | **DADO QUE:** já existe chegada registrada <br> **QUANDO:** tento registrar outra chegada, inclusive em requisições simultâneas <br> **ENTÃO:** o sistema recusa a duplicidade, mostra o registro existente e não sobrescreve o AIBT nem repete a propagação |
| 3 | **DADO QUE:** o horário informado é futuro ou inválido <br> **QUANDO:** tento registrar a chegada <br> **ENTÃO:** o sistema informa o impedimento e não grava a chegada nem altera estados |
| 4 | **DADO QUE:** a aeronave chegou às 14:07 e faço o registro às 14:10 <br> **QUANDO:** salvo a chegada <br> **ENTÃO:** o AIBT fica 14:07 e o horário do registro fica 14:10, com meu usuário e ambos os horários preservados como dados distintos |
| 5 | **DADO QUE:** não tenho tarefa atribuída nesse turnaround <br> **QUANDO:** tento registrar a chegada <br> **ENTÃO:** o sistema informa o impedimento e não grava a chegada nem altera estados |
| 6 | **DADO QUE:** o plano inicial do turnaround ainda não está confirmado <br> **QUANDO:** tento registrar a chegada <br> **ENTÃO:** o sistema informa o impedimento e não grava a chegada nem altera estados |

## US013 – REQUISITO RF-13: Corrigir horário de chegada à posição

**COMO:** Coordenador de Turnaround

**POSSO:** corrigir o AIBT registrado, informando o motivo

**PARA:** manter o horário real correto e recalcular a projeção sem alterar os estados operacionais (ADR-0013)

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** há AIBT registrado e o turnaround não está "Liberado" nem "Fora de bloco" <br> **QUANDO:** salvo um horário corrigido válido, não futuro, com data, fuso e motivo <br> **ENTÃO:** o novo AIBT é gravado com valor anterior, motivo, autor e horário da correção; a projeção é recalculada pelo RF-22, sem mudar o estado do turnaround nem das tarefas |
| 2 | **DADO QUE:** estou corrigindo a chegada <br> **QUANDO:** falta motivo ou o horário é inválido ou futuro <br> **ENTÃO:** o sistema informa o impedimento e preserva o AIBT e os estados |
| 3 | **DADO QUE:** o turnaround está "Fora de bloco" ou ainda não há AIBT registrado <br> **QUANDO:** tento corrigir a chegada <br> **ENTÃO:** a alteração é recusada sem gravar correção nem disparar recálculo |
| 4 | **DADO QUE:** estou autenticado como Operador de Solo/Rampa <br> **QUANDO:** tento corrigir o AIBT já registrado <br> **ENTÃO:** a alteração é recusada porque a correção exige Coordenador de Turnaround (RNF-1) |
| 5 | **DADO QUE:** o AIBT registrado é 14:07 <br> **QUANDO:** às 14:20 corrijo para 14:05 com motivo <br> **ENTÃO:** o AIBT vigente fica 14:05; o valor anterior 14:07 e o horário da correção 14:20 continuam no histórico, sem substituir o horário real pelo da edição |
| 6 | **DADO QUE:** há AIBT registrado e o turnaround está "Liberado" <br> **QUANDO:** o Coordenador de Turnaround salva uma correção válida, com data, fuso e motivo <br> **ENTÃO:** o novo AIBT e o histórico da correção são gravados; os estados são preservados e a projeção não é recalculada (ADR-0013) |

## US014 – REQUISITO RF-14: Consultar lista de tarefas do operador

**COMO:** Operador de Solo/Rampa
**POSSO:** consultar no celular a lista das tarefas da minha equipe atribuídas a mim, com o turnaround (aeronave e posição), o estado, a janela planejada de início e de fim e as tarefas predecessoras ainda não concluídas
**PARA:** saber o que devo executar, em qual aeronave e a partir de quando posso começar

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** estou autenticado com o perfil de operador e há tarefas da minha equipe atribuídas a mim em turnarounds abertos <br> **QUANDO:** abro a lista de tarefas <br> **ENTÃO:** o sistema exibe essas tarefas, cada uma com o turnaround (aeronave e posição), o estado e a janela planejada de início e de fim |
| 2 | **DADO QUE:** uma tarefa atribuída a mim está no estado "Aguardando" porque uma tarefa predecessora não foi concluída <br> **QUANDO:** abro essa tarefa na lista <br> **ENTÃO:** o sistema mostra o nome da predecessora pendente e não oferece a opção de registrar o início |
| 3 | **DADO QUE:** no mesmo turnaround existe uma tarefa de outra equipe, ou da minha equipe atribuída a outro operador <br> **QUANDO:** abro a lista de tarefas <br> **ENTÃO:** essa tarefa não aparece na minha lista |

## US015 – REQUISITO RF-15: Registrar início da tarefa

**COMO:** Operador de Solo/Rampa
**POSSO:** registrar o início de uma tarefa da minha equipe atribuída a mim
**PARA:** que o começo real da tarefa fique registrado com horário e chegue ao Coordenador de Turnaround e ao Motor de Eventos no momento em que acontece

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** uma tarefa atribuída a mim está no estado "Pronta" <br> **QUANDO:** registro o início da tarefa <br> **ENTÃO:** a tarefa passa para o estado "Em execução" e o sistema grava o meu usuário e o horário do registro |
| 2 | **DADO QUE:** uma tarefa atribuída a mim está no estado "Aguardando", "Em execução" ou "Concluída" <br> **QUANDO:** tento registrar o início da tarefa <br> **ENTÃO:** o sistema recusa o registro, informa que só uma tarefa no estado "Pronta" pode ser iniciada e a tarefa mantém o estado |

## US016 – REQUISITO RF-16: Registrar conclusão da tarefa

**COMO:** Operador de Solo/Rampa
**POSSO:** registrar a conclusão de uma tarefa da minha equipe atribuída a mim
**PARA:** que o fim real da tarefa fique registrado com horário e as tarefas que dependem dela possam começar

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** uma tarefa atribuída a mim está no estado "Em execução" <br> **QUANDO:** registro a conclusão da tarefa <br> **ENTÃO:** a tarefa passa para o estado "Concluída" e o sistema grava o meu usuário e o horário do registro |
| 2 | **DADO QUE:** uma tarefa atribuída a mim está no estado "Aguardando" ou "Pronta" <br> **QUANDO:** tento registrar a conclusão da tarefa <br> **ENTÃO:** o sistema recusa o registro, informa que a tarefa precisa ser iniciada antes e a tarefa mantém o estado |
| 3 | **DADO QUE:** uma tarefa de limpeza atribuída a mim está no estado "Em execução" e tem um QR Code por zona da cabine, com uma zona ainda não confirmada <br> **QUANDO:** tento registrar a conclusão da tarefa <br> **ENTÃO:** o sistema recusa o registro, mostra a zona que falta confirmar e a tarefa mantém o estado "Em execução" |

## US017 – REQUISITO RF-17: Pausar e retomar execução da tarefa

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

## US018 – REQUISITO RF-18: Marcar tarefa como "Não aplicável"

**COMO:** Operador de Solo/Rampa
**POSSO:** marcar uma tarefa da minha equipe atribuída a mim como "Não aplicável", com justificativa
**PARA:** que o Coordenador de Turnaround saiba por que a tarefa não será feita e as tarefas que dependem dela não fiquem esperando

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** uma tarefa atribuída a mim ainda não foi iniciada e o modelo de tarefas do turnaround permite marcá-la como "Não aplicável" <br> **QUANDO:** marco a tarefa como "Não aplicável" e escrevo a justificativa <br> **ENTÃO:** a tarefa passa para o estado "Não aplicável" e o sistema grava a justificativa, o meu usuário e o horário do registro |
| 2 | **DADO QUE:** uma tarefa atribuída a mim já foi iniciada, ou o modelo de tarefas não permite marcá-la como "Não aplicável" <br> **QUANDO:** tento marcar a tarefa como "Não aplicável" <br> **ENTÃO:** o sistema recusa o registro, informa o motivo da recusa e a tarefa mantém o estado |
| 3 | **DADO QUE:** uma tarefa atribuída a mim ainda não foi iniciada e o modelo de tarefas permite marcá-la como "Não aplicável" <br> **QUANDO:** tento marcar a tarefa como "Não aplicável" sem escrever a justificativa <br> **ENTÃO:** o sistema recusa o registro, pede a justificativa e a tarefa mantém o estado |

## US019 – REQUISITO RF-19: Confirmar execução da tarefa por QR Code

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

## US020 – REQUISITO RF-20: Registrar marcos do atendimento em solo

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

## US021 – REQUISITO RF-21: Propagar estado das tarefas e do turnaround

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

## US044 – REQUISITO RF-44: Registrar saída da posição e encerrar turnaround

**COMO:** Operador de Solo/Rampa
**POSSO:** registrar o horário real de saída da posição (AOBT) [2] de um turnaround no estado "Liberado", depois que a autorização de acionamento e push-back do controle de tráfego aéreo foi recebida fora do sistema
**PARA:** encerrar o turnaround com o horário real de saída e manter o histórico completo para consulta

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** um turnaround está no estado "Liberado" e a aeronave recebeu a autorização de push-back <br> **QUANDO:** registro a saída da posição <br> **ENTÃO:** o sistema grava o AOBT com o horário do registro e o meu usuário, e o turnaround passa para o estado "Fora de bloco" |
| 2 | **DADO QUE:** um turnaround está no estado "Pronto para liberação", sem a confirmação da Autoridade de Liberação <br> **QUANDO:** tento registrar a saída da posição <br> **ENTÃO:** o sistema recusa o registro, informa que o turnaround ainda não foi liberado, não grava o AOBT e o turnaround mantém o estado |
| 3 | **DADO QUE:** um turnaround está no estado "Fora de bloco" <br> **QUANDO:** um Operador de Solo/Rampa tenta registrar início, pausa ou conclusão de uma tarefa desse turnaround <br> **ENTÃO:** o sistema recusa o registro, informa que o turnaround está encerrado e mantém o histórico de tarefas, marcos e decisões disponível para consulta |

Fontes citadas: [2], [4] e [62], conforme a numeração de `pesquisa/fontes.md`.
