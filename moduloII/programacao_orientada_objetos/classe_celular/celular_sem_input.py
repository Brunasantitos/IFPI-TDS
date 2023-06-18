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
            self.__percentual_carga = 100
            if valor < 100:
                print ("carregando...")
                
            else:
                return self.__percentual_carga
        else:
            raise "error" 
            

    def descarregar(self,valor):

        if valor >= 0:
            if valor == 0:
                self.__percentual_carga = valor
                print(f'celular descarregado')
            
                

            elif valor < 100:
                valor -= 1
                self.__percentual_carga = valor
                return self.__percentual_carga
                
        else:
            raise "error"
        
    def __str__(self):
        return f'bateria em {self.__percentual_carga}%'

class Celular:
    def __init__(self, bateria):
        self.__mei = 14536789
        self.__bateria = bateria
        self.__wifi = False
        self.__ligar = False       
    
    @property
    def mei(self):
        return self.__mei

    @property
    def wifi(self):
        return self.__wifi
    
    @property
    def bateria(self):
        return self.__bateria
    
    @property
    def ligar(self):
        return self.__ligar
    
    
    def ligarDesligar(self):
        
        if self.__bateria > 0:

            self.__ligar = True
            print (f'Celular ligado')

        elif self.__bateria == 0:
            print ("SEM BATERIA")


        elif self.__ligar == True:
            self.__ligar = False
            print('Celular desligado')

    def __str__(self) -> str:
        return f'{self.__ligar} {self.__bateria}'
    

def main():
    b1 = Bateria(100)
    celular1 =  Celular(b1)

    celular1.ligarDesligar = b1
    b1.carregar(100)
    print(b1)
    print(celular1)
    

if __name__=='__main__':
    main()
