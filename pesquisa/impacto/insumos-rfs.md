---
id: insumos-rfs
titulo: "Insumos para os RFs, por área (seção 4.3)"
tipo: impacto
secao_original: "4.3"
itens_template: [6, 7, 9, 10]
areas: [A, B, C, D]
decisoes: [D3, D5, D6, D7]
fontes: [2, 3, 4, 7, 8, 9, 10, 13, 16, 20, 22, 24, 26, 27, 40, 42, 43, 44, 45, 46, 48, 51, 54, 62, 63, 64]
relacionados: [atividades-e-dependencias, tolerancias-e-indicadores, codigos-de-atraso, impacto-por-item]
status: vigente
atualizado: 2026-10-01
---
# Insumos para os RFs, por área (seção 4.3)

> Base de conhecimento do projeto · origem: seção 4.3 do [relatório consolidado](../01-referencias-setor-e-similares.md) (congelado em 01/10/2026) · fontes numeradas em [fontes.md](../fontes.md) · convenções [Fato]/[Inferência] e índices no [mapa da pesquisa](../README.md).

> **Decisões vigentes (prevalecem sobre o texto abaixo):** [D3 — Antecipação de 5 min ou mais exige atualizar a previsão](../../docs/adr/0003-atualizar-previsao-na-antecipacao.md); [D5 — Abastecimento com passageiros a bordo: regra configurável por operador](../../docs/adr/0005-abastecimento-com-passageiros-configuravel.md); [D6 — Códigos de atraso: tabela completa da ANAC (72 códigos)](../../docs/adr/0006-codigos-de-atraso-tabela-anac.md); [D7 — Dados registrados pelo operador, inclusive QR Code lido pelo celular](../../docs/adr/0007-dados-do-operador-e-qr-code.md).
>
> Linhas atualizadas com as decisões D3, D5, D6 e D7; a linha de QR Code (área B) é nova.


Capacidades observadas no setor e nos similares. **Não** são RFs redigidos. Na coluna Fonte, **[Fato]** = a capacidade aparece descrita na fonte (declarado pelo fornecedor, quando a fonte é de empresa); **[Inferência] (base: [n])** = proposta deste relatório apoiada na fonte; **[Inferência]** sozinho = sem fonte direta.

