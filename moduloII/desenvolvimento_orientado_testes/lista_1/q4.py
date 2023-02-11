def media_aluno(nota):
    if nota >= 6:
        print("PARABÉNS! Você foi aprovado!")
    else:
        print("Você foi reprovado!")
        
def main():
    nota = float(input("Informe a nota do aluno: "))
    media_aluno(nota)

if __name__=='__main__':
    main()