import csv

class Terrorismo:
    def __init__(self,arquivo):
        self.arquivo = arquivo

    def maisIncidentes(self):
        for linha in self.arquivo:
            
            print(linha[1])

def main():
    with open('terrorismo.csv', 'r', newline='') as csvfile:
        arquivo = csv.reader(csvfile, delimiter=',')
        next(arquivo)

        Cidade = Terrorismo(arquivo)
        Cidade.maisIncidentes()

if __name__=='__main__':
    main()
    
