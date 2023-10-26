import csv
import numpy as np

class Fruta:

    def __init__(self,arquivo):
        self.arquivo = arquivo

    def Moscow(self):
        
        for i,linha in enumerate(self.arquivo):
            if i == 0:
                print(f'A cidade de Moscow, vendeu essas quantidades de maças de acordo com os anos {linha}')

    def Kellningrad(self):
        for i,linha in enumerate(self.arquivo):
            if i == 1:
                print(f'A cidade de Kellningrad, vendeu essas quantidades de maças de acordo com os anos {linha}')

    def Petersburg(self):
        for i,linha in enumerate(self.arquivo):
            if i == 2:
                print(f'A cidade de Petersburg, vendeu essas quantidades de maças de acordo com os anos {linha}')

    def Krasnodar(self):
        for i,linha in enumerate(self.arquivo):
            if i == 3:
                print(f'A cidade de Krasnodar, vendeu essas quantidades de maças de acordo com os anos {linha}')

    def Ekaterinburg(self):
        for i,linha in enumerate(self.arquivo):
            if i == 4:
                print(f'A cidade de Ekaterinburg, vendeu essas quantidades de maças de acordo com os anos {linha}')


def main():
    with open('apples_ts.csv',"r") as arquivo_csv:
        arquivo = csv.reader(arquivo_csv)
        arquivo = np.loadtxt('apples_ts.csv', delimiter=',',dtype=str)#loadtxt
        VendasMaca = Fruta(arquivo)
        VendasMaca.Moscow()
        VendasMaca.Kellningrad()
        VendasMaca.Petersburg()
        VendasMaca.Krasnodar()
        VendasMaca.Ekaterinburg()
        
        
      
if __name__=='__main__':
    main()
