def dadosPopulacao(salario,nFilhos):

    if len(salario) != 0 or len(nFilhos) == 0:
        print("ok 1 if")
    
    if len(salario) != len(nFilhos):
        print("ok 2 if")

    somaSalario = somaFilhos = soma350 = 0

    for i in range(len(salario)):

        if type(salario[0]) != float or salario[i] <= 0:
            print("ok 3 if")
        
        if type(nFilhos[i]) != int or nFilhos[i] < 0 or nFilhos[i] >= 20:
            print("ok 4 if")
        
        if salario[i] <= 350:
            soma350 += 1

        somaSalario += salario[i]
        somaFilhos += nFilhos[i]

        print(f'{somaSalario} / {len(salario)}, {somaFilhos} / {len(nFilhos)}, {max(salario)}')
def main():
    dadosPopulacao(["2"],[0])
    dadosPopulacao([100],[0])


main()