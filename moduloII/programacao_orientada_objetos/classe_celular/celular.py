import random

class Bateria:
    def __init__(self,codigo,capacidade,percentual_carga):
        self.__codigo = codigo
        self.__capacidade = capacidade
        self.__percentual_carga = percentual_carga

    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def capacidade(self):
        return self.__capacidade
    
    @capacidade.setter
    def capacidade(self):
        valor = random.randint(0,100)
        return valor
    
    @property
    def percentual_carga(self):
        return self.__percentual_carga
    
    def carregar(self):
        pass


    def descarregar(self):
        pass
    
    


class Celular:
    def __init__(self,mei,bateria,wifi,ligar):
        self.__mei = mei
        self.__bateria = bateria
        self.__wifi = wifi
        self.ligar = False
        

    @property
    def mei(self):
        return self.__mei
    
    @property
    def bateria(self):
        return self.__bateria
    
    @property
    def wifi(self):
        return self.__wifi
    
    def ligar(self):
        if self.ligar == True:
            print("ligando...")

        elif self.ligar == False:
            print("desligando...")

    

    
def main():
    print('1-ligar')
    print('2-desligar')
    entrada = int(input("Digite uma opção: "))

    if entrada == 1:
        entrada.ligar = True
    
    elif entrada == 2:
        entrada.ligar = False
    

if __name__=='__main__':
    main()