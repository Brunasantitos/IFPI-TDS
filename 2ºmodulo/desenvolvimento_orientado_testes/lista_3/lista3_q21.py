def valor_s(n):
    if type(n) != int:
        return Exception
    s = 1 + 1/2 + 1/3 + 1/4 + 1/5 + 1/n
    return s

assert valor_s(5) == 2.4833333333333334
assert valor_s(2.3) == Exception
assert valor_s('3') == Exception
assert valor_s('Z') == Exception
print('Todos os testes OK!')