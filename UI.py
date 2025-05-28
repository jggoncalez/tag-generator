import tkinter as tk
import random
import string

def gerar_codigo():
    global prod_codigo
    if var_gerar.get():
        codigo = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(9))
    else:
        codigo = entrada_codigo.get().strip()
        if not codigo:
            status.config(text="Insira um código ou selecione aleatório.", fg="red")
            return
    prod_codigo = codigo
    status.config(text="Etiqueta gerada com sucesso!", fg="green")
    r.destroy()

r = tk.Tk()
r.title("Gerador de Etiquetas")
r.geometry("400x250")

# Título
tk.Label(r, text="🎫 Gerador de Etiquetas", font=("Helvetica", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

#Entrada de nome do produto
tk.Label(r, text="Nome do produto:").grid(row=1, column=0, sticky="e", padx=5)
entrada_nome = tk.Entry(r, width=30)
entrada_nome.grid(row=1, column=1, padx=5)

var_gerar = tk.IntVar()
tk.Checkbutton(r, text="Gerar código aleatório", variable=var_gerar).grid(row=4, column=0, columnspan=2)

tk.Label(r, text="Código do produto:").grid(row=3, column=0, sticky="e", padx=5)
entrada_codigo = tk.Entry(r, width=20)
entrada_codigo.grid(row=3, column=1, padx=5)

tk.Button(r, text="Gerar/Usar Código", command=gerar_codigo, bg="green", fg="white").grid(row=5, column=0, columnspan=2, pady=10)

codigo_label = tk.Label(r, text="", font=("Helvetica", 12))
codigo_label.grid(row=6, column=0, columnspan=2)

status = tk.Label(r, text="", font=("Helvetica", 10))
status.grid(row=6, column=0, columnspan=2)

r.mainloop()
