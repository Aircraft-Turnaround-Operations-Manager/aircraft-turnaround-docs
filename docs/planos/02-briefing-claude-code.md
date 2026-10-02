# Briefing para o Claude Code — Fase B da base de conhecimento

> **Para:** uma sessão do Claude Code aberta no computador do Rodrigo, na pasta do repositório `aircraft-turnaround-docs`.
> **De:** Rodrigo Alves (`rdsalvesPUC`), com o Claude (Cowork), em 01/10/2026.
> **Plano completo:** [`01-plano-integracao-base-de-conhecimento.md`](01-plano-integracao-base-de-conhecimento.md). A Fase A (conteúdo) já foi feita no Cowork e está em `_kb-staging/`.
> **Idioma:** português do Brasil em commits, PR, comentários e relatório.
> **Como iniciar:** abra o Claude Code na pasta do repositório e diga: *"Execute o briefing `_kb-staging/docs/planos/02-briefing-claude-code.md` do início ao fim."*

---

## 0. Instrução permanente sobre como encerrar turnos (leia antes de tudo)

Orientação oficial da Anthropic para o Claude Opus 5.5 ("Prompting Claude Opus 5.5", Claude Platform Docs, https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5). Texto mantido no original:

> A standing instruction from the user, the person you are working for. It is about how your turns end. A message with no tool call in it ends your turn, and the work stops there until you are asked to continue. The user has seen you end turns in four ways while work they asked for was still owed, and does not want any of them. One: a long summary of what was done that closes by announcing the next step and has no tool call, so the next thing never starts. Two: an offer to carry on with something unless the user would prefer otherwise, which stops to wait for an answer the user was not going to give. Three: a list of decisions for the user when, by your own account, none of them blocks the rest of the work. Four: deciding that this is a good place to report, because the turn has been long or a milestone is done. Status notes are welcome, and so are your recommendations on open decisions, but put them in the same message as your next tool call and carry on with whatever does not depend on the user's answer. If you notice yourself inviting the user to redirect you or offering to wait, delete it and do the next thing. The stops the user does want are the ones where nothing can move without them, or where the thing blocking you is deliberately protected from you. This does not override the need for confirmation on risky or destructive actions.

Regras práticas:

1. **Lista de tarefas antes de começar,** com **um item por passo B1 a B10** (seção 3). Não agrupe.
2. **Status não é conclusão.** Atualização de progresso vai na mesma mensagem da próxima chamada de ferramenta.
3. **Condição de término:** seção 6. Qualquer outro estado é "em andamento".
4. **Só pare em bloqueio real** — os previstos estão na seção 5. Antes de parar, faça tudo o que não depende do bloqueio. Ao parar, diga **qual passo**, **por quê** e **de onde retomar**.
5. **Espere instalações, builds e subagentes terminarem** antes de dar um passo por concluído.
6. **No máximo duas ou três tentativas automáticas** no mesmo passo; se continuar falhando, pare e descreva.
7. **Ações arriscadas continuam exigindo confirmação** (ver restrições, seção 4).

---

## 1. Contexto mínimo

- O repositório `Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs` guarda a especificação do TCC (itens 1 a 11), uma branch por tarefa e PR para a `main` com revisão de outro integrante.
- A pesquisa de setor foi dividida em arquivos por tema, com metadados e ligações, e as decisões D1–D9 viraram ADRs. Tudo isso está pronto em **`_kb-staging/`** (pasta não versionada), com os mesmos caminhos que devem ter no repositório. A lista exata está no **Anexo A**.
- A árvore de trabalho principal está na branch **`ra1/t02-e-nao-e-faz-nao-faz`**, com trabalho do Rodrigo **não commitado**, incluindo um alinhamento do item 2 feito pelo Cowork. **Nada disso pode ir para os commits desta fase.** Por isso a fase usa **git worktrees** separados.
- Há também uma cópia antiga, não versionada, de `pesquisa/01-referencias-setor-e-similares.md` na árvore principal. A versão que vale é a de `_kb-staging/` (com aviso de congelamento).
- Precedência de conteúdo: decisões (`docs/adr/`) > pesquisa vigente (`pesquisa/`) > rascunhos antigos.

