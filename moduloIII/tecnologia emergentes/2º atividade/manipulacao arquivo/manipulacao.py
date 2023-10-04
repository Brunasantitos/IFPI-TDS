import csv

with open("drinks.csv", "r") as arquivo:
    arquivo_csv = csv.reader(arquivo, delimiter=",")

    for linha in arquivo_csv:
        print(linha)



