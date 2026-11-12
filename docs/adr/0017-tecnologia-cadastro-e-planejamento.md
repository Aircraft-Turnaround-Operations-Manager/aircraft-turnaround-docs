---
id: adr-0017
titulo: "ADR-0017 — Tecnologia do serviço Cadastro e Planejamento: Java 21, Spring Boot e PostgreSQL"
tipo: decisao
decisao: D17
status: aceita
data: 2026-11-12
decisor: Eduardo Fabri
itens_template: [12, 13, 14]
areas: [A]
fontes: []
relacionados: [adr-0015, adr-0016, adr-0003, adr-0005, adr-0010]
---
# ADR-0017 — Tecnologia do serviço Cadastro e Planejamento: Java 21, Spring Boot e PostgreSQL

- **Status:** aceita · **Data:** 12/11/2026 · **Decisor:** Eduardo Fabri (responsável pelo serviço, decisão B2)

## Contexto

- A [ADR-0015](0015-divisao-em-microsservicos.md) dividiu o sistema em quatro microsserviços, um por integrante, e deixou a escolha de linguagem, framework e banco para o responsável de cada um. Esta ADR é a do serviço **Cadastro e Planejamento** (área A, RF-1 a RF-11), com o número reservado na tarefa T04-A ([issue #158](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/issues/158)).
- A escolha precisa seguir o contrato da [ADR-0016](0016-contrato-entre-os-servicos.md): REST com JSON sobre HTTPS entre os serviços, RabbitMQ com o envelope comum dos avisos, horários em UTC (Tempo Universal Coordenado) terminados em `Z`, identificadores UUID (identificador universal único) versão 4 e nomes em português.
- O que o serviço faz define o que ele precisa da tecnologia:
  - **Login e porta de entrada.** O Cadastro guarda usuários e senhas e emite o token de login (ADR-0016, ponto 2). A porta de entrada (Spring Cloud Gateway, também do `eduardofabrii`) consulta o Cadastro **a cada ação** para saber se o usuário está ativo e qual é o perfil (RNF-1). Essa consulta tem de ser rápida e não pode falhar à toa: se o Cadastro cair, o sistema para (ADR-0016, consequências).
  - **Cadastros com regras de unicidade e de vínculo.** Identificador de acesso único (RF-2), identificador de equipe único (RF-9), um turnaround só para os mesmos voos e datas (RF-3), nome e identificador do ponto de QR Code (código de resposta rápida) únicos na tarefa (RF-7).
  - **Gravação junto com a auditoria.** O plano e a auditoria são salvos juntos, sem gravar só parte das tarefas (UC05, RN5; RNF-2 e RNF-4); a auditoria guarda valores anteriores e novos, autor e horário com fuso (RNF-2).
  - **Senha protegida.** Função própria para senhas, com sal individual, nunca em texto legível (RNF-3).
  - **Grafo pequeno de dependências.** Recusa de ciclos e de referências inválidas entre tarefas (RF-8), e a sequência desembarque, abastecimento e embarque quando a política da companhia não permite abastecimento com passageiros (RF-11; ADR-0005).
- O volume é pequeno: dezenas de usuários e equipes, alguns modelos e um turnaround por par de voos. Não há requisito de vazão alta; há de consistência e de disponibilidade (99,5% ao mês, RNF-19).

## Opções consideradas

1. **Java 21 + Spring Boot 4 + PostgreSQL 16.** Mesma linguagem e mesmo ecossistema da porta de entrada (Spring Cloud Gateway). Spring Security tem funções prontas para senha com sal (BCrypt ou Argon2) e para token assinado; Spring AMQP fala com o RabbitMQ; springdoc gera o OpenAPI a partir do código. PostgreSQL tem `uuid`, `timestamptz`, `jsonb`, restrição de unicidade e transação.
2. **Node.js (TypeScript) + NestJS + PostgreSQL.** Mesmo banco e mesma linguagem do site (Angular, TypeScript). Exige outro ecossistema ao lado da porta de entrada, que já é Java, e bibliotecas separadas para validação, senha e mensageria.
3. **Python + FastAPI + PostgreSQL.** Rápido de escrever e com OpenAPI automático. Mesmo problema da opção 2 em relação à porta de entrada, e a tipagem dos contratos é mais fraca, o que pesa num serviço que é a referência de usuários, equipes e plano para os outros três.
4. **Java 21 + Spring Boot 4 + MongoDB.** Guarda o modelo de tarefas como um documento só. Perde a restrição de unicidade entre documentos e a transação simples entre plano e auditoria, que são justamente as regras mais fortes do serviço, e se afasta do modelo lógico relacional do item 12.

## Decisão

**Opção 1: Java 21, Spring Boot 4 e PostgreSQL 16.**

| Camada | Escolha | Motivo |
|---|---|---|
| **Linguagem** | Java 21 (versão de suporte longo, LTS) | Mesma linguagem da porta de entrada, que também fica com o responsável deste serviço: o token emitido aqui é conferido lá com a mesma biblioteca. Tipagem forte nos contratos que os outros três serviços consomem. Record para os dados de entrada e saída das APIs. |
| **Framework** | Spring Boot 4 (Spring Web MVC, Spring Security, Spring Data JPA, Spring AMQP, Bean Validation, springdoc-openapi, Flyway, Actuator) | Cobre tudo o que o serviço precisa sem biblioteca avulsa: REST, login e token, senha com sal, acesso ao banco com transação, mensageria, validação dos campos, OpenAPI gerado do código (ADR-0016, ponto 3) e verificação de saúde para medir a disponibilidade (RNF-19). |
| **Banco** | PostgreSQL 16 | Relacional, como o modelo lógico do item 12. Tem os tipos de que o contrato precisa (`uuid`, `timestamptz`), restrição de unicidade para as regras de duplicidade (RF-2, RF-3, RF-7, RF-9), chave estrangeira dentro do serviço, transação para gravar plano e auditoria juntos e `jsonb` para os valores anteriores e novos da auditoria. |

**Como o serviço cumpre o contrato da ADR-0016:**

| Ponto da ADR-0016 | Como o Cadastro e Planejamento cumpre |
|---|---|
| 2. Login e porta de entrada | O Cadastro guarda a senha com a função de senha do Spring Security (BCrypt, com sal individual; RNF-3) e emite o token de login assinado. Oferece à porta de entrada uma consulta da situação e do perfil do usuário, feita a cada ação; desativar o usuário (RF-2) faz a consulta seguinte responder "inativo", e a ação é recusada mesmo com sessão aberta (RNF-1). Senha, hash e token nunca entram na auditoria nem nas respostas de cadastro (RNF-2, RNF-3). |
| 3. REST entre serviços | Spring Web MVC com JSON sobre HTTPS, versão no endereço (`/v1/...`) e endereços em minúsculas e no plural (`/v1/equipes`, `/v1/turnarounds/{id}/plano`). O OpenAPI de cada versão é gerado do código pelo springdoc. Recusa de regra de negócio volta com o motivo (por exemplo, a lista de tarefas pendentes que impede desativar um operador, US002-CA7). Os pedidos com resposta que o Cadastro faz à Execução em Solo, como a entrega do plano confirmado (ADR-0015, regra 5) e a consulta de tarefas pendentes antes de desativar operador ou equipe (RF-2 e RF-9), são chamadas REST diretas. |
| 4 e 5. RabbitMQ e envelope dos avisos | Spring AMQP, com a fila durável própria do serviço. Todo aviso publicado usa o envelope comum (`id`, `tipo`, `versao`, `ocorridoEm`, `turnaroundId`, `autorId`, `origem` = `cadastro-e-planejamento`, `causaId`, `dados`), com o tipo em PascalCase no passado. O aviso é gravado numa tabela de saída na mesma transação do dado e publicado depois, para que nenhuma mudança confirmada fique sem aviso e nenhum aviso saia de uma mudança desfeita (RNF-2). Os avisos recebidos têm o `id` guardado, e o repetido é ignorado. |
| 6. Horários em UTC | Campos de horário em `timestamptz` no banco e `Instant` no código; o JSON sai em ISO 8601 terminado em `Z`. O site converte para o horário local. Os horários do RF-3 e do RF-10 (SIBT, SOBT, EIBT, TOBT planejado e vigente) chegam com data e fuso e são guardados em UTC, sem perder a virada do dia (US003-CA4). |
| 7. Identificadores | UUID versão 4 gerado pelo próprio serviço para usuários, equipes, modelos, tarefas do modelo, pontos de QR Code, turnarounds e planos; coluna do tipo `uuid`. O identificador recebido de outro serviço é guardado sem alteração e sem chave estrangeira (ADR-0015). |
| 8. Nomes | Classes em PascalCase no singular (`Usuario`, `ModeloTarefa`, `EquipeController`); métodos e atributos em camelCase; tabelas e campos em snake_case no singular (`usuario`, `equipe_id`), versionados nas migrações do Flyway; JSON em camelCase (`turnaroundId`). Tudo em português, sem acento no código. |

**Tipos do item 12 no PostgreSQL.** O item 12 continua com tipos SQL padrão (decisão B1). No desenvolvimento, `VARCHAR(n)` fica igual, `TIMESTAMP WITH TIME ZONE` vira `timestamptz`, `BOOLEAN` e `INTEGER` ficam iguais e os identificadores viram `uuid`.

## Consequências

- O responsável pelo serviço usa a mesma pilha na porta de entrada e no Cadastro, o que reduz o trabalho de manter a emissão e a conferência do token.
- Os itens 13 e 14 da área A podem usar as camadas de referência da ADR-0015 (`Controller → Service → Repository`) sem tradução: são as mesmas do Spring.
- No desenvolvimento, o serviço roda com PostgreSQL e RabbitMQ em Docker na máquina do integrante (ADR-0016, ponto 4). Os testes de integração usam o mesmo PostgreSQL em contêiner, para que as restrições de unicidade e os tipos `uuid` e `timestamptz` sejam testados como em produção.
- Como a porta de entrada consulta o Cadastro a cada ação, o serviço não guarda sessão na memória e pode rodar com mais de uma instância atrás da porta de entrada, para cumprir os 99,5% do RNF-19. A verificação de saúde do Actuator serve à medição a cada 1 minuto.
- A tabela de saída dos avisos e a tabela de avisos já processados são do próprio serviço e entram no modelo de dados do Cadastro e Planejamento no item 12, se o grupo quiser mostrá-las; elas não guardam dado de negócio.
- A escolha não muda nenhum RF, estória ou caso de uso, nem as ADRs 0015 e 0016. Se a implementação pedir outro banco ou framework, uma ADR nova substitui esta.

---

## Ligações

- **Divisão em microsserviços:** [ADR-0015](0015-divisao-em-microsservicos.md)
- **Contrato entre os serviços:** [ADR-0016](0016-contrato-entre-os-servicos.md)
- **Regras usadas na escolha:** [ADR-0003](0003-atualizar-previsao-na-antecipacao.md) (TOBT planejado e vigente), [ADR-0005](0005-abastecimento-com-passageiros-configuravel.md) (política de abastecimento), [ADR-0010](0010-administrador-usuario-e-equipe-do-operador.md) (usuários, perfis e equipes)
- **Requisitos do serviço:** [Item 6 — área A](../../especificacao/06-requisitos-funcionais/area-a.md), [Item 8 — área A](../../especificacao/08-requisitos-nao-funcionais/area-a.md)
- **Critérios do RA2:** [entregas/ra2-criterios-de-aceite.md](../../entregas/ra2-criterios-de-aceite.md) (decisões B1 e B2)
- **Índice das decisões:** [README.md](README.md) · **Contexto geral:** [CONTEXT.md](../../CONTEXT.md)
