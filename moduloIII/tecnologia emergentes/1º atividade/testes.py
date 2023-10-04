# QUESTÃO 1
#LETRA C
tuple([1,2,3])


carros = (
(
'Jetta Variant',
'Motor 4.0 Turbo',
2003,
False,
('Rodas de liga', 'Travas elétricas', 'Piloto automático')
),
(
'Passat',
'Motor Diesel',
1991,
True,
('Central multimídia', 'Teto panorâmico', 'Freios ABS')
)
)

# QUESTÃO 2
print(carros[1][4][2])
print(carros[0][4][0:2])

# QUESTÃO 3

print(carros[0][4][0])
print(carros[0][4][1])
print(carros[0][4][2])
print(carros[1][4][0])
print(carros[1][4][1])
print(carros[1][4][2])

#QUESTÃO 4

nomes = ['Passat', 'Crossfox', 'DS5', 'C4', 'Jetta']
kms = [15000, 12000, 32000, 8000, 50000]

for i in zip(nomes,kms):
    if ((i[1]<20000)):
        print(i(0))

# QUESTÃO 5

nomes = ['Passat', 'Crossfox', 'DS5', 'C4', 'Jetta']
kms = [15000, 12000, 32000, 8000, 50000]

dados = {}

for i in zip(nomes,kms):
    dados[i[0]] = {'km': i[1]}

print(dados)


# QUESTÃO 6

dados = {
    'Passat': {
    'ano': 2012,
    'km': 50000,
    'valor': 75000,
    'acessorios': ['Airbag', 'ABS']
    },
    'Crossfox': {
    'ano': 2015,
    'km': 35000,
    'valor': 25000
    }
}

# RESPOSTA A
if 'acessorios' not in dados['Crossfox']:
    print(True)

# RESPOSTA B
if 'acessorios' in dados['Passat']:
    print(True)

# RESPOSTA C
print(dados['Crossfox']['valor'])

#RESPOSTA D
print(dados['Passat']['acessorios'][1])

# QUESTÃO 7

dados = {'Jetta': 88000, 'Crossfox': 72000, 'DS5': 124000}

dados.update({'Passat': 85000, 'Fusca': 150000})

print(dados)

#QUESTÃO 8

dados = {
'Crossfox': {'valor': 72000, 'ano': 2005},
    'DS5': {'valor': 125000, 'ano': 2015},
    'Fusca': {'valor': 150000, 'ano': 1976},
    'Jetta': {'valor': 88000, 'ano': 2010},
    'Passat': {'valor': 106000, 'ano': 1998}
    }

for valor, detalhe in dados.items():
    if(detalhe['ano'] >= 2000):
        print(valor)


# QUESTÃO 9
#LETRA C

# QUESTÃO 10

dados = {
    'Crossfox': {'km': 35000, 'ano': 2005},
    'DS5': {'km': 17000, 'ano': 2015},
    'Fusca': {'km': 130000, 'ano': 1979},
    'Jetta': {'km': 56000, 'ano': 2011},
    'Passat': {'km': 62000, 'ano': 1999}
    }

def km_media(dados,ano_atual):

    for dados, detalhe in dados.items():
        ano_fabricacao = detalhe['ano']
        km_total = detalhe['km']
        anos_em_uso = ano_atual - ano_fabricacao
        km_media_anual = km_total / anos_em_uso

        print(km_media_anual)

def main():
    km_media(dados,2019)

if __name__=='__main__':
    main()


        
    