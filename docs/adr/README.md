---
id: adr-indice
titulo: "Decisões do projeto (ADRs)"
tipo: decisao-indice
status: vigente
atualizado: 2026-11-13
relacionados: [adr-0001, adr-0002, adr-0003, adr-0004, adr-0005, adr-0006, adr-0007, adr-0008, adr-0009, adr-0010, adr-0011, adr-0012, adr-0013, adr-0014, adr-0015, adr-0016, adr-0020, adr-0021, adr-0022, mapa-pesquisa]
---
# Decisões do projeto (ADRs)

> Uma decisão por arquivo. **As decisões prevalecem** sobre a pesquisa (`pesquisa/`) e sobre rascunhos antigos. Decisão nova: próximo número, mesmo formato (contexto, opções, decisão, consequências, ligações), status "aceita" e data. Decisão que muda outra: a antiga passa a "substituída por ADR-NNNN".

| ADR | Origem | Decisão | Itens afetados |
|---|---|---|---|
| [0001](0001-referencia-horario-tobt-mais-5-min.md) | D1 | Referência de horário: TOBT planejado + 5 min, unilateral | 1, 6, 7, 8, 10 |
| [0002](0002-metas-percentuais-80.md) | D2 | Metas percentuais do item 1: 80% | 1, 3 |
| [0003](0003-atualizar-previsao-na-antecipacao.md) | D3 | Antecipação de 5 min ou mais exige atualizar a previsão | 1, 6, 7, 10 |
| [0004](0004-quatro-atores-e-autoridade-de-liberacao.md) | D4 | Quatro atores operacionais; Autoridade de Liberação é o representante da companhia (complementada pela 0010) | 2, 4, 5, 6, 9, 10, 11 |
| [0005](0005-abastecimento-com-passageiros-configuravel.md) | D5 | Abastecimento com passageiros a bordo: regra configurável por operador | 4, 6, 10, 11 |
| [0006](0006-codigos-de-atraso-tabela-anac.md) | D6 | Códigos de atraso: tabela completa da ANAC (72 códigos) | 2, 4, 6, 7, 10 |
| [0007](0007-dados-do-operador-e-qr-code.md) | D7 | Dados registrados pelo operador, inclusive QR Code lido pelo celular | 2, 3, 4, 6, 7, 10 |
| [0008](0008-siglas-a-cdm-com-nome-em-portugues.md) | D8 | Siglas do A-CDM com nome em português; vale para toda sigla, inclusive órgãos e normas | todos |
| [0009](0009-nome-coordenador-de-turnaround.md) | D9 | Nome único: Coordenador de Turnaround | todos |
| [0010](0010-administrador-usuario-e-equipe-do-operador.md) | D10 | Administrador do Sistema como ator; ator abstrato Usuário; equipe do operador como dado (complementa a 0004) | 5, 6, 7, 9, 10 |
| [0011](0011-minimo-por-integrante-e-numeracao-provisoria.md) | D11 | Mínimo de 4 por integrante, sem máximo; numeração provisória por área e renumeração única no T12 (complementada pela 0022) | 6, 7, 8, 9, 10 |
| [0012](0012-matriz-de-rastreabilidade.md) | D12 | Matriz de rastreabilidade como apêndice gerado por script; sem tabelas "Base" nos arquivos de área (complementada pela 0021) | 6, 7, 8, 10 |
| [0013](0013-chegada-registrada-pelo-operador.md) | D13 | Chegada à posição (AIBT) registrada direto pelo operador, sem confirmação; o Coordenador de Turnaround pode corrigir | 6, 7, 10 |
| [0014](0014-servicos-sob-demanda.md) | D14 | Serviços sob demanda: catálogo no modelo de tarefas, acionado pelo Coordenador de Turnaround; o atraso conta na meta de 80% | 6, 7, 10 |
| [0015](0015-divisao-em-microsservicos.md) | D15 | Quatro microsserviços, com a tarefa e o estado do turnaround na Execução em Solo; avisos pela mensageria e pedidos em chamada direta | 12, 13, 14 |
| [0016](0016-contrato-entre-os-servicos.md) | D16 | Contrato comum entre os serviços, votado pelo grupo: REST, RabbitMQ, envelope dos avisos, UTC, UUID e nomes em português; base provisória do RA2 | 12, 13, 14, 15 |
| [0020](0020-tecnologia-excecoes-e-liberacao.md) | D20 | Tecnologia do serviço Exceções e Liberação: C# com .NET 10, ASP.NET Core 10 e PostgreSQL 18, seguindo o contrato da 0016 | 12, 14 |
| [0021](0021-matriz-de-rastreabilidade-estendida.md) | D21 | Matriz de rastreabilidade estendida aos itens 12, 14 e 15: RF → tabelas, caso de uso → diagrama de sequência, critério de aceite → casos de teste (complementa a 0012) | 12, 14, 15 |
| [0022](0022-ids-provisorios-dos-casos-de-teste.md) | D22 | Casos de teste com ID provisório por área (CT-A001…) e renumeração única (CT-001…) na consolidação (complementa a 0011) | 15 |

---

## Ligações

- **Contexto geral:** [CONTEXT.md](../../CONTEXT.md)
- **Mapa da pesquisa:** [pesquisa/README.md](../../pesquisa/README.md)
- **Fontes:** [pesquisa/fontes.md](../../pesquisa/fontes.md)
