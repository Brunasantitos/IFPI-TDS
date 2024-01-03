def primeira_linha(arquivo): #1
    print("Primeiras linhas do dataset:")
    print(arquivo.head())

def verificar_numero_de_linhas_colunas(arquivo): #2
    print("\nNúmero de linhas e colunas:")
    print(arquivo.shape)

def tipos_dados(arquivo): #3
    print("\nTipos de dados de cada coluna:")
    print(arquivo.dtypes)

#LIMPEZA DE DADOS

def valores_faltante(arquivo): #4
    print("\nValores faltantes por coluna:")
    print(arquivo.isnull().sum())

def remover_dados_duplicados(arquivo): #5
    arquivo.drop_duplicates(inplace=True)
    print("\nRemovido os dados duplicados:")
    print(arquivo.shape)

#ANALISE EXPLORATORIA

def variedades_de_vinhos(arquivo): #6
    variedades_dados = arquivo['variety'].value_counts().head(10)
    print("\nAs 10 variedades de vinho mais comuns:")
    print(variedades_dados)

def pontuacao_media_vinhos(arquivo): #7
    media_vinhos = arquivo.groupby('country')['points'].mean()
    print("\nPontuação média dos vinhos por país:")
    print(media_vinhos)

def vinhos_mais_caros(arquivo): #8
    vinhos = arquivo.nlargest(10, 'price')
    print("\nOs 10 vinhos mais caros:")
    print(vinhos[['title', 'price']])

def vinhos_mais_baratos(arquivo): #9
    vinhos_baratos = arquivo.nsmallest(10, 'price')
    print("\nOs 10 vinhos mais baratos:")
    print(vinhos_baratos[['title', 'price']])

def preco(arquivo): #10
    preco_vinhos = arquivo['price'].corr(arquivo['points'])
    print("\nCorrelação entre preço e pontuação:")
    print(preco_vinhos)
'''
insights que eu obtive através do dataset foram:
Variedades de Vinho Mais Comuns
Pontuação Média por País
Vinhos Mais Caros e Mais Baratos
'''
def main():
    import pandas as pd

    dados_arquivos = 'winemag-data-130k-v2.csv'
    arquivo = pd.read_csv(dados_arquivos, index_col=0)

    #primeira_linha(arquivo)
    #verificar_numero_de_linhas_colunas(arquivo)
    #tipos_dados(arquivo)
    #valores_faltante(arquivo)
    #remover_dados_duplicados(arquivo)
    #variedades_de_vinhos(arquivo)
    #pontuacao_media_vinhos(arquivo)
    #vinhos_mais_caros(arquivo)
    #vinhos_mais_baratos(arquivo)
    #preco(arquivo)

if __name__=='__main__':
    main()

