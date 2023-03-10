def posicao_elemento(lista_numeros):
    contador = 0
    for i in range(0,1):
        contador += 1
        lista_numeros.append(i)
        
        numero_maximo_lista = max(lista_numeros)
        
        numero_minimo_lista = min(lista_numeros)
        
        
        print(i)
    print(f'\nO maior número: {numero_maximo_lista} \nA sua posição: ')
    print(f'\nO menor número: {numero_minimo_lista} \nA sua posição: ')
        
def main():
    lista_numeros = []
    posicao_elemento(lista_numeros)

if __name__=='__main__':
    main()