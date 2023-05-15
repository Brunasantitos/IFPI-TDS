def remover_numeros_iguais(lista):
    lista_sem_repeticoes = list(set(lista))
    return lista_sem_repeticoes


def main():
    lista = [5, 4, 5, 7, 3, 4]
    nova_lista = remover_numeros_iguais(lista)
    print(nova_lista)

if __name__=='__main__':
    main()
