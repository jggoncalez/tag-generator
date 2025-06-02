# Bibliotecas
import qrcode
import qrcode.constants

# Importa variável da interface
from UI import prod_codigo

# Configura o QR Code
qr = qrcode.QRCode(
    version=1,  # Versão do QR Code (tamanho fixo)
    box_size=5,  # Tamanho dos blocos
    border=1,  # Borda ao redor
    error_correction=qrcode.constants.ERROR_CORRECT_Q  # Correção de erro (Q (Quartile) = 25% dos dados)
)

# Adiciona dados e gera o QR Code
qr.add_data(prod_codigo)
qr.make(fit=True)

# Cria e salva a imagem do QR Code
img = qr.make_image(fill_color="black", back_color="white")
img.save(f"qrcode_{prod_codigo}.png")
