# Ideias em estudo

> **Nada neste arquivo é requisito, decisão ou compromisso de entrega.** A especificação é o documento de compromisso do Aircraft Turnaround Orchestration System; o que está aqui fica de fora dela de propósito. Uma ideia só entra no plano depois de virar requisito funcional (RF) na especificação ou decisão em `docs/adr/`, por decisão do grupo. Até lá, não use estas ideias como base para escrever RF, estória, caso de uso ou protótipo.

Cada ideia diz de onde veio, o que é, por que está fora da especificação e o que falta para ela avançar.

## Visão 3D interativa do turnaround

- **Origem:** proposta do Rodrigo (`rdsalvesPUC`) em 11/11/2026, inspirada no vídeo de um sistema de gestão de armazém com cena 3D feita em React Three Fiber.
- **O que é:** uma **segunda visão**, dinâmica, do turnaround: a aeronave na posição e as tarefas acontecendo ao redor dela, com o estado de cada uma. Não substitui a interface principal de gestão; listas e tabelas, como as de tarefas e de alertas, continuam em 2D, onde são mais fáceis de ler.
- **Por que está fora da especificação:** o grupo decidiu que ela não entra nos RFs nem nos outros itens, porque a especificação é o documento de compromisso. Nenhum RF a cobre hoje. Pode virar apêndice no futuro.
- **Relação com o que já está decidido:** as telas do item 10 serviram à especificação e não são a interface final; a interface parte quase do zero no sprint 1 ([item 6, priorização](../especificacao/06-requisitos-funcionais/00-item.md)). O framework escolhido é o Angular ([ADR-0016](adr/0016-contrato-entre-os-servicos.md)), e não o React do vídeo de referência.
- **Para avançar:** quando o desenvolvimento começar, fazer uma prova de conceito com Three.js dentro do Angular. Se o grupo quiser a visão no produto, ela precisa antes de um RF ou de uma ADR.

## Ligações

- [CONTEXT.md](../CONTEXT.md)
- [ADR-0016 — Contrato entre os serviços](adr/0016-contrato-entre-os-servicos.md)
- [Item 6 — Requisitos funcionais, priorização](../especificacao/06-requisitos-funcionais/00-item.md)
