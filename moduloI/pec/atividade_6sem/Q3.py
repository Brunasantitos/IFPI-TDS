def consoantes(caractere):
    if 'a' <= caractere <= 'z':
        print('verdadeiro')

    elif 'A' <= caractere <= 'Z':
        print('verdadeiro')

    else:
        print('falso')
        
def main():
    caractere = input()
    consoantes(caractere)

if __name__=='__main__':
    main()
