def tempo_duracao(tempo):
    if type(tempo) == str:
        return Exception
    elif tempo < 0:
        return Exception
    elif tempo >= 0:
        h = tempo // 3600
        min = (tempo % 60) // 60
        seg = tempo % 60
        return (h,min,seg)
        #print(f'{h},{min},{seg}')
    
assert tempo_duracao('h') == Exception
assert tempo_duracao(3600) == (1,0,0)
assert tempo_duracao(0) == (0,0,0)
assert tempo_duracao(-1) == Exception
print('Testes ok!')

