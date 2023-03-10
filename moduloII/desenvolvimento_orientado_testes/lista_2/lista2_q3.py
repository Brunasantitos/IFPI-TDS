def ordem_inversa(lista_numeros):
    lista_numeros.sort(reverse = True)
    print(f'\nlista {lista_numeros}')

def main():
    lista_numeros = [1,2,3,4,5]
    ordem_inversa(lista_numeros)

if __name__=='__main__':
    main()