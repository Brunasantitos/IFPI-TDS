def tempo_duracao(tempo):
    if type(tempo) == str:
        return Exception
    elif tempo < 0:
        return Exception
    elif tempo >= 0:
        h = tempo / 60
        min = tempo%60
        seg = (min%60)/60
        return f'{h}:{min}:{seg}'
    
assert tempo_duracao('h') == Exception
#assert tempo_duracao(659) == 11:59:1
#assert tempo_duracao(0) == 0:0:0
#assert tempo_duracao(119) == 2:59:1
print('Testes ok!')