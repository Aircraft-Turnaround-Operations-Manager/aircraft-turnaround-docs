---
id: adr-0013
titulo: "ADR-0013 — Chegada à posição registrada direto pelo operador, sem confirmação"
tipo: decisao
decisao: D13
status: aceita
data: 2026-10-10
decisor: Rodrigo Alves
itens_template: [6, 7, 10]
areas: [A]
fontes: [2, 4]
relacionados: [marcos-e-horarios, papeis-e-atores, adr-0004, adr-0007]
---
# ADR-0013 — Chegada à posição registrada direto pelo operador, sem confirmação

- **Status:** aceita · **Data:** 10/10/2026 · **Decisor:** Rodrigo Alves

## Contexto

- Nenhum RF dizia quem registra o horário real de chegada à posição (AIBT), que leva o turnaround ao estado "Em solo" (pendência da issue #59).
- **[Fato][2][4]** O AIBT é o marco 7 do A-CDM (*in-blocks*); conforme a implantação local, ele vem dos sistemas do controle de tráfego aéreo, do aeroporto ou da empresa de *handling* ([marcos e horários](../../pesquisa/topicos/marcos-e-horarios.md)).
- O BPMN do item 4 tem só o evento "Aeronave em posição (AIBT)", sem tarefa de confirmação, e a saída da posição (AOBT) já é registrada direto pelo Operador de Solo/Rampa (RF-D9).
- A primeira redação dos RFs da área A (PR #79) propunha duas etapas: o operador informa o horário, que fica pendente, e o Coordenador de Turnaround confirma ou recusa; só a confirmação gravava o AIBT.

## Opções consideradas

- **(a)** Duas etapas: o operador informa e o Coordenador de Turnaround confirma ou recusa.
- **(b)** O operador registra o AIBT direto; o Coordenador de Turnaround pode corrigir o valor depois.
- **(c)** Só o Coordenador de Turnaround registra o AIBT.

## Decisão

**(b)**:

1. O **Operador de Solo/Rampa registra o AIBT** e, com esse registro, o turnaround entra em "Em solo". Não há situação "pendente" nem confirmação.
2. O registro é recusado se o operador não tiver tarefa atribuída nesse turnaround, se o horário for futuro, se a chegada já estiver registrada ou se o plano inicial não estiver confirmado.
3. O **Coordenador de Turnaround pode corrigir o AIBT registrado**, informando o motivo; o sistema guarda o valor anterior e o novo, com autor e horário.
4. **[Inferência]** A correção é permitida enquanto o turnaround não estiver "Fora de bloco". Ela não muda o estado do turnaround nem das tarefas e dispara o recálculo da projeção de prontidão.

Motivos: a chegada fica igual à saída (RF-D9); o dado vem de quem está na posição (ADR-0007); e a etapa de confirmação atrasaria a entrada em "Em solo" e, com ela, a liberação das tarefas sem predecessora.

## Consequências

- **RF-A12:** passa a registrar o AIBT e a levar o turnaround a "Em solo", com as recusas do item 2. A trava "plano confirmado" vem do RF-A13 para o RF-A12.
- **RF-A13:** deixa de ser "confirmar ou recusar" e passa a ser a correção do AIBT pelo Coordenador de Turnaround (itens 3 e 4).
- **RF-A10:** a atualização do horário estimado de chegada à posição (EIBT) e do tempo mínimo de turnaround (MTTT) vale até o registro da chegada, e não mais "até a confirmação".
- A estória e o caso de uso de cada um desses RFs acompanham (itens 7 e 10).
- Os textos das áreas B e C que citam a chegada (RF-B8, US-B8 e RF-C8) falam em "registro do AIBT" e não mudam.
- A fronteira de papéis do item 5 continua valendo: o operador executa e registra; o Coordenador de Turnaround coordena e corrige.

---

## Ligações

- **Pesquisa:** [marcos-e-horarios](../../pesquisa/topicos/marcos-e-horarios.md), [papeis-e-atores](../../pesquisa/topicos/papeis-e-atores.md)
- **Itens da especificação:** [Item 6 — Requisitos Funcionais](../../especificacao/06-requisitos-funcionais/00-item.md), [Item 7 — Estórias de Usuário](../../especificacao/07-estorias-de-usuario/00-item.md), [Item 10 — Especificações de Caso de Uso](../../especificacao/10-especificacoes-de-caso-de-uso/00-item.md)
- **Áreas do plano RA1:** [Área A — Acesso e planejamento](../../especificacao/06-requisitos-funcionais/area-a.md)
- **Outras decisões:** [D4](0004-quatro-atores-e-autoridade-de-liberacao.md), [D7](0007-dados-do-operador-e-qr-code.md)
- **Fontes citadas:** 2, 4 (em [fontes.md](../../pesquisa/fontes.md))
- **Índice das decisões:** [README.md](README.md) · **Contexto geral:** [CONTEXT.md](../../CONTEXT.md)
