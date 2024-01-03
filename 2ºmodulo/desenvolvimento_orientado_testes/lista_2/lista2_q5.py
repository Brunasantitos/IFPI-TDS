def lista_intercalada(L20, L10):
    integracaoDeListas = L20 + L10
    print(f'\n{integracaoDeListas} são as duas listas')

def main():
    lista20Elementos = ['carro', 14, 5, 'casa', 5, 'bruna, cinquenta']
    lista10Elementos = ['preto', 50, 'luna', 'mara', 5, 'laranja', 10, 15]

    lista_intercalada(lista20Elementos, lista10Elementos)

if __name__=='__main__':
    main()
