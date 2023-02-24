class Gato():
    nome = None
    raca = None
    peso = None
    idade = None

    def mudar_nome(self,nome):
        self.nome=nome

    def engordar(self,peso):
        self.peso+=peso

    def envelhecer(self,idade):
        self.idade += 1


meu_gato=Gato()
meu_gato.nome = 'mimi'
meu_gato.raca = 'siames'
meu_gato.idade = 2
meu_gato.peso = 1
meu_gato.mudar_nome('tom')
meu_gato.engordar(3)
meu_gato.envelhecer()

print(f'\nnome {meu_gato.nome}')
print('engordar {}'.format (meu_gato.engordar))
print('nenvelhecer {}'.format(meu_gato.envelhecer))
