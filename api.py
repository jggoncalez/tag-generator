import random, string, os, base64
from io import BytesIO
import qrcode, qrcode.constants
from docx import Document
from docx.shared import Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH

class Api:
    def gerar_etiqueta(self, nome_produto: str) -> dict:
        if not nome_produto.strip():
            return {"sucesso": False, "erro": "Nome do produto vazio!"}

        # Gera código
        codigo = ''.join(
            random.choice(string.ascii_uppercase + string.digits)
            for _ in range(9)
        )

        # QR Code → base64 pra mostrar no HTML direto
        qr = qrcode.QRCode(version=1, box_size=5, border=1,
                           error_correction=qrcode.constants.ERROR_CORRECT_Q)
        qr.add_data(codigo)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        # Salva o arquivo físico também
        os.makedirs("output/qrcodes", exist_ok=True)
        qr_path = f"output/qrcodes/qrcode_{codigo}.png"
        img.save(qr_path)

        # Base64 pra exibir no <img> do HTML sem precisar de servidor
        buf = BytesIO()
        img.save(buf, format="PNG")
        qr_b64 = base64.b64encode(buf.getvalue()).decode()

        # Gera o .docx
        self._gerar_docx(nome_produto, codigo, qr_path)

        return {
            "sucesso": True,
            "codigo": codigo,
            "nome": nome_produto,
            "qr_b64": f"data:image/png;base64,{qr_b64}"
        }

    def _gerar_docx(self, nome, codigo, qr_path):
        doc = Document()
        s = doc.sections[0]
        s.page_width = s.page_height = Inches(2)
        # ... (igual ao seu docxScript.py)
        os.makedirs("output/docs", exist_ok=True)
        filename = f"output/docs/tag_{codigo}.docx"
        doc.save(filename)