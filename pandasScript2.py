import json
import pandas as pd
#Caminho para o arquivo JSON
arquivo_json = "bancodedados.json"
#Dados que vão ser inseridos no arquivo JSON
novos_dados = {
    "ID": [],
    "NOME": [],
    "CÓDIGO": []
}
#Tenta ler o arquivo JSON
try:
    with open(arquivo_json,"r") as f:
        velhos_dados = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    velhos_dados = []
velhos_dados.extend(novos_dados)
#Lê o novos_dados como um dataframe
df = pd.DataFrame(novos_dados)

