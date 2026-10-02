---
id: atividades-e-dependencias
titulo: "Atividades, paralelismo e dependências (P1.5)"
tipo: pesquisa-topico
secao_original: "2.5"
itens_template: [4, 6, 7, 10, 11]
areas: [A, B]
decisoes: [D5, D7]
fontes: [2, 13, 16, 20, 21, 22, 23, 24, 26, 27, 28, 29, 31, 42, 63, 64]
relacionados: [caminho-critico, marcos-e-horarios, codigos-de-atraso, insumos-rfs]
status: vigente
atualizado: 2026-10-01
---
# Atividades, paralelismo e dependências (P1.5)

> Base de conhecimento do projeto · origem: seção 2.5 do [relatório consolidado](../01-referencias-setor-e-similares.md) (congelado em 01/10/2026) · fontes numeradas em [fontes.md](../fontes.md) · convenções [Fato]/[Inferência] e índices no [mapa da pesquisa](../README.md).

> **Decisões vigentes (prevalecem sobre o texto abaixo):** [D5 — Abastecimento com passageiros a bordo: regra configurável por operador](../../docs/adr/0005-abastecimento-com-passageiros-configuravel.md); [D7 — Dados registrados pelo operador, inclusive QR Code lido pelo celular](../../docs/adr/0007-dados-do-operador-e-qr-code.md).
>
> A relação entre abastecimento, desembarque e embarque é regra configurável por operador (D5). A execução de tarefas pode ser confirmada por leitura de QR Code no celular do operador (D7).


**[Fato][20][23]** A literatura descreve o turnaround como "five major tasks": "deboarding, catering, cleaning, fueling, and boarding", mais "the parallel processes of unloading and loading". **[Fato][22]** Kierzkowski et al. (2025) detalham 12 tarefas: calçar a aeronave, posicionar escada/ponte, desembarque, serviço de cabine, embarque, retirada da escada, descarregamento de bagagem, carregamento de bagagem, abastecimento, serviço de lavatório, reposição de água e retirada dos calços. **[Fato][31]** A SKYbrary lista entre os serviços de rampa: carregamento e descarregamento, abastecimento, "toilet and water servicing", limpeza, catering, documentação, degelo e push-back.

| # | Atividade | Executante típico | Começa depois de | Pode correr em paralelo com | Marco / observação | Fonte |
|---|---|---|---|---|---|---|
| A1 | Calçar a aeronave e posicionar ponte ou escada | Agente de rampa | Chegada à posição (AIBT) | — | "Ground handling begins with the locking of the aircraft's wheels and the placement of a passenger ramp" | [Fato][21][22] |
| A2 | Desembarque de passageiros | *Handling* de passageiros / tripulação | A1 | A3 e A7; A4 só sob regra especial (ver abaixo) | "passenger disembarkation and baggage unloading" podem ser simultâneos | [Fato][22] |
| A3 | Descarregamento de bagagem e carga | Equipe de carregamento (rampa) | A1 | A2, A4, A7 | Processo paralelo ao fluxo de passageiros | [Fato][20][22] |
| A4 | Abastecimento | Fornecedor de combustível | A1; com passageiros a bordo, só com procedimento aprovado | A3, A5, A6, A7 | Código de atraso 36 "FUELLING DEFUELLING, fuel supplier" | [Fato][16][26][27]; paralelismo = [Inferência] |
| A5 | Limpeza da cabine | Equipe de limpeza | Fim de A2 | A4, A6, A7, A3 | "aircraft cleaning can only take place after passengers have left" | [Fato][22] |
| A6 | Catering | Empresa de catering | Fim de A2 | A5, A4, A7 | "All passengers must disembark before catering teams board" (resumo do artigo) | [Fato][29] |
| A7 | Água potável e serviço de lavatório | Agente de rampa | A1 | Quase todas | Listado como tarefa própria | [Fato][22][31] (existência da tarefa); dependências = [Inferência] |
| A8 | Inspeção técnica de trânsito | Manutenção | A1 | Quase todas | Códigos 41–43 cobrem defeito e manutenção | [Fato][16][31] (existência da tarefa); dependências = [Inferência] |
| A9 | Embarque | *Handling* de passageiros | Fim de A5; fim de A4 se o operador não abastece com passageiros. Esperar também o fim de A6 = [Inferência] | A10 | Marco 11 (ASBT); alerta se não começar até TOBT − X (variável local) | [Fato][2][24][29] |
| A10 | Carregamento de bagagem e carga | Equipe de carregamento | Fim de A3 = [Inferência] | A9 | Descarregar e carregar são "parallel processes" ao fluxo de passageiros | [Fato][20] |
| A11 | Documentação de peso e balanceamento (loadsheet) | Controle de carga (*load control*) | Fim de A9 e A10 | — | "Final paperwork (weight/balance figures) requires complete passenger and baggage loading"; código 31 | [Fato][16][29] |
| A12 | Fechar portas e retirar ponte/escada | *Handling* / tripulação | Fim de A9, A10 e A11 | — | Condições do marco 12 "Aircraft Ready" | [Fato][2][29] |
| A13 | Push-back e retirada dos calços | Agente de rampa (trator) | A12 + autorização do ATC (fora de escopo) | — | Marco 15 (AOBT); código 39 cobre falta ou pane de trator | [Fato][2][16] |