Caminhos (Windows):

| Nome | Caminho |
|---|---|
| Árvore principal | `C:\Users\rdsalves\Documents\Aircraft-Turnaround-Operations-Manager\aircraft-turnaround-docs` |
| Worktree da base | `C:\Users\rdsalves\Documents\Aircraft-Turnaround-Operations-Manager\aircraft-turnaround-docs-kb` |
| Worktree do T01 | `C:\Users\rdsalves\Documents\Aircraft-Turnaround-Operations-Manager\aircraft-turnaround-docs-t01` |
| Repositório remoto | `Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs` |

Os comandos abaixo estão em sintaxe bash (Git Bash). Se o shell for PowerShell, adapte.

---

## 2. Resultado esperado

1. Branch **`ra1/kb-base-de-conhecimento`** com todos os arquivos do Anexo A e o grafo do Graphify em `graphify-out/`, e um **PR** aberto para a `main`.
2. Item 1 alinhado às decisões D1, D2 e D9 na branch do T01.
3. As **30 issues** do RA1 com um comentário de insumos (Anexo B).
4. Graphify instalado no computador do Rodrigo (integração global com o Claude Code, sem arquivos de configuração no repositório).
5. Árvore principal limpa dos arquivos temporários desta fase, sem tocar no trabalho do T02.

---

## 3. Passos

### B1 — Pré-checagem

1. Na árvore principal: `git branch --show-current` (esperado: `ra1/t02-e-nao-e-faz-nao-faz`), `git status --short`, `git fetch origin`.
2. Registrar no relatório quais arquivos aparecem modificados ou não versionados. Esperado: `especificacao/02-e-nao-e-faz-nao-faz.md` (trabalho do T02, **não mexer**), `pesquisa/` e `_kb-staging/` não versionados.
3. `gh auth status` — precisa estar logado com acesso ao repositório (escopos `repo` e, se possível, `project`). Se não estiver, ver seção 5.
4. Conferir que `_kb-staging/` tem exatamente os arquivos do Anexo A (contar; a pasta `_kb-staging/_backup/` não faz parte da base).

### B2 — Worktree da base de conhecimento

1. `git worktree add ../aircraft-turnaround-docs-kb -b ra1/kb-base-de-conhecimento origin/main`
2. **Antes de copiar**, confirmar que os arquivos marcados "novo" no Anexo A não existem na `main`: `git ls-tree -r --name-only origin/main -- .gitignore CLAUDE.md CONTEXT.md docs/adr docs/planos pesquisa claude`. Se algum existir, não sobrescreva: mescle preservando o conteúdo da `main` e registre no relatório. Ler também `docs/agents/domain.md` e registrar se o formato do `CONTEXT.md` e dos ADRs é compatível com o que ele descreve (diferença de formato não bloqueia; só registre).
3. Copiar para a raiz do worktree **todos os arquivos do Anexo A**, a partir de `_kb-staging/`, preservando os caminhos (inclusive `.gitignore`, `.graphifyignore`, `AGENTS.md`, `CLAUDE.md` e os dois arquivos de `entregas/`). Não copiar `_kb-staging/_backup/`.
4. **Conferir os arquivos que já existiam na `main`** (`AGENTS.md`, `entregas/ra1-criterios-de-aceite.md`, `entregas/ra1-tarefas.md`): `git -C ../aircraft-turnaround-docs-kb diff --stat` e `git diff` desses três. O esperado é **só acréscimo**, mais as trocas listadas abaixo:
   - `AGENTS.md`: +12 linhas no topo (título e seção "Base de conhecimento do projeto").
   - `ra1-criterios-de-aceite.md`: +1 linha (K.11 depois do K.10) e, na referência de atores do item 5, "Coordenador/Supervisor de Turnaround" → "Coordenador de Turnaround (ADR-0009)".
   - `ra1-tarefas.md`: bloco "Insumos obrigatórios" no modelo de issue (+5 linhas), "K.1 a K.10" → "K.1 a K.11" no T12 e, na área D da tabela 1.2, "pelo supervisor" → "pelo Coordenador de Turnaround".
   - Se aparecer qualquer outra remoção ou troca, a `main` mudou desde que o staging foi gerado: restaure o arquivo da `main` (`git checkout origin/main -- <arquivo>`) e reaplique à mão só as mudanças listadas acima.
   - Diferença só de fim de linha (CRLF/LF) não conta como mudança de conteúdo; confira com `git diff --ignore-cr-at-eol` ou `--ignore-space-at-eol`.
