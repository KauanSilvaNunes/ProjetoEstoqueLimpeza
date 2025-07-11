

class ErroUserRegisterNotFound(ValueError):
     def __init__(self, mensage="Password invalido"):
          super().__init__(mensage)
    