## US001 – REQUISITO RF-1: Autenticar-se

**COMO:** Usuário, ator abstrato que representa os quatro perfis humanos

**POSSO:** autenticar-me e acessar a visão do meu perfil

**PARA:** acessar apenas as funções permitidas para mim

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** meu cadastro está ativo <br> **QUANDO:** informo credenciais válidas <br> **ENTÃO:** acesso a tela do meu perfil: tarefas (Operador de Solo/Rampa), painel (Coordenador de Turnaround), liberações (Autoridade de Liberação) ou usuários (Administrador do Sistema) |
| 2 | **DADO QUE:** estou na autenticação <br> **QUANDO:** informo credenciais inválidas ou uso cadastro desativado <br> **ENTÃO:** não é criada sessão e recebo a mensagem "Não foi possível autenticar. Verifique suas credenciais ou contate o administrador", sem revelar a causa específica |
| 3 | **DADO QUE:** estou autenticado como Operador de Solo/Rampa <br> **QUANDO:** tento acessar diretamente a gestão de usuários <br> **ENTÃO:** o acesso é recusado sem retornar dados protegidos ou alterar registros (RNF-1) |

## US002 – REQUISITO RF-2: Gerenciar usuários e perfis de acesso

**COMO:** Administrador do Sistema

**POSSO:** cadastrar, alterar e desativar usuários e atribuir perfil e equipe

**PARA:** manter os acessos necessários à operação e seu histórico

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** sou Administrador do Sistema autenticado <br> **QUANDO:** cadastro nome, identificador único, senha inicial, perfil Operador de Solo/Rampa e equipe ativa <br> **ENTÃO:** o operador fica ativo e pode entrar; o cadastro é auditado sem mostrar ou registrar a senha |
| 2 | **DADO QUE:** existe um usuário <br> **QUANDO:** altero seu perfil e informo equipe ativa quando o perfil for operador <br> **ENTÃO:** os novos dados são gravados e auditados, sem alterar a senha, o identificador interno ou a situação ativa/desativada |
| 3 | **DADO QUE:** existe um usuário ativo <br> **QUANDO:** confirmo sua desativação <br> **ENTÃO:** o histórico permanece, mas a próxima entrada ou ação protegida é bloqueada, mesmo com sessão aberta |
| 4 | **DADO QUE:** estou cadastrando ou alterando um usuário <br> **QUANDO:** há campo obrigatório vazio ou falta a senha inicial na criação <br> **ENTÃO:** o sistema indica o campo inválido e não grava |
| 5 | **DADO QUE:** estou cadastrando ou alterando um usuário <br> **QUANDO:** informo um identificador de acesso que já pertence a outro usuário <br> **ENTÃO:** o sistema indica a duplicidade e não grava |
| 6 | **DADO QUE:** estou cadastrando ou alterando um usuário <br> **QUANDO:** escolho um perfil fora dos quatro previstos ou deixo um operador sem equipe ativa <br> **ENTÃO:** o sistema indica o campo inválido e não grava |
| 7 | **DADO QUE:** um Operador de Solo/Rampa tem tarefa pendente (fora de "Concluída" e "Não aplicável") em turnaround não encerrado <br> **QUANDO:** tento desativá-lo <br> **ENTÃO:** o sistema recusa a desativação, lista as tarefas que precisam ser reatribuídas antes (RF-5 ou RF-37) e o usuário continua ativo |

## US003 – REQUISITO RF-3: Abrir turnaround

**COMO:** Coordenador de Turnaround

**POSSO:** abrir o cadastro de um turnaround com os voos, a companhia, a aeronave, a posição, o horário programado de chegada à posição (SIBT), o horário programado de saída da posição (SOBT), o horário estimado de chegada à posição (EIBT), o horário-alvo de prontidão (TOBT) e o tempo mínimo de turnaround (MTTT) [2][4], com data e fuso nos horários e o MTTT em minutos positivos; o TOBT planejado fica fixo e o vigente começa igual a ele (ADR-0003)

