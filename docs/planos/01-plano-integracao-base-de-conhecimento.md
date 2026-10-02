# Plano de execução — Pesquisa como base de conhecimento do projeto

> **Projeto:** TCC — Aircraft Turnaround Orchestration System (org. GitHub `Aircraft-Turnaround-Operations-Manager`, repositório `aircraft-turnaround-docs`).
> **Pedido de:** Rodrigo Alves (`rdsalvesPUC`), em 01/10/2026.
> **Elaborado por:** Claude (Cowork).
> **Objetivo:** transformar a pesquisa `pesquisa/01-referencias-setor-e-similares.md` e as decisões D1–D9 em uma base de conhecimento que toda IA e todo integrante consultem antes de escrever qualquer parte da documentação.
> **Execução em duas fases:** **Fase A** no Cowork (conteúdo) e **Fase B** no Claude Code, no computador do Rodrigo (git, Graphify, PR e issues). A Fase B tem um briefing próprio: [`02-briefing-claude-code.md`](02-briefing-claude-code.md).

---

## 0. Instrução permanente sobre como encerrar turnos (bloco de parada)

Vale para a Fase A e para a Fase B. É a orientação oficial da Anthropic para o Claude Opus 5.5 (página "Prompting Claude Opus 5.5", Claude Platform Docs, https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5, acessada em 01/10/2026). O modelo tende a encerrar o turno no meio de tarefas longas, porque trata uma mensagem só de texto (um resumo, um status) como conclusão. Aqui isso **não** vale.

Texto oficial, mantido no original:

> A standing instruction from the user, the person you are working for. It is about how your turns end. A message with no tool call in it ends your turn, and the work stops there until you are asked to continue. The user has seen you end turns in four ways while work they asked for was still owed, and does not want any of them. One: a long summary of what was done that closes by announcing the next step and has no tool call, so the next thing never starts. Two: an offer to carry on with something unless the user would prefer otherwise, which stops to wait for an answer the user was not going to give. Three: a list of decisions for the user when, by your own account, none of them blocks the rest of the work. Four: deciding that this is a good place to report, because the turn has been long or a milestone is done. Status notes are welcome, and so are your recommendations on open decisions, but put them in the same message as your next tool call and carry on with whatever does not depend on the user's answer. If you notice yourself inviting the user to redirect you or offering to wait, delete it and do the next thing. The stops the user does want are the ones where nothing can move without them, or where the thing blocking you is deliberately protected from you. This does not override the need for confirmation on risky or destructive actions.

Regras práticas derivadas dela:

1. **Lista de tarefas antes de começar,** com um item por entrada do checklist da fase (seções 4 e 5). Não agrupe itens.
2. **Status não é conclusão.** Uma atualização de progresso vai na mesma mensagem da próxima chamada de ferramenta.
3. **Condição de término declarada** (seção 6). Qualquer outro estado é "em andamento".
4. **Só pare em bloqueio real** (algo que só o Rodrigo pode fazer, ou que está protegido de propósito). Ao parar, diga **qual item** está bloqueado, **por quê** e **de onde retomar**, e continue antes com tudo o que não depende do bloqueio.
5. **Espere processos em segundo plano** (subagentes, builds, instalações) antes de dar um item por concluído.
6. **Não pergunte o que não bloqueia.** Decisões em aberto viram recomendação no relatório final.
7. **Limite de retomadas automáticas:** no máximo duas ou três na mesma tarefa; se continuar travado, pare e descreva o bloqueio.
8. **Isto não dispensa confirmação** para ações arriscadas ou destrutivas (apagar arquivos do usuário, `push --force`, merge sem revisão).

---

## 1. Decisões que este plano aplica

| Decisão | Resumo | ADR |
|---|---|---|
| D1 | Referência de horário: TOBT planejado + 5 min, unilateral | `docs/adr/0001` |
| D2 | Metas percentuais do item 1: 80% | `docs/adr/0002` |
| D3 | Antecipação de 5 min ou mais exige atualizar a previsão | `docs/adr/0003` |
| D4 | 4 atores; Autoridade de Liberação = representante da companhia; "Liberado" não é autorização do ATC | `docs/adr/0004` |
| D5 | Abastecimento com passageiros a bordo: regra configurável por operador | `docs/adr/0005` |
| D6 | Códigos de atraso: tabela completa da ANAC (72 códigos, siglas IATA AHM 730) | `docs/adr/0006` |
| D7 | Dados registrados pelo operador, inclusive QR Code lido pelo celular; sem sensores da aeronave nem câmeras fixas | `docs/adr/0007` |
| D8 | Siglas do A-CDM com nome em português | `docs/adr/0008` |
| D9 | Nome único: "Coordenador de Turnaround" | `docs/adr/0009` |

