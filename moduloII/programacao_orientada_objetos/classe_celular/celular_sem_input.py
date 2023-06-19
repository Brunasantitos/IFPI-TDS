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
        
    
    def __str__(self):
        return f'{self.__percentual_carga}'
    
         
class Celular:
    def __init__(self, bateria):
        self.__mei = 14536789
        self.__bateria = bateria
        self.__wifi = 'desligar'
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
            print("celular sem bateria")
        
        elif self.__bateria.percentual_carga > 0:
            self.__ligar = True
          
        elif self.__bateria.percentual_carga == 0:
            print ("SEM BATERIA")

        elif self.__ligar == True:
            self.__ligar = False
            

        

    def colocar_bateria(self, bateria):

        if self.__bateria == None:
            self.__bateria = bateria
            
        else:
            self.retirar_bateria()
            self.__bateria = bateria
            

    def retirar_bateria(self):
        self.__bateria = None
        

    def ligar_desligar_wifi(self,valor):
        if valor == 'ligar':
            self.__wifi = 'ligado'
            print('wifi ligado')

        elif valor == 'desligar':
            print('wifi desligado')

    def assistir_video_tempo(self, tempo):
        pass

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
        

    def __str__(self):

        if self.__ligar == False:
            return f'\ncelular desligado'
        
        elif self.__ligar == True:

            if self.__bateria == None:
                return "\ncelular sem bateria"
            
        return f'\ncelular ligado, bateria em {self.__bateria}%'
        
        


    

def main():
    b1 = Bateria(50)
    celular1 =  Celular(b1)

    celular1.ligarDesligar()
    
    celular1.ligar_desligar_wifi('ligar')
    print(celular1)
                
    

main()