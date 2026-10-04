# aircraft-turnaround-docs

Documentação do **Aircraft Turnaround Orchestration System**, projeto da disciplina Especificação de Software (PSI151), BSI PUCPR, 6º período, 2026.

O sistema orquestra o *turnaround* de aeronaves: o intervalo entre a chegada à posição (in-block) e a saída (off-block). O objetivo não é encurtar o turnaround, e sim garantir que ele aconteça **dentro do planejado**.

Este repositório não tem código do sistema. Ele guarda três coisas:

1. a **especificação** que o grupo entrega na disciplina (pasta `especificacao/`);
2. a **base de conhecimento** que sustenta a especificação: pesquisa do setor, decisões e regras de escrita;
3. o **processo** de trabalho do grupo: plano de tarefas, critérios de aceite e convenções.

| Integrante | GitHub | Área funcional |
|---|---|---|
| Eduardo Fabri | `eduardofabrii` | A: acesso e planejamento |
| João Pedro Cardoso de Liz | `Jcliz` | B: execução em solo |
| João Vitor Correa Oliveira | `jvecodev` | C: monitoramento |
| Rodrigo Alves | `rdsalvesPUC` | D: exceções e liberação |

## Comece por aqui

Antes de escrever qualquer parte da especificação, leia nesta ordem:

