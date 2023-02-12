def fatorial(valor):

    x = 1

    for i in range(1,valor+1):

        x = i * x

    print(f'\nO fatorial de {valor} é {x}')


def main():
    valor = int(input("Valor: "))
    fatorial(valor)

if __name__=='__main__':
    main()