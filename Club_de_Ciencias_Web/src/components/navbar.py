import reflex as rx


def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "Abundio Sagastegui Alva",
            height="20px"
        ),
        position="sticky",
        top="0",
        bg="#0f7",
        box_sizing="border-box",
        width="100%",
        height="10vh",
        min_height="60px",
        # padding="10px",
        z_index="100"
    )