**PARA:** planejar as tarefas e comparar os horários previstos com os reais

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** os voos e datas ainda não têm turnaround <br> **QUANDO:** salvo voos, companhia, aeronave, posição, horários válidos e MTTT positivo <br> **ENTÃO:** o cadastro é criado com TOBT planejado fixo e vigente igual a ele, sem registrar chegada real nem iniciar tarefas |
| 2 | **DADO QUE:** estou preenchendo a abertura <br> **QUANDO:** falta um dado obrigatório, há horário inválido ou MTTT menor ou igual a zero <br> **ENTÃO:** os campos inválidos são indicados e nenhum cadastro é criado |
| 3 | **DADO QUE:** já existe um cadastro para os mesmos voos e datas <br> **QUANDO:** tento abrir novamente <br> **ENTÃO:** o sistema apresenta o identificador existente e não duplica o turnaround |
| 4 | **DADO QUE:** a chegada é às 23:50 e a partida às 00:40 do dia seguinte <br> **QUANDO:** informo datas completas e fusos <br> **ENTÃO:** os horários são preservados sem recusar a virada do dia |

## US004 – REQUISITO RF-4: Criar modelo de tarefas

**COMO:** Coordenador de Turnaround

**POSSO:** criar um modelo de tarefas por tipo de aeronave e serviço

**PARA:** reutilizar o planejamento em outros turnarounds

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** há equipes ativas cadastradas <br> **QUANDO:** salvo um modelo com nome, aeronave, serviço e tarefas com nome, tipo, equipe, duração positiva, obrigatoriedade, permissão de "Não aplicável" e indicação "sob demanda" <br> **ENTÃO:** o modelo e suas configurações são gravados com auditoria |
| 2 | **DADO QUE:** o serviço inclui embarque de passageiros <br> **QUANDO:** salvo exatamente uma tarefa do tipo Embarque <br> **ENTÃO:** essa tarefa fica identificada para o marco de embarque mesmo que seu nome livre seja diferente |
| 3 | **DADO QUE:** estou criando um modelo <br> **QUANDO:** há tarefa sem equipe ativa ou com duração não positiva <br> **ENTÃO:** o sistema indica o erro e não salva o modelo |
| 4 | **DADO QUE:** cadastro uma limpeza profunda como "sob demanda" com tipo, equipe e duração planejada <br> **QUANDO:** salvo o modelo <br> **ENTÃO:** o serviço fica no catálogo e não entra no plano até ser acionado pelo Coordenador de Turnaround (ADR-0014) [69][70][71] |
| 5 | **DADO QUE:** estou criando um modelo para um serviço com embarque de passageiros <br> **QUANDO:** o modelo não tem nenhuma tarefa do tipo Embarque ou tem mais de uma <br> **ENTÃO:** o sistema indica o erro e não salva o modelo |

## US005 – REQUISITO RF-5: Confirmar plano inicial

**COMO:** Coordenador de Turnaround

**POSSO:** atribuir responsáveis e janelas e confirmar o plano inicial

**PARA:** deixar todas as tarefas com responsável e horários válidos antes de começar

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** nenhuma tarefa começou <br> **QUANDO:** confirmo responsáveis ativos da equipe correta, horários válidos, dependências e política de abastecimento <br> **ENTÃO:** o plano é salvo e auditado com todas as tarefas atribuídas, sem iniciar a execução |
| 2 | **DADO QUE:** há tarefa sem responsável, com operador desativado ou de outra equipe <br> **QUANDO:** tento confirmar <br> **ENTÃO:** o sistema lista as tarefas inválidas e não altera o último plano |
| 3 | **DADO QUE:** o fim planejado de uma tarefa é igual ou anterior ao início, ou seu início planejado vem antes do fim de uma predecessora <br> **QUANDO:** tento confirmar o plano <br> **ENTÃO:** o sistema indica o conflito e mantém o plano anterior |
| 4 | **DADO QUE:** alguma tarefa começou durante a edição <br> **QUANDO:** tento salvar o plano inicial <br> **ENTÃO:** a alteração é recusada e a operação em andamento não é modificada; replanejamento fica no RF-42 |
| 5 | **DADO QUE:** há serviço sob demanda no catálogo e nenhuma tarefa começou <br> **QUANDO:** incluo o serviço já conhecido e confirmo responsável ativo da equipe correta, janela, dependências e política válidas <br> **ENTÃO:** a tarefa entra no plano inicial com auditoria e segue as mesmas regras das demais tarefas (ADR-0014) |

