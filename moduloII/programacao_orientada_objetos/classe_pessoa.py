class Pessoa():
    def __init__(self,nome,idade,peso,altura,sexo,estado,estado_civil,conjugue):
        self.__nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.__sexo = None
        self.__estado = True
        self.__estado_civil = False
        self.conjugue = None

    def envelhecer(self):

        if self.idade < 21:
            self.altura += 0.5
            print("você cresceu")
        elif self.idade >= 21:
            self.idade += 1
            print("você envelheceu")



def main():
    pass

if __name__=='__main__':
    main()
