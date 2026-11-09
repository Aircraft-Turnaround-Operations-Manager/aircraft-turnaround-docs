# Histórico de alterações

Este arquivo registra as mudanças da especificação do Aircraft Turnaround Orchestration System e os caminhos que levaram a cada uma delas. O formato segue o [Keep a Changelog 1.1.0](https://keepachangelog.com/pt-BR/1.1.0/). As versões seguem as entregas, e não o [Versionamento Semântico](https://semver.org/lang/pt-BR/):

- **Versão principal (MAJOR):** uma entrega de Resultado de Aprendizagem (RA). Exemplo: `1.0.0` = RA1 e `2.0.0` = RA2.
- **Versão secundária (MINOR):** uma nova tentativa da mesma entrega, enviada ao professor.
- **Correção (PATCH):** um ajuste no documento já entregue, sem um novo envio.

Cada versão entregue tem uma tag Git `vX.Y.Z` no commit que gerou o PDF enviado.

**Como registrar.** Todo PR que muda a especificação acrescenta uma linha em **[Não publicado]**, dentro da categoria certa. A linha diz o que mudou, o motivo e o link da issue ou do PR. Ao fechar uma entrega, a seção [Não publicado] vira a versão nova, com a data. Categorias: **Adicionado**, **Alterado**, **Removido**, **Corrigido**.

## [Não publicado]

### Adicionado

- Este `CHANGELOG.md` e a regra 10 do `AGENTS.md`: a partir do RA2, cada PR registra aqui o que mudou e por quê, para que quem ler a especificação pronta consiga reconstruir o caminho até ela ([#139](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/issues/139)).

- Casos de teste da área B (item 15), em `especificacao/15-casos-de-teste/area-b.md`: 109 casos para os casos de uso UC12 a UC21 e UC37, com uma massa de teste comum (turnarounds, usuários, tarefas e pontos de QR Code). Todo critério de aceite das 11 estórias da área (47) e todo fluxo dos 11 casos de uso (92) têm pelo menos um caso. Os IDs CT-B001 a CT-B109 são provisórios, até a numeração única da tarefa-mãe ([#153](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/issues/153)).

### Alterado

- Os 44 RFs ganharam um título no padrão Ação-Resultado-Objeto (ARO), numa coluna nova (TÍTULO) do item 6. É a anotação 1 do professor na correção do RA1. 23 títulos mudaram e foram levados também para as estórias (item 7), para a matriz (Apêndice A) e para os 16 casos de uso que tinham o mesmo nome, nos itens 9 e 10. O RF-18 e o RF-41 ficaram com o título antigo, porque no ARO perderiam informação: o nome do estado "Não aplicável" e a condição dos 5 minutos ([#139](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/issues/139)).
- RF-12, RF-13, RF-44, US012, US013, US044, UC12, UC13 e UC37 passaram para os arquivos da área B (Execução em Solo), que é dona do estado do turnaround (ADR-0015). O texto e os números não mudaram, e o gerador do documento passou a ordenar os IDs por número ([#139](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/issues/139)).
- Scripts: `gerar_docx.py` põe "Requisito" sobre as colunas # e TÍTULO do item 6, como no slide 12 do professor, e ordena RFs, estórias e casos de uso por número. `gerar_matriz_rastreabilidade.py` ganhou a coluna Título na A.1. `marcos_nos_diagramas.py` passou a ler a nova posição das colunas. `verificar_revisao.py` confere se o título do RF é igual ao da estória e deixou de exigir a ordem por área nos arquivos ([#139](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/issues/139)).

[Não publicado]: https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/commits/main
