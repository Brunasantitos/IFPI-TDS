def lerNumero():
    while True:
        try:
            numero = int(input('Digite o número inteiro e positivo: '))
            if (numero < 0):
                print('O número deve ser positivo. Tente novamente.')
                lerNumero()
            return numero
        except:
            print('Número inválido. Tente novamente.')


def somaTudoEntreDoisNumeros(n1, n2):
    a1 = n1 if n1 < n2 else n2
    an = n2 if n2 > n1 else n1
    return (a1+an)*((an-(a1)+1)/2)


def main():
    n = lerNumero()
    print('O somatório de 1 até %d é %d' % (n, somaTudoEntreDoisNumeros(1, n)))


if __name__ == "__main__":
    main()