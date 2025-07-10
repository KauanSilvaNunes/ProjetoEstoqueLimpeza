from flet import *
from utils.cores import Cores

class ViewLogin(View):
    def __init__(self):
        super().__init__()
        self.route="/"
        self.bgcolor=Cores().corbranca
        iconesenha=Icon(name=Icons.PASSWORD,color=Cores().corprimaria)
        iconelogin=Icon(name=Icons.LOGIN,color=Cores().corprimaria)
        iconeimagem=Image(src="Senac_logo.svg.png",width=500,height=400,col={"xs":9,"sm":6,"md":6,"lg":3.4,"xl":3.4})
        linhaimagem=ResponsiveRow(controls=[iconeimagem],alignment=MainAxisAlignment.CENTER)
        self.login=TextField(prefix_icon=iconelogin,border_radius=10,label="Registro",color="black",col={"xs":8,"sm":3,"md":4,"lg":3.4,"xl":3.4},label_style=TextStyle(color="black"),width=1000)
        self.password=TextField(prefix_icon=iconesenha,border_radius=10,label="Senha",color="black",password=True,can_reveal_password=True,col={"xs":8,"sm":3,"md":4,"lg":3.4,"xl":3.4},label_style=TextStyle(color="black"))
        self.btnEnter=ElevatedButton(text="Entrar",width=150,height=50,col={"xs":2.5,"sm":2.5,"md":3.2,"lg":1.5,"xl":1.5},style=ButtonStyle(bgcolor={ControlState.HOVERED:Cores().laranjaescuro,
        ControlState.FOCUSED:Colors.PINK,
        ControlState.DEFAULT:Cores().corsecundaria},color=Cores().corbranca,))
        self.btnCadastro=TextButton(
            text="Cadastrar",
            style=ButtonStyle(color={ControlState.DEFAULT: Cores().corsecundaria,
                                     ControlState.HOVERED: Cores().corprimaria,
                                     ControlState.FOCUSED: Cores().corprimaria},
                              bgcolor={ControlState.DEFAULT: Colors.TRANSPARENT,
                                       ControlState.HOVERED: Colors.TRANSPARENT,
                                       ControlState.FOCUSED: Colors.TRANSPARENT},
                              overlay_color={ControlState.DEFAULT: Colors.TRANSPARENT,
                                             ControlState.HOVERED: Colors.TRANSPARENT,
                                             ControlState.FOCUSED: Colors.TRANSPARENT},text_style={
            ControlState.DEFAULT: TextStyle(size=18)
        }))

        linhalogin=ResponsiveRow(controls=[self.login],alignment=MainAxisAlignment.CENTER)
        linhapassword=ResponsiveRow(controls=[self.password],alignment=MainAxisAlignment.CENTER)
        coluna=Column(controls=[linhalogin,linhapassword],spacing=30)
        container=Container(content=coluna,margin=Margin(top=100,right=0,left=0,bottom=30))
        linhabotoes=ResponsiveRow(controls=[self.btnEnter,self.btnCadastro],alignment=MainAxisAlignment.CENTER)

        colum1=Column(controls=[linhaimagem,container,linhabotoes],spacing=20)
        self.controls=[colum1]