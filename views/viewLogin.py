from flet import *
from utils.cores import Cores

class ViewLogin(View):
    def __init__(self):
        super().__init__()
        self.route="/"
        self.bgcolor=Cores().corbranca
        iconesenha=Icon(name=Icons.PASSWORD,color=Cores().corprimaria)
        iconelogin=Icon(name=Icons.LOGIN,color=Cores().corprimaria)
        iconeimagem=Image(src="Senac_logo.svg.png",width=500,height=400)
        linhaimagem=ResponsiveRow(controls=[iconeimagem],alignment=MainAxisAlignment.CENTER)
        self.login=TextField(prefix_icon=iconelogin,border_radius=10,label="Nome",color="black",col={"xs":2,"sm":2,"md":2,"lg":2,"xl":2},label_style=TextStyle(color="black"),width=1000)
        self.password=TextField(prefix_icon=iconesenha,border_radius=10,label="Senha",color="black",password=True,can_reveal_password=True,col={"xs":2,"sm":2,"md":2,"lg":2,"xl":2},label_style=TextStyle(color="black"))
        self.btnEnter=ElevatedButton(text="Entrar",width=150,height=50,col={"xs":12,"sm":8,"md":4,"lg":4,"xl":4},style=ButtonStyle(bgcolor={ControlState.HOVERED:Cores().laranjaescuro,
        ControlState.FOCUSED:Colors.PINK,
        ControlState.DEFAULT:Cores().corsecundaria},color=Cores().corbranca,))
        linha2=ResponsiveRow(controls=[self.login],alignment=MainAxisAlignment.CENTER)
        linha4=ResponsiveRow(controls=[self.password],alignment=MainAxisAlignment.CENTER)
        coluna=Column(controls=[linha2,linha4],spacing=30)
        container=Container(content=coluna,margin=Margin(top=100,right=0,left=0,bottom=30))
        linha5=Row(controls=[self.btnEnter],alignment=MainAxisAlignment.CENTER)

        colum1=Column(controls=[linhaimagem,container,linha5],spacing=20)
        self.controls=[colum1]