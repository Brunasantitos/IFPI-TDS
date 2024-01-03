def calcula_media_ponderada(n1, n2, n3, p1, p2, p3):
    return (n1 * p1 + n2 * p2 + n3 * p3) / (p1 + p2 + p3)

def calcula_media_aritmetica(n1, n2, n3):
    return (n1 + n2 + n3) / 3.0

def validar_numero(num):
    if type(num) != int and type(num) != float:
        return Exception
    if num < 0 or num > 10:
        return Exception

def calcula_media(n1, n2, n3, letra):
    if Exception in (validar_numero(n1), validar_numero(n2), validar_numero(n3)):
        return Exception
    if letra == "A":
        return calcula_media_aritmetica(n1, n2, n3)
    if letra == "P":
        return calcula_media_ponderada(n1, n2, n3, 5, 3, 2)
    return Exception


assert calcula_media(3, 4, 5, "X") == Exception
assert calcula_media("A", 4, 5, "P") == Exception
assert calcula_media(3, 4, 5, 6) == Exception
assert calcula_media(30, 4, 5, "A") == Exception
assert calcula_media(3, 40, 5, "A") == Exception
assert calcula_media(3, 4, 50, "A") == Exception
assert calcula_media(30, 4, 5, "P") == Exception
assert calcula_media(3, 40, 5, "P") == Exception
print('Testes ok!')