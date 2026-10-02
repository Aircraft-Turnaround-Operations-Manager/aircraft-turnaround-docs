---
id: assaia
titulo: "Ficha — Assaia (ApronAI e TurnaroundControl)"
tipo: similar-ficha
secao_original: "3.2"
itens_template: [3]
areas: []
decisoes: [D7]
fontes: [19, 39, 40, 41, 42]
relacionados: [matriz-comparativa, lacunas-e-diferencial, similares]
status: vigente
atualizado: 2026-10-01
---
# Ficha 1 — Assaia (ApronAI e TurnaroundControl)

> Base de conhecimento do projeto · origem: seção 3.2 do [relatório consolidado](../01-referencias-setor-e-similares.md) (congelado em 01/10/2026) · fontes numeradas em [fontes.md](../fontes.md) · convenções [Fato]/[Inferência] e índices no [mapa da pesquisa](../README.md).

> **Decisões vigentes (prevalecem sobre o texto abaixo):** [D7 — Dados registrados pelo operador, inclusive QR Code lido pelo celular](../../docs/adr/0007-dados-do-operador-e-qr-code.md).
>
> Câmeras fixas e visão computacional ficam fora; a câmera do celular para ler QR Code é permitida (D7).


| Campo | Registro |
|---|---|
| Produto e fornecedor | ApronAI e TurnaroundControl (também ResourceManager, SafetyControl, EmissionsControl). Assaia International AG, Zurique, **Suíça**, com escritórios na Alemanha e nos EUA. https://www.assaia.com [Fato][39] |
| Público-alvo | "Airports, airlines, ground handlers" [Fato][39]; o TurnaroundControl cita companhias aéreas, *ground handlers*, "departure coordinators" e "gate managers", com clientes como United e Alaska Airlines [Fato][40]. |
| Problema que resolve | "Optimize aircraft turnarounds with AI & computer vision." [Fato][39] |
| Funcionalidades | Câmeras no pátio geram "accurate timestamps for turnaround events" em tempo real [Fato][41]; painel com widgets coloridos por atividade em vários portões e vídeo ao vivo; *watchlist* de turnarounds; alertas com "Airline-specific business logic"; previsão de off-block (POBT) e de prontidão (PRDT); fila de partida; mapa multi-aeroporto; integra progresso do embarque e leitura de bagagem [Fato][40]; auditoria de SLA e detecção de violações de segurança [Fato][39]. |
| Como trata atrasos e exceções | Notificações instantâneas, com foco em "handling exceptions, rather than multitasking" [Fato][40]. Exemplo real de regra: alerta quando a "cleaning team has not been detected on the aircraft stand within 3 minutes after passenger offboarding has ended"; o alerta vai para um "AOC operative who then calls the respective ground handler service provider" [Fato][42]. |
| Fonte do dado operacional | Câmeras e visão computacional [Fato][39][41], mais integrações (embarque, bagagem) [Fato][40]. |
| Métricas divulgadas — [Fato] (declarado pelo fornecedor) | +17% de pontualidade, −5 min de atraso em solo, −50% de comportamento inseguro; 2.895.340 turnarounds monitorados em 31 aeroportos [39]; Alaska −3,9 min e United −2 min de atraso médio em solo [40]; turnaround de ~40 para ~35 min (>12%) em um aeroporto médio [42]. |
| Relação com A-CDM | Declara melhorar o A-CDM "through more accurate predictive off block time (POBT)" [Fato][39]; compara o TOBT manual com o POBT [Fato][19]. |
| O que vale incorporar [Inferência] | (1) Regra de alerta por dependência: "sucessora não iniciada X min após o fim da predecessora"; (2) *watchlist* de turnarounds em risco; (3) status por cor por atividade; (4) projeção de prontidão (equivalente ao PRDT) recalculada a cada evento. |
| O que fica fora do nosso escopo [Inferência] | Visão computacional e câmeras (exige infraestrutura; o MVP usa registro do operador; a câmera do celular para ler QR Code é permitida pela decisão D7); monitoramento de emissões; detecção de segurança por vídeo. |

---

## Ligações

- **Decisões:** [D7](../../docs/adr/0007-dados-do-operador-e-qr-code.md)
- **Itens da especificação:** [Item 3 — Visão do Produto](../../especificacao/03-visao-do-produto.md)
- **Relacionados:** [matriz-comparativa](matriz-comparativa.md), [lacunas-e-diferencial](lacunas-e-diferencial.md), [similares](README.md)
- **Fontes citadas:** 19, 39, 40, 41, 42 (em [fontes.md](../fontes.md))
- **Contexto geral:** [CONTEXT.md](../../CONTEXT.md) · [mapa da pesquisa](../README.md)
