class Bateria:
    def __init__(self, percentual):
        self.__codigo = "A37"
        self.capacidade = 100
        self.__percentual_carga = percentual
    
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
                return self.__percentual_carga
                
            else:
                return self.__percentual_carga
        else:
            raise "error" 
            

    def descarregar(self,valor):

        if valor >= 0:
            if valor == 0:
                self.__percentual_carga = valor
                return self.__percentual_carga

            elif valor < 100:
                valor -= 1
                self.__percentual_carga = valor
                return self.__percentual_carga
                
        else:
            raise "error"
        
    
class Celular:
    def __init__(self, bateria):
        self.__mei = 14536789
        self.__bateria = None
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

        if self.__bateria == None:
            raise "error"
        
        elif self.__bateria != None:
        
            if '''valor da classe bateria''' > 0:
                self.__ligar = True
                print (f'Celular ligado')

            elif '''valor da classe bateria''' == 0:
                print ("SEM BATERIA")

            elif self.__ligar == True:
                self.__ligar = False
                print('Celular desligado')

    def colocar_bateria(self, bateria):

        if self.__bateria == None:
            self.__bateria = bateria
        else:
            self.retirarBateria()
            self.__bateria = bateria

    def retirar_bateria(self):
        self.__bateria = None

    def ligar_desligar_wifi(self):
        if self.__ligar == True:
            self.__wifi = True
            print('wifi ligado')

    def assistir_video_tempo(self, tempo):
        pass

    def carregar(self,valor):
        pass

    def descarregar(self,valor):
        pass

    def __str__(self):
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
