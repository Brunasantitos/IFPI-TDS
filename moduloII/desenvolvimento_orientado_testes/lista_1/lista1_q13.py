def N_positivo(N):
    S = 0
    for i in range(1, N+1):
        S += 1/i
    return S

def main():
    while True:
        try:
            N = int(input("Informe um número: "))
            if N >= 0:
                print(f'\nO resultado é: {N_positivo(N):.2f}')
                break
            else:
                print("Somente números positivos!")
        except:
            print("Tente novamente!")


if __name__=='__main__':
    main()
