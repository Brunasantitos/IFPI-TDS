def duracao_jogo(hora_inicio,hora_final):
    if type(hora_inicio) != int or type(hora_final) != int:
        return Exception
    

assert duracao_jogo('a',5) == Exception
print('Testes ok!')