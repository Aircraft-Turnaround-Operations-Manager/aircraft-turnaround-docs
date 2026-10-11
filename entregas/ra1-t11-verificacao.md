# T11 — Verificação do diagrama de atividades (#12)

Condição de conclusão: C11.1–C11.7 atendidos com evidência, fontes e imagens versionadas, PR aberto e card em In review. O merge depende da revisão por outro integrante e da conclusão da #11.

## Lista de trabalho

- [x] C11.1 — Fluxo principal.
- [x] C11.2 — Fluxos alternativos.
- [x] C11.3 — Decisões com guardas.
- [x] C11.4 — Paralelismo com fork/join.
- [x] C11.5 — Partições por responsável.
- [x] C11.6 — Notação UML correta.
- [x] C11.7 — Legibilidade e aderência.
- [x] X.1 — Título e posição do item 11 preservados, no escopo T11.
- [x] X.9 — Nome do produto consistente.
- [x] X.10 — Imagens legíveis na seção, no escopo T11; conferir novamente no PDF em T13.
- [x] K.1 — Nomes dos atores idênticos, no escopo T11.
- [x] K.5 — Fluxos representados coerentes com RFs, estórias e casos de uso, no escopo T11.
- [x] K.7 — Fora de escopo respeitado, no escopo T11.
- [x] K.8 — Raias coerentes com o item 5 e o BPMN.
- [x] K.11 — Decisões, siglas e fontes conferidas, no escopo T11.

## Consulta ao grafo

Grafo construído em `d8cbc67dc75a77a9c5ad307bdc6200694638e683`; base da branch: `4c8b136`. Consulta pelos nós do item 11, atividades e caminho crítico e seus vizinhos. Ligações encontradas: CONTEXT; áreas A/B/C/D de RFs; estórias B/C/D; casos de uso B/C; item 4; pesquisa de marcos, atividades, papéis, serviços sob demanda e caminho crítico; ADRs 0005, 0007, 0010 e 0014. Os Markdown vigentes prevalecem sobre o grafo. Consulta complementada com os critérios C11 e com os casos de uso das quatro áreas. Grafo não regenerado nesta branch.

## Relatório por critério

Evidências relativas a [item 11](../especificacao/11-diagrama-de-atividades.md) e às fontes `especificacao/diagramas/11-*.puml`. Verificação sobre os RFs e UCs da `main` em `4c8b136`. A dependência #11 ainda estava aberta ao concluir a produção; o PR permanece em rascunho até sua conclusão e conferência das alterações. Não altera nem substitui a verificação dos demais itens em T12.

| ID | Status | Evidência |
|---|---|---|
| C11.1 | Atendido | Vista 11.1: cadastro/plano → chegada → execução → prontidão → saída. |
| C11.2 | Atendido | Vistas 11.1–11.4: pendência, confirmação recusada, duas políticas de abastecimento, Não aplicável, pausa/retomada, recusa de conclusão e quatro ações de alerta. |
| C11.3 | Atendido | 17 decisões binárias com guardas, 1 seleção com 4 guardas explícitas e 2 laços com condição de saída. |
| C11.4 | Atendido | Vista 11.2: 4 forks e 4 joins, contados nas fontes; bagagem, abastecimento, cabine e serviços independentes. |
| C11.5 | Atendido | 4 partições com os nomes exatos; validação e transições automáticas no Motor; confirmação pela Autoridade. |
| C11.6 | Atendido | 4 nós iniciais e 7 finais (incluindo recusas); ações, decisões/merges e forks/joins. Compilação PlantUML e inspeção das conexões no PNG. |
| C11.7 | Atendido na base conferida | 4 PNGs inspecionados sem cortes; aderência às áreas A/B/C/D e ao item 4; 19 RFs e 29 UCs citados, todos existentes. SVGs permitem ampliação sem perda. Revalidar se #11 alterar fluxos utilizados. |
| X.1 | Atendido no escopo T11 | Título original preservado, vistas dentro da seção 11; documento final completo será conferido em T13. |
| X.9 | Atendido | Nome Aircraft Turnaround Orchestration System no MD e nos 4 títulos. |
| X.10 | Atendido nos artefatos T11 | PNGs sem cortes, texto legível com ampliação e SVGs exportados. Escala no PDF final pertence ao T13; não foi avaliada nesta tarefa. |
| K.1 | Atendido no escopo T11 | 4 nomes coincidem com CONTEXT, item 5 e UCs. Administrador ausente por não atuar no turnaround. |
| K.5 | Atendido no escopo T11 | Validações e travas preservadas; diferença entre TOBT planejado e vigente, estado Em exceção e processamento após aceitação pelo servidor explícitos. |
| K.7 | Atendido no escopo T11 | Autorização externa fora do sistema; nenhuma programação de voo, escala ou função financeira adicionada. |
| K.8 | Atendido | Partições correspondem às quatro lanes operacionais do item 4. |
| K.11 | Atendido no escopo T11 | ADRs D1/D3/D4/D5/D6/D7/D8/D9/D10/D13/D14 respeitados; siglas expandidas na primeira ocorrência do texto e fontes numeradas. |

## Verificação técnica e independente

- PlantUML **1.2026.0**, Java 17: `-checkonly`, renderização PNG e SVG sem erros.
- 4 PNGs validados com Pillow; 4 SVGs validados como XML.
- Links locais do item conferidos; IDs de RF/UC comparados aos arquivos vigentes; `git diff --check` sem erros.
- Revisão independente por subagente com critérios, MD, fontes e PNGs. Primeira revisão devolveu problemas de partição/guardas/continuidade em 11.4. As correções foram renderizadas e reavaliadas; C11.3/C11.5/C11.6/C11.7 passaram na segunda revisão. Os demais IDs passaram na primeira.

Dimensões das imagens: ciclo de vida 2674 × 1527; paralelismo 2445 × 860; tarefa 1422 × 1499; monitoramento 2187 × 1960 pixels. Na consolidação, usar as versões vetoriais ou páginas em paisagem com escala que preserve a leitura; não reduzir automaticamente todos os diagramas a uma página A4 em retrato.

## Como reproduzir os exports

Com Java e o JAR oficial do PlantUML 1.2026.0 disponíveis, na raiz do repositório:

```powershell
java -jar <caminho-do-plantuml.jar> -charset UTF-8 -checkonly especificacao/diagramas/11-*.puml
java -jar <caminho-do-plantuml.jar> -charset UTF-8 -tpng especificacao/diagramas/11-*.puml
java -jar <caminho-do-plantuml.jar> -charset UTF-8 -tsvg especificacao/diagramas/11-*.puml
```

As fontes editáveis são a autoridade para os exports. A renumeração em T12 deve atualizar MD e fontes, regenerando PNG/SVG; não editar apenas os textos das imagens.
