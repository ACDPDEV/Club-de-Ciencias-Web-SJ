import reflex as rx
from rxconfig import config
from Club_de_Ciencias_Web.src.components.navbar import navbar
from Club_de_Ciencias_Web.src.components.main_image import main_image
from Club_de_Ciencias_Web.src.components.presentation import presentation
from Club_de_Ciencias_Web.src.components.information import information


class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.box(
        navbar(),
        main_image(),
        rx.center(
            rx.vstack(
                presentation(),
                information(),
                max_width="600px",
                width="100%",
                margin="25px"
            )
        )
    )

app = rx.App()
app.add_page(index)