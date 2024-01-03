def media(media_final):
  if type(media_final) != float:
    return Exception
  
  else:
    if media_final >= 7.0 and media_final <= 8.9:
      return 'B'
    elif media_final >= 0.0 and media_final <= 4.9:
      return 'D'
    elif media_final >= 5.0 and media_final <= 6.9:
      return 'C'
    elif media_final >= 9.0 and media_final <= 10.0:
      return 'A'

assert media(7.0) == 'B'
assert media(7) == Exception
assert media(-9) == Exception
assert media(2.3) == 'D'
assert media(5.5) == 'C'
assert media(10.0) == 'A'
assert media('nota boa') == Exception
assert media(False) == Exception
print('testes OK')
