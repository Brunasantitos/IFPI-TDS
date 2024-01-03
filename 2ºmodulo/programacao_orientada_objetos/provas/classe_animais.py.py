class Animal:
    def __init__(self,novo_animal,som_animal):
        self.novo_animal = novo_animal
        self.som_animal = som_animal

    def emitirSom(self):
        return self.som_animal

    def __str__(self) -> str:
        return f'O {self.novo_animal}\n{self.som_animal}!'

class Cachorro(Animal):
    def emitirSom(self):
        print("Au Au!")

class Gato(Animal):
    def emitirSom(self):
        print("Miau!")

class ControleDeAnimais(Animal):
# Utilizando polimorfismo
    def __init__(self):
        self.animais = [Cachorro(), Gato()]
        super().__init__(self.novo_animal,self.som_animal)

    def cadastrar_animais(self):
        self.animais.append(self.novo_animal,self.som_animal)

    def emitir_som(self):

        for animal in self.animaisanimais:
            animal.emitirSom()
            print(animal.emitirSom())

    def __str__(self):
        return f'{self.animais}'
    

A1 = Animal("pinto","piu")

print(A1.ControleDeAnimais())
