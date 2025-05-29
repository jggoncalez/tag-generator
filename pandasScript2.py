import json
import pandas as pd
#Caminho para o arquivo JSON
arquivo_json = "bancodedados.json"
#Dados que vão ser inseridos no arquivo JSON
novos_dados = {}
while True:
    escolha = int(input("Escolha entre continuar(1) ou sair(2):"))
    if escolha == 1:
        nome = input("Insira o nome de seu produto:")
        codigo = input("Insira o código de seu produto:")
        novos_dados["NOME"] = nome
        novos_dados["CÓDIGO"] = codigo
    elif escolha == 2:
        break
    else:
        print("Escolha uma opção válida (1/2)")
        continue
        
#Tenta ler o arquivo JSON
try:
    with open(arquivo_json, "r") as f:
        velhos_dados = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    velhos_dados = []

velhos_dados.extend(novos_dados)

# Salva os dados atualizados no arquivo JSON
with open(arquivo_json, "w") as f:
    json.dump(velhos_dados, f, ensure_ascii=False, indent=4)

