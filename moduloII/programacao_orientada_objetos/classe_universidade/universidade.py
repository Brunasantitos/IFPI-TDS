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
        self.__alunos = []

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
    
    @property
    def alunos(self):
        return self.__alunos
    
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
    
    def matricular_aluno(self,aluno,nome_curso):
        curso = self.buscar_curso(nome_curso)

        if curso is not None:
            if aluno.ponto_enem >= curso.nota_corte_curso:
                curso.alunos.append(aluno)
                aluno.matricula_publica = True  # Exemplo de atributo para indicar que o aluno foi matriculado
                print(f'O aluno {aluno.nome_aluno} foi matriculado no curso {nome_curso}.')
            else:
                print(f'O aluno {aluno.nome_aluno} não atende à nota de corte do curso {nome_curso}.')
        else:
            print(f'O curso {nome_curso} não foi encontrado.')

      
    def __str__(self):
    
        cab = f'{self.__sigla_universidade}\n'
        dados=''
        
        for i in self.__alunos:
            dados += f'CPF:{i.cpf}  Nome:{i.nome}\n'
        
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
    
    def cadastrar_aluno(self, aluno):
        if isinstance(aluno, Aluno):
            self.alunos.append(aluno)
            print(f'O aluno {aluno.nome_aluno} foi cadastrado no curso {self.nome_curso}.')
        else:
            print('Erro: O objeto fornecido não é uma instância da classe Aluno.')
    
    def buscar_aluno(self, cpf):
        for aluno in self.alunos:
            if aluno.cpf == cpf:
                return aluno
        return None

    def solicitar_entrada(self, curso, universidade):
        if isinstance(curso, Curso) and isinstance(universidade, Universidade):
            if self.ponto_enem >= curso.nota_corte_curso:
                universidade.matricular_aluno(self, curso)
                print(f'O aluno {self.nome_aluno} foi matriculado no curso {curso.nome_curso} da universidade {universidade.nome_universidade}.')
            else:
                print(f'O aluno {self.nome_aluno} não atende à nota de corte do curso {curso.nome_curso}.')
        else:
            print('Curso ou universidade inválidos.')

    
    def __str__(self):
                
        return f'curso: {self.__nome_curso}, nota de corte: {self.__nota_corte_curso}'

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
            if self.ponto_enem >= curso.nota_corte_curso:
                return True
        else:
            return False               

    def efetivar_matricula(self,curso,universidade):
        if universidade.matricular_aluno(self,curso):
            if self.solicita_entrada(curso,universidade):
                return True
        return False   

    def solita_transferencia(self,universidade_origem,curso_origem,universidade_destino):
        if isinstance(universidade_origem, Universidade) and isinstance(universidade_destino, Universidade) and isinstance(curso_origem, Curso):
            if self in curso_origem.alunos and universidade_origem in Sisu.__universidades:
                curso_origem.alunos.remove(self)
                universidade_destino.matricular_aluno(self, curso_origem.nome_curso)
                print(f"Transferência solicitada para o curso {curso_origem.nome_curso} na universidade {universidade_destino.nome_universidade}.")
            else:
                print("Aluno não matriculado na universidade ou curso de origem.")
        else:
            print("Entradas inválidas para solicitar transferência.")

    def __str__(self):
        if self.ponto_enem > 0:
            return f'{self.nome_aluno} cadastrado(a) com sucesso.'
        else:
            return f'{self.nome_aluno} com nota insuficiente para concorrer a uma vaga.'

def main():
    print(200*'_')  

    #CADASTRANDO UNIVERSIDADES
    uespi = Universidade('UESPI','Universidade Estadual do Piauí','publico')
    ufpi = Universidade('UFPI','Universidade Federal do Piauí','publico')
    novafapi = Universidade('NovaFapi','NovaFapi', 'particular')
    print(uespi)
    print(ufpi)
    print(novafapi)
    print(200*'_')

    #CADASTRANDO CURSOS
    enfermagem = Curso(111,'enfermagem',3,40,700)
    pedagogia = Curso(222,'pedagogia',6,45,600)
    medicina = Curso(333,'medicina',10,50,850)
    print(enfermagem)
    print(pedagogia)
    print(medicina)

    uespi.cadastrar_curso(enfermagem)
    uespi.cadastrar_curso(pedagogia)
    uespi.cadastrar_curso(medicina)

    ufpi.cadastrar_curso(enfermagem)
    ufpi.cadastrar_curso(pedagogia)
    ufpi.cadastrar_curso(medicina)

    novafapi.cadastrar_curso(enfermagem)
    novafapi.cadastrar_curso(pedagogia)
    novafapi.cadastrar_curso(medicina)

    print(200*'_')
    Sisu.inclui_universidade(uespi)
    Sisu.inclui_universidade(ufpi)
    Sisu.inclui_universidade(novafapi)
    
    #CADASTRANDO ALUNOS
    maria = Aluno ("11111111111111","Maria","01/02/1990",800)
    jose = Aluno ("22222222222","José","15/12/1998",0)
    uespi.matricular_aluno(maria,'pedagogia')
    print(maria)
    print(jose)

    
    ufpi.matricular_aluno(maria,'medicina')
    ufpi.matricular_aluno(jose,'enfermagem')
    novafapi.matricular_aluno(Aluno('33333333333','Ana','14/06/2000',850),'pedagogia')
    
    print(maria.matricula_publica)
    print(jose.matricula_publica)
    

if __name__=='__main__':
    main()