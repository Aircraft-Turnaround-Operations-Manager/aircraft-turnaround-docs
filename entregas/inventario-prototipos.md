# Inventário dos protótipos de tela

Levantado em 20/11/2026 para montar um único canvas de Design com todas as telas. Diz, para cada tela do PDF do RA1 e da pasta `especificacao/10-especificacoes-de-caso-de-uso/prototipos/`, de onde ela veio e se existe no Figma.

## Fontes conferidas

| Fonte | O que foi feito |
|---|---|
| Figma `aircraft` (fileKey `jnyAawiHZsJdwKW3KjaLVs`), só leitura | Listadas as 4 páginas e todos os frames de primeiro nível; capturadas as 4 seções da página "Céu" em tamanho real (1:1) e recortado cada frame. |
| `entregas/ra1-especificacao-de-projeto.pdf` | Extraídas as 42 imagens embutidas e comparadas com os PNGs da pasta. |
| `prototipos/` (43 PNGs) | Autor e commit de entrada por `git log --follow --diff-filter=A`; caso de uso pelo título da seção em `area-*.md`. |
| Comparação PNG × Figma | Diferença pixel a pixel (limiar 40/255) entre o PNG e o recorte do frame; os pares com diferença foram olhados lado a lado. |

**Não conferido:** o conteúdo dos frames das páginas "Pátio noturno" e "Sinalização" (só vistos em miniatura: são as mesmas telas do João em outros temas); o histórico de versões do Figma (não dá para saber se um frame existiu e foi apagado); os textos de cada frame por `get_design_context` (fica para a reconstrução).

## Resumo

- **PDF = pasta:** as 42 imagens do PDF são, uma a uma, os PNGs citados nos `area-*.md`. Só `uc-c2-linha-do-tempo.png` (v1) está na pasta e fora do PDF.
- **33 telas do PDF idênticas ao Figma**, pixel a pixel.
- **2 telas do PDF com divergência** em relação ao frame do Figma (`uc-b7`, `uc-d4-v2`).
- **7 telas do PDF sem frame no Figma**: toda a área C (UC22 a UC28). Mais a v1 da linha do tempo, fora do PDF.
- **Frames do Figma fora do PDF:** 8 na página "Céu" e as cópias de tema das páginas "Pátio noturno" e "Sinalização".

## 1. Telas do PDF e da pasta

Coluna "Figma": nome e id do frame na página "Céu". "Comparação": resultado do diff PNG × recorte do frame.

