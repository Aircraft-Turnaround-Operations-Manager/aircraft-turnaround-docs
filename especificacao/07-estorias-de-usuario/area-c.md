## US022 – REQUISITO RF-22: Recalcular a projeção de prontidão

**COMO:** Motor de Eventos
**POSSO:** recalcular a projeção de prontidão do turnaround a cada registro de tarefa, a cada alteração do plano, a cada atualização do horário-alvo de prontidão (TOBT) [2] vigente, a cada correção da chegada à posição e a cada minuto
**PARA:** que o Coordenador de Turnaround saiba, a todo momento, se a aeronave fica pronta dentro do TOBT planejado mais 5 minutos (ADR-0001)

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** no turnaround PR-XMA, com TOBT planejado e vigente 10:30, a limpeza da cabine tem duração planejada de 20 minutos e é seguida pelo embarque (12 minutos), pelo loadsheet (2 minutos) e pelo fechamento de portas (2 minutos), todos obrigatórios <br> **QUANDO:** o Operador de Solo/Rampa registra o início da limpeza às 10:01 <br> **ENTÃO:** o sistema calcula os fins projetados 10:21, 10:33, 10:35 e 10:37, grava a projeção de prontidão 10:37 com o horário 10:01 e o registro de início da limpeza como causa, e grava a comparação: 7 minutos depois do TOBT planejado, fora da régua de TOBT + 5, e 7 minutos depois do TOBT vigente |
| 2 | **DADO QUE:** o abastecimento está "Pausada" desde 10:06 e faltam 7 minutos de execução <br> **QUANDO:** o sistema faz o recálculo de minuto às 10:15 <br> **ENTÃO:** o fim projetado do abastecimento passa a 10:22, que é o horário atual somado à duração que falta |
| 3 | **DADO QUE:** uma tarefa obrigatória é a de maior fim projetado do turnaround <br> **QUANDO:** o Operador de Solo/Rampa marca essa tarefa como "Não aplicável" <br> **ENTÃO:** o sistema retira a tarefa do cálculo e grava a nova projeção de prontidão, que passa a ser o maior fim projetado entre as tarefas obrigatórias restantes |
| 4 | **DADO QUE:** o turnaround está no estado "Liberado" ou "Fora de bloco" <br> **QUANDO:** chega o horário do recálculo de minuto <br> **ENTÃO:** o sistema não recalcula, e a última projeção gravada continua a mesma |
| 5 | **DADO QUE:** a limpeza da cabine foi iniciada às 10:01, tem duração planejada de 20 minutos e continua "Em execução" às 10:25 <br> **QUANDO:** o sistema faz o recálculo de minuto às 10:25 <br> **ENTÃO:** o fim projetado da limpeza passa a 10:25, o horário atual, porque ele é maior que o início real somado à duração planejada (10:21) |

## US023 – REQUISITO RF-23: Calcular o atraso das tarefas e marcar as impactadas

**COMO:** Motor de Eventos
**POSSO:** calcular, a cada recálculo da projeção, o atraso de início e de fim de cada tarefa e marcar como "impactada" a sucessora que o atraso empurra para além do fim planejado
**PARA:** que o Coordenador de Turnaround veja onde o atraso nasceu e até onde ele se propaga

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** a limpeza da cabine tem início planejado 09:54 e fim planejado 10:14 <br> **QUANDO:** o Operador de Solo/Rampa registra o início às 10:01 e o sistema recalcula a projeção, com fim projetado 10:21 <br> **ENTÃO:** o sistema grava o atraso de início de 7 minutos e o atraso de fim de 7 minutos na limpeza |
| 2 | **DADO QUE:** o embarque tem fim planejado 10:26, e a limpeza é a predecessora dele de maior fim projetado, que passou a 10:21 em vez de 10:14 <br> **QUANDO:** o sistema recalcula a projeção <br> **ENTÃO:** o embarque fica marcado como "impactado", com a limpeza como tarefa de origem e 7 minutos de impacto |
| 3 | **DADO QUE:** o carregamento de bagagem tem início planejado 10:00 e foi iniciado às 09:58 <br> **QUANDO:** o sistema recalcula a projeção <br> **ENTÃO:** o atraso de início do carregamento é gravado como sem atraso, porque o resultado é menor que zero |
| 4 | **DADO QUE:** o catering tem início planejado 10:05, ainda não foi iniciado e o horário atual é 10:09:40 <br> **QUANDO:** o sistema faz o recálculo de minuto <br> **ENTÃO:** o atraso de início do catering é gravado como 4 minutos, contados em minutos completos [3] |