5. **Verificar os links:** rodar no worktree o script do Anexo C. Todo link relativo dos arquivos do Anexo A precisa apontar para um arquivo que existe. Link quebrado em arquivo que **não** é do Anexo A já existia na `main`: registre e siga, sem corrigir.

### B3 — Commit e push da base (sem o grafo)

1. `git add` **somente** os caminhos do Anexo A (listar explicitamente ou pelas pastas `pesquisa/`, `docs/adr/`, `docs/planos/`, `claude/` mais os arquivos da raiz e de `entregas/`).
2. `git diff --cached --stat` — conferir que não entrou nada fora do Anexo A.
3. Commit: `docs(kb): base de conhecimento — pesquisa por tema, ADRs D1–D9, CONTEXT.md e regras para IAs`.
4. `git push -u origin ra1/kb-base-de-conhecimento`.

### B4 — Pull request

1. `gh pr create --base main --head ra1/kb-base-de-conhecimento` com título **"[RA1][Geral] Base de conhecimento: pesquisa, decisões e regras para IAs"**.
2. Corpo do PR, em português:
   - o que entra (estrutura do plano, seção 2);
   - as decisões D1–D9 (tabela curta com link para cada ADR);
   - a regra de precedência;
   - o que muda para os integrantes (ler `CONTEXT.md`; insumos nas issues; K.11);
   - "O grafo do Graphify entra em commit separado neste PR" (atualize ao fim de B9);
   - evidências de B2 (resultado do verificador de links e do `diff --stat`).
3. Não fazer merge: o processo do grupo exige revisão de outro integrante.

### B5 — Item 1 alinhado às decisões (branch do T01)

1. Ver se o T01 já foi integrado: `gh pr list --state all --head ra1/t01-3-objetivos --json number,state,url`.
   - **PR aberto, fechado sem merge ou inexistente, e a branch `ra1/t01-3-objetivos` existe:** `git worktree add ../aircraft-turnaround-docs-t01 ra1/t01-3-objetivos` e `git -C ../aircraft-turnaround-docs-t01 pull --ff-only` (se houver remota).
   - **PR já integrado, ou a branch não existe:** `git worktree add ../aircraft-turnaround-docs-t01 -b ra1/t01-ajuste-decisoes origin/main`.
   - Se `especificacao/01-3-objetivos.md` não existir ou ainda for o modelo vazio, registre e pule para o passo 6 (não há texto a alinhar).
2. Em `especificacao/01-3-objetivos.md`, aplicar exatamente estas trocas (o texto atual veio da versão do T01 lida em 30/09/2026):

| Trocar | Por | Decisão |
|---|---|---|
| `pelo menos 95% das atividades sejam iniciadas` | `pelo menos 80% das atividades sejam iniciadas` | D2 |
| `pelo menos 95% dos turnarounds estejam prontos para liberação até o horário planejado, com tolerância máxima de 5 minutos` | `pelo menos 80% dos turnarounds estejam prontos para liberação até o horário-alvo de prontidão planejado (TOBT), com tolerância máxima de 5 minutos` | D1, D2 |
| `permitirá ao supervisor redistribuir` | `permitirá ao Coordenador de Turnaround redistribuir` | D9 |
| `Coordenador/Supervisor de Turnaround` (se houver) | `Coordenador de Turnaround` | D9 |

   Se algum trecho não existir com essas palavras, aplique a mesma mudança de sentido no trecho equivalente e registre o antes e o depois no relatório. Não mude mais nada no item. A D3 (antecipação) não muda o texto do item 1: ela vira regra de negócio nos itens 6, 7 e 10.
