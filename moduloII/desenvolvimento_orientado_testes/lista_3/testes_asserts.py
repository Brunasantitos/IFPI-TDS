def entrada_sexo(sexo, h):
    while True:
        try:
            if sexo == 1:
                peso = ((62.1*h) - 44.7)
                print(f'\nSeu peso idel é {peso}')
            elif sexo == 2:
                peso = ((72.7*h) - 58)
                print(f'\nSeu peso ideal é {peso}')
            break
          
        except:
            print("Informe os valores válidos")

        break

def main():
    altura = float(input("Qual a sua altura: "))
    sexo = int(input("\nInformeu seu sexo: [1]Feminno ou [2]Masculino: "))

    entrada_sexo(sexo, altura)

if __name__=='__main__':
    main()
