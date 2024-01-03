
def duracao_evento_em_horas(duracao_segundos):
    horas = duracao_segundos // 3600
    minutos = (duracao_segundos // 60) % 60
    segundos = duracao_segundos % 60

    if horas < 10: horas = '0' + str(horas)
    if minutos < 10: minutos = '0' + str(minutos)
    if segundos < 10: segundos = '0' + str(segundos)
    print(f'{horas}:{minutos}:{segundos}')


def main():
    duracao_segundos = int(input())
    duracao_evento_em_horas(duracao_segundos)


if __name__=='__main__':
    main()

