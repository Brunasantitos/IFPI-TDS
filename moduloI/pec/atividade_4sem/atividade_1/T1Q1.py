def data(dia, mes, ano):
    print(f'\n{dia}/{mes}/{ano}')

def main():
    dia = int(input("Informe o dia: "))
    mes = int(input("Informe o mês: "))
    ano = int(input("Informe o ano: "))
    data(dia, mes, ano)
        
if __name__=='__main__':
    main()
