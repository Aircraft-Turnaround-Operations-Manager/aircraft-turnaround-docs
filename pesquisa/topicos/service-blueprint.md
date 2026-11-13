---
id: service-blueprint
titulo: "Blueprint do turnaround por serviço: os cinco conflitos da primeira divisão em microsserviços"
tipo: pesquisa-topico
itens_template: [12, 13, 14]
areas: [A, B, C, D]
decisoes: [D13, D14, D15, D16]
fontes: []
relacionados: [adr-0015, adr-0016, adr-0013, adr-0014, marcos-e-horarios, atividades-e-dependencias, papeis-e-atores]
status: vigente
atualizado: 2026-11-13
---
# Blueprint do turnaround por serviço

> Base de conhecimento do projeto · revisão momento a momento feita em 30/10/2026 para decidir a divisão em microsserviços · versão interativa no [artefato publicado](https://claude.ai/artifact/8sGNer92aRqri469tj5i7V) · convenções e índices no [mapa da pesquisa](../README.md).

> **Decisão vigente (prevalece sobre o texto abaixo):** [D15 — Divisão em quatro microsserviços](../../docs/adr/0015-divisao-em-microsservicos.md), complementada pela [D16 — Contrato entre os serviços](../../docs/adr/0016-contrato-entre-os-servicos.md). Este arquivo é o material de construção da D15: guarda a análise que levou a ela. As regras de quem é dono de cada dado e de quando usar aviso ou pedido estão na ADR.

## Para que serve

A primeira proposta dividia os serviços pelas áreas A a D do RA1, e todos os serviços trocavam só avisos. O blueprint percorre o turnaround do início ao fim, em oito momentos, e mostra, em cada um, qual serviço grava o quê e que mensagem vai de um serviço para outro. Em cinco momentos, dois ou mais serviços disputavam o mesmo dado. Os cinco conflitos têm a mesma causa: a tarefa e o estado do turnaround estavam espalhados por serviços diferentes.

**Use este arquivo** para entender o porquê da D15 e para resolver um caso entre serviços que o blueprint não desenhou: aplique as regras da ADR-0015 do mesmo jeito que elas foram aplicadas aqui.

## Quatro ideias de base

- **Serviço:** programa separado, com banco de dados próprio. Um serviço não lê o banco de outro; para saber algo, pergunta ou é avisado.
- **Dono do dado:** o serviço que guarda o dado original. Qualquer outro tem uma cópia, que pode estar atrasada.
- **Aviso (evento):** mensagem que diz "isto aconteceu". Quem envia não espera; quem recebe pode receber um pouco depois.
- **Pedido (comando):** pergunta que espera resposta ("posso fazer isto?"). Quem pede espera o dono do dado responder.

O celular do Operador de Solo/Rampa é só a tela: pode mandar um registro para qualquer serviço. A questão é qual serviço deve recebê-lo.

## Os oito momentos

Serviços: Cadastro e Planejamento (Cad.), Execução em Solo (Exe.), Monitoramento (Mon.), Exceções e Liberação (Exc.). Numeração final dos RFs.

| # | Momento | Estado do turnaround | Primeira proposta | Com a correção (D15) |
|---|---|---|---|---|
| 1 | Antes da chegada | — | Cad. abre o turnaround e confirma o plano (RF-3, RF-5); aviso ao Mon., que confere se o horário estimado de chegada à posição (EIBT) somado ao tempo mínimo de turnaround (MTTT) cabe antes do horário-alvo de prontidão (TOBT) (RF-29) | Igual; o plano confirmado passa para a Exe. |
| 2 | Chegada | Em solo | Cad. grava o horário real de chegada à posição (AIBT) (RF-12) e avisa a Exe., que muda o estado e libera as tarefas (RF-21) | **Conflito 1.** A Exe. grava o AIBT, muda para Em solo e deixa as tarefas Pronta na mesma gravação (RF-12, RF-21); aviso ao Mon. |
| 3 | Tarefas em andamento | Operações em andamento | Exe. registra início, pausa e conclusão e grava o início real do atendimento em solo (ACGT) (RF-15 a RF-20); avisos ao Mon. (RF-22 a RF-28) | Igual (sem conflito) |
| 4 | Reatribuir ou replanejar | Operações em andamento | Exc. decide (RF-37, RF-38, RF-42) e avisa o Cad. (plano) e a Exe. (tarefa) | **Conflito 2.** A Exe. é a única dona da tarefa durante o turnaround; a Exc. faz um pedido e espera a resposta; o Cad. fica só com o modelo e o plano inicial |
| 5 | Exceção | Em exceção | Exc. abre a exceção (RF-36) e avisa a Exe. para mudar o estado | **Conflito 3.** A Exc. pede à Exe. que aplique Em exceção e só confirma ao Coordenador de Turnaround com a resposta |
| 6 | Última tarefa | Pronto para liberação | Exe. grava o fim real do atendimento em solo (AEGT) e muda o estado (RF-20, RF-21); aviso ao Mon. | Igual (sem conflito) |
| 7 | Liberação | Liberado | Exc. decide com uma cópia das tarefas montada pelos avisos (RF-39) | **Conflito 4.** A Exc. confere as exceções e pede à Exe. a liberação; a Exe. confere estado e tarefas no dado original; só com o "sim" a Exc. grava o horário real de prontidão (ARDT) |
| 8 | Saída | Fora de bloco | Exc. grava o horário real de saída da posição (AOBT) (RF-44) e avisa a Exe. para bloquear novos registros | **Conflito 5.** A Exe. grava o AOBT, muda para Fora de bloco e bloqueia novos registros na mesma gravação; aviso ao Mon. (RF-34) |

## Os cinco conflitos

Exemplos com o voo fictício 1234. Os segundos servem só para mostrar a ordem dos fatos; um aviso real costuma levar bem menos.

1. **Chegada: o AIBT e as tarefas em serviços diferentes (leve).** O Cadastro grava a chegada às 14:02:00 e responde "registrado"; o aviso ainda está a caminho, e às 14:02:02 o operador abre a lista e o desembarque continua Aguardando. Se a entrega de avisos falhar, a espera aumenta. **Correção:** RF-12 e RF-13 vão para a Execução em Solo. **Custo:** a área B assume dois RFs da área A.
2. **Reatribuir ou replanejar: três serviços mexem na mesma tarefa (média).** O responsável fica em dois bancos, e a decisão de mudá-lo, num terceiro. O Coordenador de Turnaround troca a limpeza de Ana para Bruno às 14:20:00; às 14:20:01 Ana toca em Iniciar e a Execução, sem o aviso, aceita; às 14:20:02 Bruno também recebe a tarefa. **Correção:** depois da confirmação do plano, a Execução é a única dona das tarefas; a Exceções e Liberação faz um pedido e espera. **Custo:** a Execução passa a receber esses pedidos.
3. **Exceção: a ordem de chegada muda o resultado (média).** O RF-21 só leva a Pronto para liberação quem está em Operações em andamento. Se a última tarefa terminar antes de o aviso da exceção chegar, o painel mostra "pronto" com um problema aberto. **Correção:** toda mudança de estado do turnaround é um pedido com resposta, e a Execução atende um de cada vez; avisos só informam o que já aconteceu. **Custo:** com a Execução fora do ar, não se abre exceção até ela voltar.
4. **Liberação: decidir sem o dado original (grave).** Às 14:50:00 o Coordenador de Turnaround inclui uma tarefa obrigatória sob demanda (RF-42); o aviso atrasa; às 14:50:02 a Autoridade de Liberação confirma com a cópia, e o sistema libera a aeronave com tarefa obrigatória pendente. A meta do item 1 proíbe isso (0 liberações com tarefa obrigatória pendente). **Correção:** a decisão final fica com quem tem o dado original; a Execução confere e responde, sem cópia. **Custo:** a liberação depende de a Execução estar no ar.
5. **Saída: o AOBT e o bloqueio em serviços diferentes (leve).** O AOBT é gravado às 15:00:00; às 15:00:02 outro operador registra uma tarefa, e a Execução, sem o aviso, aceita num turnaround encerrado, o que o RF-44 proíbe. **Correção:** RF-44 vai para a Execução em Solo. **Custo:** a área B assume um RF da área D, com o UC37.

A gravidade é avaliação da revisão, não medida ([Inferência]).

## O que mudou na divisão

| Serviço | RFs na primeira proposta | RFs com a correção |
|---|---|---|
| Cadastro e Planejamento | 13 | 11 |
| Execução em Solo | 8 | 11 |
| Monitoramento | 14 | 14 |
| Exceções e Liberação | 9 | 8 |

Saem RF-12 e RF-13 do Cadastro e RF-44 da Exceções e Liberação; todos vão para a Execução em Solo, que também passa a atender os pedidos de RF-37, RF-39 e RF-42.

## O que o blueprint não desenhou

Os oito momentos não cobrem todos os casos entre serviços. Exemplo: o encerramento de um alerta quando a ação é registrada (RF-38). Esses casos não ficam em aberto: as regras da ADR-0015 os resolvem. O alerta é do Monitoramento, e a ação foi registrada pela Exceções e Liberação; como a ação já aconteceu, ela vai num **aviso** (regra 2), e o Monitoramento encerra o alerta. Só fica para decidir o que as regras não cobrem, como o nome e os campos de um aviso.

---

## Ligações

- **Decisão que nasceu daqui:** [ADR-0015](../../docs/adr/0015-divisao-em-microsservicos.md) · **Contrato entre os serviços:** [ADR-0016](../../docs/adr/0016-contrato-entre-os-servicos.md)
- **Chegada registrada pelo operador:** [ADR-0013](../../docs/adr/0013-chegada-registrada-pelo-operador.md) · **Serviços sob demanda:** [ADR-0014](../../docs/adr/0014-servicos-sob-demanda.md)
- **Pesquisa relacionada:** [Marcos e horários](marcos-e-horarios.md) · [Atividades, paralelismo e dependências](atividades-e-dependencias.md) · [Papéis e atores](papeis-e-atores.md)
- **Itens da especificação:** [Item 12](../../especificacao/12-modelo-de-dados.md) · [Item 14](../../especificacao/14-diagramas-de-sequencia/00-item.md)
- **Mapa da pesquisa:** [README.md](../README.md) · **Contexto geral:** [CONTEXT.md](../../CONTEXT.md)