## US006 – REQUISITO RF-6: Aplicar modelo de tarefas

**COMO:** Coordenador de Turnaround

**POSSO:** selecionar e aplicar um modelo compatível ao turnaround

**PARA:** planejar as tarefas sem alterar o modelo original

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** não há plano confirmado nem tarefa iniciada <br> **QUANDO:** aplico um modelo compatível com aeronave e serviço <br> **ENTÃO:** as tarefas regulares, o catálogo sob demanda e suas configurações são copiados com identificadores próprios, respeitando a política da companhia, sem alterar o modelo nem atribuir operadores |
| 2 | **DADO QUE:** já existe uma cópia, ainda sem plano confirmado ou tarefa iniciada <br> **QUANDO:** cancelo a confirmação de substituição <br> **ENTÃO:** a cópia anterior permanece inalterada |
| 3 | **DADO QUE:** o modelo é incompatível, o plano está confirmado ou uma tarefa começou <br> **QUANDO:** tento aplicar <br> **ENTÃO:** o sistema informa a condição impeditiva e preserva as tarefas atuais |
| 4 | **DADO QUE:** o modelo possui serviço sob demanda com dependências e pontos <br> **QUANDO:** aplico o modelo <br> **ENTÃO:** o serviço e seus vínculos são copiados para o catálogo do turnaround, mas não entram no plano até acionamento pelo RF-5 ou RF-42 |
| 5 | **DADO QUE:** já existe uma cópia, ainda sem plano confirmado ou tarefa iniciada <br> **QUANDO:** confirmo a substituição por outro modelo compatível <br> **ENTÃO:** a cópia anterior é substituída pelas tarefas regulares e pelo catálogo sob demanda do novo modelo, com identificadores próprios e auditoria, sem alterar nenhum dos modelos |

## US007 – REQUISITO RF-7: Configurar pontos de confirmação

**COMO:** Coordenador de Turnaround

**POSSO:** configurar pontos de código de resposta rápida (QR Code) exigidos em uma tarefa

**PARA:** exigir a confirmação desses pontos antes de concluir a tarefa (ADR-0007)

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** a limpeza exige confirmação de duas zonas <br> **QUANDO:** salvo dois pontos com nomes e identificadores distintos na tarefa do modelo <br> **ENTÃO:** os dois pontos ficam associados à tarefa como confirmações exigidas |
| 2 | **DADO QUE:** uma tarefa não exige confirmação por pontos <br> **QUANDO:** salvo sua configuração sem pontos <br> **ENTÃO:** a lista vazia é aceita e não cria uma exigência de leitura |
| 3 | **DADO QUE:** estou editando os pontos <br> **QUANDO:** repito nome ou identificador dentro da mesma tarefa <br> **ENTÃO:** o sistema indica a duplicidade e não grava a alteração |
| 4 | **DADO QUE:** o modelo possui pontos exigidos <br> **QUANDO:** aplico o modelo <br> **ENTÃO:** os pontos são copiados com seus vínculos; editar o modelo depois não altera a cópia existente |

## US008 – REQUISITO RF-8: Definir dependências entre tarefas

**COMO:** Coordenador de Turnaround

**POSSO:** definir quais tarefas precisam terminar antes de outras

**PARA:** organizar a sequência sem impedir tarefas independentes em paralelo

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** desembarque e limpeza pertencem ao mesmo modelo <br> **QUANDO:** defino desembarque como predecessora da limpeza sem formar ciclo <br> **ENTÃO:** a dependência é salva e será copiada ao turnaround |
| 2 | **DADO QUE:** limpeza e catering são independentes e a política da companhia permite a configuração <br> **QUANDO:** confirmo janelas sobrepostas com operadores distintos <br> **ENTÃO:** o plano permite o paralelismo |
| 3 | **DADO QUE:** estou editando dependências <br> **QUANDO:** crio um ciclo (A depende de B e B de A), uso tarefa inexistente ou de outro modelo ou turnaround <br> **ENTÃO:** o sistema indica o erro e não salva |
| 4 | **DADO QUE:** alguma tarefa do turnaround começou <br> **QUANDO:** tento alterar dependências pelo plano inicial <br> **ENTÃO:** a alteração é recusada e deve ser tratada pelo replanejamento do RF-42 |

