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
    
    def matricula_aluno(self,aluno,curso):
        if self.buscar_curso(curso.nome)!=None:
            if aluno.nota_enem >= curso.nota_corte:
                pass
         
    def __str__(self):
        cab = f'{self.__sigla}- Relação de alunos\n'
        dados=''
        for i in self.__alunos:
            dados += f'CPF:{i.cpf}  Nome:{i.nome}\n'
        return cab+dados

class Curso:
    def __init__(self,id,nome,vagas,nota_corte):
        self.__id = id
        self.__nome = nome
        self.__vagas = vagas
        self.__nota_corte = nota_corte
        self.alunos = []

    @property
    def id(self):
        return self.__id
    
    def incluir_aluno(self):
        pass

    def buscar_aluno(self):
        pass

    def solicitar_entrada(self):
        pass

    def __str__(self):
        cab = f'curso:{self.__nome} - Relação de alunos'
        for i in self.__alunos:
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

    def efetivar_matricula(self,curso,universidade):
        #universidade.matricula_aluno(self,curso)
        if self.solicita_entrada(curso,universidade):
            pass

    def solita_transferencia(self,univ_ori,curso_ori,univ_dest):
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