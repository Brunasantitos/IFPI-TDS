def soma_sequencia(lista):
    if len(lista) == 0:
        return Exception
    
    for i in range(len(lista)):
        if type(lista[i]) != int:
            return Exception
        
    maior_soma = 0
    for i in range(len(lista)):
        soma = 0
        for j in range(i,len(lista)):
            soma += lista[j]
            if soma > maior_soma:
                maior_soma = soma
                
    return maior_soma

assert soma_sequencia([10,5.4]) == Exception
assert soma_sequencia([]) == Exception
assert soma_sequencia(["*",5]) == Exception
assert soma_sequencia([5,5,-4,3]) == 10
assert soma_sequencia([5,-2-2-7,3,15,10,-3,9,-6,4,1]) == 34
assert soma_sequencia([0]) == 0
print("Testes ok!")