# Critérios de Aceite da Entrega — RA1 (Especificação do Projeto, itens 1 a 11)

> Definition of Done do documento de especificação que o grupo entrega na Avaliação do RA 1.
> Este arquivo **não é** o documento de especificação. Ele define **o que** o documento precisa conter e **como verificar** que está pronto.
> Os itens 12 a 15 (Avaliação do RA 2, entrega em 28/11) ficam em um documento separado, a ser criado depois.

---

## 0. Como usar este documento

### 0.1 Para quem monta o board (GitHub Projects)
- Cada item das seções 3.1 a 3.11 vira **uma ou mais tarefas** no board.
- Os itens marcados como **por integrante** (6, 7, 8 e 10) viram **uma tarefa por integrante**, com a cota mínima indicada.
- A ordem e os bloqueios entre tarefas estão na **seção 4**.
- O corpo de cada tarefa deve copiar os IDs dos critérios correspondentes (ex.: `C07.1` a `C07.6`), para que o checklist acompanhe a tarefa.

### 0.2 Para quem escreve um item
- Antes de começar, leia a seção do item e o checklist dele.
- Um item só está pronto quando **todos** os critérios dele estão atendidos **e** a consistência da seção 5 foi conferida para ele.

### 0.3 Protocolo de execução e verificação (obrigatório para agentes de IA)

Este protocolo segue a recomendação da Anthropic para o Claude Opus 5.5: manter uma lista de tarefas persistente, não tratar uma mensagem de status como conclusão e verificar a conclusão contra uma condição declarada no início.

1. **Condição de conclusão.** O trabalho só está concluído quando **todos** os critérios aplicáveis deste arquivo (IDs `Cxx.y` e `X.y`) estiverem marcados como atendidos, cada um com evidência. Qualquer outro estado é "em andamento".
2. **Lista de tarefas antes de começar.** Antes de produzir qualquer coisa, crie uma lista de tarefas com **um item por ID de critério** no escopo pedido. Não agrupe critérios em um único item.
3. **Evidência por critério.** Um critério só pode ser marcado como atendido com evidência concreta: seção do documento, quantidade contada (ex.: "16 RFs, RF-1 a RF-16"), nome do arquivo do diagrama. "Feito" sem evidência não conta.
4. **Contagem por comando, não por estimativa.** Todo critério com número mínimo (≥3, ≥16, ≥2 por estória etc.) deve ser conferido contando de fato: listar e contar os itens, não estimar.
5. **Não encerrar com itens abertos.** Se a lista ainda tem itens abertos, não encerre com um resumo, uma oferta de continuar ou uma pergunta que não bloqueia o resto. Continue. Só pare se houver bloqueio real, e nesse caso diga **qual critério** está bloqueado e **por quê**.
6. **Verificação independente ao final.** Ao terminar, faça uma segunda passagem de verificação **separada da escrita**: de preferência um subagente ou uma sessão nova que receba **apenas** este arquivo e o documento produzido, e percorra todos os IDs marcando atendido / não atendido / evidência. Qualquer "não atendido" volta para a lista de tarefas.
7. **Relatório final.** O relatório final é a tabela `ID | status | evidência` para todos os IDs do escopo, e não um resumo em prosa.

---

## 1. Contexto da entrega

| Campo | Valor |
|---|---|
| Disciplina | Especificação de Software (PSI151) — BSI PUCPR, 6º período, Turma 6º A, noite |
| Professor | Evandro Alberto Zatti |
| Tarefa no Canvas | Avaliação do RA 1 - Projeto |
| Prazo | **Sábado, 10/10/2026, 23:59** |
| Valor | 5,0 pontos |
| Envio | Único para o grupo inteiro ("contado para todos em seu grupo"); tentativas ilimitadas até o prazo; formatos aceitos: URL, upload ou Office 365 |
| Recuperação do RA1 | Reentrega até 28/11 (nota máxima 7,0 na recuperação) |
| Produto | Aircraft Turnaround Orchestration System (organização GitHub: Aircraft-Turnaround-Operations-Manager) |

### 1.1 Integrantes

| Integrante | GitHub |
|---|---|
| Eduardo Fabri | `eduardofabrii` |
| João Pedro Cardoso de Liz | `Jcliz` |
| Rodrigo Alves | `rdsalvesPUC` |
| João Vitor Correa Oliveira | `jvecodev` |

### 1.2 Fontes (em ordem de prioridade quando houver conflito)

