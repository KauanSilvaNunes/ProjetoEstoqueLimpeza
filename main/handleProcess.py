from flet import*
from main.constructors.constructorLogin import constructorLogin
from main.constructors.constructorMenu import constructorMenu


def main(page:Page):

    page.title = "Gerenciador de Estoque"
    page.theme_mode = ThemeMode.LIGHT
    page.window.resizable = False
    page.window.maximized = True

  


        

    def changeRoute(route):
        page.views.clear()
        if page.route == "/":
            page.views.append(constructorLogin(page=page))
        elif page.route=="/home":
            page.views.append(constructorMenu())

        page.update()

    page.on_route_change = changeRoute
    page.go(page.route)


