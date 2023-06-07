def mostrarMaior_Menor(lista):
    if len(lista) == 0 or lista == [0] or type(lista) != list:
        return Exception
    
    maior = lista[0]
    menor = lista[0]
    for valor in lista:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor     
    return maior, menor


assert mostrarMaior_Menor([3, 8, 1, 5, 4]) ==  (8, 1)
assert mostrarMaior_Menor([4, 232, 20, 2]) == (232, 2)
assert mostrarMaior_Menor([0]) == Exception
print('Todos os testes OK!')