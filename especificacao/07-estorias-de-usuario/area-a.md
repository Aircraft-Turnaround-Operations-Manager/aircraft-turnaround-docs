**Termos usados nas histórias:**

- Auditoria: registro de quem fez a alteração, quando e o que mudou (RNF-A2).
- Janela: horários planejados de início e fim de uma tarefa.
- Predecessora: tarefa que precisa terminar antes de outra começar.
- Modelo: conjunto de tarefas e regras que pode ser reutilizado.

## US-A1 – REQUISITO RF-A1: Autenticar-se

**COMO:** Usuário, ator abstrato que representa os quatro perfis humanos

**POSSO:** autenticar-me e acessar a visão do meu perfil

**PARA:** acessar apenas as funções permitidas para mim

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** meu cadastro está ativo <br> **QUANDO:** informo credenciais válidas <br> **ENTÃO:** acesso a tela do meu perfil: tarefas (Operador de Solo/Rampa), painel (Coordenador de Turnaround), liberações (Autoridade de Liberação) ou usuários (Administrador do Sistema) |
| 2 | **DADO QUE:** estou na autenticação <br> **QUANDO:** informo credenciais inválidas ou uso cadastro desativado <br> **ENTÃO:** não é criada sessão e recebo a mensagem "Não foi possível autenticar. Verifique suas credenciais ou contate o administrador", sem revelar a causa específica |
| 3 | **DADO QUE:** estou autenticado como Operador de Solo/Rampa <br> **QUANDO:** tento acessar diretamente a gestão de usuários <br> **ENTÃO:** o acesso é recusado sem retornar dados protegidos ou alterar registros (RNF-A1) |

## US-A2 – REQUISITO RF-A2: Gerenciar usuários e perfis de acesso

**COMO:** Administrador do Sistema

**POSSO:** cadastrar, alterar e desativar usuários e atribuir perfil e equipe

**PARA:** manter os acessos necessários à operação e seu histórico

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** sou Administrador do Sistema autenticado <br> **QUANDO:** cadastro nome, identificador único, senha inicial, perfil Operador de Solo/Rampa e equipe ativa <br> **ENTÃO:** o operador fica ativo e pode entrar; o cadastro é auditado sem mostrar ou registrar a senha |
| 2 | **DADO QUE:** existe um usuário <br> **QUANDO:** altero seu perfil e informo equipe ativa quando o perfil for operador <br> **ENTÃO:** os novos dados são gravados e auditados, sem alterar a senha, o identificador interno ou a situação ativa/desativada |
| 3 | **DADO QUE:** existe um usuário ativo <br> **QUANDO:** confirmo sua desativação <br> **ENTÃO:** o histórico permanece, mas a próxima entrada ou ação protegida é bloqueada, mesmo com sessão aberta |
| 4 | **DADO QUE:** estou cadastrando ou alterando um usuário <br> **QUANDO:** há campo obrigatório vazio, falta senha inicial na criação, identificador duplicado, perfil fora dos quatro previstos ou operador sem equipe ativa <br> **ENTÃO:** o sistema indica o campo inválido e não grava |

## US-A3 – REQUISITO RF-A3: Abrir turnaround

**COMO:** Coordenador de Turnaround

**POSSO:** abrir o cadastro de um turnaround com os voos e suas referências

**PARA:** planejar as tarefas e comparar os horários previstos com os reais

Os dados incluem horário programado de chegada à posição (SIBT), horário programado de saída da posição (SOBT), horário estimado de chegada à posição (EIBT), horário-alvo de prontidão (TOBT) e tempo mínimo de turnaround (MTTT) [2][4]. Os horários têm data e fuso; MTTT é recebido como entrada em minutos positivos. TOBT planejado é fixo; o vigente começa igual a ele (ADR-0003).

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** os voos e datas ainda não têm turnaround <br> **QUANDO:** salvo voos, companhia, aeronave, posição, horários válidos e MTTT positivo <br> **ENTÃO:** o cadastro é criado com TOBT planejado fixo e vigente igual a ele, sem registrar chegada real nem iniciar tarefas |
| 2 | **DADO QUE:** estou preenchendo a abertura <br> **QUANDO:** falta um dado obrigatório, há horário inválido ou MTTT menor ou igual a zero <br> **ENTÃO:** os campos inválidos são indicados e nenhum cadastro é criado |
| 3 | **DADO QUE:** já existe um cadastro para os mesmos voos e datas <br> **QUANDO:** tento abrir novamente <br> **ENTÃO:** o sistema apresenta o identificador existente e não duplica o turnaround |
| 4 | **DADO QUE:** a chegada é às 23:50 e a partida às 00:40 do dia seguinte <br> **QUANDO:** informo datas completas e fusos <br> **ENTÃO:** os horários são preservados sem recusar a virada do dia |

