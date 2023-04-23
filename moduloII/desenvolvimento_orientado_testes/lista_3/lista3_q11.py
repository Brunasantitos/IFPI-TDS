def entrada_sexo(sexo, h):
        if type(sexo) != int or type(h) != float:
             return Exception
        elif sexo >=3:
            return Exception
        elif h <= 0:
             return Exception
        elif sexo == 1:
            peso = ((62.1*h) - 44.7)
            return peso
        elif sexo == 2:
            peso = ((72.7*h) - 58)
            return peso
        
assert entrada_sexo('feminino', 5) == Exception
assert entrada_sexo(1,1.62) == 55.902
assert entrada_sexo(2,1.75) == 69.22500000000001
assert entrada_sexo(3,1.62) == Exception

print('testes ok!')
  