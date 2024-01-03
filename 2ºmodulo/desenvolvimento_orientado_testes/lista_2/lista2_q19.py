from random import *

def criar_lista_com_n_elementos(qtd):
    ls = []
    for i in range(qtd):
        ls.append(randint(-999,999))
    return ls


def main():
    R = criar_lista_com_n_elementos(5)
    S = criar_lista_com_n_elementos(10)
    X = []
    for elemento in R:
        X.append(elemento)
    for elemento in S:
        X.append(elemento)        
    print("======================== LISTA R ===========================")
    print(R)
    print("\n======================== LISTA S ===========================")
    print(S)
    print("\n============================================ LISTA X ====================================================")
    print(X)

if __name__=='__main__':
    main()