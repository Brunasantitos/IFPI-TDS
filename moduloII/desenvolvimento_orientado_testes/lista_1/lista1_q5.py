def entrada_altura(altura):
   while True:
        try:
            altura
            break
       
        except:
            print("Informe valores válidos")

def entrada_sexo(sexo, h):
    while True:
        try:
            if sexo == 1:
                peso = ((62.1*h) - 44.7)
                print(f'\nSeu peso idel é {peso:.2f}')
            elif sexo == 2:
                peso = ((72.7*h) - 58)
                print(f'\nSeu peso ideal é {peso:.2f}')
            break
          
        except:
            print("Informe os valores válidos")

        break

def main():
    altura = float(input("Qual a sua altura: "))
    sexo = int(input("\nInformeu seu sexo: [1]Feminno ou [2]Masculino: "))

    entrada_altura(altura)
    entrada_sexo(sexo, entrada_altura)

if __name__=='__main__':
    main()