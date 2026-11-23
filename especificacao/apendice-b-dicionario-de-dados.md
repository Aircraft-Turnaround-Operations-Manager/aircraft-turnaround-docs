# APÊNDICE B — DICIONÁRIO DE DADOS

<!-- Apêndice B (decisão B6, critério C12.10), escrito na tarefa T12 (issue #144). Para cada tabela do item 12, uma
tabela com cada campo: tipo, obrigatoriedade, chave (PK/FK), domínio ou valores permitidos e descrição. É a fonte dos
diagramas do item 12: scripts/gerar_modelo_de_dados.py lê este arquivo, gera os diagramas e confere que as tabelas e os
campos são os mesmos nos diagramas, aqui e na tabela "Serviço | Tabela | RFs atendidos" do item 12. Formato lido pelo
script: "## B.n <serviço>", "### B.n.m `tabela`" (com " (técnica)" nas tabelas técnicas) e a tabela de campos logo
abaixo. O gerador o põe depois do Apêndice A. -->

Este apêndice descreve cada tabela do modelo de dados do item 12, serviço a serviço, na mesma ordem e com os mesmos campos dos diagramas. As tabelas de negócio vêm primeiro; as técnicas, iguais nos quatro serviços, vêm no fim de cada serviço.

**Siglas.** Os horários seguem a tomada de decisão colaborativa em aeroportos (A-CDM): horário programado de chegada à posição (SIBT), horário programado de saída da posição (SOBT), horário estimado de chegada à posição (EIBT), horário real de chegada à posição (AIBT), início real do atendimento em solo (ACGT), início real do embarque (ASBT), fim real do atendimento em solo (AEGT), horário real de prontidão (ARDT), horário real de saída da posição (AOBT), horário-alvo de prontidão (TOBT) e tempo mínimo de turnaround (MTTT). As demais: requisito funcional (RF), requisito não funcional (RNF), caso de uso (UC), registro de decisão de arquitetura (ADR), Agência Nacional de Aviação Civil (ANAC), código de resposta rápida (QR Code), chave primária (PK), chave estrangeira (FK), identificador universal único (UUID), tempo universal coordenado (UTC), notação de objetos JavaScript (JSON) e objeto grande de caracteres (CLOB).

**Como ler.**

- **Tipo:** tipo SQL padrão; o banco de cada serviço o traduz para o seu (item 12, seção 12.1).
- **Chave:** PK, FK ou as duas. Um campo que guarda o identificador de outro serviço não é FK: o domínio diz qual tabela e qual serviço são os donos do dado (ADR-0015).
- **Obrigatório:** "Sim" quando o campo não aceita vazio; nos diagramas, esses campos estão em negrito.
- **Domínio ou valores:** a lista fechada de valores, escrita com a grafia exata que todos os itens usam, ou o tipo de conteúdo. Os estados seguem o `CONTEXT.md`, seção 3.
- **Restrições:** unicidades (UNIQUE), checagens (CHECK) e regras que a aplicação confere.

## B.1 Cadastro e Planejamento

### B.1.1 `equipe`

Equipe ou especialidade (RF-9; ADR-0010). RFs: RF-2, RF-4, RF-5, RF-9, RF-43.

| Campo | Tipo | Chave | Obrigatório | Domínio ou valores | Descrição |
|---|---|---|---|---|---|
| `id` | `CHAR(36)` | PK | Sim | UUID | — |
| `codigo` | `VARCHAR(20)` | — | Sim | Texto | Identificador único (ex.: LIMP) |
| `nome` | `VARCHAR(100)` | — | Sim | Texto | — |
| `ativa` | `BOOLEAN` | — | Sim | Sim ou não | Desativada não aceita novos vínculos |

**Restrições:**

- UNIQUE (codigo)

### B.1.2 `companhia`

Companhia aérea; carga inicial, sem RF de manutenção. RFs: RF-3, RF-11.

| Campo | Tipo | Chave | Obrigatório | Domínio ou valores | Descrição |
|---|---|---|---|---|---|
| `id` | `CHAR(36)` | PK | Sim | UUID | — |
| `nome` | `VARCHAR(100)` | — | Sim | Texto | — |

**Restrições:**

- UNIQUE (nome)

### B.1.3 `usuario`

Usuário e perfil (RF-1, RF-2; ADR-0010); único serviço com dado pessoal (RNF-6). RFs: RF-1, RF-2, RF-5, RF-37, RF-42, RF-43.

| Campo | Tipo | Chave | Obrigatório | Domínio ou valores | Descrição |
|---|---|---|---|---|---|
| `id` | `CHAR(36)` | PK | Sim | UUID | Também é o identificador histórico depois da anonimização |
| `identificador_acesso` | `VARCHAR(50)` | — | Sim | Texto | Único; trocado por valor sem dado pessoal na anonimização |
| `nome` | `VARCHAR(100)` | — | Sim | Texto | Trocado por valor sem dado pessoal na anonimização |
| `senha_hash` | `VARCHAR(255)` | — | Não | Texto | Função própria para senhas, com sal (RNF-3); vazia só depois da anonimização |
| `perfil` | `VARCHAR(30)` | — | Sim | Operador de Solo/Rampa, Coordenador de Turnaround, Autoridade de Liberação, Administrador do Sistema | — |
| `equipe_id` | `CHAR(36)` | FK | Não | Identificador de `equipe` | Obrigatória para o Operador de Solo/Rampa |
| `companhia_id` | `CHAR(36)` | FK | Não | Identificador de `companhia` | Obrigatória para a Autoridade de Liberação (UC32) |
| `desativado_em` | `TIMESTAMP WITH TIME ZONE` | — | Não | Data, hora e fuso | Vazio = ativo (RF-2); início do prazo do RNF-6 |
| `bloqueado_ate` | `TIMESTAMP WITH TIME ZONE` | — | Não | Data, hora e fuso | Bloqueio de 15 min após 5 falhas (RNF-5) |
| `anonimizado_em` | `TIMESTAMP WITH TIME ZONE` | — | Não | Data, hora e fuso | Rotina do RNF-6 |

**Restrições:**

- UNIQUE (identificador_acesso)
- CHECK: Operador de Solo/Rampa exige equipe_id
- CHECK: Autoridade de Liberação exige companhia_id
- CHECK: senha_hash vazia só com anonimizado_em preenchido

### B.1.4 `falha_login`

Falhas de autenticação para o bloqueio do RNF-5 (janela de 15 min). RFs: RF-1.

| Campo | Tipo | Chave | Obrigatório | Domínio ou valores | Descrição |
|---|---|---|---|---|---|
| `id` | `CHAR(36)` | PK | Sim | UUID | — |
| `usuario_id` | `CHAR(36)` | FK | Sim | Identificador de `usuario` | — |
| `ocorrida_em` | `TIMESTAMP WITH TIME ZONE` | — | Sim | Data, hora e fuso | Apagadas na autenticação válida |

### B.1.5 `sessao`

Sessão aberta pelo login; 45 min sem ação a encerram (RNF-5). RFs: RF-1.

| Campo | Tipo | Chave | Obrigatório | Domínio ou valores | Descrição |
|---|---|---|---|---|---|
| `id` | `CHAR(36)` | PK | Sim | UUID | Referência levada no token, sem guardar o token |
| `usuario_id` | `CHAR(36)` | FK | Sim | Identificador de `usuario` | — |
| `iniciada_em` | `TIMESTAMP WITH TIME ZONE` | — | Sim | Data, hora e fuso | — |
| `ultima_acao_em` | `TIMESTAMP WITH TIME ZONE` | — | Sim | Data, hora e fuso | Só ação do usuário renova |
| `encerrada_em` | `TIMESTAMP WITH TIME ZONE` | — | Não | Data, hora e fuso | — |

### B.1.6 `politica_abastecimento`

Versões da permissão de abastecimento com passageiros por companhia (RF-11; ADR-0005); sem versão = Não permitido. RFs: RF-5, RF-6, RF-11, RF-42.

| Campo | Tipo | Chave | Obrigatório | Domínio ou valores | Descrição |
|---|---|---|---|---|---|
| `id` | `CHAR(36)` | PK | Sim | UUID | — |
| `companhia_id` | `CHAR(36)` | FK | Sim | Identificador de `companhia` | — |
| `versao` | `INTEGER` | — | Sim | Inteiro | Cada mudança cria versão nova |
| `permite_com_passageiros` | `BOOLEAN` | — | Sim | Sim ou não | — |
| `registrada_em` | `TIMESTAMP WITH TIME ZONE` | — | Sim | Data, hora e fuso | Vale para os planos criados depois |
| `autor_id` | `CHAR(36)` | FK | Sim | Identificador de `usuario` | — |

**Restrições:**

- UNIQUE (companhia_id, versao)

### B.1.7 `modelo_tarefa`

Modelo de tarefas por tipo de aeronave e serviço (RF-4). RFs: RF-4, RF-6.

| Campo | Tipo | Chave | Obrigatório | Domínio ou valores | Descrição |
|---|---|---|---|---|---|
| `id` | `CHAR(36)` | PK | Sim | UUID | — |
| `nome` | `VARCHAR(60)` | — | Sim | Texto | Ex.: MOD-A320-PAX |
| `tipo_aeronave` | `VARCHAR(10)` | — | Sim | Texto | Ex.: A320 |
| `tipo_servico` | `VARCHAR(60)` | — | Sim | Texto | Ex.: Doméstico com passageiros |
| `com_passageiros` | `BOOLEAN` | — | Sim | Sim ou não | Exige exatamente uma tarefa do tipo Embarque (RF-4) |

### B.1.8 `tarefa_modelo`

Tarefa do modelo, inclusive o catálogo sob demanda (RF-4; ADR-0014). RFs: RF-4, RF-6, RF-7, RF-8.

| Campo | Tipo | Chave | Obrigatório | Domínio ou valores | Descrição |
|---|---|---|---|---|---|
| `id` | `CHAR(36)` | PK | Sim | UUID | — |
| `modelo_id` | `CHAR(36)` | FK | Sim | Identificador de `modelo_tarefa` | — |
| `nome` | `VARCHAR(60)` | — | Sim | Texto | — |
| `tipo_atividade` | `VARCHAR(20)` | — | Sim | Embarque, Desembarque, Abastecimento, Limpeza, Catering, Descarga, Degelo… | — |
| `equipe_id` | `CHAR(36)` | FK | Sim | Identificador de `equipe` | Equipe ativa |
| `duracao_planejada_min` | `INTEGER` | — | Sim | Minutos | Maior que zero |
| `obrigatoria` | `BOOLEAN` | — | Sim | Sim ou não | — |
| `permite_nao_aplicavel` | `BOOLEAN` | — | Sim | Sim ou não | — |
| `sob_demanda` | `BOOLEAN` | — | Sim | Sim ou não | Faz parte do catálogo |

**Restrições:**

- CHECK (duracao_planejada_min > 0)

### B.1.9 `dependencia_tarefa_modelo`

Predecessora e sucessora no modelo, N:N (RF-8). RFs: RF-4, RF-8.

| Campo | Tipo | Chave | Obrigatório | Domínio ou valores | Descrição |
|---|---|---|---|---|---|
| `predecessora_id` | `CHAR(36)` | PK, FK | Sim | Identificador de `tarefa_modelo` | — |
| `sucessora_id` | `CHAR(36)` | PK, FK | Sim | Identificador de `tarefa_modelo` | — |

**Restrições:**

- CHECK (predecessora_id <> sucessora_id)
- Regra: as duas do mesmo modelo; sem ciclos (aplicação)

### B.1.10 `ponto_confirmacao_modelo`

Ponto de QR Code da tarefa do modelo (RF-7; ADR-0007). RFs: RF-7.

| Campo | Tipo | Chave | Obrigatório | Domínio ou valores | Descrição |
|---|---|---|---|---|---|
| `id` | `CHAR(36)` | PK | Sim | UUID | — |
| `tarefa_modelo_id` | `CHAR(36)` | FK | Sim | Identificador de `tarefa_modelo` | — |
| `identificador` | `VARCHAR(30)` | — | Sim | Texto | — |
| `nome` | `VARCHAR(60)` | — | Sim | Texto | — |

**Restrições:**

- UNIQUE (tarefa_modelo_id, identificador)
- UNIQUE (tarefa_modelo_id, nome)

### B.1.11 `turnaround`

Cadastro do turnaround e horários de referência (RF-3, RF-10); o UUID nasce aqui. RFs: RF-3, RF-6, RF-10.

| Campo | Tipo | Chave | Obrigatório | Domínio ou valores | Descrição |
|---|---|---|---|---|---|
| `id` | `CHAR(36)` | PK | Sim | UUID | Mesmo identificador nos quatro serviços |
| `companhia_id` | `CHAR(36)` | FK | Sim | Identificador de `companhia` | — |
| `voo_chegada` | `VARCHAR(10)` | — | Sim | Texto | — |
| `data_voo_chegada` | `DATE` | — | Sim | Data | Data local da programação |
| `voo_partida` | `VARCHAR(10)` | — | Sim | Texto | — |
| `data_voo_partida` | `DATE` | — | Sim | Data | Data local da programação |
| `tipo_aeronave` | `VARCHAR(10)` | — | Sim | Texto | — |
| `matricula` | `VARCHAR(10)` | — | Sim | Texto | — |
| `tipo_servico` | `VARCHAR(60)` | — | Sim | Texto | Compatibilidade do modelo (RF-6) |
| `posicao` | `VARCHAR(10)` | — | Sim | Texto | — |
| `sibt` | `TIMESTAMP WITH TIME ZONE` | — | Sim | Data, hora e fuso | SIBT |
| `sobt` | `TIMESTAMP WITH TIME ZONE` | — | Sim | Data, hora e fuso | SOBT |
| `eibt` | `TIMESTAMP WITH TIME ZONE` | — | Sim | Data, hora e fuso | EIBT |
| `tobt_planejado` | `TIMESTAMP WITH TIME ZONE` | — | Sim | Data, hora e fuso | TOBT planejado, fixo; o vigente é do Exceções e Liberação |
| `mttt_min` | `INTEGER` | — | Sim | Minutos | MTTT em minutos, maior que zero |
| `criado_por_id` | `CHAR(36)` | FK | Sim | Identificador de `usuario` | — |
| `criado_em` | `TIMESTAMP WITH TIME ZONE` | — | Sim | Data, hora e fuso | — |
| `aobt` | `TIMESTAMP WITH TIME ZONE` | — | Não | Data, hora e fuso | Cópia por aviso da Execução em Solo; só para o prazo do RNF-6 |

**Restrições:**

- UNIQUE (voo_chegada, data_voo_chegada, voo_partida, data_voo_partida)
- CHECK (mttt_min > 0)

### B.1.12 `plano`

Plano inicial do turnaround, 1:1 (RF-5, RF-6); nasce ao aplicar o modelo. RFs: RF-5, RF-6, RF-11.

| Campo | Tipo | Chave | Obrigatório | Domínio ou valores | Descrição |
|---|---|---|---|---|---|
| `id` | `CHAR(36)` | PK | Sim | UUID | Ex.: P-1 |
| `turnaround_id` | `CHAR(36)` | FK | Sim | Identificador de `turnaround` | Único |
| `modelo_id` | `CHAR(36)` | FK | Sim | Identificador de `modelo_tarefa` | Modelo aplicado |
| `politica_id` | `CHAR(36)` | FK | Não | Identificador de `politica_abastecimento` | Versão copiada ao aplicar o modelo; vazio = Não permitido |
| `confirmado_em` | `TIMESTAMP WITH TIME ZONE` | — | Não | Data, hora e fuso | Vazio = cópia ainda não confirmada |
| `confirmado_por_id` | `CHAR(36)` | FK | Não | Identificador de `usuario` | — |

**Restrições:**

- UNIQUE (turnaround_id)
- CHECK: confirmado_em e confirmado_por_id juntos

### B.1.13 `tarefa_plano`

Tarefa do plano inicial e do catálogo copiado (RF-5, RF-6); o UUID da tarefa nasce aqui. RFs: RF-2, RF-5, RF-6, RF-9.

| Campo | Tipo | Chave | Obrigatório | Domínio ou valores | Descrição |
|---|---|---|---|---|---|
| `id` | `CHAR(36)` | PK | Sim | UUID | Mesmo identificador da tarefa na Execução em Solo |
| `plano_id` | `CHAR(36)` | FK | Sim | Identificador de `plano` | — |
| `tarefa_modelo_id` | `CHAR(36)` | FK | Sim | Identificador de `tarefa_modelo` | Origem da cópia |
| `nome` | `VARCHAR(60)` | — | Sim | Texto | — |
| `tipo_atividade` | `VARCHAR(20)` | — | Sim | Texto | — |
| `equipe_id` | `CHAR(36)` | FK | Sim | Identificador de `equipe` | — |
| `responsavel_id` | `CHAR(36)` | FK | Não | Identificador de `usuario` | Responsável no plano inicial; o atual é da Execução em Solo |
| `duracao_planejada_min` | `INTEGER` | — | Sim | Minutos | — |
| `inicio_planejado` | `TIMESTAMP WITH TIME ZONE` | — | Não | Data, hora e fuso | — |
| `fim_planejado` | `TIMESTAMP WITH TIME ZONE` | — | Não | Data, hora e fuso | — |
| `obrigatoria` | `BOOLEAN` | — | Sim | Sim ou não | — |
| `permite_nao_aplicavel` | `BOOLEAN` | — | Sim | Sim ou não | — |
| `sob_demanda` | `BOOLEAN` | — | Sim | Sim ou não | — |
| `acionada` | `BOOLEAN` | — | Sim | Sim ou não | Serviço sob demanda já conhecido, incluído no plano (RF-5) |

**Restrições:**

- CHECK (sob_demanda OR NOT acionada)
- CHECK (fim_planejado > inicio_planejado)
- Regra: na confirmação, toda tarefa do plano (regular ou acionada) tem responsável, início e fim

### B.1.14 `dependencia_tarefa_plano`

Dependências do plano inicial, N:N (RF-5, RF-8). RFs: RF-5, RF-8.

| Campo | Tipo | Chave | Obrigatório | Domínio ou valores | Descrição |
|---|---|---|---|---|---|
| `predecessora_id` | `CHAR(36)` | PK, FK | Sim | Identificador de `tarefa_plano` | — |
| `sucessora_id` | `CHAR(36)` | PK, FK | Sim | Identificador de `tarefa_plano` | — |

**Restrições:**

- CHECK (predecessora_id <> sucessora_id)
- Regra: predecessora do catálogo não acionada não segura a sucessora

### B.1.15 `ponto_confirmacao_plano`

Pontos copiados para o plano (RF-6, RF-7). RFs: RF-6, RF-7.

| Campo | Tipo | Chave | Obrigatório | Domínio ou valores | Descrição |
|---|---|---|---|---|---|
| `id` | `CHAR(36)` | PK | Sim | UUID | Mesmo identificador na Execução em Solo |
| `tarefa_plano_id` | `CHAR(36)` | FK | Sim | Identificador de `tarefa_plano` | — |
| `identificador` | `VARCHAR(30)` | — | Sim | Texto | — |
| `nome` | `VARCHAR(60)` | — | Sim | Texto | — |

**Restrições:**

- UNIQUE (tarefa_plano_id, identificador)
- UNIQUE (tarefa_plano_id, nome)

### B.1.16 `registro_auditoria` (técnica)

Trilha de auditoria do serviço (RNF-2, RNF-6); sem FK, para sobreviver à anonimização.

| Campo | Tipo | Chave | Obrigatório | Domínio ou valores | Descrição |
|---|---|---|---|---|---|
| `id` | `CHAR(36)` | PK | Sim | UUID | Identificador do registro |
| `objeto` | `VARCHAR(40)` | — | Sim | Texto | Tabela alterada |
| `objeto_id` | `VARCHAR(80)` | — | Sim | Texto | Chave da linha; chave composta escrita como a|b |
| `acao` | `VARCHAR(30)` | — | Sim | Inclusão, Alteração, Exclusão, Desativação, Anonimização | — |
| `autor_tipo` | `VARCHAR(20)` | — | Sim | Texto | Usuário ou Motor de Eventos |
| `autor_id` | `CHAR(36)` | — | Não | Identificador de `usuario` (Cadastro e Planejamento), sem FK | Obrigatório quando o autor é Usuário |
| `causa_id` | `CHAR(36)` | — | Não | UUID | Registro ou aviso que causou a ação automática |
| `gatilho` | `VARCHAR(60)` | — | Não | Texto | Gatilho por horário sem registro (recálculo de minuto, TOBT − X, TOBT + 5, TOBT − 15) |
| `turnaround_id` | `CHAR(36)` | — | Não | Identificador de `turnaround` (Cadastro e Planejamento), sem FK | Turnaround relacionado; vazio = prazo do RNF-6 conta do próprio registro |
| `ocorrido_em` | `TIMESTAMP WITH TIME ZONE` | — | Sim | Data, hora e fuso | Data e hora da ação |
| `valores_anteriores` | `CLOB` | — | Não | Texto JSON | Valores antes da mudança, em JSON |
| `valores_novos` | `CLOB` | — | Não | Texto JSON | Valores depois da mudança, em JSON |
| `anonimizado_em` | `TIMESTAMP WITH TIME ZONE` | — | Não | Data, hora e fuso | Rotina do RNF-6 |

**Restrições:**

- CHECK: autor_tipo = Usuário exige autor_id; Motor de Eventos exige causa_id ou gatilho

### B.1.17 `aviso_saida` (técnica)

Avisos a publicar, gravados na mesma transação da mudança (ADR-0016); origem = nome do serviço, constante.

| Campo | Tipo | Chave | Obrigatório | Domínio ou valores | Descrição |
|---|---|---|---|---|---|
| `id` | `CHAR(36)` | PK | Sim | UUID | id do envelope |
| `tipo` | `VARCHAR(60)` | — | Sim | Texto | Nome do aviso, em PascalCase, no passado |
| `versao` | `INTEGER` | — | Sim | Inteiro | Versão do formato |
| `ocorrido_em` | `TIMESTAMP WITH TIME ZONE` | — | Sim | Data, hora e fuso | Quando o fato aconteceu |
| `turnaround_id` | `CHAR(36)` | — | Não | Identificador de `turnaround` (Cadastro e Planejamento), sem FK | Turnaround do fato |
| `autor_id` | `CHAR(36)` | — | Não | Identificador de `usuario` (Cadastro e Planejamento), sem FK | Autor do fato |
| `causa_id` | `CHAR(36)` | — | Não | UUID | Registro que causou o aviso |
| `dados` | `CLOB` | — | Sim | Texto JSON | Conteúdo do aviso em JSON |
| `gravado_em` | `TIMESTAMP WITH TIME ZONE` | — | Sim | Data, hora e fuso | Ordem de publicação |
| `publicado_em` | `TIMESTAMP WITH TIME ZONE` | — | Não | Data, hora e fuso | Vazio até a mensageria confirmar |

### B.1.18 `aviso_processado` (técnica)

Avisos já recebidos, para descartar o repetido (ADR-0016).

| Campo | Tipo | Chave | Obrigatório | Domínio ou valores | Descrição |
|---|---|---|---|---|---|
| `aviso_id` | `CHAR(36)` | PK | Sim | UUID | id do envelope recebido |
| `processado_em` | `TIMESTAMP WITH TIME ZONE` | — | Sim | Data, hora e fuso | Quando foi processado |


## B.2 Execução em Solo

### B.2.1 `turnaround`

Turnaround em atendimento: dono do estado (ADR-0015). RFs: RF-12, RF-14, RF-21, RF-36, RF-39, RF-40, RF-42, RF-44.

| Campo | Tipo | Chave | Obrigatório | Domínio ou valores | Descrição |
|---|---|---|---|---|---|
| `id` | `CHAR(36)` | PK | Sim | Identificador de `turnaround` (Cadastro e Planejamento), sem FK | Identificador do Cadastro |
| `plano_id` | `CHAR(36)` | — | Sim | Identificador de `plano` (Cadastro e Planejamento), sem FK | Plano recebido (ADR-0015, regra 5) |
| `voo_chegada` | `VARCHAR(10)` | — | Sim | Texto | Cópia para exibir (UC12) |
| `voo_partida` | `VARCHAR(10)` | — | Sim | Texto | Cópia para exibir |
| `matricula` | `VARCHAR(10)` | — | Sim | Texto | Cópia para exibir (RF-14) |
| `posicao` | `VARCHAR(10)` | — | Sim | Texto | Cópia para exibir |
| `estado` | `VARCHAR(30)` | — | Não | Em solo, Operações em andamento, Em exceção, Pronto para liberação, Liberado, Fora de bloco | Vazio até o AIBT |
| `permite_com_passageiros` | `BOOLEAN` | — | Sim | Sim ou não | Política recebida com o plano; trava do RF-42 (regra 5) |
| `plano_recebido_em` | `TIMESTAMP WITH TIME ZONE` | — | Sim | Data, hora e fuso | — |
| `tobt_vigente` | `TIMESTAMP WITH TIME ZONE` | — | Não | Data, hora e fuso | Cópia do Exceções e Liberação, só para exibir (UC37) |
| `ardt` | `TIMESTAMP WITH TIME ZONE` | — | Não | Data, hora e fuso | Cópia recebida na resposta da liberação, só para exibir |
| `liberado_por_id` | `CHAR(36)` | — | Não | Identificador de `usuario` (Cadastro e Planejamento), sem FK | Cópia, só para exibir (UC37) |

### B.2.2 `marco`

Marcos do A-CDM gravados pela Execução em Solo (RF-12, RF-20, RF-44). RFs: RF-12, RF-13, RF-20, RF-44.

| Campo | Tipo | Chave | Obrigatório | Domínio ou valores | Descrição |
|---|---|---|---|---|---|
| `id` | `CHAR(36)` | PK | Sim | UUID | — |
| `turnaround_id` | `CHAR(36)` | FK | Sim | Identificador de `turnaround` | — |
| `tipo` | `VARCHAR(4)` | — | Sim | AIBT, ACGT, ASBT, AEGT, AOBT | — |
| `horario` | `TIMESTAMP WITH TIME ZONE` | — | Sim | Data, hora e fuso | Horário do marco; a correção do AIBT o substitui (RF-13) |
| `registrado_em` | `TIMESTAMP WITH TIME ZONE` | — | Sim | Data, hora e fuso | Horário do registro (RF-12) |
| `autor_id` | `CHAR(36)` | — | Não | Identificador de `usuario` (Cadastro e Planejamento), sem FK | AIBT e AOBT: Operador de Solo/Rampa que registrou |
| `registro_origem_id` | `CHAR(36)` | FK | Não | Identificador de `registro_tarefa` | ACGT, ASBT e AEGT: registro que gerou o marco (RF-20) |

**Restrições:**

- UNIQUE (turnaround_id, tipo); o início sem conexão com horário anterior troca o ACGT, e um AEGT novo substitui o anterior (RF-20)
- CHECK: AIBT e AOBT com autor_id; ACGT, ASBT e AEGT com registro_origem_id

### B.2.3 `correcao_aibt`

Correções do AIBT (RF-13; ADR-0013). RFs: RF-13.

| Campo | Tipo | Chave | Obrigatório | Domínio ou valores | Descrição |
|---|---|---|---|---|---|
| `id` | `CHAR(36)` | PK | Sim | UUID | — |
| `turnaround_id` | `CHAR(36)` | FK | Sim | Identificador de `turnaround` | — |
| `aibt_anterior` | `TIMESTAMP WITH TIME ZONE` | — | Sim | Data, hora e fuso | — |
| `aibt_novo` | `TIMESTAMP WITH TIME ZONE` | — | Sim | Data, hora e fuso | Não futuro |
| `motivo` | `VARCHAR(500)` | — | Sim | Texto | — |
| `autor_id` | `CHAR(36)` | — | Sim | Identificador de `usuario` (Cadastro e Planejamento), sem FK | — |
| `corrigido_em` | `TIMESTAMP WITH TIME ZONE` | — | Sim | Data, hora e fuso | — |
| `requisicao_id` | `CHAR(36)` | — | Sim | UUID | Chave de envio (UC13 RN4) |

**Restrições:**

- UNIQUE (requisicao_id)

### B.2.4 `tarefa`

Tarefa do turnaround em andamento: dona do estado e do responsável (ADR-0015); inclui o catálogo sob demanda. RFs: RF-2, RF-9, RF-14, RF-15, RF-16, RF-17, RF-18, RF-19, RF-21, RF-37, RF-39, RF-42, RF-43.

| Campo | Tipo | Chave | Obrigatório | Domínio ou valores | Descrição |
|---|---|---|---|---|---|
| `id` | `CHAR(36)` | PK | Sim | Identificador de `tarefa_plano` (Cadastro e Planejamento), sem FK | Identificador gerado no plano (ADR-0016, ponto 7) |
| `turnaround_id` | `CHAR(36)` | FK | Sim | Identificador de `turnaround` | — |
| `nome` | `VARCHAR(60)` | — | Sim | Texto | — |
| `tipo_atividade` | `VARCHAR(20)` | — | Sim | Texto | — |
| `equipe_id` | `CHAR(36)` | — | Sim | Identificador de `equipe` (Cadastro e Planejamento), sem FK | — |
| `responsavel_id` | `CHAR(36)` | — | Não | Identificador de `usuario` (Cadastro e Planejamento), sem FK | Atual; muda na reatribuição (RF-37) |
| `duracao_planejada_min` | `INTEGER` | — | Sim | Minutos | — |
| `inicio_planejado` | `TIMESTAMP WITH TIME ZONE` | — | Não | Data, hora e fuso | — |
| `fim_planejado` | `TIMESTAMP WITH TIME ZONE` | — | Não | Data, hora e fuso | — |
| `obrigatoria` | `BOOLEAN` | — | Sim | Sim ou não | — |
| `permite_nao_aplicavel` | `BOOLEAN` | — | Sim | Sim ou não | — |
| `sob_demanda` | `BOOLEAN` | — | Sim | Sim ou não | — |
| `estado` | `VARCHAR(20)` | — | Não | Aguardando, Pronta, Em execução, Pausada, Concluída, Não aplicável | Vazio = item do catálogo não acionado |
| `versao` | `INTEGER` | — | Sim | Inteiro | Conta as mudanças da tarefa; vai nos avisos para o Monitoramento ordenar |

**Restrições:**

- CHECK: estado vazio só com sob_demanda
- CHECK: com estado, responsavel_id, inicio_planejado e fim_planejado obrigatórios
- CHECK (fim_planejado > inicio_planejado)

### B.2.5 `dependencia_tarefa`

Dependências das tarefas em andamento, N:N (RF-21, RF-42). RFs: RF-14, RF-21, RF-42.

| Campo | Tipo | Chave | Obrigatório | Domínio ou valores | Descrição |
|---|---|---|---|---|---|
| `predecessora_id` | `CHAR(36)` | PK, FK | Sim | Identificador de `tarefa` | — |
| `sucessora_id` | `CHAR(36)` | PK, FK | Sim | Identificador de `tarefa` | — |

**Restrições:**

- CHECK (predecessora_id <> sucessora_id)
- Regra: predecessora com estado vazio (catálogo não acionado) não segura a sucessora

### B.2.6 `ponto_confirmacao`

Pontos de QR Code da tarefa (RF-16, RF-19). RFs: RF-16, RF-19.

| Campo | Tipo | Chave | Obrigatório | Domínio ou valores | Descrição |
|---|---|---|---|---|---|
| `id` | `CHAR(36)` | PK | Sim | Identificador de `ponto_confirmacao_plano` (Cadastro e Planejamento), sem FK | Identificador gerado no plano |
| `tarefa_id` | `CHAR(36)` | FK | Sim | Identificador de `tarefa` | — |
| `identificador` | `VARCHAR(30)` | — | Sim | Texto | Conteúdo do QR Code |
| `nome` | `VARCHAR(60)` | — | Sim | Texto | — |

**Restrições:**

- UNIQUE (tarefa_id, identificador)
- UNIQUE (tarefa_id, nome)
- Confirmado = tem leitura (não se guarda)

### B.2.7 `leitura_qr_code`

Leitura de cada ponto (RF-19). RFs: RF-16, RF-19.

| Campo | Tipo | Chave | Obrigatório | Domínio ou valores | Descrição |
|---|---|---|---|---|---|
| `id` | `CHAR(36)` | PK | Sim | UUID | — |
| `ponto_id` | `CHAR(36)` | FK | Sim | Identificador de `ponto_confirmacao` | Uma leitura por ponto |
| `autor_id` | `CHAR(36)` | — | Sim | Identificador de `usuario` (Cadastro e Planejamento), sem FK | — |
| `horario_acao` | `TIMESTAMP WITH TIME ZONE` | — | Sim | Data, hora e fuso | Horário do celular, em UTC (RNF-8) |
| `recebido_em` | `TIMESTAMP WITH TIME ZONE` | — | Sim | Data, hora e fuso | — |
| `requisicao_id` | `CHAR(36)` | — | Sim | UUID | Chave de envio (RNF-8) |

**Restrições:**

- UNIQUE (ponto_id)
- UNIQUE (requisicao_id)

### B.2.8 `tabela_codigo_atraso`

Versões da tabela de códigos de atraso da ANAC; dona: Execução em Solo (RNF-22; ADR-0006). RFs: RF-17, RF-36.

| Campo | Tipo | Chave | Obrigatório | Domínio ou valores | Descrição |
|---|---|---|---|---|---|
| `versao` | `INTEGER` | PK | Sim | Inteiro | — |
| `referencia` | `VARCHAR(100)` | — | Sim | Texto | Ex.: Portaria nº 55/2026 |
| `carregada_em` | `TIMESTAMP WITH TIME ZONE` | — | Sim | Data, hora e fuso | — |
| `vigente` | `BOOLEAN` | — | Sim | Sim ou não | — |

**Restrições:**

- Regra: uma só versão vigente
- Regra: linhas de uma versão nunca mudam (RNF-22)

### B.2.9 `codigo_atraso`

Códigos de uma versão: 72 em 12 categorias na tabela atual (ADR-0006). RFs: RF-17, RF-36.

| Campo | Tipo | Chave | Obrigatório | Domínio ou valores | Descrição |
|---|---|---|---|---|---|
| `versao` | `INTEGER` | PK, FK | Sim | Identificador de `tabela_codigo_atraso` | — |
| `codigo` | `CHAR(2)` | PK | Sim | Texto | Sigla de duas letras |
| `categoria` | `VARCHAR(100)` | — | Sim | Texto | Uma das 12 categorias |
| `descricao` | `VARCHAR(200)` | — | Sim | Texto | — |

### B.2.10 `registro_tarefa`

Início, conclusão, pausa, retomada e "Não aplicável" (RF-15 a RF-18). RFs: RF-15, RF-16, RF-17, RF-18, RF-20, RF-43.

| Campo | Tipo | Chave | Obrigatório | Domínio ou valores | Descrição |
|---|---|---|---|---|---|
| `id` | `CHAR(36)` | PK | Sim | UUID | — |
| `tarefa_id` | `CHAR(36)` | FK | Sim | Identificador de `tarefa` | — |
| `tipo` | `VARCHAR(20)` | — | Sim | Início, Conclusão, Pausa, Retomada, Não aplicável | — |
| `horario_acao` | `TIMESTAMP WITH TIME ZONE` | — | Sim | Data, hora e fuso | Horário do celular, em UTC (RNF-8) |
| `recebido_em` | `TIMESTAMP WITH TIME ZONE` | — | Sim | Data, hora e fuso | — |
| `autor_id` | `CHAR(36)` | — | Sim | Identificador de `usuario` (Cadastro e Planejamento), sem FK | — |
| `justificativa` | `VARCHAR(500)` | — | Não | Texto | Pausa e Não aplicável |
| `codigo_versao` | `INTEGER` | FK | Não | Identificador de `codigo_atraso` | Pausa com impedimento (RNF-22) |
| `codigo_atraso` | `CHAR(2)` | FK | Não | Identificador de `codigo_atraso` | — |
| `requisicao_id` | `CHAR(36)` | — | Sim | UUID | Chave de envio (RNF-8) |

**Restrições:**

- UNIQUE (requisicao_id)
- FK (codigo_versao, codigo_atraso) → codigo_atraso; os dois juntos e só na Pausa
- CHECK: justificativa obrigatória na Pausa e no Não aplicável
- Registro recusado não é gravado

### B.2.11 `historico_estado_turnaround`

Cada mudança de estado do turnaround, com a causa (RF-21; RNF-24). RFs: RF-12, RF-21, RF-36, RF-39, RF-40, RF-44.

| Campo | Tipo | Chave | Obrigatório | Domínio ou valores | Descrição |
|---|---|---|---|---|---|
| `id` | `CHAR(36)` | PK | Sim | UUID | — |
| `turnaround_id` | `CHAR(36)` | FK | Sim | Identificador de `turnaround` | — |
| `estado_anterior` | `VARCHAR(30)` | — | Não | Texto | Vazio na chegada |
| `estado_novo` | `VARCHAR(30)` | — | Sim | Em solo, Operações em andamento, Em exceção, Pronto para liberação, Liberado, Fora de bloco | — |
| `ocorrido_em` | `TIMESTAMP WITH TIME ZONE` | — | Sim | Data, hora e fuso | — |
| `autor_id` | `CHAR(36)` | — | Não | Identificador de `usuario` (Cadastro e Planejamento), sem FK | Vazio = Motor de Eventos |
| `causa_id` | `CHAR(36)` | — | Sim | UUID | Registro, marco ou pedido que causou |

### B.2.12 `historico_estado_tarefa`

Cada mudança de estado da tarefa, com a causa (RF-21). RFs: RF-15, RF-16, RF-17, RF-18, RF-21, RF-42.

| Campo | Tipo | Chave | Obrigatório | Domínio ou valores | Descrição |
|---|---|---|---|---|---|
| `id` | `CHAR(36)` | PK | Sim | UUID | — |
| `tarefa_id` | `CHAR(36)` | FK | Sim | Identificador de `tarefa` | — |
| `estado_anterior` | `VARCHAR(20)` | — | Não | Texto | Vazio no acionamento do catálogo |
| `estado_novo` | `VARCHAR(20)` | — | Sim | Aguardando, Pronta, Em execução, Pausada, Concluída, Não aplicável | — |
| `ocorrido_em` | `TIMESTAMP WITH TIME ZONE` | — | Sim | Data, hora e fuso | — |
| `autor_id` | `CHAR(36)` | — | Não | Identificador de `usuario` (Cadastro e Planejamento), sem FK | Vazio = Motor de Eventos |
| `causa_id` | `CHAR(36)` | — | Sim | UUID | Registro ou pedido que causou |

### B.2.13 `registro_auditoria` (técnica)

Trilha de auditoria do serviço (RNF-2, RNF-6); sem FK, para sobreviver à anonimização.

| Campo | Tipo | Chave | Obrigatório | Domínio ou valores | Descrição |
|---|---|---|---|---|---|
| `id` | `CHAR(36)` | PK | Sim | UUID | Identificador do registro |
| `objeto` | `VARCHAR(40)` | — | Sim | Texto | Tabela alterada |
| `objeto_id` | `VARCHAR(80)` | — | Sim | Texto | Chave da linha; chave composta escrita como a|b |
| `acao` | `VARCHAR(30)` | — | Sim | Inclusão, Alteração, Exclusão, Desativação, Anonimização | — |
| `autor_tipo` | `VARCHAR(20)` | — | Sim | Texto | Usuário ou Motor de Eventos |
| `autor_id` | `CHAR(36)` | — | Não | Identificador de `usuario` (Cadastro e Planejamento), sem FK | Obrigatório quando o autor é Usuário |
| `causa_id` | `CHAR(36)` | — | Não | UUID | Registro ou aviso que causou a ação automática |
| `gatilho` | `VARCHAR(60)` | — | Não | Texto | Gatilho por horário sem registro (recálculo de minuto, TOBT − X, TOBT + 5, TOBT − 15) |
| `turnaround_id` | `CHAR(36)` | — | Não | Identificador de `turnaround` (Cadastro e Planejamento), sem FK | Turnaround relacionado; vazio = prazo do RNF-6 conta do próprio registro |
| `ocorrido_em` | `TIMESTAMP WITH TIME ZONE` | — | Sim | Data, hora e fuso | Data e hora da ação |
| `valores_anteriores` | `CLOB` | — | Não | Texto JSON | Valores antes da mudança, em JSON |
| `valores_novos` | `CLOB` | — | Não | Texto JSON | Valores depois da mudança, em JSON |
| `anonimizado_em` | `TIMESTAMP WITH TIME ZONE` | — | Não | Data, hora e fuso | Rotina do RNF-6 |

**Restrições:**

- CHECK: autor_tipo = Usuário exige autor_id; Motor de Eventos exige causa_id ou gatilho

### B.2.14 `aviso_saida` (técnica)

Avisos a publicar, gravados na mesma transação da mudança (ADR-0016); origem = nome do serviço, constante.

| Campo | Tipo | Chave | Obrigatório | Domínio ou valores | Descrição |
|---|---|---|---|---|---|
| `id` | `CHAR(36)` | PK | Sim | UUID | id do envelope |
| `tipo` | `VARCHAR(60)` | — | Sim | Texto | Nome do aviso, em PascalCase, no passado |
| `versao` | `INTEGER` | — | Sim | Inteiro | Versão do formato |
| `ocorrido_em` | `TIMESTAMP WITH TIME ZONE` | — | Sim | Data, hora e fuso | Quando o fato aconteceu |
| `turnaround_id` | `CHAR(36)` | — | Não | Identificador de `turnaround` (Cadastro e Planejamento), sem FK | Turnaround do fato |
| `autor_id` | `CHAR(36)` | — | Não | Identificador de `usuario` (Cadastro e Planejamento), sem FK | Autor do fato |
| `causa_id` | `CHAR(36)` | — | Não | UUID | Registro que causou o aviso |
| `dados` | `CLOB` | — | Sim | Texto JSON | Conteúdo do aviso em JSON |
| `gravado_em` | `TIMESTAMP WITH TIME ZONE` | — | Sim | Data, hora e fuso | Ordem de publicação |
| `publicado_em` | `TIMESTAMP WITH TIME ZONE` | — | Não | Data, hora e fuso | Vazio até a mensageria confirmar |

### B.2.15 `aviso_processado` (técnica)

Avisos já recebidos, para descartar o repetido (ADR-0016).

| Campo | Tipo | Chave | Obrigatório | Domínio ou valores | Descrição |
|---|---|---|---|---|---|
| `aviso_id` | `CHAR(36)` | PK | Sim | UUID | id do envelope recebido |
| `processado_em` | `TIMESTAMP WITH TIME ZONE` | — | Sim | Data, hora e fuso | Quando foi processado |


## B.3 Monitoramento

### B.3.1 `turnaround_monitorado`

Cópia do turnaround para calcular e exibir, com os parâmetros vigentes na abertura (RNF-21). RFs: RF-22, RF-25, RF-26, RF-28, RF-29, RF-30, RF-31, RF-32, RF-34.

| Campo | Tipo | Chave | Obrigatório | Domínio ou valores | Descrição |
|---|---|---|---|---|---|
| `turnaround_id` | `CHAR(36)` | PK | Sim | Identificador de `turnaround` (Cadastro e Planejamento), sem FK | — |
| `matricula` | `VARCHAR(10)` | — | Sim | Texto | — |
| `tipo_aeronave` | `VARCHAR(10)` | — | Sim | Texto | — |
| `voo_chegada` | `VARCHAR(10)` | — | Sim | Texto | — |
| `voo_partida` | `VARCHAR(10)` | — | Sim | Texto | — |
| `posicao` | `VARCHAR(10)` | — | Sim | Texto | — |
| `estado` | `VARCHAR(30)` | — | Não | Texto | Cópia; vazio até o AIBT |
| `tobt_planejado` | `TIMESTAMP WITH TIME ZONE` | — | Sim | Data, hora e fuso | — |
| `tobt_vigente` | `TIMESTAMP WITH TIME ZONE` | — | Sim | Data, hora e fuso | Cópia; começa igual ao planejado (ADR-0003) |
| `eibt` | `TIMESTAMP WITH TIME ZONE` | — | Sim | Data, hora e fuso | — |
| `mttt_min` | `INTEGER` | — | Sim | Minutos | — |
| `aibt` | `TIMESTAMP WITH TIME ZONE` | — | Não | Data, hora e fuso | — |
| `acgt` | `TIMESTAMP WITH TIME ZONE` | — | Não | Data, hora e fuso | — |
| `asbt` | `TIMESTAMP WITH TIME ZONE` | — | Não | Data, hora e fuso | — |
| `aegt` | `TIMESTAMP WITH TIME ZONE` | — | Não | Data, hora e fuso | — |
| `ardt` | `TIMESTAMP WITH TIME ZONE` | — | Não | Data, hora e fuso | — |
| `aobt` | `TIMESTAMP WITH TIME ZONE` | — | Não | Data, hora e fuso | Também define o período do RF-34 |
| `pronto_para_liberacao_em` | `TIMESTAMP WITH TIME ZONE` | — | Não | Data, hora e fuso | Primeira entrada no estado (RF-34); pode diferir do AEGT |
| `tolerancia_prontidao_min` | `INTEGER` | — | Sim | Minutos | TOBT + 5 (RNF-21) |
| `espera_tarefa_pronta_min` | `INTEGER` | — | Sim | Minutos | Y do RF-27 |
| `antecedencia_embarque_min` | `INTEGER` | — | Sim | Minutos | X do RF-30 |
| `antecedencia_checagem_min` | `INTEGER` | — | Sim | Minutos | 15 do RF-32 |
| `prazo_acao_critica_min` | `INTEGER` | — | Sim | Minutos | 2 min do RF-34 |

### B.3.2 `tarefa_monitorada`

Cópia da tarefa do plano para calcular e exibir; o catálogo só entra quando acionado. RFs: RF-22, RF-23, RF-24, RF-26, RF-27, RF-30, RF-31, RF-32, RF-34.

| Campo | Tipo | Chave | Obrigatório | Domínio ou valores | Descrição |
|---|---|---|---|---|---|
| `tarefa_id` | `CHAR(36)` | PK | Sim | Identificador de `tarefa` (Execução em Solo), sem FK | — |
| `turnaround_id` | `CHAR(36)` | FK | Sim | Identificador de `turnaround_monitorado` | — |
| `nome` | `VARCHAR(60)` | — | Sim | Texto | — |
| `tipo_atividade` | `VARCHAR(20)` | — | Sim | Texto | — |
| `equipe_id` | `CHAR(36)` | — | Sim | Identificador de `equipe` (Cadastro e Planejamento), sem FK | — |
| `responsavel_id` | `CHAR(36)` | — | Sim | Identificador de `usuario` (Cadastro e Planejamento), sem FK | — |
| `estado` | `VARCHAR(20)` | — | Sim | Aguardando, Pronta, Em execução, Pausada, Concluída, Não aplicável | — |
| `obrigatoria` | `BOOLEAN` | — | Sim | Sim ou não | — |
| `duracao_planejada_min` | `INTEGER` | — | Sim | Minutos | — |
| `inicio_planejado` | `TIMESTAMP WITH TIME ZONE` | — | Sim | Data, hora e fuso | Janela atual |
| `fim_planejado` | `TIMESTAMP WITH TIME ZONE` | — | Sim | Data, hora e fuso | — |
| `inicio_planejado_original` | `TIMESTAMP WITH TIME ZONE` | — | Sim | Data, hora e fuso | Janela do plano confirmado ou da inclusão (RF-34) |
| `fim_planejado_original` | `TIMESTAMP WITH TIME ZONE` | — | Sim | Data, hora e fuso | — |
| `inicio_real` | `TIMESTAMP WITH TIME ZONE` | — | Não | Data, hora e fuso | — |
| `fim_real` | `TIMESTAMP WITH TIME ZONE` | — | Não | Data, hora e fuso | — |
| `pronta_em` | `TIMESTAMP WITH TIME ZONE` | — | Não | Data, hora e fuso | Última entrada em Pronta (RF-27) |
| `executado_min` | `INTEGER` | — | Sim | Minutos | Minutos executados até a última pausa (RF-22) |
| `em_execucao_desde` | `TIMESTAMP WITH TIME ZONE` | — | Não | Data, hora e fuso | Início ou última retomada |
| `justificativa` | `VARCHAR(500)` | — | Não | Texto | Pausa ou Não aplicável (RF-26) |
| `codigo_versao` | `INTEGER` | — | Não | Inteiro | RNF-22 |
| `codigo_atraso` | `CHAR(2)` | — | Não | Texto | — |
| `codigo_descricao` | `VARCHAR(200)` | — | Não | Texto | Descrição gravada com o registro (RNF-22) |
| `versao_origem` | `INTEGER` | — | Sim | Inteiro | Versão da tarefa no último aviso aplicado; aviso com versão menor é ignorado |

### B.3.3 `dependencia_monitorada`

Cópia das dependências, N:N (RF-22 a RF-24). RFs: RF-22, RF-23, RF-24.

| Campo | Tipo | Chave | Obrigatório | Domínio ou valores | Descrição |
|---|---|---|---|---|---|
| `predecessora_id` | `CHAR(36)` | PK, FK | Sim | Identificador de `tarefa_monitorada` | — |
| `sucessora_id` | `CHAR(36)` | PK, FK | Sim | Identificador de `tarefa_monitorada` | — |

### B.3.4 `projecao`

Cada cálculo da projeção de prontidão (RF-22 pede o registro). RFs: RF-22, RF-25, RF-26, RF-28, RF-41.

| Campo | Tipo | Chave | Obrigatório | Domínio ou valores | Descrição |
|---|---|---|---|---|---|
| `id` | `CHAR(36)` | PK | Sim | UUID | — |
| `turnaround_id` | `CHAR(36)` | FK | Sim | Identificador de `turnaround_monitorado` | — |
| `projecao_prontidao` | `TIMESTAMP WITH TIME ZONE` | — | Sim | Data, hora e fuso | — |
| `tobt_vigente` | `TIMESTAMP WITH TIME ZONE` | — | Sim | Data, hora e fuso | TOBT vigente usado no cálculo |
| `desvio_planejado_min` | `INTEGER` | — | Sim | Minutos | Projeção − TOBT planejado, com sinal |
| `desvio_vigente_min` | `INTEGER` | — | Sim | Minutos | Projeção − TOBT vigente, com sinal |
| `calculada_em` | `TIMESTAMP WITH TIME ZONE` | — | Sim | Data, hora e fuso | — |
| `causa_tipo` | `VARCHAR(30)` | — | Sim | Início, Conclusão, Pausa, Retomada, Não aplicável, Chegada, Correção do AIBT, Replanejamento, Atualização do TOBT, Recálculo de minuto, Volta após falha | — |
| `causa_id` | `CHAR(36)` | — | Não | UUID | causaId do aviso; vazio no recálculo de minuto |
| `causa_tarefa_id` | `CHAR(36)` | FK | Não | Identificador de `tarefa_monitorada` | Para exibir a causa |

### B.3.5 `projecao_tarefa`

Atraso, impacto e projeção de cada tarefa em cada recálculo (RF-23; US023 e UC24 pedem o registro). RFs: RF-23, RF-26, RF-32.

| Campo | Tipo | Chave | Obrigatório | Domínio ou valores | Descrição |
|---|---|---|---|---|---|
| `projecao_id` | `CHAR(36)` | PK, FK | Sim | Identificador de `projecao` | — |
| `tarefa_id` | `CHAR(36)` | PK, FK | Sim | Identificador de `tarefa_monitorada` | — |
| `inicio_projetado` | `TIMESTAMP WITH TIME ZONE` | — | Não | Data, hora e fuso | — |
| `fim_projetado` | `TIMESTAMP WITH TIME ZONE` | — | Não | Data, hora e fuso | Vazio para Não aplicável |
| `atraso_inicio_min` | `INTEGER` | — | Não | Minutos | Minutos completos; 0 = sem atraso |
| `atraso_fim_min` | `INTEGER` | — | Não | Minutos | — |
| `impactada_por_id` | `CHAR(36)` | FK | Não | Identificador de `tarefa_monitorada` | Tarefa de origem do atraso |
| `impacto_min` | `INTEGER` | — | Não | Minutos | — |

**Restrições:**

- CHECK: impactada_por_id e impacto_min juntos

### B.3.6 `caminho_critico`

Cada mudança do caminho crítico (RF-24 pede o anterior e o novo). RFs: RF-24, RF-26.

| Campo | Tipo | Chave | Obrigatório | Domínio ou valores | Descrição |
|---|---|---|---|---|---|
| `id` | `CHAR(36)` | PK | Sim | UUID | — |
| `projecao_id` | `CHAR(36)` | FK | Sim | Identificador de `projecao` | Recálculo que mudou o caminho (horário e causa) |
| `anterior_id` | `CHAR(36)` | FK | Não | Identificador de `caminho_critico` | Vazio no primeiro caminho do turnaround |

**Restrições:**

- UNIQUE (projecao_id)
- UNIQUE (anterior_id)

### B.3.7 `caminho_critico_tarefa`

Tarefas de cada caminho, em ordem, N:N. RFs: RF-24.

| Campo | Tipo | Chave | Obrigatório | Domínio ou valores | Descrição |
|---|---|---|---|---|---|
| `caminho_id` | `CHAR(36)` | PK, FK | Sim | Identificador de `caminho_critico` | — |
| `tarefa_id` | `CHAR(36)` | PK, FK | Sim | Identificador de `tarefa_monitorada` | — |
| `ordem` | `INTEGER` | — | Sim | Inteiro | Posição na cadeia; empatadas têm a mesma ordem |

### B.3.8 `alerta`

Alertas emitidos e encerrados (RF-27 a RF-31, RF-33); dados do gatilho por tipo. RFs: RF-25, RF-27, RF-28, RF-29, RF-30, RF-31, RF-33, RF-34, RF-38.

| Campo | Tipo | Chave | Obrigatório | Domínio ou valores | Descrição |
|---|---|---|---|---|---|
| `id` | `CHAR(36)` | PK | Sim | UUID | — |
| `turnaround_id` | `CHAR(36)` | FK | Sim | Identificador de `turnaround_monitorado` | — |
| `tipo` | `VARCHAR(30)` | — | Sim | Tarefa pronta não iniciada, Projeção além de TOBT + 5, Viabilidade, Embarque não iniciado, Prontidão não registrada | — |
| `tarefa_id` | `CHAR(36)` | FK | Não | Identificador de `tarefa_monitorada` | RF-27 e RF-30 |
| `critico` | `BOOLEAN` | — | Sim | Sim ou não | Classificação na emissão (RF-33; medida no RF-34) |
| `ciclo` | `INTEGER` | — | Sim | Inteiro | Número da emissão; rearme do RF-28 |
| `emitido_em` | `TIMESTAMP WITH TIME ZONE` | — | Sim | Data, hora e fuso | — |
| `minutos_espera` | `INTEGER` | — | Não | Inteiro | RF-27 |
| `projecao_id` | `CHAR(36)` | FK | Não | Identificador de `projecao` | RF-28: projeção e desvio |
| `eibt` | `TIMESTAMP WITH TIME ZONE` | — | Não | Data, hora e fuso | RF-29, na emissão |
| `mttt_min` | `INTEGER` | — | Não | Minutos | RF-29, na emissão |
| `tobt_vigente` | `TIMESTAMP WITH TIME ZONE` | — | Não | Data, hora e fuso | RF-29 a RF-31, na emissão |
| `estado_turnaround` | `VARCHAR(30)` | — | Não | Texto | RF-31, na emissão |
| `encerrado_em` | `TIMESTAMP WITH TIME ZONE` | — | Não | Data, hora e fuso | Pelo aviso da ação (RF-38) |
| `acao_id` | `CHAR(36)` | — | Não | Identificador de `acao_alerta` (Exceções e Liberação), sem FK | Cópia do aviso da ação |
| `tipo_acao` | `VARCHAR(30)` | — | Não | Texto | Cópia |
| `acao_autor_id` | `CHAR(36)` | — | Não | Identificador de `usuario` (Cadastro e Planejamento), sem FK | Cópia (UC26 E1) |
| `acao_registrada_em` | `TIMESTAMP WITH TIME ZONE` | — | Não | Data, hora e fuso | Cópia; indicador de 2 min (RF-34) |

**Restrições:**

- UNIQUE (turnaround_id, tipo, tarefa_id, ciclo)
- Regra: campos do gatilho preenchidos conforme o tipo

### B.3.9 `alerta_tarefa`

Tarefas listadas no alerta, com o estado na emissão (RF-28, RF-30, RF-31). RFs: RF-28, RF-30, RF-31.

| Campo | Tipo | Chave | Obrigatório | Domínio ou valores | Descrição |
|---|---|---|---|---|---|
| `alerta_id` | `CHAR(36)` | PK, FK | Sim | Identificador de `alerta` | — |
| `tarefa_id` | `CHAR(36)` | PK, FK | Sim | Identificador de `tarefa_monitorada` | — |
| `estado` | `VARCHAR(20)` | — | Sim | Texto | Estado na emissão |
| `atraso_inicio_min` | `INTEGER` | — | Não | Minutos | — |
| `atraso_fim_min` | `INTEGER` | — | Não | Minutos | — |

### B.3.10 `aviso_checagem`

Aviso de TOBT − 15 e checagem com as equipes, um por turnaround (RF-32, RF-35). RFs: RF-26, RF-32, RF-35.

| Campo | Tipo | Chave | Obrigatório | Domínio ou valores | Descrição |
|---|---|---|---|---|---|
| `id` | `CHAR(36)` | PK | Sim | UUID | — |
| `turnaround_id` | `CHAR(36)` | FK | Sim | Identificador de `turnaround_monitorado` | — |
| `tobt_vigente` | `TIMESTAMP WITH TIME ZONE` | — | Sim | Data, hora e fuso | TOBT que gerou o aviso |
| `emitido_em` | `TIMESTAMP WITH TIME ZONE` | — | Sim | Data, hora e fuso | — |
| `encerrado_em` | `TIMESTAMP WITH TIME ZONE` | — | Não | Data, hora e fuso | Horário da checagem (RF-35) |
| `autor_checagem_id` | `CHAR(36)` | — | Não | Identificador de `usuario` (Cadastro e Planejamento), sem FK | — |

**Restrições:**

- UNIQUE (turnaround_id)
- CHECK: encerrado_em e autor_checagem_id juntos

### B.3.11 `atualizacao_tobt_monitorada`

Cópia das atualizações do TOBT para o indicador (RF-34). RFs: RF-34.

| Campo | Tipo | Chave | Obrigatório | Domínio ou valores | Descrição |
|---|---|---|---|---|---|
| `id` | `CHAR(36)` | PK | Sim | Identificador de `atualizacao_tobt` (Exceções e Liberação), sem FK | — |
| `turnaround_id` | `CHAR(36)` | FK | Sim | Identificador de `turnaround_monitorado` | — |
| `tobt_anterior` | `TIMESTAMP WITH TIME ZONE` | — | Sim | Data, hora e fuso | Vigente no momento |
| `tobt_novo` | `TIMESTAMP WITH TIME ZONE` | — | Sim | Data, hora e fuso | — |
| `registrada_em` | `TIMESTAMP WITH TIME ZONE` | — | Sim | Data, hora e fuso | — |

### B.3.12 `registro_auditoria` (técnica)

Trilha de auditoria do serviço (RNF-2, RNF-6); sem FK, para sobreviver à anonimização.

| Campo | Tipo | Chave | Obrigatório | Domínio ou valores | Descrição |
|---|---|---|---|---|---|
| `id` | `CHAR(36)` | PK | Sim | UUID | Identificador do registro |
| `objeto` | `VARCHAR(40)` | — | Sim | Texto | Tabela alterada |
| `objeto_id` | `VARCHAR(80)` | — | Sim | Texto | Chave da linha; chave composta escrita como a|b |
| `acao` | `VARCHAR(30)` | — | Sim | Inclusão, Alteração, Exclusão, Desativação, Anonimização | — |
| `autor_tipo` | `VARCHAR(20)` | — | Sim | Texto | Usuário ou Motor de Eventos |
| `autor_id` | `CHAR(36)` | — | Não | Identificador de `usuario` (Cadastro e Planejamento), sem FK | Obrigatório quando o autor é Usuário |
| `causa_id` | `CHAR(36)` | — | Não | UUID | Registro ou aviso que causou a ação automática |
| `gatilho` | `VARCHAR(60)` | — | Não | Texto | Gatilho por horário sem registro (recálculo de minuto, TOBT − X, TOBT + 5, TOBT − 15) |
| `turnaround_id` | `CHAR(36)` | — | Não | Identificador de `turnaround` (Cadastro e Planejamento), sem FK | Turnaround relacionado; vazio = prazo do RNF-6 conta do próprio registro |
| `ocorrido_em` | `TIMESTAMP WITH TIME ZONE` | — | Sim | Data, hora e fuso | Data e hora da ação |
| `valores_anteriores` | `CLOB` | — | Não | Texto JSON | Valores antes da mudança, em JSON |
| `valores_novos` | `CLOB` | — | Não | Texto JSON | Valores depois da mudança, em JSON |
| `anonimizado_em` | `TIMESTAMP WITH TIME ZONE` | — | Não | Data, hora e fuso | Rotina do RNF-6 |

**Restrições:**

- CHECK: autor_tipo = Usuário exige autor_id; Motor de Eventos exige causa_id ou gatilho

### B.3.13 `aviso_saida` (técnica)

Avisos a publicar, gravados na mesma transação da mudança (ADR-0016); origem = nome do serviço, constante.

| Campo | Tipo | Chave | Obrigatório | Domínio ou valores | Descrição |
|---|---|---|---|---|---|
| `id` | `CHAR(36)` | PK | Sim | UUID | id do envelope |
| `tipo` | `VARCHAR(60)` | — | Sim | Texto | Nome do aviso, em PascalCase, no passado |
| `versao` | `INTEGER` | — | Sim | Inteiro | Versão do formato |
| `ocorrido_em` | `TIMESTAMP WITH TIME ZONE` | — | Sim | Data, hora e fuso | Quando o fato aconteceu |
| `turnaround_id` | `CHAR(36)` | — | Não | Identificador de `turnaround` (Cadastro e Planejamento), sem FK | Turnaround do fato |
| `autor_id` | `CHAR(36)` | — | Não | Identificador de `usuario` (Cadastro e Planejamento), sem FK | Autor do fato |
| `causa_id` | `CHAR(36)` | — | Não | UUID | Registro que causou o aviso |
| `dados` | `CLOB` | — | Sim | Texto JSON | Conteúdo do aviso em JSON |
| `gravado_em` | `TIMESTAMP WITH TIME ZONE` | — | Sim | Data, hora e fuso | Ordem de publicação |
| `publicado_em` | `TIMESTAMP WITH TIME ZONE` | — | Não | Data, hora e fuso | Vazio até a mensageria confirmar |

### B.3.14 `aviso_processado` (técnica)

Avisos já recebidos, para descartar o repetido (ADR-0016).

| Campo | Tipo | Chave | Obrigatório | Domínio ou valores | Descrição |
|---|---|---|---|---|---|
| `aviso_id` | `CHAR(36)` | PK | Sim | UUID | id do envelope recebido |
| `processado_em` | `TIMESTAMP WITH TIME ZONE` | — | Sim | Data, hora e fuso | Quando foi processado |


## B.4 Exceções e Liberação

### B.4.1 `turnaround_referencia`

Turnaround e TOBT vigente: dono do vigente (ADR-0015), com os parâmetros vigentes na abertura (RNF-21). RFs: RF-36, RF-37, RF-38, RF-39, RF-40, RF-41, RF-42.

| Campo | Tipo | Chave | Obrigatório | Domínio ou valores | Descrição |
|---|---|---|---|---|---|
| `turnaround_id` | `CHAR(36)` | PK | Sim | Identificador de `turnaround` (Cadastro e Planejamento), sem FK | — |
| `companhia_id` | `CHAR(36)` | — | Sim | Identificador de `companhia` (Cadastro e Planejamento), sem FK | Cópia imutável; quem pode liberar (UC32) |
| `tobt_planejado` | `TIMESTAMP WITH TIME ZONE` | — | Sim | Data, hora e fuso | Recebido na abertura |
| `tobt_vigente` | `TIMESTAMP WITH TIME ZONE` | — | Sim | Data, hora e fuso | Começa igual ao planejado (ADR-0003); só o RF-41 muda |
| `projecao_prontidao` | `TIMESTAMP WITH TIME ZONE` | — | Não | Data, hora e fuso | Última projeção recebida do Monitoramento (RF-41) |
| `projecao_calculada_em` | `TIMESTAMP WITH TIME ZONE` | — | Não | Data, hora e fuso | — |
| `limiar_atualizacao_tobt_min` | `INTEGER` | — | Sim | Minutos | 5 min do RF-41 (RNF-21; ADR-0020) |
| `prazo_acao_critica_min` | `INTEGER` | — | Sim | Minutos | 2 min (RNF-21; ADR-0020) |
| `aobt` | `TIMESTAMP WITH TIME ZONE` | — | Não | Data, hora e fuso | Cópia por aviso; só para o prazo do RNF-6 |

### B.4.2 `solicitacao_atualizacao_tobt`

Pedido ao Coordenador de Turnaround quando a projeção se afasta 5 min do vigente (RF-41). RFs: RF-41.

| Campo | Tipo | Chave | Obrigatório | Domínio ou valores | Descrição |
|---|---|---|---|---|---|
| `id` | `CHAR(36)` | PK | Sim | UUID | — |
| `turnaround_id` | `CHAR(36)` | FK | Sim | Identificador de `turnaround_referencia` | — |
| `projecao_prontidao` | `TIMESTAMP WITH TIME ZONE` | — | Sim | Data, hora e fuso | Projeção que disparou |
| `projecao_calculada_em` | `TIMESTAMP WITH TIME ZONE` | — | Sim | Data, hora e fuso | — |
| `solicitada_em` | `TIMESTAMP WITH TIME ZONE` | — | Sim | Data, hora e fuso | — |
| `encerrada_em` | `TIMESTAMP WITH TIME ZONE` | — | Não | Data, hora e fuso | — |
| `motivo_encerramento` | `VARCHAR(30)` | — | Não | Atendida, Projeção de volta à faixa, Turnaround liberado (UC34) | — |

**Restrições:**

- Regra: uma solicitação aberta por turnaround
- CHECK: encerrada_em e motivo_encerramento juntos

### B.4.3 `atualizacao_tobt`

Cada atualização do TOBT vigente (RF-41). RFs: RF-38, RF-41.

| Campo | Tipo | Chave | Obrigatório | Domínio ou valores | Descrição |
|---|---|---|---|---|---|
| `id` | `CHAR(36)` | PK | Sim | UUID | — |
| `turnaround_id` | `CHAR(36)` | FK | Sim | Identificador de `turnaround_referencia` | — |
| `solicitacao_id` | `CHAR(36)` | FK | Não | Identificador de `solicitacao_atualizacao_tobt` | Atualização sem solicitação também é aceita |
| `tobt_anterior` | `TIMESTAMP WITH TIME ZONE` | — | Sim | Data, hora e fuso | — |
| `tobt_novo` | `TIMESTAMP WITH TIME ZONE` | — | Sim | Data, hora e fuso | — |
| `autor_id` | `CHAR(36)` | — | Sim | Identificador de `usuario` (Cadastro e Planejamento), sem FK | — |
| `registrada_em` | `TIMESTAMP WITH TIME ZONE` | — | Sim | Data, hora e fuso | — |

**Restrições:**

- UNIQUE (solicitacao_id)
- CHECK (tobt_novo <> tobt_anterior)

### B.4.4 `tabela_codigo_atraso`

Cópia das versões da tabela da ANAC (dona: Execução em Solo). RFs: RF-36.

| Campo | Tipo | Chave | Obrigatório | Domínio ou valores | Descrição |
|---|---|---|---|---|---|
| `versao` | `INTEGER` | PK | Sim | Identificador de `tabela_codigo_atraso` (Execução em Solo), sem FK | — |
| `referencia` | `VARCHAR(100)` | — | Sim | Texto | — |
| `carregada_em` | `TIMESTAMP WITH TIME ZONE` | — | Sim | Data, hora e fuso | — |
| `vigente` | `BOOLEAN` | — | Sim | Sim ou não | — |

**Restrições:**

- Regra: uma só versão vigente

### B.4.5 `codigo_atraso`

Cópia dos códigos de cada versão. RFs: RF-36.

| Campo | Tipo | Chave | Obrigatório | Domínio ou valores | Descrição |
|---|---|---|---|---|---|
| `versao` | `INTEGER` | PK, FK | Sim | Identificador de `tabela_codigo_atraso` | — |
| `codigo` | `CHAR(2)` | PK | Sim | Texto | — |
| `categoria` | `VARCHAR(100)` | — | Sim | Texto | — |
| `descricao` | `VARCHAR(200)` | — | Sim | Texto | — |

### B.4.6 `excecao`

Exceção do turnaround (RF-36, RF-40). RFs: RF-36, RF-39, RF-40.

| Campo | Tipo | Chave | Obrigatório | Domínio ou valores | Descrição |
|---|---|---|---|---|---|
| `id` | `CHAR(36)` | PK | Sim | UUID | — |
| `turnaround_id` | `CHAR(36)` | FK | Sim | Identificador de `turnaround_referencia` | — |
| `tarefa_id` | `CHAR(36)` | — | Sim | Identificador de `tarefa` (Execução em Solo), sem FK | Tarefa afetada (UC29 RN1) |
| `codigo_versao` | `INTEGER` | FK | Sim | Identificador de `codigo_atraso` | — |
| `codigo_atraso` | `CHAR(2)` | FK | Sim | Identificador de `codigo_atraso` | — |
| `descricao_problema` | `VARCHAR(500)` | — | Sim | Texto | — |
| `estado_turnaround_anterior` | `VARCHAR(30)` | — | Não | Texto | Resposta da Execução em Solo, só para exibir (UC33) |
| `aberta_por_id` | `CHAR(36)` | — | Sim | Identificador de `usuario` (Cadastro e Planejamento), sem FK | — |
| `aberta_em` | `TIMESTAMP WITH TIME ZONE` | — | Sim | Data, hora e fuso | — |
| `solucao` | `VARCHAR(500)` | — | Não | Texto | RF-40 |
| `encerrada_por_id` | `CHAR(36)` | — | Não | Identificador de `usuario` (Cadastro e Planejamento), sem FK | — |
| `encerrada_em` | `TIMESTAMP WITH TIME ZONE` | — | Não | Data, hora e fuso | — |

**Restrições:**

- FK (codigo_versao, codigo_atraso) → codigo_atraso
- CHECK: solucao, encerrada_por_id e encerrada_em juntos

### B.4.7 `reatribuicao`

Motivo de cada reatribuição (RF-37). RFs: RF-37, RF-38.

| Campo | Tipo | Chave | Obrigatório | Domínio ou valores | Descrição |
|---|---|---|---|---|---|
| `id` | `CHAR(36)` | PK | Sim | UUID | — |
| `turnaround_id` | `CHAR(36)` | FK | Sim | Identificador de `turnaround_referencia` | — |
| `tarefa_id` | `CHAR(36)` | — | Sim | Identificador de `tarefa` (Execução em Solo), sem FK | — |
| `operador_anterior_id` | `CHAR(36)` | — | Sim | Identificador de `usuario` (Cadastro e Planejamento), sem FK | Da resposta da Execução em Solo |
| `operador_novo_id` | `CHAR(36)` | — | Sim | Identificador de `usuario` (Cadastro e Planejamento), sem FK | — |
| `motivo` | `VARCHAR(500)` | — | Sim | Texto | — |
| `autor_id` | `CHAR(36)` | — | Sim | Identificador de `usuario` (Cadastro e Planejamento), sem FK | — |
| `registrada_em` | `TIMESTAMP WITH TIME ZONE` | — | Sim | Data, hora e fuso | — |

### B.4.8 `replanejamento`

Cada replanejamento (RF-42); os valores anterior e novo ficam na auditoria da Execução em Solo. RFs: RF-38, RF-42.

| Campo | Tipo | Chave | Obrigatório | Domínio ou valores | Descrição |
|---|---|---|---|---|---|
| `id` | `CHAR(36)` | PK | Sim | UUID | — |
| `turnaround_id` | `CHAR(36)` | FK | Sim | Identificador de `turnaround_referencia` | — |
| `tarefa_id` | `CHAR(36)` | — | Sim | Identificador de `tarefa` (Execução em Solo), sem FK | Tarefa alterada ou incluída |
| `tipo` | `VARCHAR(30)` | — | Sim | Janela, Dependências, Inclusão sob demanda | — |
| `motivo` | `VARCHAR(500)` | — | Não | Texto | Obrigatório na inclusão sob demanda (ADR-0014) |
| `autor_id` | `CHAR(36)` | — | Sim | Identificador de `usuario` (Cadastro e Planejamento), sem FK | — |
| `registrada_em` | `TIMESTAMP WITH TIME ZONE` | — | Sim | Data, hora e fuso | — |

**Restrições:**

- CHECK: tipo = Inclusão sob demanda exige motivo

### B.4.9 `acao_alerta`

Ação tomada para cada alerta: uma por alerta (RF-38). RFs: RF-38.

| Campo | Tipo | Chave | Obrigatório | Domínio ou valores | Descrição |
|---|---|---|---|---|---|
| `id` | `CHAR(36)` | PK | Sim | UUID | — |
| `alerta_id` | `CHAR(36)` | — | Sim | Identificador de `alerta` (Monitoramento), sem FK | — |
| `turnaround_id` | `CHAR(36)` | FK | Sim | Identificador de `turnaround_referencia` | — |
| `tipo_acao` | `VARCHAR(30)` | — | Sim | Reatribuir tarefa, Replanejar, Atualizar a previsão, Abrir exceção | — |
| `excecao_id` | `CHAR(36)` | FK | Não | Identificador de `excecao` | — |
| `reatribuicao_id` | `CHAR(36)` | FK | Não | Identificador de `reatribuicao` | — |
| `replanejamento_id` | `CHAR(36)` | FK | Não | Identificador de `replanejamento` | — |
| `atualizacao_tobt_id` | `CHAR(36)` | FK | Não | Identificador de `atualizacao_tobt` | — |
| `autor_id` | `CHAR(36)` | — | Sim | Identificador de `usuario` (Cadastro e Planejamento), sem FK | — |
| `registrada_em` | `TIMESTAMP WITH TIME ZONE` | — | Sim | Data, hora e fuso | — |

**Restrições:**

- UNIQUE (alerta_id)
- UNIQUE (excecao_id)
- UNIQUE (reatribuicao_id)
- UNIQUE (replanejamento_id)
- UNIQUE (atualizacao_tobt_id)
- CHECK: exatamente uma das quatro FKs preenchida, coerente com tipo_acao

### B.4.10 `liberacao`

Confirmação da prontidão: uma por turnaround (RF-39); recusa não é gravada. RFs: RF-39.

| Campo | Tipo | Chave | Obrigatório | Domínio ou valores | Descrição |
|---|---|---|---|---|---|
| `id` | `CHAR(36)` | PK | Sim | UUID | — |
| `turnaround_id` | `CHAR(36)` | FK | Sim | Identificador de `turnaround_referencia` | — |
| `ardt` | `TIMESTAMP WITH TIME ZONE` | — | Sim | Data, hora e fuso | Horário da confirmação, guardado no pedido pendente |
| `autor_id` | `CHAR(36)` | — | Sim | Identificador de `usuario` (Cadastro e Planejamento), sem FK | — |
| `registrada_em` | `TIMESTAMP WITH TIME ZONE` | — | Sim | Data, hora e fuso | — |

**Restrições:**

- UNIQUE (turnaround_id)

### B.4.11 `registro_auditoria` (técnica)

Trilha de auditoria do serviço (RNF-2, RNF-6); sem FK, para sobreviver à anonimização.

| Campo | Tipo | Chave | Obrigatório | Domínio ou valores | Descrição |
|---|---|---|---|---|---|
| `id` | `CHAR(36)` | PK | Sim | UUID | Identificador do registro |
| `objeto` | `VARCHAR(40)` | — | Sim | Texto | Tabela alterada |
| `objeto_id` | `VARCHAR(80)` | — | Sim | Texto | Chave da linha; chave composta escrita como a|b |
| `acao` | `VARCHAR(30)` | — | Sim | Inclusão, Alteração, Exclusão, Desativação, Anonimização | — |
| `autor_tipo` | `VARCHAR(20)` | — | Sim | Texto | Usuário ou Motor de Eventos |
| `autor_id` | `CHAR(36)` | — | Não | Identificador de `usuario` (Cadastro e Planejamento), sem FK | Obrigatório quando o autor é Usuário |
| `causa_id` | `CHAR(36)` | — | Não | UUID | Registro ou aviso que causou a ação automática |
| `gatilho` | `VARCHAR(60)` | — | Não | Texto | Gatilho por horário sem registro (recálculo de minuto, TOBT − X, TOBT + 5, TOBT − 15) |
| `turnaround_id` | `CHAR(36)` | — | Não | Identificador de `turnaround` (Cadastro e Planejamento), sem FK | Turnaround relacionado; vazio = prazo do RNF-6 conta do próprio registro |
| `ocorrido_em` | `TIMESTAMP WITH TIME ZONE` | — | Sim | Data, hora e fuso | Data e hora da ação |
| `valores_anteriores` | `CLOB` | — | Não | Texto JSON | Valores antes da mudança, em JSON |
| `valores_novos` | `CLOB` | — | Não | Texto JSON | Valores depois da mudança, em JSON |
| `anonimizado_em` | `TIMESTAMP WITH TIME ZONE` | — | Não | Data, hora e fuso | Rotina do RNF-6 |

**Restrições:**

- CHECK: autor_tipo = Usuário exige autor_id; Motor de Eventos exige causa_id ou gatilho

### B.4.12 `aviso_saida` (técnica)

Avisos a publicar, gravados na mesma transação da mudança (ADR-0016); origem = nome do serviço, constante.

| Campo | Tipo | Chave | Obrigatório | Domínio ou valores | Descrição |
|---|---|---|---|---|---|
| `id` | `CHAR(36)` | PK | Sim | UUID | id do envelope |
| `tipo` | `VARCHAR(60)` | — | Sim | Texto | Nome do aviso, em PascalCase, no passado |
| `versao` | `INTEGER` | — | Sim | Inteiro | Versão do formato |
| `ocorrido_em` | `TIMESTAMP WITH TIME ZONE` | — | Sim | Data, hora e fuso | Quando o fato aconteceu |
| `turnaround_id` | `CHAR(36)` | — | Não | Identificador de `turnaround` (Cadastro e Planejamento), sem FK | Turnaround do fato |
| `autor_id` | `CHAR(36)` | — | Não | Identificador de `usuario` (Cadastro e Planejamento), sem FK | Autor do fato |
| `causa_id` | `CHAR(36)` | — | Não | UUID | Registro que causou o aviso |
| `dados` | `CLOB` | — | Sim | Texto JSON | Conteúdo do aviso em JSON |
| `gravado_em` | `TIMESTAMP WITH TIME ZONE` | — | Sim | Data, hora e fuso | Ordem de publicação |
| `publicado_em` | `TIMESTAMP WITH TIME ZONE` | — | Não | Data, hora e fuso | Vazio até a mensageria confirmar |

### B.4.13 `aviso_processado` (técnica)

Avisos já recebidos, para descartar o repetido (ADR-0016).

| Campo | Tipo | Chave | Obrigatório | Domínio ou valores | Descrição |
|---|---|---|---|---|---|
| `aviso_id` | `CHAR(36)` | PK | Sim | UUID | id do envelope recebido |
| `processado_em` | `TIMESTAMP WITH TIME ZONE` | — | Sim | Data, hora e fuso | Quando foi processado |

### B.4.14 `pedido_pendente` (técnica)

Pedido à Execução em Solo gravado antes da chamada e retomado depois de uma queda (ADR-0020; RNF-20).

| Campo | Tipo | Chave | Obrigatório | Domínio ou valores | Descrição |
|---|---|---|---|---|---|
| `id` | `CHAR(36)` | PK | Sim | UUID | — |
| `tipo` | `VARCHAR(30)` | — | Sim | Abertura de exceção, Encerramento de exceção, Reatribuição, Replanejamento, Liberação | — |
| `turnaround_id` | `CHAR(36)` | — | Sim | Identificador de `turnaround` (Cadastro e Planejamento), sem FK | — |
| `registro_id` | `CHAR(36)` | — | Sim | UUID | UUID do registro a criar; chave de idempotência do pedido |
| `autor_id` | `CHAR(36)` | — | Sim | Identificador de `usuario` (Cadastro e Planejamento), sem FK | Autor da ação |
| `horario_acao` | `TIMESTAMP WITH TIME ZONE` | — | Sim | Data, hora e fuso | Horário da ação; na liberação, é o ARDT |
| `dados` | `CLOB` | — | Sim | Texto JSON | Conteúdo do pedido em JSON |
| `situacao` | `VARCHAR(20)` | — | Sim | Pendente, Concluído, Desfeito | — |
| `resolvido_em` | `TIMESTAMP WITH TIME ZONE` | — | Não | Data, hora e fuso | — |