1. Página da tarefa no Canvas, "Avaliação do RA 1 - Projeto", com rubrica "Atividades do RA 1" (lida em 28/09/2026).
2. Template: `ESSW - Especificacao de Projeto - Template.docx`.
3. Plano de ensino: `BSI_PE_Especificacao de Software_2026_2 - v3 - 2026_08_16.pdf` (a v3 substitui a versão sem data).
4. Lista de tópicos: `Tópicos da Especificação de Software.txt`.

Todos os arquivos ficam na pasta local "01 Especificacao de Software" (OneDrive, 2026.2).

---

## 2. Regras gerais (valem para o documento inteiro)

- [ ] **X.1 — Template.** O documento final (PDF consolidado a partir dos MDs do repositório) segue a estrutura do template oficial: seções na ordem de 1 a 11, títulos originais e quadros no formato do template.
- [ ] **X.2 — Capa.** Nome do produto no lugar de "NOME DO PRODUTO DE SOFTWARE", os 4 autores no lugar de "NOME AUTOR 1..4" e ano **2026** (o template traz 2025).
- [ ] **X.3 — Textos em azul.** Todos os textos personalizáveis (em azul) foram substituídos e estão na cor **preta**.
- [ ] **X.4 — Textos em laranja.** Todos os quadros de aviso e textos de orientação em **laranja** foram removidos.
- [ ] **X.5 — Exemplos do template.** Os exemplos do template foram removidos ou substituídos, por exemplo RF1 "Realizar login de usuário" com o ator genérico e as estórias US001/US002 de exemplo. Um RF de login do próprio sistema pode existir, mas escrito para o nosso contexto.
- [ ] **X.6 — Sumário.** O sumário está atualizado, com números de página corretos.
- [ ] **X.7 — Declaração de uso de IA.** O documento contém a declaração obrigatória (plano de ensino, seção 7.1): *"Durante a preparação deste [TIPO DE CONTEÚDO], o(s) autor(es) usaram [FERRAMENTA, VERSÃO] para [EXPLICITAR MOTIVOS]. Após usar essa ferramenta, o(s) autor(es) revisaram e editaram o conteúdo conforme necessário e assumem total responsabilidade pelo conteúdo."*, preenchida.
- [ ] **X.8 — Regra dos 4 por integrante.** Nos itens que dependem da quantidade de integrantes, o mínimo é **4 itens por integrante**. Com 4 integrantes, o mínimo é **16** (ver itens 6, 7, 8 e 10).
- [ ] **X.9 — Nome do produto.** O mesmo nome aparece em todos os campos "NOME DO PRODUTO" / "PRODUTO" dos quadros.
- [ ] **X.10 — Legibilidade dos diagramas.** Os diagramas (itens 4, 9 e 11) estão legíveis no documento final, sem texto cortado ou ilegível.

---

## 3. Critérios por item

Cada item traz: o que o template pede, o mínimo exigido, o peso na nota e o checklist com o critério **"Excede"** (nota máxima) da rubrica.

Resumo dos pesos:

| Item | Peso | Por integrante? |
|---|---|---|
| 1 – 3 Objetivos | 0,2 | Não |
| 2 – É / Não é / Faz / Não faz | 0,2 | Não |
| 3 – Visão do Produto | 0,2 | Não |
| 4 – Mapeamento de Negócios | 0,2 | Não |
| 5 – Atores / Usuários | 0,2 | Não |
| 6 – Requisitos Funcionais | 0,5 | **Sim (≥16)** |
| 7 – Estórias de Usuário | **1,5** | **Sim (≥16)** |
| 8 – Requisitos Não Funcionais | 0,1 | **Sim (≥16)** |
| 9 – Diagrama Geral de Casos de Uso | 0,2 | Não |
| 10 – Especificações de Caso de Uso | **1,5** | **Sim (≥16)** |
| 11 – Diagrama de Atividades | 0,2 | Não |
| **Total** | **5,0** | |

### 3.1 Item 1 — Quadro "3 Objetivos" (0,2)

**Template:** tabela "QUADRO 3 OBJETIVOS" com NOME DO PRODUTO e as colunas OBJETIVOS / DESCRIÇÃO, linhas 1, 2 e 3. Relaciona os 3 grandes **objetivos de negócio** que o produto deve atender.

- [ ] **C01.1** Exatamente **3** objetivos.
- [ ] **C01.2** Cada objetivo é claro, específico e **verificável**.
- [ ] **C01.3** Cada objetivo articula **problema, valor e métrica de sucesso**: a métrica é explícita e mensurável.
- [ ] **C01.4** Os objetivos são coerentes com a Visão do Produto (item 3) e com os demais artefatos.

### 3.2 Item 2 — Quadro "É – Não é – Faz – Não faz" (0,2)

