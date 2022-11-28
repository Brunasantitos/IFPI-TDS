def pessoa(numeric_identificacao, nome):
    if numeric_identificacao == 1:
        print(f'Ilmo Sr. {nome}')
    if numeric_identificacao == 2:
        print(f'Ilma Sra. {nome}')

def main():
    nome = input()
    numeric_identificacao = int(input())
    pessoa(numeric_identificacao, nome)

if __name__=='__main__':
    main()