| PNG | UC | Texto que cita | Commit · data · autor | Figma (frame · id) | Comparação |
|---|---|---|---|---|---|
| uc-a1-autenticar-web | UC01 | area-a | 3160183 · 10/10 · Eduardo Fabri | uc-a1-autenticar-web · 52:1059 | idêntico |
| uc-a1-autenticar-celular | UC01 | area-a | 3160183 · 10/10 · Eduardo Fabri | uc-a1-autenticar-celular · 52:1085 | idêntico |
| uc-a2-gerenciar-usuarios | UC02 | area-a | 3160183 · 10/10 · Eduardo Fabri | uc-a2-gerenciar-usuarios · 52:1119 | idêntico |
| uc-a3-abrir-turnaround | UC03 | area-a | 3160183 · 10/10 · Eduardo Fabri | uc-a3-abrir-turnaround · 47:687 | idêntico |
| uc-a4-criar-modelo | UC04 | area-a | 3160183 · 10/10 · Eduardo Fabri | uc-a4-criar-modelo · 49:750 | idêntico |
| uc-a5-confirmar-plano | UC05 | area-a | 3160183 · 10/10 · Eduardo Fabri | uc-a5-confirmar-plano · 50:892 | idêntico |
| uc-a6-aplicar-modelo | UC06 | area-a | 3160183 · 10/10 · Eduardo Fabri | uc-a6-aplicar-modelo · 50:1391 | idêntico |
| uc-a7-pontos-de-confirmacao | UC07 | area-a | 3160183 · 10/10 · Eduardo Fabri | uc-a7-pontos-de-confirmacao · 49:995 | idêntico |
| uc-a8-definir-dependencias | UC08 | area-a | 3160183 · 10/10 · Eduardo Fabri | uc-a8-definir-dependencias · 49:1295 | idêntico |
| uc-a9-gerenciar-equipes | UC09 | area-a | 3160183 · 10/10 · Eduardo Fabri | uc-a9-gerenciar-equipes · 52:1316 | idêntico |
| uc-a10-atualizar-previsao | UC10 | area-a | 3160183 · 10/10 · Eduardo Fabri | uc-a10-atualizar-previsao · 50:1137 | idêntico |
| uc-a11-politica-de-abastecimento | UC11 | area-a | 3160183 · 10/10 · Eduardo Fabri | uc-a11-politica-de-abastecimento · 51:1016 | idêntico |
| uc-a12-registrar-chegada | UC12 | area-b | 3160183 · 10/10 · Eduardo Fabri | uc-a12-registrar-chegada · 52:1592 | idêntico |
| uc-a13-corrigir-chegada | UC13 | area-b | 3160183 · 10/10 · Eduardo Fabri | uc-a13-corrigir-chegada · 51:1130 | idêntico |
| uc-b1-lista-de-tarefas | UC14 | area-b | 3c73d19 · 08/10 · João Pedro Cardoso de Liz | uc-b1-lista-de-tarefas · 5:12 | idêntico |
| uc-b1-detalhe-da-tarefa | UC14 | area-b | 3c73d19 · 08/10 · João Pedro Cardoso de Liz | uc-b1-detalhe-da-tarefa · 5:140 | idêntico |
| uc-b2-iniciar-tarefa | UC15 | area-b | 3c73d19 · 08/10 · João Pedro Cardoso de Liz | uc-b2-iniciar-tarefa · 5:214 | idêntico |
| uc-b3-concluir-tarefa | UC16 | area-b | 3c73d19 · 08/10 · João Pedro Cardoso de Liz | uc-b3-concluir-tarefa · 6:79 | idêntico |
| uc-b4-pausar-tarefa | UC17 | area-b | 3c73d19 · 08/10 · João Pedro Cardoso de Liz | uc-b4-pausar-tarefa · 6:150 | idêntico |
| uc-b4-retomar-tarefa | UC17 | area-b | 3c73d19 · 08/10 · João Pedro Cardoso de Liz | uc-b4-retomar-tarefa · 6:222 | idêntico |
| uc-b5-nao-aplicavel | UC18 | area-b | 3c73d19 · 08/10 · João Pedro Cardoso de Liz | uc-b5-nao-aplicavel · 6:282 | idêntico |
| uc-b6-leitura-qr-code | UC19 | area-b | 3c73d19 · 08/10 · João Pedro Cardoso de Liz | uc-b6-leitura-qr-code · 7:137 | idêntico |
| uc-b6-pontos-da-tarefa | UC19 | area-b | 3c73d19 · 08/10 · João Pedro Cardoso de Liz | uc-b6-pontos-da-tarefa · 7:311 | idêntico |
| uc-b7-marcos-do-turnaround | UC20 | area-b | 3c73d19 · 08/10 · João Pedro Cardoso de Liz | uc-b7-marcos-do-turnaround · 9:260 | **diverge** (D-1) |
| uc-b8-propagacao-de-estado | UC21 | area-b | 3c73d19 · 08/10 · João Pedro Cardoso de Liz | uc-b8-propagacao-de-estado · 7:418 | idêntico |
| uc-c1-painel-de-turnarounds | UC22 | area-c | 144bdd5 · 08/10 · joao.correa | **não existe no Figma** | — |
| uc-c2-linha-do-tempo-v2 | UC23 | area-c | 18a2ddb · 10/10 · rdsalves | **não existe no Figma** | — (D-3) |
| uc-c3-recalculo-e-caminho-critico | UC24 | area-c | 144bdd5 · 08/10 · joao.correa | **não existe no Figma** | — |
| uc-c4-alerta-emitido | UC25 | area-c | 144bdd5 · 08/10 · joao.correa | **não existe no Figma** | — |
| uc-c5-lista-de-alertas | UC26 | area-c | 144bdd5 · 08/10 · joao.correa | **não existe no Figma** | — (aba "Encerrados hoje") |
| uc-c6-checagem-tobt-15 | UC27 | area-c | 144bdd5 · 08/10 · joao.correa | **não existe no Figma** | — |
| uc-c7-indicadores-de-aderencia | UC28 | area-c | 144bdd5 · 08/10 · joao.correa | **não existe no Figma** | — |
| uc-d1-abrir-excecao | UC29 | area-d | 0ce470e · 10/10 · rdsalves | uc-d1-abrir-excecao · 41:375 | idêntico |
| uc-d2-reatribuir-tarefa | UC30 | area-d | 0ce470e · 10/10 · rdsalves | uc-d2-reatribuir-tarefa · 41:688 | idêntico |
| uc-d3-registrar-acao-do-alerta | UC31 | area-d | 0ce470e · 10/10 · rdsalves | uc-d3-registrar-acao-do-alerta · 41:1001 | idêntico |
| uc-d4-confirmar-prontidao-v2 | UC32 | area-d | 18a2ddb · 10/10 · rdsalves | uc-d4-confirmar-prontidao · 41:1314 | **diverge** (D-2) |
| uc-d5-encerrar-excecao | UC33 | area-d | 0ce470e · 10/10 · rdsalves | uc-d5-encerrar-excecao · 41:1458 | idêntico |
| uc-d6-atualizar-tobt | UC34 | area-d | 0ce470e · 10/10 · rdsalves | uc-d6-atualizar-tobt · 41:1771 | idêntico |
| uc-d7-replanejar-tarefas | UC35 | area-d | 0ce470e · 10/10 · rdsalves | uc-d7-replanejar-tarefas · 41:2084 | idêntico |
| uc-d7-acionar-servico-sob-demanda | UC35 | area-d | 0ce470e · 10/10 · rdsalves | uc-d7-acionar-servico-sob-demanda · 41:2397 | idêntico |
| uc-d8-operadores-disponiveis | UC36 | area-d | 0ce470e · 10/10 · rdsalves | uc-d8-operadores-disponiveis · 41:2710 | idêntico |
| uc-d9-registrar-saida-da-posicao | UC37 | area-b | 0ce470e · 10/10 · rdsalves | uc-d9-registrar-saida-da-posicao · 41:3023 | idêntico |
| uc-c2-linha-do-tempo (v1) | UC23 (substituída) | nenhum | 144bdd5 · 08/10 · joao.correa | **não existe no Figma** | fora do PDF |

