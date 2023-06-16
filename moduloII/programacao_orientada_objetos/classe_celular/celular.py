import random

class Bateria:
    def __init__(self, codigo, capacidade):
        self.__codigo = codigo
        self.__capacidade = capacidade
        self._percentual_carga = random.randint(0,100)

    @property
    def codigo(self):
        return self.__codigo

    @property
    def capacidade(self):
        return self.__capacidade

    @capacidade.setter
    def capacidade(self, value):
        self.__capacidade = value

    @property
    def percentual_carga(self):
        return self._percentual_carga


    def carregar(self,valor):
        if valor >= 0:
            if valor < 100:
                print(f'bateria em {valor}%')
                self._percentual_carga = 100
                print("carregando...")
            else:
                print("bateria em 100%")
        else:
            raise "error" 
            

    def descarregar(self,valor):
        if valor >= 0:
            if valor == 0:
                self._percentual_carga = valor
                print("descarregado")
                print(f'{self._percentual_carga}%')
            elif valor < 100:
                valor -= 1
                self._percentual_carga = valor
                print(f'bateria em {self._percentual_carga}%')
                print("descarregando...")
        else:
            raise "error"
        
        

class Celular:
    def __init__(self, mei, wifi):
        self.__mei = mei
        self.__bateria = None
        self.__wifi = wifi
        self.__ligar = False        

    @property
    def mei(self):
        return self.__mei

    @property
    def bateria(self):
        return self.__bateria

    @property
    def wifi(self):
        return self.__wifi
    
    @property
    def ligar(self):
        return self.__ligar
    
    
    def ligarDesligar(self):
        
        if self.__bateria > 0:
            self.__ligar = True
            print(f'{self.__bateria}%')
            print("Ligando...")

        elif self.__bateria == 0:
            print("SEM BATERIA")
    

def main():
    bateria = Bateria(1, 3000)
    celular1 = Celular("123456789", True)
    while True:
        print('1-ligar')
        print('2-desligar')
        print('3-carregar')
        print('4-descarregar')
        entrada = int(input("Digite uma opção: "))

        if entrada == 1:
            celular1.ligarDesligar()

        elif entrada == 2:
            celular1.ligarDesligar()

        elif entrada == 3:
            pc_bateria = int(input("Porcentagem da bateria -> "))
            bateria.carregar(pc_bateria)

        elif entrada == 4:
            pc_bateria = int(input("Porcentagem da bateria -> "))
            bateria.descarregar(pc_bateria)



if __name__=='__main__':
    main()
