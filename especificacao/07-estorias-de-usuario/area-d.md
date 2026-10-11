## US036 – REQUISITO RF-36: Abrir exceção com código de atraso

**COMO:** Coordenador de Turnaround
**POSSO:** abrir uma exceção em um turnaround, informando a tarefa afetada, a causa pelo código da tabela de códigos de atraso da Agência Nacional de Aviação Civil (ANAC) [62] e uma descrição
**PARA:** que o impedimento fique registrado com a causa padronizada e que o turnaround não seja liberado enquanto a exceção não for resolvida

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** um turnaround está no estado "Operações em andamento" e a tarefa de abastecimento está parada por falta do caminhão de combustível <br> **QUANDO:** abro uma exceção informando a tarefa de abastecimento, um código da tabela da ANAC e a descrição do problema <br> **ENTÃO:** o sistema grava a exceção com a tarefa, o código, a descrição, o meu usuário e o horário, e o turnaround passa para o estado "Em exceção" |
| 2 | **DADO QUE:** estou abrindo uma exceção em um turnaround <br> **QUANDO:** confirmo a abertura sem escolher um código da tabela da ANAC <br> **ENTÃO:** o sistema recusa a abertura, informa que o código é obrigatório e o turnaround mantém o estado |
| 3 | **DADO QUE:** um turnaround já está no estado "Em exceção", com uma exceção aberta na tarefa de abastecimento <br> **QUANDO:** abro uma segunda exceção, na tarefa de catering, com outro código da tabela da ANAC <br> **ENTÃO:** o sistema grava a segunda exceção, o turnaround continua "Em exceção" e as duas exceções aparecem abertas |

## US037 – REQUISITO RF-37: Reatribuir tarefa a outro operador da mesma equipe

**COMO:** Coordenador de Turnaround
**POSSO:** reatribuir uma tarefa ainda não concluída a outro Operador de Solo/Rampa da mesma equipe que esteja disponível, informando o motivo
**PARA:** recuperar o prazo quando o operador original está ocupado ou impedido, sem esperar que ele fique livre

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** a tarefa de limpeza da cabine está no estado "Pronta", atribuída a um operador da equipe de limpeza, e outro operador da mesma equipe está sem tarefa em execução <br> **QUANDO:** reatribuo a tarefa a esse outro operador, informando o motivo <br> **ENTÃO:** o sistema grava o motivo, o meu usuário e o horário, a tarefa passa a aparecer só na lista do novo operador e os dois operadores recebem o aviso da reatribuição |
| 2 | **DADO QUE:** a tarefa de catering está no estado "Concluída" <br> **QUANDO:** tento reatribuí-la a outro operador <br> **ENTÃO:** o sistema recusa a reatribuição, informa que tarefa concluída não pode ser reatribuída e a tarefa mantém o operador original |
| 3 | **DADO QUE:** a tarefa de limpeza da cabine está no estado "Pronta" <br> **QUANDO:** tento reatribuí-la a um operador de outra equipe ou a um operador da equipe de limpeza que tem tarefa em execução <br> **ENTÃO:** o sistema recusa a reatribuição, informa que o operador escolhido não é da mesma equipe ou não está disponível e a tarefa mantém o operador original |
| 4 | **DADO QUE:** reatribuí uma tarefa enquanto o operador original estava sem conexão e ele registrou, no celular, o início dessa tarefa <br> **QUANDO:** a conexão do operador original volta e o registro é enviado ao servidor <br> **ENTÃO:** o sistema recusa o registro, a tarefa não muda de estado e o operador original recebe o aviso da recusa com o motivo, como define o RNF-8 |

## US038 – REQUISITO RF-38: Registrar a ação tomada para cada alerta