## US-A4 – REQUISITO RF-A4: Criar modelo de tarefas

**COMO:** Coordenador de Turnaround

**POSSO:** criar um modelo de tarefas por tipo de aeronave e serviço

**PARA:** reutilizar o planejamento em outros turnarounds

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** há equipes ativas cadastradas <br> **QUANDO:** salvo um modelo com nome, aeronave, serviço e tarefas com nome, tipo, equipe, duração positiva, obrigatoriedade e permissão de "Não aplicável" <br> **ENTÃO:** o modelo e suas configurações são gravados com auditoria |
| 2 | **DADO QUE:** o serviço inclui embarque de passageiros <br> **QUANDO:** salvo exatamente uma tarefa do tipo Embarque <br> **ENTÃO:** essa tarefa fica identificada para o marco de embarque mesmo que seu nome livre seja diferente |
| 3 | **DADO QUE:** estou criando um modelo <br> **QUANDO:** há tarefa sem equipe ativa, duração não positiva ou, para serviço com embarque, nenhuma ou mais de uma tarefa desse tipo <br> **ENTÃO:** o sistema indica o erro e não salva o modelo |

## US-A5 – REQUISITO RF-A5: Confirmar plano inicial

**COMO:** Coordenador de Turnaround

**POSSO:** atribuir responsáveis e janelas e confirmar o plano inicial

**PARA:** deixar todas as tarefas com responsável e horários válidos antes de começar

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** nenhuma tarefa começou <br> **QUANDO:** confirmo responsáveis ativos da equipe correta, horários válidos, dependências e política de abastecimento <br> **ENTÃO:** o plano é salvo e auditado com todas as tarefas atribuídas, sem iniciar a execução |
| 2 | **DADO QUE:** há tarefa sem responsável, com operador desativado ou de outra equipe <br> **QUANDO:** tento confirmar <br> **ENTÃO:** o sistema lista as tarefas inválidas e não altera o último plano |
| 3 | **DADO QUE:** o fim planejado de uma tarefa é igual ou anterior ao início, ou seu início planejado vem antes do fim de uma predecessora <br> **QUANDO:** tento confirmar o plano <br> **ENTÃO:** o sistema indica o conflito e mantém o plano anterior |
| 4 | **DADO QUE:** alguma tarefa começou durante a edição <br> **QUANDO:** tento salvar o plano inicial <br> **ENTÃO:** a alteração é recusada e a operação em andamento não é modificada; replanejamento pertence à área D |

## US-A6 – REQUISITO RF-A6: Aplicar modelo de tarefas

**COMO:** Coordenador de Turnaround

**POSSO:** selecionar e aplicar um modelo compatível ao turnaround

**PARA:** planejar as tarefas sem alterar o modelo original

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** não há plano confirmado nem tarefa iniciada <br> **QUANDO:** aplico um modelo compatível com aeronave e serviço <br> **ENTÃO:** todas as tarefas e configurações são copiadas com identificadores próprios, respeitando a política da companhia, sem alterar o modelo nem atribuir operadores |
| 2 | **DADO QUE:** já existe uma cópia, ainda sem plano confirmado ou tarefa iniciada <br> **QUANDO:** cancelo a confirmação de substituição <br> **ENTÃO:** a cópia anterior permanece inalterada |
| 3 | **DADO QUE:** o modelo é incompatível, o plano está confirmado ou uma tarefa começou <br> **QUANDO:** tento aplicar <br> **ENTÃO:** o sistema informa a condição impeditiva e preserva as tarefas atuais |

## US-A7 – REQUISITO RF-A7: Configurar pontos de confirmação

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

## US-A8 – REQUISITO RF-A8: Definir dependências entre tarefas

**COMO:** Coordenador de Turnaround

**POSSO:** definir quais tarefas precisam terminar antes de outras

**PARA:** organizar a sequência sem impedir tarefas independentes em paralelo

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** desembarque e limpeza pertencem ao mesmo modelo <br> **QUANDO:** defino desembarque como predecessora da limpeza sem formar ciclo <br> **ENTÃO:** a dependência é salva e será copiada ao turnaround |
| 2 | **DADO QUE:** limpeza e catering são independentes e a política da companhia permite a configuração <br> **QUANDO:** confirmo janelas sobrepostas com operadores distintos <br> **ENTÃO:** o plano permite o paralelismo |
| 3 | **DADO QUE:** estou editando dependências <br> **QUANDO:** crio um ciclo (A depende de B e B de A), uso tarefa inexistente ou de outro modelo ou turnaround <br> **ENTÃO:** o sistema indica o erro e não salva |
| 4 | **DADO QUE:** alguma tarefa do turnaround começou <br> **QUANDO:** tento alterar dependências pelo plano inicial <br> **ENTÃO:** a alteração é recusada e deve ser tratada pelo replanejamento da área D |

