from views.viewLogin import  ViewLogin

class ControllerLogin:

    def __init__(self,telaLogin:ViewLogin,page):
        self.login=telaLogin.login
        self.password=telaLogin.password
        self.btnEnter=telaLogin.btnEnter
        self.page=page
        self.btnEnter.on_click=self.handleEnter

    def handleEnter(self,e):
        if self.password.value=="1234" and self.login.value=="carlos":
            print("estou dentro do evento")
            self.page.go("/home")