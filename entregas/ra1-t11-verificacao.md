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
| K.11 | Atendido no escopo T11 | ADRs D1/D3/D4/D5/D6/D7/D8/D9/D10/D13/D14 respeitados; expansões de siglas e fontes preservadas no anexo técnico; a seção de entrega foi reduzida a títulos e imagens por orientação do usuário para seguir o template. |

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


## Adequação ao template do professor

Template encontrado na pasta local `01 Especificacao de Software`, arquivo `ESSW - Especificacao de Projeto - Template.docx`. A seção DIAGRAMA DE ATIVIDADES contém a orientação “Apresenta o diagrama de atividades do sistema.” e a identificação do diagrama. Conforme orientação do usuário, o item 11 de entrega contém apenas título, subtítulos e imagens. Fontes editáveis, versões vetoriais, referências, explicações e evidências permanecem fora da seção de entrega.

## Anexo técnico interno — explicação das vistas

Este anexo apoia manutenção e revisão; não integra o item 11 do documento entregue ao professor.

# 11 DIAGRAMA DE ATIVIDADES

O diagrama de atividades do **Aircraft Turnaround Orchestration System** usa a Linguagem de Modelagem Unificada (UML), dividido em quatro vistas complementares. A vista 11.1 acompanha o turnaround; as demais detalham as ações chamadas por ela. As vistas têm início e fim próprios porque representam atividades distintas, não quatro turnarounds consecutivos.

**Referências de tempo e registro.** O planejamento distingue o horário estimado de chegada à posição (EIBT), o tempo mínimo de turnaround (MTTT) e o horário-alvo de prontidão (TOBT). Os registros reais são o horário real de chegada à posição (AIBT), o início real do atendimento em solo (ACGT), o início real do embarque (ASBT), o fim real do atendimento em solo (AEGT), o horário real de prontidão (ARDT) e o horário real de saída da posição (AOBT) [2][4]. Confirmações de pontos usam código de resposta rápida (QR Code), lido com o celular (ADR-0007). Causas de impedimento usam a tabela da Agência Nacional de Aviação Civil (ANAC) [62], conforme ADR-0006.

## 11.1 Ciclo de vida do turnaround

[Diagrama de atividades — ciclo de vida do turnaround](../especificacao/diagramas/11-atividades.png)

Fonte editável: [11-atividades.puml](../especificacao/diagramas/11-atividades.puml).

Versão vetorial para ampliação e consolidação: [11-atividades.svg](../especificacao/diagramas/11-atividades.svg).

O Coordenador de Turnaround abre o cadastro, aplica o modelo e confirma o plano com responsáveis. O Motor de Eventos verifica a viabilidade antes da chegada (RF-C8). Um risco gera alerta e tratamento, não uma proibição automática de executar o turnaround. O Operador de Solo/Rampa registra diretamente a chegada, após a confirmação do plano, e o Motor de Eventos coloca o turnaround em **Em solo** (ADR-0013). O primeiro início aceito registra ACGT e leva a **Operações em andamento**; o início do embarque registra ASBT; a última obrigatória concluída ou marcada **Não aplicável** registra AEGT e permite **Pronto para liberação** (RF-B7, RF-B8).

Durante a execução, registros são processados pela vista 11.3 e o monitoramento da vista 11.4 ocorre a cada evento e temporizador aplicável. Uma exceção mantém **Em exceção** até seu encerramento com solução; o estado restaurado corresponde ao andamento das tarefas (RF-D5). A Autoridade de Liberação consulta as condições e confirma a prontidão somente em **Pronto para liberação**, sem obrigatória pendente ou exceção aberta. A revalidação na confirmação também recusa uma pendência surgida enquanto a tela estava aberta (UC-D4, E1/E2). O sucesso registra ARDT e leva a **Liberado**.

