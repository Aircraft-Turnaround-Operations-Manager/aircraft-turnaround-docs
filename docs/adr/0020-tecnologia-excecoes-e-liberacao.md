---
id: adr-0020
titulo: "ADR-0020 — Tecnologia do serviço Exceções e Liberação: C#, ASP.NET Core e PostgreSQL"
tipo: decisao
decisao: D20
status: aceita
data: 2026-11-13
decisor: Rodrigo Alves
itens_template: [12, 14]
areas: [D]
fontes: []
relacionados: [adr-0015, adr-0016, adr-0003, adr-0004, adr-0006]
---
# ADR-0020 — Tecnologia do serviço Exceções e Liberação: C#, ASP.NET Core e PostgreSQL

- **Status:** aceita · **Data:** 13/11/2026 · **Decisor:** Rodrigo Alves (responsável pelo serviço)

## Contexto

- A [ADR-0015](0015-divisao-em-microsservicos.md) dividiu o sistema em quatro microsserviços e deixou a cada integrante a escolha da linguagem, do framework e do banco do seu serviço. A [ADR-0016](0016-contrato-entre-os-servicos.md) fixou o contrato que todos seguem. Esta ADR registra a escolha do **Exceções e Liberação** (decisão B2 de `entregas/ra2-criterios-de-aceite.md`; tarefa T04-D, [issue #161](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/issues/161)).
- O serviço cuida dos RF-36 a RF-43. Ele é o dono das exceções, das ações sobre os alertas, dos motivos de reatribuição e de replanejamento, do horário-alvo de prontidão (TOBT) vigente e do horário real de prontidão (ARDT) (ADR-0015). Quase todas as suas ações dependem de um dado que é da Execução em Solo, dona da tarefa e do estado do turnaround. Por isso o serviço faz **pedidos com resposta** à Execução em Solo na abertura e no encerramento da exceção, na reatribuição, no replanejamento, na liberação e na consulta dos operadores disponíveis (ADR-0015, regras 3 e 6). Ele também consome os avisos do Monitoramento, que disparam o pedido de atualização do TOBT (RF-41).
- O que o serviço grava é um conjunto de registros pequenos, ligados entre si e com regras de integridade: a exceção com o código de atraso da Agência Nacional de Aviação Civil (ANAC) e a versão da tabela (RNF-22; ADR-0006), a ação sobre o alerta ligada à exceção, à reatribuição, ao replanejamento ou à atualização do TOBT (RF-38), a liberação única por turnaround (RF-39) e o valor anterior e o novo do TOBT (RF-41). Cada registro guarda o autor e o horário (RNF-2).
- Os requisitos não funcionais que mais pesam na escolha são:
  - **RNF-19:** as funções dos RF-36 a RF-43 ficam disponíveis em 99,5% do mês.
  - **RNF-20:** depois de uma falha, nenhum registro confirmado se perde, inclusive aberturas e encerramentos de exceção, reatribuições, ações sobre alertas, atualizações do TOBT e liberações.
  - **RNF-21:** o limiar de 5 minutos da atualização do TOBT e o prazo de 2 minutos da ação sobre alerta crítico são parâmetros, e não valores fixos no código.
  - **RNF-22:** a tabela de códigos de atraso é dado versionado, carregado de arquivo.
  - **RNF-23:** as regras do RF-39 e do RF-40 têm teste automatizado a cada integração na `main`.
  - **RNF-24:** toda exceção e toda ação sobre alerta geram log estruturado.
- Os itens 12 a 15 não dependem desta escolha: o item 12 usa tipos SQL padrão e o item 13 usa tipos UML neutros (decisão B1). Esta ADR vale para o desenvolvimento.

## Opções consideradas

1. **Java + Spring Boot + PostgreSQL.** Mesmo ecossistema da porta de entrada (Spring Cloud Gateway), do Cadastro e Planejamento ([ADR-0017](0017-tecnologia-cadastro-e-planejamento.md)) e da Execução em Solo ([ADR-0018](0018-tecnologia-execucao-em-solo.md)). Atende todo o contrato. Contra: o responsável pelo serviço trabalha há três períodos com C# e prefere a plataforma .NET.
2. **C# + ASP.NET Core + PostgreSQL.** Atende todo o contrato com recursos do próprio framework: REST, descrição OpenAPI gerada do código, erro no formato Problem Details, verificação de saúde, log em JSON e injeção de dependência. Tem biblioteca oficial do RabbitMQ e acesso ao PostgreSQL com o Entity Framework Core. Contra: nenhum outro serviço do grupo usa C#, então o responsável não divide com os colegas a configuração do framework.
3. **TypeScript + NestJS + PostgreSQL.** Mesma linguagem do site em Angular. Contra: o ganho é pequeno num serviço sem tela própria, e é um ecossistema diferente do da Execução em Solo, com quem o serviço mais conversa.
4. **Python + FastAPI + PostgreSQL.** Mesma linguagem do Monitoramento ([ADR-0019](0019-tecnologia-monitoramento.md)), que gera os alertas que o serviço trata. Contra: tipagem mais fraca nos contratos dos pedidos à Execução em Solo, que são a maior parte do serviço.

O banco é o mesmo nas quatro opções. Os dados do serviço são registros pequenos, com dono, autor e ligação entre si, e as gravações precisam ser atômicas: a exceção junto com a auditoria e com o aviso a publicar; o ARDT junto com a decisão. Um banco relacional faz isso com transação, chave estrangeira e restrição de unicidade, e segue o modelo lógico relacional do item 12. Um banco de documentos, como o MongoDB do Monitoramento, também teria transação, mas compensa quando o dado é um documento único regravado de uma vez, o que não é o caso aqui.

**Mesmo banco que outros serviços não é banco compartilhado.** O princípio do microsserviço é que cada serviço tem o seu banco e nenhum serviço acessa o banco de outro (ADR-0015; critérios C12.4 e C14.3). Usar o mesmo produto do Cadastro e da Execução em Solo não junta os dados: o Exceções e Liberação tem o seu próprio banco, num contêiner próprio, com um usuário que não tem acesso a nenhum outro banco, e as suas migrações ficam no código do próprio serviço. Variar o produto do banco só se justifica quando o dado pede, como no Monitoramento.

## Decisão

**Opção 2.**

| Parte | Escolha | Motivo |
|---|---|---|
| Linguagem | **C# 14**, na plataforma **.NET 10** (versão de suporte longo, até novembro de 2028) | É a linguagem que o responsável pelo serviço usa há três períodos, dois deles na faculdade, e com a qual está habituado. Na avaliação dele, é a linguagem orientada a objeto mais madura hoje, mesmo com a evolução recente do Java. Tipagem forte nos contratos dos pedidos à Execução em Solo e no envelope dos avisos, com `record` para os dados de entrada e saída. UUID na biblioteca padrão (`Guid.NewGuid()`, versão 4) e horário em UTC no próprio tipo (`DateTime` com `Kind = Utc`). Versão com suporte longo, que não sai de linha durante o projeto. |
| Framework | **ASP.NET Core 10** | Separa as camadas da ADR-0015 em controladores (`Controller`), serviços (`Service`) e repositórios (`Repository`), registrados na injeção de dependência do próprio framework. Traz de fábrica o que o contrato pede: REST com JSON, descrição OpenAPI gerada do código (`Microsoft.AspNetCore.OpenApi`), recusa no formato Problem Details, verificação de saúde e log em JSON. O cliente HTTP para os pedidos à Execução em Solo vem do próprio .NET (`IHttpClientFactory`), com prazo de resposta configurado. |
| Banco | **PostgreSQL 18** | Transação completa, chave estrangeira dentro do serviço, restrição de unicidade (uma liberação por turnaround) e trava de linha (`SELECT ... FOR UPDATE`) quando duas pessoas mexem na mesma exceção ou no mesmo TOBT. Tipos nativos `uuid` e `timestamp with time zone`, o mesmo tipo de horário do item 12. Gravação confirmada em disco antes da resposta, o que atende o RNF-20. Mesma versão da Execução em Solo. |

Bibliotecas de apoio: Entity Framework Core 10 com o provedor Npgsql, para o acesso ao banco e para as migrações versionadas (`dotnet ef migrations`); EFCore.NamingConventions, para gravar tabelas e campos em snake_case; RabbitMQ.Client, a biblioteca oficial do RabbitMQ; e as ferramentas de teste e de cobertura da seção "Testes", abaixo. No desenvolvimento, o banco e a mensageria rodam em Docker na máquina do integrante (ADR-0016, ponto 4).

### Como o serviço cumpre o contrato da ADR-0016

| Ponto da ADR-0016 | Como o Exceções e Liberação cumpre |
|---|---|
| **2. Porta de entrada** | O serviço só recebe as ações do site pela porta de entrada. Ele lê o usuário e o perfil que a porta de entrada informa e confere, com as políticas de autorização do ASP.NET Core, se o perfil pode fazer a ação (RNF-1). Por exemplo, só a Autoridade de Liberação confirma a prontidão, e só da companhia que ela representa (RF-39; ADR-0004); só o Coordenador de Turnaround abre e encerra exceção, reatribui, replaneja e registra a ação sobre o alerta. O formato em que a porta de entrada passa o usuário e o perfil (cabeçalho, token ou outro) ainda não está definido; ele é combinado com o responsável pela porta de entrada (ADR-0016, ponto 2), e esta ADR não o supõe. |
| **3. REST entre serviços** | As ações do site chegam em REST com JSON sobre HTTPS (RNF-3), em endereços versionados, minúsculos e no plural, como `/v1/excecoes` e `/v1/liberacoes/{turnaroundId}`. Os pedidos à Execução em Solo também saem em REST. Uma recusa de regra de negócio volta com o motivo no formato Problem Details, por exemplo a lista de tarefas obrigatórias pendentes que impede a liberação. Em falha técnica da Execução em Solo, o serviço não repete sozinho um pedido que muda dado: informa ao usuário que a ação não foi concluída, como manda o ponto 3. A descrição OpenAPI é gerada do código. O serviço não oferece GraphQL nem WebSocket, porque não tem painel; se os itens 13 e 14 pedirem, o ASP.NET Core tem WebSocket nativo. |
| **4 e 5. RabbitMQ e envelope dos avisos** | O serviço tem uma fila durável própria, `excecoes-e-liberacao`, e publica e consome pelo RabbitMQ.Client, com mensagens persistentes e confirmação de publicação. Todo aviso usa um único `record` de envelope, com os campos `id`, `tipo`, `versao`, `ocorridoEm`, `turnaroundId`, `autorId`, `origem` (sempre `excecoes-e-liberacao`), `causaId` e `dados`. O aviso é gravado numa tabela de saída na mesma transação da mudança e publicado logo depois, por um serviço em segundo plano (`BackgroundService`); assim, não há mudança gravada sem aviso nem aviso de mudança que não aconteceu (RNF-20). Ao consumir, por exemplo o aviso do Monitoramento que dispara o RF-41, o serviço grava o `id` do aviso numa tabela de avisos processados, com chave única, na mesma transação das mudanças que ele causa, e ignora o repetido. A mensagem só é confirmada à fila depois de gravada. |
| **6. Horários em UTC** | Os horários são `DateTime` com `Kind = Utc` no código e `timestamp with time zone` no banco; o provedor Npgsql recusa gravar um horário que não esteja em UTC. O JSON sai no formato ISO 8601 terminado em `Z`. O ARDT é o horário da confirmação pela Autoridade de Liberação (RF-39), registrado pelo serviço em UTC. |
| **7. UUID** | Cada exceção, ação sobre alerta, atualização do TOBT e liberação recebe um UUID versão 4 gerado pelo próprio serviço (`Guid.NewGuid()`), no tipo `uuid` do banco. Identificadores de outros serviços, como turnaround, tarefa, usuário, equipe e alerta, ficam guardados como vieram, sem chave estrangeira (ADR-0015, consequências). |
| **8. Nomes em português** | Classes em PascalCase no singular (`Excecao`, `ExcecaoController`, `LiberacaoService`, `LiberacaoRepository`). Métodos e atributos em camelCase, como pede a ADR-0016 (`confirmarProntidao()`, `turnaroundId`), com o analisador de estilo do .NET configurado no `.editorconfig` para aceitar essa convenção no lugar do PascalCase usual do C#, como o Monitoramento fez com o Python. Tabelas e campos em snake_case e no singular (`excecao`, `turnaround_id`), pelo EFCore.NamingConventions, com o nome da tabela tirado do nome da classe. O JSON sai em camelCase, o padrão do ASP.NET Core. Endereços em minúsculas e no plural; avisos em PascalCase, no passado, como `ExcecaoAberta` e `TurnaroundLiberado`. |

### Pedidos à Execução em Solo sem perder registro (RNF-20)

Na abertura e no encerramento da exceção e na liberação, a decisão sobre o estado do turnaround é da Execução em Solo, e o registro é deste serviço (ADR-0015, regras 1 e 6). Para que uma queda entre a resposta da Execução em Solo e a gravação local não perca o registro, o serviço grava primeiro o pedido como pendente, com o autor e o horário da ação; faz o pedido; e conclui ou desfaz o registro com a resposta, na mesma transação do aviso a publicar. Se o serviço cair no meio, ao voltar ele consulta a Execução em Solo para cada pedido pendente e conclui ou desfaz o registro conforme o estado do turnaround. Na liberação, o ARDT gravado é o horário da confirmação, guardado no pedido pendente, e não o horário em que a resposta chegou.

### Parâmetros, códigos de atraso, disponibilidade e logs

- **RNF-21:** o limiar da atualização do TOBT (5 minutos) e o prazo da ação sobre alerta crítico (2 minutos) ficam na configuração do serviço, lida pelo padrão de opções do .NET com recarga, e valem para os turnarounds abertos depois da troca, sem alterar o código.
- **RNF-22:** os códigos de atraso são carregados de arquivo versionado. Cada exceção guarda o código, a descrição e a versão da tabela vigente no momento do registro, de modo que os registros antigos continuam com o código original depois de uma troca. Qual serviço é o dono da tabela e como os outros a recebem (a pausa do RF-17 também usa os códigos) é decidido no modelo de dados do item 12.
- **RNF-19:** a verificação de saúde do ASP.NET Core (`/health`) confere o banco e a mensageria e serve para a medição automática a cada minuto. O serviço roda em contêiner com reinício automático.
- **RNF-2 e RNF-24:** a auditoria é gravada na mesma transação da mudança. O log sai em JSON, com o formatador de console do próprio .NET, e traz o identificador do turnaround, o estado anterior e o novo, o autor, o horário e o `causaId`.

### Testes

O serviço segue uma pirâmide de testes completa: muitos testes de unidade, menos de integração e poucos de ponta a ponta. Todos rodam a cada pull request e a cada integração na `main`, o que faz deles também os testes de regressão: uma mudança que quebra uma regra já testada não entra (RNF-23).

| Camada | O que testa | Ferramenta |
|---|---|---|
| **Unidade (servidor)** | As regras dos RF-36 a RF-43 na camada de serviço, com os repositórios e o cliente da Execução em Solo substituídos por dublês. Por exemplo, a recusa da liberação com exceção aberta (RF-39) e a permanência em "Em exceção" quando outra exceção continua aberta (RF-40). | xUnit |
| **Integração (servidor)** | O serviço com banco e mensageria reais: gravação com auditoria, tabela de saída dos avisos, descarte do aviso repetido e retomada dos pedidos pendentes depois de uma queda (RNF-20). | xUnit com Testcontainers (PostgreSQL e RabbitMQ em Docker) |
| **API e pedidos entre serviços** | Os endereços REST de ponta a ponta dentro do serviço, com a autorização por perfil e as recusas no formato Problem Details; as respostas da Execução em Solo, inclusive recusa, demora e falha técnica, são simuladas. | `Microsoft.AspNetCore.Mvc.Testing` (servidor de teste do ASP.NET Core) e WireMock.Net |
| **Unidade e componente (site)** | As telas da área D no site em Angular: lista de liberações, abertura e encerramento de exceção, reatribuição, replanejamento e ação sobre o alerta. | Vitest, o executor de testes padrão do Angular |
| **Ponta a ponta (site e serviços)** | Os fluxos completos no navegador, com os serviços no ar: por exemplo, abrir uma exceção, encerrá-la e liberar a aeronave (UC29, UC33 e UC32). | Playwright |

**Cobertura.** No servidor, o coverlet mede a cobertura durante os testes, e o ReportGenerator gera a partir dela uma página HTML com as estatísticas por classe e por método e as linhas cobertas e não cobertas. No site, o Vitest gera a mesma página com o provedor de cobertura v8. As duas páginas são publicadas como resultado de cada execução da integração contínua.

As transições de estado do turnaround são testadas pela Execução em Solo, que as grava (ADR-0018). As ferramentas do site (Vitest e Playwright) valem para as telas da área D; como o site é um só (ADR-0016, ponto 1), elas são combinadas com o responsável pela estrutura inicial do site, para que todas as áreas usem as mesmas.

## Consequências

- Os itens 12 a 15 continuam com tipos SQL padrão e tipos UML neutros (decisão B1). No desenvolvimento, `TIMESTAMP WITH TIME ZONE` vira `DateTime` em UTC, os identificadores viram `Guid` e as camadas `Controller → Service → Repository` do item 13 viram as classes do ASP.NET Core com o mesmo nome.
- Nos diagramas de sequência da área D (item 14), os participantes do serviço são as camadas de referência e o banco do Exceções e Liberação. Não é preciso citar ASP.NET Core ou PostgreSQL nos diagramas.
- O serviço passa a ter três tabelas técnicas, além das tabelas de negócio: a de avisos a publicar, a de avisos processados e a de pedidos pendentes à Execução em Solo. Como os diagramas de sequência gravam nelas, elas entram no modelo do item 12 como tabelas técnicas do serviço.
- O sistema passa a ter três plataformas: Java (porta de entrada, Cadastro e Planejamento, Execução em Solo), Python (Monitoramento) e .NET (Exceções e Liberação). O contrato da ADR-0016 é o que os mantém compatíveis; a descrição OpenAPI de cada serviço e o envelope comum dos avisos são a referência entre eles, e não código compartilhado.
- A escolha pode ser revista durante a implementação. Nesse caso, uma ADR nova substitui esta.

---

## Ligações

- **Divisão em microsserviços:** [ADR-0015](0015-divisao-em-microsservicos.md)
- **Contrato entre os serviços:** [ADR-0016](0016-contrato-entre-os-servicos.md)
- **Tecnologia dos outros serviços:** [ADR-0017](0017-tecnologia-cadastro-e-planejamento.md), [ADR-0018](0018-tecnologia-execucao-em-solo.md), [ADR-0019](0019-tecnologia-monitoramento.md)
- **Atualização do TOBT:** [ADR-0003](0003-atualizar-previsao-na-antecipacao.md) · **Autoridade de Liberação:** [ADR-0004](0004-quatro-atores-e-autoridade-de-liberacao.md) · **Códigos de atraso:** [ADR-0006](0006-codigos-de-atraso-tabela-anac.md)
- **Requisitos da área D:** [RFs](../../especificacao/06-requisitos-funcionais/area-d.md), [RNFs](../../especificacao/08-requisitos-nao-funcionais/area-d.md)
- **Critérios do RA2:** [entregas/ra2-criterios-de-aceite.md](../../entregas/ra2-criterios-de-aceite.md)
- **Contexto geral:** [CONTEXT.md](../../CONTEXT.md)
