def piso_sala(largura, comprimento):
    area_do_piso = largura*comprimento
    print(f'\nArea do piso da sala: {area_do_piso}')

def volume_sala(largura, comprimento, altura):
    volume_da_sala = largura * comprimento * altura
    print(f'\nVolume da sala: {volume_da_sala}')

def parede_sala(altura, largura,comprimento):
    area_das_paredes = 2 * altura * largura + 2 * altura * comprimento
    print(f'\nArea das paredes: {area_das_paredes}')

def main():
    altura = float(input("Informe a altura da sala: "))
    comprimento = float(input("Informe o comprimento da sala: "))
    largura = float(input("Informe a largura da sala: "))
    piso_sala(largura, comprimento)
    volume_sala(largura, comprimento, altura)
    parede_sala(altura, largura,comprimento)

if __name__=='__main__':
    main()
    

