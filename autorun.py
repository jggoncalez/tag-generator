import time


import UI
UI  # Access the module to avoid "not accessed" error
print("UI concluído")
import gen_qrcode
gen_qrcode  # Access the module to avoid "not accessed" error
print("QR CODE gerado")
time.sleep(5)
import docxScript
docxScript  # Access the module to avoid "not accessed" error
print("Documento gerado!")