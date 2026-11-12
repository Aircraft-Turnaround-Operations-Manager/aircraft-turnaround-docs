---
id: adr-0019
titulo: "ADR-0019 — Tecnologia do serviço Monitoramento: Python, FastAPI e MongoDB"
tipo: decisao
decisao: D19
status: aceita
data: 2026-11-12
decisor: João Vitor Correa Oliveira
itens_template: [12, 14]
areas: [C]
fontes: []
relacionados: [adr-0015, adr-0016, adr-0001]
---
# ADR-0019 — Tecnologia do serviço Monitoramento: Python, FastAPI e MongoDB

- **Status:** aceita · **Data:** 12/11/2026 · **Decisor:** João Vitor Correa Oliveira (responsável pelo serviço)

## Contexto

- A [ADR-0015](0015-divisao-em-microsservicos.md) dividiu o sistema em quatro microsserviços e deixou a cada integrante a escolha da linguagem, do framework e do banco do seu serviço. A [ADR-0016](0016-contrato-entre-os-servicos.md) fixou o contrato que todos seguem. Esta ADR registra a escolha do **Monitoramento** (decisão B2 de `entregas/ra2-criterios-de-aceite.md`, seção 6).
- O Monitoramento cuida dos RF-22 a RF-35 e é o lado de cálculo e alerta do Motor de Eventos (ADR-0015, regra 7). Ele recalcula a projeção de prontidão, o atraso das tarefas e o caminho crítico (RF-22 a RF-24). Mostra o painel, a linha do tempo, a lista de alertas e os indicadores de aderência (RF-25, RF-26, RF-33 e RF-34). Emite os alertas: tarefa pronta não iniciada, projeção além do horário-alvo de prontidão (TOBT) + 5 min, viabilidade pelo horário estimado de chegada à posição (EIBT) somado ao tempo mínimo de turnaround (MTTT), embarque não iniciado e prontidão não registrada (RF-27 a RF-31). Também faz o aviso de checagem em TOBT − 15 e o registro dessa checagem (RF-32 e RF-35).
- Pela ADR-0015 (regra 1), os únicos dados que **só o Monitoramento grava** são as projeções, os alertas, os indicadores e as checagens. Tarefas, marcos e estado do turnaround chegam por aviso, e o serviço guarda uma cópia só para exibir e calcular, nunca para decidir. O Monitoramento não decide liberação nem estado: ele lê, calcula e avisa.
- Os requisitos não funcionais que mais pesam na escolha são:
  - **RNF-11:** a mudança aparece no painel, na linha do tempo e na lista de alertas em até 5 s, sem recarregar a página.
  - **RNF-12:** o recálculo de um turnaround com até 30 tarefas termina em até 1 s no percentil 95, e cada alerta de risco aparece em até 5 s, contados do instante-limite nos gatilhos por horário.
  - **RNF-13:** os tempos se mantêm com 40 turnarounds abertos, 10 coordenadores com o painel aberto, 200 operadores conectados e 5 registros por segundo.
  - **RNF-14:** o painel abre em até 3 s, e os indicadores de um período de até 31 dias, em até 5 s.
  - **RNF-20:** depois de uma falha, nenhum registro confirmado se perde.
  - **RNF-21:** as tolerâncias e os gatilhos (TOBT + 5, Y do RF-27, X do RF-30, TOBT − 15) são parâmetros, e não valores fixos no código.
- Os itens 12 a 15 não dependem desta escolha: o item 12 usa tipos SQL padrão e o item 13 usa tipos UML neutros (decisão B1). Esta ADR vale para o desenvolvimento.

## Opções consideradas

