def intervalo_entradas(n1, n2):
    soma = 0
    for i in range(n1,n2+1):
      soma += i

    return soma

def main():
    while True:
        try:
            n1 = int(input(f'Informe um número: '))
            n2 = int(input(f'Informe um número: '))

            if n1 <= n2:
                print("\nA soma do intervalo informado é ", intervalo_entradas(n1,n2))
                break
            else:
                print("\nn2 deve ser maior que n1. Digite novamente!")
            
        except:
            print("\nValor inválido. Digite novamente!")

if __name__=='__main__':
    main()