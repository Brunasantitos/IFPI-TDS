def faturamento(L1,L2):
    pass

def main():
    ListaQuantidade = []
    ListaValores = []
    contador = 0
    while contador<=20:
        ListaQuantidade.append(int(input('Informe a quantidade de produto: ')))
        ListaValores.append(float(input('Informe o valor do produto: ')))
        faturamento(ListaQuantidade,ListaValores)
        contador+=1
        

if __name__=='__main__':
    main()
