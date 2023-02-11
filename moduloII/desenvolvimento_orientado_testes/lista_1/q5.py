def peso_ideal(s,h):
    if s == 1:
        peso = ((62.1*h) - 44.7)
        print(f'\nSeu peso idel é {peso:.2f}')
    elif s == 2:
        peso = ((72.7*h) - 58)
        print(f'\nSeu peso ideal é {peso:.2f}')

def main():
    altura = float(input("Qual a sua altura: "))
    sexo = int(input("\n1-Feminino\n2-Masculino"))
    peso_ideal(sexo, altura)

if __name__=='__main__':
    main()