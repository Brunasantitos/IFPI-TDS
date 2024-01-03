def quadrado(lado_quadrado):
    area_quadrado = lado_quadrado * lado_quadrado
    print(f'Area do quadrado é {area_quadrado:10.4f}')

def perimetro_quadrado(lado_quadrado):
    perimetro = lado_quadrado * 4
    print(f'Seu perímetro é {perimetro:10.4f}')

def main():
    lado_quadrado = float(input("Informe o valor do lado do quadrado: "))
    quadrado(lado_quadrado)
    perimetro_quadrado(lado_quadrado)

if __name__=='__main__':
    main()
