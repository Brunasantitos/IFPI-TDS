import pandas as pd

def tipo_dados(arquivo):
    print(arquivo.dtypes)

def estatisticas_das_colunas(arquivo):
    pass

def informacoes(arquivo):
    print(arquivo.info())
    print(100*'_')

def km_media(arquivo,ano_atual):
    #pegar a media de cada carro: km / (2023 - ano)
    #coluna 2 Ano e 3 Quilometragem
    km_media = arquivo['Quilometragem']/(ano_atual-arquivo['Ano']) 
    print(km_media)
    print(100*'_')

def motor_diesel(arquivo):
    valor_motor = carros.loc[carros['Motor'] == 'Diesel V8']
    print(valor_motor)

def main():
    arquivo = pd.read_csv('carros.csv', sep=';')
    tipo_dados(arquivo)
    estatisticas_das_colunas(arquivo)
    informacoes(arquivo)
    km_media(arquivo,2023)
    motor_diesel(arquivo)


if __name__=='__main__':
    main()
