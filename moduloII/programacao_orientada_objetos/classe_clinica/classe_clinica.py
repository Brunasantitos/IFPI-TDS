from datetime import *

class ConsultaMedica:
  dia_semana = {0:'segunda-feira',1:'terça-feira',2:'quarta-feira',3:'quinta-feira',4:'sexta-feira'}

  def __init__(self,data_consulta,medico,paciente):
    finalDeSemana = [5,6]
    self.data_consulta = data_consulta
    self.data_retorno = None
    self.medico = medico
    self.paciente = paciente
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

def main():
    consultas = []
    cancelado = []
    while True:
        print('\n1-Nova Consulta')
        print('2-Pagar Consulta')
        print('3-Cancelar Consulta')

        MenuAtendimento = input("opção:")
        if MenuAtendimento=='1':
            consultas.append(ConsultaMedica(input("entre com a data da consulta:(dd/mm/aaaa): "),input("entre com o nome do médico: "),input("entre com o nome do paciente: ")))
      
        elif MenuAtendimento=='2': 
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
              
        elif MenuAtendimento=='3':
          cont = 0
          for i,j in enumerate(consultas):
              #seq+=1
            if j.cancelado == False:
              cont+=1
              print(i,j)
              
          if cont > 0:
            op1 = int(input("\nescolha um indice correspondente a consulta: "))
            consultas[op1].cancelado = True
            print("\nConsulta cancelada")
            
          else:
            print("\nNão há consultas para serem canceladas")
            break
     

if __name__=='__main__':
    main()

