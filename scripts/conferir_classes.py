"""Confere o diagrama de classes do item 13 (fontes especificacao/diagramas/13-classes-*.iuml).

O que confere (critérios de entregas/ra2-criterios-de-aceite.md, seção 3.2):
  C13.1  todo membro tem visibilidade (- # +); enumerações só têm valores
  C13.2  todo atributo segue `nome: Tipo`, com tipo neutro (B1) ou classe/enumeração do diagrama
  C13.3  todo método segue `nome(p: Tipo, ...): Retorno`
  C13.5  nenhum atributo, parâmetro ou retorno de um serviço usa classe de outro serviço (entre serviços, só UUID);
         todo atributo que aponta para outra classe de negócio do serviço tem a linha de associação desenhada;
         entre serviços, só a dependência de tela para tela ou controle (o site é um só) e de «client» para o
         controle do outro serviço; todo método de um «client» existe, com os mesmos parâmetros e retorno, num
         controle ligado a ele; o mesmo «dto» declarado em dois serviços tem os mesmos campos
  C13.6  toda tabela de negócio do Apêndice B tem classe no serviço, com um atributo por campo e tipo compatível;
         e, no outro sentido, toda entidade de serviço tem tabela, e todo atributo dela tem campo (ou é a lista das
         partes que apontam para ela);
         a chave estrangeira vira atributo do tipo da classe (sem o _id) ou a lista na classe do todo (composição);
         as tabelas associativas de dependência viram a lista `predecessoras`; o atributo de campo opcional
         (Obrigatório = Não) tem [0..1], e o de campo obrigatório não tem
  C13.7  EstadoTurnaround, EstadoTarefa e Perfil têm exatamente os valores do CONTEXT.md e do Apêndice B; toda
         enumeração usada por um atributo que vem de uma tabela tem os valores do domínio do campo
  C13.8  (com --sequencia) toda mensagem dos diagramas de sequência 14-sequencia-*.puml que chama `metodo(...)`
         numa classe do item 13 existe nessa classe; mensagens a participantes que não são classes são ignoradas
  C13.9  classes em PascalCase, sem acento

Uso: python scripts/conferir_classes.py [--sequencia]
Sai com código 1 se houver problema.
"""
import re, sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
DIAG = RAIZ / 'especificacao' / 'diagramas'
SERVICOS = {'cadastro': 'Cadastro e Planejamento', 'execucao': 'Execução em Solo',
            'monitoramento': 'Monitoramento', 'excecoes': 'Exceções e Liberação'}
COMPARTILHADOS = ('contrato', 'comum')
PRIMITIVOS = {'String', 'Integer', 'Boolean', 'Date', 'DateTime', 'Real', 'UUID'}
TECNICAS = {'registro_auditoria': 'comum.RegistroAuditoria', 'aviso_saida': 'comum.AvisoSaida',
            'aviso_processado': 'comum.AvisoProcessado', 'pedido_pendente': 'excecoes.PedidoPendente'}
SQL_UML = [('CHAR(36)', {'UUID'}), ('VARCHAR', {'String'}), ('CHAR', {'String'}), ('CLOB', {'String'}),
           ('INTEGER', {'Integer'}), ('BOOLEAN', {'Boolean'}), ('DATE', {'Date'}), ('TIMESTAMP', {'DateTime'})]

problemas = []
def erro(msg):
    if msg not in problemas: problemas.append(msg)


