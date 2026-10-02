---
id: papeis-e-atores
titulo: "Papéis reais e os 4 atores do projeto (P1.7)"
tipo: pesquisa-topico
secao_original: "2.7"
itens_template: [4, 5, 9, 10, 11]
areas: [A, D]
decisoes: [D4, D9]
fontes: [2, 3, 4, 5, 7, 8, 13, 16, 29, 30, 31, 42, 57]
relacionados: [marcos-e-horarios, impacto-por-item]
status: vigente
atualizado: 2026-10-01
---
# Papéis reais e os 4 atores do projeto (P1.7)

> Base de conhecimento do projeto · origem: seção 2.7 do [relatório consolidado](../01-referencias-setor-e-similares.md) (congelado em 01/10/2026) · fontes numeradas em [fontes.md](../fontes.md) · convenções [Fato]/[Inferência] e índices no [mapa da pesquisa](../README.md).

> **Decisões vigentes (prevalecem sobre o texto abaixo):** [D4 — Quatro atores; Autoridade de Liberação é o representante da companhia](../../docs/adr/0004-quatro-atores-e-autoridade-de-liberacao.md); [D9 — Nome único: Coordenador de Turnaround](../../docs/adr/0009-nome-coordenador-de-turnaround.md).
>
> Nomes vigentes dos atores: Operador de Solo/Rampa, Coordenador de Turnaround (D9), Autoridade de Liberação (representante da companhia aérea que confirma a prontidão; não é o ATC — D4) e Motor de Eventos. Onde o texto abaixo usa "Coordenador/Supervisor", leia "Coordenador de Turnaround".


## 2.7.1 Papéis encontrados nas fontes

| Papel real | O que faz no turnaround | Fonte |
|---|---|---|
| Companhia aérea (*Aircraft Operator*, AO) | Dona do plano de voo; "responsible for the TOBT and any updates", podendo delegar ao *ground handler*. A IATA diz que o TOBT é "owned by the airline". | [Fato][2] seção 4.7; [5] |
| *Ground handler* (GH) / "TOBT Responsible Person" | Executa o atendimento em solo; assume o TOBT quando a companhia delega. | [Fato][2] seção 4.6; [13] |
| Turnaround Coordinator / Turnaround Manager / Dispatcher | "responsible for coordinating all functions around the aircraft to enable a safe, secure and on time departure, whilst following airline specific procedures" (Menzies). Em Heathrow, "Ground Handlers/Turnaround Managers" trabalham para cumprir o TOBT. | [Fato][30]; [7] seção 2.5; [29] |
| Equipes e prestadores de rampa | Carregamento, abastecimento, limpeza, catering, água/lavatório, push-back. Vários são empresas diferentes (os códigos IATA citam "fuel supplier" e "late delivery" de catering). | [Fato][13][16][31] |
| Controle de carga (*load control*) | Prepara a documentação de peso e balanceamento (código 31). | [Fato][16] |
| Tripulação / comandante | Reporta "pronto" e pede acionamento; em Dublin, "The Pilot shall ensure that the flight is ready to depart at TOBT (window of -/+5 minutes)". | [Fato][2] seção 5.1.11; [8] seção 4.22.1 |
| Operador do aeroporto / centro de operações (AOC/APOC) | "responsible for the operational management of the airport"; pode atualizar o status de pronto no A-CDM System; no estudo de caso da Assaia, um "AOC operative" recebe o alerta e liga para o *handling*. | [Fato][2] seções 4.2 e 5.1.11; [42] |
| Controle de tráfego aéreo (ATC) | Registra ARDT, emite TSAT e autoriza acionamento e push-back. | [Fato][2][3] |
| Network Manager | Gerenciamento de fluxo (ATFM) e CTOT. | [Fato][2] seção 4.8; [4] |
| Sistema A-CDM / plataforma de informação | Calcula horários (EIBT, TOBT inicial, TTOT) e envia alertas (CDM07, CDM08). No Brasil, o anúncio de GRU cita a ACISP (*Airport Collaborative Information Sharing Platform*). | [Fato][2][3][57] |