---

## 2. Arquitetura da base de conhecimento

Três camadas, nesta ordem de autoridade:

1. **Fonte oficial (Markdown no repositório):**
   - `CONTEXT.md` — porta de entrada curta, lida por toda IA antes de qualquer tarefa.
   - `docs/adr/` — uma decisão por arquivo (D1–D9).
   - `pesquisa/` — a pesquisa dividida por tema, cada arquivo com cabeçalho YAML de metadados e uma seção **Ligações** com links Markdown para decisões, itens da especificação, tópicos relacionados e fontes.
2. **Índice em grafo (Graphify):** `graphify-out/` (`graph.json`, `GRAPH_REPORT.md`, `graph.html`), gerado a partir da camada 1 e versionado. Serve para **achar** o que ler; nunca para decidir.
3. **Regras para as IAs:** `AGENTS.md` (lido por Codex, Copilot, Cursor e outros), `CLAUDE.md` (importa o `AGENTS.md` para o Claude Code) e as instruções do projeto TCC no claude.ai.

**Regra de precedência:** decisões (`docs/adr/`) > pesquisa vigente (`pesquisa/`) > rascunhos e textos antigos. O relatório consolidado original fica congelado como histórico e fora do grafo.

Estrutura final:

```
CONTEXT.md
CLAUDE.md
AGENTS.md                      (seção nova: Base de conhecimento)
.graphifyignore
.gitignore                     (linha do graphify-out/cost.json)
docs/adr/README.md, 0001…0009
docs/planos/01-plano…, 02-briefing-claude-code.md
claude/instrucoes-projeto-tcc.md (texto para as instruções do projeto no claude.ai)
pesquisa/README.md             (mapa: resumo, índices por item e por área, diagrama)
pesquisa/fontes.md             (64 fontes, numeração original)
pesquisa/topicos/              (9 arquivos: P1.1 a P1.9)
pesquisa/similares/            (seleção, 5 fichas, matriz, lacunas e diferencial)
pesquisa/impacto/              (métricas do item 1, impacto por item, insumos RF e RNF)
pesquisa/01-referencias-setor-e-similares.md   (congelado)
graphify-out/                  (gerado na Fase B)
```

---

## 3. Onde a Fase A grava

Para não misturar com o trabalho em andamento na branch `ra1/t02-e-nao-e-faz-nao-faz`, a Fase A grava tudo numa pasta de preparação **não versionada**: `aircraft-turnaround-docs/_kb-staging/`, com os mesmos caminhos da estrutura final. A Fase B copia essa pasta para uma árvore de trabalho separada (git worktree) criada a partir da `main`, faz o commit lá e, no fim, move a pasta de preparação para fora do repositório.

Exceção: o item 2 (`especificacao/02-e-nao-e-faz-nao-faz.md`) está em edição na branch atual e recebe o alinhamento às decisões direto no arquivo, **sem commit** (passo A11).

---

## 4. Fase A — Cowork (conteúdo)

| ID | Entrega | Evidência esperada |
|---|---|---|
| A1 | Este plano, com o bloco de parada | `docs/planos/01-…` |
| A2 | `pesquisa/topicos/` — 9 arquivos (seções 2.1 a 2.9 do relatório) | 9 arquivos, cada um com YAML, "Decisões vigentes" e "Ligações" |
| A3 | `pesquisa/similares/` — seleção, 5 fichas, matriz, lacunas e diferencial (com DF5) | 8 arquivos |
| A4 | `pesquisa/impacto/` — métricas do item 1, impacto por item, insumos de RF e RNF, já com as decisões aplicadas | 4 arquivos |
| A5 | `pesquisa/fontes.md`, `pesquisa/README.md` (mapa) e aviso de congelamento no relatório original | 64 fontes; mapa com índices e diagrama |
| A6 | `docs/adr/` — 9 ADRs e índice | 10 arquivos |
| A7 | `CONTEXT.md` | 1 arquivo, curto |
| A8 | `AGENTS.md` (seção nova), `CLAUDE.md`, `.graphifyignore`, `.gitignore` e texto das instruções do projeto TCC | 4 arquivos no staging + 1 doc no projeto |
| A9 | K.11 em `entregas/ra1-criterios-de-aceite.md` e bloco "Insumos obrigatórios" no modelo de issue de `entregas/ra1-tarefas.md` | 2 arquivos no staging |
| A10 | Briefing da Fase B | `docs/planos/02-briefing-claude-code.md` |
| A11 | Alinhar o item 2 (em edição) às decisões D6, D7 e D9, sem commit | diferenças listadas no relatório final |
| A12 | Gravar tudo em `_kb-staging/` e no projeto TCC; conferir | contagem de arquivos e md5 |
| A13 | Verificação independente da Fase A (subagente) | tabela `ID \| status \| evidência`; correções feitas |

