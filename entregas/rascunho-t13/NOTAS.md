# T13 — notas de trabalho (rascunho; apagar esta pasta antes do PR)

Parada em 15/11/2026, 05:20, com 77% do limite de 5 horas. Tudo está na branch `ra2/t13-diagrama-de-classes`.

## Feito

- Fontes: `especificacao/diagramas/13-classes-{contrato,cadastro,execucao,monitoramento,excecoes}.iuml`.
- Estilo e vistas: `13-classes-estilo.iuml` e 14 vistas `13-classes-*.puml`, geradas por `vistas.py` (nesta pasta; rodar de novo depois de mudar classes).
- Script `scripts/conferir_classes.py`, com 0 problema (sem `--sequencia`).
- Texto `especificacao/13-diagrama-de-classes.md` (rascunho completo).
- Conferências independentes da Execução em Solo e do Exceções e Liberação, nesta pasta: `conferencia-execucao.md` (6 graves, 17 médios, 11 leves) e `conferencia-excecoes.md` (11 graves, 15 médios, 10 leves).

## Retomada em 15/11/2026 (tarde)

- Passos 1 e 2 feitos: correções da EX e da EL aplicadas; script em 0 problema; vistas regeradas.
- Script ganhou: `[0..1]` contra a coluna Obrigatório do Apêndice B (achou 42 no Cadastro e no Monitoramento, já corrigidos); dependência entre serviços só de tela e de cliente para controle (passo 5 feito); contrato cliente × controle; «dto» espelho igual dos dois lados.
- Conferência do Cadastro (scratchpad `conferencia-cadastro.md`: 2 graves, 14 médios, 12 leves) aplicada: RotinaAnonimizacaoUsuarios; plano confirmado reenviado por receberPlano antes de gravar; telas com abrir; UsuarioResumo, NomeUsuario, TokenAcesso; verificarAcesso com acaoDoUsuario; AutenticacaoService com auditoria; métodos do plano e do modelo pelo id do todo; PlanoRepository.buscarComTrava e tarefas não confirmadas; politicaVersao no PlanoConfirmado; Acesso [0..1]; aplicarAobt. Fora do item: #178 (comentário), #192 (UC04, UC05), #205 (versão da política).
- Conferência do Monitoramento (scratchpad `conferencia-monitoramento.md`: 4 graves, 14 médios, 11 leves) aplicada: painel atualizado por alerta, cópia e aviso de checagem; telas recebem as notificações; regra de ordem na CopiaService; trava; RotinaAnonimizacao abstrata com uma subclasse por serviço; MarcoMonitorado; ReplanejamentoView abre a LinhaDoTempoView. Fora do item: #205 (3 itens), #206 (UC31 A4.1), #183 (ADR-0019 × item 12), #178.
- Conferência transversal (scratchpad `conferencia-transversal.md`: 0 graves, 5 médios, 15 leves). Aplicados: M1 (`13-classes-ligacoes.iuml` incluído por último; setas entre serviços agora aparecem), M2, M3, M4 (frase), M5, L3, L9, L11, L12, L14. Fora do item: #205 (ARDT e cópias), #179 (exemplo da ADR-0018).
- **Falta da transversal (leves):** L1 verbos `aplicarX` nas cópias (TurnaroundMonitorado.registrarMarco/mudarEstado, TurnaroundReferencia.registrarProjecao, execucao.atualizarTobtVigente → aplicarTobtVigente; mesmo formato de `aplicarTurnaroundAberto` nos dois consumidores); L2 atributos `- auditoria`/`- publicador` na Execução, Monitoramento e Exceções; L4 classes no plural (MarcosView, AlertasView, IndicadoresView, IndicadoresAderencia); L5 frase em 13.2 sobre nomes do resolver e consultas derivadas; L6 `abrir(...)` em toda tela e `TurnaroundView.abrirTurnaround` → `salvarTurnaround`; L7 frase sobre CompanhiaController → repositório; L8 `Tarefa.conferirResponsavel`; L10 dividir a vista do Motor de Eventos e pôr publicador/consumidor; L13 mover `vistas.py` para `scripts/`; L15 ordem dos pacotes na visão geral.
- Siglas do texto passadas (TOBT, DTO, UC, AIBT, QR Code na primeira ocorrência).
- Decisões novas: gravação pelo todo da composição (Execução em Solo sem MarcoRepository e sem os repositórios de histórico; as partes só consultam); `EncerramentoExcecao` «dto» (UC33 passo 7 mostra o estado de retorno); `PlanoConfirmado`, `TarefaPlanejada` e `PontoPlanejado` também no Cadastro, e o cliente chama `receberPlano`; `AuditoriaService.existeCausa` responde o `consultarPedido`.

