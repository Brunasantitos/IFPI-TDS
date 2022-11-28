def valor_deX(X):
    cubo_x = (X**3)
    print(f'seu valor elevado ao cubo é: {cubo_x}')

def main():
    X = int(input("informe um valor inteiro: "))
    valor_deX(X)


if __name__=='__main__':
    main()