def ler_classes():
    """{ 'ns.Classe': {'ns', 'nome', 'tipo', 'estereotipo', 'atributos': [(vis, nome, tipo)], 'metodos': [...],
    'valores': [...]} } e a lista de relações (origem, destino, seta, rótulo)."""
    classes, relacoes = {}, []
    for arq in sorted(DIAG.glob('13-classes-*.iuml')):
        ns, atual = None, None
        for n, linha in enumerate(arq.read_text(encoding='utf-8').splitlines(), 1):
            t = linha.strip()
            if not t or t.startswith("'"): continue
            m = re.match(r'namespace (\w+) \{', t)
            if m: ns = m.group(1); continue
            m = re.match(r'(abstract class|class|interface|enum) (\w+)(?: <<(\w+)>>)? \{$', t)
            if m:
                chave = f'{ns}.{m.group(2)}'
                if chave in classes: erro(f'{arq.name}:{n}: classe repetida {chave}')
                atual = classes[chave] = {'ns': ns, 'nome': m.group(2), 'tipo': m.group(1), 'est': m.group(3) or '',
                                          'atributos': [], 'metodos': [], 'valores': [], 'arq': arq.name, 'linha': n}
                continue
            if t == '}':
                if atual: atual = None
                else: ns = None
                continue
            if atual:
                if atual['tipo'] == 'enum': atual['valores'].append(t); continue
                m = re.match(r'([-#+])\s*(\{static\}\s*|\{abstract\}\s*)?(\w+)\((.*)\):\s*(.+)$', t)
                if m:
                    params = [p.strip() for p in re.split(r',\s*(?![^<]*>)', m.group(4)) if p.strip()]
                    atual['metodos'].append((m.group(1), m.group(3), params, m.group(5).strip(), n)); continue
                m = re.match(r'([-#+])\s*(\w+):\s*(.+)$', t)
                if m: atual['atributos'].append((m.group(1), m.group(2), m.group(3).strip(), n)); continue
                erro(f'{arq.name}:{n}: membro fora do formato (C13.1 a C13.3): {t}')
                continue
            # [norank] só muda a disposição da figura (a seta não define a camada), não a relação
            m = re.match(r'([\w.]+)\s*(?:"([^"]*)")?\s*([.\-*o<|]+[.\->|*o]*)\s*(?:"([^"]*)")?\s*([\w.]+)(?:\s*:\s*(\w+))?$', t.replace('[norank]', ''))
            if m:
                relacoes.append((m.group(1), m.group(5), m.group(3), m.group(6), m.group(2), m.group(4), arq.name, n))
            elif ns:
                erro(f'{arq.name}:{n}: linha não reconhecida: {t}')
    return classes, relacoes


def tipos_usados(texto):
    return set(re.findall(r'[A-Za-z_]\w*', texto.replace('List<', ' ').replace('>', ' '))) - {'List'}


def resolver(nome, ns, classes):
    for cand in (f'{ns}.{nome}', f'contrato.{nome}', f'comum.{nome}'):
        if cand in classes: return cand
    return None


def conferir_tipos(classes):
    for chave, c in classes.items():
        if not re.fullmatch(r'[A-Z][A-Za-z0-9]*', c['nome']): erro(f'{chave}: nome fora do PascalCase sem acento (C13.9)')
        def conferir(texto, onde):
            limpo = re.sub(r'\s*\[[0-9.*]+\]$', '', texto)
            for t in tipos_usados(limpo):
                if t in PRIMITIVOS or t == 'void': continue
                alvo = resolver(t, c['ns'], classes)
                if not alvo:
                    outro = [k for k in classes if k.endswith('.' + t)]
                    msg = f'usa {outro[0]}, de outro serviço (C13.5)' if outro else f'tipo desconhecido "{t}" (C13.2)'
                    erro(f'{chave}.{onde}: {msg}')
        for vis, nome, tipo, n in c['atributos']: conferir(tipo, nome)
        for vis, nome, params, ret, n in c['metodos']:
            for p in params:
                m = re.match(r'(\w+):\s*(.+)$', p)
                if not m: erro(f'{chave}.{nome}(): parâmetro sem tipo "{p}" (C13.3)'); continue
                conferir(m.group(2), f'{nome}({m.group(1)})')
            conferir(ret, f'{nome}() retorno')


