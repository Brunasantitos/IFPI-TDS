import random

class Bateria:
    def __init__(self, capacidade):
        self.__codigo = "A37"
        self.capacidade = capacidade
        self.__percentual_carga = random.randint(0,100)

    @property
    def codigo(self):
        return self.__codigo

    @property
    def percentual_carga(self):
        return self.__percentual_carga


    def carregar(self,valor):

        if valor >= 0:
            if valor < 100:
                print(f'bateria em {valor}%')
                self.__percentual_carga = 100
                print("carregando...")
            else:
                print("bateria em 100%")
        else:
            raise "error" 
            

    def descarregar(self,valor):

        if valor >= 0:
            if valor == 0:
                self.__percentual_carga = valor
                print("descarregado")
                print(f'{self.__percentual_carga}%')

            elif valor < 100:
                valor -= 1
                self.__percentual_carga = valor
                print(f'bateria em {self.__percentual_carga}%')
                print("descarregando...")
        else:
            raise "error"
        
        

class Celular:
    def __init__(self, bateria1):
        self.__mei = 14536789
        self.bateria = bateria1
        self.__wifi = False
        self.__ligar = False        

    @property
    def mei(self):
        return self.__mei

    @property
    def wifi(self):
        return self.__wifi
    
    @property
    def ligar(self):
        return self.__ligar
    
    
    def ligarDesligar(self):
        
        if self.bateria > 0:

            self.__ligar = True
            print(f'{self.bateria}%')
            print("Ligando...")

        elif self.__bateria == 0:
            print("SEM BATERIA")


    

def main():
    bateria1 = Bateria(50)
    celular1 = Celular(bateria1)

    print(celular1)
    

if __name__=='__main__':
    main()
