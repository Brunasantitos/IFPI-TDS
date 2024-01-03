def graus(entrada):
    c = ((entrada-32)/9)*5
    return c
def main():
    while True:
        try:

            entrada = int(input("Informe uma temperatura: "))
            print(f'\nEm graus Fahrenheit {entrada}, graus em Celsius {graus(entrada):.2f}')

            break
        except:
            print(f'\nInforme um valor para calcular!')
if __name__=='__main__':
    main()
