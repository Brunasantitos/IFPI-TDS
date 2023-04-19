class Eletrodomestico:
    def __init__(self, marca, ano, modelo, cor, capacidade_liquida, temperatura_minima, temperatura_maxima, temperatura_atual, desligado):
        self.marca = marca
        self.ano = ano
        self.modelo = modelo
        self.cor = cor
        self.capacidade_liquida = capacidade_liquida
        self.temperatura_minima = temperatura_minima
        self.temperatura_maxima = temperatura_maxima
        self.tempertaura_atual = temperatura_atual
        self. desligado = desligado

    def estado_eletro(self):

        if self.desligado == True:
            print(f'\nGeladeira ligada.')
            print(f'\nTemperatura minima {self.temperatura_minima}')
            print(f'\nTemperatura máxima {self.temperatura_maxima}')

        elif self.desligado == False:
            print(f'\nGeladeira desligada.')

def main():
    geladeira = Eletrodomestico('samsung', 2019, 'frost free', 'branco', 345, 1, 18, True)
    geladeira.estado_eletro()

if __name__=='__main__':
    main()


