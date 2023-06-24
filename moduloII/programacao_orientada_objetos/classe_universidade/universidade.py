class Sisu(object):
    __universidades = []
  
    def inclui_universidade(universidade):
        if type(universidade) == Universidade:
            Sisu.__universidades.append(universidade)
      
    def busca_universidade(nome):
        for i in Sisu.__universidades:
            if i.nome == nome:
                return i
        return None
  

class Universidade:
    def __init__(self,sigla,nome,tipo):
        self.__sigla_universidade = sigla
        self.__nome_universidade = nome
        self.__tipo_universidade = tipo
        self.__cursos = []

    @property
    def sigla_universidade(self):
        return self.__sigla_universidade
    
    @property
    def nome_universidade(self):
        return self.__nome_universidade
    
    @property
    def tipo_universidade(self):
        return self.__tipo_universidade
    
    @property
    def cursos(self):
        return self.__cursos
    
    def cadastrar_curso(self,curso):
        if type(curso) == Curso:
            self.__cursos.append(curso)
            print(f'curso cadastrado com sucesso!')
        else:
            print("Erro!")
    
    def buscar_curso(self,curso):
        for i in self.alunos:
            if i.curso == curso:
                return i
        return None
    
    '''
    def matricula_aluno(self,aluno,curso):
        if self.buscar_curso(curso.nome)!= None:
            if aluno.ponto_enem >= curso.nota_corte_curso:
                pass
    '''     
    def __str__(self):
    
        cab = f'{self.__sigla_universidade}\n'
        dados=''
        ''' 
        for i in self.__alunos:
            dados += f'CPF:{i.cpf}  Nome:{i.nome}\n'
        ''' 
        return cab+dados
        
class Curso:
    def __init__(self,id,nome,duracao,vagas,nota_corte):
        self.__id_curso = id
        self.__nome_curso = nome
        self.__duracao_curso = duracao
        self.__vagas_curso = vagas
        self.__nota_corte_curso = nota_corte
        self.alunos = []

    @property
    def id_curso(self):
        return self.__id_curso
    
    @property
    def nome_curso(self):
        return self.__nome_curso
    
    @property
    def duracao_curso(self):
        return self.__duracao_curso
    
    @property
    def vagas_curso(self):
        return self.__vagas_curso
    
    @property
    def nota_corte_curso(self):
        return self.__nota_corte_curso
    
    def cadastrar_aluno(self):
        pass

    '''
    def buscar_aluno(self):
        pass

    def solicitar_entrada(self):
        pass
    '''
    def __str__(self):
        cab = f'curso: {self.__nome_curso}'
        return cab

        #for i in self.alunos:
            

class Aluno:
    def __init__(self,cpf,nome,dt_nasc,ponto_enem):
        self.__cpf = cpf
        self.nome_aluno = nome
        self.dt_nasc_aluno = dt_nasc
        self.ponto_enem = ponto_enem
        self.matricula_publica = False
        self.matricula_privada = False
    
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

    def solita_transferencia(self,universidade_origem,curso_origem,univ_destino):
        pass

    def __str__(self):
        if self.ponto_enem > 0:
            return f'{self.nome_aluno} matriculado'

def main():
    #CADASTRANDO ALUNOS
    maria = Aluno ("11111111111111","Maria","01/02/1990",800)
    jose = Aluno ("22222222222","José","15/12/1998",400)
    print(maria)
    print(jose)
    
    #CADASTRANDO UNIVERSIDADES
    uespi = Universidade('UESPI','Universidade Estadual do Piauí','publico')
    ufpi = Universidade('UFPI','Universidade Federal do Piauí','publico')
    novafapi = Universidade('NovaFapi','NovaFapi', 'particular')
    print(uespi)
    print(ufpi)
    print(novafapi)

    #CADASTRANDO CURSOS
    enfermagem = Curso(111,'enfermanem',3,40,700)
    pedagogia = Curso(222,'pedagogia',6,45,600)
    medicina = Curso(333,'medicina',10,50,850)
    print(enfermagem)
    print(pedagogia)
    print(medicina)

    Sisu.inclui_universidade(uespi)
    Sisu.inclui_universidade(ufpi)
    Sisu.inclui_universidade(novafapi)

    ''' 
    uespi.matricula_aluno(maria,'pedagogia')
    ufpi.matricula_aluno(maria,'medicina')
    ufpi.matricula_aluno(jose,'enfermagem')
    novafapi.matricula_aluno(Aluno('33333333333','Ana','14/06/2000',850))
    
    print(maria.matricula_publica)
    print(jose.matricula_publica)
    ''' 

if __name__=='__main__':
    main()