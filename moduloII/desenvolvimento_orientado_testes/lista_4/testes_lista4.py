def remover_numeros_iguais(lista):
    if len(lista) != int:
        lista_sem_repeticoes = list(set(lista))
        print(lista_sem_repeticoes)
    else:
        lista_sem_repeticoes = list(set(lista))
        print(lista_sem_repeticoes)


def main():
    lista = [1,1,1,3,4,45]
    nova_lista = remover_numeros_iguais(lista)
    print(nova_lista)

    
    print("Testes ok!")

if __name__=='__main__':
    main()
