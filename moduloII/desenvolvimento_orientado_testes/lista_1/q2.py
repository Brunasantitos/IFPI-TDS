def valor_area(r):
    area = 3,14 * r**2
    print(f'\nO valor da área é {area}.')

def valor_perimetro(r):
    perimetro = 3,14 * 2 * r
    print(f'\nO valor do perimetro é {perimetro}')

def main():
    r = int(input("Informe o valor do raio: "))
    valor_area(r)
    valor_perimetro(r)

if __name__=='__main__':
    main()