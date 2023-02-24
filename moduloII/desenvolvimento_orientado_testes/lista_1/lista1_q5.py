def entrada_altura(h):
    pass

def entrada_sexo(s):
    pass

def peso_ideal(h,s):
    if s == 1:
        peso = ((62.1*h) - 44.7)
        print(f'\nSeu peso idel é {peso:.2f}')
    elif s == 2:
        peso = ((72.7*h) - 58)
        print(f'\nSeu peso ideal é {peso:.2f}')

def main():
    while True:
            try:
                altura = float(input("Qual a sua altura: "))
            except:
                print("\nInforme uma altura válida!")

            try:
                sexo = int(input("\nInformeu seu sexo: [1]Feminno ou [2]Masculino: "))

                if sexo == 1 or sexo ==2:
                    peso_ideal(altura,sexo)
                    break
            except:
                print("\nInforme um valor válido para o seu sexo!")


if __name__=='__main__':
    main()

gov
catce.2022111mtds0088@aluno.ifpi.edu.br