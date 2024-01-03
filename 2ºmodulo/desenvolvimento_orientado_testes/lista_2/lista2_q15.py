from random import *

def criar_lista():
    ls = []
    for i in range(10):
        ls.append(randint(-999,999))
    return ls

def criar_lista_inversa(num_ls):
    index_lista_normal = 0
    ls_inversa = [0]*len(num_ls)
    ultima_posicao = len(num_ls) - 1
    for i in range(ultima_posicao, -1, -1):
        ls_inversa[i] = num_ls[index_lista_normal]
        index_lista_normal +=1
    return ls_inversa


def main():
    C = criar_lista()
    print("=================== LISTA NORMAL ===============")
    print(C)
    print()
    D = criar_lista_inversa(C)
    print("============== LISTA INVERSA ========================")
    print(D)
    print()
    print("=============== LISTA INVERSA COM REVERSERD =========")
    print(list(reversed(C)))

if __name__=='__main__':
    main()