**Template:** quadro de 4 quadrantes. É = atributos necessários ou desejados; Não é = atributos indesejados ou impeditivos; Faz = ações ou capacidades esperadas; Não faz = ações ou capacidades indesejadas ou não permitidas.

- [ ] **C02.1** Os 4 quadrantes estão preenchidos.
- [ ] **C02.2** Cada quadrante tem **≥3 itens específicos**, não genéricos.
- [ ] **C02.3** Não há contradição entre quadrantes nem com os outros itens.
- [ ] **C02.4** O quadro delimita claramente escopo, anti-escopo, capacidades e restrições. O "Não faz" deve ser coerente com o fora de escopo do projeto: programação de voos, escala de tripulação, financeiro e integração real com controle de tráfego aéreo.

### 3.3 Item 3 — Visão do Produto (0,2)

**Template:** dois quadros.
- Quadro A: **PROBLEMAS** (estado atual, antes da solução) e **EXPECTATIVAS** (estado desejado, alinhado aos problemas).
- Quadro B: **CLIENTE-ALVO**, **CATEGORIA-SEGMENTO**, **BENEFÍCIO-CHAVE**, **DIFERENCIAL-CHAVE** e **META-VALOR**.

- [ ] **C03.1** O quadro A está completo: problemas e expectativas bem definidos.
- [ ] **C03.2** Cada expectativa corresponde a pelo menos um problema levantado.
- [ ] **C03.3** Os 5 campos do quadro B estão preenchidos com precisão.
- [ ] **C03.4** Valor (meta-valor) e diferencial são **verificáveis**, não apenas slogans.
- [ ] **C03.5** Os dois quadros são coerentes entre si e com os itens 1 e 2.

### 3.4 Item 4 — Mapeamento de Negócios (0,2)

**Template:** diagrama **BPMN** do processo de negócio na versão **TO BE**, ou seja, como o processo fica com o sistema.

- [ ] **C04.1** A notação é BPMN de verdade, não um fluxograma improvisado.
- [ ] **C04.2** O diagrama representa apenas o TO BE, sem misturar com o AS IS.
- [ ] **C04.3** Tem evento de **início** e de **fim**.
- [ ] **C04.4** Tem **atividades** rotuladas de forma padronizada.
- [ ] **C04.5** Tem **gateways com condições** escritas nas saídas.
- [ ] **C04.6** Tem **pools/lanes** coerentes com os atores do item 5.
- [ ] **C04.7** Tem eventos e mensagens quando aplicável, por exemplo alertas e eventos do motor de eventos.
- [ ] **C04.8** O caminho principal está representado; o nível de detalhe é adequado e o diagrama é legível.
- [ ] **C04.9** É consistente com a Visão do Produto.

### 3.5 Item 5 — Relação de Atores / Usuários (0,2)

**Template:** tabela `# | ATOR / USUÁRIO`.

- [ ] **C05.1** **≥3 atores**.
- [ ] **C05.2** Cada ator tem **papel e responsabilidades** descritos. Como a tabela do template só tem nome, acrescentar descrição, em coluna extra ou texto abaixo.
- [ ] **C05.3** Cada ator tem sua relação com o processo e com o sistema explicitada.
- [ ] **C05.4** As descrições são sucintas, sem ambiguidade e sem sobreposição de papéis.
- [ ] **C05.5** Os atores são os mesmos usados nas lanes do BPMN (item 4), nos RFs (item 6), nas estórias (item 7) e nos casos de uso (itens 9 e 10).

Referência do projeto (já definida pelo grupo): Operador de Solo/Rampa, Coordenador de Turnaround (ADR-0009), Autoridade de Liberação, Administrador do Sistema (ADR-0010) e o ator não humano Motor de Eventos; no diagrama de casos de uso (item 9), o ator abstrato Usuário generaliza os atores humanos (ADR-0010).

### 3.6 Item 6 — Relação de Requisitos Funcionais (0,5) · por integrante

**Template:** tabela `# | REQUISITO FUNCIONAL | ATOR / USUÁRIO | SPRINT`. Relacionar **todos** os requisitos do sistema completo.

