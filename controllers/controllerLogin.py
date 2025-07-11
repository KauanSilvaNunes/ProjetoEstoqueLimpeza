from views.viewLogin import  ViewLogin


class ControllerLogin:

    def __init__(self,telaLogin:ViewLogin,page,autentication):
        self.login=telaLogin.login
        self.password=telaLogin.password
        self.btnEnter=telaLogin.btnEnter
        self.btnCadastro=telaLogin.btnCadastro
        self.page=page
        self.btnEnter.on_click=self.handleEnter
<<<<<<< HEAD
        self.autentication=autentication

    def handleEnter(self,e):
        try:
            user=self.autentication(self.login,self.password)
            print(user)
            self.page.go("/home")
        except Exception as e:
            print("Erro", e)
=======
        self.btnCadastro.on_click=self.handleRegister

    def handleEnter(self,e):
        # if self.password.value=="1234" and self.login.value=="carlos":
        #     print("estou dentro do evento")
            self.page.go("/home")

    def handleRegister(self,e):
         self.page.go("/cadastro")
>>>>>>> cc8823d84c140be19a767078acf5f3f164b365ea
