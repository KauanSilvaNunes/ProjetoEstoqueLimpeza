import bcrypt
import re
class Password:

    def __init__(self, password):

        if self.verificarPassword(password):
            self.password=self.criptografarSenha(password)


    def verificarPassword(self,password):
         padrao = r'^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()])[A-Za-z\d!@#$%^&*()]{6}$'
         if re.match(padrao, password):
             return True
         raise ValueError("Senha esta fora do Esperado")
    
    def criptografarSenha(self,password):
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def verify(self, senha):
        return bcrypt.checkpw(senha.encode('utf-8'), self.password)
    

    

if __name__=="__main__":
    senha=Password("A1@bcx")
    print(senha.password)