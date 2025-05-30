# Bibliotecas
from docx import Document
from docx.shared import Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
import os

# Importando variáveis

from UI import prod_codigo
# from UI import prod_nome

doc = Document()

# Tamanho do documento
section = doc.sections[0]
section.page_width = Inches(2)
section.page_height = Inches(3)
section.top_margin = section.right_margin = section.left_margin = section.bottom_margin = 0

# Documento
title = doc.add_heading(f"Etiqueta: {prod_codigo}", level=1)
text = doc.add_paragraph(str(prod_codigo))

# QR Code
qrcode_p = doc.add_paragraph("")
run = qrcode_p.add_run()
run.add_picture(f"qrcode_{prod_codigo}.png", width=Inches(1.0))

# Alinhamento do texto
title.alignment = WD_ALIGN_PARAGRAPH.CENTER
text.alignment = WD_ALIGN_PARAGRAPH.CENTER
qrcode_p.alignment = WD_ALIGN_PARAGRAPH.CENTER

# Salvar
filename = "Docs/tag.docx"
os.makedirs(os.path.dirname(filename), exist_ok=True)
doc.save(filename)
print(f"Documento salvo como: {os.path.abspath(filename)}")