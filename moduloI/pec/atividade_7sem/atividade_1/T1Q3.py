def sinal_transito(cor):
    if cor == 'V':
        print("Siga")

    elif cor == 'A':
        print("Atenção")

    elif cor == 'E':
        print("Pare")

def main():
    cor = input().upper()
    sinal_transito(cor)

if __name__=='__main__':
    main()
