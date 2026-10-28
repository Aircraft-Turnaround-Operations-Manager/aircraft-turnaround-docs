# Critérios de Aceite da Entrega — RA2 (Especificação do Projeto, itens 12 a 15)

> Definition of Done do documento de especificação que o grupo entrega na Avaliação do RA 2.
> Este arquivo **não é** o documento de especificação. Ele define **o que** o documento precisa conter e **como verificar** que está pronto.
> O RA2 entrega o documento **completo**: os itens 1 a 11 continuam valendo pelos critérios do [RA1](ra1-criterios-de-aceite.md), e este arquivo acrescenta os ajustes pedidos na correção do RA1 e os itens 12 a 15.

---

## 0. Como usar este documento

### 0.1 Para quem monta o board (GitHub Projects)
- Cada seção de 3.0 a 3.4 vira **uma ou mais tarefas** no board.
- O ajuste do título ARO (seção 3.0) é a **primeira tarefa** do RA2, antes de qualquer item novo; ela e os itens 12 e 13 ficam com rdsalvesPUC.
- Os itens 14 e 15 são divididos por área (A, B, C e D), seguindo os casos de uso e as estórias que cada integrante escreveu no RA1 (seção 4).
- A ordem e os bloqueios entre tarefas estão na **seção 4**.
- O corpo de cada tarefa copia os IDs dos critérios correspondentes (ex.: `C14.1` a `C14.8`), para que o checklist acompanhe a tarefa.

### 0.2 Para quem escreve um item
- Antes de começar, leia a seção do item, o checklist dele e as decisões da seção 6 que o afetam.
- Um item só está pronto quando **todos** os critérios dele estão atendidos **e** a consistência da seção 5 foi conferida para ele.

### 0.3 Protocolo de execução e verificação (obrigatório para agentes de IA)