## US-A9 – REQUISITO RF-A9: Gerenciar equipes e especialidades

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

## US-A10 – REQUISITO RF-A10: Atualizar referências de previsão

**COMO:** Coordenador de Turnaround

**POSSO:** atualizar o horário estimado de chegada à posição (EIBT) e o tempo mínimo de turnaround (MTTT)

**PARA:** permitir que a área C verifique se o planejamento ainda é viável [3][7]

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** a chegada ainda não foi confirmada <br> **QUANDO:** salvo EIBT com data e fuso e MTTT positivo <br> **ENTÃO:** a mudança é auditada e enviada ao Motor de Eventos, sem alterar os horários-alvo planejado e vigente |
| 2 | **DADO QUE:** estou revisando a previsão <br> **QUANDO:** altero apenas um dos dois campos <br> **ENTÃO:** somente esse valor é atualizado e o outro permanece igual |
| 3 | **DADO QUE:** o horário é inválido, MTTT não é positivo ou a chegada real já foi confirmada <br> **QUANDO:** tento confirmar <br> **ENTÃO:** a alteração é recusada com motivo e os valores anteriores permanecem |

## US-A11 – REQUISITO RF-A11: Configurar política de abastecimento

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

## US-A12 – REQUISITO RF-A12: Registrar chegada à posição

**COMO:** Operador de Solo/Rampa com tarefa atribuída no turnaround

**POSSO:** informar o horário real de chegada à posição (AIBT) da aeronave [2][4]

**PARA:** solicitar a confirmação da chegada pelo Coordenador de Turnaround

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** tenho tarefa atribuída nesse turnaround e não há chegada confirmada ou envio pendente <br> **QUANDO:** envio o horário real com data e fuso, sem horário futuro <br> **ENTÃO:** a chegada fica "Pendente" com meu usuário e horário do envio, sem AIBT oficial, estado "Em solo" ou liberação de tarefas |
| 2 | **DADO QUE:** já existe envio pendente ou chegada confirmada <br> **QUANDO:** tento registrar outra chegada <br> **ENTÃO:** o sistema apresenta o registro existente e recusa a duplicidade, sem sobrescrever dados |
| 3 | **DADO QUE:** informo horário futuro ou inválido, ou não tenho tarefa atribuída nesse turnaround <br> **QUANDO:** tento enviar <br> **ENTÃO:** o sistema informa o motivo e não cria registro |
| 4 | **DADO QUE:** meu envio foi recusado com motivo <br> **QUANDO:** corrijo o horário e envio novamente <br> **ENTÃO:** há novo envio pendente ligado ao anterior, mantendo o histórico da recusa |

## US-A13 – REQUISITO RF-A13: Confirmar chegada à posição

**COMO:** Coordenador de Turnaround

**POSSO:** confirmar ou recusar o registro de chegada informado pelo operador

**PARA:** confirmar a chegada antes de liberar as tarefas que podem começar

O horário real de chegada à posição (AIBT) é o informado pelo operador, não o instante da confirmação [2][4].

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** existe chegada pendente e plano confirmado <br> **QUANDO:** confirmo a chegada <br> **ENTÃO:** o registro fica "Confirmado" e auditado; o AIBT usa o horário do operador, e o turnaround entra em "Em solo", acionando a área B |
| 2 | **DADO QUE:** existe chegada pendente <br> **QUANDO:** a recuso com motivo <br> **ENTÃO:** o registro fica "Recusado", o operador pode consultar o motivo e reenviar, e o AIBT oficial e o estado operacional não são alterados |
| 3 | **DADO QUE:** o envio já foi confirmado ou recusado <br> **QUANDO:** tento decidir novamente <br> **ENTÃO:** a decisão existente é mostrada, sem mudar horários nem acionar a área B de novo |
| 4 | **DADO QUE:** o plano ainda não está confirmado ou tento recusar sem motivo <br> **QUANDO:** tento concluir a respectiva ação <br> **ENTÃO:** o sistema informa o impedimento e mantém o registro pendente |
| 5 | **DADO QUE:** o operador informou chegada às 14:07 e estou confirmando às 14:10 <br> **QUANDO:** confirmo <br> **ENTÃO:** o AIBT fica 14:07 e o horário da confirmação fica 14:10, preservados como dados distintos |

Fontes citadas: [2], [3], [4], [7], [24], [26] e [27], conforme `pesquisa/fontes.md`. Os critérios de validação, unicidade e auditoria são regras internas propostas. O fluxo de chegada em duas etapas é uma proposta escolhida pelo autor e deve ser revisada em equipe antes do merge. O envio pendente não é o AIBT oficial nem um novo estado do turnaround.
