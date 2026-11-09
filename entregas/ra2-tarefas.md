# Quebra de Tarefas — RA2 (Especificação do Projeto, itens 12 a 15)

> Plano de tarefas para o GitHub Project **"Especificação de Software - 6p"**, derivado de [`ra2-criterios-de-aceite.md`](ra2-criterios-de-aceite.md).
> Os critérios (IDs `C00.y`, `C12.y` a `C15.y`, `Y.y`, `K.y`) estão definidos naquele arquivo. Aqui só se referenciam os IDs.
> **Status:** aprovado pelo Rodrigo em 08/11/2026 — pronto para criação no GitHub.

---

## 1. Decisões de divisão

### 1.1 Responsáveis fixos

- **Ajustes do RA1 (C00.1 a C00.10) e itens 12 e 13:** Rodrigo Alves (`rdsalvesPUC`), por formarem um modelo único do sistema (decisão B7).
- **Itens 14 e 15:** por área, cada integrante com os casos de uso e as estórias da sua área (seção 1.2).
- **Escolha da tecnologia de cada serviço:** cada integrante para o seu serviço, numa sub-issue própria e numa ADR própria (decisão B2).
- **Preparação, revisão final, consolidação e envio:** sem responsável. Quem puxar a tarefa se coloca como responsável ao começar.

### 1.2 Divisão por área (itens 14 e 15)

As áreas do RA1 passaram a corresponder aos quatro serviços (ADR-0015). Depois da troca de área (C00.6), a divisão fica assim:

| Área | Serviço | Casos de uso (item 14) | Estórias e critérios (item 15) | Responsável |
|---|---|---|---|---|
| **A** | Cadastro e Planejamento | 11 (UC01 a UC11) | 11 estórias, 48 critérios | Eduardo Fabri (`eduardofabrii`) |
| **B** | Execução em Solo | 11 (UC12 a UC21 e UC37) | 11 estórias, 47 critérios | João Pedro Cardoso de Liz (`Jcliz`) |
| **C** | Monitoramento | 7 (UC22 a UC28) | 14 estórias, 52 critérios | João Vitor Correa Oliveira (`jvecodev`) |
| **D** | Exceções e Liberação | 8 (UC29 a UC36) | 8 estórias, 32 critérios | Rodrigo Alves (`rdsalvesPUC`) |
| **Total** | | **37** | **44 estórias, 179 critérios** | |

A divisão por área serve só para dividir o trabalho. Diagramas e textos agrupam por função do sistema.

### 1.3 Fluxo de trabalho

O fluxo é o mesmo do RA1 ([`ra1-tarefas.md`](ra1-tarefas.md), seção 1.3), com estes acréscimos:

- **Diagramas:** cada diagrama tem a fonte editável em `especificacao/diagramas/`, ao lado da SVG e da PNG exportadas (Y.6 e Y.7). Diagrama grande tem uma visão geral e vistas detalhadas. A ferramenta dos diagramas de sequência sai da tarefa T02 (decisão B3).
- **Contrato entre os serviços:** os itens 12 a 15 seguem a ADR-0016 (nomes, identificadores, horários em UTC, envelope dos avisos, porta de entrada).
- **Checagem cruzada:** antes de mudar um diagrama e de novo ao terminar, cada passo, sigla e marco é conferido contra o RF e o caso de uso que o definem (`AGENTS.md`, regra 6; Y.8).

### 1.4 Pendências cruzadas entre áreas

Valem as regras do RA1 ([`ra1-tarefas.md`](ra1-tarefas.md), seção 1.4): uma issue com o rótulo `pendencia-cruzada` por área e item, registrada como bloqueio da tarefa-mãe. Como os itens 12 e 13 são de um responsável só, a pendência mais provável vai no sentido contrário: um diagrama de sequência (item 14) precisa de uma tabela, de um campo ou de um método que não existe nos itens 12 e 13. Nesse caso, a linha vai para a issue de pendência do item 12 ou 13, atribuída a `rdsalvesPUC`, e o método entra no item 13 (C13.8).

---

## 2. Rótulos (labels)

Já existem: `ra2`, `geral`, `por-integrante`, `area-a` … `area-d` e `pendencia-cruzada`. Falta criar:

