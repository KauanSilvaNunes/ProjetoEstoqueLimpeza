
from models.DAO.usuarioDAO import UserDAO
from exceptions.errorUser import ErroUserRegisterNotFound
from exceptions.erroPassword import ErroUserPasswordInvalid
from models.valueObject.password import Password

class Autenticacao:

    def __init__(self, respositorioUsuario: UserDAO):
        self.__respositorioUsuario = respositorioUsuario

    def executar(self, registro: int, senha: str) -> dict:
        senhaCripto = Password(senha)
        user_list = self.__respositorioUsuario.selectionUser(registro)

        if not user_list:
            raise ErroUserRegisterNotFound()

        user = user_list[0]  # pega o primeiro registro retornado (supondo que é uma tupla)

        # Verifica a senha
        if not senhaCripto.verify(user[1]):  # Supondo que user[1] é a senha criptografada
            raise ErroUserPasswordInvalid()

        return {"user": user, "token": "srsrrsrsrsrrsrssrsrr"}  # Token fictício

