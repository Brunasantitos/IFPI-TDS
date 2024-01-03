def fatorial(valor):
    if type(valor) != int:
        return Exception
    retorno = 1
    for i in range(1, valor):
        retorno += retorno * i
    return retorno

assert fatorial(5) == 120
assert fatorial(2.3) == Exception
assert fatorial('R') == Exception
print('Todos os testes OK!')