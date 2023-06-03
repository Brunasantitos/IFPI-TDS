class Sisu(object):
    __universidades = []
  
    def inclui_universidade(universidade):
        if type(universidade)== universidade:
            Sisu.__universidades.append(universidade)
      
  
    def busca_universidade(nome):
        for i in Sisu.__universidades:
            if i.nome == nome:
                return i
        return None
  

class Universidade:
    def __init__(self,sigla,nome,tipo):
        self.__sigla = sigla
        self.__nome = nome
        self.__tipo = tipo
        self.__cursos = []
    @property
    def sigla(self):
        return self.__sigla
    @property
    def nome(self):
        return self.__nome
    @property
    def tipo(self):
        return self.__tipo
    @property
    def cursos(self):
        return self.__cursos
    
    def cadastrar_curso(self,curso):
        if type(curso)==Curso:
            self.__cursos.append(curso)
            print(f'curso cadastrado com sucesso!')
        else:
            print("Erro!")
      
  
    def buscar_curso(self,curso):
        for i in self.__alunos:
            if i.curso == curso:
                return i
        return None
         

    def __str__(self):
        cab = f'{self.__sigla}- Relação de alunos\n'
        dados=''
        for i in self.__alunos:
            dados += f'CPF:{i.cpf}  Nome:{i.nome}\n'
        return cab+dados

class Curso:
    def __init__(self,id,nome,duracao,vagas,nota_corte):
        self.__id = id
        self.nome = nome
        self.duracao = duracao
        self.vagas = vagas
        self.nota_corte = nota_corte

    @property
    def id(self):
        return self.__id
    
    def cadastrar_aluno(self):
        pass




class Aluno:
    def __init__(self,cpf,nome,dt_nasc,ponto_enem):
        self.__cpf = cpf
        self.nome = nome
        self.dt_nasc = dt_nasc
        self.ponto_enem = ponto_enem
        self.matricula_publica = False
    
    
    @property
    def cpf(self):
        return self.__cpf
    

    def solicita_entrada(self,curso,universidade):
        if type(curso) == Curso and type(universidade) == Universidade:
            if self.ponto_enem:
                pass

    
    def __str__(self):
        pass    

def main():
    maria = Aluno ("11111111111111","Maria","01/02/1990")
    josé = Aluno ("22222222222","José","15/12/1998")
    uespi = Universidade('UESPI','Universidade Estadual do Piauí','publico')
    ufpi = Universidade('UFPI','Universidade Federal do Piauí','publico')
    novafapi = Universidade('NovaFapi','NovaFapi', 'particular')

    Sisu.inclui_universidade(uespi)
    Sisu.inclui_universidade(ufpi)
    Sisu.inclui_universidade(novafapi)

    uespi.inclui_aluno(maria)
    ufpi.inclui_aluno(maria)
    ufpi.inclui_aluno(josé)
    novafapi.inclui_aluno(Aluno('33333333333','Ana','14/06/2000'))
    print(uespi)
    print(ufpi)
    print(novafapi)
    print(maria.matricula_publica)
    print(josé.matricula_publica)

if __name__=='__main__':
    main()