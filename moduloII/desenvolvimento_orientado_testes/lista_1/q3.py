def graus(entrada):
    c = ((entrada-32)/9)*5
    print(f'\nEm graus Fahrenheit {entrada}, graus em Celsius {c:.2f}')

def main():
    entrada = int(input("Informe uma temperatura: "))
    graus(entrada)

if __name__=='__main__':
    main()
