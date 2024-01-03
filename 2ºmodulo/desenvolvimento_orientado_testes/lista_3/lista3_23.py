def valor_s(n):
    if type(n) != int:
        return Exception
    s = 0
    for i in range(1, n + 1):
        s += (i ** 2 + 1) / (i + 3)
    return s

assert valor_s(12) == 56.8489565989566
assert valor_s(5) == 8.845238095238095
assert valor_s(8) == 23.865440115440116
assert valor_s(4.5) == Exception
assert valor_s('3.2') == Exception
assert valor_s('*') == Exception
print('Todos os testes OK!')