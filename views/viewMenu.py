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
        self.produtos = Column(
        visible=False,
        controls=[
        Text("Sabão - Quantidade: 10 (Mín: 5, Máx: 20) | Status: OK", size=20),
        Divider(thickness=1, color=Colors.BLACK),
        Text("Desinfetante - Quantidade: 3 (Mín: 5, Máx: 15) | Status: Precisa reabastecer", size=20),
        Divider(thickness=1, color=Colors.BLACK),
        Text("Papel Higiênico - Quantidade: 25 (Mín: 10, Máx: 30) | Status: OK", size=20),
        Divider(thickness=1, color=Colors.BLACK),
        Text("Álcool 70% - Quantidade: 2 (Mín: 5, Máx: 20) | Status: Precisa reabastecer", size=20),
        Divider(thickness=1, color=Colors.BLACK),
        Text("Vassoura - Quantidade: 6 (Mín: 3, Máx: 10) | Status: OK", size=20),
        Divider(thickness=1, color=Colors.BLACK),
        Text("Balde - Quantidade: 1 (Mín: 2, Máx: 5) | Status: Precisa reabastecer", size=20),
        Divider(thickness=1, color=Colors.BLACK),
        Text("Lustra-móveis - Quantidade: 8 (Mín: 4, Máx: 10) | Status: OK", size=20),
        Divider(thickness=1, color=Colors.BLACK),
        Text("Detergente - Quantidade: 0 (Mín: 5, Máx: 15) | Status: Precisa reabastecer", size=20),
        Divider(thickness=1, color=Colors.BLACK),
        Text("Pano de chão - Quantidade: 12 (Mín: 6, Máx: 20) | Status: OK", size=20),
        Divider(thickness=1, color=Colors.BLACK),
        Text("Saco de lixo - Quantidade: 4 (Mín: 5, Máx: 25) | Status: Precisa reabastecer", size=20),
        Divider(thickness=1, color=Colors.BLACK),
        Text("Desengordurante - Quantidade: 7 (Mín: 5, Máx: 12) | Status: OK", size=20),Divider(thickness=1, color=Colors.BLACK),
        ],
        scroll=ScrollMode.AUTO)

        self.entradas = Column(
        visible=False,
        controls=[
            Text("Sabão - Entrada: 5 unidades", size=20),
            Divider(thickness=1, color=Colors.BLACK),
            Text("Desinfetante - Entrada: 10 unidades", size=20),
            Divider(thickness=1, color=Colors.BLACK),
            Text("Papel Higiênico - Entrada: 20 unidades", size=20),
            Divider(thickness=1, color=Colors.BLACK),
            Text("Álcool 70% - Entrada: 3 unidades", size=20),
            Divider(thickness=1, color=Colors.BLACK),
            Text("Vassoura - Entrada: 2 unidades", size=20),
            Divider(thickness=1, color=Colors.BLACK),
            Text("Detergente - Entrada: 15 unidades", size=20),
            Divider(thickness=1, color=Colors.BLACK),
            Text("Saco de lixo - Entrada: 12 unidades", size=20),
            Divider(thickness=1, color=Colors.BLACK),
            Text("Lustra-móveis - Entrada: 4 unidades", size=20),
            Divider(thickness=1, color=Colors.BLACK),
            Text("Pano de chão - Entrada: 7 unidades", size=20),
            Divider(thickness=1, color=Colors.BLACK),
            Text("Balde - Entrada: 1 unidade", size=20),
            Divider(thickness=1, color=Colors.BLACK)
        ],
        scroll=ScrollMode.AUTO
            )
        self.saidas = Column(
            visible=False,
            controls=[
                Text("Sabão - Saída: 3 unidades | Estoque → Sala 21", size=20),
                Divider(thickness=1, color=Colors.BLACK),
                Text("Desinfetante - Saída: 2 unidades | Estoque → Banheiro Feminino 3º andar", size=20),
                Divider(thickness=1, color=Colors.BLACK),
                Text("Papel Higiênico - Saída: 6 unidades | Estoque → Banheiro Masculino 2º andar", size=20),
                Divider(thickness=1, color=Colors.BLACK),
                Text("Álcool 70% - Saída: 4 unidades | Estoque → Copa", size=20),
                Divider(thickness=1, color=Colors.BLACK),
                Text("Detergente - Saída: 1 unidade | Estoque → Sala dos Professores", size=20),
                Divider(thickness=1, color=Colors.BLACK),
                Text("Pano de chão - Saída: 5 unidades | Estoque → Banheiro Masculino 3º andar", size=20),
                Divider(thickness=1, color=Colors.BLACK),
                Text("Vassoura - Saída: 2 unidades | Estoque → Banheiro Feminino Térreo", size=20),
                Divider(thickness=1, color=Colors.BLACK),
                Text("Saco de lixo - Saída: 10 unidades | Estoque → Sala 13", size=20),
                Divider(thickness=1, color=Colors.BLACK)
            ],
            scroll=ScrollMode.AUTO
            )


        self.conteinerprodutos=Container(content=self.produtos,padding=10)
        partedecima=Container(bgcolor=Cores().corbranca,width=3000,height=500,content=conteudo)
        partedebaixo=Container(bgcolor=Cores().corprimaria,width=2000,height=1000,alignment=alignment.center,content=Container(bgcolor=Cores().corbranca,width=1200,height=900,border=border.all(2, Colors.BLACK),content=self.conteinerprodutos))
        self.scroll=True

   
        

        self.controls=[partedecima,partedebaixo]