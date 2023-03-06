def maximo(n1, n2):
    o_maior = (max(n1, n2))
    print(f'\nO maior número é {o_maior}')

def main():
    numero1 = int(input("Informe um valor: "))
    numero2 = int(input("Informe um número: "))

    maximo(numero1, numero2)

if __name__=='__main__':
    main()