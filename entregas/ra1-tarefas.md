# Quebra de Tarefas — RA1 (Especificação do Projeto, itens 1 a 11)

> Plano de tarefas para o GitHub Project **"Especificação de Software - 6p"**, derivado de [`ra1-criterios-de-aceite.md`](ra1-criterios-de-aceite.md).
> Os critérios (IDs `Cxx.y`, `X.y`, `K.y`) estão definidos naquele arquivo. Aqui só se referenciam os IDs.
> **Status:** aprovado pelo Rodrigo em 29/09/2026 — pronto para criação no GitHub.

---

## 1. Decisões de divisão

### 1.1 Responsáveis fixos
- **Itens 1 a 5:** Rodrigo Alves (`rdsalvesPUC`).
- **Itens 9 e 11 (integração dos diagramas):** sem responsável; quem puxar se atribui.
- **Tarefas gerais (preparação do repositório, revisão final, consolidação e envio):** sem responsável.
- **Regra para tarefas sem responsável:** quem puxar a tarefa se coloca como responsável (assignee) no momento em que começar.

### 1.3 Fluxo de trabalho

- **Formato:** todo o conteúdo é produzido em arquivos **Markdown (.md)** no repositório `aircraft-turnaround-docs`, e não diretamente no .docx do template.
- **Diagramas:** escritos como código, com **Mermaid** ou **PlantUML**, o que funcionar melhor para cada diagrama. O arquivo-fonte (`.mmd` ou `.puml`) fica versionado junto com a imagem exportada. Exceção: o BPMN do item 4 é feito em BPMN 2.0 (`.bpmn`), porque Mermaid e PlantUML não têm notação BPMN (critério C04.1).
- **Branches:** cada tarefa é feita em uma **branch própria**, e o trabalho entra na `main` por **pull request**. O PR aberto corresponde ao status **In review** no board.
- **Consolidação:** quando todos os itens estiverem na `main`, os arquivos MD são consolidados em um único documento, na ordem e com os títulos do template, e exportados em **PDF**, que é o formato de envio no Canvas.

### 1.2 Divisão por área funcional (itens 6, 7, 8 e 10)

Cada integrante fica com **uma área funcional** do sistema. Dentro dela, faz **no mínimo 4 RFs** (sem máximo), uma estória para cada RF, **no mínimo 4 especificações de caso de uso** e **no mínimo 4 RNFs** nas características da ISO/IEC 25010 indicadas (ADR-0011). Um RF além do mínimo pode ser coberto por um caso de uso já existente, por `include` ou `extend`. Assim a cadeia RF → estória → caso de uso fica com a mesma pessoa, e as áreas não se sobrepõem.

Atribuição de áreas confirmada pelo Rodrigo em 29/09/2026.

| Área | Escopo funcional | IDs provisórios (ADR-0011) | RNF (ISO/IEC 25010) | Responsável |
|---|---|---|---|---|
| **A** | Acesso e planejamento: autenticação e perfis de acesso (gestão de usuários, perfis e equipes pelo Administrador do Sistema, ADR-0010), abertura do turnaround, definição das tarefas do turnaround | RF-A1… · US-A1… · UC-A1… · RNF-A1… (mínimo 4 de cada) | Segurança (incl. LGPD) · Compatibilidade | Eduardo Fabri (`eduardofabrii`) |
| **B** | Execução em solo: o operador consulta, inicia, pausa, conclui ou marca "não aplicável" nas tarefas | RF-B1… · US-B1… · UC-B1… · RNF-B1… (mínimo 4 de cada) | Confiabilidade · Portabilidade | João Pedro Cardoso de Liz (`Jcliz`) |
| **C** | Monitoramento: dashboard em tempo real, cálculo de atraso e caminho crítico, alertas | RF-C1… · US-C1… · UC-C1… · RNF-C1… (mínimo 4 de cada) | Eficiência de desempenho · Usabilidade | João Vitor Correa Oliveira (`jvecodev`) |
| **D** | Exceções e liberação: tratamento de exceção, redistribuição de recursos pelo Coordenador de Turnaround, liberação da aeronave | RF-D1… · US-D1… · UC-D1… · RNF-D1… (mínimo 4 de cada) | Manutenibilidade · Confiabilidade | Rodrigo Alves (`rdsalvesPUC`) |

Os escopos acima são **orientação para evitar sobreposição**. Os RFs em si são definidos por cada integrante na tarefa T06.

---

## 2. Rótulos (labels) a criar no repositório `aircraft-turnaround-docs`