## Próximos passos, em ordem

1. Aplicar as correções abaixo nas fontes, nos dois serviços de uma vez, porque os achados se cruzam.
2. Rodar `conferir_classes.py` e `vistas.py`.
3. Conferência independente do Cadastro e Planejamento e do Monitoramento (uma de cada vez; medir o consumo entre elas).
4. Conferência transversal: K.3, K.4, K.6, siglas, nomes e contratos entre os serviços.
5. Ajustar o checker para permitir dependência entre serviços só de «boundary» (o site é um só) e de «client» para «control»/«resolver»; desenhar essas dependências.
6. Exportar as figuras (`python scripts/exportar_plantuml.py`, com `PLANTUML_JAR` = `../plantuml-1.2026.0.jar`), conferir a legibilidade e tirar `PedidoPendente` da visão geral.
7. Passar as siglas do texto (Y.5): falta o TOBT na primeira ocorrência (13.5.6), e conferir REST, UC, RNF e DTO.
8. Registrar as pendências (seção "Fora do item 13" abaixo), atualizar o CHANGELOG e abrir o PR com `Closes #145` e os rótulos `ra2` e `item-13`, e mover o card.

## Decisões já tomadas para os achados

Siglas: EX = conferencia-execucao.md; EL = conferencia-excecoes.md.

**Contrato entre os serviços**
- EX13, EX14, EX15, EL15: «dto» `TarefaResumo` também na Execução em Solo, com os mesmos campos dos dois lados, mais `turnaroundId` e `matricula`. Ele é usado em `listarNaoIniciadas`, `alterarJanela`, `alterarDependencias`, `acionarSobDemanda`, `SituacaoTurnaround`, `listarTarefas`, `consultarTarefa` e nos pendentes. Os pendentes ficam com um nome só dos dois lados: `listarTarefasPendentesDoOperador` e `listarTarefasPendentesDaEquipe`, que devolvem `List<TarefaResumo>`; o `TarefaPendente` do Cadastro sai.
- EX15: «dto» `PlanoConfirmado` na Execução em Solo, com voos, matrícula, posição, política, tarefas com `sobDemanda` e `acionada`, dependências e pontos. A Execução em Solo monta o `Turnaround` e define os estados.
- EX16: receber o plano depois do AIBT chama `propagarChegada`, e o caso vai como pendência (O7).
- EL3, EX18, EX19, EL16: `consultarPedido(registroId: UUID): Boolean` no `TurnaroundController` da Execução em Solo e no cliente. Todo pedido leva a chave (`liberacaoId` em `liberar`) e o `horarioAcao` (reatribuir e replanejar). A auditoria ganha `causaId` em `AuditoriaService.registrar`.
- EL14, EX26: «dto» `MudancaEstado` (estadoAnterior, estadoNovo), devolvido por `aplicarExcecao` e `sairDeExcecao` nos dois lados. `aplicarExcecao` recebe `tarefaId`, e a Execução em Solo confere a tarefa (EX6).
- EX6, EL8: `listarTarefas(turnaroundId): List<TarefaResumo>` na Execução em Solo, no cliente e no `ExcecaoController`.
- EL19: `consultarTarefa(tarefaId): TarefaResumo` nos dois lados e no `ReatribuicaoController`.
- EL21, EX20: `listarCatalogoSobDemanda(turnaroundId): List<TarefaResumo>` nos dois lados.
- EL10: `listarOperadoresAtivos(equipeId)` no cliente do Exceções e Liberação e no `ReplanejamentoController`; a Execução em Solo repassa ao Cadastro.
- EL11, EX23, EX33: o `CadastroCliente` devolve o «dto» `OperadorAtivo` (usuarioId, nome), sem gravar o nome. O `EquipeController.listarOperadoresAtivos` do Cadastro devolve `List<OperadorAtivo>` (dto do Cadastro). `OperadorDisponivel` ganha `nome` nos dois lados, e a Execução em Solo devolve a lista já ordenada pela RN4 do UC36.
- EL27, EX30: o mesmo nome nos dois lados (`operadorNovoId`), e o retorno de `reatribuir` é documentado como o operador anterior.
- EL18: `SituacaoTurnaround` ganha `matricula`, `vooChegada`, `vooPartida` e `posicao`, e o `TurnaroundLiberavel` copia esses dados. O filtro e a ordem da lista do UC32 viram pendência do UC32 (EL-O5).

