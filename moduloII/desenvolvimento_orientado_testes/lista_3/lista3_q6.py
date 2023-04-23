def perfect(value):
  if type(value) != int:
    return Exception
  else:
    divider = 0
    for c in range(1,value):
      if value%c == 0:
            divider += c
    if divider == value:
      return True
    else:
      return False    
    
assert perfect(6) == True
assert perfect(3) == False
assert perfect(4.3) == Exception
assert perfect('sete') == Exception
assert perfect(True) == Exception
assert perfect(7) == False

print('testes ok!')