1. **Python + FastAPI + MongoDB.** É a linguagem e o banco que o responsável pelo serviço mais conhece. O FastAPI gera a descrição OpenAPI a partir do código e valida a entrada e a saída com o Pydantic, inclusive o envelope dos avisos. Tem WebSocket próprio e é assíncrono, o que serve para manter muitas conexões abertas do painel com pouco consumo. No MongoDB, o estado monitorado de um turnaround cabe num documento só: a cópia das tarefas, a projeção e o caminho crítico. Esse documento é lido e regravado inteiro a cada recálculo. Contra: não compartilha linguagem com a porta de entrada nem com a Execução em Solo (ADR-0018, em revisão no [PR #165](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/165)), e o grupo reaproveita menos código e revisão. O MongoDB só tem transação entre documentos com replica set. Os tipos do item 12 precisam de uma tabela de conversão (ver abaixo).
2. **Java + Spring Boot + PostgreSQL.** Mesma escolha da Execução em Solo e mesmo ecossistema da porta de entrada (Spring Cloud Gateway, ADR-0016, ponto 2). Tem Spring for GraphQL, WebSocket, tarefas agendadas e Spring AMQP. Contra: o responsável pelo serviço tem pouca prática com ele, o que atrasaria o desenvolvimento.
3. **TypeScript + NestJS + PostgreSQL.** Mesma linguagem do site em Angular, com bom suporte a GraphQL, WebSocket e agendamento. Contra: também é uma stack em que o responsável tem menos prática, e o ganho de linguagem comum com o site não compensa isso num serviço sem tela própria.

O argumento a favor do banco relacional na ADR-0018 vem de a Execução em Solo decidir a liberação conferindo várias tarefas e o estado numa só transação. Esse argumento não vale aqui, porque o Monitoramento não decide liberação nem estado (ADR-0015, regras 1 e 6). As gravações próprias do serviço são projeções, alertas e checagens. Cada uma toca um turnaround por vez e cabe em poucos documentos.

## Decisão

**Opção 1.**

| Parte | Escolha | Motivo |
|---|---|---|
| Linguagem | **Python 3.14** | Linguagem que o responsável mais conhece. Horário com fuso no próprio tipo (`datetime` com `timezone.utc`) e UUID na biblioteca padrão (`uuid.uuid4()`). Com dicas de tipo (`type hints`) conferidas pelo mypy, o código do cálculo fica legível e tipado. |
| Framework | **FastAPI**, com Pydantic 2 | Separa as camadas da ADR-0015 em rotas (`Controller`), serviços (`Service`) e repositórios (`Repository`), com injeção de dependência (`Depends`). Gera a descrição OpenAPI a partir do código (ADR-0016, ponto 3). Tem WebSocket nativo e é assíncrono. Junto vêm as bibliotecas de apoio: Strawberry GraphQL (painel), aio-pika (RabbitMQ), PyMongo com a API assíncrona (MongoDB) e Pydantic Settings (parâmetros do RNF-21). |
| Banco | **MongoDB 8.0**, em replica set | O estado monitorado de um turnaround (cópia das até 30 tarefas, projeção e caminho crítico) é um documento único, lido e regravado de uma vez no recálculo. A gravação de um documento é atômica. O painel lê um documento por turnaround, sem junções, o que ajuda no RNF-14. Os alertas dos RF-27 a RF-31 têm conteúdos diferentes (minutos de espera, desvio, EIBT e MTTT, tarefas pendentes) e ficam numa coleção só, sem colunas vazias. O pipeline de agregação calcula os indicadores do RF-34 com numerador e denominador. O replica set (um nó só no desenvolvimento) libera as transações entre documentos usadas abaixo. |

No desenvolvimento, o MongoDB (replica set de um nó) e a mensageria rodam em Docker, na máquina do integrante (ADR-0016, ponto 4). Os testes usam pytest com Testcontainers, com MongoDB e RabbitMQ reais em Docker.

### Como o serviço cumpre o contrato da ADR-0016

| Ponto da ADR-0016 | Como o Monitoramento cumpre |
|---|---|
| **2. Porta de entrada** | O serviço só recebe as ações do site pela porta de entrada. Uma dependência do FastAPI lê o usuário e o perfil que a porta de entrada informa e confere se o perfil pode fazer a ação (RNF-1). Por exemplo, só o Coordenador de Turnaround abre o painel (RF-25) e registra a checagem (RF-35). O formato em que a porta de entrada passa o usuário e o perfil ainda não está definido (mesmo ponto em aberto da ADR-0018); ele é combinado com o responsável pela porta de entrada, e esta ADR não o supõe. |
| **3. REST entre serviços e no site** | As consultas e ações do site chegam em REST com JSON sobre HTTPS (RNF-3), em endereços versionados no plural, como `/v1/turnarounds/{id}/linha-do-tempo` e `/v1/alertas`. Se outro serviço precisar de um dado que só o Monitoramento tem, o pedido também chega em REST. Uma recusa de regra de negócio, como a checagem de um aviso já encerrado (RF-35), volta com o motivo no corpo, num formato de erro único (Problem Details, RFC 9457). A descrição OpenAPI sai do código pelo FastAPI. O painel (RF-25) é o lugar previsto para o GraphQL da ADR-0016 e usa Strawberry GraphQL na mesma aplicação; se os itens 13 e 14 pedirem GraphQL em outra tela de monitoramento, a mesma biblioteca atende. As mudanças chegam ao painel, à linha do tempo e à lista de alertas por WebSocket, para cumprir os 5 s do RNF-11. |
| **4 e 5. RabbitMQ e envelope dos avisos** | O serviço tem uma fila durável própria, `monitoramento`, e consome e publica com o aio-pika, com mensagens persistentes. Todo aviso passa por um único modelo Pydantic de envelope, com os campos `id`, `tipo`, `versao`, `ocorridoEm`, `turnaroundId`, `autorId`, `origem` (sempre `monitoramento` nos avisos que ele publica), `causaId` e `dados`. Aviso com campo faltando ou com `versao` desconhecida é recusado e registrado no log, sem quebrar o consumo. **Ao consumir**, o serviço grava o `id` do aviso numa coleção de avisos processados, com índice único, na mesma transação das mudanças que o aviso causa (cópia da tarefa, recálculo, alerta), e ignora o repetido. A mensagem só é confirmada à fila depois da gravação. **Ao publicar** (por exemplo, um aviso de alerta emitido), o aviso é gravado numa coleção de saída na mesma transação da mudança e enviado logo depois; assim não há alerta gravado sem aviso nem aviso de alerta que não existe (RNF-20). |
| **6. Horários em UTC** | O cliente do MongoDB usa `tz_aware=True` com `tzinfo=timezone.utc`, e todo horário é `datetime` com fuso UTC no código. O MongoDB grava datas sempre em UTC (tipo `date` do BSON, com milissegundos), então não há horário sem fuso no banco. O JSON sai em ISO 8601 terminado em `Z`. Os instantes-limite dos gatilhos (TOBT − X, TOBT + 5, TOBT − 15) são calculados em UTC; só a tela converte para o horário local. |
| **7. UUID** | Cada projeção, alerta, checagem ou cálculo gravado recebe um UUID versão 4 gerado pelo próprio serviço (`uuid.uuid4()`), guardado como `_id` do documento no subtipo 4 do BSON (`uuidRepresentation="standard"`). Identificadores de outros serviços (turnaround, tarefa, usuário, equipe) ficam guardados como vieram, sem referência obrigatória (ADR-0015, consequências). |
| **8. Nomes em português** | Classes em PascalCase no singular (`Alerta`, `AlertaController`, `ProjecaoService`, `AlertaRepository`). Métodos e atributos em camelCase, como pede a ADR-0016 (`recalcularProjecao()`, `turnaroundId`), com o verificador de estilo (Ruff) configurado para aceitar essa convenção no lugar do snake_case usual do Python. Coleções e campos no MongoDB em snake_case e no singular (`alerta`, `turnaround_id`), como as tabelas e os campos da ADR-0016: o modelo base do Pydantic tem um gerador de apelidos (`alias_generator=to_snake`) usado só na gravação no banco, e o JSON sai com o nome do atributo, em camelCase. Endereços em minúsculas e no plural; avisos em PascalCase e no passado, por exemplo `AlertaEmitido` e `CaminhoCriticoAlterado`. |

### Tipos do item 12 no MongoDB (decisão B1)

O item 12 continua com tipos SQL padrão. No desenvolvimento, cada coleção do Monitoramento tem um validador `$jsonSchema` com os campos obrigatórios, os tipos e os tamanhos do item 12. Assim, o banco recusa um documento fora do modelo, como faria uma tabela.

| Tipo no item 12 | No MongoDB |
|---|---|
| `TIMESTAMP WITH TIME ZONE` | `date` do BSON, sempre em UTC |
| identificador `UUID` | `binData` subtipo 4 |
| `VARCHAR(n)` | `string`, com `maxLength: n` no validador |
| `INTEGER` | `int` (minutos de atraso, desvio, contagens) |
| `DECIMAL(p,s)` | `decimal` (Decimal128), se o item 12 usar |
| `BOOLEAN` | `bool` |
| chave primária | `_id` |
| restrição de unicidade | índice único |
| chave estrangeira dentro do serviço | identificador guardado no documento ou subdocumento embutido (por exemplo, as tarefas copiadas dentro do turnaround monitorado) |
| tabela associativa | lista dentro do documento (por exemplo, as tarefas do caminho crítico) |

### Recálculo, gatilhos por horário e concorrência

- **Recálculo (RF-22 a RF-24).** Cada aviso que muda o turnaround dispara o recálculo daquele turnaround dentro da mesma transação do consumo: registro de tarefa, plano, TOBT vigente ou correção da chegada. Com até 30 tarefas, o cálculo da projeção, dos atrasos e do caminho crítico é um percurso único pelo grafo de dependências, em memória. [Inferência] Ele fica bem abaixo de 1 s, e o teste de carga do RNF-13 confirma o RNF-12.
- **Concorrência.** O documento do turnaround monitorado tem um campo de revisão. A gravação só acontece se a revisão não mudou desde a leitura; se mudou, o serviço relê e recalcula. Assim, dois avisos do mesmo turnaround consumidos ao mesmo tempo não perdem atualização, mesmo com mais de uma cópia do serviço no ar. A cópia de cada tarefa guarda o `ocorridoEm` do último aviso aplicado, e um aviso mais antigo não sobrescreve a cópia.
- **Gatilhos por horário (RF-27, RF-30, RF-31, RF-32 e o recálculo a cada minuto do RF-22).** Cada turnaround monitorado guarda o próximo instante-limite, com índice. Uma tarefa em segundo plano do serviço confere a cada segundo os turnarounds com instante vencido, o que deixa folga dentro dos 5 s do RNF-12. Os valores de X, Y, da tolerância de 5 min e dos 15 min vêm de parâmetros, e não do código (RNF-21).
- **Alerta sem duplicação.** Cada alerta tem uma chave única com o turnaround, o tipo e o ciclo de emissão. Mesmo com duas cópias do serviço vendo o mesmo gatilho, só um alerta é gravado. É também essa chave que faz o RF-28 só emitir de novo depois de a projeção voltar para até TOBT + 5 e passar outra vez desse limite (ADR-0001).

### Disponibilidade, gravação e logs

- **RNF-19:** a rota de saúde (`/health`) confere o MongoDB e a mensageria e serve para a medição automática a cada minuto. O serviço roda em contêiner com reinício automático e com mais de uma cópia, o que a chave única dos alertas e a revisão do documento permitem.
- **RNF-20:** as gravações usam `writeConcern` `majority` com diário (`j: true`). A resposta ao usuário, como na checagem do RF-35, só sai depois da gravação confirmada. Em produção, o replica set tem três nós.
- **RNF-2 e RNF-24:** a trilha de auditoria é gravada na mesma transação da mudança. As ações automáticas identificam o Motor de Eventos e o `causaId` do aviso que as causou. O log sai em JSON (biblioteca structlog) e traz o turnaround, o autor, o horário e o `causaId`.

## Consequências

- Os itens 12 a 15 continuam com tipos SQL padrão e tipos UML neutros (decisão B1). No desenvolvimento, as tabelas do Monitoramento no item 12 viram coleções com validador, segundo a tabela de conversão acima, e as camadas `Controller → Service → Repository` do item 13 viram rotas, serviços e repositórios do FastAPI com o mesmo nome de classe.
- Nos diagramas de sequência da área C (item 14), os participantes são as camadas de referência e o banco do Monitoramento. Não é preciso citar FastAPI ou MongoDB nos diagramas, e as mensagens seguem em camelCase.
- Como na ADR-0018, o Monitoramento tem duas coleções técnicas além das de negócio: a de avisos a publicar e a de avisos processados. Os diagramas de sequência gravam nelas; por isso elas entram no modelo do item 12 como tabelas técnicas do serviço.
- As transações entre documentos exigem replica set, inclusive no desenvolvimento (um nó em Docker). Sem ele, a gravação do aviso processado junto das mudanças não funciona.
- O serviço é o único do grupo em Python. A revisão de código entre integrantes fica mais lenta e nenhum código é compartilhado com os outros serviços; o contrato da ADR-0016 (JSON, envelope, OpenAPI) é o que garante a conversa entre eles.
- A escolha pode ser revista durante a implementação. Nesse caso, uma ADR nova substitui esta.

---

## Ligações

- **Divisão em microsserviços:** [ADR-0015](0015-divisao-em-microsservicos.md)
- **Contrato entre os serviços:** [ADR-0016](0016-contrato-entre-os-servicos.md)
- **Referência de horário TOBT + 5 min:** [ADR-0001](0001-referencia-horario-tobt-mais-5-min.md)
- **Requisitos da área C:** [RFs](../../especificacao/06-requisitos-funcionais/area-c.md), [RNFs](../../especificacao/08-requisitos-nao-funcionais/area-c.md)
- **Critérios do RA2:** [entregas/ra2-criterios-de-aceite.md](../../entregas/ra2-criterios-de-aceite.md)
- **Contexto geral:** [CONTEXT.md](../../CONTEXT.md)
