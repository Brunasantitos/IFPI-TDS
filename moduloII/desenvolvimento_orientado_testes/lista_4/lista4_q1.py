def remover_numeros_iguais(lista):
    if len(lista) != int:
        return Exception
    
    else:
        lista_sem_repeticoes = list(set(lista))
        return lista_sem_repeticoes



assert remover_numeros_iguais(["*",5]) == Exception
assert remover_numeros_iguais([1,1,1,2,3,45]) == Exception

print("Testes ok!")