1. **[`CONTEXT.md`](CONTEXT.md)**: resumo do que já está decidido (produto, atores, estados, siglas, decisões D1 a D10, metas). A seção 9 dele diz o que ler para cada item.
2. **A issue da sua tarefa** no board [Especificação de Software - 6p](https://github.com/orgs/Aircraft-Turnaround-Operations-Manager/projects/1). Cada issue tem os critérios de aceite e um comentário "Insumos da base de conhecimento" com os arquivos e as decisões que valem para ela.
3. **Só os arquivos de pesquisa indicados** para o seu item. Não é preciso ler a pesquisa inteira.

## Mapa do repositório

```
.
├── README.md                  este arquivo
├── CONTEXT.md                 porta de entrada: o que está decidido e o que ler para cada item
├── AGENTS.md                  regras para assistentes de IA (Codex, Copilot, Cursor e outros)
├── CLAUDE.md                  faz o Claude Code carregar o AGENTS.md e o CONTEXT.md
│
├── especificacao/             a entrega: itens 1 a 11 do template da disciplina
├── entregas/                  plano de tarefas e critérios de aceite de cada entrega
│
├── pesquisa/                  pesquisa do setor e de produtos similares, dividida por tema
├── docs/
│   ├── adr/                   decisões do projeto (D1 a D10), uma por arquivo
│   ├── agents/                configuração das skills de IA (issues, rótulos, documentos de domínio)
│   └── planos/                planos de execução já concluídos (histórico)
├── claude/                    texto das instruções do projeto TCC no claude.ai
│
├── graphify-out/              grafo de conhecimento gerado a partir dos arquivos acima
├── .graphifyignore            o que fica fora do grafo
└── .gitignore
```

## Especificação (`especificacao/`)

Há um arquivo ou pasta por item do template, com o número e o título original. O documento final é a concatenação dos arquivos `.md` desta pasta em **ordem alfabética de caminho**, que coincide com a ordem do template.

```
especificacao/
├── 01-3-objetivos.md
├── 02-e-nao-e-faz-nao-faz.md
├── 03-visao-do-produto.md
├── 04-mapeamento-de-negocios.md
├── 05-atores-usuarios.md
├── 06-requisitos-funcionais/        00-item.md + area-a.md … area-d.md
├── 07-estorias-de-usuario/          00-item.md + area-a.md … area-d.md
├── 08-requisitos-nao-funcionais/    00-item.md + area-a.md … area-d.md
├── 09-diagrama-geral-de-casos-de-uso.md
├── 10-especificacoes-de-caso-de-uso/
│   ├── 00-item.md + area-a.md … area-d.md
│   └── prototipos/                  imagens dos protótipos de tela (ucNN-<tela>.png)
├── 11-diagrama-de-atividades.md
└── diagramas/                       fonte e imagem exportada de cada diagrama
```

- **Itens por integrante (6, 7, 8 e 10):** cada área edita **apenas o seu `area-x.md`**, assim não há conflito de merge. O `00-item.md` é da tarefa-mãe, que consolida.
- **Tabelas dos itens 6 e 8:** cada `area-x.md` tem a tabela com o mesmo cabeçalho do template. Na consolidação, as 4 tabelas viram uma só.
- **Numeração fixa por área:** A = RF-1 a RF-4, B = RF-5 a RF-8, C = RF-9 a RF-12, D = RF-13 a RF-16. O mesmo vale para USnnn, UCnn e RNF-n.
- **Diagramas:** escritos como código em Mermaid (`.mmd`) ou PlantUML (`.puml`). A fonte e o `.png` exportado ficam juntos em `especificacao/diagramas/`, com o mesmo nome base (`04-bpmn-to-be`, `09-casos-de-uso`, `11-atividades`).
- **Comentários `<!-- ... -->`** nos arquivos ainda não preenchidos são orientações para quem escreve. Apague-os quando o item estiver pronto.
- **Nome do produto:** sempre "Aircraft Turnaround Orchestration System", exatamente assim.

O andamento de cada item está no board, e não neste arquivo.

## Entregas (`entregas/`)

- [`ra1-tarefas.md`](entregas/ra1-tarefas.md): o plano do RA1. Divide os itens 1 a 11 em 30 tarefas, com responsáveis, dependências e o modelo de issue.
- [`ra1-criterios-de-aceite.md`](entregas/ra1-criterios-de-aceite.md): a definição de pronto. Lista o que cada item precisa ter para valer a nota máxima da rubrica (`C01.1` … `C11.7`), as regras gerais do documento (`X.1` a `X.10`) e a revisão cruzada (`K.1` a `K.11`).

Prazo do RA1: **10/10/2026, 23:59**, em PDF, no Canvas.

## Base de conhecimento

### Por que existe

A especificação fala de um domínio técnico (operação de solo em aeroportos) e é escrita por quatro pessoas, com ajuda de assistentes de IA. Sem uma referência comum, cada parte usaria números, siglas e nomes diferentes. A base de conhecimento resolve isso:

- **Sustenta as afirmações.** Metas e regras da especificação se apoiam em fontes do setor, e não em suposição. Exemplo: a tolerância de 5 minutos em torno do horário-alvo de prontidão (TOBT) vem das especificações de A-CDM da EUROCONTROL.
- **Mantém todos alinhados.** Os mesmos nomes de atores, estados e siglas aparecem em todos os itens.
- **Registra as decisões.** Quando o grupo escolhe entre opções, a escolha e o motivo ficam escritos.

### As três camadas

| Camada | Onde fica | Para que serve |
|---|---|---|
| **Decisões** | [`docs/adr/`](docs/adr/README.md) | O que o grupo decidiu (D1 a D10), uma decisão por arquivo, com contexto, opções e consequências. |
| **Pesquisa** | [`pesquisa/`](pesquisa/README.md) | O que o setor faz e o que os produtos similares oferecem, com fonte. |
| **Resumo** | [`CONTEXT.md`](CONTEXT.md) | O essencial das duas camadas acima, em uma página. |

**Regra de precedência:** decisões > pesquisa vigente > rascunhos e textos antigos. Se um item da especificação precisar contrariar uma decisão, não mude o texto por conta própria: leve a dúvida ao grupo.

### Pesquisa (`pesquisa/`)

```
pesquisa/
├── README.md        mapa: índices por item do template e por área, e resumo
├── fontes.md        lista única de fontes, numeradas
├── topicos/         9 temas do setor: A-CDM, marcos e horários, tolerâncias, previsibilidade,
│                    atividades e dependências, caminho crítico, papéis, códigos de atraso, IATA
├── similares/       5 produtos de mercado, matriz comparativa, lacunas e diferenciais
├── impacto/         o que a pesquisa muda em cada item: métricas, insumos para RFs e RNFs
└── 01-referencias-setor-e-similares.md    relatório original, congelado (só histórico)
```

Como usar:

- **Cite a fonte** ao usar número ou sigla do setor, pelo número de `pesquisa/fontes.md`. Exemplo: "tabela de códigos de atraso da ANAC [62]". O critério K.11 cobra isso na revisão.
- **Separe fato de inferência.** Os arquivos de pesquisa marcam cada afirmação como [Fato] ou [Inferência], e o que vem de material de fornecedor aparece como "declarado pelo fornecedor".
- **Sigla com nome em português** na primeira ocorrência de cada item (ADR-0008). O glossário está no `CONTEXT.md`, seção 4.
- **Fonte nova** entra no fim de `fontes.md`, com o próximo número. A numeração existente nunca muda.
- **Arquivo novo de pesquisa** segue o formato dos existentes: cabeçalho YAML de metadados e seção "Ligações" no fim, com links relativos.

### Decisões (`docs/adr/`)

Cada arquivo `NNNN-titulo.md` registra uma decisão: contexto, opções consideradas, decisão e consequências. O índice está em [`docs/adr/README.md`](docs/adr/README.md). Uma decisão nova recebe o próximo número e segue o mesmo formato.

## Grafo de conhecimento (`graphify-out/`)

### O que é

O [Graphify](https://github.com/Graphify-Labs/graphify) lê os arquivos Markdown do repositório e monta um grafo: cada conceito, decisão, fonte ou item da especificação vira um nó, e cada relação entre eles vira uma ligação. O grafo ajuda a responder "o que eu preciso ler sobre X?" e "o que mais depende desta decisão?".

**O grafo serve para achar o que ler. A decisão é sempre tomada pelos arquivos Markdown.**

| Arquivo | O que é |
|---|---|
| `graph.html` | Visualização interativa do grafo. |
| `GRAPH_REPORT.md` | Resumo em texto: nós mais conectados, conexões inesperadas e comunidades. |
| `graph.json` | O grafo em si, usado pelas consultas. |
| `manifest.json` | Registro do estado de cada arquivo na última geração, para a atualização incremental. |
| `.graphify_labels.json` | Nomes das comunidades. |

Ficam fora do grafo (`.graphifyignore`): o relatório de pesquisa congelado, `docs/planos/`, `claude/` e `LICENSE`.

### Como abrir

Não precisa instalar nada. Dê dois cliques em `graphify-out/graph.html`, ou rode:

```bash
start graphify-out/graph.html
```

A página precisa de internet, porque carrega a biblioteca de desenho da web. Nela:

- arraste o fundo para mover e use a rodinha do mouse para dar zoom;
- clique em um nó para ver o arquivo de origem e as ligações dele;
- use a busca no canto superior direito para achar um conceito;
- desmarque comunidades na lateral para ver uma área de cada vez.

Para ler sem abrir o navegador, use o [`GRAPH_REPORT.md`](graphify-out/GRAPH_REPORT.md).

### Como consultar pelo terminal (opcional)

Requer o Graphify instalado (ver abaixo). Rode na raiz do repositório:

```bash
graphify query "como o atraso é medido?"
```

```bash
graphify explain "context_tobt"
```

```bash
graphify path "context_tobt" "especificacao_03_visao_do_produto_item" --undirected
```

`query` busca os nós ligados a uma pergunta, `explain` descreve um nó e seus vizinhos, e `path` mostra o caminho entre dois nós. Quando um nome é ambíguo, o comando lista os identificadores possíveis.

### Como instalar o Graphify (opcional)

Só é necessário para consultar pelo terminal ou para regerar o grafo.

```bash
winget install astral-sh.uv
```

```bash
uv tool install graphifyy
```

```bash
graphify install
```

O pacote se chama `graphifyy`, com dois "y"; o comando é `graphify`. O último comando instala a skill `/graphify` no Claude Code, de forma global. **Não** use `graphify install --project` nem `graphify hook install` neste repositório: eles gravariam configuração e ganchos de git que quebrariam o trabalho de quem não tem o Graphify.

### Como atualizar o grafo

O grafo é regerado **só a partir da `main`, por pull request, depois que os PRs de conteúdo forem integrados**. Nunca regere em branch de tarefa: duas pessoas alterando o `graph.json` ao mesmo tempo geram conflito.

1. Atualize a `main` local e crie uma branch (por exemplo, `ra1/kb-atualizar-grafo`).
2. No Claude Code, na raiz do repositório, rode `/graphify . --update`. Ele reextrai só os arquivos que mudaram.
3. Confira o resultado: o `GRAPH_REPORT.md` cita os arquivos alterados, e o `graph.json` não contém o relatório congelado nem caminhos da sua máquina.
4. Faça commit de `graphify-out/` e abra o PR.

Dois cuidados:

- O comando `graphify update .` do terminal **não serve** para este repositório. Ele só reprocessa código-fonte, e aqui tudo é Markdown, que precisa da skill do Claude Code.
- Se o grafo novo ficar menor que o anterior, o Graphify se recusa a gravar. Confira quais nós saíram antes de forçar a gravação.

## Como trabalhamos

### Tarefas e board

- As tarefas do RA1 são issues com o rótulo `ra1`, no board [Especificação de Software - 6p](https://github.com/orgs/Aircraft-Turnaround-Operations-Manager/projects/1).
- Os itens 6, 7, 8 e 10 têm uma tarefa-mãe e 4 sub-issues, uma por área.
- Quem puxar uma tarefa sem responsável se atribui e move o card para **In progress**.

### Branches e pull requests

- Uma branch por tarefa, no padrão `ra1/<tarefa>-<descricao-curta>`, em minúsculas e sem acentos. Exemplos: `ra1/t05-atores`, `ra1/t06-a-rfs-area-a`.
- Nada entra na `main` sem **pull request**. O título do PR é o título da issue, e o corpo traz `Closes #<n>` e a evidência de cada critério de aceite.
- Com o PR aberto, o card vai para **In review**. Outro integrante revisa, e o card vai para **Done** depois do merge.
- Ajuste em um item já integrado segue o mesmo caminho: branch, PR e revisão.

### Definição de pronto de uma tarefa

1. Todos os critérios de aceite da issue atendidos, cada um com evidência (arquivo, seção, contagem).
2. Nenhuma contradição com o `CONTEXT.md` nem com as decisões.
3. Números e siglas do setor com a fonte citada.
4. PR revisado por outro integrante.

### Consolidação e envio

Quando todos os itens estiverem na `main`, os arquivos de `especificacao/` são consolidados em um único documento, com capa, sumário, seções 1 a 11 e a declaração de uso de IA, e exportados em PDF. Antes disso acontece a revisão cruzada (tarefa T12), que percorre todos os critérios.

## Assistentes de IA

O grupo usa assistentes de IA para escrever e revisar. Estes arquivos fazem todos seguirem as mesmas regras:

| Arquivo | Quem lê | O que faz |
|---|---|---|
| [`AGENTS.md`](AGENTS.md) | Codex, Copilot, Cursor e outros | Manda ler o `CONTEXT.md`, respeitar a precedência, citar fontes e usar os nomes exatos. |
| [`CLAUDE.md`](CLAUDE.md) | Claude Code | Carrega o `AGENTS.md` e o `CONTEXT.md` automaticamente. |
| [`claude/instrucoes-projeto-tcc.md`](claude/instrucoes-projeto-tcc.md) | Projeto no claude.ai | Texto para colar nas instruções do projeto. Não é aplicado sozinho. |
| [`docs/agents/`](docs/agents/) | Skills de engenharia | Dizem onde ficam as issues, quais rótulos de triagem existem e onde está a documentação de domínio. |

O plano de ensino exige declarar o uso de IA no documento final (critério X.7).

## Licença

[MIT](LICENSE).
