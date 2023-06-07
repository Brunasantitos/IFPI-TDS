def somatorio(valor):
    if type(valor) != int or valor < 0:
        return Exception
    
    soma = 0
    for i in range(0, valor+1):
        soma += i
    
    return soma

assert somatorio(5) == 15
assert somatorio('a') == Exception
assert somatorio(-2) == Exception
assert somatorio('*') == Exception
print('Todos os testes OK!')