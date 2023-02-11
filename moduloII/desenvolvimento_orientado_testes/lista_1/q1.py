def numero_par(entradaDados):
    if entradaDados % 2 == 0:
        valor = bool(entradaDados)
        print(f'{valor}, o número {entradaDados} é par.')
        
    else:
        print(f'False, o número {entradaDados} é ímpar.') 

def main():
    entradaDados = int(input())
    numero_par(entradaDados)

if __name__=='__main__':
    main()