## US024 – REQUISITO RF-24: Identificar o caminho crítico

**COMO:** Motor de Eventos
**POSSO:** identificar, a cada recálculo da projeção, o caminho crítico do turnaround e gravar cada mudança dele
**PARA:** que o Coordenador de Turnaround saiba quais tarefas, se atrasarem, atrasam a prontidão da aeronave [24]

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** o caminho crítico gravado do PR-XMA é calçar → desembarque → limpeza → embarque → loadsheet → fechar portas <br> **QUANDO:** o sistema recalcula a projeção depois do início da limpeza e o caminho continua o mesmo <br> **ENTÃO:** o caminho crítico gravado continua o mesmo e o sistema não grava mudança de caminho |
| 2 | **DADO QUE:** às 10:15 o abastecimento está "Pausada" e o fim projetado dele (10:22) passa o da limpeza (10:21), ambos predecessores do embarque <br> **QUANDO:** o sistema faz o recálculo de minuto <br> **ENTÃO:** o novo caminho crítico passa a ser calçar → desembarque → abastecimento → embarque → loadsheet → fechar portas, e o sistema grava o caminho anterior, o novo, o horário 10:15 e o recálculo de minuto como causa |
| 3 | **DADO QUE:** uma tarefa do caminho crítico ainda não foi iniciada <br> **QUANDO:** o Operador de Solo/Rampa a marca como "Não aplicável" <br> **ENTÃO:** o sistema recalcula o caminho crítico sem essa tarefa e grava a mudança com o registro de "Não aplicável" como causa |

## US025 – REQUISITO RF-25: Acompanhar os turnarounds no painel

**COMO:** Coordenador de Turnaround
**POSSO:** acompanhar em um painel todos os turnarounds que ainda não saíram da posição, com o estado, o TOBT planejado e o vigente, a projeção de prontidão, a diferença em minutos, a quantidade de alertas abertos e uma cor de risco
**PARA:** atender primeiro os turnarounds que estão mais longe do horário planejado

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** há três turnarounds abertos: PR-XMA com projeção 10:37 e TOBT planejado 10:30, PR-YRB com 11:03 e 11:00 e PR-GTA com 10:43 e 10:45 <br> **QUANDO:** abro o painel <br> **ENTÃO:** o sistema exibe PR-XMA em vermelho (+7 min), PR-YRB em amarelo (+3 min) e PR-GTA em verde (−2 min), nessa ordem, cada um com o estado, os dois TOBT, a projeção, a diferença e a quantidade de alertas abertos |
| 2 | **DADO QUE:** o PR-YRB está em amarelo no painel <br> **QUANDO:** o Motor de Eventos emite um alerta crítico para o PR-YRB <br> **ENTÃO:** o PR-YRB passa a vermelho e a quantidade de alertas abertos dele aumenta em 1, em até 5 segundos e sem que eu recarregue a página |
| 3 | **DADO QUE:** o PR-GTA está no painel <br> **QUANDO:** o turnaround do PR-GTA passa para o estado "Fora de bloco" <br> **ENTÃO:** o PR-GTA sai do painel, sem que eu recarregue a página |
| 4 | **DADO QUE:** um turnaround foi aberto e a aeronave ainda não chegou à posição <br> **QUANDO:** abro o painel <br> **ENTÃO:** o turnaround aparece na lista com o horário estimado de chegada à posição (EIBT) no lugar do estado |

## US026 – REQUISITO RF-26: Consultar a linha do tempo do turnaround

