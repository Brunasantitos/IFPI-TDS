def valor_area(r):
    area = 3,14 * r**2
    return area

def valor_perimetro(r):
    perimetro = 3,14 * 2 * r
    return perimetro

def main():
    while True:
        try:

            r = int(input("Informe o valor do raio: "))
            print(f'\nO valor da area é{valor_area(r)}')
            print(f'\nO valor do perimetro é {valor_perimetro(r)}')
            break
        except:
            print(f'\nInforme valores válidos para a área e perímetro!')

if __name__=='__main__':
    main()