class Paciente:
  def __init__(self,id_pac,nome_pac,dt_nasc,contato):
    self.__id_paciente = id_pac
    self.nome = nome_pac 
    self.__dt_nasc = dt_nasc
    self.__contato = contato

  @property
  def id_paciente(self):
    return self.__id_paciente
  
  @property
  def dt_nasc(self):
    return self.__dt_nasc

  @property
  def contato(self):
    return self.__contato
  
  #realizar modificação do número 
  #@contato.setter

  def __str__(self):
    return f'Nome do Paciente: {self.nome} \t Data.Nasc.:{self.__dt_nasc}'

class Medico:
  def __init__(self,id_medico,crm,nome_medico,esp):
    self.__id = id_medico
    self.__crm = crm
    self.nome = nome_medico
    self.especialidade = esp
  
  @property
  def id(self):
    return self.__id
  
  def __str__(self):
    return f'Nome do médico:{self.nome} \n CRM:{self.__crm} \n Especialidade:{self.especialidade}'


class ConsultaMedica:
  id = 0 # atributo de classe 
  def __init__(self,medico,paciente,data,pago=False):
    ConsultaMedica.id+=1
    self.__id = ConsultaMedica.id
    if type(medico)==Medico:
      self.__medico = medico
    else:
      raise "Error!"
    if type(paciente)==Paciente:
      self.__paciente = paciente
    else:
      raise "Error!"
    self.__data = data # fazer a validação de data
    self.__pago = pago
    self.__data_retorno = None


  @property
  def pago(self):
    return self.__pago

  @property
  def data(self):
    return self.__data
  
  @property
  def data_retorno(self):
    return self.__data_retorno
    

  def __str__(self):
    v1 = f'Consulta {self.__id} marcada para a data: {self.__data}\nPaciente:{self.__paciente.nome}\nMédico:{self.__medico.nome}'
    return v1

consultas = [ConsultaMedica(Medico(32165498754,1234,"João","ortopedista"),Paciente(3216548954,"Maria",'12/12/2000',8699885321),'02/05/2023')]
pacientes = [Paciente(3216548954,"Maria",'12/12/2000',8699885321)]
medicos= [Medico(32165498754,1234,"João","ortopedista")]

maria = Paciente(3216548954,"Maria",'12/12/2000',8699885321)
joão = Medico(32165498754,1234,"João","ortopedista")

c1 = ConsultaMedica(joão,maria,'02/05/2023')
c2 = ConsultaMedica(joão,maria,'12/05/2023')
'''
print(c1)
print(c2)
print(ConsultaMedica.id)
#print(f'{c1.paciente.nome_paciente} vai se consultar com o Dr. {c1.medico.nome_medico}')
'''

def menu():
  print("1 - Cadastrar Paciente")
  print("2 - Cadastrar Médico")
  print("3 - Marcar consulta")
  print("4 - Pagar consulta")
  print("5 - Cancelar consulta")
  print("6 - Marcar retorno")
  print("7 - Sair")

def consultaObjeto(nome,lista):
  for i in lista:
    if nome==i.nome:
      return i  # objeto
  return None

def buscaConsulta(nome_pac,data,lista):
    for i in lista:
        if nome_pac == i.consultas and data==i.data:
          return i
    return None

while True:
  menu()
  op = int(input("Entre com a opção:"))
  if op==1:
      nome = input("Nome do paciente:")
      pac = consultaObjeto(nome,pacientes)
      if pac==None:
        print("Paciente não cadastrado!")
        pacientes.append(Paciente(int(input("Informe o id paciente: ")),input("Nome do paciente: "),input("Data nascimento DD/MM/AAAA: "),int(input("Contato: "))))
        print("Cadastro realizado!")
      else:
        print(pac)
  elif op==2:
      nome = input("Nome do Medico:")
      pac = consultaObjeto(nome,pacientes)
      if pac==None:
        print("Médico não cadastrado!")
        medicos.append(Medico(int(input("Informe o id_medico: ")),int(input("Informe o crm: ")),input("Informe o nome do médico: "),input("Especialidade: ")))
        print("Cadastro realizado!")
      else:
        print(pac)
      
  elif op==3:
     # dar os inputs para os atributos
     # pegar o nome do paciente
     # buscar na lista de pacientes o objeto correspondente
    nome = input("Nome do paciente:")
    pac = consultaObjeto(nome,pacientes)
    if pac==None:
      nome_medico = input("Informe o nome do médico: ")
      med = consultaObjeto(nome_medico,medicos)
      if med != None:
        nome_paciente = input("Informe o nome do paciente: ")
        if nome_paciente != None:
          pac = (consultaObjeto(nome_paciente,pacientes))
          if pac != None:
            data = input("Informe a data da consulta: ")

            consultas.append(ConsultaMedica(med,pac,data))
            print("Consulta agendada com sucesso!")
        else:
            print("Paciente não encontrado!")
      else:
        print("Médico não encontrado!")
        
        #consultas.append(ConsultaMedica (Paciente(int(input("Informe o id paciente: ")),nome,input("Data nascimento DD/MM/AAAA: "),
                                                     #int(input("Contato: "))),Medico(int(input("Informe o id_medico: ")),int(input("Informe o crm: ")),
                                                        #input("Informe o nome do médico: "),input("Especialidade: ")),input("Data da consulta DD/MM/AAAA: ")))
    else:
      print("Consulta não agendada!")
     # input do médico
     # input da data   
     # criar a instancia de consulta e adicionar na lista
      
     #consultas.append(ConsultaMedica(med,pac,data))     
     
     # pegar o nome do medico
     #buscar na lista de médicos o objeto correspondente
     #criar o objeto ConsultaMedica
     # inserir na lista de consultas médicas
  elif op==4:
    nome_pac = input("Entre com o nome do paciente:")
    data = input("Entre com a data:")
    c = buscaConsulta(nome_pac,data,consultas)
    if c!=None:
      if c.pago == False:
        c.pagar_consulta()
      else:
        print("A consulta já está paga!")
    else:
      print("Consulta não encontrada!")
      nome_pac = input("Entre com o nome do paciente:")
      data = input("Entre com a data:")
      c = buscaConsulta(nome_pac,data,consultas)
      if c!=None:
        if c.pago == False:
          c.pagar_consulta()
        else:
          print("A consulta já está paga!")
      else:
        print("Consulta não encontrada!")
     # pegar na lista de consultas (por data, por nome do paciente ou por nome do médico)
     # retornar o objeto correspondente ao critério da pesquisa
  elif op==5:
    nome_pac = input("Entre com o nome do paciente:")
    data = input("Entre com a data:")
    c = buscaConsulta(nome_pac,data,consultas)
    if c!=None:
      if c.pago == False:
          c.pagar_consulta()
      else:
          print("A consulta já está paga!")
    else:
      print("Consulta não encontrada!")
      nome_pac = input("Entre com o nome do paciente:")
      data = input("Entre com a data:")
      c = buscaConsulta(nome_pac,data,consultas)
      if c!=None:
        if c.pago == False:
          c.pagar_consulta()
        else:
          print("A consulta já está paga!")
      else:
        print("Consulta não encontrada!")
  elif op==6:
    pass
  elif op==7:
    break
