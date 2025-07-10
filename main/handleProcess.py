from flet import*
from main.constructors.constructorLogin import constructorLogin
from main.constructors.constructorMenu import constructorMenu
from main.constructors.constructorCadastro import constructorCadastro


def main(page:Page):

    page.title = "Gerenciador de Estoque"
    page.theme_mode = ThemeMode.LIGHT
    page.window.resizable = True
    page.window.maximized = True
    page.window.min_height=1000
    page.window.min_width=600

        
    def changeRoute(route):
        page.views.clear()
        if page.route == "/":
            page.views.append(constructorLogin(page=page))
        elif page.route=="/home":
            page.views.append(constructorMenu())
        elif page.route=="/cadastro":
            page.views.append(constructorCadastro())

        page.update()

    page.on_route_change = changeRoute
    page.go(page.route)
