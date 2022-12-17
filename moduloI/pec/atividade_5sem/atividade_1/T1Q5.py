def pagamento_Avista(valor):

    porcentagem = valor * 0.09
    valor_desconto = valor - porcentagem
    print(f'Valor à vista com 9% de desconto R${valor_desconto:.2f}')
    

def pagamento_5Vezes(valor):

    valor_5Vezes = valor / 5
    print(f'Pagamento em 5X no valor de R${valor_5Vezes:.2f}')

def pagamento_10Vezes(valor):

    porcentagem_10Vezes = valor * 0.17
    valor_juros = valor + porcentagem_10Vezes
    
    print(f'Pagamento em 10X + 17% de juros de R${valor_juros:.2f}')


def main():
    valor = int(input())
    
    pagamento_Avista(valor)
    pagamento_5Vezes(valor)
    pagamento_10Vezes(valor)

if __name__=='__main__':
    main()
