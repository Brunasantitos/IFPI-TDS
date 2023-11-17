import pandas as pd

url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
arquivo = pd.read_csv(url, sep = ',')
list(arquivo.iterrows())

male=0
total=0
for indice,coluna in arquivo.iterrows():
    total+=1
    if coluna['Sex']=='male':
      male+=1

print(f'percentual de homens:{male/total*100}')

male=0
tot=0
for indice,coluna in arquivo.iterrows():
    tot+=1
    if coluna['Sex']=='male':
      female+=1
print(f'percentual de mulheres: {male/tot*100}')


children=0
total=0
for indice,linha in arquivo.iterrows():
    total+=1
    if linha['Age'] <= 12 :
      children+=1
print(f'Quantidade de crianças com idade menor ou igual a 12 anos: {children}')


sobreviventes=0
total=0
for indice,linha in arquivo.iterrows():
    total+=1
    if linha['Pclass'] == 1:
      sobreviventes+=1
print(f'Quantidade de sobreviventes na classe 1: {sobreviventes}')

sobreviventes=0
total=0
for indice,linha in arquivo.iterrows():
    total+=1
    if linha['Pclass'] == 2:
      sobreviventes+=1
print(f'Quantidade de sobreviventes na classe 2: {sobreviventes}')

sobreviventes=0
total=0
for indice,linha in arquivo.iterrows():
    total+=1
    if linha['Pclass'] == 3:
      sobreviventes+=1
print(f'Quantidade de sobreviventes na classe 3: {sobreviventes}')


