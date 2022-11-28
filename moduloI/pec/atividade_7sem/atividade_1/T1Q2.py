def numeric(numero):
    par = (numero/2)
    numero_par = par % 1

    if numero_par == 0:
        print(False)

    else:
        print(True)


def main():
    numero = int(input())
    numeric(numero)

if __name__=='__main__':
    main()
