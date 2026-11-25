---
id: adr-0023
titulo: "ADR-0023 — Interfaces da porta de entrada e do Cadastro e Planejamento com os outros serviços"
tipo: decisao
decisao: D23
status: aceita
data: 2026-11-15
decisor: Eduardo Fabri
itens_template: [12, 13, 14, 15]
areas: [A, B, C, D]
fontes: []
relacionados: [adr-0016, adr-0015, adr-0017, adr-0018, adr-0019, adr-0020]
---
# ADR-0023 — Interfaces da porta de entrada e do Cadastro e Planejamento com os outros serviços

- **Status:** aceita · **Data:** 15/11/2026 · **Decisor:** Eduardo Fabri (responsável pela porta de entrada e pelo Cadastro e Planejamento) · **Complementa:** [ADR-0016](0016-contrato-entre-os-servicos.md) (contrato entre os serviços)

## Contexto

- A [ADR-0016](0016-contrato-entre-os-servicos.md) diz que a porta de entrada consulta o Cadastro e Planejamento a cada ação e informa ao serviço quem é o usuário e o perfil, mas não diz como. A porta de entrada e o Cadastro são da área A (ADR-0016, ponto 2).
- Os outros serviços, os itens 12 a 15 e as ADRs de tecnologia supunham essas amarrações. A [pendência #178](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/issues/178) reuniu as suposições, e a área A respondeu ponto a ponto em 15/11/2026.
- A resposta foi escrita primeiro dentro da [ADR-0017](0017-tecnologia-cadastro-e-planejamento.md) (PR [#175](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/175)). Mas a ADR-0017 é a da tecnologia de um serviço (tarefa T04-A, decisão B2), e estes pontos obrigam os quatro serviços: são contrato entre os serviços, o assunto da ADR-0016. Por isso passaram para esta ADR, **com o mesmo texto e a mesma numeração**. Quem cita "ADR-0017, interfaces, ponto N" encontra aqui o mesmo ponto N.
- Siglas usadas abaixo: requisito funcional (RF), requisito não funcional (RNF), caso de uso (UC), regra de negócio (RN), token JSON assinado (JWT), horário estimado de chegada à posição (EIBT), tempo mínimo de turnaround (MTTT) e horário real de saída da posição (AOBT).

## Decisão

1. **Identidade passada aos serviços: token interno assinado.** A cada ação, a porta de entrada confere o token de login, consulta o Cadastro e só então gera um token interno: um token JSON assinado (JWT), com validade de 60 s, assinado com a chave privada da porta de entrada. Ele leva o identificador do usuário, o perfil, a equipe (Operador de Solo/Rampa), a companhia (Autoridade de Liberação), o identificador da sessão e se a chamada é ação do usuário. Cada serviço confere a assinatura com a chave pública da porta de entrada e a validade, e recusa a chamada sem token válido. Cabeçalhos simples foram descartados: bastaria um serviço exposto na rede para alguém se passar por outro perfil.
2. **Ação do usuário × consulta automática (RNF-5).** O site marca as consultas automáticas (painel, recarga de lista) ao chamar a porta de entrada. Nelas, a porta de entrada não renova a sessão e põe "não é ação do usuário" no token interno; as demais chamadas renovam a sessão.
3. **Consultas que o Cadastro oferece.** À porta de entrada, a situação, o perfil, a equipe e a companhia do usuário. À Execução em Solo, os operadores ativos de uma equipe, com identificador e nome, consultados na hora da reatribuição, da inclusão de tarefa e da lista de disponíveis (RF-37, RF-42 e RF-43), sem cópia na Execução em Solo (ADR-0015, regra 1). Aos quatro perfis, pela porta de entrada, o nome dos usuários e das equipes, para exibir nas telas (RNF-1).
4. **Consultas que o Cadastro faz à Execução em Solo.** Antes de desativar um operador ou uma equipe ou de trocar a equipe de um operador (RF-2 e RF-9), as tarefas pendentes nos planos já entregues; as dos planos ainda não confirmados o Cadastro confere no próprio banco. Antes de gravar o EIBT e o MTTT (RF-10; UC10, RN3), se a chegada já foi registrada. Se a Execução em Solo não responder, a ação é recusada como falha técnica (ADR-0016, ponto 3), e nada é gravado.
5. **Confirmação do plano (RF-5; RNF-20).** O Cadastro grava o plano como "confirmação pendente", com uma chave de idempotência, e só então o envia à Execução em Solo. Com a resposta positiva, marca o plano como confirmado; com a recusa (por exemplo, tarefa já iniciada), volta ao plano anterior. Se cair depois do envio, a retomada reenvia o mesmo pedido com a mesma chave, e a Execução em Solo responde o mesmo resultado, como o pedido pendente da ADR-0020. Enquanto a confirmação está pendente, o plano não pode ser editado.
6. **Prazo dos dados pessoais (RNF-6).** O Cadastro não conhece sozinho todos os turnarounds de um usuário, porque a reatribuição e os registros ficam na Execução em Solo. O prazo é calculado com o aviso de encerramento do turnaround (Fora de bloco), que a Execução em Solo publica com o horário real de saída da posição (AOBT) e os usuários que tiveram tarefa ou registro nele. O Cadastro grava esses vínculos e anonimiza cada usuário na data mais tardia entre 90 dias depois da desativação e 90 dias depois do AOBT de cada turnaround vinculado. O conteúdo desse aviso é da Execução em Solo e fica como pendência da área B.
7. **Conexões em tempo real (WebSocket).** As telas que recebem mudanças em tempo real (a lista de tarefas do operador, os painéis do coordenador e a solicitação de atualização da previsão) abrem a conexão pela porta de entrada, como toda outra chamada do site; nenhum serviço fica exposto direto ao site ([pendência #228](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/issues/228)).
   - **Na abertura,** a porta de entrada confere o token de login e consulta o Cadastro (RNF-1), como numa ação, e repassa a conexão ao serviço com o token interno do ponto 1. O serviço confere o token e só então aceita a conexão.
   - **Com a conexão aberta,** a porta de entrada consulta o Cadastro de novo a cada minuto. Se o usuário foi desativado (RNF-1) ou a sessão venceu por inatividade (RNF-5), ela fecha a conexão, e a tela volta para a autenticação. Na saída do usuário (UC01), que também passa pela porta de entrada, ela fecha na hora as conexões da sessão.
   - **O intervalo de um minuto é escolha do projeto,** e não vem de requisito. Entre duas consultas, o usuário desativado ou com a sessão vencida ainda pode receber mudanças na tela por até um minuto; nenhuma ação dele é aceita nesse tempo, porque cada ação passa pela consulta do ponto 1 (RNF-1).
   - **A conexão só leva mudanças do serviço à tela.** As ações do usuário continuam indo pela porta de entrada como chamadas comuns, cada uma com o seu token interno (ponto 1).
   - **As mensagens que chegam à tela não renovam a sessão,** como as consultas automáticas do ponto 2; só as ações do usuário a renovam.

## Consequências

- **Todos os serviços** conferem o token interno (ponto 1) e leem dele o usuário, o perfil, a equipe, a companhia, a sessão e se a chamada é ação do usuário. As ADRs 0018 e 0020 e a interação "Verificar o acesso na porta de entrada" do item 14 podem citar o ponto 1.
- **Execução em Solo:** responde às consultas do ponto 4, consulta os operadores ativos no Cadastro (ponto 3), reconhece o reenvio do plano pela chave (ponto 5) e publica o aviso de encerramento com os usuários vinculados (ponto 6).
- **Itens 12 e 13:** o plano do Cadastro ganha a situação "confirmação pendente" e a chave de idempotência (ponto 5), e o Cadastro grava os vínculos de usuário e turnaround (ponto 6). O item 13 supunha outra ordem entre gravar e enviar o plano ([#208](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/208), seção 13.5.2) e se ajusta a esta ADR.
- **Serviços com tempo real (Execução em Solo, Monitoramento e Exceções e Liberação):** aceitam a conexão só pela porta de entrada e com o token interno (ponto 7). No item 13, a `PortaDeEntrada` também encaminha a abertura das conexões dos notificadores, e o item 14 mostra a abertura passando por ela.
- A ADR-0017 continua sendo só a da tecnologia do Cadastro e Planejamento e aponta para esta.
- O ponto 7 entrou depois da aceitação desta ADR, pelo [PR #237](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/237), para responder à [pendência #228](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/issues/228): nenhuma ADR dizia como a conexão em tempo real passa pela porta de entrada. Os pontos 1 a 6 não mudaram.

---

## Ligações

- **Contrato entre os serviços:** [ADR-0016](0016-contrato-entre-os-servicos.md) (complementada por esta)
- **Divisão em microsserviços:** [ADR-0015](0015-divisao-em-microsservicos.md)
- **Tecnologia dos serviços:** [ADR-0017](0017-tecnologia-cadastro-e-planejamento.md) (Cadastro e Planejamento), [ADR-0018](0018-tecnologia-execucao-em-solo.md) (Execução em Solo), [ADR-0019](0019-tecnologia-monitoramento.md) (Monitoramento), [ADR-0020](0020-tecnologia-excecoes-e-liberacao.md) (Exceções e Liberação, pedido pendente)
- **Requisitos:** [Item 6 — área A](../../especificacao/06-requisitos-funcionais/area-a.md), [Item 8 — área A](../../especificacao/08-requisitos-nao-funcionais/area-a.md)
- **Índice das decisões:** [README.md](README.md) · **Contexto geral:** [CONTEXT.md](../../CONTEXT.md)
