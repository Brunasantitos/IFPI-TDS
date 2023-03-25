def DivisorNumero(numero):
    pass
    
        
            
def main():
    while True:
        try:
            numero = int(input("Informe um número para saber seus divisores: "))
            
            if numero > 0:
                DivisorNumero(numero)
                break
            
            elif numero < 0:
                print("Não é permitido número negativo")
                continue
        
        except:
            print("Informe apenas números")


if __name__=='__main__':
    main()
