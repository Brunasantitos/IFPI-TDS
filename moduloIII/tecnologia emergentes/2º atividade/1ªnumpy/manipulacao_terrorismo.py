import csv

with open('terrorismo.csv',"r") as arquivo_csv:
    arquivo = csv.reader(arquivo_csv)

    for linha in arquivo:
        print(linha)

# criar dois metodos que mostres as cidades com mais ataques e a cidade com menos ataques



    
