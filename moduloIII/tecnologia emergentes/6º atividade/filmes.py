import pandas as pd


def generos_filmes(arquivo):
    generos = arquivo.groupby('genres').size()
    print(f'{generos}')

def nota(arquivo_notas):
    notinhas = arquivo_notas['rating'].min()
    print(f'menor nota {notinhas}')

def media_notas(arquivo_notas):
    notinhas = arquivo_notas['rating'].mean()
    print(f'media das notas \n {notinhas}')

def mediana_notas(arquivo_notas):
  notinhas = arquivo_notas['rating'].median()
  print(f'Mediana das notas \n {notinhas}')

def filmes_cadastrados(arquivo):
    i = 0
    for i in arquivo['movieId']:
      i += i
    print(f'Quantidade de filmes cadastrados {i}')

def quantidade_notas(arquivo_notas):
  i = 0
  for i in arquivo_notas['rating']:
    i += i
  print(f'Quantidade de avaliações {i}')
  
def filmes_nota_minima(filmes,notas):
  filmes_com_notas = pd.merge(filmes,notas, on = 'movieId')
  notas_minimas = filmes_com_notas[filmes_com_notas['rating'] == filmes_com_notas['rating'].min()]
  print(notas_minimas[['movieId','title','rating']])

def filmes_nota_maxima(filmes,notas):
  filmes_notas_maximas = pd.merge(filmes,notas, on = 'movieId')
  notas_maximas = filmes_notas_maximas[filmes_notas_maximas['rating'] == filmes_notas_maximas['rating'].max()]
  print(notas_maximas[['movieId','title','rating']])

def filmes_avaliacoes_minima(filmes,notas):
  filmes_avaliacoes = pd.merge(filmes,notas, on = 'movieId')
  avaliacoes_minimas = filmes_avaliacoes[filmes_avaliacoes['timestamp'] == filmes_avaliacoes['timestamp'].min()]
  print("Filmes com menos avaliações")
  print(avaliacoes_minimas[['movieId','title','timestamp']])

def filmes_avaliacoes_maxima(filmes,notas):
  filmes_avaliacoes_maximas = pd.merge(filmes,notas, on = 'movieId')
  avaliacoes_maximas = filmes_avaliacoes_maximas[filmes_avaliacoes_maximas['timestamp'] == filmes_avaliacoes_maximas['timestamp'].max()]
  print("Filmes com mais avaliações")
  print(avaliacoes_maximas[['movieId','title','timestamp']])
 
def media_avaliacoes_melhores(filmes,notas):
  filmes_avaliacoes = pd.merge(filmes,notas, on = 'movieId')
  media = notas.groupby('movieId')['rating'].mean()
  melhores_avaliacoes = media.max()
  print("Filmes com melhores avaliações")
  print(melhores_avaliacoes[['movieId','title','rating']])
  

def media_avaliacoes_piores(filmes,notas):
  filmes_avaliacoes = pd.merge(filmes,notas, on = 'movieId')
  media = filmes_avaliacoes.groupby('movieId')['rating'].mean()
  piores_avaliacoes = media[media['rating'] == media['rating'].min()]
  print("Filmes com melhores avaliações")
  print(piores_avaliacoes[['movieId','title','rating']])

def main():
    uri_filmes = "https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula0/ml-latest-small/movies.csv"
    filmes = pd.read_csv(uri_filmes)

    uri_notas = "https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula0/ml-latest-small/ratings.csv"
    notas = pd.read_csv(uri_notas)
    
    generos_filmes(filmes)
    nota(notas)
    media_notas(notas)
    mediana_notas(notas)
    filmes_cadastrados(filmes)
    quantidade_notas(notas)
    filmes_nota_minima(filmes,notas)
    filmes_nota_maxima(filmes,notas)
    filmes_avaliacoes_minima(filmes,notas)
    filmes_avaliacoes_maxima(filmes,notas)
    media_avaliacoes_melhores(filmes,notas)
    media_avaliacoes_piores(filmes,notas)
if __name__=='__main__':
    main()
    
