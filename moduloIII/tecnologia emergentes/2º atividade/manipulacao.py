import csv

with open('drinks.csv',"r") as arquivo_csv:
    arquivo = csv.reader(arquivo_csv)

    for linha in arquivo:
        print(linha)



        




