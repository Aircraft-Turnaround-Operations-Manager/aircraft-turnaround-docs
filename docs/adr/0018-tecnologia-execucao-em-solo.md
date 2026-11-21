---
id: adr-0018
titulo: "ADR-0018 — Tecnologia do serviço Execução em Solo: Java, Spring Boot e PostgreSQL"
tipo: decisao
decisao: D18
status: aceita
data: 2026-11-09
decisor: João Pedro Cardoso de Liz
itens_template: [12, 14]
areas: [B]
fontes: []
relacionados: [adr-0015, adr-0016, adr-0020, adr-0023, adr-0007, adr-0013]
---
# ADR-0018 — Tecnologia do serviço Execução em Solo: Java, Spring Boot e PostgreSQL

- **Status:** aceita · **Data:** 09/11/2026 · **Decisor:** João Pedro Cardoso de Liz (responsável pelo serviço)

## Contexto

- A [ADR-0015](0015-divisao-em-microsservicos.md) dividiu o sistema em quatro microsserviços e deixou a cada integrante a escolha da linguagem, do framework e do banco do seu serviço. A [ADR-0016](0016-contrato-entre-os-servicos.md) fixou o contrato que todos seguem. Esta ADR registra a escolha da **Execução em Solo** (decisão B2 de `entregas/ra2-criterios-de-aceite.md`, seção 6).
- A Execução em Solo cuida dos RF-12 a RF-21 e do RF-44. Ela é o único serviço que grava o estado do turnaround e das tarefas, os marcos e os horários reais de chegada à posição (AIBT), de início do atendimento em solo (ACGT), de início do embarque (ASBT), de fim do atendimento em solo (AEGT) e de saída da posição (AOBT). Ela atende um pedido de cada vez por turnaround e responde aos pedidos dos outros serviços: exceção (RF-36 e RF-40), reatribuição (RF-37), liberação (RF-39) e replanejamento (RF-42) (ADR-0015, regras 3, 4 e 6).
- Os requisitos não funcionais que mais pesam na escolha são:
  - **RNF-7:** as funções do Operador de Solo/Rampa ficam disponíveis em 99,5% do mês.
  - **RNF-8:** os registros feitos sem conexão chegam na ordem, com o horário do celular e sem duplicação.
  - **RNF-11:** a mudança aparece na lista de tarefas do operador (RF-14) em até 5 s, sem recarregar a página.
  - **RNF-20:** depois de uma falha, nenhum registro confirmado se perde.
  - **RNF-23:** cada transição de estado do turnaround tem teste automatizado.
  - **RNF-24:** toda mudança de estado gera log estruturado.
- Os itens 12 a 15 não dependem desta escolha: o item 12 usa tipos SQL padrão e o item 13 usa tipos UML neutros (decisão B1). Esta ADR vale para o desenvolvimento.

## Opções consideradas

1. **Java + Spring Boot + PostgreSQL.** Mesmo ecossistema da porta de entrada (Spring Cloud Gateway, ADR-0016, ponto 2). As camadas de referência da ADR-0015 (`Controller → Service → Repository`) são as do próprio Spring. Tem biblioteca oficial para RabbitMQ (Spring AMQP), gera a descrição OpenAPI a partir do código e grava os campos em snake_case sem configuração. Contra: consome mais memória e demora mais para subir que as outras opções.
2. **TypeScript + NestJS + PostgreSQL.** Mesma linguagem do site em Angular, e o NestJS tem módulos e injeção de dependência parecidos com os do Angular. Também tem suporte a RabbitMQ e a OpenAPI. Contra: a trava por turnaround e a gravação do aviso na mesma transação dependem mais de código próprio, e a conversão de camelCase para snake_case no banco exige configuração em cada entidade ou um plugin.
3. **C# + ASP.NET Core + PostgreSQL.** Atende o contrato todo, com bom suporte a REST, OpenAPI e RabbitMQ. Contra: não compartilha linguagem nem com a porta de entrada nem com o site, então ninguém do grupo reaproveita o que já sabe.