3. Commit: `docs(item-01): alinhar metas e nomes às decisões D1, D2 e D9`. Push.
4. Se houver PR aberto do T01, comentar nele: "Ajuste conforme ADR-0001, ADR-0002 e ADR-0009 (PR da base de conhecimento #<n>)".
5. Se foi criada a branch `ra1/t01-ajuste-decisoes`, abrir PR para a `main` com esse título e corpo curto.
6. Remover o worktree: `git worktree remove ../aircraft-turnaround-docs-t01`.

### B6 — Comentários de insumos nas 30 issues

1. Listar **todas** as issues com rótulos: `gh issue list --repo Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs --state all --limit 200 --json number,title,labels,assignees`. Ficam as que têm o rótulo `ra1` **ou** algum rótulo `item-NN` ou `geral`. Esperado: 30 (14 principais + 16 sub-issues).
2. Associar cada issue a uma linha do **Anexo B** pelos **rótulos**: `item-NN` dá o item; `area-a` … `area-d` dá a área (sub-issue); sem rótulo de área é a issue principal; `geral` + título dá T00, T12 ou T13. Use o título e o responsável (A = `eduardofabrii`, B = `Jcliz`, C = `jvecodev`, D = `rdsalvesPUC`) só para desempatar. Se a contagem não der 30, ou uma issue não casar com nenhuma linha, registre e siga com as que casaram.
3. Antes de comentar, verificar se já existe comentário com o marcador `<!-- kb-insumos-v1 -->` (`gh api repos/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/issues/<n>/comments --jq '.[].body'`). Se existir, pular.
4. Comentar com o modelo do Anexo B (`gh issue comment <n> --body-file <arquivo>`), trocando `<PR>` pelo número do PR de B4. Grave os arquivos de corpo **fora do repositório** (ex.: `../_kb-backup/comentarios/`).
5. Contar: 30 issues com o comentário (novo ou já existente).

### B7 — Limpeza da árvore principal

Nesta fase **nada é apagado**: os arquivos temporários são **movidos** para `../_kb-backup/`, fora do repositório, e o Rodrigo apaga depois de revisar.

1. Listar o que não é versionado na árvore principal: `git status --short --untracked-files=all -- _kb-staging pesquisa`.
2. Mover `_kb-staging/` inteira para `../_kb-backup/_kb-staging/` (inclui `_backup/`, a cópia do item 2 antes do alinhamento).
3. Mover para `../_kb-backup/pesquisa/` **todo** arquivo não versionado de `pesquisa/` na árvore principal. O esperado é só `pesquisa/01-referencias-setor-e-similares.md` (versão anterior ao aviso de congelamento). Se houver outro arquivo, mova também e registre o nome.
4. **Não** tocar em `especificacao/02-e-nao-e-faz-nao-faz.md` nem em nenhum outro arquivo da branch do T02.
5. `git status --short` na árvore principal: deve sobrar só o trabalho do T02.
6. Se o sistema operacional pedir confirmação para mover arquivos, é uma ação do Rodrigo: peça e siga com B8 enquanto isso não bloquear.

### B8 — Instalar o Graphify

1. `uv --version`. Se não existir: `winget install astral-sh.uv` (se pedir administrador, ver seção 5).
2. `uv tool install graphifyy` (o pacote tem dois "y"; o comando é `graphify`). Conferir com `graphify --version` ou `graphify --help`.
3. `graphify install` — integração **global** com o Claude Code. **Não** usar `--project` (escreveria `.claude/` no repositório) e **não** rodar `graphify hook install` (os ganchos de git regerariam o grafo em branches de tarefa e causariam conflitos no `graph.json`).
4. Se a instalação criar ou alterar arquivos dentro de algum worktree do repositório, não commitar e registrar no relatório.
5. Se a skill do Graphify não estiver disponível nesta sessão depois da instalação, é a parada prevista da seção 5: só pare depois de B1–B7 concluídos.

### B9 — Gerar o grafo e completar o PR

