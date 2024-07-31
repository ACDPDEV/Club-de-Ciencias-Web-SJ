import reflex as rx


def main_image() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.image(
                src="/ASA.svg",                
            ),
            rx.center(     
                rx.image(
                    src="/Background Icons.svg",
                ),
                
                position="absolute",
                left="0px",
                
                width="100%",
                
                z_index="96",
            ),
            rx.center(    
                rx.image(
                    src="ABUNDIO SAGASTEGUI ALVA.svg"  
                ),
                
                width="100%",
            ),
            
            gap="10vh",
            
            max_width="860px",
        )
    )