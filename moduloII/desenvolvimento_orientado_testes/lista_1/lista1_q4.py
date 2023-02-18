def media_aluno(nota):
    if nota >= 6:
        print("\nPARABÉNS! Você foi aprovado!")
    else:
        print("\nVocê foi reprovado!")
        
def main():
    while True:
        while True:
            try:

                nota = float(input("\nInforme a nota do aluno: "))
                media_aluno(nota)
                break
            except:
                print(f'\nInforme notas válidas!')
        continuar = input("\nDeseja continuar? [S]im ou [N]ão: ").upper()

        if continuar == 'N':
            break

if __name__=='__main__':
    main()