**COMO:** Coordenador de Turnaround
**POSSO:** abrir, a partir do painel, a linha do tempo de um turnaround, com as tarefas, os horários planejados e os reais ou projetados, os atrasos, o caminho crítico, as tarefas impactadas e os marcos já registrados
**PARA:** entender onde está o atraso e quem é o responsável antes de decidir como agir

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** o PR-XMA está no painel, com a limpeza da cabine atrasada 7 minutos e o embarque impactado por ela <br> **QUANDO:** seleciono o PR-XMA <br> **ENTÃO:** o sistema exibe cada tarefa com a equipe, o Operador de Solo/Rampa responsável, o estado, o início e o fim planejados, o início e o fim reais ou projetados e o atraso, com as tarefas do caminho crítico destacadas e o embarque marcado como "impactado por Limpeza da cabine · +7 min" |
| 2 | **DADO QUE:** o abastecimento foi pausado com a justificativa "atraso do caminhão" e o código GF da tabela de códigos de atraso da Agência Nacional de Aviação Civil (ANAC) [62] <br> **QUANDO:** abro a linha do tempo do turnaround <br> **ENTÃO:** o abastecimento aparece como "Pausada", com a justificativa e o código informados na pausa |
| 3 | **DADO QUE:** a água potável foi marcada como "Não aplicável" com a justificativa "tanque cheio" <br> **QUANDO:** abro a linha do tempo do turnaround <br> **ENTÃO:** a tarefa aparece como "Não aplicável", com a justificativa, e sem atraso calculado |
| 4 | **DADO QUE:** o turnaround tem registrados só o horário real de chegada à posição (AIBT) [2], às 09:40, e o início real do atendimento em solo (ACGT), às 09:42 <br> **QUANDO:** abro a linha do tempo do turnaround <br> **ENTÃO:** a faixa de marcos mostra AIBT 09:40 e ACGT 09:42 e mostra sem horário o início real do embarque (ASBT), o fim real do atendimento em solo (AEGT), o horário real de prontidão (ARDT) e o horário real de saída da posição (AOBT) |

## US027 – REQUISITO RF-27: Alertar tarefa pronta não iniciada

**COMO:** Motor de Eventos
**POSSO:** emitir um alerta ao Coordenador de Turnaround quando uma tarefa fica "Pronta" sem registro de início por mais de Y minutos, sendo Y um parâmetro configurável
**PARA:** que a espera de uma equipe seja percebida antes de atrasar as tarefas seguintes, como na regra de limpeza não iniciada 3 minutos depois do fim do desembarque [42]

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** Y é 3 minutos e a limpeza da cabine do PR-OKV, com início planejado 09:58, está "Pronta" desde 09:59 <br> **QUANDO:** às 10:03 a limpeza continua sem registro de início <br> **ENTÃO:** o sistema emite o alerta com o turnaround, a tarefa, a equipe, o Operador de Solo/Rampa responsável e 4 minutos de espera |
| 2 | **DADO QUE:** Y é 3 minutos e o catering ficou "Pronta" às 09:50, com início planejado 10:00 <br> **QUANDO:** às 10:02 o catering continua sem registro de início <br> **ENTÃO:** o sistema não emite alerta, porque a espera conta a partir do início planejado, mais tarde que a entrada em "Pronta", e é de 2 minutos |
| 3 | **DADO QUE:** Y é 3 minutos e a limpeza da cabine está "Pronta" desde 09:59 <br> **QUANDO:** o Operador de Solo/Rampa registra o início às 10:01 <br> **ENTÃO:** o sistema não emite alerta para essa tarefa |

## US028 – REQUISITO RF-28: Alertar projeção além de TOBT + 5

