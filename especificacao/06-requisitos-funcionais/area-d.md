| # | REQUISITO FUNCIONAL | ATOR / USUÁRIO | OBJETIVO | SPRINT |
|---|---|---|---|---|
| RF-D1 | O sistema deve permitir ao Coordenador de Turnaround abrir uma exceção em um turnaround, informando a tarefa afetada, a causa pelo código da tabela de códigos de atraso da Agência Nacional de Aviação Civil (ANAC) [62] e uma descrição, e levar o turnaround ao estado "Em exceção". O registro grava o autor e o horário. | Coordenador de Turnaround | Obj. 3 | |
| RF-D2 | O sistema deve permitir ao Coordenador de Turnaround reatribuir uma tarefa ainda não concluída a outro Operador de Solo/Rampa da mesma equipe que esteja disponível (sem tarefa em execução), registrando o motivo, o autor e o horário e avisando os dois operadores. | Coordenador de Turnaround | Obj. 2 e 3 | |
| RF-D3 | O sistema deve permitir ao Coordenador de Turnaround registrar, para cada alerta recebido, a ação tomada (reatribuir tarefa, replanejar, atualizar a previsão ou abrir exceção), com autor e horário, encerrando o alerta. | Coordenador de Turnaround | Obj. 3 | |
| RF-D4 | O sistema deve permitir à Autoridade de Liberação confirmar a prontidão da aeronave, registrando o horário real de prontidão (ARDT) [2], em um turnaround no estado "Pronto para liberação", levando-o a "Liberado"; a confirmação é recusada enquanto houver tarefa obrigatória pendente ou exceção aberta, e a decisão é registrada com autor e horário. | Autoridade de Liberação | Obj. 3 | |
| RF-D5 | O sistema deve permitir ao Coordenador de Turnaround encerrar uma exceção, registrando a solução, o autor e o horário, e devolver o turnaround ao estado anterior à exceção quando não houver outra exceção aberta. | Coordenador de Turnaround | Obj. 3 | |
| RF-D6 | O sistema deve solicitar ao Coordenador de Turnaround a atualização do horário-alvo de prontidão (TOBT) [2] quando a projeção de prontidão se afastar 5 minutos ou mais do TOBT vigente, para mais ou para menos [8][9], e registrar o valor anterior, o novo valor, o autor e o horário. | Coordenador de Turnaround | Obj. 1 | |
| RF-D7 | O sistema deve permitir ao Coordenador de Turnaround alterar a janela planejada ou as dependências das tarefas ainda não iniciadas, registrando autor e horário, e recalcular a projeção de prontidão e o caminho crítico após a alteração. | Coordenador de Turnaround | Obj. 1 e 3 | |
| RF-D8 | O sistema deve permitir ao Coordenador de Turnaround consultar, ao reatribuir uma tarefa, a lista dos operadores da mesma equipe da tarefa que estão disponíveis (sem tarefa em execução), ordenada pelo tempo desde a última tarefa concluída por cada um. | Coordenador de Turnaround | Obj. 2 | |
| RF-D9 | O sistema deve permitir ao Operador de Solo/Rampa registrar o horário real de saída da posição (AOBT) [2] de um turnaround no estado "Liberado", depois da autorização de acionamento e push-back recebida fora do sistema, e com isso encerrar o turnaround no estado "Fora de bloco", recusando novos registros de tarefas e mantendo o histórico completo para consulta. O registro grava o autor e o horário. | Operador de Solo/Rampa | Obj. 3 | |

**Base dos RFs da área D.**

| RF | Base |
|---|---|
| RF-D1 | [Inferência] exceção com causa pela tabela completa da ANAC, 72 códigos (ADR-0006; base: [16][62]); estado "Em exceção" do `CONTEXT.md`. |
| RF-D2 | [Fato] redistribuição de equipe entre tarefas e turnarounds nos similares [45][46][54]; equipe do operador como dado (ADR-0010). |
| RF-D3 | [Inferência] fluxo "alerta → ação" (base: [42][54]); sustenta a meta do objetivo 3 de 90% dos alertas críticos com ação registrada em até 2 minutos. |
| RF-D4 | [Fato] definição do marco *Aircraft Ready* [2]; [Inferência] recusar a confirmação com pendência ou exceção aberta é regra do projeto (ADR-0004) e sustenta a meta de 0 liberações com pendência. |
| RF-D5 | [Inferência] ciclo de vida da exceção, regra do projeto: sem encerramento, a liberação ficaria bloqueada pelo RF-D4. |
| RF-D6 | [Fato] atualização obrigatória do TOBT quando a previsão difere em 5 minutos ou mais [8][9][10][13]; antecipação de 5 minutos ou mais (ADR-0003). |
| RF-D7 | [Inferência] replanejamento pelo Coordenador de Turnaround, como no quadro "Faz" do item 2; caminho crítico recalculado a cada evento (base: [24][45]). |
| RF-D8 | [Fato] apoio do sistema à alocação de recursos em tempo real nos similares [45][46][54]; [Inferência] o critério de ordenação é regra do projeto. |
| RF-D9 | [Fato] marco AOBT, registrado na saída da posição [2]; no BPMN do item 4, quem registra é o Operador de Solo/Rampa; [Inferência] o encerramento do turnaround a partir do AOBT é regra do projeto. |

Fontes citadas: [2], [8], [9], [10], [13], [16], [24], [42], [45], [46], [54] e [62], conforme a numeração de `pesquisa/fontes.md`.
