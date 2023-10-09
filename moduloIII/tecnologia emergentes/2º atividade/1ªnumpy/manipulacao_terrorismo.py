import csv 
import numpy as np

class Terrorismo:
    
    def __init__(self, arquivo):
        self.arquivo = arquivo

    def maiorPorcentagem(self):
        cidades = self.arquivo[:, 0]
        ataques = self.arquivo[:, 1].astype(int)
        maior_ataque = np.max(ataques)
        cidade_maior_ataque = cidades[np.argmax(ataques)]
        print(f'Maior número de incidentes: {maior_ataque}, na cidade: {cidade_maior_ataque}')
    
    def numeroMortos(self):
        cidades = self.arquivo[:, 0]
        mortos = self.arquivo[:, 3].astype(int)
        maior_numero_mortos = np.max(mortos)
        cidade_maior_mortos = cidades[np.argmax(mortos)]
        print(f'Maior número de mortos: {maior_numero_mortos}, na cidade: {cidade_maior_mortos}')
    

def main():
    
    arquivo = np.genfromtxt('terrorismo.csv', delimiter=',', skip_header=1, missing_values='')
    Cidade = Terrorismo(arquivo)
    Cidade.maiorPorcentagem()
    Cidade.numeroMortos()

if __name__=='__main__':
    main()
