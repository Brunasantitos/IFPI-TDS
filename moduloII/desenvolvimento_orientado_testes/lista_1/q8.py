def caracteresValidos(caractere):
    
    while True:

        try:
            valor_inteiiro = int(caractere)

            if 0 <= valor_inteiiro >= 0:
                print(f'\nO cubo de {caractere} é {valor_inteiiro**2}')
                break

        except:
                
                if (caractere.upper()) != 'S' or (caractere.upper()) != 'N':
                    print('Caractere inválido! Digite novamente.')

                elif caractere.upper() == 'N':
                    break


def main():
    caractere = input("Informe um número: ")
    caracteresValidos(caractere)

if __name__=='__main__':
    main()