import pandas as pd
from openpyxl.workbook import Workbook
dados = {
    "ID": [],
    "NOME": [],
    "CÓDIGO": []
}
df = pd.DataFrame(dados)
id = 0
while True:
    print("Escolha dentre as opções abaixo")
    print("continuar (Você deseja continuar cadastrando)")
    print("sair (Você deseja parar de cadastrar)")
    escolha = input("").lower()
    if escolha == "continuar":
        id += 1
        nome = input("Insira o nome desse produto:")
        codigo = int(input("Insira o código desse produto:"))
        df = pd.concat([df, pd.DataFrame({"ID": [id], "NOME": [nome] ,"CÓDIGO": [codigo]})], ignore_index=True)
    else:
        break
df.to_excel("bancodedados.xlsx", index=False)