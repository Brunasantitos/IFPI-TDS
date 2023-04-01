class Pessoa():
    def __init__(self,nome,idade,peso,altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

        def envelhecer(self):
            self.idade += 1
            return self.idade

        def engordar(self,peso_atual):
            peso_atual += self.peso
            return peso_atual

        def emagrecer(self,peso_atual):
            peso_atual -= self.peso
            return peso_atual
        
        def crescer(self,altura_atual):
            if self.idade <= 21:
                self.altura = altura_atual

            elif self.idade => 21:
                return self.altura

def main():
    pass

if __name__=='__main__':
    main()