É o mesmo protocolo do RA1 ([seção 0.3](ra1-criterios-de-aceite.md#03-protocolo-de-execução-e-verificação-obrigatório-para-agentes-de-ia)):

1. **Condição de conclusão:** todos os critérios aplicáveis deste arquivo (`C00.y`, `C12.y` a `C15.y`, `Y.y` e `K.y`) marcados como atendidos, cada um com evidência.
2. **Lista de tarefas antes de começar,** com um item por ID de critério do escopo pedido.
3. **Evidência por critério:** seção do documento, contagem feita, nome do arquivo do diagrama ou da planilha.
4. **Contagem por comando, não por estimativa:** 37 diagramas de sequência, 179 critérios de aceite cobertos etc. são conferidos por script ou listagem.
5. **Não encerrar com itens abertos;** só parar em bloqueio real, dizendo qual critério e por quê.
6. **Verificação independente ao final,** separada da escrita, que recebe só este arquivo e o documento produzido.
7. **Relatório final** em tabela `ID | status | evidência`.

---

## 1. Contexto da entrega

| Campo | Valor |
|---|---|
| Disciplina | Especificação de Software (PSI151) — BSI PUCPR, 6º período, Turma 6º A, noite |
| Professor | Evandro Alberto Zatti |
| Tarefa no Canvas | Avaliação do RA 2 - Projeto |
| Prazo | **Sábado, 28/11/2026, 23:59** |
| Valor | 5,0 pontos (5 critérios de 1,0) |
| Envio | Único para o grupo inteiro ("contado para todos em seu grupo"); tentativas ilimitadas até o prazo; formatos aceitos: URL, upload ou Office 365 |
| O que se entrega | "Documento de especificação COMPLETO, com itens da entrega anterior + os itens" 12 a 15 |
| Nota do RA1 | 5,0/5,0 (tentativa 2, de 23/10); não há recuperação de RA1 a fazer |
| Produto | Aircraft Turnaround Orchestration System (organização GitHub: Aircraft-Turnaround-Operations-Manager) |

### 1.1 Integrantes

| Integrante | GitHub | Área no RA1 |
|---|---|---|
| Eduardo Fabri | `eduardofabrii` | A — acesso e planejamento |
| João Pedro Cardoso de Liz | `Jcliz` | B — execução em solo |
| João Vitor Correa Oliveira | `jvecodev` | C — monitoramento |
| Rodrigo Alves | `rdsalvesPUC` | D — exceções e liberação |

### 1.2 Fontes (em ordem de prioridade quando houver conflito)

1. Página da tarefa no Canvas, "Avaliação do RA 2 - Projeto", com rubrica "Atividades do RA 2" (lida em 28/10/2026).
2. Correção do RA1 no Canvas: anotações do professor no PDF da tentativa 1 e comentários das tentativas 1 e 2 (lidos em 28/10/2026; seção 3.0).
3. Template: `ESSW - Especificacao de Projeto - Template.docx`, seções 12 a 15.
4. Slides do professor: `ESSW_TE4 - Modelagem de Dados.pdf`, `ESSW_TE5_1 - Modelagem Estrutural.pdf`, `ESSW_TE5_2 - Modelagem Comportamental.pdf` e `ESSW_TE6 - Verificacao e Validacao de Software.pdf`; para o ajuste do RA1, `ESSW_TE3_2 - Requisitos de Sistema.pdf`.
5. Plano de ensino: `BSI_PE_Especificacao de Software_2026_2 - v3 - 2026_08_16.pdf`.

Todos os arquivos ficam na pasta local "01 Especificacao de Software" (OneDrive, 2026.2).

### 1.3 O que cada fonte pede para os itens 12 a 15

| Item | Canvas (descrição da tarefa) | Template | Plano de ensino (avaliação formativa) |
|---|---|---|---|
| 12 | "um diagrama do modelo lógico relacional, utilizando notação UML" | Entidades que atendem ao tema, "de acordo com os REQUISITOS FUNCIONAIS mapeados, evidenciando seus relacionamentos" | Diagrama do modelo lógico do banco de dados, relacional, em UML |
| 13 | "um diagrama com notação UML, em nível técnico (contendo atributos tipados e métodos em nível de implementação)" | Classes do sistema "já considerando a arquitetura de implementação", em nível técnico | Classes com elementos "negociais quanto de implementação" |
| 14 | "um diagrama para cada caso de uso apresentado anteriormente" | "Sequência de interação entre as camadas, para cada caso de uso especificado"; legenda "Diagrama de Sequência do UC00n" | No mínimo 4 casos de uso (só na atividade formativa) |
| 15 | "planilha de casos de teste, considerando os diferentes cenários previstos nos critérios de aceite das histórias de usuário" | Casos de teste projetados "a partir das especificações de caso de uso", na "PLANILHA DE CASOS DE TESTE" | No mínimo 4 casos de uso (só na atividade formativa) |

A coluna do plano de ensino descreve a **atividade prática feita em aula** (avaliação formativa, sem nota no RA2), que pede diagramas e casos de teste de no mínimo 4 casos de uso. Esse mínimo **não vale** para a entrega do RA2, que segue a tarefa e a rubrica: **um diagrama de sequência para cada um dos 37 casos de uso** e casos de teste para **todos** os critérios de aceite.

---

## 2. Regras gerais (valem para o documento inteiro)

- [ ] **Y.1 — Documento completo.** O PDF tem os itens 1 a 15 na ordem e com os títulos do template, seguidos do Apêndice A e das referências. Os itens 12 a 15 entram no lugar das seções 12 a 15 do template, que hoje o `scripts/gerar_docx.py` remove (opção `--manter-ra2`).
- [ ] **Y.2 — Itens 1 a 11 continuam prontos.** Todos os critérios do RA1 (`C01.1` a `C11.7`, `X.1` a `X.10` e `K.1` a `K.13`) continuam atendidos depois das mudanças do RA2. Se a modelagem dos itens 12 a 14 revelar lacuna ou contradição nos itens 1 a 11, corrige-se o item de origem (com PR próprio) em vez de contornar no modelo.
- [ ] **Y.3 — Capa, cabeçalho e textos do template.** Ano **2026** na capa e no cabeçalho; nos itens 12 a 15, os textos em azul do template foram substituídos e os de orientação em laranja foram removidos.
- [ ] **Y.4 — Nomes exatos.** Produto, atores e estados com os nomes do `CONTEXT.md` (seções 1 a 3) também nos diagramas, nas classes e na planilha; nomes de classes e tabelas podem seguir a convenção técnica (seção 6, B2), mas o texto do item diz a qual ator ou estado cada uma corresponde.
- [ ] **Y.5 — Siglas (ADR-0008).** Em cada um dos itens 12 a 15, a primeira ocorrência de cada sigla vem com o nome em português, inclusive UML, SGBD, MVC, PK e FK.
- [ ] **Y.6 — Diagramas legíveis na tela.** Cada diagrama dos itens 12 a 14 é legível no PDF ao ampliar, sem texto cortado, sobreposto ou cruzado por linhas; diagrama grande ganha visão geral mais vistas detalhadas. Os diagramas entram em SVG no documento (vetoriais), com a PNG de reserva.
- [ ] **Y.7 — Fonte editável versionada.** Cada diagrama tem a fonte editável em `especificacao/diagramas/`, ao lado da imagem exportada, como os dos itens 4, 9 e 11. A planilha do item 15 entra só no PDF, como tabela gerada da fonte Markdown do item (seção 6, B4).
- [ ] **Y.8 — Checagem cruzada dos diagramas (AGENTS.md, regra 6).** Todo passo, mensagem, sigla e marco dos diagramas novos bate com o RF e o UC que o definem (quem faz, o que é gravado e por quem). `python scripts/marcos_nos_diagramas.py` não deixa nenhuma linha "conferir".

---

## 3. Critérios por item

Cada item traz: o que pedem as fontes, o peso na nota e o checklist com o critério **"Excede"** (nota máxima) da rubrica.

| Critério da rubrica | Peso | Seção |
|---|---|---|
| Ajustes do RA 1 | 1,0 | 3.0 |
| Modelo de Dados (item 12) | 1,0 | 3.1 |
| Diagrama de Classes (item 13) | 1,0 | 3.2 |
| Diagramas de Sequência (item 14) | 1,0 | 3.3 |
| Casos de Teste (item 15) | 1,0 | 3.4 |
| **Total** | **5,0** | |

### 3.0 Ajustes do RA1 (1,0)

**Rubrica:** "Avalia se foram implementados os ajustes solicitados na correção do RA 1 (primeira parcial do documento)". Excede = **todos** os ajustes apontados implementados; Domínio = pelo menos a metade.

**Ordem e responsável:** é a primeira tarefa do RA2 e entra na `main` antes de qualquer item novo, porque os itens 14 e 15 citam os títulos dos RFs. Responsável: rdsalvesPUC.

**Ajustes apontados** (anotações no PDF da tentativa 1, de 10/10; a tentativa 2 não tem anotações):

| # | Página (tentativa 1) | Anotação do professor | Situação em 28/10 |
|---|---|---|---|
| 1 | 14 — tabela de RFs | "faltou o título de cada RF no padrão ARO" | **Pendente** |
| 2 | 14 — tabela de RFs | "dica: quando tiver uma coluna de uma tabela que tem muito mais texto que as outras, ajustem a largura para que ela seja priorizada." | Corrigido na tentativa 2 (largura pelo conteúdo) |
| 3 | 31 — tabela da US002 | "mais uma vez: ajustar a largura" | Corrigido na tentativa 2 |
| 4 | 65 — UC01 | "Faltaram os protótipos de tela. Acho que deu algum problema com referência das imagens." | Corrigido na tentativa 2 ("Agora com os protótipos") |
| 5 | 65 — "[imagem não encontrada: …]" | "???" | Corrigido na tentativa 2 (mesmo problema do 4) |

**Padrão ARO** (slides `ESSW_TE3_2`, p. 11): o título do requisito funcional usa **Ação-Resultado-Objeto**, por exemplo "Gerenciar cadastro do cliente" e "Solicitar entrega do pedido".

- [ ] **C00.1** Cada um dos 44 RFs do item 6 tem um **título no padrão ARO** (ação + resultado + objeto), visível na tabela do item 6 no PDF.
- [ ] **C00.2** O título de cada RF é o mesmo em todo lugar que o cita: título da estória (`USnnn – REQUISITO RF-n: <título>`, item 7), matriz de rastreabilidade (Apêndice A) e, quando o nome do caso de uso derivar do RF, item 9 e item 10. Conferido por script. As estórias já têm título no formato verbo + objeto ("Abrir turnaround", "Concluir tarefa"); o ajuste parte desses títulos, e só o título que precisar mudar para entrar no padrão muda também na estória, no caso de uso, no diagrama do item 9 e na matriz. Os itens 4 e 11 não citam título de RF e não mudam.
- [ ] **C00.3** No PDF final, toda tabela com uma coluna de texto muito mais longo que as outras dá a maior largura a essa coluna (itens 6, 7, 8 e 10, Apêndice A e a planilha do item 15).
- [ ] **C00.4** No PDF final, todos os protótipos de tela do item 10 aparecem (42 imagens) e não há nenhum "[imagem não encontrada" no documento.
- [ ] **C00.5** O PR dos ajustes lista cada anotação da tabela acima e a evidência de que foi atendida.

### 3.1 Item 12 — Modelo de Dados (1,0)

**Fontes:** diagrama do **modelo lógico relacional** em **notação UML**, com as entidades que atendem aos RFs e seus relacionamentos. Notação dos slides `ESSW_TE4` (p. 22 a 25): cada tabela é uma caixa com o nome, a região da chave primária (PK), uma coluna que marca PK/FK e os demais campos com o tipo (`Nome: VARCHAR(100)`); campos obrigatórios (sem nulo) em **negrito**; a seta do relacionamento aponta para a tabela que tem a PK; cardinalidade nas duas pontas (`1` / `n`). Mapeamento do modelo conceitual para o relacional pelos 6 passos dos slides (p. 26 a 38) e normalização até a terceira forma normal (p. 46 a 62).

**Rubrica, Excede:** "Diagrama completo e coerente com o domínio, contendo todas as entidades, relacionamentos, cardinalidades e atributos corretamente tipados."

- [ ] **C12.1** A notação é a UML de modelo lógico relacional dos slides: nome da tabela, região da PK, coluna PK/FK e demais campos; campos obrigatórios em negrito.
- [ ] **C12.2** **Todas as entidades:** todo dado que um RF manda cadastrar, registrar, calcular e guardar ou consultar tem tabela e campo no modelo. O texto do item traz a tabela `Tabela | RFs atendidos`, e todo RF que guarda dado aparece nela (conferido por script).
- [ ] **C12.3** **Atributos tipados:** todo campo tem um tipo SQL padrão (seção 6, B1), com tamanho quando o tipo pede (`VARCHAR(n)`, `DECIMAL(p,s)`); horários com data e fuso usam o tipo de data e hora com fuso; nenhum campo sem tipo.
- [ ] **C12.4** **Chaves:** toda tabela tem PK; todo relacionamento tem FK do lado certo (1:N → FK no lado N; 1:1 → FK no lado de participação parcial, passo 3).
- [ ] **C12.5** **Cardinalidades:** todo relacionamento mostra a cardinalidade nas duas pontas, coerente com as regras dos RFs (ex.: um turnaround tem várias tarefas; uma tarefa tem um responsável).
- [ ] **C12.6** **N:N e multivalorados:** relacionamento N:N vira tabela associativa com PK composta pelas duas FKs (passo 5); atributo multivalorado vira tabela própria (passo 6).
- [ ] **C12.7** **Terceira forma normal:** sem grupos repetitivos, sem dependência parcial nem transitiva; valor calculado (atraso, projeção, caminho crítico) só é guardado quando o RF pede o registro histórico dele, e o texto diz qual RF.
- [ ] **C12.8** **Coerente com o domínio e as decisões:** o modelo cobre, com os nomes do `CONTEXT.md`, turnarounds e seus horários do A-CDM (SIBT, SOBT, EIBT, AIBT, ACGT, ASBT, AEGT, ARDT, AOBT, TOBT planejado e vigente, MTTT); tarefas, modelos de tarefas, dependências e serviços sob demanda (ADR-0014); usuários, perfis e equipes (ADR-0010); pontos de confirmação por QR Code (ADR-0007); a permissão de abastecimento com passageiros por companhia (ADR-0005); a tabela de 72 códigos de atraso da ANAC (ADR-0006); alertas, exceções e a auditoria de autor e horário dos registros. Os estados de turnaround e de tarefa usam os valores do `CONTEXT.md`, seção 3.
- [ ] **C12.9** O diagrama é legível na tela (Y.6) e tem fonte editável (Y.7).
- [ ] **C12.10** **Dicionário de dados** (seção 6, B6) no Apêndice B: para cada tabela, cada campo com tipo, obrigatoriedade, chave (PK/FK), domínio ou valores permitidos e descrição; as mesmas tabelas e campos do diagrama (conferido por script).

### 3.2 Item 13 — Diagrama de Classes (1,0)

**Fontes:** diagrama de classes em **UML**, em **nível técnico**, "já considerando a arquitetura de implementação", com elementos de negócio e de implementação. Notação dos slides `ESSW_TE5_1`: atributo `- nome: tipo` e método `+ nome(tipo): retorno` (p. 18 e 19); visibilidade `-` privado, `#` protegido, `+` público (p. 20); membro estático sublinhado (p. 21); relacionamentos de associação, dependência, herança, composição e agregação, com multiplicidade (p. 22 a 31); visão geral com as classes de negócio e visões técnicas mais detalhadas, como `ClienteController` no MVC (p. 32 e 33); na transposição do modelo relacional, a classe referencia **o tipo** da outra classe, nunca só o identificador (p. 37, "NÃO FAÇA ISSO!").

**Rubrica, Excede:** "Diagrama completo e tecnicamente consistente, com classes bem nomeadas, atributos e métodos tipados, relacionamentos corretos e aderência ao modelo conceitual."

- [ ] **C13.1** A notação é UML: classe com compartimentos de nome, atributos e métodos; visibilidade em todo membro; estáticos sublinhados.
- [ ] **C13.2** **Atributos tipados:** todo atributo segue `nome: Tipo`, com tipos UML neutros (seção 6, B1) ou de outra classe ou enumeração do diagrama.
- [ ] **C13.3** **Métodos em nível de implementação:** todo método segue `nome(parametro: Tipo): Retorno`, com parâmetros e retorno tipados (`void` quando não retorna nada).
- [ ] **C13.4** **Nível técnico:** a arquitetura de implementação está declarada no texto do item (seção 6, B2), e o diagrama tem, além das classes de negócio, as classes técnicas dessa arquitetura (por exemplo, as de interface, controle, serviço e acesso a dados de cada função do sistema).
- [ ] **C13.5** **Relacionamentos corretos:** cada relação usa o tipo certo (associação, dependência, herança, composição ou agregação), com multiplicidade nas associações; a referência entre classes é por tipo (`- turnaround: Turnaround`), e não só pelo identificador.
- [ ] **C13.6** **Aderência ao modelo de dados:** toda tabela de negócio do item 12 tem classe correspondente (as tabelas associativas podem virar coleções), com os mesmos nomes de domínio e tipos compatíveis; diferenças intencionais são explicadas no texto.
- [ ] **C13.7** Os estados do turnaround e da tarefa são enumerações com exatamente os valores do `CONTEXT.md`, seção 3; perfis de acesso também.
- [ ] **C13.8** Todo método chamado nos diagramas de sequência (item 14) existe na classe que recebe a mensagem, com o mesmo nome e a mesma assinatura (conferido por script na seção 5, K.4).
- [ ] **C13.9** Classes bem nomeadas: nomes no singular, sem abreviação obscura, seguindo uma só convenção (seção 6, B2).
- [ ] **C13.10** O diagrama é legível na tela, com visão geral das classes de negócio e vistas técnicas por função do sistema (Y.6), e tem fonte editável (Y.7).

### 3.3 Item 14 — Diagramas de Sequência (1,0)

**Fontes:** **um diagrama para cada caso de uso** especificado no item 10 (37: UC01 a UC37), mostrando a "sequência de interação entre as camadas", com a legenda "Diagrama de Sequência do UCnn". Notação dos slides `ESSW_TE5_2` (p. 11 a 20): o ator inicia a sequência; cada objeto tem linha de vida (cabeça com o nome da classe e cauda tracejada) e, opcionalmente, estereótipo de limite (*boundary*, View), controle (*control*, Controller), entidade (*entity*, Model) ou banco de dados; ativações sobre a linha de vida; mensagem de chamada em seta contínua e retorno em seta tracejada; fragmentos `opt`, `alt` e outros com a condição entre colchetes; exemplo em MVC com `PedidoView`, `PizzaController`, `PedidoController` e o banco de dados.

**Rubrica, Excede:** "Todos os casos de uso possuem diagramas de sequência completos, coerentes e alinhados à lógica do sistema, utilizando corretamente objetos, mensagens e interações UML."

- [ ] **C14.1** **Um por caso de uso:** 37 diagramas, UC01 a UC37, cada um com a legenda "Diagrama de Sequência do UCnn – <nome do caso de uso>" e o mesmo nome do item 10 (contagem por script).
- [ ] **C14.2** **Notação UML:** ator que inicia, linhas de vida, ativações, mensagens de chamada contínuas, retornos tracejados e fragmentos com condição de guarda.
- [ ] **C14.3** **Camadas:** os participantes seguem a arquitetura do item 13 (interface, controle, serviço ou modelo, acesso a dados e banco de dados), com o estereótipo correspondente, e as mensagens descem e voltam pelas camadas, sem atalho da interface para o banco.
- [ ] **C14.4** **Completo:** o diagrama cobre o fluxo básico do caso de uso e, em fragmentos `alt`/`opt`, cada fluxo alternativo e cada fluxo de exceção do item 10 (37 básicos, 119 alternativos e 122 de exceção no RA1). Fluxo que não muda a interação (ex.: só volta a um passo) pode ser agrupado, e o texto diz quais foram agrupados.
- [ ] **C14.5** **Mensagens específicas:** cada mensagem é um método com nome e argumentos (`registrarInicio(tarefaId, horario)`), nada genérico como `processar()` ou `executar()`; cada chamada ao banco cita a tabela do item 12.
- [ ] **C14.6** **Coerente com o comportamento descrito:** a ordem das mensagens segue a ordem dos passos do caso de uso; as regras de negócio que o caso de uso verifica aparecem como mensagens ou condições de guarda; o que o RF manda gravar (autor, horário, valor anterior) aparece gravado.
- [ ] **C14.7** **Atores e relacionamentos do item 9:** o ator que inicia é o do caso de uso (inclusive o Motor de Eventos nos casos de uso dele); `«include»` aparece como fragmento `ref` para o caso de uso incluído, e `«extend»` como fragmento `opt` com a condição de extensão.
- [ ] **C14.8** Cada diagrama é legível na tela (Y.6), tem fonte editável (Y.7) e passa na checagem cruzada dos marcos (Y.8): por exemplo, ACGT e AEGT são gravados pelo Motor de Eventos a partir dos registros do Operador de Solo/Rampa (RF-20).

### 3.4 Item 15 — Casos de Teste (1,0)

**Fontes:** **planilha de casos de teste** (PCT) projetada a partir das especificações de caso de uso e que considera **os diferentes cenários dos critérios de aceite** das estórias. Método dos slides `ESSW_TE6` (p. 67 a 82, Heumann, 2001): (1) levantar os fluxos de eventos de cada caso de uso (FP, FA-n, FE-n); (2) definir os cenários de teste como caminhos pelos fluxos; (3) montar a tabela `Cenário | Caso de Teste | Entradas | Resultado Esperado`, com pelo menos um caso de teste por cenário e valores concretos de entrada (ex.: "Senha atual = válida; Nova senha e Confirmação = a1b2c3").

**Rubrica, Excede:** "Planilha completa e bem estruturada, contendo cenários diversos, dados de entrada, passos, resultados esperados e clara relação com os critérios de aceite."

- [ ] **C15.1** **Estrutura:** a planilha tem as colunas `ID` (CT-nnn), `Caso de uso`, `Cenário` (fluxos percorridos, ex.: FP1–FP3 / A1.1–A1.3), `Estória e critério de aceite` (ex.: US015-CA2), `Caso de teste` (título), `Pré-condições`, `Dados de entrada`, `Passos` e `Resultado esperado`.
- [ ] **C15.2** **Relação com os critérios de aceite:** todo critério de aceite das 44 estórias (179 no RA1) é coberto por pelo menos um caso de teste, e todo caso de teste aponta para um critério existente (conferido por script).
- [ ] **C15.3** **Cenários diversos:** para cada um dos 37 casos de uso, o fluxo básico, cada fluxo alternativo e cada fluxo de exceção têm pelo menos um cenário com caso de teste.
- [ ] **C15.4** **Dados de entrada concretos:** valores de verdade (horários com data e fuso, identificadores, quantidades, códigos de atraso da ANAC), e não "dados válidos"; valores-limite onde a regra tem limite (ex.: TOBT + 5 min, 5 s, antecipação de 5 min; ADR-0001 e ADR-0003).
- [ ] **C15.5** **Passos:** cada caso de teste tem passos numerados, executáveis por quem não escreveu o caso.
- [ ] **C15.6** **Resultado esperado observável:** mensagem exibida, estado resultante, registro gravado ou alerta emitido, coerente com o "ENTÃO" do critério de aceite e com o caso de uso.
- [ ] **C15.7** **Consistência:** nenhum caso de teste contradiz o RF, a estória ou o caso de uso de origem, nem as decisões D1–D14.
- [ ] **C15.8** A planilha é legível no PDF (colunas de texto longo priorizadas, cabeçalho repetido em cada página, agrupada por caso de uso) e é gerada da fonte Markdown do item 15 (Y.7).

---

## 4. Dependências e ordem de execução

```
Ajustes do RA1 (3.0) ── primeira tarefa; entra na main antes de todo o resto
      │
      ▼
Decisões B1 a B3 (seção 6)
      │
      └──► Item 12 (modelo de dados)
                 │
                 └──► Item 13 (classes: negócio a partir do 12 + classes técnicas da arquitetura)
                            │
                            └──► Item 14 (sequência, 1 por caso de uso) ◄──► ajuste de métodos no 13
Itens 7 e 10 (RA1) ──► Item 15 (casos de teste) ── pode começar já; não depende dos itens 12 a 14
      │
      └──► Consolidação: revisão cruzada (seção 5), matriz, PDF e envio
```

- **Integração (rdsalvesPUC, com revisão de todos):** ajuste ARO e itens 12 e 13, por serem um modelo único do sistema, como os itens 9 e 11 no RA1.
- **Por área:** itens 14 e 15. Cada integrante faz os diagramas de sequência dos casos de uso da sua área e os casos de teste das estórias e casos de uso da sua área, o que mantém a rastreabilidade RF → estória → caso de uso → sequência → teste na mesma pessoa.

| Área | Casos de uso (item 14) | Estórias e critérios (item 15) |
|---|---|---|
| A — acesso e planejamento | 13 (UC01 a UC13) | 13 estórias, 60 critérios |
| B — execução em solo | 8 (UC14 a UC21) | 8 estórias, 32 critérios |
| C — monitoramento | 7 (UC22 a UC28) | 14 estórias, 52 critérios |
| D — exceções e liberação | 9 (UC29 a UC37) | 9 estórias, 35 critérios |
| **Total** | **37** | **44 estórias, 179 critérios** |

- **Janela de tempo:** de 28/10 a 28/11. Pelo plano de ensino, as aulas de 29/10 (classes), 05/11 (sequência) e 12/11 e 19/11 (casos de teste) são de prática desses itens; 21/11 é o TDE3; a entrega é sábado, 28/11, às 23:59.

---

## 5. Checklist final de consistência cruzada

Executar depois que todos os itens estiverem prontos, e de novo antes do envio.

- [ ] **K.1** Os mesmos atores (nomes idênticos) aparecem nos itens 4, 5, 6, 7, 9, 10 e 11 e nos diagramas de sequência (item 14).
- [ ] **K.2** Todo caso de uso do item 10 tem **exatamente um** diagrama de sequência, e todo diagrama aponta para um caso de uso existente, com o mesmo nome.
- [ ] **K.3** Toda tabela de negócio do item 12 tem classe no item 13 e é usada por pelo menos um RF; toda classe de negócio do item 13 tem tabela no item 12 ou o texto explica por que não tem.
- [ ] **K.4** Toda mensagem dos diagramas de sequência existe como método na classe que a recebe (item 13), com a mesma assinatura; toda chamada ao banco cita uma tabela do item 12.
- [ ] **K.5** Todo critério de aceite (item 7) é coberto por pelo menos um caso de teste (item 15), e todo fluxo de cada caso de uso (item 10) tem cenário de teste.
- [ ] **K.6** Os estados (turnaround e tarefa) têm os mesmos valores no `CONTEXT.md`, no item 12 (domínio do campo), no item 13 (enumerações), no item 14 (condições de guarda) e no item 15 (resultados esperados).
- [ ] **K.7** O título ARO de cada RF é idêntico nos itens 6 e 7 e no Apêndice A (C00.2).
- [ ] **K.8** As contagens conferem por contagem real: 44 títulos ARO, 37 diagramas de sequência, 179 critérios de aceite cobertos, fluxos de 37 casos de uso cobertos.
- [ ] **K.9** Os critérios gerais Y.1 a Y.8 estão atendidos, e a checagem do RA1 continua passando (`scripts/verificar_revisao.py`, `scripts/marcos_nos_diagramas.py`).
- [ ] **K.10** Nenhum item contradiz o `CONTEXT.md` nem as decisões D1–D14 (`docs/adr/`) e as que forem criadas para o RA2; todo número ou sigla do setor cita a fonte (`pesquisa/fontes.md`).
- [ ] **K.11** Não há issue aberta com o rótulo `pendencia-cruzada`: toda suposição de um item sobre outro foi resolvida com o ID do requisito ou com a decisão do grupo registrada.
- [ ] **K.12** A matriz de rastreabilidade (Apêndice A) foi gerada de novo depois de todas as mudanças, com `scripts/gerar_matriz_rastreabilidade.py`, e a seção "Lacunas encontradas" diz "Nenhuma." (ADR-0012), já com as colunas dos itens 12 a 15 (seção 6, B5).

---

## 6. Decisões do RA2

Respostas de rdsalvesPUC em 28/10. Cada decisão fechada vira ADR na tarefa correspondente.

| | Decisão | Situação |
|---|---|---|
| B1 | **Tipos sem SGBD nem linguagem específica.** A tarefa não pede um SGBD; o que ela pede são campos tipados (item 12) e atributos e métodos tipados (item 13). Proposta: item 12 com tipos SQL padrão (`INTEGER`, `VARCHAR(n)`, `DECIMAL(p,s)`, `BOOLEAN`, `TIMESTAMP WITH TIME ZONE` para os horários com data e fuso), como nos slides; item 13 com tipos UML neutros (`String`, `Integer`, `Boolean`, `DateTime`) e as classes e enumerações do próprio diagrama. | Proposta; confirmar |
| B2 | **Arquitetura de implementação e convenção de nomes.** O item 13 declara a arquitetura (C13.4), e o item 14 mostra as mensagens entre as camadas dela (C14.3). Falta decidir as camadas, onde fica o Motor de Eventos e a convenção de nomes de classes, tabelas e campos. | Em aberto; conversa dedicada antes do item 13 |
| B3 | **Ferramenta dos diagramas de sequência.** Testar primeiro Mermaid e PlantUML em um caso de uso e comparar o resultado no PDF; se ficarem ruins, usar o draw.io. | Decidido; teste antes do item 14 |
| B4 | **Planilha do item 15 só no PDF**, sem arquivo `.xlsx` ou `.csv`. | Decidido |
| B5 | **Matriz estendida:** o Apêndice A ganha as colunas dos itens 12 a 15 (RF → tabelas; caso de uso → diagrama de sequência; critério de aceite → casos de teste). Pede atualização da ADR-0012 e do script. | Decidido |
| B6 | **Dicionário de dados como apêndice** (Apêndice B, C12.10). | Decidido |
| B7 | **Divisão:** ajuste ARO e itens 12 e 13 com rdsalvesPUC; itens 14 e 15 por área (seção 4). | Decidido |
