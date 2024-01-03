def faturamento(L1,L2,contador):

    faturamento_produto = [L1[i] * L2[i] for i in range(len(L1))]
    print(f'Valor: {faturamento_produto}')
    
    if contador == 2:
        faturamento_total = sum(faturamento_produto)
        print(f'Faturamento total {faturamento_total}')

  


def main():
    ListaQuantidade = []
    ListaValores = []
    contador = 0
    while contador<=2:
        ListaQuantidade.append(int(input('Informe a quantidade de produto: ')))
        ListaValores.append(float(input('Informe o valor do produto: ')))
        faturamento(ListaQuantidade,ListaValores,contador)
        contador+=1
        

if __name__=='__main__':
    main()
