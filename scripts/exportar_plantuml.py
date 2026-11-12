"""Exporta um diagrama de sequência .puml (PlantUML) para PNG e SVG.

Um arquivo com `newpage` gera uma imagem por parte: <nome>.png, <nome>_001.png e assim por diante (e o .svg de cada uma).
O SVG sai com o texto como texto SVG (sem <foreignObject>), para o Word e os leitores de PDF desenharem o texto como vetor.

Uso: python scripts/exportar_plantuml.py especificacao/diagramas/14-sequencia-uc15.puml [outro.puml ...]
Precisa de Java e do plantuml.jar (https://plantuml.com/download); o caminho do .jar vai na variável PLANTUML_JAR.
"""
import os, shutil, subprocess, sys
from pathlib import Path


def comando():
    jar = os.environ.get('PLANTUML_JAR')
    if jar and Path(jar).exists():
        return ['java', '-DPLANTUML_LIMIT_SIZE=16384', '-jar', jar]
    if shutil.which('plantuml'):
        return ['plantuml']
    sys.exit('plantuml.jar não encontrado; defina a variável PLANTUML_JAR com o caminho do arquivo')


def main():
    arqs = [Path(a) for a in sys.argv[1:]]
    if not arqs: sys.exit(__doc__)
    base = comando()
    for formato in ('-tpng', '-tsvg'):
        subprocess.run(base + [formato, '-charset', 'UTF-8'] + [str(a) for a in arqs], check=True)
    for a in arqs:
        for img in sorted(a.parent.glob(a.stem + '*.svg')):
            if 'foreignObject' in img.read_text(encoding='utf-8'): sys.exit(f'{img}: texto em <foreignObject>')
        print('exportado:', ', '.join(p.name for p in sorted(a.parent.glob(a.stem + '*.*')) if p.suffix in ('.png', '.svg')))


if __name__ == '__main__':
    main()
