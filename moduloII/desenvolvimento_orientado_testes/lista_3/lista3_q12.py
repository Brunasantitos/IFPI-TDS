def funcao_crescente(n1,n2):
    if type(n1) != int or type(n2) != int:
        return Exception
    elif n1 <= n2:
        return n1,n2
    else:
        return n2,n1
        
assert funcao_crescente(4,5) == (4,5)
assert funcao_crescente('a',5) == Exception
assert funcao_crescente(4.5,5) == Exception
assert funcao_crescente(58,1) == (1,58)
assert funcao_crescente('49',5) == Exception
print('Teste ok!')