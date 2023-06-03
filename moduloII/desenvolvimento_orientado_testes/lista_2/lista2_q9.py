from random import *

def reverte_lista(ls):
    last_index = len(ls) - 1
    rev = [0] * len(ls)
    index = 0
    for i in range(last_index, -1 , -1):
        rev[index] = ls[i]
        index += 1 
    return rev


def seed_lista(ls):
    for i in range(5):
        ls.append(randint(-99, 99))
    

def main():
    lista = []
    seed_lista(lista)
    lista_reversa = reverte_lista(lista)
    print("Lista")
    print(lista)
    print("Lista Reversa")
    print(lista_reversa)

    
if __name__=='__main__':
    main()