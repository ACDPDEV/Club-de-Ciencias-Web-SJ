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
        rx.box(    
            main_image(),
            rx.center(
                rx.vstack(
                    presentation(),
                    information(),
                    max_width="600px",
                    width="100%",
                    margin="25px"
                ),
                
                margin_top="150px"
            ),
            
            width="100%",
            height="100%",
            
            box_sizing="border-box",
            padding="15px",
        ),
    )

app = rx.App(
    stylesheets=[
        "/general.css",
    ],
)
app.add_page(index)