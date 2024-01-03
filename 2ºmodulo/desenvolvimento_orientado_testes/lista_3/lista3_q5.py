def idade(anos, meses, day):
  if type(anos) != int or type(meses) != int or type(day) != int or type(anos) == str or type(meses) == str or type(day) == str or anos < 0 or meses < 0  or day < 0:
    return Exception
  else:
    ano = anos*365
    mes = meses*30
    dia = day
    dias = ano + mes + day
    return dias

assert idade(1,1,1) == 396
assert idade(1,0,0) == 365
assert idade(2,0,0) == 730
assert idade(-1,3,4) == Exception
assert idade(1,-30,3) == Exception
assert idade(1.23,42,3) == Exception
assert idade(1,89.2,45) == Exception
assert idade(1,4,-78) == Exception
assert idade('1 ano',4,7) == Exception

print('Todos ok!')
