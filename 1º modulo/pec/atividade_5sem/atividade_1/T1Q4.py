def numeros_lidos(numero):
    
    maximo = max(numero) #retorna o max de um numero
    minimo = min(numero) #retorna o minimo de um numero

    a, b, c, d, e = int(numero[0]), int(numero[1]), int(numero[2]), int(numero[3]), int(numero[4])

    media = (a + b + c + d + e) / 5
    print(maximo, minimo, media)

def main():
    numero = input() .split()
    numeros_lidos(numero)

if __name__=='__main__':
    main()

# alguns outros modulos:

'''
ORD: retorna código do caractere recebido (entrada seria strings)
ABS: retorna o valor absoluto de um número
CHR: retorna código do caractere recebido (entrada seria numeros)
LEN: quantidade de caracteres
'''
