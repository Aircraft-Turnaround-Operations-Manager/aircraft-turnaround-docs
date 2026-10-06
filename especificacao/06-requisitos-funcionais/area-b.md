| # | REQUISITO FUNCIONAL | ATOR / USUÁRIO | OBJETIVO | SPRINT |
|---|---|---|---|---|
| RF-5 | O sistema deve permitir ao Operador de Solo/Rampa consultar a lista das tarefas da sua equipe atribuídas a ele, exibindo, para cada tarefa, o turnaround (aeronave e posição), o estado da tarefa, a janela planejada de início e de fim e as tarefas predecessoras ainda não concluídas. | Operador de Solo/Rampa | Obj. 2 | |
| RF-6 | O sistema deve permitir ao Operador de Solo/Rampa registrar a execução de uma tarefa da sua equipe atribuída a ele: o início, aceito só quando a tarefa está no estado "Pronta", e a conclusão, aceita só quando a tarefa está no estado "Em execução". Cada registro grava o autor e o horário. O primeiro início registrado no turnaround marca o início real do atendimento em solo (ACGT), o início da tarefa de embarque marca o início real do embarque (ASBT) e a conclusão da última tarefa obrigatória marca o fim real do atendimento em solo (AEGT) [2][4]. | Operador de Solo/Rampa | Obj. 1 e 2 | |
| RF-7 | O sistema deve permitir ao Operador de Solo/Rampa registrar um desvio na execução de uma tarefa da sua equipe atribuída a ele: a pausa, aceita só quando a tarefa está no estado "Em execução", com justificativa e, quando houver impedimento, com o código do motivo escolhido na tabela de códigos de atraso da Agência Nacional de Aviação Civil (ANAC) [62], que leva a tarefa ao estado "Pausada", e a retomada, que a devolve ao estado "Em execução"; ou a marcação "Não aplicável", aceita só antes do início da tarefa, quando o modelo de tarefas do turnaround permite essa marcação para ela, e com justificativa escrita. Cada registro grava o autor e o horário. | Operador de Solo/Rampa | Obj. 2 e 3 | |
| RF-8 | O sistema deve permitir ao Operador de Solo/Rampa confirmar a execução de uma tarefa da sua equipe atribuída a ele pela leitura, com a câmera do celular, do QR Code fixado no ponto da aeronave correspondente (por exemplo, zona, fileira ou assento da cabine na limpeza). Cada leitura grava o autor e o horário, e o sistema recusa o QR Code que não pertença a uma tarefa da sua equipe atribuída a ele no turnaround. | Operador de Solo/Rampa | Obj. 2 | |
| RF-B5 | O sistema deve propagar o estado das tarefas e do turnaround a cada registro: quando uma tarefa passa para "Concluída" ou "Não aplicável", cada tarefa sucessora cujas predecessoras estejam todas nesses dois estados passa de "Aguardando" para "Pronta"; quando todas as tarefas obrigatórias do turnaround estão nesses dois estados, o turnaround passa de "Operações em andamento" para "Pronto para liberação". Cada mudança de estado feita pela propagação é gravada com o horário e com o registro que a causou. | Motor de Eventos | Obj. 2 | |

<!-- RF-B5: numeração provisória. A numeração definitiva segue a regra de numeração por área que está sendo atualizada no plano de tarefas e no README. -->

**Base dos RFs da área B.**

| RF | Base |
|---|---|
| RF-5 | [Fato] consulta das próprias tarefas pelo operador em app/web [43][46]; equipe do operador como dado (ADR-0010). |
| RF-6 | [Fato] marcos ACGT, ASBT e AEGT [2][4]; [Inferência] registro de início e conclusão por tarefa (base: [2][40]); aceitar a conclusão só de tarefa "Em execução" impede conclusão sem início, como pede a métrica do objetivo 2. |
| RF-7 | [Inferência] pausa e "Não aplicável" com justificativa (pausa não descrita nas fontes); justificativa em toda pausa, como nos itens 2 e 5; código do impedimento pela tabela completa da ANAC, 72 códigos (ADR-0006) [62]; tarefas que admitem "Não aplicável" definidas no modelo de tarefas da área A (base: [22][45]). |
| RF-8 | [Inferência] confirmação por QR Code lido pelo celular (ADR-0007; base: [42][63][64]). |
| RF-B5 | [Fato] dependências entre as atividades do turnaround, como a limpeza da cabine, que só começa depois do desembarque [22]; quadro "Faz" do item 2, que atribui a propagação de estado à área B; [Inferência] a regra de passagem para "Pronta" e para "Pronto para liberação" é do projeto e segue os estados do `CONTEXT.md`. |

Fontes citadas: [2], [4], [22], [40], [42], [43], [45], [46], [62], [63] e [64], conforme a numeração de `pesquisa/fontes.md`.
