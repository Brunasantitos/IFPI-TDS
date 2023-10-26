import pandas as pd

arquivo = pd.read_csv('./heart.csv', sep=',',na_values=['--','n/a','nada'])

print(arquivo.head()) #primeira linha
print(arquivo.tail()) #últimas linhas
print(arquivo.info)
print(arquivo.describe())
print(arquivo.loc[[1]]) #colunas
print(arquivo.loc[0:3]) #linhas




