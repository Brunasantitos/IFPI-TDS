from datetime import *

class ConsultaMedica:
  dia_semana = {0:'segunda-feira',1:'terça-feira',2:'quarta-feira',3:'quinta-feira',4:'sexta-feira'}

  def __init__(self,data_consulta,medico,paciente, cpf_paciente):
    finalDeSemana = [5,6]
    self.data_consulta = data_consulta
    self.data_retorno = None
    self.medico = medico
    self.paciente = paciente
    self.cpf_paciente = cpf_paciente
    self.pago = False
    self.cancelado = False

    dataAtual = datetime.strptime(data_consulta,"%d/%m/%Y").date()

    if dataAtual <= date.today() or dataAtual.weekday() in finalDeSemana:
        raise ValueError("data de consulta menor que data atual ou caiu em final de semana")
        print("Valor:", dataAtual)

    else:
        self.data_consulta = datetime.strptime(data_consulta,"%d/%m/%Y").date()
        self.medico = medico

  def __str__(self):
        return f'data da consulta: {self.data_consulta} {ConsultaMedica.dia_semana[self.data_consulta.weekday()]}'

  def pagar_consulta(self):
    self.pago = True

  def cancelar_consulta(self):
    self.cancelado = False

  def agendar_retorno(self):
    print("Retorno agendado")
 
        

def main():
    consultas = []
    cancelado = []
    retorno = []
    
    while True:
        print('\n1-Nova Consulta')
        print('2-Pagar Consulta')
        print('3-Cancelar Consulta')
        print('4-Agendar retorno')

        MenuAtendimento = input("opção:")
        
        if MenuAtendimento == '1':
            consultas.append(ConsultaMedica(input("entre com a data da consulta:(dd/mm/aaaa): "),
                                            input("entre com o nome do médico: "),input("entre com o nome do paciente: "), input("cpf do paciente: ")))
            print("\nConsulta agendada")
        elif MenuAtendimento == '2': 
            cont=0
            for i,j in enumerate(consultas):
              #seq+=1
              if j.pago == False:
                cont+=1
                print(i,j)
            if cont > 0:
              op1 = int(input("\nescolha um indice correspondente a consulta: "))
              consultas[op1].pago = True
            else:
              print("\nNão existem consultas a serem pagas")
              
        elif MenuAtendimento == '3':
          cont = 0
          for i,j in enumerate(consultas):
                        
            if j.cancelado == False:
              cont+=1
              print(i,j)
              
          if cont > 0:
            op1 = int(input("\nescolha um indice correspondente a consulta: "))
            consultas[op1].cancelado = True
            print("\nConsulta cancelada")
            
          else:
            print("\nNão há consultas para serem canceladas")

        elif MenuAtendimento == '4':
          
            retorno_paciente = input("Informe o cpf do paciente: ")

            for i in consultas:
                if i.cpf_paciente == retorno_paciente and i.cancelado == False:
                   data_maxima_retorno = consultas[retorno_paciente].data_consulta+timedelta(days=30)
                   print(f'Data máxima de retorno {data_maxima_retorno.strftime('%d/%m/%Y')}')
                   data_retorno = input('Informe a data do retorno: ')
                   data_retorno = datetime.strptime(data_retorno,'%d/%m/%Y').date()
                   if data_retorno>data_maxima_retorno:
                     print('Data inválida!')
                   

                else:
                  print("Paciente não encontrado")

            
     

if __name__=='__main__':
    main()