1. Gerar o grafo da pasta do worktree da base, usando a skill do Graphify nesta sessão (equivalente a `/graphify <caminho do worktree>`), para que a leitura dos documentos use o modelo da própria sessão. O `.graphifyignore` já exclui o relatório congelado, `docs/planos/`, `claude/`, `_kb-staging/` e `LICENSE`.
2. Conferir:
   - `graphify-out/` foi criado **na raiz do worktree** (se foi criado em outro lugar, mova para lá) com `graph.json`, `GRAPH_REPORT.md` e `graph.html`;
   - `graph.json` não contém o caminho `pesquisa/01-referencias-setor-e-similares.md`;
   - `GRAPH_REPORT.md` cita `CONTEXT.md`, os ADRs e os tópicos da pesquisa;
   - contar nós e arestas do `graph.json` (com um script curto) e anotar.
3. `.gitignore`: além de `graphify-out/cost.json` (já presente), acrescentar `graphify-out/cache/` se essa pasta existir.
4. Commit: `docs(kb): grafo do Graphify da base de conhecimento`, com `graphify-out/` (sem `cost.json` e sem `cache/`). Push.
5. Atualizar o corpo do PR com: número de nós e arestas, os destaques do `GRAPH_REPORT.md` e a regra "o grafo serve para achar o que ler; decide-se pelos arquivos; regerar só a partir da `main`, via PR".
6. Remover o worktree da base só depois do push: `git worktree remove ../aircraft-turnaround-docs-kb`.

### B10 — Verificação independente e relatório final

1. Rodar um subagente que receba **apenas** este briefing e o acesso ao repositório (branch `ra1/kb-base-de-conhecimento`, PR e issues) e confira cada passo B1–B10 com evidência: arquivos do Anexo A no PR, links válidos (Anexo C), 30 issues comentadas, commit do T01, `graphify-out/` no PR, árvore principal só com o trabalho do T02, nenhuma configuração do Graphify versionada.
2. Corrigir o que o subagente apontar como não atendido.
3. Relatório final ao Rodrigo: a tabela `ID | status | evidência` de B1 a B10, o link do PR, os números das issues comentadas, o hash do commit do T01, nós e arestas do grafo e a lista do que ficou para ele (seção 7). Sem resumo em prosa no lugar da tabela.

---

## 4. Restrições

- Nenhum `push --force`, nenhum merge, nenhum commit direto na `main`.
- Nada do trabalho do T02 entra em commit; `especificacao/02-e-nao-e-faz-nao-faz.md` não é tocado.
- Não editar arquivos de área (`area-a.md` … `area-d.md`) nem itens de outros integrantes.
- Não versionar `.claude/`, `graphify-out/cost.json`, `graphify-out/cache/` nem ganchos.
- Não apagar arquivos nesta fase: B7 **move** os temporários para `../_kb-backup/`.
- Não alterar issues além de adicionar o comentário (sem mudar título, corpo, rótulos ou responsáveis).

---

## 5. Paradas previstas (legítimas)

| Situação | O que fazer antes de parar | Como retomar |
|---|---|---|
| `gh` sem login ou sem acesso | Fazer B1–B3 e B7 (não dependem do `gh`) | Rodrigo roda `gh auth login`; retomar em B4 |
| `winget`/instalação pede administrador ou confirmação na tela | Fazer B1–B7 | Rodrigo instala o `uv`; retomar em B8, item 2 |
| A skill do Graphify não carrega sem reiniciar o Claude Code | Fazer B1–B8 | Rodrigo reinicia o Claude Code na pasta do repositório e pede: "continue o briefing `../aircraft-turnaround-docs-kb/docs/planos/02-briefing-claude-code.md` a partir do passo B9" |
| Conflito inesperado no git (ex.: worktree já existe, branch já existe com outro conteúdo) | Não sobrescrever; descrever o estado | Rodrigo decide |

Em todas as paradas, escreva o passo, o motivo e o ponto de retomada.

---

## 6. Condição de término

B1 a B10 marcados, cada um com evidência (saída de comando, contagem, link ou hash). Qualquer outro estado é "em andamento".

---

## 7. O que fica com o Rodrigo (manual)

