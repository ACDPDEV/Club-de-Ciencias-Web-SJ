import reflex as rx


def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "SJ - Club de Ciencias - Abundio Sagastegui Alva",
            height="20px"
        ),
        position="sticky",
        bg="#0f7",
        box_sizing="border-box",
        width="100vw",
        height="10vh",
        padding="10px",
        z_index="100"
    )