| Rótulo | Cor | Uso |
|---|---|---|
| `ra1` | `#1D76DB` | Todas as tarefas desta entrega |
| `item-01` … `item-11` | `#C5DEF5` | Item do template a que a tarefa se refere |
| `geral` | `#BFDADC` | Tarefas que não são de um item específico |
| `por-integrante` | `#FBCA04` | Subtarefas da cota mínima de 4 por integrante (sem máximo) |
| `area-a` … `area-d` | `#D4C5F9` | Área funcional (seção 1.2) |

---

## 3. Lista de tarefas

Convenção de título: `[RA1][Item NN] <descrição>`. Para tarefas gerais: `[RA1][Geral] <descrição>`.
Estrutura hierárquica: **T06, T07, T08 e T10 são tarefas-mãe** com 4 **sub-issues** cada (uma por área). O campo "Sub-issues progress" do project mostra o andamento.

Total: **30 issues** (14 principais + 16 sub-issues).

### Fase 0 — Preparação

**T00 · [RA1][Geral] Preparar a estrutura do repositório para a especificação**
- Responsável: quem puxar · Rótulos: `ra1`, `geral`
- Descrição: criar no repositório a estrutura de pastas e arquivos MD, um por item do template (1 a 11), com os títulos originais. Nos itens por integrante, definir como cada área terá sua parte para evitar conflito de merge, por exemplo um arquivo por área. Definir também a pasta dos diagramas (fonte `.mmd`/`.puml` + imagem exportada), o nome do produto a usar em todos os quadros e o padrão de nome de branch. Registrar essas convenções no `README.md` do repositório.
- Critérios: X.1 (estrutura e títulos na ordem do template), X.9
- Bloqueia: nada (pode começar já; convém ser a primeira tarefa concluída)

### Fase 1 — Visão do produto (Rodrigo)

**T01 · [RA1][Item 01] Quadro "3 Objetivos"**
- Responsável: `rdsalvesPUC` · Rótulos: `ra1`, `item-01`
- Critérios: C01.1 a C01.4
- Bloqueia: T03, T06

**T02 · [RA1][Item 02] Quadro "É – Não é – Faz – Não faz"**
- Responsável: `rdsalvesPUC` · Rótulos: `ra1`, `item-02`
- Critérios: C02.1 a C02.4
- Bloqueia: T03, T06

**T03 · [RA1][Item 03] Visão do Produto**
- Responsável: `rdsalvesPUC` · Rótulos: `ra1`, `item-03`
- Critérios: C03.1 a C03.5
- Bloqueada por: T01, T02 · Bloqueia: T05, T06

**T05 · [RA1][Item 05] Relação de Atores / Usuários**
- Responsável: `rdsalvesPUC` · Rótulos: `ra1`, `item-05`
- Critérios: C05.1 a C05.5
- Bloqueada por: T03 · Bloqueia: T04, T06

**T04 · [RA1][Item 04] Mapeamento de Negócios (BPMN TO BE)**
- Responsável: `rdsalvesPUC` · Rótulos: `ra1`, `item-04`
- Critérios: C04.1 a C04.9
- Bloqueada por: T05

### Fase 2 — Requisitos (todos)

**T06 · [RA1][Item 06] Relação de Requisitos Funcionais (≥16 RFs)** — tarefa-mãe
- Responsável: quem puxar (consolidação) · Rótulos: `ra1`, `item-06`
- Descrição: consolidar na tabela do template os RFs das 4 áreas (no mínimo 16), com os IDs provisórios até a renumeração do T12 e, no documento final, RF-1 a RF-n sem lacunas, ator, sprint/prioridade e justificativa da priorização.
- Critérios: C06.1 a C06.8
- Bloqueada por: T03, T05 · Bloqueia: T07, T09
- Sub-issues:
  - **T06-A** · RFs da área A (RF-A1…, mínimo 4) · `eduardofabrii` · `ra1`, `item-06`, `por-integrante`, `area-a`
  - **T06-B** · RFs da área B (RF-B1…, mínimo 4) · `Jcliz` · `ra1`, `item-06`, `por-integrante`, `area-b`
  - **T06-C** · RFs da área C (RF-C1…, mínimo 4) · `jvecodev` · `ra1`, `item-06`, `por-integrante`, `area-c`
  - **T06-D** · RFs da área D (RF-D1…, mínimo 4) · `rdsalvesPUC` · `ra1`, `item-06`, `por-integrante`, `area-d`
  - Critérios de cada sub-issue: C06.2 a C06.5 para todos os RFs da área (mínimo 4)
  - Formato da tabela de cada área: `# | REQUISITO FUNCIONAL | ATOR / USUÁRIO | OBJETIVO | SPRINT`. A coluna OBJETIVO traz o objetivo do item 1 (C06.5). A coluna SPRINT fica **vazia** nas sub-issues: a divisão em sprints e a justificativa da priorização (C06.6 e C06.7) são feitas nesta tarefa-mãe, depois que todas as áreas definirem os RFs e os RNFs.