*Nota sobre a tabela:* nas colunas "Começa depois de" e "Pode correr em paralelo com", são [Fato] apenas as relações sustentadas pela citação da coluna "Marco / observação" ou pela fonte da linha (A1, A2 ∥ A3, A5 e A6 depois de A2, A9 depois de A5, A11, A12). As demais relações são [Inferência] a partir da descrição geral do processo.

**Restrições de segurança — abastecimento com passageiros a bordo:**

- **[Fato][26]** Regra europeia CAT.OP.MPA.195: "An aircraft shall not be refuelled/defuelled with Avgas or wide-cut type fuel when passengers are embarking, on board or disembarking." Para os demais combustíveis, "necessary precautions shall be taken and the aircraft shall be properly manned by qualified personnel ready to initiate and direct an evacuation."
- **[Fato][27]** Regra brasileira, RBAC 91 (Emenda 05, 01/04/2025), seção 91.102(g): o abastecimento com passageiros a bordo, embarcando ou desembarcando só é permitido se houver (1) procedimento aprovado e um tripulante de voo na cabine supervisionando; (2) no mínimo 50% dos comissários requeridos e/ou pessoas treinadas para dirigir evacuação, com meios de evacuação disponíveis; (3) motores desligados (exceto APU, a unidade auxiliar de energia); e (4) comunicação entre o pessoal de solo e a cabine dos pilotos. *Emendas posteriores à 05 não foram conferidas.*
- **[Fato][28]** A Airbus (briefing de 2007) lista precauções: sinal de "NO SMOKING" aceso, "FASTEN SEAT BELT" apagado, saídas de emergência desobstruídas e área sob as saídas livre de equipamentos.
- **[Fato][24]** Há modelos acadêmicos que adotam a regra mais restritiva: "The refuelling procedure cannot begin until the disembarking has ended, as well as boarding cannot begin until refuelling has finished".
- **[Inferência]** Abastecer com passageiros é **permitido sob condições**, e a escolha é de cada operador. Por isso, a dependência entre abastecimento, desembarque e embarque deve ser uma **regra configurável** do modelo de tarefas, não uma dependência fixa. Ela muda o caminho crítico (ver [Caminho crítico](caminho-critico.md)).

**Pontos de verificação usados na prática [Fato][13]:** o cartão de rampa dos aeroportos alemães manda, no **TOBT − 15 min**, conferir com tripulação, portão/embarque, carregamento, abastecimento, limpeza e catering se todos estão no prazo, e ajustar o TOBT se preciso; no **TOBT − 3 min**, conferir se a ponte ou escada foi removida e se todas as portas estão fechadas. **[Inferência]** Esses dois instantes são bons candidatos a eventos de temporizador no BPMN (item 4) e a regras do Motor de Eventos.

- **Decisão D7 (vigente):** a confirmação de tarefas pode ser feita por leitura de QR Code no celular do operador, por exemplo a limpeza da cabine por assento, fileira ou zona. Registro das leituras de 01/10/2026: **[Fato][63]** piloto do app Wellness Trace (GE Aviation) no Aeroporto de Albany, EUA, a partir de nov/2020, com QR Codes em banheiros e totens para registrar e consultar a limpeza; **[Fato][64]** modelo de checklist digital de limpeza de cabine organizado por zona (assentos, galleys, lavatórios), assinado pelo líder da equipe; **[Fato][42]** a Assaia alerta quando a equipe de limpeza não é detectada pela câmera de pátio até 3 min depois do fim do desembarque. **[Inferência]** Não foi encontrada leitura de QR Code por assento ligada ao andamento do turnaround nas fontes consultadas.

---

## Ligações

- **Decisões:** [D5](../../docs/adr/0005-abastecimento-com-passageiros-configuravel.md), [D7](../../docs/adr/0007-dados-do-operador-e-qr-code.md)
- **Itens da especificação:** [Item 4 — Mapeamento de Negócios (BPMN TO BE)](../../especificacao/04-mapeamento-de-negocios.md), [Item 6 — Requisitos Funcionais](../../especificacao/06-requisitos-funcionais/00-item.md), [Item 7 — Estórias de Usuário](../../especificacao/07-estorias-de-usuario/00-item.md), [Item 10 — Especificações de Caso de Uso](../../especificacao/10-especificacoes-de-caso-de-uso/00-item.md), [Item 11 — Diagrama de Atividades](../../especificacao/11-diagrama-de-atividades.md)
- **Áreas do plano RA1:** [Área A — Acesso e planejamento](../../especificacao/06-requisitos-funcionais/area-a.md), [Área B — Execução em solo](../../especificacao/06-requisitos-funcionais/area-b.md) (divisão em [entregas/ra1-tarefas.md](../../entregas/ra1-tarefas.md), tabela 1.2)
- **Relacionados:** [caminho-critico](caminho-critico.md), [marcos-e-horarios](marcos-e-horarios.md), [codigos-de-atraso](codigos-de-atraso.md), [insumos-rfs](../impacto/insumos-rfs.md)
- **Fontes citadas:** 2, 13, 16, 20, 21, 22, 23, 24, 26, 27, 28, 29, 31, 42, 63, 64 (em [fontes.md](../fontes.md))
- **Contexto geral:** [CONTEXT.md](../../CONTEXT.md) · [mapa da pesquisa](../README.md)
