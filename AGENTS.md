# AGENTS.md

## Base de conhecimento do projeto (leia antes de qualquer tarefa de documentação)

1. Leia `CONTEXT.md` (raiz). Ele resume produto, atores, estados, decisões D1–D12 e metas do item 1, e diz o que ler para cada item da especificação.
2. Abra só os arquivos indicados para o seu item (`CONTEXT.md`, seção 9, ou `pesquisa/README.md`). Não leia o relatório consolidado inteiro: `pesquisa/01-referencias-setor-e-similares.md` está congelado e serve só como histórico.
3. Precedência: `docs/adr/` (decisões) > `pesquisa/` (pesquisa vigente) > rascunhos e textos antigos. Não contradiga uma decisão; se algo pedir mudança, registre a dúvida para o grupo em vez de mudar o texto.
4. Ao usar número ou sigla do setor, cite a fonte pelo número de `pesquisa/fontes.md` e separe [Fato] de [Inferência] quando não for óbvio.
5. Use os nomes exatos: produto "Aircraft Turnaround Orchestration System"; atores "Operador de Solo/Rampa", "Coordenador de Turnaround", "Autoridade de Liberação", "Administrador do Sistema" e "Motor de Eventos"; ator abstrato "Usuário" (só no diagrama de casos de uso).
6. Grafo (obrigatório): **antes de escrever ou revisar um item, consulte o grafo** (`graphify-out/`) pelos nós do item e pelos seus termos-chave (IDs, siglas, marcos, atores), com `graphify query`, `explain` e `path` ou com uma busca no `graphify-out/graph.json`, e liste o que se liga a eles em outras áreas, ADRs, critérios e diagramas. Leia esses arquivos antes de escrever; decida sempre pelos arquivos Markdown, porque o grafo pode estar defasado em relação à `main` (confira o `built_at_commit`). Não regenere o grafo em branches de tarefa: ele é regerado só na branch da base de conhecimento ou a partir da `main`, via PR.
7. Arquivo novo de pesquisa segue o mesmo formato: cabeçalho YAML (`id`, `titulo`, `tipo`, `itens_template`, `areas`, `decisoes`, `fontes`, `relacionados`, `status`, `atualizado`) e seção "Ligações" com links Markdown relativos (os links viram ligações no grafo). Decisão nova segue o formato dos ADRs em `docs/adr/` (campos `decisao`, `status`, `data`, `decisor`, `itens_template`, `areas`, `fontes`, `relacionados`).
8. Pendência entre áreas: se o texto que você escreve ou revisa supõe algo que outra área ainda não definiu (um RF, um dado do modelo de tarefas, um RNF), não pare e não invente o requisito da outra área. Registre a suposição como uma linha na issue `pendencia-cruzada` da área que precisa resolver, ou avise quem pediu a tarefa para que ela seja registrada (`entregas/ra1-tarefas.md`, seção 1.4).
9. Siglas (ADR-0008): **toda** sigla vem com o nome em português na primeira ocorrência de cada item da especificação, no formato "nome em português (SIGLA)", inclusive A-CDM e as de órgãos e normas (ANAC, ISO/IEC). Vale também nas regras de negócio. Antes de entregar um texto, confira a primeira ocorrência de cada sigla do item contra o glossário do `CONTEXT.md` (seção 4).

## Agent skills

### Issue tracker

Issues live in this repo's GitHub Issues (`gh` CLI). See `docs/agents/issue-tracker.md`.

### Triage labels

Default vocabulary: `needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`. See `docs/agents/triage-labels.md`.

### Domain docs

Single-context: `CONTEXT.md` + `docs/adr/` at the repo root. See `docs/agents/domain.md`.
