def parametroN(N):
    S = 0
    for i in range(1, N+1):
        S += (i**2+1)/(i+3)
    return S

def main():
    while True:
        try:
            N = int(input("Informe um número: "))
            if N >= 0:
                print(f'\nO resultado é: {parametroN(N):.2f}')
                break
            else:
                print('Informe apenas números positivos')

        except:
            print('Tente novamente')

if __name__=='__main__':
    main()
        