**COMO:** Coordenador de Turnaround
**POSSO:** registrar, para cada alerta recebido, a ação que tomei (reatribuir tarefa, replanejar, atualizar a previsão ou abrir exceção)
**PARA:** que todo alerta tenha uma resposta registrada, com autor e horário, e que se possa medir quanto tempo levou entre o alerta e a ação

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** recebi um alerta de risco ao horário-alvo de prontidão (TOBT) [2] de um turnaround, e o alerta está aberto <br> **QUANDO:** reatribuo a tarefa atrasada e registro "reatribuir tarefa" como ação do alerta <br> **ENTÃO:** o sistema grava a ação, o meu usuário e o horário no alerta, encerra o alerta e o retira da lista de alertas abertos |
| 2 | **DADO QUE:** um alerta está aberto <br> **QUANDO:** tento encerrá-lo sem escolher uma das ações <br> **ENTÃO:** o sistema recusa o encerramento, informa que a ação é obrigatória e o alerta continua aberto |
| 3 | **DADO QUE:** recebi um alerta às 10:00 e registrei a ação às 10:01:30 <br> **QUANDO:** consulto o histórico do alerta <br> **ENTÃO:** o sistema exibe o horário do alerta, o horário da ação, a ação escolhida e o meu usuário, o que permite calcular o tempo de resposta de 1 minuto e 30 segundos |

## US039 – REQUISITO RF-39: Confirmar a prontidão e liberar a aeronave

**COMO:** Autoridade de Liberação
**POSSO:** confirmar a prontidão da aeronave de um turnaround no estado "Pronto para liberação", registrando o horário real de prontidão (ARDT) [2]
**PARA:** liberar a aeronave só quando todas as tarefas obrigatórias terminaram e não há exceção aberta, deixando a decisão registrada com o meu nome e o horário

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** um turnaround está no estado "Pronto para liberação", com todas as tarefas obrigatórias nos estados "Concluída" ou "Não aplicável" e sem exceção aberta <br> **QUANDO:** confirmo a prontidão da aeronave <br> **ENTÃO:** o sistema grava o ARDT com o horário da confirmação, grava a decisão com o meu usuário e o turnaround passa para o estado "Liberado" |
| 2 | **DADO QUE:** um turnaround está no estado "Em exceção", com uma exceção aberta <br> **QUANDO:** tento confirmar a prontidão da aeronave <br> **ENTÃO:** o sistema recusa a confirmação, informa a exceção aberta, não grava o ARDT e o turnaround mantém o estado |
| 3 | **DADO QUE:** um turnaround está no estado "Operações em andamento", com a tarefa obrigatória de carregamento no estado "Em execução" <br> **QUANDO:** tento confirmar a prontidão da aeronave <br> **ENTÃO:** o sistema recusa a confirmação, lista a tarefa de carregamento como pendente, não grava o ARDT e o turnaround mantém o estado |
| 4 | **DADO QUE:** um turnaround está no estado "Pronto para liberação" <br> **QUANDO:** abro esse turnaround para confirmar a prontidão <br> **ENTÃO:** o sistema exibe as condições da liberação: as tarefas obrigatórias, com o estado e o horário de cada uma, e a indicação de que não há exceção aberta, antes da opção de confirmar |

## US040 – REQUISITO RF-40: Encerrar exceção

**COMO:** Coordenador de Turnaround
**POSSO:** encerrar uma exceção, registrando a solução adotada
**PARA:** que o turnaround saia da exceção no estado que corresponde ao andamento das tarefas e possa seguir para a liberação

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** um turnaround estava no estado "Operações em andamento" quando passou para "Em exceção", e só há uma exceção aberta <br> **QUANDO:** encerro essa exceção informando a solução <br> **ENTÃO:** o sistema grava a solução, o meu usuário e o horário na exceção, e o turnaround volta para o estado "Operações em andamento" |
| 2 | **DADO QUE:** um turnaround está no estado "Em exceção", com duas exceções abertas <br> **QUANDO:** encerro uma delas informando a solução <br> **ENTÃO:** o sistema grava a solução da exceção encerrada e o turnaround continua "Em exceção", porque ainda há outra exceção aberta |
| 3 | **DADO QUE:** um turnaround está no estado "Em exceção" <br> **QUANDO:** tento encerrar a exceção sem informar a solução <br> **ENTÃO:** o sistema recusa o encerramento, informa que a solução é obrigatória e a exceção continua aberta |
| 4 | **DADO QUE:** um turnaround estava em "Operações em andamento" quando passou para "Em exceção" e, durante a exceção, todas as tarefas obrigatórias chegaram a "Concluída" ou "Não aplicável" <br> **QUANDO:** encerro a única exceção aberta informando a solução <br> **ENTÃO:** o turnaround passa para "Pronto para liberação", e não para "Operações em andamento" |
| 5 | **DADO QUE:** um turnaround estava em "Em solo" quando passou para "Em exceção" e, durante a exceção, o Operador de Solo/Rampa iniciou a primeira tarefa <br> **QUANDO:** encerro a única exceção aberta informando a solução <br> **ENTÃO:** o turnaround passa para "Operações em andamento", e não volta para "Em solo" |

