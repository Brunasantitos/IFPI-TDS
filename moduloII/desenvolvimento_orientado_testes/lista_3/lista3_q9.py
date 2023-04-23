def valor(a):
  if type(a) != int:
    return Exception
  
  else:
    if a%2 == 0:
      return True
    else:
      return False

assert valor(2) == True
assert valor(-2) == True
assert valor(5) == False
assert valor(True) == Exception
assert valor(4.3) == Exception
assert valor('noventa e sete') == Exception
assert valor(0) == True
assert valor(-15) == False

print('testes OK')