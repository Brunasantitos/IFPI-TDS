def valor_primo(valor):
    if type(valor) == str:
        return Exception
    elif type(valor) == float:
        return Exception
    elif valor < 0:
        return Exception
    elif valor % 2 != 0:
        return Exception
    elif valor % 2 == 0:
        return valor

assert valor_primo(3) == Exception
assert valor_primo(2) == 2
assert valor_primo('a') == Exception
assert valor_primo(5.3) == Exception
assert valor_primo(-5) == Exception
print('Teste ok!')