- Pedir a revisão do PR a outro integrante e fazer o merge.
- Depois do merge, apagar a branch remota se quiser e rodar `graphify update .` na `main` só quando for regerar o grafo (via PR).
- Colar o texto de `claude/instrucoes-projeto-tcc.md` nas instruções do projeto TCC no claude.ai.
- Revisar o alinhamento do item 2 (diferença em relação a `../_kb-backup/_kb-staging/_backup/`) e commitar quando quiser, na branch do T02.
- Apagar `../_kb-backup/` depois de revisar.

---

## Anexo A — Arquivos da base de conhecimento (conteúdo de `_kb-staging/`)

Total: **44 arquivos**. Os marcados "existente" já estão na `main` e recebem só acréscimos; os demais são novos.

| # | Caminho | Observação |
|---|---|---|
| 1 | `.gitignore` | novo |
| 2 | `.graphifyignore` | novo |
| 3 | `AGENTS.md` | existente na `main` — acréscimo da seção "Base de conhecimento" |
| 4 | `CLAUDE.md` | novo |
| 5 | `CONTEXT.md` | novo |
| 6 | `claude/instrucoes-projeto-tcc.md` | novo |
| 7 | `docs/adr/0001-referencia-horario-tobt-mais-5-min.md` | novo |
| 8 | `docs/adr/0002-metas-percentuais-80.md` | novo |
| 9 | `docs/adr/0003-atualizar-previsao-na-antecipacao.md` | novo |
| 10 | `docs/adr/0004-quatro-atores-e-autoridade-de-liberacao.md` | novo |
| 11 | `docs/adr/0005-abastecimento-com-passageiros-configuravel.md` | novo |
| 12 | `docs/adr/0006-codigos-de-atraso-tabela-anac.md` | novo |
| 13 | `docs/adr/0007-dados-do-operador-e-qr-code.md` | novo |
| 14 | `docs/adr/0008-siglas-a-cdm-com-nome-em-portugues.md` | novo |
| 15 | `docs/adr/0009-nome-coordenador-de-turnaround.md` | novo |
| 16 | `docs/adr/README.md` | novo |
| 17 | `docs/planos/01-plano-integracao-base-de-conhecimento.md` | novo |
| 18 | `docs/planos/02-briefing-claude-code.md` | novo |
| 19 | `entregas/ra1-criterios-de-aceite.md` | existente — acréscimo do K.11 |
| 20 | `entregas/ra1-tarefas.md` | existente — bloco "Insumos obrigatórios" e K.11 no T12 |
| 21 | `pesquisa/01-referencias-setor-e-similares.md` | novo |
| 22 | `pesquisa/README.md` | novo |
| 23 | `pesquisa/fontes.md` | novo |
| 24 | `pesquisa/impacto/impacto-por-item.md` | novo |
| 25 | `pesquisa/impacto/insumos-rfs.md` | novo |
| 26 | `pesquisa/impacto/insumos-rnfs.md` | novo |
| 27 | `pesquisa/impacto/metricas-item-1.md` | novo |
| 28 | `pesquisa/similares/README.md` | novo |
| 29 | `pesquisa/similares/adb-safegate.md` | novo |
| 30 | `pesquisa/similares/assaia.md` | novo |
| 31 | `pesquisa/similares/inform-groundstar.md` | novo |
| 32 | `pesquisa/similares/lacunas-e-diferencial.md` | novo |
| 33 | `pesquisa/similares/matriz-comparativa.md` | novo |
| 34 | `pesquisa/similares/sita.md` | novo |
| 35 | `pesquisa/similares/veovo.md` | novo |
| 36 | `pesquisa/topicos/a-cdm.md` | novo |
| 37 | `pesquisa/topicos/atividades-e-dependencias.md` | novo |
| 38 | `pesquisa/topicos/caminho-critico.md` | novo |
| 39 | `pesquisa/topicos/codigos-de-atraso.md` | novo |
| 40 | `pesquisa/topicos/marcos-e-horarios.md` | novo |
| 41 | `pesquisa/topicos/papeis-e-atores.md` | novo |
| 42 | `pesquisa/topicos/previsibilidade-vs-velocidade.md` | novo |
| 43 | `pesquisa/topicos/referencias-iata.md` | novo |
| 44 | `pesquisa/topicos/tolerancias-e-indicadores.md` | novo |