| Rótulo | Cor | Uso |
|---|---|---|
| `item-12` … `item-15` | `#C5DEF5` | Item do template a que a tarefa se refere |
| `ajustes-ra1` | `#C5DEF5` | Ajustes pedidos na correção do RA1 (seção 3.0 dos critérios) |

---

## 3. Lista de tarefas

Convenção de título: `[RA2][Item NN] <descrição>`. Para tarefas gerais, `[RA2][Geral] <descrição>`, e para os ajustes do RA1, `[RA2][Ajustes do RA1] <descrição>`.

As tarefas T04, T14 e T15 são **tarefas-mãe** com quatro **sub-issues** cada, uma por área.

Total: **23 issues**, sendo 11 principais e 12 sub-issues. A issue #136, fechada como "não planejada", é substituída por T00.

### Fase 0 — Ajustes do RA1 (Rodrigo)

**T00 · [RA2][Ajustes do RA1] Título ARO dos RFs e troca de área**
- Responsável: `rdsalvesPUC` · Rótulos: `ra2`, `ajustes-ra1`, `item-06`
- Descrição: dar a cada um dos 44 RFs um título no padrão Ação-Resultado-Objeto (ARO), partindo dos títulos das estórias, e propagá-lo para as estórias, a matriz e os casos de uso. No mesmo PR, porque mexem nos mesmos arquivos: passar RF-12, RF-13, RF-44, US012, US013, US044, UC12, UC13 e UC37 para os arquivos da área B, fazer o gerador ordenar os IDs por número e reescrever a introdução do item 10. Nenhum número muda.
- Critérios: C00.1 a C00.9
- Bloqueia: T01, T12, T15 (os itens 14 e 15 citam os títulos dos RFs). É a primeira tarefa do RA2 e entra na `main` antes de qualquer item novo.

**T01 · [RA2][Ajustes do RA1] Sprints do item 6 pelas dependências entre RFs**
- Responsável: `rdsalvesPUC` · Rótulos: `ra2`, `ajustes-ra1`, `item-06`
- Descrição: refazer a coluna SPRINT e a justificativa da priorização do item 6 a partir das dependências reais entre os RFs, com um responsável por serviço (ADR-0015). Um RF entra numa sprint igual ou posterior à dos RFs de que depende, salvo quando o texto justifica o uso de dados simulados.
- Critérios: C00.10
- Bloqueada por: T00 (mesmos arquivos)

### Fase 1 — Preparação

**T02 · [RA2][Item 14] Testar a ferramenta dos diagramas de sequência**
- Responsável: quem puxar · Rótulos: `ra2`, `item-14`
- Descrição: desenhar o mesmo caso de uso em Mermaid e em PlantUML, gerar o PDF e comparar a legibilidade (Y.6). Se os dois ficarem ruins, usar o draw.io. Registrar a escolha, com o arquivo de exemplo, no `README.md` do repositório.
- Critérios: decisão B3; Y.6 e Y.7 no diagrama de teste
- Bloqueia: T14

**T03 · [RA2][Geral] Preparar a estrutura, o gerador e a matriz para os itens 12 a 15**
- Responsável: quem puxar · Rótulos: `ra2`, `geral`
- Descrição: criar os arquivos dos itens 12 e 13 e as pastas dos itens 14 e 15, com um arquivo por área, no mesmo padrão dos itens 6 a 10. Incluir os itens 12 a 15 e o Apêndice B no `scripts/gerar_docx.py`, que hoje os remove. Estender a matriz de rastreabilidade com as colunas dos itens 12 a 15, atualizando a ADR-0012 e `scripts/gerar_matriz_rastreabilidade.py` (decisão B5).
- Critérios: Y.1 (estrutura); decisões B5 e B6
- Bloqueia: T12, T14, T15

