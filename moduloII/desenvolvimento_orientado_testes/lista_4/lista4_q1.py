def remover_numeros_iguais(lista):
    if:
        pass
    else:
        for item in lista:
            if item == item:
                lista_sem_repeticoes = list(set(lista))
        return lista_sem_repeticoes


def main():
    lista = []
    nova_lista = remover_numeros_iguais(lista)
    print(nova_lista)

    assert remover_numeros_iguais(["*",5]) == Exception
    assert remover_numeros_iguais([1,1,1,2,3,45]) == Exception
    print("Testes ok!")

if __name__=='__main__':
    main()
