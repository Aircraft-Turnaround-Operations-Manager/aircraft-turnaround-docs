# 13 DIAGRAMA DE CLASSES

**PRODUTO:** Aircraft Turnaround Orchestration System

<!-- Item 13, tarefa T13 (issue #145), critérios C13.1 a C13.10 de entregas/ra2-criterios-de-aceite.md.
Fontes únicas das classes: especificacao/diagramas/13-classes-{contrato,cadastro,execucao,monitoramento,excecoes}.iuml
(PlantUML). Cada figura é uma vista 13-classes-<nome>.puml, que inclui as fontes e escolhe as classes que mostra;
a .png e a .svg têm o mesmo nome (Y.6, Y.7). scripts/conferir_classes.py confere as fontes contra o Apêndice B, o
CONTEXT.md e, com --sequencia, contra os diagramas de sequência do item 14 (C13.8). Tipos UML neutros (decisão B1). -->

O diagrama de classes descreve como o código do sistema se organiza. Ele parte do modelo de dados do item 12: cada tabela de negócio vira uma classe, com os mesmos nomes de domínio. Também mostra as classes técnicas da arquitetura de implementação, isto é, as que recebem as ações das telas, aplicam as regras de negócio e acessam o banco de cada serviço. O diagrama usa a linguagem de modelagem unificada (UML), em nível técnico: atributos com tipo e métodos com parâmetros e retorno tipados.

## 13.1 Arquitetura de implementação

O sistema tem quatro serviços, cada um com o seu banco, como decidido no registro de decisão de arquitetura (ADR) 0015: Cadastro e Planejamento, Execução em Solo, Monitoramento e Exceções e Liberação. Cada classe pertence a um só serviço, e o pacote da classe no diagrama é o serviço (`cadastro`, `execucao`, `monitoramento`, `excecoes`). Dois pacotes não são serviços: `contrato`, com o que os serviços combinaram entre si (ADR-0016), e `comum`, com a infraestrutura que cada serviço repete no seu próprio código.

Dentro de cada serviço, as classes seguem as camadas de referência da ADR-0015, `Controller → Service → Repository`, mais a tela e a comunicação com os outros serviços:

| Camada | Estereótipo | O que faz | Exemplo |
|---|---|---|---|
| Interface | «boundary» | Tela do site, em Angular (ADR-0016). Os métodos são as ações do usuário na tela. | `LiberacaoView` |
| Controle | «control», «resolver» | Recebe a requisição da porta de entrada ou de outro serviço por transferência de estado representacional (REST); nos painéis, por GraphQL («resolver») | `LiberacaoController`, `PainelResolver` |
| Serviço | «service» | Aplica as regras de negócio e decide sobre o dado de que o serviço é dono | `LiberacaoService` |
| Acesso a dados | «repository» | Lê e grava as tabelas do item 12 do próprio serviço | `LiberacaoRepository` |
| Negócio | «entity» | Classe que corresponde a uma tabela do item 12, com as regras que dependem só dos seus dados | `Liberacao` |
| Dado de troca | «dto» | Objeto de transferência de dados (DTO, em inglês *data transfer object*): dado de entrada ou de saída sem tabela própria, como o resultado de uma consulta | `SituacaoLiberacao` |
| Comunicação | «client», «publisher», «consumer», «websocket», «scheduler», «gateway» | Pedido a outro serviço, aviso pela mensageria, atualização da tela em tempo real, tarefa por horário e porta de entrada | `ExecucaoEmSoloCliente` |

As regras de comunicação são as da ADR-0015 e da ADR-0016:

- **Porta de entrada.** Toda ação do site passa pela `PortaDeEntrada`, que pergunta ao Cadastro, a cada ação, se a sessão e o usuário continuam ativos (`AcessoController.verificarAcesso`, requisito não funcional (RNF) 1). O controle do serviço recebe o `Acesso` (usuário, perfil, equipe e companhia) e confere se o perfil pode fazer a ação.
- **Pedido.** Quando um serviço precisa da decisão do dono do dado, faz um pedido em REST, com resposta, pelo seu cliente (`ExecucaoEmSoloCliente`, `CadastroCliente`). É o caso da abertura e do encerramento da exceção, da reatribuição, do replanejamento, da liberação e das consultas de tarefas pendentes e de operadores disponíveis (ADR-0015, regra 3). O diagrama liga cada cliente, por dependência, ao controle do outro serviço que atende o pedido, e todo método do cliente tem o mesmo nome, os mesmos parâmetros e o mesmo retorno no controle. Quando o pedido leva ou devolve um dado de troca, os dois serviços declaram o mesmo «dto», com os mesmos campos (`TarefaResumo`, `SituacaoTurnaround`, `PlanoConfirmado`, `MudancaEstado`, `OperadorAtivo`, `OperadorDisponivel`), porque nenhum usa a classe do outro.
- **Aviso.** O que já aconteceu vai num aviso, com o envelope comum da ADR-0016 (`EnvelopeAviso`). O serviço grava o aviso em `AvisoSaida` na mesma transação da mudança, e o `PublicadorAvisos` o publica na mensageria. Quem recebe usa o seu `ConsumidorAvisos`, que descarta o aviso repetido (`AvisoProcessado`).
- **Tempo real.** A lista de tarefas do operador (`ListaTarefasNotificador`, ADR-0018), os painéis do coordenador (`PainelNotificador`) e a solicitação de atualização da previsão (`CoordenadorNotificador`, ADR-0020) recebem as mudanças por WebSocket, para cumprir os 5 segundos do objetivo 2.
- **Telas de serviços diferentes.** O site é um só, então uma tela pode abrir a tela de outro serviço ou chamar o controle dele pela porta de entrada. O diagrama desenha essas dependências entre serviços (por exemplo, `AlertasView` do Monitoramento abre a `RegistroAcaoAlertaView` do Exceções e Liberação). Fora delas e dos clientes, nenhuma classe de um serviço depende de classe de outro.

**Correspondência com os atores e os estados** (critério Y.4):

- O Motor de Eventos, ator não humano do item 5, não é uma classe: é o comportamento automático de classes de três serviços. Na Execução em Solo, o `MarcoService` grava o início real do atendimento em solo (ACGT), o início real do embarque (ASBT) e o fim real do atendimento em solo (AEGT) (requisito funcional (RF) 20), e o `PropagacaoService` propaga o estado das tarefas e do turnaround (RF-21). No Monitoramento, o `RecalculoService` recalcula a projeção e o caminho crítico (RF-22 a RF-24), o `AlertaService` emite os alertas (RF-27 a RF-31), e o `AvisoChecagemService` emite o aviso de checagem (RF-32). O `AgendadorMinuto` dispara o que depende do relógio (ADR-0015, regra 7). No Exceções e Liberação, o `AtualizacaoTobtService.avaliarProjecao` compara cada projeção recebida com o horário-alvo de prontidão (TOBT) vigente e abre ou encerra a solicitação de atualização da previsão (caso de uso (UC) 34, passo 1).
- O Operador de Solo/Rampa, o Coordenador de Turnaround, a Autoridade de Liberação e o Administrador do Sistema são os valores da enumeração `Perfil`. As telas que cada um usa estão nas vistas da seção 13.5.
- Os estados do turnaround e da tarefa são as enumerações `EstadoTurnaround` e `EstadoTarefa`, com os valores exatos do `CONTEXT.md`. Só a Execução em Solo os muda (ADR-0015, regra 4); os outros serviços guardam cópia para exibir ou calcular.

## 13.2 Notação e convenções

- **Classe:** compartimentos de nome, atributos e métodos. Visibilidade em todo membro: `-` privado, `#` protegido e `+` público. O membro estático aparece sublinhado (por exemplo, `EnvelopeAviso.novo`).
- **Atributo:** `nome: Tipo`, com a multiplicidade entre colchetes quando o valor pode faltar (`[0..1]`); o atributo de um campo que o item 12 aceita vazio tem sempre `[0..1]`, e o de campo obrigatório não tem. **Método:** `nome(parametro: Tipo): Retorno`, e `void` quando não há retorno.
- **Tipos neutros** (decisão B1 dos critérios de aceite): `String`, `Integer`, `Real`, `Boolean`, `Date`, `DateTime` (data, hora e fuso, sempre em tempo universal coordenado (UTC)), `UUID` (identificador universal único, um tipo de dado do pacote `contrato`) e `List<T>`. Cada serviço traduz os tipos para a sua linguagem (ADR-0018 e ADR-0020).
- **Nomes** (ADR-0016, ponto 8): classes em PascalCase e no singular, métodos e atributos em camelCase, em português e sem acento. O atributo tem o nome do campo do item 12 em camelCase (`tobt_vigente` → `tobtVigente`). Os valores das enumerações são os valores exatos do domínio, com acento, porque são os que as telas mostram e os avisos levam; no código, cada serviço os escreve na convenção da sua linguagem.
- **Relacionamentos:** associação (seta aberta) quando um atributo tem o tipo de outra classe; composição (losango cheio) quando a parte só existe dentro do todo, como a tarefa dentro do plano; agregação (losango vazio) quando a parte existe sem o todo, como o operador na equipe; dependência (seta tracejada) quando a classe só usa a outra como parâmetro, retorno ou chamada; herança (triângulo) nos consumidores de avisos. As associações têm a multiplicidade nas duas pontas.
- **Gravação.** O todo de uma composição grava as partes: na Execução em Solo, `TurnaroundRepository.salvar` grava o turnaround com as tarefas, os marcos, as correções do horário real de chegada à posição (AIBT), os registros, as leituras e o histórico. Os repositórios das partes só consultam (por exemplo, a busca pela chave de envio). Toda ação que muda o turnaround ou uma tarefa começa por `buscarComTrava`, que trava a linha do turnaround até o fim da transação (ADR-0018), e confere se o turnaround ainda aceita registros (RF-44).
- **Referência entre classes e entre serviços.** Dentro do serviço, a classe guarda o objeto (`- turnaround: TurnaroundReferencia`), e não o identificador. Entre serviços, guarda só o identificador (`- tarefaId: UUID`), porque cada serviço tem o seu código e o seu banco, e só o dono decide sobre o dado (ADR-0015, regra 1). Nenhuma classe de um serviço tem atributo, parâmetro ou retorno do tipo de uma classe de outro serviço; o que vai de um serviço para outro é um dado de troca do próprio serviço.

## 13.3 Visão geral das classes de negócio

A visão geral mostra as classes de negócio de cada serviço e as associações entre elas, sem os membros. Os membros estão nas vistas da seção 13.4.

![Diagrama de classes — visão geral das classes de negócio](diagramas/13-classes-visao-geral.png)

## 13.4 Classes de negócio por serviço

Cada vista mostra as classes de negócio do serviço, com atributos e métodos, e as enumerações que ele usa. Os tipos do pacote `contrato` (`UUID`, `EstadoTurnaround`, `EstadoTarefa`, `Perfil`, `TipoAcaoAlerta`) estão na seção 13.6.

### 13.4.1 Cadastro e Planejamento

![Diagrama de classes — Cadastro e Planejamento](diagramas/13-classes-negocio-cadastro.png)

### 13.4.2 Execução em Solo

![Diagrama de classes — Execução em Solo](diagramas/13-classes-negocio-execucao.png)

### 13.4.3 Monitoramento

![Diagrama de classes — Monitoramento](diagramas/13-classes-negocio-monitoramento.png)

### 13.4.4 Exceções e Liberação

![Diagrama de classes — Exceções e Liberação](diagramas/13-classes-negocio-excecoes.png)

### 13.4.5 Diferenças em relação ao modelo de dados

Toda tabela de negócio do item 12 tem classe com o mesmo nome em PascalCase, e todo campo tem atributo com o mesmo nome em camelCase e tipo compatível (`CHAR(36)` → `UUID`, `VARCHAR` → `String` ou enumeração, `INTEGER` → `Integer`, `BOOLEAN` → `Boolean`, `DATE` → `Date`, `TIMESTAMP WITH TIME ZONE` → `DateTime`). As diferenças são intencionais:

- **Chave estrangeira dentro do serviço vira objeto.** `plano.turnaround_id` vira `- turnaround: Turnaround`. Quando a tabela é parte de um todo, a chave vira a lista no todo, com composição: `tarefa_plano.plano_id` é a lista `Plano.tarefas`.
- **Tabelas associativas de dependência viram lista.** `dependencia_tarefa_modelo`, `dependencia_tarefa_plano`, `dependencia_tarefa` e `dependencia_monitorada` são a lista `predecessoras` da própria classe da tarefa. As associativas com atributos próprios continuam classes: `ProjecaoTarefa`, `CaminhoCriticoTarefa` e `AlertaTarefa`.
- **Chave composta vira um atributo.** O par `codigo_versao` e `codigo_atraso` do registro da pausa e da exceção é o atributo `codigoAtraso: CodigoAtraso`.
- **Domínios fechados viram enumeração** (`TipoMarco`, `TipoRegistro`, `TipoAlerta`, `CausaRecalculo`, `TipoReplanejamento` e as demais), com os valores do Apêndice B.
- **Mesmo nome em dois serviços.** `Turnaround`, `TabelaCodigoAtraso` e `CodigoAtraso` existem no Cadastro e na Execução em Solo, ou na Execução em Solo e no Exceções e Liberação, como no item 12. São classes diferentes, cada uma no pacote do seu serviço.
- **Classes sem tabela.** Os dados de troca («dto») e as enumerações não têm tabela; as tabelas técnicas do item 12 (seção 12.6) estão no pacote `comum` e, a de pedidos pendentes, no Exceções e Liberação (seção 13.6).

## 13.5 Vistas técnicas por função do sistema

Cada vista mostra, para uma função do sistema, as telas, os controles, os serviços, os repositórios e a comunicação com outros serviços. As classes de negócio aparecem só com o nome; os membros estão na seção 13.4. Uma função pode atravessar dois serviços, como o Motor de Eventos e a liberação.

### 13.5.1 Autenticação, usuários e equipes

UC01, UC02 e UC09.

![Diagrama de classes — autenticação, usuários e equipes](diagramas/13-classes-tecnica-acesso.png)

### 13.5.2 Abertura e planejamento do turnaround

UC03 a UC08, UC10 e UC11.

![Diagrama de classes — abertura e planejamento do turnaround](diagramas/13-classes-tecnica-planejamento.png)

### 13.5.3 Execução das tarefas no solo

UC12 a UC19 e UC37. A `FilaRegistrosSemConexao` guarda no celular o registro e a leitura de código de resposta rápida (QR Code) feitos sem conexão, com o operador, o horário da ação e a chave de envio, e os envia na ordem quando a conexão volta e o mesmo operador está autenticado (RNF-8). O serviço confere, a cada registro, que a tarefa é do operador e da equipe dele (`TarefaService.conferirResponsavel`).

![Diagrama de classes — execução das tarefas no solo](diagramas/13-classes-tecnica-execucao.png)

### 13.5.4 Motor de Eventos: marcos, propagação, recálculo e alertas

UC20, UC21, UC24, UC25 e o aviso de checagem do UC27.

![Diagrama de classes — Motor de Eventos](diagramas/13-classes-tecnica-motor-de-eventos.png)

### 13.5.5 Painel, linha do tempo, alertas, checagem e indicadores

UC22, UC23, UC26, UC27 e UC28. Os painéis (UC22 e UC23) são lidos por GraphQL, como decidido na ADR-0016 ("GraphQL só nos painéis").

![Diagrama de classes — acompanhamento](diagramas/13-classes-tecnica-acompanhamento.png)

### 13.5.6 Exceções, atualização do TOBT e ação sobre o alerta

UC29, UC31, UC33 e UC34. A abertura e o encerramento da exceção são pedidos à Execução em Solo, gravados antes como pedido pendente (ADR-0020); a Execução em Solo responde com a mudança de estado (`MudancaEstado`). A ação sobre um alerta (UC31) não é uma chamada à parte: a tela de registro abre a tela da ação com o alerta, e abrir a exceção, reatribuir, replanejar ou atualizar o TOBT recebem o `alertaId` e gravam a `AcaoAlerta` na mesma transação, depois de conferir que o alerta ainda não tem ação. A atualização do TOBT é recusada quando a solicitação já foi encerrada ou o turnaround já foi liberado.

![Diagrama de classes — exceções, TOBT e ação sobre o alerta](diagramas/13-classes-tecnica-excecoes.png)

### 13.5.7 Reatribuição e replanejamento

UC30, UC35 e UC36. A decisão é da Execução em Solo, que é a dona da tarefa; o Exceções e Liberação guarda o motivo e o autor. Todo pedido leva o horário da ação e a chave do registro (`reatribuicaoId`, `replanejamentoId`), que a Execução em Solo grava como causa na auditoria; depois de uma queda, `consultarPedido` diz se o pedido já foi aplicado, e o pedido pendente é concluído ou desfeito (ADR-0020). A lista de operadores vem com o nome, buscado no Cadastro na hora, e já ordenada (RF-43).

![Diagrama de classes — reatribuição e replanejamento](diagramas/13-classes-tecnica-reatribuicao-replanejamento.png)

### 13.5.8 Liberação e saída da posição

UC32 e UC37. O Exceções e Liberação confere as exceções e pede a liberação; a Execução em Solo confere o estado e as tarefas, grava "Liberado" e responde, e só então o horário real de prontidão (ARDT) é gravado (ADR-0015, regra 6).

![Diagrama de classes — liberação e saída da posição](diagramas/13-classes-tecnica-liberacao.png)

## 13.6 Contrato entre os serviços e infraestrutura comum

O pacote `contrato` tem o que os quatro serviços combinaram (ADR-0016): o identificador `UUID`, as enumerações de estado e de perfil, o tipo da ação sobre o alerta, o `Acesso` que a porta de entrada passa a cada ação e o `EnvelopeAviso`. O pacote `comum` mostra uma vez a infraestrutura que cada serviço tem no seu código: a trilha de auditoria (RNF-2), a tabela de avisos a publicar, a de avisos processados, o publicador e o consumidor de avisos. Cada serviço tem o seu consumidor, que herda de `ConsumidorAvisos`, e a sua `RotinaAnonimizacao`, que anonimiza a trilha vencida (RNF-6). O Exceções e Liberação tem também o `PedidoPendente`, que guarda o pedido à Execução em Solo antes da chamada e é retomado depois de uma queda (ADR-0020; RNF-20).

![Diagrama de classes — contrato e infraestrutura comum](diagramas/13-classes-contrato.png)

## 13.7 Conferência

`python scripts/conferir_classes.py` confere as fontes das classes contra os critérios do item: formato dos atributos e dos métodos, tipos, nenhuma classe de outro serviço, associação desenhada para todo atributo que aponta para outra classe de negócio, toda tabela de negócio do Apêndice B com classe e atributos, `[0..1]` só nos campos opcionais, os valores das enumerações contra o `CONTEXT.md` e os domínios do Apêndice B, e o contrato entre os serviços (todo método de cliente igual ao do controle que atende o pedido e o mesmo «dto» com os mesmos campos dos dois lados). Com `--sequencia`, confere também que todo método chamado nos diagramas de sequência do item 14 existe na classe que recebe a mensagem (C13.8); os métodos que o item 14 pedir entram aqui.
