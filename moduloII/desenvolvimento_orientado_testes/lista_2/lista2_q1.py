def numeros_pares(lista_par, contador_par):
    for i in range(0,101):
        
        if i % 2 == 0:
            contador_par += 1 
            lista_par.append(i)
        
    print(f'\nQuantidade de números pares: {contador_par}')
    print(f'\nEsses são os números pares {lista_par}')
    
def numeros_impares(lista_impar, contador_par):
    for i in range(0,101):
        
        if i % 2 != 0:
            contador_par += 1
            lista_impar.append(i)
        
    print(f'\nQuantidade de números ímpares: {contador_par}')
    print(f'\nEsses são os números ímpares {lista_impar}')

def main():
    lista_par = []
    lista_impar = []
    contador_par = 0
    
    numeros_pares(lista_par, contador_par)
    numeros_impares(lista_impar, contador_par)
    
    
if __name__=='__main__':
    main()
    