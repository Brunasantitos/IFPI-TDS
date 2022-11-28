tempo_funcionario = float(input("Informe o tempo de empresa: "))

valor_bonus_funcionario = float(input("Informe o valor da bonificação por ano trabalhado: "))
bonificação = (valor_bonus_funcionario * tempo_funcionario)

print(f'{tempo_funcionario:.2f} de tempo trabalhado, receberá {bonificação:.2f} de bônus.')
