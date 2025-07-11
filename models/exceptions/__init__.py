
class ErroUserRegisterNotFound(ValueError):
    def __init__(self, mensage="Registro não Encontrado"):
        super().__init__(mensage)