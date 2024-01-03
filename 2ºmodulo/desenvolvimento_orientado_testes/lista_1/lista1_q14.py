def fatorial(N):
    S = 1
    contador = 1
    for i in range(1, N+1):
        S = i * S
        contador += 1/S
    return contador


def main():
    while True:
        try:
            N = int(input("Informe um número: "))
            if N >= 0:
                print(f'\nfatorial: {fatorial(N):.3f}')
                break
            else:
                print("Somente números positivos!")
        except:
            print("Tente novamente!")


if __name__=='__main__':
    main()