**Exceções e Liberação**
- EL1: `ExcecaoService` ganha `execucao: ExecucaoEmSoloCliente`. O padrão de todo pedido: `PedidoService.registrar`, depois o cliente, depois `concluir` ou `desfazer`, na mesma transação do aviso.
- EL2: reatribuir e replanejar recebem `turnaroundId` (tela, controle e serviço), e os dois serviços ganham `TurnaroundReferenciaRepository`, com trava.
- EL4: `atualizar(turnaroundId, tobtNovo, solicitacaoId)`, que recusa quando a solicitação já foi encerrada. `abrirSolicitacao` e `consultarSolicitacao` passam a usar o `turnaroundId`.
- EL5: `AtualizacaoTobtService` usa `LiberacaoRepository` e recusa a atualização depois de "Liberado".
- EL6: novo «websocket» `CoordenadorNotificador` no Exceções e Liberação (ADR-0020 diz que o WebSocket é nativo "se os itens 13 e 14 pedirem"), com `notificarSolicitacao` e `retirarSolicitacao`. Registrar na #183.
- EL7: `RegistroAcaoAlertaView.abrir(alertaId)`; as dependências `..> monitoramento.AlertaController` e `monitoramento.AlertasView ..> excecoes.RegistroAcaoAlertaView`.
- EL12, EL13: a ação sobre o alerta vai junto da ação. Abrir, reatribuir, replanejar e atualizar o TOBT recebem `alertaId` (opcional), e o serviço confere que não há `AcaoAlerta` para o alerta antes do pedido e grava a `AcaoAlerta` na mesma transação. Sai o `AcaoAlertaController`, e o `AcaoAlertaService` passa a ser chamado pelos outros serviços.
- EL9, EL20: `ReplanejamentoView ..> monitoramento.PainelResolver` e `+ exibirResultado(turnaroundId)`.
- EL17: `consultarCondicoes(turnaroundId, companhiaId)`.
- EL22: `consultarTobt(turnaroundId): TurnaroundReferencia`.
- EL23: o 13.1 passa a citar `AtualizacaoTobtService.avaliarProjecao` como parte do Motor de Eventos; registrar na #183.
- EL24: `codigoVersao` em `abrir` (tela, controle e serviço).
- EL25: `comum.RotinaAnonimizacao` «scheduler», em todos os serviços (RNF-6).
- EL26: UC36 E2.1 (a lista se atualiza sozinha) fica sem canal; vira pendência do UC36.
- EL28: métodos da `ExcecaoView`: abrirFormulario, buscarCodigo, confirmarAbertura, selecionarExcecao e encerrarExcecao.
- EL29: `contarAbertas(turnaroundId): Integer`.
- EL30: nota sobre a trava em `encerrar` e `abrir`.
- EL31: `CondicoesLiberacao` vira `SituacaoLiberacao`.
- EL32: associações com multiplicidade nos DTOs.
- EL33 e EL34: vistas e comentário de cabeçalho.
- EL36: `TurnaroundReferenciaService.aplicarTurnaroundAberto` recebe campos e lê a configuração do RNF-21.

