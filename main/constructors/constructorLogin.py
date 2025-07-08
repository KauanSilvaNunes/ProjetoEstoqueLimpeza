from views.viewLogin import ViewLogin
from controllers.controllerLogin import ControllerLogin

def constructorLogin(page):
    telaLogin=ViewLogin()
    controllerLogin=ControllerLogin(telaLogin=telaLogin,page=page)


    return telaLogin
