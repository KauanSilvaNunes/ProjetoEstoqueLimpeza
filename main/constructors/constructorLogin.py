from views.viewLogin import ViewLogin
from controllers.controllerLogin import ControllerLogin
from models.services.autenticacao import Autenticacao
from models.DAO.usuarioDAO import UserDAO

def constructorLogin(page):
    telaLogin=ViewLogin()
    bdUser=UserDAO()
    autentication=Autenticacao(bdUser)


    controllerLogin=ControllerLogin(telaLogin=telaLogin,page=page,autentication=autentication)



    return telaLogin
