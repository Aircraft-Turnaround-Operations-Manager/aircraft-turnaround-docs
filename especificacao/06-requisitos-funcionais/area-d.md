| # | REQUISITO FUNCIONAL | ATOR / USUÁRIO | OBJETIVO | SPRINT |
|---|---|---|---|---|
| RF-D1 | O sistema deve permitir ao Coordenador de Turnaround abrir uma exceção em um turnaround, informando a tarefa afetada, a causa pelo código da tabela de códigos de atraso da Agência Nacional de Aviação Civil (ANAC) [62] e uma descrição, e levar o turnaround ao estado "Em exceção". | Coordenador de Turnaround | Obj. 3 | |
| RF-D2 | O sistema deve permitir ao Coordenador de Turnaround reatribuir uma tarefa ainda não concluída a outro Operador de Solo/Rampa da mesma equipe que esteja disponível (sem tarefa em execução), registrando o motivo, o autor e o horário e avisando os dois operadores. | Coordenador de Turnaround | Obj. 2 e 3 | |
| RF-D3 | O sistema deve permitir ao Coordenador de Turnaround registrar, para cada alerta recebido, a ação tomada (reatribuir tarefa, replanejar, atualizar a previsão ou abrir exceção), com autor e horário, encerrando o alerta. | Coordenador de Turnaround | Obj. 3 | |
| RF-D4 | O sistema deve permitir à Autoridade de Liberação confirmar a prontidão da aeronave, registrando o horário real de prontidão (ARDT) [2], em um turnaround no estado "Pronto para liberação", levando-o a "Liberado"; a confirmação deve ser bloqueada enquanto houver tarefa obrigatória pendente ou exceção aberta, e a decisão é registrada com autor e horário. | Autoridade de Liberação | Obj. 3 | |
| RF-D5 | O sistema deve permitir ao Coordenador de Turnaround encerrar uma exceção, registrando a solução, o autor e o horário, e devolver o turnaround ao estado anterior à exceção quando não houver outra exceção aberta. | Coordenador de Turnaround | Obj. 3 | |
| RF-D6 | O sistema deve solicitar ao Coordenador de Turnaround a atualização do horário-alvo de prontidão (TOBT) [2] quando a projeção de prontidão se afastar 5 minutos ou mais do TOBT vigente, para mais ou para menos [8][9], e registrar o valor anterior, o novo valor, o autor e o horário. | Coordenador de Turnaround | Obj. 1 | |
| RF-D7 | O sistema deve permitir ao Coordenador de Turnaround alterar a janela planejada ou as dependências das tarefas ainda não iniciadas, registrando autor e horário, e recalcular a projeção de prontidão e o caminho crítico após a alteração. | Coordenador de Turnaround | Obj. 1 e 3 | |
| RF-D8 | O sistema deve apresentar ao Coordenador de Turnaround, ao reatribuir uma tarefa, a lista de operadores da mesma equipe da tarefa que estão disponíveis (sem tarefa em execução), ordenada pelo tempo desde a última tarefa concluída. | Motor de Eventos | Obj. 2 | |
| RF-D9 | O sistema deve encerrar o turnaround, levando-o ao estado "Fora de bloco", quando o horário real de saída da posição (AOBT) [2] for registrado, bloqueando novos registros de tarefas e mantendo o histórico completo para consulta. | Motor de Eventos | Obj. 3 | |

**Base dos RFs da área D.**

| RF | Base |
|---|---|
| RF-D1 | [Inferência] abertura de exceção com o código da tabela completa da ANAC, 72 códigos (ADR-0006; base: [16][62]); o estado lateral "Em exceção" é do projeto e segue os estados do `CONTEXT.md`. |
| RF-D2 | [Fato] redistribuição de equipe e de recursos entre tarefas [45][46][54]; equipe do operador como dado (ADR-0010); [Inferência] o critério de operador disponível (sem tarefa em execução) é regra do projeto. |
| RF-D3 | [Inferência] registro da ação tomada para cada alerta (base: [42][54]); sustenta a métrica do objetivo 3, de ação registrada em até 2 minutos para pelo menos 90% dos alertas críticos. |
| RF-D4 | [Inferência] liberação só com as condições do marco *Aircraft Ready* atendidas (base: [2]); o bloqueio com exceção aberta é regra do projeto; a Autoridade de Liberação é o representante da companhia aérea, e não a autorização do controle de tráfego aéreo (ADR-0004). |
| RF-D5 | [Inferência] encerramento da exceção com a solução registrada; regra do projeto, par do RF-D1. |
| RF-D6 | [Fato] atualização do TOBT quando a previsão se afasta 5 minutos ou mais [8][9][10][13]; vale para mais e para menos, inclusive na antecipação (ADR-0003). |
| RF-D7 | [Inferência] replanejamento de janelas e dependências pelo Coordenador de Turnaround, como no quadro "Faz" do item 2 (área D); o recálculo da projeção e do caminho crítico é da área C. |
| RF-D8 | [Fato] sugestão do sistema na redistribuição de recursos [45][46][54]; [Inferência] a ordenação pelo tempo desde a última tarefa concluída é regra do projeto. |
| RF-D9 | [Fato] registro da saída da posição (AOBT) e encerramento do turnaround [2]. |

Fontes citadas: [2], [8], [9], [10], [13], [16], [42], [45], [46], [54] e [62], conforme a numeração de `pesquisa/fontes.md`.
