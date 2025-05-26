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
    print("Bem-Vindo ao Criador de banco de dados pro")
    print("Escolha entre cadastrar ou sair")
    print("Escolha dentre as opções abaixo")
    print("cadastrar (Você deseja cadastrar um produto ?)")
    print("sair (Você deseja parar de cadastrar)")
    escolha = input("").lower()
    if escolha == "cadastrar":
        id += 1
        codigo = int(input("Insira o código desse produto:"))
        df = pd.concat([df, pd.DataFrame({"ID": [id], "NOME": ["H2JKV"] ,"CÓDIGO": [codigo]})], ignore_index=True)
    else:
        break
df.to_excel("bancodedados.xlsx", index=False)