def conferir_associacoes(classes, relacoes):
    ligadas = {(a, b, r) for a, b, s, r, *_ in relacoes} | {(b, a, r) for a, b, s, r, *_ in relacoes}
    for chave, c in classes.items():
        if c['est'] not in ('entity', 'dto'): continue
        for vis, nome, tipo, n in c['atributos']:
            t = re.sub(r'\s*\[[0-9.*]+\]$', '', tipo).replace('List<', '').replace('>', '')
            alvo = resolver(t, c['ns'], classes)
            if alvo and alvo.split('.')[0] == c['ns'] and classes[alvo]['est'] == 'entity' and c['est'] == 'entity':
                if (chave, alvo, nome) not in ligadas:
                    erro(f'{chave}.{nome}: aponta para {alvo} sem a linha de associação com o rótulo "{nome}" (C13.5)')
    for a, b, seta, rotulo, m1, m2, arq, n in relacoes:
        for x in (a, b):
            if x not in classes: erro(f'{arq}:{n}: relação com classe inexistente {x}')
        sa, sb = a.split('.')[0], b.split('.')[0]
        if sa in SERVICOS and sb in SERVICOS and sa != sb:
            ea, eb = classes.get(a, {}).get('est'), classes.get(b, {}).get('est')
            if not (seta == '..>' and ((ea == 'boundary' and eb in ('boundary', 'control', 'resolver')) or
                                       (ea == 'client' and eb in ('control', 'resolver')))):
                erro(f'{arq}:{n}: relação entre serviços {a} e {b} (C13.5; só tela → tela/controle e cliente → controle)')
        if '--' in seta and '..' not in seta and not (m1 or m2) and classes.get(a, {}).get('est') == 'entity':
            erro(f'{arq}:{n}: associação sem multiplicidade {a} — {b} (C13.5)')


def assinatura(params):
    return [re.sub(r'\s+', '', p) for p in params if not p.startswith('acesso:')]


def conferir_contratos(classes, relacoes):
    """C13.5: cada método de um «client» existe, com os mesmos parâmetros e o mesmo retorno, num controle do outro
    serviço ligado a ele por dependência; e todo «client» tem essa ligação."""
    for chave, c in classes.items():
        if c['est'] != 'client': continue
        alvos = [b for a, b, seta, *_ in relacoes if a == chave and classes.get(b, {}).get('est') in ('control', 'resolver')
                 and b.split('.')[0] != c['ns']]
        if not alvos: erro(f'{chave}: cliente sem dependência para o controle do outro serviço (C13.5)'); continue
        for vis, nome, params, ret, n in c['metodos']:
            cands = [(b, m) for b in alvos for m in classes[b]['metodos'] if m[1] == nome]
            if not cands: erro(f'{chave}.{nome}(): nenhum controle ligado ({", ".join(alvos)}) atende o pedido (C13.5)'); continue
            if not any(assinatura(m[2]) == assinatura(params) and m[3] == ret for b, m in cands):
                b, m = cands[0]
                erro(f'{chave}.{nome}({", ".join(params)}): {ret} ≠ {b}.{nome}({", ".join(m[2])}): {m[3]} (C13.5)')


def conferir_dtos_espelho(classes):
    """C13.5: o mesmo dado de troca, declarado nos dois serviços, tem os mesmos campos e tipos dos dois lados."""
    por_nome = {}
    for chave, c in classes.items():
        if c['est'] == 'dto' and c['ns'] in SERVICOS: por_nome.setdefault(c['nome'], []).append(chave)
    for nome, chaves in por_nome.items():
        base = [(a[1], a[2]) for a in classes[chaves[0]]['atributos']]
        for outra in chaves[1:]:
            if [(a[1], a[2]) for a in classes[outra]['atributos']] != base:
                erro(f'{chaves[0]} e {outra}: o mesmo dado de troca com campos diferentes (C13.5)')


def camel(snake):
    p = snake.split('_')
    return p[0] + ''.join(x.capitalize() for x in p[1:])


def pascal(snake): return ''.join(x.capitalize() for x in snake.split('_'))


