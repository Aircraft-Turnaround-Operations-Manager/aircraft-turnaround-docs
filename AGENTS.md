# AGENTS.md

## Base de conhecimento do projeto (leia antes de qualquer tarefa de documentação)

1. Leia `CONTEXT.md` (raiz). Ele resume produto, atores, estados, decisões D1–D10 e metas do item 1, e diz o que ler para cada item da especificação.
2. Abra só os arquivos indicados para o seu item (`CONTEXT.md`, seção 9, ou `pesquisa/README.md`). Não leia o relatório consolidado inteiro: `pesquisa/01-referencias-setor-e-similares.md` está congelado e serve só como histórico.
3. Precedência: `docs/adr/` (decisões) > `pesquisa/` (pesquisa vigente) > rascunhos e textos antigos. Não contradiga uma decisão; se algo pedir mudança, registre a dúvida para o grupo em vez de mudar o texto.
4. Ao usar número ou sigla do setor, cite a fonte pelo número de `pesquisa/fontes.md` e separe [Fato] de [Inferência] quando não for óbvio.
5. Use os nomes exatos: produto "Aircraft Turnaround Orchestration System"; atores "Operador de Solo/Rampa", "Coordenador de Turnaround", "Autoridade de Liberação", "Administrador do Sistema" e "Motor de Eventos"; ator abstrato "Usuário" (só no diagrama de casos de uso).
6. Grafo: se existir `graphify-out/`, use `graphify-out/GRAPH_REPORT.md` (ou a consulta do Graphify) para **achar** o que ler; decida sempre pelos arquivos Markdown. Não regenere o grafo em branches de tarefa: ele é regerado só na branch da base de conhecimento ou a partir da `main`, via PR.
7. Arquivo novo de pesquisa segue o mesmo formato: cabeçalho YAML (`id`, `titulo`, `tipo`, `itens_template`, `areas`, `decisoes`, `fontes`, `relacionados`, `status`, `atualizado`) e seção "Ligações" com links Markdown relativos (os links viram ligações no grafo). Decisão nova segue o formato dos ADRs em `docs/adr/` (campos `decisao`, `status`, `data`, `decisor`, `itens_template`, `areas`, `fontes`, `relacionados`).

## Agent skills

### Issue tracker

Issues live in this repo's GitHub Issues (`gh` CLI). See `docs/agents/issue-tracker.md`.

### Triage labels

Default vocabulary: `needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`. See `docs/agents/triage-labels.md`.

### Domain docs

Single-context: `CONTEXT.md` + `docs/adr/` at the repo root. See `docs/agents/domain.md`.
