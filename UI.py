import tkinter as tk
import random
import string

# Função para gerar o código da etiqueta
def gerar_codigo():
    global prod_codigo, status, r, nome_produto
    nome_produto = entrada_nome.get()  # Captura o texto digitado no campo "Nome do produto"
    if not nome_produto.strip():  # Verifica se o campo está vazio
        status.config(text="Por favor, insira o nome do produto.", fg="red")  # Exibe mensagem de erro
        return
    # Gera um código aleatório de 9 caracteres (letras maiúsculas e dígitos)
    codigo = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(9))
    prod_codigo = codigo  # Armazena o código gerado
    # Atualiza o status com uma mensagem de sucesso
    status.config(text=f"Etiqueta gerada para '{nome_produto}' com sucesso!", fg="green")
    r.destroy()  # Fecha a janela principal

# Criação da janela principal
r = tk.Tk()
r.title("Gerador de Etiquetas")  # Define o título da janela
r.geometry("400x250")  # Define o tamanho da janela

# Configurar o layout para centralizar os elementos
r.grid_rowconfigure(0, weight=1)
r.grid_rowconfigure(7, weight=1)
r.grid_columnconfigure(0, weight=1)
r.grid_columnconfigure(1, weight=1)

# Título da aplicação
tk.Label(r, text="🎫 Gerador de Etiquetas", font=("Helvetica", 16, "bold")).grid(row=1, column=0, columnspan=2, pady=10)

# Campo de entrada para o nome do produto
tk.Label(r, text="Nome do produto:").grid(row=2, column=0, sticky="e", padx=5)
entrada_nome = tk.Entry(r, width=30)  # Campo de texto para entrada do nome
entrada_nome.grid(row=2, column=1, padx=5)

# Botão para gerar ou usar o código
tk.Button(r, text="Gerar/Usar Código", command=gerar_codigo, bg="green", fg="white").grid(row=3, column=0, columnspan=2, pady=10)

# Label para exibir o código gerado (atualmente não utilizado)
codigo_label = tk.Label(r, text="", font=("Helvetica", 12))
codigo_label.grid(row=4, column=0, columnspan=2)

# Label para exibir mensagens de status
status = tk.Label(r, text="", font=("Helvetica", 10))
status.grid(row=5, column=0, columnspan=2)

# Inicia o loop principal da interface gráfica
r.mainloop()
