from random import *

def criar_lista():
    ls = []
    for i in range(10):
        num_random = randint(-999,999)
        ls.append(num_random)
    return ls


def troca_num_negativo_por_zero(num_ls):
    flag = True
    for i in range(len(num_ls)):
        if num_ls[i] < 0:
           num_ls[i] = 0
           flag = False

    if flag:
        print('A lista não possui números negativos...')
            
    

def main():
     lista = criar_lista()
     print("================= LISTA ORIGINAL ===================")
     print(lista)
     troca_num_negativo_por_zero(lista)
     print("====================== LISTA =============================")
     print(lista)

if __name__=='__main__':
    main()