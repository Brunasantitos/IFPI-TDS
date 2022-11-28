def showResult(n1, n2, n3):
    soma = n1 + n2 + n3
    media = soma / 3
    if (n3 > 8): media = media + 1
    if (media > 10): media = 10
    return media

def main():
    nota1 = float(input().strip())
    nota2 = float(input().strip())
    nota3 = float(input().strip())
    print(f'{showResult(nota1, nota2, nota3):0.2f}')

if __name__ == "__main__":
    main()
