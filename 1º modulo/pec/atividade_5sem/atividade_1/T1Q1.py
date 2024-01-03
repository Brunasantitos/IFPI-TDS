def caracter(nome):
    minusculo = nome.lower()
    print(len(minusculo))

def main():
    nome =  input("Informe seu nome: ")
    caracter(f' o nome possui {nome} caracteres.')

if __name__=='__main__':
    main()

