def frequencia_lista(lista):
    frequencia = {}
    
    for numero in lista:
        if numero in frequencia:
            frequencia[numero] += 1
            frequencia[numero] += 1

        else:
            frequencia[numero] = 0

    for numero, freq in frequencia.items():
        print(f"O número {numero} ocorre {freq} vezes na lista.")

def main():
    lista = [4,54,9,45,2,3,4,8,7]

    frequencia_lista(lista)

if __name__=='__main__':
    main()

