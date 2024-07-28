import reflex as rx


def information() -> rx.Component:
    return rx.vstack(
        rx.card(
            rx.text(
                "Ubicación"
            ),
            rx.text(
                "[Ubicación]"
            ),
            width="100%"
        ),
        rx.card(
            rx.text(
                "Grupo",
            ),
            rx.text(
                "[Grupo]"
            ),
            width="100%"
        ),
        width="100%"
    )