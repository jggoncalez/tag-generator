import qrcode                   # Importa a biblioteca principal para gerar QR Codes
import qrcode.constants         # Importa constantes úteis da biblioteca

data = "............."  # Cole aqui a URL ou texto que você quer codificar no QR Code

# Cria uma instância de QRCode com configurações específicas
qr = qrcode.QRCode(
    version=1,                                 # Define a versão do QR Code (tamanho e capacidade)
    box_size=5,                               # Tamanho de cada quadrado do QR Code em pixels
    border=1,                                  # Largura da borda (em caixas)
    error_correction=qrcode.constants.ERROR_CORRECT_Q,  # Nível de correção de erro (Q(Quartile) = 25% dos dados)
)

qr.add_data(data)              # Adiciona os dados (texto ou URL) ao QR Code
qr.make(fit = True)              # Gera a matriz do QR Code, ajustando o tamanho para acaber todos os dados, se necessário


img = qr.make_image(fill_color="black", back_color="white")   # Cria uma imagem do QR Code com as cores especificadas

img.save("qrcode_exemplo.png") # Salva a imagem gerada em um arquivo PNG