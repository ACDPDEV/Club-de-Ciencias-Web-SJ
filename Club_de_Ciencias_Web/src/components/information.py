import reflex as rx


def information() -> rx.Component:
    return rx.vstack(
        rx.center(
            rx.html(
                "<strong>Datos</strong>",
                
                font_size="50px",
            ),
            
            width="100%"
        ),
        rx.vstack(
            rx.card(
                rx.html(
                    "<strong>Ubicación</strong>"
                ),
                rx.text(
                    "'Working in progress...'"
                ),
                
                width="100%"
            ),
            rx.card(
                rx.html(
                    "<strong>Grupo</strong>",
                ),
                rx.text(
                    "'Working in progress...'"
                ),
                
                width="100%"
            ),
            
            gap="25px",
            width="100%",
        ),
        
        gap="50px",
        width="100%",
    )