"""Gera as vistas do diagrama de classes (item 13): especificacao/diagramas/13-classes-*.puml.

As classes ficam nas fontes 13-classes-*.iuml; cada vista inclui todas e restaura só as da sua lista.
Rode de novo depois de criar, renomear ou apagar uma classe; o script avisa a classe que ficou fora de toda vista.
Uso: python scripts/gerar_vistas_classes.py
"""
import re
from pathlib import Path

D = Path(__file__).resolve().parent.parent / 'especificacao' / 'diagramas'
classes = {}
for arq in sorted(D.glob('13-classes-*.iuml')):
    ns = None
    for t in arq.read_text(encoding='utf-8').splitlines():
        t = t.strip()
        m = re.match(r'namespace (\w+) \{', t)
        if m: ns = m.group(1)
        m = re.match(r'(?:abstract class|class|interface|enum) (\w+)(?: <<(\w+)>>)?', t)
        if m and ns: classes[f'{ns}.{m.group(1)}'] = m.group(2) or ''

def de(ns, *est):
    return [k for k, v in classes.items() if k.startswith(ns + '.') and v in est]

VISTAS = {
  'visao-geral': ('Visão geral das classes de negócio', [k for k, v in classes.items() if v == 'entity' and k.split('.')[0] not in ('comum',) and k != 'excecoes.PedidoPendente'], 'todas', 'left to right direction\n'
                  "' pacotes na ordem da seção 13.4 e do ciclo do turnaround\n"
                  'cadastro.Plano -[hidden]down- execucao.Turnaround\n'
                  'execucao.Turnaround -[hidden]down- monitoramento.TurnaroundMonitorado\n'
                  'monitoramento.TurnaroundMonitorado -[hidden]down- excecoes.TurnaroundReferencia'),
  'negocio-cadastro': ('Classes de negócio — Cadastro e Planejamento', de('cadastro', 'entity', 'enumeration'), None, ''),
  'negocio-execucao': ('Classes de negócio — Execução em Solo', de('execucao', 'entity', 'enumeration'), None, ''),
  'negocio-monitoramento': ('Classes de negócio — Monitoramento', de('monitoramento', 'entity', 'enumeration'), None, ''),
  'negocio-excecoes': ('Classes de negócio — Exceções e Liberação', [k for k in de('excecoes', 'entity', 'enumeration') if 'Pedido' not in k], None, ''),
  'contrato': ('Contrato entre os serviços e infraestrutura comum', [k for k in classes if k.split('.')[0] in ('contrato', 'comum')] +
               ['cadastro.ConsumidorAvisosCadastro', 'execucao.ConsumidorAvisosExecucao', 'monitoramento.ConsumidorAvisosMonitoramento', 'excecoes.ConsumidorAvisosExcecoes',
                'cadastro.RotinaAnonimizacaoCadastro', 'execucao.RotinaAnonimizacaoExecucao', 'monitoramento.RotinaAnonimizacaoMonitoramento', 'excecoes.RotinaAnonimizacaoExcecoes',
               ], None, ''),
  'pedidos-pendentes': ('Pedidos pendentes do Exceções e Liberação à Execução em Solo',
               ['excecoes.RetomadaPedidos', 'excecoes.PedidoService', 'excecoes.PedidoPendenteRepository', 'excecoes.PedidoPendente',
                'excecoes.TipoPedido', 'excecoes.SituacaoPedido'], None, ''),
}
def tec(nome, titulo, lista):
    VISTAS[nome] = (titulo, lista, 'entidades', '')

tec('tecnica-acesso', 'Autenticação, usuários e equipes', [
  'contrato.PortaDeEntrada', 'contrato.Acesso',
  'cadastro.AutenticacaoView', 'cadastro.UsuarioView', 'cadastro.EquipeView',
  'cadastro.AcessoController', 'cadastro.AutenticacaoController', 'cadastro.UsuarioController', 'cadastro.EquipeController',
  'cadastro.AutenticacaoService', 'cadastro.UsuarioService', 'cadastro.EquipeService',
  'cadastro.UsuarioRepository', 'cadastro.FalhaLoginRepository', 'cadastro.SessaoRepository', 'cadastro.EquipeRepository',
  'cadastro.ExecucaoEmSoloCliente', 'cadastro.TarefaResumo', 'cadastro.OperadorAtivo',
  'cadastro.UsuarioResumo', 'cadastro.NomeUsuario', 'cadastro.TokenAcesso', 'cadastro.RotinaAnonimizacaoCadastro', 'cadastro.CompanhiaController',
  'execucao.TarefaController', 'execucao.CadastroCliente', 'execucao.OperadorAtivo'])
