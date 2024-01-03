def numeros_reais_positivos(numeros_positivos, contador):
    for i in range(0, 11):
        contador += 1
        soma_positivos = i + i

        numeros_positivos.append(i)

    print(f'\nNúmeros positivos {numeros_positivos}')
    print(f'Números positivos somados {soma_positivos}')

def numeros_reais_negativos(numeros_negativos, contador):
    for i in range(-11, 0):
        contador += 1
        soma_negativos = i + i

        numeros_negativos.append(i)

    print(f'\nNúmeros negativos {numeros_negativos}')
    print(f'Números negativos somados {soma_negativos}')

def main():

    numeros_positivos = []
    numeros_negativos = []
    contador = 0
    numeros_reais_positivos(numeros_positivos, contador)
    numeros_reais_negativos(numeros_negativos, contador)

if __name__=='__main__':
    main()