Observações de origem:

- `uc-a12` e `uc-a13` são do UC12 e do UC13, citados em `area-b.md`, mas os PNGs e os frames são do Eduardo (seção "Área A" do Figma). `uc-d9` é do UC37, citado em `area-b.md`, com PNG e frame do Rodrigo (seção "Área D").
- As duas "v2" (`uc-c2-…-v2`, `uc-d4-…-v2`) entraram no commit de consolidação 18a2ddb, em 1586 × 992 px (escala ≈ 1,1 de 1440 × 900); as demais estão no tamanho do frame.
- Os autores do 144bdd5 (`joao.correa`, área C) e do 3c73d19 (João Pedro Cardoso de Liz, área B) são registros diferentes no git.

## 2. Divergências PNG × Figma

| # | Tela | PNG (PDF) | Figma |
|---|---|---|---|
| D-1 | uc-b7-marcos-do-turnaround (UC20) | Logo da barra lateral: "Aircraft Turnaround Orchestration System", em três linhas. | "Aircraft Turnaround", em uma linha. Resto idêntico. |
| D-2 | uc-d4-confirmar-prontidao (UC32) | "Tarefas obrigatórias" com 12 linhas; na coluna da direita, a 2ª linha é "Troca de mantas", com o selo "Não aplicável" e um traço no lugar do visto. | 12 linhas; no mesmo lugar está "Água potável e lavatório 13:41", que não aparece no PNG. O resto da lista e o cabeçalho "12 de 12 … 11 concluídas · 1 não aplicável (Troca de mantas…)" são iguais nos dois. Conferido por regiões no tamanho nativo do PNG (1586 × 992): é a única diferença. |
| D-3 | uc-c2-linha-do-tempo (UC23), v1 × v2 | v2 (no PDF): a faixa dos marcos termina em "Marcos registrados". | v1 (fora do PDF): termina em "gravados pelo Motor de Eventos". Nenhuma das duas está no Figma; outras diferenças pequenas ficam para a reconstrução. |

