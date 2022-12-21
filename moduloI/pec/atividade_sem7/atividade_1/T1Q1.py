
def AnoAtual(ano,ano_nascimento):
    if ano > ano_nascimento:
        ano_atual = ano - ano_nascimento
        print(f'{ano_atual} anos')

    elif ano < ano_nascimento:
        ANO_atual = ano_nascimento - ano
        print(f'{ANO_atual} anos')

    else:
        AnoAtual= ano - ano_nascimento
        print(f'{AnoAtual} anos')


def mesDataAtual(mes, mes_nascimento):
    if mes > mes_nascimento:
        MesAtual = mes - mes_nascimento
        print(f'{MesAtual} mes(es)')

    elif mes < mes_nascimento:
        MESatual = mes_nascimento - mes
        print(f'{MESatual} mes(es)')

    else:
        MesAtual = mes - mes_nascimento
        print(f'{MesAtual} mes(es)')

def DiaAtual(dia,dia_nascimento):
    if dia>dia_nascimento:
        DiaAtual = dia - dia_nascimento
        print(f'{DiaAtual} dia(s)')

    elif dia_nascimento > dia:
        diaAtual = dia_nascimento - dia
        print(f'{diaAtual} dia(s)')

    else:
        DIAatual = dia - dia_nascimento
        print(f'{DIAatual} dia(s)')

    

def main():
    dia = int(input())
    mes = int(input())
    ano = int(input())

    dia_nascimento = int(input())
    mes_nascimento = int(input())
    ano_nascimento = int(input())

    AnoAtual(ano,ano_nascimento)
    mesDataAtual(mes, mes_nascimento)
    DiaAtual(dia,dia_nascimento)

if __name__=='__main__':
    main()

