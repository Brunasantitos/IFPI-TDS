class Pessoa():
    registrar_pessoa = []
        print('1-Cadastrar uma pessoa')
        print('2-Registrar óbito')
        print('3-Estado civil')
        print('4-Atualizar cadastro')
    def __init__(self,nome,idade,peso,altura,sexo,cpf):
        self.__nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.__sexo = sexo
        self.cpf = cpf
        self.__estado = True
        self.__estado_civil = False
        self.conjugue = None

    def envelhecer(self):
        pass
            
    def engordar(self):
        pass
    
    def emagrecer(self):
        pass
    
    def crescer(self):
        pass
    
    @property
    def estado(self):
        return self.__estado
    
    @estado.setter
    def estado(self,estado_obito):
        self.__estado = False
    
    @property
    def estado_civil(self):
        return self.__estado_civil
        pass
    
    @estado_civil.setter
    def estado_civil(self,estado_civil):
        pass

def main():
    pass
                    
            
            
            
        

if __name__=='__main__':
    main()
