def tempo_duracao(tempo):
    if type(tempo) == str:
        return Exception
    elif tempo < 0:
        return Exception
    elif tempo >= 0:
        h = tempo // 3600
        seg = 3600
        min = seg //60
        return f'{h}:{min}:{seg}'
    
#assert tempo_duracao('h') == Exception
assert tempo_duracao(3600) == (1,0,0)
#assert tempo_duracao(0) == 0:0:0
#assert tempo_duracao(119) == 2:59:1
print('Testes ok!')