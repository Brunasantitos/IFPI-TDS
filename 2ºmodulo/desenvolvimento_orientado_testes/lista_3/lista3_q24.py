def valores(x, z):
    if type(x) != int or type(z) != int:
        return Exception
    
    return x ** z


assert valores(8, 4) == 4096
assert valores(35, 4) == 1500625
assert valores('e', 23) == Exception
print('Todos os testes OK!')