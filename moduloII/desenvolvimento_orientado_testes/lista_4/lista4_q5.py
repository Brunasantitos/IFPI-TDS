def verificar_ordem(lista):
    if len(lista) == 0:
        return Exception
    for i in range(len(lista)):
        if type(lista[i]) != int:
            return Exception
    ordenada = True
    for i in range(1,len(lista)):
        if lista[i] < lista[i-1]:
            ordenada = False
    return ordenada

assert verificar_ordem([10,5.4]) == Exception
assert verificar_ordem([]) == Exception
assert verificar_ordem(["*",5]) == Exception
assert verificar_ordem([1,2,3]) == True
assert verificar_ordem([3,7,2]) == False
assert verificar_ordem([0,0,0,0]) == True
assert verificar_ordem([2,4,6,5]) == False
assert verificar_ordem([5,2]) == False
print("Testes ok!")