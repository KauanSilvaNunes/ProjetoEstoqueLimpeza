from views.viewLogin import  ViewLogin


class ControllerLogin:

    def __init__(self,telaLogin:ViewLogin,page,autentication):
        self.login=telaLogin.login
        self.password=telaLogin.password
        self.btnEnter=telaLogin.btnEnter
        self.page=page
        self.btnEnter.on_click=self.handleEnter
        self.autentication=autentication

    def handleEnter(self,e):
        try:
            user=self.autentication(self.login,self.password)
            print(user)
            self.page.go("/home")
        except Exception as e:
            print("Erro", e)