def valor_s(n):
    if type(n) != int:
        return Exception
    s = 0
    for i in range(1, n + 1):
        s += 1 / i
    return s

assert valor_s(24) == 3.7759581777535067
assert valor_s(8) == 2.7178571428571425
assert valor_s(2.4) == Exception
assert valor_s('r') == Exception
print('Todos os testes OK!')