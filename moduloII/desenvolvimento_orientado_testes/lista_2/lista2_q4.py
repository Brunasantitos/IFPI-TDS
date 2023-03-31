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
    while True:
        try:
            contador = 0
            if contador <= 15:
                numero = [int(input("Informe um número: "))]
                contador += 1
                posicao_elemento(numero)
                break
                
        except:
            print("Informe somente números válidos!")

if __name__=='__main__':
    main()
