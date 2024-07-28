import reflex as rx
from rxconfig import config
from Club_de_Ciencias_Web.src.components.navbar import navbar
from Club_de_Ciencias_Web.src.components.main_image import main_image
from Club_de_Ciencias_Web.src.components.presentation import presentation


class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.vstack(
        navbar(),
        #main_image(),
        #presentation()
    )


app = rx.App()
app.add_page(index)