## US041 – REQUISITO RF-41: Atualizar o TOBT quando a projeção se afasta 5 minutos ou mais

**COMO:** Coordenador de Turnaround
**POSSO:** receber a solicitação de atualizar o TOBT quando a projeção de prontidão se afasta 5 minutos ou mais do TOBT vigente, para mais ou para menos, e registrar o novo valor
**PARA:** manter a previsão de prontidão confiável para quem depende dela, como pedem as regras de atualização do TOBT [8][9]

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** o TOBT vigente de um turnaround é 10:30 e a projeção de prontidão passa para 10:37 <br> **QUANDO:** o sistema recalcula a projeção <br> **ENTÃO:** o sistema me exibe a solicitação de atualização do TOBT do turnaround, com o TOBT vigente e a projeção |
| 2 | **DADO QUE:** o TOBT vigente de um turnaround é 10:30 e a projeção de prontidão passa para 10:24, ou seja, 6 minutos antes <br> **QUANDO:** o sistema recalcula a projeção <br> **ENTÃO:** o sistema me exibe a solicitação de atualização do TOBT como aviso de antecipação, e não como alerta de risco (ADR-0003) |
| 3 | **DADO QUE:** recebi a solicitação de atualização do TOBT de um turnaround com TOBT vigente 10:30 <br> **QUANDO:** informo o novo TOBT 10:37 <br> **ENTÃO:** o sistema grava o valor anterior (10:30), o novo valor (10:37), o meu usuário e o horário, passa a exibir 10:37 como TOBT vigente e mantém o TOBT planejado como referência da tolerância de 5 minutos (ADR-0001) |
| 4 | **DADO QUE:** o TOBT vigente de um turnaround é 10:30 e a projeção de prontidão passa para 10:34 <br> **QUANDO:** o sistema recalcula a projeção <br> **ENTÃO:** o sistema não exibe solicitação de atualização do TOBT, porque o desvio é menor que 5 minutos |

## US042 – REQUISITO RF-42: Replanejar tarefas ainda não iniciadas

**COMO:** Coordenador de Turnaround
**POSSO:** alterar a janela planejada ou as dependências das tarefas ainda não iniciadas e acionar um serviço sob demanda do catálogo, incluindo-o no plano
**PARA:** ajustar o plano diante de um desvio ou de um serviço que surgiu durante o turnaround e ver em seguida a nova projeção de prontidão e o novo caminho crítico

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** a tarefa de catering está no estado "Aguardando" e faz parte do caminho crítico <br> **QUANDO:** antecipo a janela planejada de início dessa tarefa em 10 minutos <br> **ENTÃO:** o sistema grava a alteração com o meu usuário e o horário, e exibe a projeção de prontidão e o caminho crítico recalculados |
| 2 | **DADO QUE:** a tarefa de abastecimento está no estado "Em execução" <br> **QUANDO:** tento alterar a janela planejada ou as dependências dessa tarefa <br> **ENTÃO:** o sistema recusa a alteração, informa que só tarefas ainda não iniciadas podem ser replanejadas e a tarefa mantém a janela e as dependências |
| 3 | **DADO QUE:** a tarefa de carregamento está no estado "Pronta" e tem como predecessora o descarregamento <br> **QUANDO:** retiro essa dependência <br> **ENTÃO:** o sistema grava a alteração com o meu usuário e o horário, e exibe a projeção de prontidão e o caminho crítico recalculados sem essa dependência |
| 4 | **DADO QUE:** a tripulação avisou que um assento precisa de limpeza profunda e o catálogo sob demanda do turnaround tem esse serviço, com duração planejada de 15 minutos <br> **QUANDO:** aciono o serviço, escolho um operador da equipe de limpeza, a janela, o desembarque como predecessora e o embarque como sucessora e informo o motivo <br> **ENTÃO:** o sistema inclui a tarefa no plano, grava a inclusão com o motivo, o meu usuário e o horário, a tarefa aparece na lista do operador escolhido e a projeção de prontidão e o caminho crítico são recalculados (ADR-0014) |
| 5 | **DADO QUE:** o embarque já depende do catering e o catering está "Aguardando" <br> **QUANDO:** tento fazer o catering depender do embarque <br> **ENTÃO:** o sistema recusa a alteração, mostra as tarefas que formariam o ciclo e o plano fica como estava |
| 6 | **DADO QUE:** a companhia do turnaround não permite abastecer com passageiros a bordo <br> **QUANDO:** tento retirar a dependência entre o abastecimento e o embarque <br> **ENTÃO:** o sistema recusa a alteração, informa a regra da companhia (ADR-0005) e o plano fica como estava |

