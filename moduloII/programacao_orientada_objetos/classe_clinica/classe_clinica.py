from datetime import *
class ConsultaMedica:
  dia_semana = {0:'segunda-feira',1:'terça-feira',2:'quarta-feira',3:'quinta-feira',4:'sexta-feira'}
  def __init__(self,data_consulta,medico,paciente):
    fds = [5,6]
    self.data_consulta = data_consulta
    self.data_retorno = None
    self.medico = medico
    self.paciente = paciente
    self.pago = False
    self.cancelado = False

    d = datetime.strptime(data_consulta,"%d/%m/%Y").date()
    if d <= date.today() or d.weekday() in fds:
                raise ValueError("data de consulta menor que data atual ou caiu em final de semana")
                print("Valor:", data)
    else:
      self.data_consulta = datetime.strptime(data_consulta,"%d/%m/%Y").date()
      self.medico = medico
  def __str__(self):
    return f'data da consulta: {self.data_consulta} {ConsultaMedica.dia_semana[self.data_consulta.weekday()]}'

  def pagar_consulta(self):
      self.pago = True

def main():
    consultas = []
    while True:
        print('1-Nova Consulta')
        print('2-Pagar Consulta')

        op = input("opção:")
        if op=='1':
            consultas.append(ConsultaMedica(input("entre com a data da consulta:(dd/mm/aaaa):"),input("entre com o nome do médico:"),input("entre com o nome do paciente")))
      
        elif op=='2': 
            cont=0
        for i,j in enumerate(consultas):
      #seq+=1
            if j.pago==False:
                cont+=1
                print(i,j)
                if cont >0:
                    op1 = int(input("escolha um indice correspondente a consulta:"))
                    consultas[op1].pago = True
                else:
                    print("Não existem consultas a serem pagas")   
            elif op=='3':
                break
     
    
if __name__=='__main__':
    main()
#consultas.append(ConsultaMedica('20/03/2023',"Maria","João"))
#for i in consultas:
#  print(i)