from models.valueObject.password import Password
class Usuario:

    def __init__(self,id,registro_funcionario,nome, password):
        self.__id=id
        self.__registro_funcionario=registro_funcionario
        self.nome=nome
        self.password=Password(password)



    

