from views.viewMenu import ViewMenu
from controllers.controllerMenu import ControllerMenu

def constructorMenu(page):
    telaMenu=ViewMenu()
    controllerMenu=ControllerMenu(telaMenu=telaMenu,page=page)

    return telaMenu