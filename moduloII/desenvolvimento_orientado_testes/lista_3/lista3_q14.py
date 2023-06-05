def valores(X,Y,Z):
    if type(X) == str or type(Y) == str or type(Z) == str:
        return Exception
    elif  type(X) == bool or type(Y) == bool or type(Z) == bool:
        return Exception
    elif X == Y == Z:
        return "Triângulo Equilátero!"
    elif X == Z or Y == Z or X == Y:
        return "Triângulo Isósceles!"
    elif X != Y and X != Z and Y != Z:
        return "Triângulo Escaleno!"
    


assert valores("4",2,5) == Exception
assert valores(7,7,7) == "Triângulo Equilátero!"
assert valores(7,7,3) == "Triângulo Isósceles!"
assert valores(4,2,1.0) == "Triângulo Escaleno!"
assert valores(1,2.1,1) == "Triângulo Isósceles!"
assert valores(True,2,7) == Exception
print("Testes ok!")