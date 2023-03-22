import datetime
class Agendamento():
    
    def __init__(self, dia, nomePaciente, nomeMedico):
        self.dataEhorario = datetime
        self.dia = float(input("data da consulta: "))
        self.nomePaciente = int(input("nome do paciente: "))
        self.nomeMedico = int(input("informe o nome do médico: "))
        self.valorConsulta = 300
        self.pagamentoEfetuado = False
        
        def NovaConsulta(self):
            if self.dia > self.dataEhoario.datatime.now():
                print("Agendamento realizado!")
            else:
                print("Data inválida!")
                
        
        def PagarConsulta(self):
            if self.pagamentoEfetuado == True:
                print("Pagamento efetuado!")
        
        def CancelarConsulta(self, cancelarAtendimento):
            if cancelarAtendimento == True:
                del Paciente1
                print("Agendamento cancelado!")
        
        def AgendarRetorno(self):
            if self.pagamentoEfetuado == True:
                if self.dataEhorario.datatime.now():
                    print("Novo agendamento!")
        
        def RelatorioConsultasPorMedico(self):
            pass
        
        def RelatorioFaturamentoMensal(self):
            pass
        
def main():
    Paciente1 = [Agendamento()]
    Paciente2 = [Agendamento()]

if __name__=='__main__':
    main()