**COMO:** Motor de Eventos
**POSSO:** emitir um alerta de risco ao horário ao Coordenador de Turnaround quando um recálculo leva a projeção de prontidão para mais de 5 minutos depois do TOBT planejado
**PARA:** que o Coordenador de Turnaround aja assim que o turnaround sai da régua do objetivo 1 (ADR-0001)

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** o PR-XMA tem TOBT planejado 10:30 e projeção 10:35 <br> **QUANDO:** às 10:00 o recálculo leva a projeção para 10:36 <br> **ENTÃO:** o sistema emite o alerta crítico com a projeção 10:36, o desvio de 6 minutos e as tarefas do caminho crítico com atraso |
| 2 | **DADO QUE:** já foi emitido o alerta do PR-XMA com a projeção 10:36 <br> **QUANDO:** o recálculo seguinte leva a projeção para 10:38 <br> **ENTÃO:** o sistema não emite outro alerta, porque a projeção não voltou para até 5 minutos depois do TOBT planejado |
| 3 | **DADO QUE:** o Coordenador de Turnaround registrou a ação do alerta anterior do PR-XMA (RF-38) e depois a projeção voltou para 10:35 <br> **QUANDO:** um novo recálculo leva a projeção para 10:37 <br> **ENTÃO:** o sistema emite um novo alerta crítico com a projeção 10:37 e o desvio de 7 minutos |
| 4 | **DADO QUE:** o PR-GTA tem TOBT planejado 10:45 <br> **QUANDO:** o recálculo leva a projeção para 10:50 <br> **ENTÃO:** o sistema não emite alerta, porque a projeção está até 5 minutos depois do TOBT planejado |

## US029 – REQUISITO RF-29: Verificar a viabilidade do turnaround

**COMO:** Motor de Eventos
**POSSO:** verificar, antes da chegada da aeronave à posição, se o EIBT somado ao tempo mínimo de turnaround (MTTT) fica depois do TOBT vigente
**PARA:** que o Coordenador de Turnaround saiba, antes de a aeronave chegar, que o turnaround já nasce sob risco [3][7]

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** o PR-AXB, sem chegada registrada, tem MTTT de 40 minutos e TOBT vigente 11:15 <br> **QUANDO:** às 10:11 o EIBT é alterado de 10:30 para 10:40 <br> **ENTÃO:** o sistema emite o alerta crítico com o EIBT 10:40, o MTTT de 40 minutos, o TOBT vigente 11:15 e o excesso de 5 minutos |
| 2 | **DADO QUE:** um turnaround sem chegada registrada tem MTTT de 45 minutos e TOBT vigente 10:30 <br> **QUANDO:** o turnaround é aberto com EIBT 09:40 <br> **ENTÃO:** o sistema não emite alerta, porque 09:40 mais 45 minutos dá 10:25, antes do TOBT vigente |
| 3 | **DADO QUE:** o AIBT do turnaround já foi registrado <br> **QUANDO:** o Coordenador de Turnaround atualiza o TOBT vigente do turnaround <br> **ENTÃO:** o sistema não faz a verificação de viabilidade nem emite alerta de viabilidade |

## US030 – REQUISITO RF-30: Alertar embarque não iniciado

**COMO:** Motor de Eventos
**POSSO:** emitir um alerta de risco ao horário ao Coordenador de Turnaround quando o ASBT não foi registrado até X minutos antes do TOBT vigente, sendo X um parâmetro configurável
**PARA:** que o Coordenador de Turnaround saiba a tempo que o TOBT pode não ser cumprido, como prevê o alerta de embarque não iniciado da tomada de decisão colaborativa em aeroportos (A-CDM) [2]

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** X é 20 minutos e o TOBT vigente do PR-XMA é 10:30 <br> **QUANDO:** às 10:10 o ASBT do PR-XMA não foi registrado <br> **ENTÃO:** o sistema emite o alerta crítico com o turnaround, o TOBT vigente e o estado da tarefa de embarque e das predecessoras dela |
| 2 | **DADO QUE:** X é 20 minutos e o TOBT vigente do PR-MBC é 10:30 <br> **QUANDO:** o ASBT do PR-MBC é registrado às 10:08 <br> **ENTÃO:** o sistema não emite o alerta de embarque não iniciado para o PR-MBC |
| 3 | **DADO QUE:** X é 20 minutos e o TOBT vigente do PR-XMA passa de 10:30 para 10:40 antes das 10:10 <br> **QUANDO:** às 10:10 o ASBT ainda não foi registrado <br> **ENTÃO:** o sistema não emite alerta às 10:10 e passa a verificar o ASBT às 10:20 |

## US031 – REQUISITO RF-31: Alertar prontidão não registrada

