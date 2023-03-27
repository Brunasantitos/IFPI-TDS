# LISTA 1 - QUESTÃO 14
"""
14. Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S.

S = 1 + 1/1! + 1/2! + 1/3! + 1 /N!
"""

def cacula_expressao(n):
    s = 1
    for i in range(1, n + 1):
        s += 1/fatorial(i)
    return s


def fatorial(k):
    acc = 1
    for i in range(k, 1, -1):
        acc *= i
    return acc


while True:
    try:
        numero = int(input('Digite um número inteiro positivo: '))
        while numero <= 0:
            print('>>>>Número inválido... por favor, digite um número positivo e maior que Zero.\n')
            numero = int(input('Digite um número inteiro positivo: '))
        print(f'O resultado da expressão é: {cacula_expressao(numero):.3f}')
        break
    except:
        print('Dado inválido! Por favor, digite novamente')