O banco é o mesmo nas três opções. Um banco relacional com transação é o que garante as regras da ADR-0015 (só o dono do dado decide, um pedido de cada vez por turnaround) e o RNF-20. Um banco de documentos foi descartado porque a liberação confere várias tarefas e o estado do turnaround numa só decisão.

## Decisão

**Opção 1.**

| Parte | Escolha | Motivo |
|---|---|---|
| Linguagem | **Java 21** (versão de suporte longo) | Mesma linguagem e mesma versão da porta de entrada e do Cadastro e Planejamento (ADR-0017), com o mesmo ambiente e as mesmas imagens de contêiner. Tipos próprios para horário em UTC (`Instant`) e para UUID (`java.util.UUID`). Versão com suporte longo, que não sai de linha durante o projeto, e aceita pelo Spring Boot 4, que pede Java 17 ou mais novo. |
| Framework | **Spring Boot 4** | Já traz as três camadas da ADR-0015 (`@RestController`, `@Service`, `@Repository`) e os módulos de que o serviço precisa: Spring Web (REST), Spring Data JPA (banco), Spring AMQP (RabbitMQ), Spring WebSocket (lista do operador), Spring Security (perfil) e Spring Boot Actuator (verificação de disponibilidade). A descrição OpenAPI sai do código com o springdoc-openapi. |
| Banco | **PostgreSQL 18** | Transação completa e trava de linha (`SELECT ... FOR UPDATE`) para atender um pedido de cada vez por turnaround. Tipos nativos `uuid` e `timestamp with time zone`, o mesmo tipo de horário do item 12. Gravação confirmada em disco antes da resposta, o que atende o RNF-20. |

Bibliotecas de apoio: Flyway para criar e versionar as tabelas por scripts SQL; JUnit 5 com Testcontainers para os testes automatizados, com PostgreSQL e RabbitMQ reais em Docker (RNF-23). No desenvolvimento, o banco e a mensageria rodam em Docker na máquina do integrante (ADR-0016, ponto 4).

### Como o serviço cumpre o contrato da ADR-0016

