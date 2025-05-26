# Bibliotecas
from docx import Document
import os

doc = Document()
# Documento

doc.add_heading("Teste", level=1)
doc.add_paragraph("Olá mundo!")


# Salvar
filename = "Docs/tag.docx"
doc.save(filename)
print(f"Documento salvo como: {os.path.abspath(filename)}")