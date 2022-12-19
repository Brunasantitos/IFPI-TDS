def caractere(entrada):
    if 'a' <= entrada <= 'z':
        print('verdadeiro')

    elif 'A' <= entrada <= 'Z':
        print('verdadeiro')

    elif '0' <= entrada >= '9':
        print('verdadeiro')

    else:
        print('falso')


def main():
    entrada = input()
    caractere(entrada)


if __name__=='__main__':
    main()