tec('tecnica-planejamento', 'Abertura e planejamento do turnaround', [
  'cadastro.TurnaroundView', 'cadastro.ModeloTarefaView', 'cadastro.PlanoView', 'cadastro.PoliticaAbastecimentoView',
  'cadastro.TurnaroundController', 'cadastro.CompanhiaController', 'cadastro.ModeloTarefaController', 'cadastro.PlanoController', 'cadastro.PoliticaAbastecimentoController',
  'cadastro.TurnaroundService', 'cadastro.ModeloTarefaService', 'cadastro.PlanoService', 'cadastro.PoliticaAbastecimentoService',
  'cadastro.TurnaroundRepository', 'cadastro.CompanhiaRepository', 'cadastro.ModeloTarefaRepository', 'cadastro.PlanoRepository', 'cadastro.PoliticaAbastecimentoRepository',
  'cadastro.ConsumidorAvisosCadastro', 'comum.PublicadorAvisos', 'cadastro.ExecucaoEmSoloCliente', 'cadastro.PlanoConfirmado', 'cadastro.TarefaPlanejada', 'cadastro.PontoPlanejado',
  'cadastro.SituacaoPlano', 'cadastro.RetomadaConfirmacaoPlano',
  'execucao.TurnaroundController', 'execucao.ChegadaController', 'execucao.TurnaroundService', 'execucao.PlanoConfirmado',
  'execucao.TarefaPlanejada', 'execucao.PontoPlanejado'])
tec('tecnica-execucao', 'Execução das tarefas no solo', [
  'execucao.ChegadaView', 'execucao.CorrecaoChegadaView', 'execucao.ListaTarefasView', 'execucao.TarefaView', 'execucao.LeituraQrCodeView', 'execucao.MarcoView', 'execucao.FilaRegistrosSemConexao',
  'execucao.ChegadaController', 'execucao.TarefaController', 'execucao.LeituraQrCodeController', 'execucao.CodigoAtrasoController',
  'execucao.ChegadaService', 'execucao.TarefaService', 'execucao.LeituraQrCodeService', 'execucao.CodigoAtrasoService', 'execucao.CargaTabelaCodigoAtraso',
  'execucao.TurnaroundRepository', 'execucao.TarefaRepository', 'execucao.RegistroTarefaRepository', 'execucao.CorrecaoAibtRepository',
  'execucao.PontoConfirmacaoRepository', 'execucao.LeituraQrCodeRepository', 'execucao.CodigoAtrasoRepository', 'execucao.ListaTarefasNotificador',
  'execucao.TurnaroundController', 'execucao.TarefaDoOperador'])
tec('tecnica-marcos-propagacao', 'Motor de Eventos na Execução em Solo: marcos e propagação', [
  'execucao.ChegadaService', 'execucao.TarefaService', 'execucao.TurnaroundService', 'execucao.ReplanejamentoService',
  'execucao.MarcoService', 'execucao.PropagacaoService', 'execucao.TurnaroundRepository', 'execucao.ListaTarefasNotificador',
  'execucao.ConsumidorAvisosExecucao', 'comum.ConsumidorAvisos', 'comum.PublicadorAvisos'])
tec('tecnica-recalculo-alertas', 'Motor de Eventos no Monitoramento: recálculo e alertas', [
  'comum.PublicadorAvisos', 'comum.ConsumidorAvisos',
  'monitoramento.ConsumidorAvisosMonitoramento', 'monitoramento.CopiaService', 'monitoramento.AgendadorMinuto',
  'monitoramento.RecalculoService', 'monitoramento.AlertaService', 'monitoramento.AvisoChecagemService',
  'monitoramento.TurnaroundMonitoradoRepository', 'monitoramento.TarefaMonitoradaRepository', 'monitoramento.ProjecaoRepository',
  'monitoramento.CaminhoCriticoRepository', 'monitoramento.AlertaRepository', 'monitoramento.AvisoChecagemRepository',
  'monitoramento.AtualizacaoTobtMonitoradaRepository', 'monitoramento.PainelNotificador', 'monitoramento.PainelService',
  'excecoes.ConsumidorAvisosExcecoes', 'excecoes.AtualizacaoTobtService'])