| Área | Capacidade observada | Fonte |
|---|---|---|
| **A** — Acesso e planejamento | Perfis de acesso e visões configuráveis por papel; gestão de usuários, perfis e equipes pelo Administrador do Sistema e autenticação pelo ator abstrato Usuário ([D10](../../docs/adr/0010-administrador-usuario-e-equipe-do-operador.md)) | [Fato][51] |
| A | Abrir o turnaround a partir do par chegada/partida, com horários de referência (SIBT/SOBT, EIBT, TOBT) | [Inferência] (base: [2][4]) |
| A | Calcular o TOBT inicial como o mais tarde entre EIBT + MTTT e EOBT | [Fato][3] |
| A | Modelo (template) de tarefas por tipo de aeronave/serviço, com dependências e marcação de "Não aplicável" | [Inferência] (base: [22][45]) |
| A | Regra configurável "abastecimento com passageiros a bordo permitido?" | [Inferência] (decisão D5; base: [26][27]) |
| A | Checagem de viabilidade na abertura: EIBT + MTTT > TOBT → turnaround "sob estresse" | [Fato][3][7] |
| **B** — Execução em solo | Operador consulta as próprias tarefas em app/web | [Fato][43][46] |
| B | Iniciar, pausar e concluir tarefa com horário registrado | [Inferência] (base: registro de horários dos marcos [2] e status por atividade [40]; pausa não descrita nas fontes) |
| B | Registrar marcos: início do atendimento (ACGT), início do embarque (ASBT), fim do atendimento (AEGT) | [Fato][2][4] |
| B | Marcar tarefa "Não aplicável" com justificativa | [Inferência] |
| B | Confirmar tarefa por leitura de QR Code no celular (ex.: limpeza por assento, fileira ou zona) | [Inferência] (decisão D7; base: [42][63][64]) |
| B | Registrar impedimento com código da tabela da ANAC (72 códigos; siglas da IATA AHM 730) | [Inferência] (decisão D6; base: [16][62]) |
| **C** — Monitoramento | Painel multi-turnaround com status por cor e *watchlist* | [Fato][40][51] |
| C | Linha do tempo de marcos por turnaround | [Fato][51] |
| C | Projeção de prontidão recalculada a cada evento e comparada ao TOBT | [Fato][40][44][48] |
| C | Cálculo do impacto de um atraso nos processos dependentes | [Fato][45] |
| C | Caminho crítico destacado por turnaround — conceito da literatura [20][24]; **não** documentado nos similares ([Lacunas e diferencial](../similares/lacunas-e-diferencial.md)) | [Inferência] |
| C | Alerta: sucessora não iniciada X min após o fim da predecessora | [Fato][42] (regra observada: limpeza não iniciada 3 min após o desembarque) |
| C | Alerta: embarque não iniciado até TOBT − X | [Fato][2] |
| C | Alerta: prontidão não registrada em TOBT + 5 | [Fato][2] |
| C | Indicadores no estilo "TOBT Quality": antecedência das atualizações, atualizações tardias | [Fato][7] |
| **D** — Exceções e liberação | Abrir exceção com código da tabela da ANAC | [Inferência] (decisão D6; base: [16][62]) |
| D | Redistribuir equipe/recurso entre tarefas e turnarounds, com sugestão do sistema | [Fato][45][46][54] |
| D | Exigir atualização do TOBT quando a projeção se afasta 5 min ou mais (para mais **ou** para menos) | [Fato][8][9][10][13]; decisão D3 |
| D | Registrar a ação tomada para cada alerta crítico ("alerta → ação") | [Inferência] (base: [42][54]) |
| D | Liberação só com as condições do marco "Aircraft Ready" atendidas e sem exceção aberta | [Inferência] (base: definição de Aircraft Ready [2]; "sem exceção aberta" é regra do projeto) |
| D | Registrar off-block (AOBT) e encerrar o turnaround | [Fato][2] |

---

## Ligações

- **Decisões:** [D3](../../docs/adr/0003-atualizar-previsao-na-antecipacao.md), [D5](../../docs/adr/0005-abastecimento-com-passageiros-configuravel.md), [D6](../../docs/adr/0006-codigos-de-atraso-tabela-anac.md), [D7](../../docs/adr/0007-dados-do-operador-e-qr-code.md)
- **Itens da especificação:** [Item 6 — Requisitos Funcionais](../../especificacao/06-requisitos-funcionais/00-item.md), [Item 7 — Estórias de Usuário](../../especificacao/07-estorias-de-usuario/00-item.md), [Item 9 — Diagrama Geral de Casos de Uso](../../especificacao/09-diagrama-geral-de-casos-de-uso.md), [Item 10 — Especificações de Caso de Uso](../../especificacao/10-especificacoes-de-caso-de-uso/00-item.md)
- **Áreas do plano RA1:** [Área A — Acesso e planejamento](../../especificacao/06-requisitos-funcionais/area-a.md), [Área B — Execução em solo](../../especificacao/06-requisitos-funcionais/area-b.md), [Área C — Monitoramento](../../especificacao/06-requisitos-funcionais/area-c.md), [Área D — Exceções e liberação](../../especificacao/06-requisitos-funcionais/area-d.md) (divisão em [entregas/ra1-tarefas.md](../../entregas/ra1-tarefas.md), tabela 1.2)
- **Relacionados:** [atividades-e-dependencias](../topicos/atividades-e-dependencias.md), [tolerancias-e-indicadores](../topicos/tolerancias-e-indicadores.md), [codigos-de-atraso](../topicos/codigos-de-atraso.md), [impacto-por-item](impacto-por-item.md)
- **Fontes citadas:** 2, 3, 4, 7, 8, 9, 10, 13, 16, 20, 22, 24, 26, 27, 40, 42, 43, 44, 45, 46, 48, 51, 54, 62, 63, 64 (em [fontes.md](../fontes.md))
- **Contexto geral:** [CONTEXT.md](../../CONTEXT.md) · [mapa da pesquisa](../README.md)