def ler_apendice_b():
    """{ 'servico': { 'tabela': {'tecnica': bool, 'campos': [(nome, tipo, chave, dominio)]} } }"""
    txt = (RAIZ / 'especificacao' / 'apendice-b-dicionario-de-dados.md').read_text(encoding='utf-8')
    serv, tab, out = None, None, {}
    for linha in txt.splitlines():
        m = re.match(r'## B\.\d+ (.+)$', linha)
        if m: serv = m.group(1).strip(); out[serv] = {}; continue
        m = re.match(r'### B\.\d+\.\d+ `(\w+)`( \(técnica\))?', linha)
        if m: tab = out[serv][m.group(1)] = {'tecnica': bool(m.group(2)), 'campos': []}; continue
        m = re.match(r'\| `(\w+)` \| `([^`]+)` \| ([^|]+) \| ([^|]+) \| ([^|]+) \|', linha)
        if m and tab is not None:
            tab['campos'].append((m.group(1), m.group(2), m.group(3).strip(), m.group(5).strip(), m.group(4).strip() == 'Não'))
    return out


def dominio_fechado(dom):
    if dom in ('Texto', 'Inteiro', 'UUID', 'Minutos', 'Sim ou não', 'Data', 'Data, hora e fuso', 'Texto JSON') or \
       dom.startswith('Identificador') or '…' in dom: return None
    partes = [x.strip() for x in re.split(r',\s*|\s+ou\s+', re.sub(r'\s*\(.*\)$', '', dom)) if x.strip()]
    return partes if len(partes) > 1 else None