**COMO:** Motor de Eventos
**POSSO:** emitir um alerta de risco ao horário ao Coordenador de Turnaround quando o ARDT não foi registrado até 5 minutos depois do TOBT vigente
**PARA:** que o Coordenador de Turnaround saiba que o TOBT passou sem a confirmação de prontidão, como prevê a especificação do A-CDM [2]

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** o TOBT vigente do PR-XMA é 10:30 e o turnaround está "Operações em andamento" <br> **QUANDO:** às 10:36:00 o ARDT não foi registrado <br> **ENTÃO:** o sistema emite o alerta crítico com o turnaround, o TOBT vigente, o estado do turnaround e as tarefas obrigatórias ainda não concluídas |
| 2 | **DADO QUE:** o TOBT vigente do PR-XMA é 10:30 <br> **QUANDO:** às 10:35:59 o ARDT ainda não foi registrado <br> **ENTÃO:** o sistema ainda não emite o alerta, porque os minutos são contados completos [3] |
| 3 | **DADO QUE:** o TOBT vigente do PR-XMA é 10:30 <br> **QUANDO:** a Autoridade de Liberação registra o ARDT às 10:33 <br> **ENTÃO:** o sistema não emite o alerta de prontidão não registrada para o PR-XMA |

## US032 – REQUISITO RF-32: Exibir o aviso de checagem em TOBT − 15

**COMO:** Motor de Eventos
**POSSO:** exibir ao Coordenador de Turnaround, 15 minutos antes do TOBT vigente, um aviso de checagem com as tarefas obrigatórias não concluídas e as equipes responsáveis
**PARA:** que o Coordenador de Turnaround confira o prazo com essas equipes, como manda o cartão de rampa dos aeroportos alemães [13]

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** o PR-YRB tem TOBT vigente 11:00 e está "Operações em andamento", com tarefas obrigatórias ainda não concluídas, entre elas a limpeza da cabine, o carregamento de bagagem e o embarque <br> **QUANDO:** o relógio chega a 10:45 <br> **ENTÃO:** o sistema exibe ao Coordenador de Turnaround o aviso de checagem, identificado como aviso, com todas as tarefas obrigatórias não concluídas, as equipes, os responsáveis, os estados e os fins projetados |
| 2 | **DADO QUE:** o PR-TLD tem TOBT vigente 11:00 e já está "Pronto para liberação" <br> **QUANDO:** o relógio chega a 10:45 <br> **ENTÃO:** o sistema não exibe o aviso de checagem para o PR-TLD |
| 3 | **DADO QUE:** o aviso de checagem do PR-YRB foi exibido <br> **QUANDO:** o Coordenador de Turnaround consulta a lista de alertas e o painel <br> **ENTÃO:** o aviso não aparece na lista de alertas e não muda a cor do PR-YRB no painel |
| 4 | **DADO QUE:** o TOBT vigente do PR-YRB passa de 11:00 para 11:10 antes das 10:45 <br> **QUANDO:** o relógio chega a 10:45 <br> **ENTÃO:** o sistema não exibe o aviso às 10:45 e o exibe às 10:55 |

## US033 – REQUISITO RF-33: Consultar a lista de alertas abertos

**COMO:** Coordenador de Turnaround
**POSSO:** consultar a lista dos alertas abertos de todos os turnarounds, do mais antigo para o mais recente, com o tipo, a tarefa, o horário de emissão, o tempo decorrido e a classificação
**PARA:** tratar primeiro os alertas mais antigos e os críticos, dentro do prazo de 2 minutos do objetivo 3

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** às 10:12 há quatro alertas abertos, emitidos às 10:00, 10:03, 10:10 e 10:11 <br> **QUANDO:** abro a lista de alertas <br> **ENTÃO:** o sistema exibe os quatro nessa ordem, cada um com o turnaround, o tipo, a tarefa quando houver, o horário de emissão, o tempo decorrido (12, 9, 2 e 1 minutos) e a classificação |
| 2 | **DADO QUE:** o alerta de tarefa pronta não iniciada da limpeza do PR-OKV, que está no caminho crítico, e o do carregamento de bagagem do PR-GTA, fora do caminho crítico, estão abertos <br> **QUANDO:** abro a lista de alertas <br> **ENTÃO:** o alerta do PR-OKV aparece como "crítico" e o do PR-GTA como "não crítico" |
| 3 | **DADO QUE:** o alerta mais antigo da lista está aberto <br> **QUANDO:** registro a ação tomada para ele (RF-38) <br> **ENTÃO:** o alerta sai da lista e os demais continuam |
| 4 | **DADO QUE:** não há alerta aberto em nenhum turnaround <br> **QUANDO:** abro a lista de alertas <br> **ENTÃO:** o sistema exibe a mensagem "Nenhum alerta aberto" |

