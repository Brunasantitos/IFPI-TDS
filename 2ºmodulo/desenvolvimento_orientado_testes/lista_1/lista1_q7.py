def fatorial(valor):

    x = 1

    for i in range(1,valor+1):

        x = i * x

    print(f'\nFatorial de {i}, é {x}')


def main():
    while True:
        try:
            valor = int(input("Valor: "))
            break
        except:
            print(f'\nInforme um valor válido')

    fatorial(valor)

if __name__=='__main__':
    main()