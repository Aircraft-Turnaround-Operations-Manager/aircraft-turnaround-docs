"""Exporta um diagrama .drawio para PNG e SVG com o draw.io desktop.

O SVG sai com o texto como texto SVG de verdade (sem <foreignObject>), para o Word e os leitores de PDF
desenharem o texto como vetor: numa cópia temporária, os rótulos HTML viram texto simples, com as quebras de
linha preservadas. O arquivo .drawio original não é alterado.

Uso: python scripts/exportar_drawio.py especificacao/diagramas/09-casos-de-uso.drawio [escala_png]
Precisa do draw.io desktop instalado (https://www.drawio.com); o caminho pode ser dado em DRAWIO.
"""
import html, os, re, shutil, subprocess, sys, tempfile, xml.etree.ElementTree as ET
from pathlib import Path


def drawio_exe():
    candidatos = [os.environ.get('DRAWIO'), shutil.which('draw.io'), shutil.which('drawio'),
                  str(Path(os.environ.get('LOCALAPPDATA', '')) / 'Programs' / 'draw.io' / 'draw.io.exe'),
                  r'C:\Program Files\draw.io\draw.io.exe', '/Applications/draw.io.app/Contents/MacOS/draw.io']
    for c in candidatos:
        if c and Path(c).exists(): return c
    sys.exit('draw.io desktop não encontrado; defina a variável DRAWIO com o caminho do executável')


def texto_simples(origem, destino):
    """Copia o diagrama trocando rótulos HTML por texto simples (quebras de linha mantidas)."""
    arv = ET.parse(origem)
    for c in arv.getroot().iter('mxCell'):
        st = c.get('style') or ''
        v = c.get('value')
        if 'html=1' not in st or not v: continue
        txt = html.unescape(re.sub(r'<[^>]+>', '', re.sub(r'<br\s*/?>', '\n', v)))
        c.set('value', txt)
        # a quebra automática também faz o draw.io usar <foreignObject>; as quebras já estão no texto
        c.set('style', st.replace('html=1', 'html=0').replace('whiteSpace=wrap', 'whiteSpace=nowrap'))
    arv.write(destino, encoding='utf-8')


def main(arq, escala='2'):
    arq = Path(arq); exe = drawio_exe()
    with tempfile.TemporaryDirectory() as tmp:
        simples = Path(tmp) / arq.name
        texto_simples(arq, simples)
        for fmt, extra in (('png', ['--scale', escala]), ('svg', [])):
            saida = arq.with_suffix('.' + fmt)
            subprocess.run([exe, '--export', '--format', fmt, '--border', '20', *extra, '-o', str(saida), str(simples)], check=True,
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print('exportado', saida)
    svg = arq.with_suffix('.svg').read_text(encoding='utf-8')
    print('foreignObject no SVG:', svg.count('<foreignObject'), '| textos SVG:', svg.count('<text'))


if __name__ == '__main__':
    main(*sys.argv[1:])
