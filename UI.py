# Bibliotecas
import tkinter as tk
import random
import string

# Função para gerar o código da etiqueta
def gerar_codigo():
    global prod_codigo, status, r, nome_produto
    nome_produto = entrada_nome.get()  # Captura o nome digitado
    if not nome_produto.strip():  # Verifica se está vazio
        status.config(text="Por favor, insira o nome do produto.", fg="red")  # Mostra erro
        return
    # Gera um código de 9 caracteres (letras e números)
    codigo = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(9))
    prod_codigo = codigo  # Salva o código
    status.config(text=f"Etiqueta gerada para '{nome_produto}' com sucesso!", fg="green")  # Mensagem de sucesso
    r.destroy()  # Fecha a janela

# Cria a janela principal
r = tk.Tk()
r.title("Gerador de Etiquetas")
r.geometry("400x250")

# Configura o layout para centralizar os elementos
r.grid_rowconfigure(0, weight=1)
r.grid_rowconfigure(7, weight=1)
r.grid_columnconfigure(0, weight=1)
r.grid_columnconfigure(1, weight=1)

# Título da aplicação
tk.Label(r, text="Gerador de Etiquetas", font=("Helvetica", 16, "bold")).grid(row=1, column=0, columnspan=2, pady=10)

# Campo para digitar o nome do produto
tk.Label(r, text="Nome do produto:").grid(row=2, column=0, sticky="e", padx=5)
entrada_nome = tk.Entry(r, width=30)
entrada_nome.grid(row=2, column=1, padx=5)

# Botão para gerar o código
tk.Button(r, text="Gerar/Usar Código", command=gerar_codigo, bg="green", fg="white").grid(row=3, column=0, columnspan=2, pady=10)

# Label para mostrar o código (não está sendo usado)
codigo_label = tk.Label(r, text="", font=("Helvetica", 12))
codigo_label.grid(row=4, column=0, columnspan=2)

# Label para mensagens de status
status = tk.Label(r, text="", font=("Helvetica", 10))
status.grid(row=5, column=0, columnspan=2)

# Inicia a interface gráfica
r.mainloop()
