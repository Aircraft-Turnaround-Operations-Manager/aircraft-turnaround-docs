# 3 VISÃO DO PRODUTO

**NOME DO PRODUTO:** Aircraft Turnaround Orchestration System

| PROBLEMAS | EXPECTATIVAS |
|---|---|
| **P1.** Desvios no turnaround são percebidos tarde e se propagam para os voos seguintes: o atraso reacionário respondeu por 46% dos minutos de atraso na Europa em 2023, e só 67,9% das partidas saíram em até 15 minutos do horário programado [16]. | **E1.** Desvios detectados durante a operação: a cada registro, a projeção de prontidão e o caminho crítico são recalculados, e o Coordenador de Turnaround é alertado enquanto ainda há tempo de agir. *(responde a P1 · Objetivo 3)* |
| **P2.** O horário-alvo de prontidão (TOBT) é pouco confiável: mesmo onde há tomada de decisão colaborativa em aeroportos (A-CDM) resta imprecisão relevante nos marcos de saída [14], e há relatos de menos de 60% de acerto dentro de 5 minutos em grandes aeroportos (declarado pelo fornecedor) [18]. | **E2.** Turnaround executado dentro do planejado e medido com a régua do setor: prontidão até o TOBT planejado + 5 minutos, com cada atividade acompanhada em relação à sua janela. *(responde a P2 · Objetivo 1)* |
| **P3.** Equipes diferentes executam atividades em paralelo, com dependências entre si, sem uma visão compartilhada. A coordenação depende de rádio, que às vezes falha e deixa informações se perderem, o que gera atrasos, e quem coordena não consegue acompanhar fisicamente todas as operações (declarado pelo fornecedor) [65]; o congestionamento de rádio está entre as pressões das operações de rampa [66]. O embarque, de duração variável, costuma estar no caminho crítico [20]. | **E3.** Uma visão única de tarefas, responsáveis, dependências e estados, atualizada no painel em até 5 segundos após cada registro. *(responde a P3 · Objetivo 2)* |
| **P4.** Nas soluções de monitoramento automático, o andamento vem de câmeras ou sensores instalados no pátio [41][49], o que exige infraestrutura e não registra quem executou cada tarefa. | **E4.** Andamento registrado pelo próprio Operador de Solo/Rampa no celular, inclusive pela leitura de QR Code, sem infraestrutura instalada no pátio. *(responde a P4 · ADR-0007)* |
| **P5.** A prontidão da aeronave (*Aircraft Ready*) exige o atendimento em solo concluído, portas fechadas e ponte retirada [2], mas não há garantia formal de que nenhuma tarefa obrigatória ou exceção ficou pendente na liberação. | **E5.** Liberação bloqueada enquanto houver tarefa obrigatória pendente ou exceção aberta, com a decisão da Autoridade de Liberação registrada com autor e horário. *(responde a P5 · Objetivo 3)* |

**VISÃO DE PRODUTO**

**NOME DO PRODUTO:** Aircraft Turnaround Orchestration System

| | |
|---|---|
| **CLIENTE-ALVO** | Empresas de *handling* (atendimento em solo) e companhias aéreas, responsáveis pelo TOBT no A-CDM [2][5]. Usuários diretos: Operador de Solo/Rampa, Coordenador de Turnaround e Autoridade de Liberação. Público secundário: centro de operações do aeroporto [2]. |
| **CATEGORIA-SEGMENTO** | Software de gestão de operações de solo / gestão de turnaround (*turnaround management*), mesma categoria de INFORM GroundStar, Assaia e ADB SAFEGATE [39][44][49], no segmento de operações aeroportuárias da aviação comercial. |
| **BENEFÍCIO-CHAVE** | Aeronave pronta para liberação no horário-alvo (TOBT), com os desvios detectados e tratados durante a operação, e não depois dela. |
| **DIFERENCIAL-CHAVE** | Recursos não documentados nas fontes públicas dos similares analisados [39]–[55]: (1) cada turnaround é um grafo de tarefas com dependências, com caminho crítico e projeção de prontidão recalculados a cada registro e exibidos no painel em até 5 segundos; (2) bloqueio da liberação enquanto houver tarefa obrigatória pendente ou exceção aberta; (3) registro feito pelo operador, inclusive com confirmação de tarefas por QR Code no celular (por exemplo, a limpeza da cabine por zona), sem sensores da aeronave nem câmeras no pátio; (4) aderência medida com a régua do setor, prontidão até TOBT + 5 minutos [2]. |
| **META-VALOR** | Pelo menos 80% dos turnarounds prontos para liberação até o TOBT planejado + 5 minutos e pelo menos 80% das atividades iniciadas e concluídas dentro das janelas planejadas, metas alinhadas às referências de mercado [7] (e, como analogia, [15]); e 0 liberações com tarefa obrigatória pendente ou exceção não resolvida. |

Fontes citadas: [2], [5], [7], [14], [15], [16], [18], [20], [39] a [55], [65] e [66], conforme a numeração de `pesquisa/fontes.md`.
