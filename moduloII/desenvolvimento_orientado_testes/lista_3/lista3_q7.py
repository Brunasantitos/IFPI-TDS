def definir_categoria(idade):
    if type(idade) != int:
        return Exception
    if idade >= 5 and idade <= 7:
        categoria = "Infantil A"
    elif idade >= 8 and idade <=10:
        categoria = "infanitl B"
    elif idade >= 11 and idade <= 13:
        categoria = "juvenil A"
    elif idade >= 14 and idade <= 17:
        categoria = "juvenil B"
    elif idade >= 17 and idade <= 120:
        categoria = "adulto"
    else:
        return Exception
    return categoria
assert definir_categoria("*") == Exception
assert definir_categoria(-1) == Exception
assert definir_categoria(10.35) == Exception
assert definir_categoria(4) == Exception
assert definir_categoria(400) == Exception
assert definir_categoria(20) == "adulto"

print('Testes OK')