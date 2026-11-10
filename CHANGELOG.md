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

### Alterado

- Os 44 RFs ganharam um título no padrão Ação-Resultado-Objeto (ARO), numa coluna nova (TÍTULO) do item 6. É a anotação 1 do professor na correção do RA1. 23 títulos mudaram e foram levados também para as estórias (item 7), para a matriz (Apêndice A) e para os 16 casos de uso que tinham o mesmo nome, nos itens 9 e 10. O RF-18 e o RF-41 ficaram com o título antigo, porque no ARO perderiam informação: o nome do estado "Não aplicável" e a condição dos 5 minutos ([#139](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/issues/139)).
- RF-12, RF-13, RF-44, US012, US013, US044, UC12, UC13 e UC37 passaram para os arquivos da área B (Execução em Solo), que é dona do estado do turnaround (ADR-0015). O texto e os números não mudaram, e o gerador do documento passou a ordenar os IDs por número ([#139](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/issues/139)).
- Scripts: `gerar_docx.py` põe "Requisito" sobre as colunas # e TÍTULO do item 6, como no slide 12 do professor, e ordena RFs, estórias e casos de uso por número. `gerar_matriz_rastreabilidade.py` ganhou a coluna Título na A.1. `marcos_nos_diagramas.py` passou a ler a nova posição das colunas. `verificar_revisao.py` confere se o título do RF é igual ao da estória e deixou de exigir a ordem por área nos arquivos ([#139](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/issues/139)).

### Corrigido

- Revisão do PR [#164](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/164): os 13 títulos que ainda tinham artigo depois do verbo ficaram sem ele ("Registrar marcos do atendimento em solo"), e os casos de uso com o mesmo nome acompanharam; o UC29 passou a "Abrir exceção do turnaround", par do UC33; no item 9, o UC16 e o UC33 desceram para as setas «include» não cruzarem a elipse e para o rótulo do conjunto aparecer inteiro. As introduções dos itens 6 e 10 passaram a explicar o padrão ARO (e por que o RF-18 e o RF-41 ficam fora dele) e a diferença entre a divisão por serviço do item 10 e o agrupamento por função do item 9. Nenhuma regra de negócio mudou: fora os títulos e nomes, o texto dos RFs, estórias e casos de uso é igual ao da `main`.

[Não publicado]: https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/commits/main