**T04 · [RA2][Geral] Escolher a tecnologia de cada serviço (4 ADRs)** — tarefa-mãe
- Responsável: quem puxar (conferência) · Rótulos: `ra2`, `geral`
- Descrição: cada integrante escolhe a linguagem, o framework e o banco do seu serviço, seguindo o contrato da ADR-0016, e registra a escolha numa ADR própria, com o número reservado para não haver conflito entre PRs em paralelo. A tarefa-mãe fecha quando as quatro sub-issues fecharem e alguém conferir que as quatro escolhas respeitam a ADR-0016.
- Critérios: decisão B2
- Não bloqueia os itens 12 a 15. Os itens usam tipos SQL padrão e tipos UML neutros (decisão B1).
- Sub-issues:
  - **T04-A** · Cadastro e Planejamento · ADR-0017 · `eduardofabrii` · `area-a`
  - **T04-B** · Execução em Solo · ADR-0018 · `Jcliz` · `area-b`
  - **T04-C** · Monitoramento · ADR-0019 · `jvecodev` · `area-c`
  - **T04-D** · Exceções e Liberação · ADR-0020 · `rdsalvesPUC` · `area-d`
  - Rótulos de cada uma: `ra2`, `geral`, `por-integrante`, `area-x`

### Fase 2 — Modelagem (Rodrigo)

**T12 · [RA2][Item 12] Modelo de dados**
- Responsável: `rdsalvesPUC` · Rótulos: `ra2`, `item-12`
- Descrição: um modelo lógico relacional em notação de linguagem de modelagem unificada (UML) para cada serviço, mais uma visão geral, e o dicionário de dados no Apêndice B.
- Critérios: C12.1 a C12.10
- Bloqueada por: T00, T03 · Bloqueia: T13

**T13 · [RA2][Item 13] Diagrama de classes**
- Responsável: `rdsalvesPUC` · Rótulos: `ra2`, `item-13`
- Descrição: as classes de negócio a partir do item 12 e as classes técnicas das camadas de referência (`Controller → Service → Repository`), com uma visão geral e vistas por função do sistema.
- Critérios: C13.1 a C13.10. O C13.8 só fecha depois do item 14: os métodos que os diagramas de sequência pedirem entram aqui.
- Bloqueada por: T12 · Bloqueia: T14

### Fase 3 — Por área (todos)

**T14 · [RA2][Item 14] Diagramas de sequência (37, um por caso de uso)** — tarefa-mãe
- Responsável: quem puxar (consolidação) · Rótulos: `ra2`, `item-14`
- Descrição: começar pela conferência cruzada do item (seção 1.4). Depois, conferir as legendas e a contagem dos 37 diagramas e ajustar o C13.8 com o responsável do item 13.
- Critérios: C14.1 a C14.8
- Bloqueada por: T02, T03, T13
- Sub-issues:
  - **T14-A** · UC01 a UC11 (11 diagramas) · `eduardofabrii` · `area-a`
  - **T14-B** · UC12 a UC21 e UC37 (11 diagramas) · `Jcliz` · `area-b`
  - **T14-C** · UC22 a UC28 (7 diagramas) · `jvecodev` · `area-c`
  - **T14-D** · UC29 a UC36 (8 diagramas) · `rdsalvesPUC` · `area-d`
  - Rótulos de cada uma: `ra2`, `item-14`, `por-integrante`, `area-x`
  - Critérios de cada sub-issue: C14.2 a C14.8 para todos os casos de uso da área

**T15 · [RA2][Item 15] Casos de teste (179 critérios de aceite)** — tarefa-mãe
- Responsável: quem puxar (consolidação) · Rótulos: `ra2`, `item-15`
- Descrição: começar pela conferência cruzada do item. Depois, juntar as planilhas das áreas, numerar os casos de teste de forma única (CT-nnn) e conferir por script a cobertura dos critérios e dos fluxos.
- Critérios: C15.1 a C15.8
- Bloqueada por: T00, T03. Não depende dos itens 12 a 14 e pode correr em paralelo com eles.
- Sub-issues:
  - **T15-A** · Casos de teste da área A (11 estórias, 48 critérios; UC01 a UC11) · `eduardofabrii` · `area-a`
  - **T15-B** · Casos de teste da área B (11 estórias, 47 critérios; UC12 a UC21 e UC37) · `Jcliz` · `area-b`
  - **T15-C** · Casos de teste da área C (14 estórias, 52 critérios; UC22 a UC28) · `jvecodev` · `area-c`
  - **T15-D** · Casos de teste da área D (8 estórias, 32 critérios; UC29 a UC36) · `rdsalvesPUC` · `area-d`
  - Rótulos de cada uma: `ra2`, `item-15`, `por-integrante`, `area-x`
  - Critérios de cada sub-issue: C15.1 a C15.7 para todas as estórias e casos de uso da área