**Decisão do Rodrigo (20/11/2026):** nas divergências D-1, D-2 e D-3, o PNG é a fonte da verdade. As melhorias provavelmente foram feitas direto nos PNGs, sem passar pelo Figma. O canvas segue o PNG nessas telas (e, na D-3, a v2, que é a do PDF).

## 3. Frames do Figma que não aparecem no PDF

Página "Céu":

| Frame · id | Seção | O que mostra | Tela do PDF mais próxima |
|---|---|---|---|
| comum-login-celular · 4:2 | Operador de Solo/Rampa · celular (João) | Login do operador no celular | uc-a1-autenticar-celular (Eduardo) |
| operador-sem-conexao · 7:525 | Operador de Solo/Rampa · celular (João) | Lista de tarefas sem conexão, com registros na fila | nenhuma |
| comum-login-web · 8:230 | Web · Coordenador… (João) | Login web | uc-a1-autenticar-web (Eduardo) |
| coord-painel · 8:256 | Web · Coordenador… (João) | "Painel do turno": indicadores, turnarounds em solo, alertas | uc-c1-painel-de-turnarounds (área C, fora do Figma) |
| coord-abrir-turnaround · 10:273 | Web · Coordenador… (João) | Abrir turnaround com checagem de viabilidade | uc-a3-abrir-turnaround (Eduardo) |
| coord-tratar-alerta · 10:492 | Web · Coordenador… (João) | Alerta "Embarque não iniciado em TOBT − 15" com ações | uc-d3-registrar-acao-do-alerta (Rodrigo) |
| lib-confirmar-prontidao · 11:335 | Web · Coordenador… (João) | Liberações da Autoridade de Liberação | uc-d4-confirmar-prontidao (Rodrigo) |
| admin-usuarios · 12:359 | Web · Coordenador… (João) | Usuários, com painel de edição | uc-a2-gerenciar-usuarios (Eduardo) |

Páginas "Pátio noturno" (1:49, tema azul-escuro) e "Sinalização" (1:50, tema preto e laranja): cada uma repete as duas seções do João, com os mesmos 19 nomes de frame (12 de celular e 7 web), ids 19:1119 a 19:3090 e 19:3248 a 19:5219. Nenhuma está no PDF. Página "Componentes" (3:2): logo e 37 ícones, sem telas.

## Ligações

- [Especificações de caso de uso — área A](../especificacao/10-especificacoes-de-caso-de-uso/area-a.md)
- [Especificações de caso de uso — área B](../especificacao/10-especificacoes-de-caso-de-uso/area-b.md)
- [Especificações de caso de uso — área C](../especificacao/10-especificacoes-de-caso-de-uso/area-c.md)
- [Especificações de caso de uso — área D](../especificacao/10-especificacoes-de-caso-de-uso/area-d.md)
