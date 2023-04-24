def raio_esfera(r):
    if type(r) == str:
        return Exception
    elif r <=0:
        return Exception
    return 4/3 * 3.14 * r**3 


assert raio_esfera('b') == Exception
assert raio_esfera(-4) == Exception
assert raio_esfera(5) == 523.3333333333334
assert raio_esfera(7.1) == 1498.4540533333331
print("Teste ok!")

