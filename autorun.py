# Bibliotecas
import time

# Importa e inicia a interface gráfica
import UI
UI  
print("UI concluído")

# Importa e gera o QR Code
import gen_qrcode
gen_qrcode  
print("QR CODE gerado")
time.sleep(1)  # Espera 1 segundo

# Importa o código do produto da UI
from UI import prod_codigo

# Importa e gera o documento Word
import docxScript
docxScript 

print("Documento gerado!")