- [ ] **C06.1** **≥16 RFs** (4 por integrante).
- [ ] **C06.2** Enumeração padrão **RF-n**, sequencial e sem lacunas.
- [ ] **C06.3** Cada RF está redigido de forma clara e **testável**: uma ação verificável, sem "etc." e sem termos vagos.
- [ ] **C06.4** Cada RF é rastreado a um **ator** (coluna preenchida, com ator do item 5).
- [ ] **C06.5** Cada RF é rastreado a um **objetivo** do item 1.
- [ ] **C06.6** A **priorização** está presente: coluna SPRINT preenchida e/ou prioridade.
- [ ] **C06.7** Há uma **breve justificativa** da priorização.
- [ ] **C06.8** Os RFs cobrem o núcleo operacional do produto: orquestração do turnaround, execução paralela de tarefas, propagação de estado, cálculo de atraso e caminho crítico, dashboard em tempo real, alertas e redistribuição de recursos. Não se limitam a CRUD.

### 3.7 Item 7 — Relação de Estórias de Usuário (1,5) · por integrante

**Template:** para cada estória, `USnnn – REQUISITO n: <nome>`, **COMO / POSSO / PARA** e Critérios de Aceite numerados em **DADO QUE / QUANDO / ENTÃO**.

- [ ] **C07.1** **≥16 estórias** (4 por integrante).
- [ ] **C07.2** Todas no formato **COMO / POSSO / PARA**.
- [ ] **C07.3** Cada estória está vinculada a um RF correspondente, com o número do RF no título.
- [ ] **C07.4** Cada estória tem **≥2 critérios de aceite**.
- [ ] **C07.5** Todos os critérios estão no formato **DADO QUE / QUANDO / ENTÃO**, claros e **verificáveis**, com resultado observável.
- [ ] **C07.6** Os critérios cobrem cenários diferentes (caminho principal e ao menos uma variação ou erro), e não repetições do mesmo cenário.
- [ ] **C07.7** As estórias são consistentes com as outras especificações: atores, RFs e casos de uso.

### 3.8 Item 8 — Relação de Requisitos Não Funcionais (0,1) · por integrante

**Template:** tabela `# | REQUISITO NÃO-FUNCIONAL | NORMA ISO/IEC 25010`. O plano de ensino exige a classificação pela ISO/IEC 25010.

- [ ] **C08.1** **≥16 RNFs** (4 por integrante).
- [ ] **C08.2** Enumeração padrão **RNF-n**.
- [ ] **C08.3** Cada RNF está classificado em uma característica da **ISO/IEC 25010**.
- [ ] **C08.4** Cada RNF é **mensurável**, com medida ou critério de aceitação objetivo (ex.: tempo de resposta ≤ X s no percentil 95). Nada de "ser rápido" ou "ser seguro".
- [ ] **C08.5** Cobre várias categorias: desempenho, segurança/LGPD, confiabilidade, usabilidade e manutenibilidade, no mínimo.

### 3.9 Item 9 — Diagrama Geral de Casos de Uso (0,2)

**Template:** diagrama geral considerando **generalização de atores** e **inclusão e extensão** de casos de uso.

- [ ] **C09.1** Tem **fronteira do sistema** com o nome do produto.
- [ ] **C09.2** Os atores estão corretos e são os mesmos do item 5.
- [ ] **C09.3** Os casos de uso principais correspondem aos RFs (≈ RF).
- [ ] **C09.4** Tem **generalização de atores** onde fizer sentido, como o template pede.
- [ ] **C09.5** Tem relacionamentos **include/extend** onde forem pertinentes, com a direção correta das setas.
- [ ] **C09.6** Os nomes dos casos de uso são consistentes com os RFs e as estórias.
- [ ] **C09.7** O diagrama é legível.

### 3.10 Item 10 — Especificações de Caso de Uso (1,5) · por integrante

**Template:** para cada caso de uso, no formato reduzido: **Nome, Ator(es), Descrição, Pré-condições, Pós-condições, Regras de negócio, Protótipo(s) de tela, Fluxo básico, Fluxos alternativos, Fluxos de exceção**. O plano de ensino pede **protótipos de tela de alta fidelidade**.

- [ ] **C10.1** **≥16 especificações** (4 por integrante × 4 integrantes). Decisão fechada pelo grupo; o "mínimo 8" do plano de ensino não se aplica.
- [ ] **C10.2** Cada especificação tem os **10 campos** preenchidos.
- [ ] **C10.3** Cada especificação tem **protótipo(s) de tela de alta fidelidade**.
- [ ] **C10.4** Cada especificação tem **fluxo básico** completo, em passos numerados.
- [ ] **C10.5** Cada especificação tem ao menos um **fluxo alternativo** (variação intencional do ator).
- [ ] **C10.6** Cada especificação tem ao menos um **fluxo de exceção** (variação não intencional ou erro).
- [ ] **C10.7** A linguagem é testável: cada passo é observável.
- [ ] **C10.8** Cada especificação corresponde a um caso de uso do diagrama (item 9), com o mesmo nome e os mesmos atores.
- [ ] **C10.9** As regras de negócio são coerentes com as estórias e os RFs.