| Ponto da ADR-0016 | Como a Execução em Solo cumpre |
|---|---|
| **2. Porta de entrada** | O serviço só recebe as ações do site pela porta de entrada. O Spring Security confere o token interno assinado que a porta de entrada envia ([ADR-0023](0023-interfaces-da-porta-de-entrada-e-do-cadastro.md), ponto 1: assinatura com a chave pública da porta de entrada e validade), lê dele o usuário, o perfil e a equipe e confere se o perfil pode fazer a ação (RNF-1). Por exemplo, só o Operador de Solo/Rampa com a tarefa atribuída registra o início, e só o Coordenador de Turnaround corrige o AIBT (RF-13). O token também diz se a chamada é ação do usuário (ADR-0023, ponto 2): as consultas automáticas da lista de tarefas não renovam a sessão (RNF-5). |
| **3. REST entre serviços** | Os pedidos com resposta (confirmação do plano, exceção, reatribuição, liberação, replanejamento e lista de operadores disponíveis do RF-43) chegam em REST com JSON sobre HTTPS (RNF-3), em endereços versionados, como `/v1/turnarounds/{id}/tarefas`. Uma recusa de regra de negócio volta com o motivo no corpo da resposta, no formato de erro padrão do Spring (Problem Details). A descrição OpenAPI é gerada a partir do código. Para cumprir os 5 s do RNF-11, a lista de tarefas do operador (RF-14) recebe as mudanças por WebSocket. A ADR-0016 cita o WebSocket só no painel; esta ADR estende o mesmo meio à lista do operador, que tem o mesmo prazo de 5 s. O serviço não oferece GraphQL; se os itens 13 e 14 pedirem, o Spring for GraphQL atende sem trocar de framework. |
| **4 e 5. RabbitMQ e envelope dos avisos** | O serviço tem uma fila durável própria, `execucao-em-solo`, e publica e consome pelo Spring AMQP, com mensagens persistentes. Todo aviso usa uma única classe de envelope, com os campos `id`, `tipo`, `versao`, `ocorridoEm`, `turnaroundId`, `autorId`, `origem` (sempre `execucao-em-solo`), `causaId` e `dados`, como `ChegadaRegistrada` ou `TarefaConcluida`. O aviso é gravado numa tabela de saída na mesma transação da mudança e publicado logo depois da gravação; assim, não há mudança gravada sem aviso nem aviso de mudança que não aconteceu (RNF-20). Ao consumir, o serviço grava o `id` do aviso numa tabela de avisos processados, com chave única, na mesma transação das mudanças que o aviso causa (por exemplo, a cópia do horário-alvo de prontidão (TOBT) vigente), e ignora o repetido. A mensagem só é confirmada à fila depois de gravada. Os marcos (RF-20) e a propagação do estado (RF-21) não passam pela fila: o Motor de Eventos roda na mesma transação do registro do operador que o aciona, e o aviso só leva o resultado aos outros serviços (item 13, seção 13.5.4). |
| **6. Horários em UTC** | Os horários são `Instant` no código e `timestamp with time zone` no banco, com a conexão do banco em UTC. O JSON sai no formato ISO 8601 terminado em `Z`. O registro feito sem conexão chega com o horário do celular, já convertido para UTC, e o serviço grava esse horário como horário da ação, e não o do envio (RNF-8). |
| **7. UUID** | Cada marco, registro, histórico ou aviso que o serviço cria recebe um UUID versão 4 gerado pelo próprio serviço (`UUID.randomUUID()`), no tipo `uuid` do banco. A tarefa e o ponto de QR Code nascem no plano do Cadastro e Planejamento (RF-6; ADR-0015, regra 5) e guardam o UUID do plano, sem alterá-lo (ADR-0016, ponto 7), como no item 12. Identificadores de outros serviços, como usuário, equipe e plano, ficam guardados como vieram, sem chave estrangeira (ADR-0015, consequências). O plano chega com a chave de idempotência do Cadastro (ADR-0023, ponto 5): o serviço guarda a chave do último plano aplicado e, se o mesmo pedido chegar de novo, responde o mesmo resultado, sem tratá-lo como nova confirmação. Para o RNF-8 ("sem duplicação"), o celular manda junto de cada registro uma chave de envio (`requisicaoId`), inclusive no registro feito sem conexão; o serviço grava a chave junto do registro, com valor único, e, se o mesmo registro chegar de novo, devolve a resposta da primeira vez. A chave serve só para o reenvio: o identificador do registro continua sendo gerado pelo serviço. |
| **8. Nomes em português** | Classes em PascalCase no singular (`Tarefa`, `TarefaController`, `TarefaService`, `TarefaRepository`), métodos e atributos em camelCase (`registrarInicio()`, `turnaroundId`), sem acento. O Spring Boot converte os nomes dos atributos para snake_case no banco sem configuração (`turnaroundId` vira `turnaround_id`), e as tabelas ficam no singular (`tarefa`, `turnaround`). O JSON sai em camelCase, o padrão da biblioteca de JSON do Spring. Endereços em minúsculas e no plural; avisos em PascalCase, no passado. |

### Um pedido de cada vez por turnaround (ADR-0015, regra 4)

Toda ação que muda o turnaround ou uma tarefa roda numa transação que trava antes a linha do turnaround (`@Lock(PESSIMISTIC_WRITE)` no Spring Data JPA, que vira `SELECT ... FOR UPDATE` no PostgreSQL). Dois pedidos do mesmo turnaround esperam um pelo outro; turnarounds diferentes andam em paralelo. Isso vale mesmo com mais de uma cópia do serviço no ar, porque a trava fica no banco. Na liberação, a Execução em Solo confere o estado e as tarefas dentro dessa transação, e nenhum registro de tarefa entra no meio da conferência (ADR-0015, regra 6).

### Disponibilidade, logs e testes

