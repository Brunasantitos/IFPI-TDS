class Seguro:
    def __init__(self, numero_apolice, proprietario, valor_seguro, valor_premio):
        self._numero_apolice = numero_apolice
        self._proprietario = proprietario
        self._valor_seguro = valor_seguro
        self._valor_premio = valor_premio

    def calcular_valor(self):
        pass

    def calcular_premio(self):
        pass

    def __str__(self):
        return f'Valor seguro: R${self._valor_seguro:.2f}\nValor prêmio: R${self._valor_premio:.2f}\nNumero apolice: {self._numero_apolice}'

class SeguroVida(Seguro):
    def __init__(self, numero_apolice, proprietario, valor_seguro, valor_premio, idade_segurado, nome_beneficiario):

        super().__init__(numero_apolice, proprietario, valor_seguro, valor_premio)
        self._idade_segurado = idade_segurado
        self._nome_beneficiario = nome_beneficiario

    def calcular_valor_vida(self):
        if self._idade_segurado <= 30:
            self.valor_seguro = 800.00
            
        elif 31 <= self._idade_segurado <= 50:
            self.valor_seguro = 1300.00
            
        else:
            self.valor_seguro = 1600.00
            
    def calcular_premio_vida(self):
        if self._idade_segurado <= 30:
            self.valor_premio = 50000
            
        elif 31 <= self._idade_segurado <= 50:
            self.valor_premio = 30000
            
        else:
            self.valor_premio = 20000 

    def __str__(self):
        return super().__str__()+f'\nValor seguro: R${self._valor_seguro:.2f}\nValor prêmio: R${self._valor_premio:.2f}\nBeneficiario {self._nome_beneficiario}'


class SeguroAutomovel(Seguro):
    def __init__(self, numero_apolice, proprietario, valor_seguro, valor_premio, numero_licenca, modelo, ano, valor_automovel):

        super().__init__(numero_apolice, proprietario, valor_seguro, valor_premio)
        self._numero_licenca = numero_licenca
        self._modelo = modelo
        self._ano = ano
        self._valor_automovel = valor_automovel

    def calcular_valor_automovel(self):
        self.valor_seguro = self._valor_automovel * 0.03

    def calcular_premio_automovel(self):
        self.valor_premio = self._valor_automovel * 0.8

    def franquia(self):
        self.valor_seguro * 0.4            
    
    def __str__(self):
        return f'Valor seguro: R${self._valor_seguro:.2f}\nValor prêmio: R${self._valor_premio:.2f}'
    
class Cliente:
    def __init__(self,cpf_cliente,nome_cliente,idade_cliente,):
        self.__cpf_cliente = cpf_cliente
        self.__nome_cliente = nome_cliente
        self.__idade_cliente = idade_cliente

    @property
    def cpf_cliente(self):
        return self.__cpf_cliente
        
    @property
    def nome_cliente(self):
        return self.__nome_cliente
    
    @property
    def idade_cliente(self):
        return self.__idade_cliente
    
class ControleDeSeguros:
    def __init__(self):
        self.lista_seguros = []

    def adicionar_seguro(self, seguro):
        self.lista_seguros.append(seguro)

    def remover_seguro(self, seguro):
        self.lista_seguros.remove(seguro)
       
    def __str__(self):
        retorno = ""
        for seguro in self.lista_seguros:
            retorno += f"Número Apólice: {seguro._numero_apolice}\n"
            retorno += f"Proprietário: {seguro._proprietario}\n"
            retorno += f"Valor do Seguro: R${seguro._valor_seguro:.2f}\n"
            retorno += f"Valor do Prêmio: R${seguro._valor_premio:.2f}\n"
            retorno += 100*'_'
            retorno += "\n"
        return retorno

def main():

    controle_seguros = ControleDeSeguros()

    seguro1 = SeguroAutomovel("A425","bruna",48,25,1111,"onix",2015,75.000)
    seguro1.calcular_valor_automovel()
    seguro1.calcular_premio_automovel()
    
    controle_seguros.adicionar_seguro(seguro1)
    print(controle_seguros)

    seguro2 = SeguroVida("V11","Carla",50.00,25.00,80,"Ana")
    seguro2.calcular_valor_vida()
    seguro2.calcular_premio_vida()
    controle_seguros.adicionar_seguro(seguro2)
    print(controle_seguros)

if __name__=='__main__':
    main()
