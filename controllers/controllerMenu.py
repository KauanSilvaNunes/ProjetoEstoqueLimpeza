from views.viewMenu import ViewMenu
from flet import *
from utils.cores import Cores
from flet.core.alignment import center


class ControllerMenu:
    def __init__(self,telaMenu:ViewMenu,page):
        self.page=page
        self.conteinerprodutos=telaMenu.conteinerprodutos
        self.btnVisualizar=telaMenu.btnVisualizar
        self.btnGerenciar=telaMenu.btnGerenciar
        self.btnEntrada=telaMenu.btnEntrada
        self.btnSaida=telaMenu.btnSaida
        self.produtos=telaMenu.produtos
        self.entradas=telaMenu.entradas
        self.saidas=telaMenu.saidas
        self.btnVisualizar.on_click=self.visualizar
        self.btnGerenciar.on_click=self.gerenciar
        self.btnEntrada.on_click=self.verentradas
        self.btnSaida.on_click=self.versaidas
        self.btnADD=ElevatedButton(text="Registrar",width=130,height=40,style=ButtonStyle(bgcolor=Cores().corsecundaria,color=Cores().corbranca))
        self.btnRemov=ElevatedButton(text="Remover",width=130,height=40,style=ButtonStyle(bgcolor=Cores().corsecundaria,color=Cores().corbranca))
        self.btnADD.on_click=self.troca
        self.btnRemov.on_click=self.trocadelete
        self.popup=AlertDialog(
        title=Text("Deseja registrar ou remover um produto?",size=15,color=Cores().corbranca),
        bgcolor=Cores().teste,
        content=Row(controls=[self.btnADD,self.btnRemov],height=100),actions=[
            TextButton("Fechar",style=ButtonStyle(color=Cores().corbranca),on_click=lambda e:page.close(self.popup)),
        ])
        self.txt_nome = TextField(
            label="Nome do Produto",
            width=300,
            border_radius=10,
            bgcolor=Colors.WHITE,
            label_style=TextStyle(color=Colors.BLACK),
            color=Colors.BLACK
        )

        self.txt_qtd = TextField(
            label="Quantidade",
            width=140,
            border_radius=10,
            bgcolor=Colors.WHITE,
            label_style=TextStyle(color=Colors.BLACK),
            color=Colors.BLACK,
        )

        self.txt_min = TextField(
            label="Quantidade Mínima",
            width=140,
            border_radius=10,
            bgcolor=Colors.WHITE,
            label_style=TextStyle(color=Colors.BLACK),
            color=Colors.BLACK,
        )

        self.txt_max = TextField(
            label="Quantidade Máxima",
            width=140,
            border_radius=10,
            bgcolor=Colors.WHITE,
            label_style=TextStyle(color=Colors.BLACK),
            color=Colors.BLACK,
        )

        formulario = Column(height=200,
            controls=[
                self.txt_nome,
                Column(controls=[self.txt_qtd, self.txt_min, self.txt_max],height=200,spacing=10)
            ],
            spacing=10
        )

        formulariodel = Column(height=200,
            controls=[
                self.txt_nome],
            spacing=10
        )


        self.popupadd = AlertDialog(
                    title=Text("Registrar novo produto", size=15, color=Cores().corbranca),
                    bgcolor=Cores().teste,
                    content=formulario,
                    actions=[
                        TextButton("Fechar", style=ButtonStyle(color=Cores().corbranca), on_click=lambda e: page.close(self.popupadd)),
                        TextButton("Confirmar", style=ButtonStyle(color=Cores().corbranca), on_click=self.registrar_produto)
                    ]
                )
        
        self.popupdel= AlertDialog(
                title=Text("Deletar produto", size=15, color=Cores().corbranca),
                bgcolor=Cores().teste,
                content=formulariodel,
                actions=[
                    TextButton("Fechar", style=ButtonStyle(color=Cores().corbranca), on_click=lambda e: page.close(self.popupdel)),
                    TextButton("Confirmar", style=ButtonStyle(color=Cores().corbranca), on_click=self.deletar_produto)
                ]
                )   




    def visualizar(self,e):
        self.conteinerprodutos.content = self.produtos
        self.produtos.visible=True
        self.saidas.visible=False
        self.entradas.visible=False
        self.page.update()


    def verentradas(self,e):
        self.conteinerprodutos.content = self.entradas
        self.produtos.visible=False
        self.saidas.visible=False
        self.entradas.visible=True
        self.page.update()

    def versaidas(self,e):
        self.conteinerprodutos.content=self.saidas
        self.produtos.visible=False
        self.entradas.visible=False
        self.saidas.visible=True
        self.page.update()

    def gerenciar(self,e):
        self.page.open(self.popup)
        self.page.update()

    def troca(self,e):
        self.page.close(self.popup)
        self.page.open(self.popupadd)

    def trocadelete(self,e):
        self.page.close(self.popup)
        self.page.open(self.popupdel)


    def registrar_produto(self, e):
        nome = self.txt_nome.value.strip()
        try:
            qtd = int(self.txt_qtd.value)
            minimo = int(self.txt_min.value)
            maximo = int(self.txt_max.value)
        except ValueError:
            self.page.snack_bar = SnackBar(Text("Preencha os campos numéricos corretamente.", color=Colors.WHITE), bgcolor=Colors.RED)
            self.page.snack_bar.open = True
            self.page.update()
            return

        if nome == "":
            self.page.snack_bar = SnackBar(Text("O nome do produto não pode estar vazio.", color=Colors.WHITE), bgcolor=Colors.RED)
            self.page.snack_bar.open = True
            self.page.update()
            return

        status = "Precisa reabastecer" if qtd < minimo else "OK"

        novo_texto = Text(
            f"{nome} - Quantidade: {qtd} (Mín: {minimo}, Máx: {maximo}) | Status: {status}",
            size=20,
        )
        divisor = Divider(thickness=1, color=Colors.BLACK)

        self.produtos.controls.append(novo_texto)
        self.produtos.controls.append(divisor)

        self.txt_nome.value = ""
        self.txt_qtd.value = ""
        self.txt_min.value = ""
        self.txt_max.value = ""

        self.popup.open = False
        self.page.update()

    def deletar_produto(self,e):
        pass




       

