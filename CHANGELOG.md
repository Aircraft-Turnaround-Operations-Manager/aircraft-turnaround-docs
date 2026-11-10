# Histórico de alterações

Este arquivo registra as mudanças da especificação do Aircraft Turnaround Orchestration System e os caminhos que levaram a cada uma delas. O formato segue o [Keep a Changelog 1.1.0](https://keepachangelog.com/pt-BR/1.1.0/). As versões seguem as entregas, e não o [Versionamento Semântico](https://semver.org/lang/pt-BR/):

- **Versão principal (MAJOR):** uma entrega de Resultado de Aprendizagem (RA). Exemplo: `1.0.0` = RA1 e `2.0.0` = RA2.
- **Versão secundária (MINOR):** uma nova tentativa da mesma entrega, enviada ao professor.
- **Correção (PATCH):** um ajuste no documento já entregue, sem um novo envio.

Cada versão entregue tem uma tag Git `vX.Y.Z` no commit que gerou o PDF enviado. Ao enviar a tag para o GitHub, a automação `.github/workflows/release.yml` cria a release com as notas da versão e o PDF anexado.

**Como registrar.** Todo PR que muda a especificação acrescenta uma linha em **[Não publicado]**, dentro da categoria certa. A linha diz o que mudou, o motivo e o link da issue ou do PR. Ao fechar uma entrega, a seção [Não publicado] vira a versão nova, com a data. Categorias: **Adicionado**, **Alterado**, **Removido**, **Corrigido**.

## [Não publicado]

### Adicionado

- Este `CHANGELOG.md` e a regra 10 do `AGENTS.md`: a partir do RA2, cada PR registra aqui o que mudou e por quê, para que quem ler a especificação pronta consiga reconstruir o caminho até ela ([#139](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/issues/139)).

- Releases automáticas: ao enviar uma tag `vX.Y.Z`, o `.github/workflows/release.yml` cria a release do GitHub com a seção da versão neste arquivo e o PDF daquela entrega anexado. Antes, as tags e as releases dependiam de alguém lembrar de criá-las à mão, e as do RA1 nunca foram criadas. As tags `v1.0.0`, `v1.1.0` e `v1.1.1` foram criadas depois, nos commits que geraram os PDFs, e as releases delas vieram da mesma automação, rodada à mão ([#169](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/169)).

### Alterado

- Os 44 RFs ganharam um título no padrão Ação-Resultado-Objeto (ARO), numa coluna nova (TÍTULO) do item 6. É a anotação 1 do professor na correção do RA1. 23 títulos mudaram e foram levados também para as estórias (item 7), para a matriz (Apêndice A) e para os 16 casos de uso que tinham o mesmo nome, nos itens 9 e 10. O RF-18 e o RF-41 ficaram com o título antigo, porque no ARO perderiam informação: o nome do estado "Não aplicável" e a condição dos 5 minutos ([#139](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/issues/139)).
- RF-12, RF-13, RF-44, US012, US013, US044, UC12, UC13 e UC37 passaram para os arquivos da área B (Execução em Solo), que é dona do estado do turnaround (ADR-0015). O texto e os números não mudaram, e o gerador do documento passou a ordenar os IDs por número ([#139](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/issues/139)).
- Scripts: `gerar_docx.py` põe "Requisito" sobre as colunas # e TÍTULO do item 6, como no slide 12 do professor, e ordena RFs, estórias e casos de uso por número. `gerar_matriz_rastreabilidade.py` ganhou a coluna Título na A.1. `marcos_nos_diagramas.py` passou a ler a nova posição das colunas. `verificar_revisao.py` confere se o título do RF é igual ao da estória e deixou de exigir a ordem por área nos arquivos ([#139](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/issues/139)).

### Corrigido

- Revisão do PR [#164](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/164): os 13 títulos que ainda tinham artigo depois do verbo ficaram sem ele ("Registrar marcos do atendimento em solo"), e os casos de uso com o mesmo nome acompanharam; o UC29 passou a "Abrir exceção do turnaround", par do UC33; no item 9, o UC16 e o UC33 desceram para as setas «include» não cruzarem a elipse e para o rótulo do conjunto aparecer inteiro. As introduções dos itens 6 e 10 passaram a explicar o padrão ARO (e por que o RF-18 e o RF-41 ficam fora dele) e a diferença entre a divisão por serviço do item 10 e o agrupamento por função do item 9. Nenhuma regra de negócio mudou: fora os títulos e nomes, o texto dos RFs, estórias e casos de uso é igual ao da `main`.

<!-- RA1: as seções abaixo foram reconstruídas em 09/11/2026 a partir do histórico do git e das descrições dos PRs. -->

## [1.1.1] - 2026-10-28

Ajustes no documento do RA1 depois da nota, sem novo envio ao professor. O PDF (156 páginas) foi gerado do commit `3ed270c` e serviu de base para o RA2.

### Adicionado

- `scripts/exportar_bpmn.mjs` e `scripts/verificar_bpmn.py`: exportam as vistas do BPMN para PNG e SVG e conferem a geometria de cada uma. Foram usados para redesenhar o item 4 ([#117](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/117)).
- `scripts/verificar_drawio.py` e `scripts/medir_svg.mjs`: conferem a geometria dos diagramas do draw.io sobre o SVG exportado ([#120](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/120)).
- Checagem cruzada de diagramas: a regra 6 do `AGENTS.md` passa a pedir que cada passo, sigla e marco seja conferido contra o RF e o caso de uso, antes de mudar o diagrama e de novo ao terminar. O `scripts/marcos_nos_diagramas.py` lista, para cada marco, os RFs que o definem e os passos de diagrama que o citam. A regra surgiu porque o BPMN mostrava o Operador de Solo/Rampa registrando marcos que o RF-20 atribui ao Motor de Eventos ([#124](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/124)).

### Alterado

- Item 4: o horário real de início do atendimento em solo (ACGT) e o de fim (AEGT) passam a ser gravados pelo Motor de Eventos, a partir dos registros do operador, como pede o RF-20. Antes, o BPMN dava a entender que o operador digitava os dois ([#122](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/122)).
- Item 4: o BPMN TO BE foi refeito em sete vistas do mesmo modelo (geral, principal, tarefas em solo, monitoramento, alerta, previsão e TOBT − 15), com prioridade para a leitura na tela ([#117](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/117)).
- Item 11: os quatro diagramas de atividades foram refeitos no draw.io, com a posição de cada elemento definida à mão ([#120](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/120)).
- Documento: os diagramas entram em SVG, vetoriais no Word e no PDF, e a PNG fica de reserva. Antes eram só imagens PNG ([#129](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/129), [#131](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/131)).

### Removido

- Fontes PlantUML do item 11, substituídas pelas do draw.io ([#120](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/120)).

### Corrigido

- Item 11: o AEGT e a passagem a "Pronto para liberação" faltavam nas vistas 11.1 e 11.2. A lacuna foi apontada pela extração do grafo ([#127](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/127)).
- SVG do draw.io: o diagrama ficava preto, com linhas claras, para quem usa tema escuro. O SVG passa a ter só as cores do tema claro ([#120](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/120)).
- Cabeçalho do documento: o ano saía como "2025" e passa a sair "2026" em todas as páginas ([#131](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/131)).

## [1.1.0] - 2026-10-23

Segunda tentativa do RA1, enviada no Canvas em 23/10/2026 e avaliada com nota 5,0/5,0. O PDF (151 páginas) foi gerado do commit `2c03d49`. Esta versão atende quatro das cinco anotações do professor na primeira tentativa. O título dos RFs no padrão Ação-Resultado-Objeto (ARO) ficou para o RA2 ([#139](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/issues/139)).

### Alterado

- Item 9: o diagrama geral de casos de uso foi refeito no draw.io, com a posição de cada elemento definida à mão, porque o PlantUML não permitia controlar o layout. O `scripts/verificar_revisao.py` passou a conferir o diagrama: os 37 nomes contra o item 10, as 10 relações «include», as 8 «extend» e as linhas soltas ([#112](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/issues/112), [#113](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/113)).
- Tabelas do PDF: a largura de cada coluna passa a seguir o conteúdo, e a coluna com mais texto ganha mais espaço. Antes, a largura era dividida em partes iguais. Atende às anotações do professor nas páginas 14 e 31 da primeira tentativa. Os fluxos do item 10 e os quadros É/Não é e Faz/Não faz ficam em 50/50 ([#115](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/115)).

### Removido

- Fonte PlantUML do item 9, substituída pela do draw.io ([#113](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/113)).

### Corrigido

- Item 10: os 42 protótipos de tela não apareciam no PDF, e no lugar deles saía "[imagem não encontrada: …]". O script procurava as imagens na pasta errada. Atende à anotação do professor na página 65 ([#115](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/115)).
- Item 7: as linhas COMO/POSSO/PARA e "Critérios de Aceite" deixavam uma coluna vazia ao lado e passam a ocupar a largura toda ([#115](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/115)).
- Referências: o número entre colchetes e o autor sumiam de cada referência ([#115](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/115)).

## [1.0.0] - 2026-10-10

Primeira tentativa do RA1 (itens 1 a 11), enviada no Canvas em 10/10/2026. O PDF (154 páginas) foi gerado do commit `fd1a508`. Como esta é a primeira versão, as linhas de "Alterado", "Removido" e "Corrigido" registram o que mudou durante a construção, antes do envio.

### Adicionado

- Estrutura do repositório: um arquivo Markdown por item do template, com um arquivo por área nos itens divididos entre os integrantes, para que o grupo trabalhasse em paralelo sem conflito ([#31](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/31), [#42](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/42)).
- Orientações para agentes de IA no repositório ([#32](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/32)).
- Base de conhecimento: `CONTEXT.md`, pesquisa do setor em `pesquisa/`, fontes numeradas e as decisões D1 a D9 (ADR-0001 a ADR-0009). Com ela, pessoas e IAs passaram a escrever a partir das mesmas decisões, como a régua do TOBT planejado + 5 min e a meta de 80% ([#35](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/35)).
- Grafo de conhecimento em `graphify-out/`, atualizado depois de cada leva de PRs de conteúdo ([#38](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/38) e seguintes). Depois virou regra consultar o grafo antes de escrever ou revisar um item, para achar o que se liga ao item em outras áreas ([#68](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/68)).
- Item 1, "3 Objetivos" ([#33](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/33)); item 2, "É – Não é – Faz – Não faz" ([#34](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/34)); item 3, "Visão do Produto" ([#40](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/40)).
- Item 5, "Relação de Atores / Usuários", com a ADR-0010: Administrador do Sistema como ator, ator abstrato Usuário e a equipe do operador como dado do cadastro, e não como ator ([#43](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/43)).
- Item 4, "Mapeamento de Negócios (BPMN TO BE)" ([#45](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/45)).
- ADR-0011: mínimo de 4 RFs, estórias, RNFs e casos de uso por integrante, sem máximo, e IDs provisórios por área (RF-A1, US-B1, RNF-C1, UC-D1…), para que cada área escrevesse sem esperar a numeração das outras ([#53](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/53)).
- Itens 6, 7, 8 e 10 por área. Área B, execução em solo: [#50](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/50), [#51](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/51), [#52](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/52), [#56](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/56), [#74](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/74). Área D, exceções e liberação: [#57](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/57), [#64](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/64), [#72](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/72), [#86](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/86). Área C, monitoramento: [#75](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/75), [#77](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/77), [#92](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/92), [#76](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/76). Área A, acesso e planejamento: [#79](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/79), [#81](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/81), [#80](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/80), [#82](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/82).
- Regra das pendências cruzadas: quando uma área supõe algo que outra ainda não definiu, a suposição vira uma linha numa issue `pendencia-cruzada`, em vez de parar o trabalho ou inventar o requisito da outra área ([#62](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/62)).
- ADR-0012: matriz de rastreabilidade como Apêndice A, gerada por script ([#65](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/65)).
- Pesquisa sobre serviços sob demanda, ADR-0013 (a chegada à posição é registrada direto pelo Operador de Solo/Rampa, sem confirmação) e ADR-0014 (serviços sob demanda acionados pelo Coordenador de Turnaround) ([#83](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/83), [#84](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/84)).
- Consolidação dos itens 6, 7, 8 e 10: 44 RFs com a coluna SPRINT (8 sprints em 2027) e a justificativa da priorização, 44 estórias, 24 RNFs e 37 especificações de caso de uso, com 42 protótipos de tela ([#96](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/96), [#97](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/97), [#98](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/98), [#99](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/99), [#108](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/108)).
- Item 9, diagrama geral de casos de uso, em PlantUML ([#106](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/106)).
- Item 11, diagrama de atividades em quatro vistas, em PlantUML ([#107](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/107)).
- `scripts/verificar_revisao.py` e `entregas/ra1-renumeracao.md`, com a correspondência entre os IDs provisórios e os definitivos ([#109](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/109)).
- `scripts/gerar_docx.py`, que monta o documento a partir do template da disciplina e dos arquivos Markdown, e a declaração de uso de IA ([#110](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/110)).

### Alterado

- Item 1: as metas passam de 95% para 80% (ADR-0002), e "horário planejado" passa a ser o horário-alvo de prontidão (TOBT) planejado (ADR-0001). "Supervisor" passa a "Coordenador de Turnaround" (ADR-0009). O item tinha sido escrito antes da base de conhecimento ([#36](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/36)).
- Item 2: os atores passam a usar os nomes exatos ("Operador de Solo/Rampa", "Autoridade de Liberação"), as siglas ganham o nome em português e a fonte, e entram itens novos: não é um sistema completo de tomada de decisão colaborativa em aeroportos (A-CDM); registra a causa do atraso com o código da tabela da Agência Nacional de Aviação Civil (ANAC); não define o turnaround programado nem o tempo mínimo de turnaround (MTTT) ([#37](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/37), [#39](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/39)).
- ADR-0008: a regra do nome em português passa a valer para toda sigla, inclusive a própria A-CDM e as de órgãos e normas, e não só para os marcos do A-CDM. O `CONTEXT.md` e o `AGENTS.md` já aplicavam a regra assim ([#69](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/issues/69), [#70](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/70)).
- ADR-0003: a antecipação de 5 min passa a ser medida em relação ao TOBT vigente, e o projeto separa o TOBT planejado do vigente ([#72](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/72)).
- RNF-B2: o prazo de 5 s para enviar os registros feitos sem conexão passa a contar da nova autenticação quando a sessão expirou. Sem a mudança, ele contradizia o RNF-A5, que encerra a sessão após 45 min sem ação ([#89](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/89)).
- Oito RFs foram ajustados para não se contradizerem entre si nem com as decisões. Por exemplo, o RF-A2 passa a recusar a desativação de um operador com tarefa pendente, e o parâmetro do RF-C6 passa de "X" para "Y", porque "X" já era o do embarque no RF-C9 ([#95](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/95)).
- Seis RNFs passam a citar os RFs a que se aplicam, e a matriz fica sem lacunas. Isso resolveu a pendência cruzada [#61](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/issues/61) ([#101](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/101)).
- Item 10: as especificações das áreas A, B e C passam para o formato em tabelas da área D, com as colunas "Ações do ator" e "Ações do sistema". As regras de negócio ganham o prefixo RN ([#87](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/issues/87), [#102](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/102)).
- Item 10: os casos de uso de acesso e planejamento ganham as relações «include» e «extend» que o diagrama do item 9 precisava ([#104](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/104)).
- Numeração: os IDs provisórios por área passam à numeração definitiva única (RF-A1 → RF-1, US-A1 → US001, RNF-A1 → RNF-1, UC-A1 → UC01), em todas as referências cruzadas ([#109](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/109)).

### Removido

- Tabelas "Base" dos arquivos de área. A ADR-0012 foi corrigida: a relação entre RFs, estórias, RNFs e casos de uso fica só na matriz de rastreabilidade, e cada RNF e cada especificação citam os RFs que atendem (critérios C08.6 e C10.10) ([#66](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/66)).

### Corrigido

- Item 10: lacunas nos fluxos de propagação, projeção, alertas e replanejamento, e o cenário da correção da chegada com o turnaround em "Liberado" ([#108](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/108)).
- Itens 4 e 11: as esperas do BPMN passam a depender de condições do turnaround que continuam valendo, a propagação de estados depois do replanejamento foi corrigida, e a emissão da folha de carga mudou de posição no fluxo paralelo ([#109](https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/pull/109)).

[Não publicado]: https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/commits/main
[1.1.1]: https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/compare/2c03d492b655150639f6fb5e86ad630b97173b8a...3ed270cf2e095a30761c86cea1b952f9674db851
[1.1.0]: https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/compare/fd1a50855d83fdbf2b4ad66a44567d1bf453191a...2c03d492b655150639f6fb5e86ad630b97173b8a
[1.0.0]: https://github.com/Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs/compare/15fbc68a82017e2a2f6f018a53f98573e0444dc9...fd1a50855d83fdbf2b4ad66a44567d1bf453191a
