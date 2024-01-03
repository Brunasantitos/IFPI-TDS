import pandas as pd
arquivo = pd.read_csv('./heart.csv', sep=',',na_values=['--','n/a','nada'])

#filtrando colunas
filtrando = (arquivo['age'] > 2) & (arquivo['sex'] < 40)
filtrando2 = (arquivo['age'] > 2) | (arquivo['sex'] < 40)
print(filtrando)
print(filtrando2)

#Agrupar por uma única coluna e aplicar várias funções de agregação
valor = arquivo.groupby('age')['sex'].agg(['mean','min','max'])
print(valor)

#ordenado por idade
valor2 = arquivo.sort_values(by='age')
print(valor2)