tec('tecnica-acompanhamento', 'Painel, linha do tempo, alertas, checagem e indicadores', [
  'monitoramento.PainelView', 'monitoramento.LinhaDoTempoView', 'monitoramento.ListaAlertasView', 'monitoramento.AvisoChecagemView', 'monitoramento.IndicadorView',
  'monitoramento.PainelResolver', 'monitoramento.AlertaController', 'monitoramento.AvisoChecagemController', 'monitoramento.IndicadorController',
  'monitoramento.PainelService', 'monitoramento.AlertaService', 'monitoramento.AvisoChecagemService', 'monitoramento.IndicadorService',
  'monitoramento.Painel', 'monitoramento.LinhaPainel', 'monitoramento.LinhaDoTempo', 'monitoramento.RelatorioAderencia', 'monitoramento.Indicador',
  'monitoramento.PainelNotificador', 'monitoramento.TurnaroundMonitoradoRepository', 'monitoramento.ProjecaoRepository',
  'monitoramento.CaminhoCriticoRepository', 'monitoramento.AlertaRepository', 'monitoramento.AvisoChecagemRepository',
  'monitoramento.AtualizacaoTobtMonitoradaRepository', 'excecoes.RegistroAcaoAlertaView',
  'cadastro.UsuarioController', 'cadastro.EquipeController'])
tec('tecnica-excecoes', 'Exceções, atualização do TOBT e ação sobre o alerta', [
  'excecoes.ExcecaoView', 'excecoes.RegistroAcaoAlertaView', 'excecoes.AtualizacaoTobtView',
  'excecoes.ExcecaoController', 'excecoes.AtualizacaoTobtController', 'excecoes.CoordenadorNotificador',
  'excecoes.EncerramentoExcecao', 'excecoes.MudancaEstado', 'excecoes.LiberacaoRepository',
  'monitoramento.ListaAlertasView', 'monitoramento.AlertaController',
  'excecoes.ExcecaoService', 'excecoes.AcaoAlertaService', 'excecoes.AtualizacaoTobtService', 'excecoes.PedidoService',
  'excecoes.ExcecaoRepository', 'excecoes.TurnaroundReferenciaRepository', 'excecoes.CodigoAtrasoRepository', 'excecoes.AcaoAlertaRepository',
  'excecoes.SolicitacaoAtualizacaoTobtRepository', 'excecoes.AtualizacaoTobtRepository', 'excecoes.ExecucaoEmSoloCliente',
  'execucao.TurnaroundController', 'execucao.TurnaroundService', 'execucao.MudancaEstado',
  'cadastro.UsuarioController'])
tec('tecnica-reatribuicao-replanejamento', 'Reatribuição e replanejamento', [
  'excecoes.ReatribuicaoView', 'excecoes.ReplanejamentoView',
  'excecoes.ReatribuicaoController', 'excecoes.ReplanejamentoController',
  'excecoes.ReatribuicaoService', 'excecoes.ReplanejamentoService', 'excecoes.PedidoService',
  'excecoes.ReatribuicaoRepository', 'excecoes.ReplanejamentoRepository', 'excecoes.ExecucaoEmSoloCliente',
  'excecoes.OperadorDisponivel', 'excecoes.OperadorAtivo', 'excecoes.TarefaResumo', 'excecoes.TurnaroundReferenciaRepository',
  'excecoes.AcaoAlertaService', 'monitoramento.LinhaDoTempoView',
  'execucao.AtribuicaoController', 'execucao.ReplanejamentoController', 'execucao.AtribuicaoService', 'execucao.ReplanejamentoService',
  'execucao.CadastroCliente', 'execucao.OperadorDisponivel', 'execucao.OperadorAtivo', 'execucao.TarefaResumo',
  'cadastro.EquipeController'])
