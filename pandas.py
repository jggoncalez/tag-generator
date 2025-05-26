import pandas as pd

# Criando um "banco de dados" com uma lista de dicionários
dados = [
    {"ID": 1, "Nome": "Ana", "Idade": 28},
    {"ID": 2, "Nome": "Carlos", "Idade": 34},
    {"ID": 3, "Nome": "João", "Idade": 22}
]

# Criando o DataFrame (banco de dados em memória)
df = pd.DataFrame(dados)

# Exibindo os dados
print(df)