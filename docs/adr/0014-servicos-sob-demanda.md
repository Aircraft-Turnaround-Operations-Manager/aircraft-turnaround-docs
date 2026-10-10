---
id: adr-0014
titulo: "ADR-0014 — Serviços sob demanda: catálogo no modelo de tarefas, acionado pelo Coordenador de Turnaround"
tipo: decisao
decisao: D14
status: aceita
data: 2026-10-10
decisor: Rodrigo Alves
itens_template: [6, 7, 10]
areas: [A, D]
fontes: [45, 69, 70, 71, 73, 94, 96, 97]
relacionados: [servicos-sob-demanda, atividades-e-dependencias, caminho-critico, adr-0001, adr-0002, adr-0005, adr-0007]
---
# ADR-0014 — Serviços sob demanda: catálogo no modelo de tarefas, acionado pelo Coordenador de Turnaround

- **Status:** aceita · **Data:** 10/10/2026 · **Decisor:** Rodrigo Alves

## Contexto

- Alguns serviços do turnaround não acontecem em todo voo e podem surgir com o atendimento em andamento: limpeza profunda de assento, limpeza com risco biológico, assistência extra a passageiro, catering adicional. O modelo de tarefas da área A e o replanejamento da área D (RF-D7) não previam esses serviços.
- **[Fato][69][70][71]** Nos contratos de atendimento em solo, parte dos serviços vem marcada "on request": o serviço está contratado, mas só é prestado quando a companhia pede ([serviços sob demanda](../../pesquisa/topicos/servicos-sob-demanda.md), seção 1.1).
- **[Fato][96][97]** Softwares de *handling* permitem incluir tarefas ou serviços durante a operação; **[Fato][45][94]** o INFORM GroundStar recalcula o impacto nos processos dependentes.
- **[Fato][73]** Depois de um evento a bordo, a tripulação avisa as equipes de solo, durante o voo ou na chegada, sem antecedência fixa.
- A pesquisa deixou duas dúvidas abertas: se o atraso causado por um serviço sob demanda conta na meta de 80% e quem aciona o serviço no sistema.

## Opções consideradas

Na área A (modelo e plano): **A-1** catálogo de serviços sob demanda no modelo; **A-2** tarefa opcional marcada "Não aplicável" quando não pedida; **A-3** serviço já conhecido incluído no plano inicial.

Na área D (operação em andamento): **D-1** ampliar o RF-D7 para incluir a tarefa no plano em andamento; **D-2** tratar só como exceção (RF-D1); **D-3** exceção mais tarefa.

O detalhe de cada opção está na seção 5 da pesquisa.

## Decisão

**A-1 + A-3 + D-1**:

1. **Catálogo no modelo (A-1).** O modelo de tarefas passa a ter tarefas marcadas como **"sob demanda"**, com tipo de atividade, equipe e duração planejada. Elas não entram no plano do turnaround até serem acionadas.
2. **Serviço já conhecido (A-3).** Quando o serviço é conhecido antes de as tarefas começarem, ele entra no plano inicial, com responsável, janela e dependências, como qualquer outra tarefa.
3. **Acionamento com o turnaround em andamento (D-1).** O **Coordenador de Turnaround** inclui no plano em andamento uma tarefa do catálogo, com responsável, janela, dependências e motivo; o sistema registra autor e horário e recalcula a projeção de prontidão e o caminho crítico.
4. **Quem aciona.** Só o Coordenador de Turnaround aciona o serviço no sistema. A tripulação e as equipes de solo avisam por fora do sistema. O Operador de Solo/Rampa executa e registra a tarefa incluída, mas não replaneja (item 5).
5. **Travas do replanejamento.** A inclusão e as demais alterações do RF-D7 recusam ciclos, exigem que a sucessora comece depois das predecessoras e respeitam a regra de abastecimento com passageiros a bordo (ADR-0005), como no plano inicial.
6. **Meta do objetivo 1.** O atraso causado por um serviço sob demanda **conta** na meta de 80%. O serviço é previsto no catálogo, e a folga da meta absorve esses casos. A ADR-0001 e a ADR-0002 não mudam.

Motivos da rejeição de A-2: o operador teria de marcar "Não aplicável" em quase todo turnaround, o que polui o plano. De D-2: sem tarefa própria, o serviço não entra na projeção nem no caminho crítico e não tem responsável.

## Consequências

- **RF-A4:** a tarefa do modelo ganha a indicação "sob demanda". **RF-A5:** aceita o serviço já conhecido no plano inicial. **RF-A6:** diz se a cópia do modelo leva o catálogo.
- **RF-D7:** passa a incluir no plano em andamento uma tarefa do catálogo e a aplicar as travas do item 5. A US-D7 e o caso de uso da área D acompanham.
- A tarefa incluída é uma tarefa como as outras: entra na projeção e no caminho crítico (RF-C1 e RF-C3), pode ter pontos de confirmação por QR Code (ADR-0007) e, se for obrigatória, bloqueia a liberação (RF-D4).
- A área B não muda: o operador executa e registra a tarefa incluída pelos RFs que já existem.
- As amarrações entre as áreas A e D estão nas issues de pendência cruzada #59 e #78.

---

## Ligações

- **Pesquisa:** [servicos-sob-demanda](../../pesquisa/topicos/servicos-sob-demanda.md), [atividades-e-dependencias](../../pesquisa/topicos/atividades-e-dependencias.md), [caminho-critico](../../pesquisa/topicos/caminho-critico.md)
- **Itens da especificação:** [Item 6 — Requisitos Funcionais](../../especificacao/06-requisitos-funcionais/00-item.md), [Item 7 — Estórias de Usuário](../../especificacao/07-estorias-de-usuario/00-item.md), [Item 10 — Especificações de Caso de Uso](../../especificacao/10-especificacoes-de-caso-de-uso/00-item.md)
- **Áreas do plano RA1:** [Área A — Acesso e planejamento](../../especificacao/06-requisitos-funcionais/area-a.md), [Área D — Exceções e liberação](../../especificacao/06-requisitos-funcionais/area-d.md)
- **Outras decisões:** [D1](0001-referencia-horario-tobt-mais-5-min.md), [D2](0002-metas-percentuais-80.md), [D5](0005-abastecimento-com-passageiros-configuravel.md), [D7](0007-dados-do-operador-e-qr-code.md)
- **Fontes citadas:** 45, 69, 70, 71, 73, 94, 96, 97 (em [fontes.md](../../pesquisa/fontes.md))
- **Índice das decisões:** [README.md](README.md) · **Contexto geral:** [CONTEXT.md](../../CONTEXT.md)
