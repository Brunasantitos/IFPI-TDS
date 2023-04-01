class Email():
    def __init__(self,nome, nome_usuario, senha):
        self.nome = input("\nInforme seu nome: ")
        self.nome_usuario = input("\nInforme o seu usuário: ")
        self.senha = input('Informe a sua senha de acesso: ')
        self.logado = False
        
    def login_usuario(self, nome_usuario, senha):
        if nome_usuario == self.nome_usuario and senha == self.senha:
            self.logado = True
            print("Logado")
        else:
            print("Usuário/senha inválidos!")
                    
    def logoff_usuario(self):
        if self.logado==False:
            print('Deslogado')
    
        
    def mudar_senha_usuario(self, nova_senha):
        self.senha = nova_senha
        print('nova senha cadastrada com sucesso')
                  
                  
def main():
    P1 = Email(None, None, None)
    P1.login_usuario()
    P1.logoff_usuario()
    P1.mudar_senha_usuario()
    
    
if __name__=='__main__':
    main()
    

           
        