## US034 – REQUISITO RF-34: Consultar os indicadores de aderência

**COMO:** Coordenador de Turnaround
**POSSO:** consultar, para um período escolhido, os indicadores de aderência dos turnarounds encerrados nele, cada um com numerador e denominador
**PARA:** acompanhar as metas dos objetivos 1 e 3 e as atualizações tardias do TOBT [7]

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** 10 turnarounds chegaram ao estado "Fora de bloco" entre 01/10/2026 e 07/10/2026 <br> **QUANDO:** consulto os indicadores desse período <br> **ENTÃO:** o sistema exibe o percentual, o numerador e o denominador de cada indicador: prontidão até TOBT planejado + 5 (8/10, 80%), tarefas dentro da janela planejada (120/150, 80%), alertas críticos com ação em até 2 minutos (18/20, 90%) e atualizações do TOBT a menos de 10 minutos do TOBT vigente (2/10, 20%) |
| 2 | **DADO QUE:** um turnaround do período está no estado "Liberado", sem saída da posição registrada <br> **QUANDO:** consulto os indicadores do período <br> **ENTÃO:** esse turnaround não entra em nenhum indicador |
| 3 | **DADO QUE:** um turnaround tem TOBT planejado 10:30 e entrou em "Pronto para liberação" às 10:35:59, e outro tem TOBT planejado 11:00 e entrou às 11:06:00 <br> **QUANDO:** consulto os indicadores do período <br> **ENTÃO:** o primeiro conta como dentro da régua e o segundo como fora, porque os minutos são contados completos [3] |
| 4 | **DADO QUE:** nenhum turnaround chegou a "Fora de bloco" entre 08/10/2026 e 09/10/2026 <br> **QUANDO:** consulto os indicadores desse período <br> **ENTÃO:** o sistema informa que não há turnarounds encerrados no período e não exibe percentuais |
| 5 | **DADO QUE:** informei a data de início 07/10/2026 e a data de fim 01/10/2026 <br> **QUANDO:** peço os indicadores <br> **ENTÃO:** o sistema recusa o período, informa que a data de fim deve ser igual ou posterior à de início e não calcula os indicadores |

## US035 – REQUISITO RF-35: Registrar a checagem com as equipes

**COMO:** Coordenador de Turnaround
**POSSO:** registrar que fiz a checagem com as equipes de um aviso de TOBT − 15 aberto
**PARA:** deixar gravado quem conferiu o prazo e quando, e encerrar o aviso

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** o aviso de checagem do PR-YRB está aberto desde 10:45 <br> **QUANDO:** confiro o prazo com as equipes e registro a checagem às 10:47 <br> **ENTÃO:** o sistema grava o meu usuário e o horário 10:47 e encerra o aviso |
| 2 | **DADO QUE:** outro Coordenador de Turnaround já registrou a checagem do aviso do PR-YRB <br> **QUANDO:** tento registrar a checagem do mesmo aviso <br> **ENTÃO:** o sistema recusa o registro, informa que o aviso já foi encerrado e mantém o autor e o horário do primeiro registro |
| 3 | **DADO QUE:** o aviso de checagem do PR-YRB está aberto <br> **QUANDO:** fecho o aviso sem registrar a checagem <br> **ENTÃO:** o aviso continua aberto e aparece na linha do tempo do PR-YRB até a checagem ser registrada |

Fontes citadas: [2], [3], [7], [13], [24], [42] e [62], conforme a numeração de `pesquisa/fontes.md`.