### Fase 4 — Fechamento

**T16 · [RA2][Geral] Revisão cruzada e verificação independente**
- Responsável: quem puxar · Rótulos: `ra2`, `geral`
- Descrição: com tudo na `main`, gerar de novo a matriz de rastreabilidade (sem lacunas) e rodar `scripts/verificar_revisao.py` e `scripts/marcos_nos_diagramas.py`. Depois, executar o checklist de consistência cruzada e a verificação independente (seção 0.3 dos critérios), com a tabela `ID | status | evidência`. O que não passar volta para o responsável.
- Critérios: K.1 a K.12, Y.1 a Y.8, e todos os `C00.y` e `C12.y` a `C15.y`
- Bloqueada por: T00 a T15

**T17 · [RA2][Geral] Consolidar em PDF e enviar no Canvas**
- Responsável: quem puxar · Rótulos: `ra2`, `geral`
- Descrição: gerar o documento completo, com os itens 1 a 15, o Apêndice A, o Apêndice B e as referências, além da declaração de uso de IA atualizada. Exportar em PDF e enviar na tarefa "Avaliação do RA 2 - Projeto" até **sábado, 28/11/2026, às 23:59**.
- Critérios: Y.1, Y.3, Y.6, C00.3, C00.4, C15.8
- Bloqueada por: T16

---

## 4. Calendário de referência

O plano de ensino tem aulas práticas em 05/11 (diagramas de sequência), em 12/11 e 19/11 (casos de teste) e o TDE3 em 21/11. A entrega é em 28/11. Como o item 14 depende de T00, T12 e T13, essa é a cadeia mais longa: T00 → T12 → T13 → T14. O item 15 pode começar logo depois de T00.

---

## 5. Corpo padrão de cada issue

É o mesmo do RA1 ([`ra1-tarefas.md`](ra1-tarefas.md), seção 4), com duas trocas: os critérios vêm de `entregas/ra2-criterios-de-aceite.md`, e os insumos incluem as ADRs 0015 e 0016 e as decisões da seção 6 daquele arquivo. Cada critério é copiado com o texto resumido, e não só com o ID.

---

## 6. Instruções para o Claude Code (criação no GitHub)

**Pré-requisitos:** `gh` autenticado com o escopo `project`. Repositório: `Aircraft-Turnaround-Operations-Manager/aircraft-turnaround-docs`. Project: número **1** da organização.

Siga o protocolo da seção 0.3 de `ra2-criterios-de-aceite.md`.

1. Ler este arquivo e `ra2-criterios-de-aceite.md` por inteiro.
2. Criar os rótulos da seção 2, ignorando os que já existirem.
3. Criar as 11 issues principais na ordem da seção 3, com título, corpo no formato da seção 5, rótulos e responsáveis. Guardar o número de cada uma.
4. Criar as 12 sub-issues (T04-A a T04-D, T14-A a T15-D) e vinculá-las como sub-issues das tarefas-mãe.
5. Preencher "Bloqueada por" e "Bloqueia" nos corpos com os números reais e registrar também o relacionamento nativo de bloqueio do GitHub.
6. Adicionar as 23 issues ao project 1 com Status **Todo**.
7. **Verificar por comando:**
   - 23 issues novas com o rótulo `ra2`;
   - 23 itens novos no project, todos com Status Todo;
   - 3 tarefas-mãe com 4 sub-issues cada;
   - cada sub-issue com o responsável da tabela 1.2;
   - T00, T01, T12 e T13 com `rdsalvesPUC`; as demais principais sem responsável;
   - nenhum `#<n>` pendente nos corpos.
8. Relatório final em tabela: `Tarefa | nº da issue | responsável | status no project | verificado (sim/não)`.

---

## 7. Pontos em aberto

- **P1. Datas-alvo no board:** este plano não preenche Start date nem Target date, como no RA1. Se o grupo quiser datas, a seção 4 serve de base.
- **P2. Tarefas do contrato (ADR-0016):** a estrutura inicial do site (`Jcliz`) e a porta de entrada (`eduardofabrii`) são tarefas de implementação. Ficam fora deste plano, que cobre só a especificação.