- **RNF-7 e RNF-19:** o Spring Boot Actuator expõe a verificação de saúde (`/actuator/health`), que confere o banco e a mensageria e serve para a medição automática a cada minuto. O serviço roda em contêiner com reinício automático.
- **RNF-2 e RNF-24:** a trilha de auditoria é gravada na mesma transação da mudança. O log sai em JSON, com o log estruturado do próprio Spring Boot, e traz o identificador do turnaround, o estado anterior e o novo, o autor, o horário e o `causaId`.
- **RNF-23:** cada transição de estado do turnaround e a recusa de registro depois de "Fora de bloco" (RF-44) têm teste com JUnit 5 e Testcontainers, executado a cada integração na `main`.
- **Testes do site:** a estrutura inicial do site é montada pelo responsável por esta área (ADR-0016, ponto 1), e as ferramentas de teste valem para as telas das quatro áreas. O site usa o Vitest, padrão do Angular, nos testes de unidade e de componente e o Playwright nos de ponta a ponta, com a cobertura numa página HTML (provedor v8 do Vitest), como propõe a [ADR-0020](0020-tecnologia-excecoes-e-liberacao.md), seção "Testes" ([#179](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/issues/179)).

## Consequências

- Os itens 12 a 15 continuam com tipos SQL padrão e tipos UML neutros (decisão B1). No desenvolvimento, `TIMESTAMP WITH TIME ZONE` vira `Instant`, os identificadores viram `UUID` e as camadas `Controller → Service → Repository` do item 13 viram as classes do Spring com o mesmo nome.
- Nos diagramas de sequência da área B (item 14), os participantes do serviço são as camadas de referência e o banco da Execução em Solo. Não é preciso citar Spring ou PostgreSQL nos diagramas.
- A Execução em Solo passa a ter duas tabelas técnicas, além das tabelas de negócio: a de avisos a publicar e a de avisos processados. Elas não guardam dado de negócio, mas os diagramas de sequência (item 14) gravam nelas; por isso entram no modelo do item 12 como tabelas técnicas do serviço. A chave de envio do celular não tem tabela própria: é uma coluna das tabelas de registro.
- A trava por turnaround faz um pedido esperar o outro. Com até 30 tarefas por turnaround e 5 registros por segundo no sistema todo (RNF-13), a espera fica curta. [Inferência] Ainda assim, o teste de carga do RNF-13 precisa confirmar os 5 s do RNF-11.
- Java com Spring Boot usa mais memória e demora mais para subir do que um serviço em Node.js. No desenvolvimento, isso pesa só na máquina do integrante. Em produção, a verificação de saúde só libera o serviço depois que ele está pronto.
- A primeira versão desta ADR escolhia o Java 25. A troca para o Java 21 alinha os três serviços em Java (porta de entrada, Cadastro e Planejamento e Execução em Solo), a pedido do responsável pela porta de entrada ([#178](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/issues/178)). Nada do serviço depende de recurso que só existe no Java 25, e o contrato da ADR-0016 não depende da versão.
- A primeira versão desta ADR dava os marcos e a propagação como exemplo de mudança causada por um aviso consumido. O diagrama de classes (item 13, [#208](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/208)) os faz na mesma transação do registro, sem passar pela fila: assim o marco e o novo estado são gravados junto com o registro que os causa, sem esperar a fila e sem corrida entre dois avisos do mesmo turnaround. O texto do ponto 4 e 5 acompanha.
- A escolha pode ser revista durante a implementação. Nesse caso, uma ADR nova substitui esta.

---

## Ligações

- **Divisão em microsserviços:** [ADR-0015](0015-divisao-em-microsservicos.md)
- **Contrato entre os serviços:** [ADR-0016](0016-contrato-entre-os-servicos.md); identidade passada pela porta de entrada na [ADR-0023](0023-interfaces-da-porta-de-entrada-e-do-cadastro.md)
- **Ferramentas de teste do site:** [ADR-0020](0020-tecnologia-excecoes-e-liberacao.md), seção "Testes"
- **Dados do operador e QR Code:** [ADR-0007](0007-dados-do-operador-e-qr-code.md)
- **Chegada registrada pelo operador:** [ADR-0013](0013-chegada-registrada-pelo-operador.md)
- **Requisitos da área B:** [RFs](../../especificacao/06-requisitos-funcionais/area-b.md), [RNFs](../../especificacao/08-requisitos-nao-funcionais/area-b.md)
- **Critérios do RA2:** [entregas/ra2-criterios-de-aceite.md](../../entregas/ra2-criterios-de-aceite.md)
- **Contexto geral:** [CONTEXT.md](../../CONTEXT.md)
