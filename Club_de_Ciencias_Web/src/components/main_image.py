import reflex as rx


def main_image() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="/main_image.jpg",
            min_width="100%",
            min_height="100%",
            filter="blur(10px)"
        ),
        width="100%",
        height="90vh",
        bg="#574710"
    )