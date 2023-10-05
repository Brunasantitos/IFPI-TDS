import csv

with open('terrorismo.csv',"r") as arquivo_csv:
    arquivo = csv.reader(arquivo_csv)

    for linha in arquivo:
        print(linha)



    