def conferir_modelo(classes):
    ab = ler_apendice_b()
    nsdo = {v: k for k, v in SERVICOS.items()}
    tabelas = 0
    for serv, tabs in ab.items():
        ns = nsdo[serv]
        for tabela, d in tabs.items():
            if d['tecnica']:
                chave = TECNICAS.get(tabela)
                if not chave or chave not in classes: erro(f'tabela técnica {serv}.{tabela} sem classe'); continue
            elif tabela.startswith('dependencia_'):
                dona = {'dependencia_tarefa_modelo': 'TarefaModelo', 'dependencia_tarefa_plano': 'TarefaPlano',
                        'dependencia_tarefa': 'Tarefa', 'dependencia_monitorada': 'TarefaMonitorada'}[tabela]
                c = classes.get(f'{ns}.{dona}')
                if not c or not any(a[1] == 'predecessoras' and a[2] == f'List<{dona}>' for a in c['atributos']):
                    erro(f'{ns}.{tabela}: falta a lista predecessoras: List<{dona}> em {dona} (C13.6)')
                tabelas += 1; continue
            elif len(d['campos']) == 2 and all(x[2] == 'PK, FK' for x in d['campos']):
                # associativa pura (N:N sem atributos próprios): vira a lista de um lado no outro
                a, b = (re.search(r'Identificador de `(\w+)`', x[3]).group(1) for x in d['campos'])
                ok = any(at[2] == f'List<{pascal(y)}>' for x, y in ((a, b), (b, a))
                         for at in classes.get(f'{ns}.{pascal(x)}', {}).get('atributos', []))
                if not ok: erro(f'{ns}.{tabela}: associativa sem a lista List<{pascal(b)}> em {pascal(a)} (ou o inverso) (C13.6)')
                tabelas += 1; continue
            else:
                chave = f'{ns}.{pascal(tabela)}'
                if chave not in classes: erro(f'tabela {serv}.{tabela} sem a classe {chave} (C13.6)'); continue
                tabelas += 1
            c = classes[chave]
            attrs = {a[1]: a[2] for a in c['atributos']}
            campos = {x[0] for x in d['campos']}
            for nome, tipo_sql, chave_campo, dom, opcional in d['campos']:
                an = camel(nome) if camel(nome) in attrs else camel(nome[:-3]) if nome.endswith('_id') else None
                if an in attrs and not attrs[an].startswith('List<') and attrs[an].endswith('[0..1]') != opcional:
                    erro(f'{chave}.{an}: {"falta" if opcional else "sobra"} [0..1] (campo {tabela}.{nome} '
                         f'{"opcional" if opcional else "obrigatório"} no Apêndice B) (C13.6)')
                if nome == 'codigo_versao' and 'codigo_atraso' in campos and 'FK' in chave_campo: continue
                if nome == 'codigo_atraso' and 'FK' in chave_campo:
                    if 'codigoAtraso' not in attrs: erro(f'{chave}: falta codigoAtraso: CodigoAtraso (FK composta) (C13.6)')
                    continue
                if 'FK' in chave_campo:
                    ref = re.search(r'Identificador de `(\w+)`', dom).group(1)
                    alvo = f'{ns}.{pascal(ref)}'
                    if nome.endswith('_id') and camel(nome[:-3]) in attrs: continue
                    if 'PK' in chave_campo and nome == 'versao': continue
                    todo = classes.get(alvo, {})
                    if any(re.sub(r'\s*\[[0-9.*]+\]$', '', a[2]) in (f'List<{c["nome"]}>', c['nome'])
                           for a in todo.get('atributos', [])): continue
                    erro(f'{chave}: campo {nome} (FK para {ref}) sem atributo {camel(nome[:-3])} nem lista em {alvo} (C13.6)')
                    continue
                if camel(nome) not in attrs:
                    erro(f'{chave}: campo {tabela}.{nome} sem o atributo {camel(nome)} (C13.6)'); continue
                tipo = re.sub(r'\s*\[[0-9.*]+\]$', '', attrs[camel(nome)])
                aceitos = next((v for k, v in SQL_UML if tipo_sql.startswith(k)), set())
                alvo = resolver(tipo, c['ns'], classes)
                if tipo in aceitos: pass
                elif alvo and classes[alvo]['tipo'] == 'enum' and tipo_sql.startswith(('VARCHAR', 'CHAR')):
                    valores = dominio_fechado(dom)
                    if valores and set(valores) != set(classes[alvo]['valores']):
                        erro(f'{chave}.{camel(nome)}: {tipo} = {classes[alvo]["valores"]}, domínio = {valores} (C13.7)')
                else:
                    erro(f'{chave}.{camel(nome)}: tipo {tipo} incompatível com {tipo_sql} (C13.6)')
                if alvo and classes[alvo]['tipo'] == 'enum' and dominio_fechado(dom) is None:
                    erro(f'{chave}.{camel(nome)}: {tipo} é enumeração, mas o domínio de {tabela}.{nome} '
                         f'no Apêndice B é "{dom}" (C13.7)')
    conferir_modelo_reverso(classes, ab)
    return tabelas


def conferir_modelo_reverso(classes, ab):
    """C13.6 no outro sentido: toda entidade de serviço tem tabela no Apêndice B, e todo atributo dela tem campo
    (pelo nome, pela FK sem o _id ou como lista das partes que apontam para ela)."""
    nsdo = {v: k for k, v in SERVICOS.items()}
    tabela_de = {}
    for serv, tabs in ab.items():
        for tabela, d in tabs.items():
            if not d['tecnica']: tabela_de[f'{nsdo[serv]}.{pascal(tabela)}'] = (tabela, d, tabs)
    for chave, c in classes.items():
        if c['est'] != 'entity' or c['ns'] not in SERVICOS or chave in TECNICAS.values(): continue
        if chave not in tabela_de:
            erro(f'{chave}: entidade sem tabela no Apêndice B (C13.6, classe → tabela)'); continue
        tabela, d, tabs = tabela_de[chave]
        campos = {x[0] for x in d['campos']}
        for vis, nome, tipo, n in c['atributos']:
            base = re.sub(r'\s*\[[0-9.*]+\]$', '', tipo)
            if re.sub(r'([A-Z])', r'_\1', nome).lower() in campos: continue
            if re.sub(r'([A-Z])', r'_\1', nome).lower() + '_id' in campos: continue
            if nome == 'codigoAtraso' and 'codigo_atraso' in campos: continue
            m = re.fullmatch(r'List<(\w+)>', base) or re.fullmatch(r'(\w+)', base)
            if m and m.group(1) not in PRIMITIVOS:
                parte = re.sub(r'([A-Z])', r'_\1', m.group(1)).lstrip('_').lower()
                if nome == 'predecessoras' or (parte in tabs and any(f[0] == f'{tabela}_id' or
                                                                   f'`{tabela}`' in f[3] for f in tabs[parte]['campos'])):
                    continue
                if any({f[0] for f in t['campos']} == {f'{tabela}_id', f'{parte}_id'} for t in tabs.values()):
                    continue  # associativa pura entre as duas tabelas
            erro(f'{chave}.{nome}: atributo sem campo em {tabela} no Apêndice B (C13.6, classe → tabela)')


