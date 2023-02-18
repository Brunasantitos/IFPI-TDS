def fatorial(valor):

    x = 1

    for i in range(1,valor+1):

        x = i * x

    print(f'\{x} {i}')


def main():
    valor = int(input("Valor: "))
    fatorial(valor)

if __name__=='__main__':
    main()