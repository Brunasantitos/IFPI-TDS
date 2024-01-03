def vogal(entrada):
    if entrada == 'a' or entrada == 'A':
        print('vogal')

    elif entrada == 'e' or entrada == 'E':
        print('vogal')

    elif entrada == 'i' or entrada == 'I':
        print('vogal')

    elif entrada == 'o' or entrada == 'O':
        print('vogal')

    elif entrada == 'u' or entrada == 'U':
        print('vogal')

def consoante(entrada):

    if 'a' <= entrada <= 'z':
        print('consoante')

    elif 'A' <= entrada <= 'Z':
        print('consoante')

def simbolo(entrada):

    if '0' <= entrada <= '9':
        print('numero')

    else:
        print('simbolo')


def main():
    
    entrada = input()
    vogal(entrada)
    consoante(entrada)
    simbolo(entrada)

if __name__=='__main__':
    main()
