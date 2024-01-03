def MaiorNumero(A, B, C, D):
    maior = max(A, B, C, D)
    print(f'O maior número é {maior}')

def main():
    contador = 0
    cont = 1
    while contador < 4:
        print(f'\nO MAIOR NÚMERO DA SÉRIE {cont}:')
        cont += 1
        A = int(input("Informe um número: "))
        B = int(input("Informe um número: "))
        C = int(input("Informe um número: "))
        D = int(input("Informe um número: "))

        contador += 1
        MaiorNumero(A,B,C,D)
            

if __name__=='__main__':
    main()
