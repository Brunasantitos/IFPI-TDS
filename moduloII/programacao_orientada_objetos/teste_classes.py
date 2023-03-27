#coding: latin-1

def somatorio_fracoes(n):
    s = 0
    for i in range(1, n + 1):
        s += 1/i
    return s

#region MAIN
def main():
    while True:
        try:
            numero = int(input('Digite um n�mero inteiro positivo: '))
            while numero <= 0:
                numero = int(input("N�mero inv�lido! Digite um n�mero inteiro positivo! "))
            print(f'O somat�rio das fra��es at� 1/{numero} � igual a: {somatorio_fracoes(numero):.2f}')
            break
        except:
            print('!! DADO INV�LIDO !! Digite um n�mero inteiro positivo!')

    

#endregion MAIN

if __name__ == '__main__':
    main()