Depois da autorização de acionamento e push-back recebida fora do sistema, o operador registra AOBT, levando a **Fora de bloco**. A autorização pertence ao controle de tráfego aéreo (ATC); o sistema não a emite nem a verifica (ADR-0004, RF-D9). O histórico é preservado e novos registros de tarefas são recusados.

## 11.2 Dependências e execução paralela

[Diagrama de atividades — tarefas em paralelo e política de abastecimento](../especificacao/diagramas/11-atividades-paralelas.png)

Fonte editável: [11-atividades-paralelas.puml](../especificacao/diagramas/11-atividades-paralelas.puml).

Versão vetorial: [11-atividades-paralelas.svg](../especificacao/diagramas/11-atividades-paralelas.svg).

**[Inferência de modelagem]** Esta vista exemplifica um modelo de atendimento com passageiros, bagagem, abastecimento e serviços de rampa. As relações de desembarque, limpeza, catering e embarque e os fluxos de bagagem se apoiam na pesquisa [20][22][29]. As tarefas efetivas e suas dependências vêm do modelo confirmado, não são criadas automaticamente pelo desenho (RF-A4, RF-A5, RF-A8). Cada ação de execução utiliza os registros da vista 11.3. Uma tarefa permitida como **Não aplicável** satisfaz as dependências sem executar o serviço (RF-B5, RF-B8).

As barras de **fork** distribuem fluxos independentes a operadores distintos das equipes responsáveis; as barras de **join** sincronizam os fluxos necessários antes da sucessora. Limpeza e catering podem ocorrer em paralelo depois do desembarque; bagagem e serviços independentes não precisam esperar o fluxo da cabine inteiro.

A decisão de abastecimento representa a política copiada ao turnaround, imutável após o início das tarefas (RF-A11, ADR-0005) [24][26][27]:

- **[sim]**: permite abastecimento em paralelo com passageiros, sem retirar outras dependências configuradas. O join antes da documentação e do fechamento aguarda os fluxos necessários.
- **[não]**: desembarque precede abastecimento e o join anterior ao embarque exige o término de abastecimento, limpeza e catering. Bagagem e demais serviços independentes seguem em paralelo.

Os serviços sob demanda conhecidos podem integrar o plano inicial. Durante a operação, apenas o Coordenador de Turnaround pode incluir uma tarefa do catálogo, com responsável, janela, dependências e motivo, respeitando as travas de RF-D7. Ela passa a ser executada pela mesma vista 11.3 e, quando obrigatória, bloqueia a liberação até seu término ou marcação permitida como **Não aplicável** (ADR-0014). Os forks ilustram um plano; o teste final de prontidão considera **todas** as obrigatórias efetivamente presentes nele, incluindo as adicionadas depois.

## 11.3 Registro de uma tarefa

[Diagrama de atividades — registro de uma tarefa](../especificacao/diagramas/11-registro-tarefa.png)

Fonte editável: [11-registro-tarefa.puml](../especificacao/diagramas/11-registro-tarefa.puml).

Versão vetorial: [11-registro-tarefa.svg](../especificacao/diagramas/11-registro-tarefa.svg).

O operador consulta somente tarefas da sua equipe atribuídas a ele. Antes do início, pode solicitar **Não aplicável** se o modelo permitir e houver justificativa; caso contrário, solicita início, aceito somente em **Pronta**. Cada registro aceito grava autor e horário e aciona o processamento da vista 11.4. Uma recusa encerra apenas a tentativa, mantendo o estado anterior; uma nova tentativa começa nesta vista.

Durante a execução, a pausa exige justificativa e, quando há impedimento, código da ANAC; a retomada exige **Pausada**. Cada registro passa pelas validações de seu caso de uso (UC-B4). Leituras de QR Code só são aceitas em **Em execução**, para pontos da tarefa atribuída ao operador; pontos inválidos são recusados sem confirmação (UC-B6). A conclusão exige **Em execução** e todos os pontos configurados confirmados (UC-B3). A recusa mantém a tarefa e permite corrigir os pontos ou o estado antes de tentar novamente. A marcação **Não aplicável** não exige nem simula um início.