## US043 – REQUISITO RF-43: Consultar operadores disponíveis da equipe

**COMO:** Coordenador de Turnaround
**POSSO:** consultar, ao reatribuir uma tarefa, a lista dos operadores da mesma equipe da tarefa que estão disponíveis, ordenada pelo tempo desde a última tarefa concluída por cada um
**PARA:** escolher rapidamente para quem passar a tarefa, sem procurar operador por operador

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** a equipe de limpeza tem três operadores sem tarefa em execução, que concluíram a última tarefa há 25, 10 e 3 minutos <br> **QUANDO:** escolho reatribuir uma tarefa de limpeza da cabine <br> **ENTÃO:** o sistema lista os três operadores na ordem de 25, 10 e 3 minutos desde a última tarefa concluída, mostrando esse tempo ao lado de cada nome |
| 2 | **DADO QUE:** a equipe de limpeza tem um operador com tarefa em execução e há operadores de outras equipes sem tarefa em execução <br> **QUANDO:** escolho reatribuir uma tarefa de limpeza da cabine <br> **ENTÃO:** a lista não mostra o operador com tarefa em execução nem os operadores de outras equipes |
| 3 | **DADO QUE:** todos os operadores da equipe de catering têm tarefa em execução <br> **QUANDO:** escolho reatribuir uma tarefa de catering <br> **ENTÃO:** o sistema informa que não há operador disponível na equipe e a tarefa mantém o operador original |

## US044 – REQUISITO RF-44: Registrar a saída da posição e encerrar o turnaround

**COMO:** Operador de Solo/Rampa
**POSSO:** registrar o horário real de saída da posição (AOBT) [2] de um turnaround no estado "Liberado", depois que a autorização de acionamento e push-back do controle de tráfego aéreo foi recebida fora do sistema
**PARA:** encerrar o turnaround com o horário real de saída e manter o histórico completo para consulta

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** um turnaround está no estado "Liberado" e a aeronave recebeu a autorização de push-back <br> **QUANDO:** registro a saída da posição <br> **ENTÃO:** o sistema grava o AOBT com o horário do registro e o meu usuário, e o turnaround passa para o estado "Fora de bloco" |
| 2 | **DADO QUE:** um turnaround está no estado "Pronto para liberação", sem a confirmação da Autoridade de Liberação <br> **QUANDO:** tento registrar a saída da posição <br> **ENTÃO:** o sistema recusa o registro, informa que o turnaround ainda não foi liberado, não grava o AOBT e o turnaround mantém o estado |
| 3 | **DADO QUE:** um turnaround está no estado "Fora de bloco" <br> **QUANDO:** um Operador de Solo/Rampa tenta registrar início, pausa ou conclusão de uma tarefa desse turnaround <br> **ENTÃO:** o sistema recusa o registro, informa que o turnaround está encerrado e mantém o histórico de tarefas, marcos e decisões disponível para consulta |

Fontes citadas: [2], [8], [9] e [62], conforme a numeração de `pesquisa/fontes.md`.