**Execução em Solo**
- EX1: `MarcoService.registrarMarcos(turnaround, tarefa, registro)`, com `AuditoriaService` (EX21).
- EX2: `PropagacaoService.propagarRegistro(turnaround, tarefa, registro)`, com o turnaround travado pelo chamador.
- EX3: `AtribuicaoService` e `LeituraQrCodeService` ganham `TurnaroundRepository`, travam e conferem `aceitaRegistros`.
- EX4: `LeituraQrCodeView ..> FilaRegistrosSemConexao`.
- EX5: métodos de exibição nas telas (ChegadaView.abrir, CorrecaoChegadaView.abrir, ListaTarefasView.carregar, LeituraQrCodeView.abrir, SaidaPosicaoView.abrir) e as ligações.
- EX7: tirar o `requisicaoId` de `registrarChegada` (o marco não tem esse campo; a unicidade resolve).
- EX8: o «dto» `TarefaDoOperador` (tarefa, matrícula, posição, estado do turnaround) em `listarDoOperador` e `consultar`.
- EX9: passar o `equipeId` ao serviço e conferi-lo em `conferirResponsavel`.
- EX10: `FilaRegistrosSemConexao.guardar(usuarioId, tarefaId, tipo, dados, horarioAcao, requisicaoId)` e `enviarPendentes(usuarioId)`.
- EX11: `TarefaView.pausar(tarefaId, justificativa, impedimento, codigoVersao, codigoAtraso)`, e `impedimento` também no controle e no serviço.
- EX12: `registrarLeitura` devolve `PontoConfirmacao`, e `buscarPorIdentificador(turnaroundId, identificador): List<PontoConfirmacao>`.
- EX17: `liberar(turnaroundId, liberacaoId, ardt, autorId)`.
- EX22: `CodigoAtrasoService.carregarVersao(..., autorId)` e `CodigoAtrasoController.carregarVersao`. O ator vira dúvida para o grupo (EX-O8).
- EX24: `Marco "0..2"`.
- EX25: marcar `[0..1]` em todos os atributos opcionais (vale para os quatro serviços).
- EX27: regra única. O agregado grava as partes, e os repositórios das partes ficam só para consulta. Escrever no 13.2.
- EX28, EX29: `registrarMudanca()` privado; `ehEmbarque()`, `ehDesembarque()` e `ehAbastecimento()`.
- EX30: `buscarMarco(tipo)`, `buscarCodigo(sigla)` e `ListaTarefasNotificador ..> ListaTarefasView`.
- EX31: já explicado no texto 13.2 (valores com acento, constante sem acento no código).
- EX32: `atualizarTobtVigente(turnaroundId, tobtVigente, ocorridoEm)`.

## Fora do item 13: registrado em 15/11 (#151, #178, #179, #183 por comentário; #205 item 12; #206 área D UC32/UC36; #207 dúvidas do grupo)

- **#151, T14-D:** o UC32 de exemplo não bate com as classes (EL-O1, EX-O1).
- **#183:** o Exceções e Liberação compara a projeção com o TOBT; o Monitoramento publica toda projeção; e o canal da solicitação passa a ser o `CoordenadorNotificador` (EL-O7).
- **#178:** `Acesso.companhiaId` (EL-O4); a troca de equipe com tarefa pendente (EX-O11); a desativação com item de catálogo (EX-O6).
- **#179:** QR Code único só por tarefa (EX-O2); transições não definidas (EX-O7); desempate alfabético (EX-O12); TOBT vigente inicial na Execução em Solo (EX-O5).
- **Issue nova "Ajustes do RA1" ou do item 12:** `estado_turnaround_anterior` e `estado_anterior` com o domínio dos estados (EL-O2, EX-O4); `tarefa.tipo_atividade` com o domínio da lista (EX-O3); justificativa da cópia de `companhia_id` (EL-O3); pedido pendente também na reatribuição e no replanejamento (EL-O6); filtro da lista do UC32 (EL-O5); UC36 E2.1 (EL26).
- **Dúvidas para o grupo:** o ator da carga da tabela da ANAC (EX-O8) e como um serviço se identifica para outro (EX-O10).
