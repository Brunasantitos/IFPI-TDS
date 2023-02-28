def max(n1, n2):
    if (n1 > n2):
        return n1
    return n2


def lerNumero(iesimoNumero, serie):
    while True:
        try:
            numero = float(input('Digite o ' + iesimoNumero +
                           ' número inteiro da série ' + str(serie) +
                                 ': '))
            return numero
        except:
            print('Número inválido. Tente novamente.')


def main():
    i = 0
    while(i < 4):
        num1 = lerNumero('primeiro', i+1)
        num2 = lerNumero('segundo', i+1)
        num3 = lerNumero('terceiro', i+1)
        num4 = lerNumero('quarto', i+1)
        print('O maior número da série %d é: %d' %
              (i+1, max(num1, max(num2, max(num3, num4)))))
        i += 1


if __name__ == "__main__":
    main()