Sem conexão, os registros de tarefa permanecem no celular como pendentes de envio. Somente após aceitação pelo servidor produzem propagação compartilhada; o servidor revalida estado, atribuição e permissões no envio, conforme os fluxos de exceção da área B e RNF-B2. Esse transporte é abstraído nesta vista; não representa autorização para liberar com registros ainda pendentes no celular.

## 11.4 Eventos, alertas e intervenções

[Diagrama de atividades — monitoramento e tratamento de desvios](../especificacao/diagramas/11-monitoramento.png)

Fonte editável: [11-monitoramento.puml](../especificacao/diagramas/11-monitoramento.puml).

Versão vetorial: [11-monitoramento.svg](../especificacao/diagramas/11-monitoramento.svg).

A vista representa **uma ocorrência** do processamento, repetida a cada registro aceito, alteração do plano, atualização de TOBT, correção de AIBT ou minuto enquanto não houver **Liberado** ou **Fora de bloco** (RF-C1). Não é uma etapa que espera todas as tarefas terminarem. O Motor de Eventos atualiza marcos e estados nos registros aplicáveis, recalcula projeção, atraso e caminho crítico (UC-C3) e fornece os dados ao painel (UC-C1). Exceção aberta prevalece sobre o estado operacional até ser encerrada (RF-D5).

Os gatilhos não são intercambiáveis: RF-C6 trata espera em **Pronta**; RF-C7 compara projeção com **TOBT planejado + 5 min**; RF-C8 trata viabilidade **antes da chegada**; RF-C9 trata ausência de início do embarque no limite configurado; RF-C10 trata falta de prontidão até **TOBT vigente + 5 min**. O aviso **TOBT vigente − 15 min** é checagem com as equipes, não alerta de risco (RF-C11, RF-C14) [2][3][7][13]. Cada um mantém suas condições e regras de emissão conforme os RFs e UC-C4/UC-C6.

O coordenador escolhe reatribuir, replanejar, atualizar a previsão ou abrir uma exceção, e registra a ação para encerrar o alerta (UC-D3). Reatribuição exige operador disponível da mesma equipe; replanejamento só altera tarefas não iniciadas, recusa ciclos e preserva a política de abastecimento. Pode incluir serviço sob demanda (UC-D7). Alterações recusadas mantêm o plano; o alerta só encerra com ação efetivamente registrada. Encerrar um alerta não encerra uma exceção, que exige solução própria (UC-D5).

Quando a projeção se afasta do TOBT vigente em **5 minutos ou mais**, para mais ou para menos, solicita-se a atualização da previsão (RF-D6, ADR-0003) [8][9]. O TOBT planejado permanece fixo como régua de aderência (ADR-0001). Eventos produzidos pelas intervenções voltam ao processamento, com recálculo e atualização do painel.

**Responsabilidades e notação.** As quatro partições usam os nomes do item 5 e das lanes operacionais do item 4: Coordenador de Turnaround, Operador de Solo/Rampa, Motor de Eventos e Autoridade de Liberação. O Administrador do Sistema mantém os cadastros utilizados como pré-condição e não executa atividades do turnaround (ADR-0010). Círculo preenchido = início; círculo com contorno = fim da atividade; retângulo arredondado = ação; losango = decisão ou merge; barras = fork/join. Rótulos entre colchetes indicam guardas. A partição Motor de Eventos reúne o processamento automático e as respostas do sistema dos casos de uso, sem criar um novo ator humano.

Fontes numeradas: [2], [3], [4], [7], [8], [9], [13], [20], [22], [24], [26], [27], [29] e [62], em [fontes da pesquisa](../pesquisa/fontes.md). A decomposição em vistas é uma escolha de modelagem do projeto; não acrescenta regras operacionais às decisões vigentes.