## US009 – REQUISITO RF-9: Gerenciar equipes e especialidades

**COMO:** Administrador do Sistema

**POSSO:** cadastrar, alterar e desativar equipes ou especialidades

**PARA:** organizar as equipes dos operadores e das tarefas

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** o identificador ainda não está cadastrado <br> **QUANDO:** salvo nome e identificador de uma equipe <br> **ENTÃO:** a equipe é criada ativa e fica disponível para novos vínculos, com autor e horário registrados |
| 2 | **DADO QUE:** existe uma equipe <br> **QUANDO:** altero seu nome <br> **ENTÃO:** o nome é atualizado sem mudar seu identificador interno ou perder vínculos e histórico |
| 3 | **DADO QUE:** uma equipe não tem usuários ativos vinculados nem tarefas pendentes em turnarounds não encerrados <br> **QUANDO:** confirmo sua desativação <br> **ENTÃO:** novos vínculos são impedidos e os anteriores permanecem consultáveis |
| 4 | **DADO QUE:** faltam dados, há identificador duplicado ou a equipe tem vínculo que impede desativação <br> **QUANDO:** tento salvar ou desativar <br> **ENTÃO:** o motivo é informado e a equipe permanece inalterada |

## US010 – REQUISITO RF-10: Atualizar referências de previsão

**COMO:** Coordenador de Turnaround

**POSSO:** atualizar o horário estimado de chegada à posição (EIBT) e o tempo mínimo de turnaround (MTTT)

**PARA:** fornecer os dados à checagem de viabilidade do RF-29 [3][7]

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** a chegada ainda não foi registrada <br> **QUANDO:** salvo EIBT com data e fuso e MTTT positivo <br> **ENTÃO:** a mudança é auditada e enviada ao Motor de Eventos, sem alterar os horários-alvo planejado e vigente |
| 2 | **DADO QUE:** estou revisando a previsão <br> **QUANDO:** altero apenas um dos dois campos <br> **ENTÃO:** somente esse valor é atualizado e o outro permanece igual |
| 3 | **DADO QUE:** o horário é inválido, MTTT não é positivo ou a chegada real já foi registrada <br> **QUANDO:** tento confirmar <br> **ENTÃO:** a alteração é recusada com motivo e os valores anteriores permanecem |

## US011 – REQUISITO RF-11: Configurar política de abastecimento

**COMO:** Coordenador de Turnaround

**POSSO:** configurar por companhia a permissão de abastecimento com passageiros

**PARA:** aplicar ao plano a política operacional autorizada da companhia (ADR-0005) [24][26][27]

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** uma companhia ainda não tem configuração <br> **QUANDO:** consulto sua regra <br> **ENTÃO:** a permissão está desabilitada por padrão e o plano exige desembarque antes do abastecimento e abastecimento antes do embarque |
| 2 | **DADO QUE:** disponho da política autorizada da companhia <br> **QUANDO:** habilito a regra e confirmo <br> **ENTÃO:** a configuração é salva e auditada para novos turnarounds; permite paralelismo sem remover outras dependências |
| 3 | **DADO QUE:** um turnaround já foi iniciado com a regra desabilitada <br> **QUANDO:** altero a configuração geral da companhia <br> **ENTÃO:** a cópia da regra e as dependências desse turnaround permanecem inalteradas |
| 4 | **DADO QUE:** um plano tem permissão desabilitada e não respeita a sequência desembarque, abastecimento e embarque <br> **QUANDO:** tento confirmá-lo <br> **ENTÃO:** o sistema indica o conflito e não confirma o plano |

## US012 – REQUISITO RF-12: Registrar chegada à posição

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

## US013 – REQUISITO RF-13: Corrigir chegada à posição

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

Fontes citadas: [2], [3], [4], [7], [24], [26], [27], [69], [70] e [71], conforme `pesquisa/fontes.md`.
