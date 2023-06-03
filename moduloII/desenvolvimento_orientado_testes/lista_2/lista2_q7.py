def lista_numerica(L1):
    valor = float(input("Informe um valor: "))
    if valor in L1:
        print(f"O valor {valor} pertence à lista.")
    else:
        print(f"O valor {valor} não pertence à lista.")

def  main():
    
    L1 = [5,0.5,0,25,36,14,25,9]

    lista_numerica(L1)

if __name__=='__main__':
    main()