def calcular_media(lista):
    if len(lista) == 0: #testar se a lista é vazia
        return Exception
    
    soma = 0
    for i in range(len(lista)):
        if type(lista[i]) != int or lista[i] < 0: #testar se algum valor da lista não é inteiro ou negativo
            return Exception
        soma += lista[i]
    return soma/len(lista)

assert calcular_media([1,4,8,9,10]) == (6.4)
assert calcular_media([]) == Exception
assert calcular_media([10,15,20,'a']) == Exception
assert calcular_media([25,-14,18,19]) == Exception
assert calcular_media([15,350,58,1.5]) == Exception
print('teste ok!')