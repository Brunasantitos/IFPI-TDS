def triangulo(valor,medidas):
    if valor == 3:
        perimetro = 3 * medidas
        print(f'\nTRIÂNGULO e o valor do seu perímetro {perimetro}.')
    if valor == 4:
        area = medidas**2
        print(f'\nQUADRADO e o valor da sua área {area}. ')
    if valor == 5:
        print("\nPENTÁGONO")

def main():
    while True:
        try:

            valor = int(input("Quantidade de lados: "))
            medidas = float(input("\nMedidas dos lados em cm: "))
            triangulo(valor,medidas)
            break
        except:
            print("\nInforme valores númericos!")

if __name__=='__main__':
    main()