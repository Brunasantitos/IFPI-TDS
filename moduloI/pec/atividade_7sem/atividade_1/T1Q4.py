def valor(caractere):
    if caractere <= 0 or caractere <= 9:
        print(True)
    else:
        print(False)

def main():
    caractere = int(input())
    valor(caractere)

if __name__=='__main__':
    main()
