class Pessoa:
    def __init__(self,nome,idade,peso,altura,estado="vivo(a)"):
        self.nome = nome
        self.__idade = idade
        self.peso = peso
        self.altura = altura
        self.__estado = estado
        
    def engordar(self,ganhar_peso):
        self.peso += ganhar_peso
        print('você engordou')
        
    def emagrecer(self,perder_peso):
        self.peso -= perder_peso
        print('você emagreceu')

    def altura(self,altura_atual):
        if self.idade <= 21:
            self.altura += altura_atual
            print('você cresceu')            
        
    @property
    def idade(self):
        return self.__idade
      
    @idade.setter
    def idade(self,valor):
        self.__idade += valor
        print('você está mais velho')


    def __str__(self):
        return f'Nome: {self.nome} \t Idade: {self.__idade} \t peso: {self.peso} \t altura: {self.altura}'

def menu():
  print('1-Listar pessoas')
  print('2-Nova Pessoa')
  print('3-Engordar')
  print('4-Emagrecer')
  print('5-Crescer')
  print('6-Casar')
  print('7-Morrer')
  print('8-Alterar idade')
  print('9-Fim')

def buscaPessoa(nome,pessoas):
  for i in pessoas:
    if i.nome == nome:
      return i
  return None


def main():
  pessoas = [Pessoa("Maria",5,75,162),Pessoa("Pedro",22,54,152)]

  while True:
    menu()
    opcao = int(input("opção:"))

    if opcao == 1:
        for i in pessoas:
          print(i)

    if opcao == 2:
        pessoas.append(Pessoa(input('nome: ')),int(input('idade: ')),int(input('peso: ')),int(input('altura: ')))

    if opcao == 3:
        nome = input("Qual o nome da pessoa?")
        p = buscaPessoa(nome,pessoas)
        if p!=None:
            ganhar_peso = int(input('Informe o peso: '))
            p.engordar(ganhar_peso)
        else:
            print("Pessoa não encontrada!")

    if opcao == 4:
        nome = input("Qual o nome da pessoa?")
        p = buscaPessoa(nome,pessoas)
        if p!=None:
            perder_peso = int(input('Informe o peso: '))
            p.emagrecer(perder_peso)
        else:
            print("Pessoa não encontrada!")

    if opcao == 5:
        nome = input("Qual o nome da pessoa?")
        p = buscaPessoa(nome,pessoas)
        if p!=None:
            altura_atual = int(input('Informe a altura: '))
            p.altura(altura_atual)
        else:
            print("Pessoa não encontrada!")
        

    if opcao == 8:
        nome = input("Qual o nome da pessoa?")
        p = buscaPessoa(nome,pessoas)
        if p!=None:
            p.idade = int(input('Informe a idade: '))
        else:
            print("Pessoa não encontrada!")
    elif opcao==9:
        break;

if __name__ == '__main__':
    main()

#pedro = Pessoa("Pedro",22)
#pedro.idade = 50





