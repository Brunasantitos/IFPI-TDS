def lados(valor,medidas):
    if valor == 3:
        perimetro = 3 * medidas
        print(f'\nTRIÂNGULO e o valor do seu perímetro {perimetro}.')
    elif valor == 4:
        area = medidas**2
        print(f'\nQUADRADO e o valor da sua área {area}. ')
    elif valor == 5:
        print("\nPENTÁGONO")
def main():
    valor = int(input("Quantidade de lados: "))
    medidas = float(input("\nMedidas dos lados em cm: "))
    lados(valor,medidas)

if __name__=='__main__':
    main()