import webview
from api import Api

window = webview.create_window(
    title="Gerador de Etiquetas",
    url="frontend/index.html",      # seu HTML bonito aqui
    js_api=Api(),          # expõe a classe pra o JS chamar
    width=520,
    height=680,
    resizable=False
)

webview.start()