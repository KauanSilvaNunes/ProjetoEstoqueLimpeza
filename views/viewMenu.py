from flet import *
from flet.core.alignment import center
from utils.cores import Cores

class ViewMenu(View):

    def __init__(self):
        super().__init__()

        self.route=("/home")

        self.img=Image(src="profile.png")
        self.imgS = Image(src="senac.png")

        self.bloco = Container(
            bgcolor=Cores().corprimaria,
            width=1920,
            height=300,
            content=Column(
                alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                spacing=30,
                controls=[
                    Row(
                        alignment=MainAxisAlignment.CENTER,
                        spacing=100,
                        controls=[
                            Container(bgcolor="White", width=100, height=100, border_radius=100, content=self.img),
                            Container(bgcolor=Cores().corprimaria, width=530, height=100, content=self.imgS),
                            Container(bgcolor="White", width=450, height=40,border_radius=5,
                                                        content=TextField(label="Procurar Produtos",
                                                        bgcolor=Cores().homefundo,
                                                        color="Black",
                                                        hint_text="Buscando...",
                                                        label_style= TextStyle(color="Black"))),
                        ]
                    ),
                    Row(
                        alignment=MainAxisAlignment.CENTER,
                        spacing=10,
                        controls=[
                            ElevatedButton(
                                bgcolor=Cores().corsecundaria,
                                width=320,
                                height=50,
                                content=Text("Visualizar Estoque", text_align=center, color=Cores().corbranca)
                            ),
                            ElevatedButton(
                                bgcolor=Cores().corsecundaria,
                                width=320,
                                height=50,
                                content=Text("Gerenciar Produtos", text_align=center, color=Cores().corbranca)
                            ),
                            ElevatedButton(
                                bgcolor=Cores().corsecundaria,
                                width=320,
                                height=50,
                                content=Text("Entrada de Produto", text_align=center, color=Cores().corbranca)
                            ),
                            ElevatedButton(
                                bgcolor=Cores().corsecundaria,
                                width=320,
                                height=50,
                                content=Text("Saída de Produto", text_align=center, color=Cores().corbranca)
                            ),
                        ]
                    )
                ]
            )
        )

        self.bloco2 = Container(
            bgcolor=Cores().corbranca,
            width=1920,
            height=400,
            alignment=alignment.center,
            content=Container(
                bgcolor=Cores().corprimaria,
                width=1300,
                height=350,
                border=border.all(2, "Black"),
                alignment=alignment.center,
                    content=Column(
                        spacing=5,
                        scroll=ScrollMode.AUTO,
                        controls=[

                        Container(
                        bgcolor=Cores().corbranca,
                        width=1250,
                        height=50,
                        alignment=alignment.center,
                            content=Container(
                                bgcolor="Black",
                                width=1230,
                                height=40,
                                alignment=alignment.center,
                                    content=Text("Exemplo de Produto", color=Cores().corbranca)
                            )
                    ),
                        Container(
                        bgcolor=Cores().corbranca,
                        width=1250,
                        height=50,
                        alignment=alignment.center
                    ),
                        Container(
                        bgcolor=Cores().corbranca,
                        width=1250,
                        height=50,
                        alignment=alignment.center
                    ),
                        Container(
                        bgcolor=Cores().corbranca,
                        width=1250,
                        height=50,
                        alignment=alignment.center
                    ),
                        Container(
                        bgcolor=Cores().corbranca,
                        width=1250,
                        height=50,
                        alignment=alignment.center

                    ),  Container(
                        bgcolor=Cores().corbranca,
                        width=1250,
                        height=50,
                        alignment=alignment.center
                    ),

                        Container(
                        bgcolor=Cores().corbranca,
                        width=1250,
                        height=50,
                        alignment=alignment.center
                    ),

                        Container(
                        bgcolor=Cores().corbranca,
                        width=1250,
                        height=50,
                        alignment=alignment.center
                    ),
                    ]
                )
            )
        )

        self.controls=[self.bloco, self.bloco2]