---
id: adr-0010
titulo: "ADR-0010 — Administrador do Sistema, ator abstrato Usuário e equipe do operador como dado"
tipo: decisao
decisao: D10
status: aceita
data: 2026-10-03
decisor: Rodrigo Alves
itens_template: [5, 6, 7, 9, 10]
areas: [A, B]
fontes: [16, 31]
relacionados: [papeis-e-atores, atividades-e-dependencias, adr-0004, adr-0009]
---
# ADR-0010 — Administrador do Sistema, ator abstrato Usuário e equipe do operador como dado

- **Status:** aceita · **Data:** 03/10/2026 · **Decisor:** Rodrigo Alves · **Complementa:** [ADR-0004](0004-quatro-atores-e-autoridade-de-liberacao.md) (os quatro atores operacionais e a definição da Autoridade de Liberação continuam valendo)

## Contexto

- A área A do plano RA1 inclui **autenticação e perfis de acesso** ([entregas/ra1-tarefas.md](../../entregas/ra1-tarefas.md), tabela 1.2), mas nenhum dos quatro atores da ADR-0004 administra usuários e perfis.
- O template pede, no diagrama geral de casos de uso, **generalização de atores** onde fizer sentido (critério C09.4).
- **[Fato]** Cada tarefa do turnaround é executada por uma equipe diferente, muitas vezes de empresas diferentes: fornecedor de combustível, limpeza, catering, agentes de rampa, manutenção [16][31] (detalhe em [Atividades e dependências](../../pesquisa/topicos/atividades-e-dependencias.md)).
- **[Inferência]** Todas essas equipes interagem com o sistema do mesmo modo: veem as tarefas atribuídas e registram início, pausa, conclusão, "não aplicável" e leitura de QR Code.

## Opções consideradas

- **(a)** Manter os quatro atores da ADR-0004.
- **(b)** Acrescentar o **Administrador do Sistema** e o ator abstrato **Usuário**.
- **(c)** Criar um ator por especialidade do operador (Operador de Abastecimento, Operador de Limpeza etc.), herdando de Operador de Solo/Rampa.

## Decisão

**(b)**, sem **(c)**:

1. **Administrador do Sistema** passa a ser ator: mantém usuários, perfis de acesso e equipes ou especialidades. Não atua nos turnarounds.
2. **Usuário** é um ator **abstrato**: generaliza os quatro atores humanos (Operador de Solo/Rampa, Coordenador de Turnaround, Autoridade de Liberação e Administrador do Sistema) e reúne os casos de uso comuns, como autenticar-se e encerrar a sessão. Não é um perfil próprio. O Motor de Eventos, não humano, não o especializa.
3. **Operador de Solo/Rampa** continua sendo **um único ator**. A **equipe ou especialidade** (abastecimento, limpeza da cabine, catering, carregamento, água e lavatório etc.) é um **dado** do cadastro do usuário e da tarefa: cada operador vê e registra só as tarefas da sua equipe atribuídas a ele.

Motivo da rejeição de (c): as especialidades não têm casos de uso diferentes; atores separados repetiriam as mesmas ligações no diagrama, e a generalização pedida pelo C09.4 já é atendida pelo Usuário.

## Consequências

- Nomes exatos dos atores passam a ser: Operador de Solo/Rampa, Coordenador de Turnaround, Autoridade de Liberação, Administrador do Sistema, Motor de Eventos e, só como ator abstrato, Usuário (critério K.1).
- Item 5: linha do Administrador do Sistema, parágrafo de generalização e redação do Operador por equipe.
- Item 6 (área A): RFs de gestão de usuários, perfis e equipes, com ator Administrador do Sistema; autenticação com ator Usuário.
- Item 9: generalização Usuário → atores humanos; casos de uso comuns ligados ao Usuário.
- Itens 6, 7 e 10 (área B): a atribuição de tarefa respeita a equipe do operador.
- O BPMN (item 4) e o diagrama de atividades (item 11) não ganham lane para o Administrador, que não participa do processo de turnaround.

---

## Ligações

- **Pesquisa:** [papeis-e-atores](../../pesquisa/topicos/papeis-e-atores.md), [atividades-e-dependencias](../../pesquisa/topicos/atividades-e-dependencias.md)
- **Itens da especificação:** [Item 5 — Atores / Usuários](../../especificacao/05-atores-usuarios.md), [Item 6 — Requisitos Funcionais](../../especificacao/06-requisitos-funcionais/00-item.md), [Item 7 — Estórias de Usuário](../../especificacao/07-estorias-de-usuario/00-item.md), [Item 9 — Diagrama Geral de Casos de Uso](../../especificacao/09-diagrama-geral-de-casos-de-uso.md), [Item 10 — Especificações de Caso de Uso](../../especificacao/10-especificacoes-de-caso-de-uso/00-item.md)
- **Outras decisões:** [D4](0004-quatro-atores-e-autoridade-de-liberacao.md), [D9](0009-nome-coordenador-de-turnaround.md)
- **Fontes citadas:** 16, 31 (em [fontes.md](../../pesquisa/fontes.md))
- **Índice das decisões:** [README.md](README.md) · **Contexto geral:** [CONTEXT.md](../../CONTEXT.md)
