def divisores(valor):
    if type(valor) != int or valor < 0:
        return Exception
    divisores = 0
    for n in range(1, valor):
        if valor % n == 0:
            divisores += 1
            
    return divisores

assert divisores(6) == 3
assert divisores(12) == 5
assert divisores(-2) == Exception
assert divisores('X') == Exception
print('Todos os testes OK!')