## Anexo B — Comentário de insumos por issue

Modelo do comentário (trocar `<PR>`, `<LEIA>` e `<ADRS>`):

```markdown
<!-- kb-insumos-v1 -->
## Insumos da base de conhecimento

Antes de escrever, leia o [CONTEXT.md](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/blob/main/CONTEXT.md) e depois só estes arquivos:

<LEIA>

**Decisões que valem para esta tarefa:** <ADRS>. Além delas, [ADR-0008](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/blob/main/docs/adr/0008-siglas-a-cdm-com-nome-em-portugues.md) (siglas) e [ADR-0009](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/blob/main/docs/adr/0009-nome-coordenador-de-turnaround.md) (nome do coordenador) valem para todas as tarefas.

Regra: decisões (`docs/adr/`) > pesquisa (`pesquisa/`) > rascunhos antigos. Números e siglas do setor citam a fonte pelo número de [`pesquisa/fontes.md`](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/blob/main/pesquisa/fontes.md). Novo critério de revisão: **K.11** em `entregas/ra1-criterios-de-aceite.md`.

> Os links valem depois do merge do PR #<PR>.
```

`<LEIA>` vira uma lista de links `https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/blob/main/<caminho>`; `<ADRS>` vira links para `docs/adr/<arquivo>`.

| Tarefa | Como achar a issue | Leia (caminhos) | ADRs |
|---|---|---|---|
| T00 | `[Geral]` + "estrutura" | `pesquisa/README.md` | 0008, 0009 |
| T01 | `[Item 01]` | `pesquisa/impacto/metricas-item-1.md`, `pesquisa/topicos/tolerancias-e-indicadores.md`, `pesquisa/topicos/previsibilidade-vs-velocidade.md` | 0001, 0002, 0003 |
| T02 | `[Item 02]` | `pesquisa/impacto/impacto-por-item.md`, `pesquisa/similares/lacunas-e-diferencial.md` | 0004, 0006, 0007 |
| T03 | `[Item 03]` | `pesquisa/impacto/impacto-por-item.md`, `pesquisa/similares/README.md`, `pesquisa/similares/matriz-comparativa.md`, `pesquisa/similares/lacunas-e-diferencial.md` | 0002, 0007 |
| T04 | `[Item 04]` | `pesquisa/topicos/atividades-e-dependencias.md`, `pesquisa/topicos/caminho-critico.md`, `pesquisa/topicos/marcos-e-horarios.md` | 0004, 0005, 0006, 0007 |
| T05 | `[Item 05]` | `pesquisa/topicos/papeis-e-atores.md` | 0004, 0009 |
| T06 (mãe) | `[Item 06]`, sem área | `pesquisa/impacto/insumos-rfs.md` | 0001, 0003, 0004, 0005, 0006, 0007 |
| T06-A | `[Item 06]` + área A | `pesquisa/impacto/insumos-rfs.md` (linhas A), `pesquisa/topicos/atividades-e-dependencias.md` | 0005 |
| T06-B | `[Item 06]` + área B | `pesquisa/impacto/insumos-rfs.md` (linhas B), `pesquisa/topicos/atividades-e-dependencias.md`, `pesquisa/topicos/codigos-de-atraso.md` | 0006, 0007 |
| T06-C | `[Item 06]` + área C | `pesquisa/impacto/insumos-rfs.md` (linhas C), `pesquisa/topicos/tolerancias-e-indicadores.md`, `pesquisa/topicos/caminho-critico.md` | 0001, 0003 |
| T06-D | `[Item 06]` + área D | `pesquisa/impacto/insumos-rfs.md` (linhas D), `pesquisa/topicos/codigos-de-atraso.md`, `pesquisa/topicos/papeis-e-atores.md` | 0003, 0004, 0006 |
| T07 (mãe) | `[Item 07]`, sem área | `pesquisa/topicos/tolerancias-e-indicadores.md` (regras T8, T11, T12), `pesquisa/impacto/insumos-rfs.md` | 0001, 0003, 0006, 0007 |
| T07-A a D | `[Item 07]` + área | os mesmos arquivos e ADRs da sub-issue T06 da mesma área, mais `pesquisa/topicos/tolerancias-e-indicadores.md` | os da T06 da área + 0003 |
| T08 (mãe) | `[Item 08]`, sem área | `pesquisa/impacto/insumos-rnfs.md` | 0001 |
| T08-A a D | `[Item 08]` + área | `pesquisa/impacto/insumos-rnfs.md` (linhas das características ISO/IEC 25010 da área) | 0001 |
| T09 | `[Item 09]` | `pesquisa/topicos/papeis-e-atores.md`, `pesquisa/impacto/insumos-rfs.md` | 0004 |
| T10 (mãe) | `[Item 10]`, sem área | `pesquisa/topicos/atividades-e-dependencias.md`, `pesquisa/topicos/caminho-critico.md`, `pesquisa/topicos/codigos-de-atraso.md` | 0001, 0003, 0004, 0005, 0006, 0007 |
| T10-A a D | `[Item 10]` + área | os mesmos arquivos e ADRs da sub-issue T06 da mesma área, mais `pesquisa/topicos/atividades-e-dependencias.md` | os da T06 da área + 0005 |
| T11 | `[Item 11]` | `pesquisa/topicos/atividades-e-dependencias.md`, `pesquisa/topicos/caminho-critico.md`, `pesquisa/topicos/papeis-e-atores.md` | 0004, 0005 |
| T12 | `[Geral]` + "revisão" | `docs/adr/README.md`, `entregas/ra1-criterios-de-aceite.md` (K.11) | todas (0001–0009) |
| T13 | `[Geral]` + "PDF" ou "consolidar" | `pesquisa/topicos/marcos-e-horarios.md` (glossário de siglas) | 0008, 0009 |

