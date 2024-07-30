import reflex as rx


def main_image() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.image(
                src="/ASA.svg",                
            ),
            rx.image(
                src="/Background Icons.svg",
                
                position="absolute",
                justify_content="center",
                z_index="99",
            ),
            rx.center(    
                rx.text(
                    " ABUNDIO SAGASTEGUI ALVA",
                    
                    class_name="main_name"
                ),
                
                width="100%"
            ),
            
            max_width="860px"
        )
    )