---

## 5. Fase B — Claude Code (resumo; o detalhe está no briefing)

| ID | Entrega |
|---|---|
| B1 | Pré-checagem: branch atual, `git status` no Windows, `gh auth status`, conteúdo de `_kb-staging/` |
| B2 | Worktree `ra1/kb-base-de-conhecimento` a partir de `origin/main`; cópia do staging; conferência das diferenças e dos links |
| B3 | Commit e push da base de conhecimento (sem o grafo) |
| B4 | Abrir o PR da base de conhecimento (com evidências) |
| B5 | Alinhar o item 1 às decisões D1, D2 e D9 na branch do T01, commit e push |
| B6 | Comentar as 30 issues do RA1 com os insumos de cada uma |
| B7 | Limpeza da árvore principal: **mover** `_kb-staging/` (com o backup do item 2) e a cópia antiga de `pesquisa/` para `../_kb-backup/`, fora do repositório; nada é apagado |
| B8 | Instalar `uv` e Graphify (`graphifyy`), integração global com o Claude Code |
| B9 | Gerar o grafo no worktree, conferir `graphify-out/`, commit, push e atualização do PR |
| B10 | Verificação independente da Fase B e relatório final |

A ordem põe o Graphify por último de propósito: se for preciso reiniciar o Claude Code para carregar a skill, todo o resto já está feito.

**Paradas previstas (legítimas):** `gh` sem login; instalação que peça permissão de administrador; necessidade de reiniciar o Claude Code para carregar a skill do Graphify. Em todas, o Claude Code segue antes com o que não depende delas e diz de qual passo retomar.

**Manual (Rodrigo):** colar o texto de `claude/instrucoes-projeto-tcc.md` nas instruções do projeto TCC no claude.ai; pedir a revisão do PR a outro integrante e fazer o merge.

---

## 6. Condição de término

O trabalho só está concluído quando **A1–A13** e **B1–B10** estiverem marcados, cada um com evidência (arquivo, contagem, link do PR, número das issues comentadas). O relatório final de cada fase é a tabela `ID | status | evidência`, não um resumo em prosa.

---

## 7. Restrições

- Nenhum `push --force`, nenhum merge sem revisão de outro integrante, nenhum commit direto na `main`.
- Não commitar nada do trabalho em andamento da branch `ra1/t02-…`.
- Não editar os arquivos de área (`area-a.md` … `area-d.md`) de outros integrantes.
- Não versionar ganchos do Graphify (`.claude/settings*.json`) no repositório: quem não tem o Graphify instalado teria erros.
- O grafo é regerado só na branch da base de conhecimento e, depois, na `main` (via PR), nunca em branches de tarefa, para evitar conflitos no `graph.json`.

---

## 8. Riscos e mitigação

| Risco | Mitigação |
|---|---|
| Arquivos aparecem todos como modificados por diferença de fim de linha | Conferir com `git diff --stat` no Windows; commitar só os caminhos listados |
| Graphify grava `graphify-out/` fora do worktree | Conferir o caminho e mover para a raiz do worktree |
| Conflito no `graph.json` em PRs futuros | Regerar só na `main`, por uma pessoa, depois dos merges |
| Links das issues apontam para a `main` antes do merge | Comentário avisa que os links valem após o merge do PR da base |
| Skill nova não carrega sem reiniciar | Parada legítima com ponto de retomada (B9), depois de B1–B8 |