**T07 · [RA1][Item 07] Relação de Estórias de Usuário (≥16 estórias)** — tarefa-mãe
- Responsável: quem puxar (consolidação) · Rótulos: `ra1`, `item-07`
- Critérios: C07.1 a C07.7
- Bloqueada por: T06 · Bloqueia: T10
- Sub-issues (cada uma bloqueada pela sub-issue de RF da mesma área):
  - **T07-A** · Estórias US-A1… (uma por RF da área) · `eduardofabrii` · `area-a`
  - **T07-B** · Estórias US-B1… (uma por RF da área) · `Jcliz` · `area-b`
  - **T07-C** · Estórias US-C1… (uma por RF da área) · `jvecodev` · `area-c`
  - **T07-D** · Estórias US-D1… (uma por RF da área) · `rdsalvesPUC` · `area-d`
  - Rótulos de cada: `ra1`, `item-07`, `por-integrante`, `area-x`
  - Critérios de cada sub-issue: C07.2 a C07.7 para todas as estórias da área (≥2 critérios DADO QUE/QUANDO/ENTÃO por estória)

**T08 · [RA1][Item 08] Relação de Requisitos Não Funcionais (≥16 RNFs)** — tarefa-mãe
- Responsável: quem puxar (consolidação) · Rótulos: `ra1`, `item-08`
- Critérios: C08.1 a C08.5
- Bloqueada por: T03 (pode correr em paralelo com T06 e T07)
- Sub-issues:
  - **T08-A** · RNF-A1…, mínimo 4 (Segurança/LGPD, Compatibilidade) · `eduardofabrii` · `area-a`
  - **T08-B** · RNF-B1…, mínimo 4 (Confiabilidade, Portabilidade) · `Jcliz` · `area-b`
  - **T08-C** · RNF-C1…, mínimo 4 (Eficiência de desempenho, Usabilidade) · `jvecodev` · `area-c`
  - **T08-D** · RNF-D1…, mínimo 4 (Manutenibilidade, Confiabilidade) · `rdsalvesPUC` · `area-d`
  - Rótulos de cada: `ra1`, `item-08`, `por-integrante`, `area-x`
  - Critérios de cada sub-issue: C08.2 a C08.4 para todos os RNFs da área (mínimo 4)

### Fase 3 — Casos de uso (todos + integração)

**T09 · [RA1][Item 09] Diagrama Geral de Casos de Uso**
- Responsável: quem puxar · Rótulos: `ra1`, `item-09`
- Descrição: um único diagrama com todos os casos de uso (no mínimo 16), montado a partir dos RFs de todas as áreas; todo RF coberto por pelo menos um caso de uso (K.3).
- Critérios: C09.1 a C09.7
- Bloqueada por: T06 · Bloqueia: T10

**T10 · [RA1][Item 10] Especificações de Caso de Uso (≥16 especificações)** — tarefa-mãe
- Responsável: quem puxar (consolidação) · Rótulos: `ra1`, `item-10`
- Critérios: C10.1 a C10.9
- Bloqueada por: T07, T09 · Bloqueia: T11
- Sub-issues:
  - **T10-A** · UC-A1…, mínimo 4, com protótipos · `eduardofabrii` · `area-a`
  - **T10-B** · UC-B1…, mínimo 4, com protótipos · `Jcliz` · `area-b`
  - **T10-C** · UC-C1…, mínimo 4, com protótipos · `jvecodev` · `area-c`
  - **T10-D** · UC-D1…, mínimo 4, com protótipos · `rdsalvesPUC` · `area-d`
  - Rótulos de cada: `ra1`, `item-10`, `por-integrante`, `area-x`
  - Critérios de cada sub-issue: C10.2 a C10.9 para todas as especificações da área (mínimo 4) (10 campos, protótipo de alta fidelidade, fluxos básico, alternativo e de exceção)

**T11 · [RA1][Item 11] Diagrama de Atividades**
- Responsável: quem puxar · Rótulos: `ra1`, `item-11`
- Critérios: C11.1 a C11.7
- Bloqueada por: T10

### Fase 4 — Fechamento

