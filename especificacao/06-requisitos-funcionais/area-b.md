| # | REQUISITO FUNCIONAL | ATOR / USUÁRIO | SPRINT |
|---|---|---|---|
| RF-5 | O sistema deve permitir ao Operador de Solo/Rampa consultar a lista das tarefas da sua equipe atribuídas a ele, exibindo, para cada tarefa, o turnaround (aeronave e posição), o estado da tarefa, a janela planejada de início e de fim e as tarefas predecessoras ainda não concluídas. | Operador de Solo/Rampa | Sprint 1 (prioridade alta) |
| RF-6 | O sistema deve permitir ao Operador de Solo/Rampa registrar o início de uma tarefa no estado "Pronta" e a conclusão de uma tarefa no estado "Em execução", gravando o autor e o horário de cada registro e recusando a conclusão de tarefa sem início registrado. O primeiro início registrado no turnaround marca o início real do atendimento em solo (ACGT), e o início da tarefa de embarque marca o início real do embarque (ASBT) [2][4]. | Operador de Solo/Rampa | Sprint 1 (prioridade alta) |
| RF-7 | O sistema deve permitir ao Operador de Solo/Rampa pausar uma tarefa no estado "Em execução", exigindo o código do motivo do impedimento da tabela de códigos de atraso da Agência Nacional de Aviação Civil (ANAC) [62], retomar a tarefa pausada e marcar como "Não aplicável" uma tarefa definida como dispensável no turnaround, exigindo uma justificativa escrita; cada registro grava o autor e o horário. | Operador de Solo/Rampa | Sprint 2 (prioridade alta) |
| RF-8 | O sistema deve permitir ao Operador de Solo/Rampa confirmar a execução de uma tarefa pela leitura, com a câmera do celular, do QR Code fixado no ponto da aeronave correspondente (por exemplo, zona, fileira ou assento da cabine na limpeza), registrando cada leitura com autor e horário e recusando o QR Code que não pertença a uma tarefa da sua equipe atribuída a ele no turnaround. | Operador de Solo/Rampa | Sprint 3 (prioridade média) |

**Rastreabilidade da área B.**

| RF | Objetivo (item 1) | Base |
|---|---|---|
| RF-5 | 2. Sincronizar equipes, recursos e atividades paralelas | [Fato] consulta das próprias tarefas pelo operador em app/web [43][46]; equipe do operador como dado (ADR-0010). |
| RF-6 | 1. Assegurar a precisão temporal do turnaround; 2. Sincronizar equipes, recursos e atividades paralelas | [Fato] marcos ACGT e ASBT [2][4]; [Inferência] registro de início e conclusão por tarefa (base: [2][40]); a recusa de conclusão sem início atende à métrica do objetivo 2. |
| RF-7 | 2. Sincronizar equipes, recursos e atividades paralelas; 3. Antecipar e coordenar o tratamento de desvios operacionais | [Inferência] pausa e "Não aplicável" com justificativa (pausa não descrita nas fontes); código do impedimento pela tabela completa da ANAC, 72 códigos (ADR-0006) [62]. |
| RF-8 | 2. Sincronizar equipes, recursos e atividades paralelas | [Inferência] confirmação por QR Code lido pelo celular (ADR-0007; base: [42][63][64]). |

**Priorização.** RF-5 e RF-6 estão na Sprint 1 porque sem eles nenhuma tarefa sai de "Pronta" e o painel, os cálculos e os alertas da área C ficam sem dados. RF-7 vem na Sprint 2 porque trata os desvios da execução e alimenta as exceções da área D. RF-8 fica na Sprint 3 porque é uma forma adicional de confirmar tarefas que já podem ser concluídas pelo RF-6.

Fontes citadas: [2], [4], [40], [42], [43], [46], [62], [63] e [64], conforme a numeração de `pesquisa/fontes.md`.
