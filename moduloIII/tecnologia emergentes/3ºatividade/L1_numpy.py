import numpy as np 


# QUESTÃO 1: LETRA B E C 

peso = np.array([106.0, 68.5, 75.0]) #CERTO
altura = np.array([1.9, 1.53, 1.75])
IMC = peso / (altura * altura)
print(IMC)

peso = np.array([106.0, 68.5, 75.0]) #CERTO
altura = np.array([1*.9, 1.53, 1.75])
IMC = peso / altura ** 2
print(IMC)


# QUESTÃO 2: LETRA B E D 
idades = np.array([10,23,45,34,25])

print(idades.mean())


# QUESTÃO 3: OPÇÕES 2 E 3

#QUESTÃO 4:

dados = np.array([1,1,1,1,1,1,1,4,5,6,8])
y=(np.bincount(dados))
maximo = max(y)

for i in range(len(y)):
    if y[i] == maximo:
        print(i, end = " ")
  