**T12 · [RA1][Geral] Revisão cruzada e verificação independente**
- Responsável: quem puxar · Rótulos: `ra1`, `geral`
- Descrição: antes de tudo, rodar a renumeração única dos IDs provisórios (RF-A1… → RF-1…, US-A1… → US001…, RNF-A1… → RNF-1…, UC-A1… → UC01…; ADR-0011), atualizar todas as referências cruzadas e registrar a correspondência em `entregas/ra1-renumeracao.md`. Depois, com todos os MDs na `main`, executar o checklist de consistência cruzada e a verificação independente de todos os IDs (seção 0.3, passo 6, do arquivo de critérios), produzindo a tabela `ID | status | evidência`. Corrigir ou devolver aos responsáveis o que não passar.
- Critérios: K.1 a K.11, X.8, e todos os `Cxx.y` dos itens 1 a 11
- Bloqueada por: T01 a T11

**T13 · [RA1][Geral] Consolidar em PDF e enviar no Canvas**
- Responsável: quem puxar · Rótulos: `ra1`, `geral`
- Descrição: consolidar todos os arquivos MD em um único documento seguindo a estrutura do template (capa com nome do produto, 4 autores e ano 2026; sumário; seções 1 a 11 na ordem e com os títulos originais; quadros no formato do template; diagramas como imagem legível), incluir a declaração de uso de IA preenchida, exportar em **PDF** e enviar na tarefa "Avaliação do RA 1 - Projeto" até **10/10/2026, 23:59**.
- Critérios: X.1 a X.7, X.9, X.10
- Bloqueada por: T12

---

## 4. Corpo padrão de cada issue

```markdown
## Objetivo
<descrição da tarefa>

## Insumos obrigatórios
- Ler `CONTEXT.md` antes de começar.
- Arquivos da pesquisa e decisões indicados para este item em `CONTEXT.md` (seção 9) ou em `pesquisa/README.md`: <links>
- Decisões aplicáveis (`docs/adr/`): <ADRs>

## Critérios de aceite
Referência: `entregas/ra1-criterios-de-aceite.md`
- [ ] <ID> <texto resumido do critério>
- [ ] ...

## Dependências
- Bloqueada por: #<n>, ...
- Bloqueia: #<n>, ...

## Definição de pronto
- Trabalho feito em branch própria, em arquivo(s) MD do repositório (diagramas em Mermaid ou PlantUML, com fonte versionada).
- Todos os critérios acima marcados, cada um com evidência (arquivo e seção, quantidade contada).
- Abrir pull request para a `main` e mover o card para **In review**; outro integrante revisa. Só vai para **Done** após o merge.
```

No corpo, cada critério deve ser **copiado com o texto resumido** do arquivo de critérios, não só o ID, para que quem abre a issue veja o que precisa cumprir.

---

## 5. Instruções para o Claude Code (execução da criação)

**Pré-requisitos:** `gh` autenticado com escopo `project` (`gh auth status`; se faltar, `gh auth refresh -s project`). Repositório: `Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs`. Project: número **1** da organização `Aircraft-Turnaround-Operations-Manager`.

Siga o **protocolo da seção 0.3** de `ra1-criterios-de-aceite.md`: crie uma lista de tarefas com um item por passo abaixo e não encerre com itens abertos.

1. Ler este arquivo e `ra1-criterios-de-aceite.md` por inteiro.
2. Criar os rótulos da seção 2 (ignorar os que já existirem).
3. Criar as 14 issues principais na ordem da seção 3 (T00 a T13), com título, corpo no formato da seção 4, rótulos e responsáveis. Guardar o número de cada uma.
4. Criar as 16 sub-issues (T06-A a T10-D) e vinculá-las como **sub-issues** das tarefas-mãe correspondentes.
5. Preencher as dependências ("Bloqueada por" / "Bloqueia") nos corpos com os números reais das issues. Se disponível, registrar também como relacionamento nativo de bloqueio do GitHub.
6. Adicionar **todas as 30 issues** ao project 1 com Status **Todo**. Não preencher Start date nem Target date.
7. **Verificar**, contando por comando:
   - 30 issues com o rótulo `ra1` no repositório;
   - 30 itens no project 1, todos com Status Todo;
   - 4 tarefas-mãe com 4 sub-issues cada;
   - cada sub-issue com o responsável da tabela 1.2;
   - T01 a T05 com responsável `rdsalvesPUC`; T00, T06 a T13 (principais) sem responsável;
   - nenhum número `#<n>` pendente nos corpos.
8. Relatório final: tabela `Tarefa | nº da issue | responsável | status no project | verificado (sim/não)`.

---

## 6. Pontos em aberto

Todos resolvidos em 29/09/2026:

- **B1.** Atribuição de áreas: **confirmada** conforme a tabela 1.2.
- **B2.** Responsáveis de T00, T09, T11, T12, T13 e das tarefas-mãe T06, T07, T08, T10: **ficam sem responsável**; quem puxar se atribui.
- **B3.** Onde o documento é produzido: **arquivos MD no repositório**, uma branch por tarefa, consolidados em PDF no final (seção 1.3).
