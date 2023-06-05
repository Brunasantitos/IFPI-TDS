from random import *

def criar_lista():
    ls = []
    for i in range(10):
        ls.append(randint(-999,999))
    return ls


def main():
    X = criar_lista()
    tamnho_lista_X = len(X)
    Y = [0] * tamnho_lista_X
    for i in range(tamnho_lista_X):
        if i % 2 == 0:
            Y[i] = X[i] // 2
        else:
            Y[i] = X[i] * 3

    print("======================== LISTA X ========================")
    print(X)
    print("\n======================== LISTA Y =======================")
    print(Y)


if __name__=='__main__':
    main()