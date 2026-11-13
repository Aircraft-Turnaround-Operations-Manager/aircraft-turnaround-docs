---
id: adr-0015
titulo: "ADR-0015 — Quatro microsserviços, com a tarefa e o estado do turnaround na Execução em Solo"
tipo: decisao
decisao: D15
status: aceita
data: 2026-11-01
decisor: Rodrigo Alves
itens_template: [12, 13, 14]
areas: [A, B, C, D]
fontes: []
relacionados: [adr-0004, adr-0012, adr-0013, adr-0014]
---
# ADR-0015 — Quatro microsserviços, com a tarefa e o estado do turnaround na Execução em Solo

- **Status:** aceita · **Data:** 01/11/2026 · **Decisor:** Rodrigo Alves

## Contexto

- O sistema será feito em microsserviços, um por integrante. Cada serviço tem banco próprio, e um serviço não lê o banco de outro.
- Os itens 12, 13 e 14 precisam da divisão: o modelo de dados se reparte por serviço, as classes declaram a arquitetura de implementação e os diagramas de sequência mostram a comunicação.
- Na primeira proposta, os serviços seguiam as áreas A a D, e todos os serviços trocavam apenas avisos. A revisão momento a momento do turnaround encontrou cinco conflitos: chegada (RF-12), reatribuição e replanejamento (RF-37 e RF-42), exceção (RF-36), liberação (RF-39) e saída (RF-44). Todos vêm de a tarefa e o estado do turnaround estarem espalhados.
- O conflito mais grave é o da liberação: decidir com uma cópia atrasada das tarefas pode liberar a aeronave com tarefa obrigatória pendente, o que a meta do item 1 proíbe.

## Opções consideradas

1. **Versão 1:** dados nos serviços das áreas e comunicação só por avisos. Mantém os cinco conflitos.
2. **Versão 2:** tarefa e estado na Execução em Solo; avisos pela mensageria e pedidos com resposta em chamada direta.
3. **Versão 3:** igual à versão 2, com os pedidos também pela mensageria. Nos pedidos alguém está esperando a resposta, então a fila traz pouca vantagem e exige ligar cada resposta ao pedido, além de tratar tempo de espera e resposta repetida.

## Decisão

**Versão 2.**

**Serviços e RFs.** A numeração dos RFs, as estórias e os casos de uso não mudam.

| Serviço | RFs | Dados que só ele grava |
|---|---|---|
| Cadastro e Planejamento | RF-1 a RF-11 | Usuários, perfis, equipes, cadastro do turnaround, modelos, plano inicial, política de abastecimento |
| Execução em Solo | RF-12 a RF-21 e RF-44 | Tarefas do turnaround em andamento, marcos, AIBT, ACGT, ASBT, AEGT, AOBT e estado do turnaround e das tarefas |
| Monitoramento | RF-22 a RF-35 | Projeções, alertas, indicadores e checagens |
| Exceções e Liberação | RF-36 a RF-43 | Exceções, ações sobre alertas, motivos de reatribuição e replanejamento, TOBT vigente e ARDT |

**Regras.**

1. Só o dono do dado decide sobre ele. Outro serviço pode guardar uma cópia para exibir ou calcular, nunca para decidir.
2. **Aviso (evento), pela mensageria:** informa o que já aconteceu; quem envia não espera.
3. **Pedido (comando) com resposta, em chamada direta:** usado quando alguém espera a decisão do dono do dado. Vale para reatribuição (RF-37), replanejamento (RF-42), exceção (RF-36 e RF-40), liberação (RF-39) e consultas que dependem do dado original (RF-2, RF-9 e RF-43).
4. A Execução em Solo é o único serviço que grava o estado do turnaround e atende um pedido de cada vez por turnaround.
5. Ao confirmar o plano (RF-5), a Execução em Solo recebe tarefas, dependências, pontos de QR Code, catálogo sob demanda e política de abastecimento. Uma nova confirmação substitui esses dados e é recusada depois do início das tarefas.
6. Na liberação, Exceções e Liberação confere as exceções e pede a liberação; a Execução em Solo confere o estado e as tarefas e responde; o ARDT é gravado com a resposta positiva.
7. O Motor de Eventos é um ator lógico: a propagação e os marcos (RF-20 e RF-21) ficam na Execução em Solo, e os cálculos e alertas, no Monitoramento.
8. Cada área corresponde a um serviço. RF-12, RF-13 e RF-44, com US012, US013, US044, UC12, UC13 e UC37, passam da área de origem para a área B, sem mudar de número.

**Documento e implementação.** A especificação usa em todos os serviços a referência `Controller → Service → Repository`, com publicadores e consumidores de avisos. Cada integrante escolhe linguagem, framework e banco do seu serviço.

## Consequências

- O item 12 tem um modelo por serviço e uma visão geral. Entre serviços não há chave estrangeira: a tabela guarda só o identificador, e o texto explica isso.
- No item 13, as classes se referenciam por tipo dentro do serviço e por identificador entre serviços.
- O item 14 mostra avisos na mensageria e pedidos entre serviços.
- A Execução em Solo fica com 11 RFs e passa a atender os pedidos dos demais serviços. Se ela cair, chegada, saída, exceção e liberação param. O limite é o do RNF-7 e do RNF-19: 99,5% ao mês.
- Fica para o grupo o contrato comum: formato dos avisos e das APIs, token de login, horários com fuso, identificadores e produto de mensageria.
- A área B passa a ter 11 RFs e 11 casos de uso, e faz os itens 14 e 15 desses casos. A troca de área nos arquivos do RA1 é uma tarefa do RA2; o conteúdo dos RFs, estórias e casos de uso não muda.

---

## Ligações

- **Material de construção:** [Blueprint do turnaround por serviço](../../pesquisa/topicos/service-blueprint.md), a revisão momento a momento citada no Contexto ([versão interativa](https://claude.ai/artifact/8sGNer92aRqri469tj5i7V))
- **Contexto geral:** [CONTEXT.md](../../CONTEXT.md)
- **Critérios do RA2:** [entregas/ra2-criterios-de-aceite.md](../../entregas/ra2-criterios-de-aceite.md)
- **Matriz de rastreabilidade:** [ADR-0012](0012-matriz-de-rastreabilidade.md)
- **Chegada registrada pelo operador:** [ADR-0013](0013-chegada-registrada-pelo-operador.md)
- **Serviços sob demanda:** [ADR-0014](0014-servicos-sob-demanda.md)
