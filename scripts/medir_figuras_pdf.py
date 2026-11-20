"""Mede quanto cada figura PNG encolhe no PDF: o tamanho da letra de 12 px depois de caber em 18 x 22 cm (gerar_docx.py).

Uso: python scripts/medir_figuras_pdf.py especificacao/diagramas/13-classes-*.png
"""
import struct, sys
from pathlib import Path
LARG, ALT = 18.0, 22.0
for arq in sys.argv[1:]:
    w, h = struct.unpack('>II', Path(arq).read_bytes()[16:24])
    cm_px = min(LARG / w, ALT / h)
    print(f'{Path(arq).stem:50} {w:5} x {h:5}  proporção {h / w:4.2f}  letra no PDF {12 * cm_px * 28.35:4.1f} pt')