Nomes dos arquivos dos ADRs:

| ADR | Arquivo |
|---|---|
| 0001 | `docs/adr/0001-referencia-horario-tobt-mais-5-min.md` |
| 0002 | `docs/adr/0002-metas-percentuais-80.md` |
| 0003 | `docs/adr/0003-atualizar-previsao-na-antecipacao.md` |
| 0004 | `docs/adr/0004-quatro-atores-e-autoridade-de-liberacao.md` |
| 0005 | `docs/adr/0005-abastecimento-com-passageiros-configuravel.md` |
| 0006 | `docs/adr/0006-codigos-de-atraso-tabela-anac.md` |
| 0007 | `docs/adr/0007-dados-do-operador-e-qr-code.md` |
| 0008 | `docs/adr/0008-siglas-a-cdm-com-nome-em-portugues.md` |
| 0009 | `docs/adr/0009-nome-coordenador-de-turnaround.md` |

## Anexo C — Verificador de links

Rodar na raiz do worktree (`python verificar_links.py` ou colar no `python -`). Não versionar o script.

```python
import os, re, sys
ruins = []
for raiz, pastas, arquivos in os.walk('.'):
    if '.git' in raiz.split(os.sep) or 'graphify-out' in raiz:
        continue
    for nome in arquivos:
        if not nome.endswith('.md'):
            continue
        caminho = os.path.join(raiz, nome)
        texto = open(caminho, encoding='utf-8').read()
        texto = re.sub(r'```.*?```', '', texto, flags=re.S)
        for alvo in re.findall(r'\]\(([^)\s]+)\)', texto):
            if re.match(r'^(https?:|mailto:|#)', alvo):
                continue
            arquivo = alvo.split('#')[0]
            if not arquivo:
                continue
            destino = os.path.normpath(os.path.join(os.path.dirname(caminho), arquivo))
            if not os.path.exists(destino):
                ruins.append(f'{caminho} -> {alvo}')
print(f'links quebrados: {len(ruins)}')
print('\n'.join(ruins))
sys.exit(1 if ruins else 0)
```
