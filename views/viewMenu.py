from flet import *
from flet.core.alignment import center
from utils.cores import Cores

class ViewMenu(View):

    def __init__(self):
        super().__init__()
        self.route=("/home")
        self.img=Image(src="profile.png",width=200,height=200,col={"xs":3,"sm":3,"md":4,"lg":3.4,"xl":3.4})
        self.imgS = Image(src="senac.png",width=200,height=200,col={"xs":3,"sm":3.5,"md":4,"lg":3.4,"xl":3.4})
        iconepesquisa=Icon(name=Icons.SEARCH,color=Cores().corprimaria)
        self.pesquisa=TextField(prefix_icon=iconepesquisa,border_radius=10,label="Pesquisar",color="black",col={"xs":8,"sm":4,"md":4,"lg":3.4,"xl":3.4},label_style=TextStyle(color="black"),width=1000,bgcolor=Cores().corbranca)
        linhapesquisa=ResponsiveRow(controls=[self.img,self.imgS,self.pesquisa],alignment=MainAxisAlignment.CENTER,vertical_alignment=CrossAxisAlignment.CENTER)
        self.btnVisualizar=ElevatedButton(text="Visualizar",width=150,height=50,col={"xs":4,"sm":4,"md":4,"lg":2.7,"xl":2.7},style=ButtonStyle(bgcolor={ControlState.HOVERED:Cores().laranjaescuro,
        ControlState.FOCUSED:Colors.PINK,
        ControlState.DEFAULT:Cores().corsecundaria},color=Cores().corbranca,))
        self.btnGerenciar=ElevatedButton(text="Gerenciar",width=150,height=50,col={"xs":4,"sm":4,"md":4,"lg":2.7,"xl":2.7},style=ButtonStyle(bgcolor={ControlState.HOVERED:Cores().laranjaescuro,
        ControlState.FOCUSED:Colors.PINK,
        ControlState.DEFAULT:Cores().corsecundaria},color=Cores().corbranca,))
        self.btnEntrada=ElevatedButton(text="Entradas",width=150,height=50,col={"xs":4,"sm":4,"md":4,"lg":2.7,"xl":2.7},style=ButtonStyle(bgcolor={ControlState.HOVERED:Cores().laranjaescuro,
        ControlState.FOCUSED:Colors.PINK,
        ControlState.DEFAULT:Cores().corsecundaria},color=Cores().corbranca,))
        self.btnSaida=ElevatedButton(text="Saidas",width=150,height=50,col={"xs":4,"sm":4,"md":4,"lg":2.7,"xl":2.7},style=ButtonStyle(bgcolor={ControlState.HOVERED:Cores().laranjaescuro,
        ControlState.FOCUSED:Colors.PINK,
        ControlState.DEFAULT:Cores().corsecundaria},color=Cores().corbranca,))
        linhabotoes=ResponsiveRow(controls=[self.btnVisualizar,self.btnGerenciar,self.btnEntrada,self.btnSaida],alignment=MainAxisAlignment.CENTER,vertical_alignment=CrossAxisAlignment.CENTER,spacing=20)
        conteudo=Column(controls=[linhapesquisa,linhabotoes],spacing=100)
        self.produtos=Column(controls=[Text("Vassoura",size=40),Text("Sabonete",size=40),Text("Alvejante",size=40),Text("Alvejante",size=40),Text("Alvejante",size=40),Text("Alvejante",size=40),Text("Alvejante",size=40),Text("Alvejante",size=40),Text("Alvejante",size=40),Text("Alvejante",size=40),Text("Alvejante",size=40),Text("Alvejante",size=40),Text("Alvejante",size=40),Text("Alvejante",size=40),Text("Alvejante",size=40),Text("Alvejante",size=40),Text("Alvejante",size=40)],scroll=ScrollMode.AUTO)
        conteinerprodutos=Container(content=self.produtos,alignment=alignment.center)
        partedecima=Container(bgcolor=Cores().corbranca,width=3000,height=500,content=conteudo)
        partedebaixo=Container(bgcolor=Cores().corprimaria,width=2000,height=1000,alignment=alignment.center,content=Container(bgcolor=Cores().corbranca,width=1200,height=900,border=border.all(2, Colors.BLACK),content=conteinerprodutos))
        self.scroll=True

   
        

        self.controls=[partedecima,partedebaixo]