**Quem declara a aeronave pronta? [Fato][2][4]** No A-CDM, o marco "Aircraft Ready" (ARDT) é registrado pelo controlador "When the flight reports ready", ou pelas operações do aeroporto no A-CDM System. O *ground handler* marca o fim do atendimento (AEGT, que "can be equal to ARDT"). **[Inferência]** Não existe, nas fontes, um papel único chamado "autoridade de liberação": a prontidão resulta de três atos — o *handling* encerra o atendimento, a tripulação reporta pronto e o ATC autoriza o acionamento.

## 2.7.2 Comparação com os atores do projeto

| Ator do projeto | Papel(éis) real(is) correspondente(s) | Aderência [Inferência] | Sugestão [Inferência] |
|---|---|---|---|
| Operador de Solo/Rampa | Equipes e prestadores de rampa (carregamento, abastecimento, limpeza, catering, água/lavatório, push-back) | Alta | Descrever como "executante de tarefas do turnaround, da própria empresa de *handling* ou de prestador contratado". Isso explica por que o sistema precisa de responsável por tarefa. |
| Coordenador/Supervisor de Turnaround | Turnaround Coordinator/Manager; também o "TOBT Responsible Person" quando a companhia delega | Alta | Usar **um único nome** em todos os itens (critério K.1). "Coordenador de Turnaround" é o termo mais próximo do setor. Incluir na descrição: manter atualizado o horário planejado de prontidão (TOBT). |
| Autoridade de Liberação | Sem papel único. O mais próximo é o representante da companhia aérea/comandante, que confirma a prontidão depois que o *handling* encerra o atendimento | Parcial | Manter o ator (separa quem executa de quem libera, o que sustenta a métrica "0 liberações com pendência"), mas descrevê-lo como "representante da companhia aérea que confirma a prontidão da aeronave (equivalente ao marco Aircraft Ready do A-CDM)", deixando claro que **não** é a autorização do ATC. Ver [D4](../../docs/adr/0004-quatro-atores-e-autoridade-de-liberacao.md). |
| Motor de Eventos | Sistema A-CDM / plataforma de informação compartilhada | Alta | Descrever como "componente que recebe os registros, recalcula projeções e caminho crítico e emite alertas", citando o A-CDM System como analogia. |
| (sem ator) | ATC, Network Manager, AOC/APOC | — | ATC e Network Manager ficam fora (integração com ATC fora de escopo). O AOC pode, no máximo, aparecer como consumidor do painel; não é necessário como ator no MVP. |

---

## Ligações

- **Decisões:** [D4](../../docs/adr/0004-quatro-atores-e-autoridade-de-liberacao.md), [D9](../../docs/adr/0009-nome-coordenador-de-turnaround.md)
- **Itens da especificação:** [Item 4 — Mapeamento de Negócios (BPMN TO BE)](../../especificacao/04-mapeamento-de-negocios.md), [Item 5 — Atores / Usuários](../../especificacao/05-atores-usuarios.md), [Item 9 — Diagrama Geral de Casos de Uso](../../especificacao/09-diagrama-geral-de-casos-de-uso.md), [Item 10 — Especificações de Caso de Uso](../../especificacao/10-especificacoes-de-caso-de-uso/00-item.md), [Item 11 — Diagrama de Atividades](../../especificacao/11-diagrama-de-atividades.md)
- **Áreas do plano RA1:** [Área A — Acesso e planejamento](../../especificacao/06-requisitos-funcionais/area-a.md), [Área D — Exceções e liberação](../../especificacao/06-requisitos-funcionais/area-d.md) (divisão em [entregas/ra1-tarefas.md](../../entregas/ra1-tarefas.md), tabela 1.2)
- **Relacionados:** [marcos-e-horarios](marcos-e-horarios.md), [impacto-por-item](../impacto/impacto-por-item.md)
- **Fontes citadas:** 2, 3, 4, 5, 7, 8, 13, 16, 29, 30, 31, 42, 57 (em [fontes.md](../fontes.md))
- **Contexto geral:** [CONTEXT.md](../../CONTEXT.md) · [mapa da pesquisa](../README.md)