### 3.11 Item 11 — Diagrama de Atividades (0,2)

**Template:** diagrama de atividades do sistema, em notação UML.

- [ ] **C11.1** Representa o **fluxo principal**.
- [ ] **C11.2** Representa os **fluxos alternativos**.
- [ ] **C11.3** Tem **decisões** com **condições de guarda** escritas.
- [ ] **C11.4** Tem **atividades paralelas** (fork/join), essenciais neste domínio de tarefas de turnaround em paralelo.
- [ ] **C11.5** Tem **responsabilidades** (partições/raias) coerentes com os atores.
- [ ] **C11.6** A notação UML é usada corretamente: nó inicial e final, ações, decisão/merge, fork/join.
- [ ] **C11.7** É legível e aderente à documentação (atores, casos de uso, BPMN).

---

## 4. Dependências e ordem de execução

```
Itens 1, 2, 3  (base do produto)
      │
      ├──► Item 5 (atores) ──► Item 4 (BPMN, lanes = atores)
      │                    │
      │                    └──► Item 6 (RFs, ator por RF)
      │                              │
      │                              ├──► Item 7 (estórias, 1 por RF)
      │                              ├──► Item 9 (diagrama de casos de uso ≈ RFs)
      │                              │         │
      │                              │         └──► Item 10 (especificações, 1 por caso de uso)
      │                              │                   │
      │                              │                   └──► Item 11 (atividades)
      └──► Item 8 (RNFs) — pode ser feito em paralelo após os itens 1 a 3
```

- **Uma pessoa só:** itens 1, 2 e 3; recomenda-se a mesma pessoa para o item 5 e para o item 4, por serem de visão única do produto.
- **Por integrante (4 cada):** itens 6, 7, 8 e 10. Cada integrante fica com um conjunto de RFs e, a partir deles, com as estórias e as especificações de caso de uso correspondentes. Isso mantém a rastreabilidade RF → estória → caso de uso na mesma pessoa.
- **Integração:** os itens 9 e 11 consolidam o trabalho de todos, então precisam de um responsável que junte as partes.
- **Janela de tempo:** de 28/09 a 10/10. A semana de 01/10 é Poliweek.

---

## 5. Checklist final de consistência cruzada

Executar depois que todos os itens estiverem prontos, e de novo antes do envio.

- [ ] **K.1** Os mesmos atores (nomes idênticos) aparecem nos itens 4, 5, 6, 7, 9, 10 e 11.
- [ ] **K.2** Todo RF (item 6) tem **exatamente uma** estória (item 7) e toda estória aponta para um RF existente.
- [ ] **K.3** Todo RF está coberto por **pelo menos um** caso de uso no diagrama (item 9).
- [ ] **K.4** Toda especificação (item 10) corresponde a um caso de uso do diagrama (item 9), com o mesmo nome.
- [ ] **K.5** Os critérios de aceite das estórias não contradizem as regras de negócio nem os fluxos das especificações do mesmo requisito.
- [ ] **K.6** Os objetivos (item 1) são atendidos por algum RF e aparecem refletidos na Visão (item 3).
- [ ] **K.7** Nada listado em "Não faz" (item 2) aparece como RF, estória ou caso de uso.
- [ ] **K.8** As lanes do BPMN (item 4) e as raias do diagrama de atividades (item 11) usam os atores do item 5.
- [ ] **K.9** As contagens mínimas conferem por contagem real: RF ≥16, estórias ≥16, cada estória com ≥2 critérios, RNF ≥16, especificações ≥16.
- [ ] **K.10** Todos os critérios gerais X.1 a X.10 estão atendidos.
- [ ] **K.11** Nenhum item contradiz o `CONTEXT.md` nem as decisões D1–D10 (`docs/adr/`), e todo número ou sigla do setor usado na especificação cita a fonte da pesquisa (`pesquisa/fontes.md`).

---

## 6. Pontos em aberto

- ~~**A1.** Quantidade de especificações de caso de uso.~~ **Resolvido:** 16 (4 por integrante × 4 integrantes), confirmado pelo grupo.
- ~~**A2.** Quais itens são "dependentes da quantidade de integrantes".~~ **Resolvido:** itens 6, 7, 8 e 10 (os marcados na rubrica com "≥ mínimo por integrante"), confirmado pelo grupo.
- ~~**A3.** Formato de envio.~~ **Resolvido:** **PDF**, gerado a partir da consolidação dos arquivos MD do repositório, seguindo a estrutura do template.
