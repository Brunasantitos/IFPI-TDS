def somatorioNumero(numero):
     x = 0
     for i in range(1,numero+1):
         x = i + x
     print(f'\no somatorio de {i}, é {x}')

        

def main():
    while True:
        try:
            numero = int(input('Informe um número: '))
            somatorioNumero(numero)
            break
        except:
            print('Informe apenas números')

if __name__=='__main__':
    main()