tec('tecnica-liberacao', 'Liberação e saída da posição', [
  'excecoes.LiberacaoView', 'excecoes.LiberacaoController', 'excecoes.LiberacaoService', 'excecoes.PedidoService',
  'excecoes.LiberacaoRepository', 'excecoes.ExcecaoRepository', 'excecoes.TurnaroundReferenciaRepository',
  'excecoes.ExecucaoEmSoloCliente', 'excecoes.SituacaoLiberacao', 'excecoes.TurnaroundLiberavel', 'excecoes.SituacaoTurnaround',
  'excecoes.TarefaResumo', 'excecoes.AtualizacaoTobtService',
  'execucao.SaidaPosicaoView', 'execucao.TurnaroundController', 'execucao.TurnaroundService', 'execucao.TurnaroundRepository', 'execucao.SituacaoTurnaround',
  'comum.PublicadorAvisos', 'excecoes.ConsumidorAvisosExcecoes', 'excecoes.TurnaroundReferenciaService',
  'cadastro.UsuarioController'])

# Disposição de cada vista, escolhida para a figura caber na página do PDF sem linhas amontoadas
# (medida por scripts/medir_figuras_pdf.py). "empilhar" põe a segunda classe uma camada abaixo da primeira,
# por uma ligação oculta, para quebrar uma linha larga em duas.
DISPOSICAO = {}
def disp(nome, direcao='', linha='', empilhar=()):
    DISPOSICAO[nome] = ([direcao] if direcao else []) + ([f'skinparam linetype {linha}'] if linha else []) +                        [f'{a} -[hidden]down- {b}' for a, b in empilhar]
disp('tecnica-execucao', empilhar=[
  ('execucao.TurnaroundRepository', 'execucao.CorrecaoAibtRepository'),
  ('execucao.LeituraQrCodeRepository', 'execucao.PontoConfirmacaoRepository'),
  ('execucao.RegistroTarefaRepository', 'execucao.TarefaDoOperador'),
  ('execucao.ListaTarefasNotificador', 'execucao.CodigoAtrasoRepository')])
disp('tecnica-acesso', 'left to right direction')
disp('tecnica-planejamento', 'left to right direction')
disp('tecnica-marcos-propagacao', empilhar=[('execucao.ListaTarefasNotificador', 'comum.PublicadorAvisos'), ('execucao.ListaTarefasNotificador', 'comum.ConsumidorAvisos')])
disp('tecnica-recalculo-alertas', 'left to right direction')
disp('tecnica-acompanhamento', empilhar=[
  ('monitoramento.CaminhoCriticoRepository', 'monitoramento.Painel'), ('monitoramento.ProjecaoRepository', 'monitoramento.LinhaDoTempo'),
  ('monitoramento.AtualizacaoTobtMonitoradaRepository', 'monitoramento.RelatorioAderencia'),
  ('monitoramento.AlertaRepository', 'excecoes.RegistroAcaoAlertaView')])
disp('tecnica-excecoes', 'left to right direction')
disp('tecnica-reatribuicao-replanejamento', 'left to right direction')
disp('contrato', 'left to right direction')
disp('negocio-execucao', 'left to right direction', 'ortho')
disp('negocio-monitoramento', 'left to right direction')

usadas = set()
for nome, (titulo, lista, ocultar, extra) in VISTAS.items():
    faltam = [x for x in lista if x not in classes]
    assert not faltam, (nome, faltam)
    usadas |= set(lista)
    ns = sorted({x.split('.')[0] for x in lista})
    linhas = ['@startuml', f"' Item 13 — {titulo}. Vista gerada a partir das fontes 13-classes-*.iuml.",
              '!include 13-classes-estilo.iuml']
    if extra: linhas.append(extra)
    linhas += DISPOSICAO.get(nome, [])
    linhas += [f'restore {n}' for n in ns] + [f'restore {x}' for x in lista]
    if ocultar == 'todas':
        linhas.append('hide members')
    elif ocultar == 'entidades':
        linhas += [f'hide {x} members' for x in lista if classes[x] == 'entity']
    linhas.append('@enduml')
    (D / f'13-classes-{nome}.puml').write_text('\n'.join(linhas) + '\n', encoding='utf-8')
sem = sorted(k for k, v in classes.items() if k not in usadas)
print('vistas:', len(VISTAS), '| classes fora de vista:', sem)