def conferir_estados(classes):
    ctx = (RAIZ / 'CONTEXT.md').read_text(encoding='utf-8')
    m = re.search(r'\*\*Turnaround:\*\* (.+?); estado lateral \*\*(.+?)\*\*', ctx)
    turn = [x.strip() for x in m.group(1).split('→')] + [m.group(2)]
    m = re.search(r'\*\*Tarefa:\*\* (.+?); ramos \*\*(.+?)\*\* e \*\*(.+?)\*\*', ctx)
    tar = [x.strip() for x in m.group(1).split('→')] + [m.group(2), m.group(3)]
    for chave, esperado in (('contrato.EstadoTurnaround', turn), ('contrato.EstadoTarefa', tar)):
        if classes[chave]['valores'] != esperado: erro(f'{chave} = {classes[chave]["valores"]}, CONTEXT.md = {esperado} (C13.7)')


def conferir_sequencia(classes):
    """C13.8: mensagem `X -> Y : metodo(...)` com Y declarado como uma classe do item 13."""
    por_nome = {}
    for k, c in classes.items(): por_nome.setdefault(c['nome'], []).append(c)
    total = 0
    for arq in sorted(DIAG.glob('14-sequencia-*.puml')):
        apelido = {}
        for t in arq.read_text(encoding='utf-8').splitlines():
            m = re.match(r'\s*(?:participant|control|boundary|entity|database|actor|collections|queue)\s+"([^"]+)"\s+as\s+(\w+)', t)
            if m: apelido[m.group(2)] = m.group(1)
        for n, t in enumerate(arq.read_text(encoding='utf-8').splitlines(), 1):
            m = re.match(r'\s*(\w+)\s*-+>+\s*(\w+)\s*:\s*(\w+)\((.*)\)\s*$', t)
            if not m or m.group(2) not in apelido: continue
            nome = apelido[m.group(2)]
            if nome not in por_nome: continue
            total += 1
            if not any(mt[1] == m.group(3) for c in por_nome[nome] for mt in c['metodos']):
                erro(f'{arq.name}:{n}: {nome}.{m.group(3)}() não existe no item 13 (C13.8)')
    return total


def main():
    classes, relacoes = ler_classes()
    conferir_tipos(classes)
    conferir_associacoes(classes, relacoes)
    conferir_contratos(classes, relacoes)
    conferir_dtos_espelho(classes)
    tabelas = conferir_modelo(classes)
    conferir_estados(classes)
    msgs = conferir_sequencia(classes) if '--sequencia' in sys.argv else None
    por_est = {}
    for c in classes.values(): por_est[c['est'] or c['tipo']] = por_est.get(c['est'] or c['tipo'], 0) + 1
    resumo = ', '.join(f'{v} {k}' for k, v in sorted(por_est.items()))
    print(f'{len(classes)} classes ({resumo}); {len(relacoes)} relações; {tabelas} tabelas de negócio conferidas'
          + (f'; {msgs} mensagens de sequência conferidas' if msgs is not None else ''))
    for p in problemas: print('-', p)
    print(f'{len(problemas)} problema(s)')
    sys.exit(1 if problemas else 0)


if __name__ == '__main__':
    main()
