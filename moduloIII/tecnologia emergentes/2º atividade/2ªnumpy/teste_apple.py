import csv
import numpy as np

class Fruta:

    def __init__(self, arquivo):
        self.arquivo = arquivo

    def Moscow(self):
        print(self.arquivo[0])

    def Kellningrad(self):
        print(self.arquivo[1])

    def Petersburg(self):
        print(self.arquivo[2])

    def Krasnodar(self):
        print(self.arquivo[3])

    def Ekaterinburg(self):
        print(self.arquivo[4])

def main():
    with open('apples_ts.csv', "r") as arquivo_csv:
        csv_reader = csv.reader(arquivo_csv)
        # Converte os dados do CSV em uma lista de listas
        lista_de_listas = [linha for linha in csv_reader]

        # Converte a lista de listas em um array NumPy e substitui valores vazios por 0
        arquivo = np.array([[float(valor) if valor else 0 for valor in linha] for linha in lista_de_listas])

        VendasMaca = Fruta(arquivo)
        VendasMaca.Moscow()
        VendasMaca.Kellningrad()
        VendasMaca.Petersburg()
        VendasMaca.Krasnodar()
        VendasMaca.Ekaterinburg()

if __name__ == '__main__':
    main()
