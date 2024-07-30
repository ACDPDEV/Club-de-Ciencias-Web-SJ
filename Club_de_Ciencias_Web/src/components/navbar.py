import reflex as rx


def navbar() -> rx.Component:
    return rx.hstack(
        rx.hstack(    
            rx.image(
                src="/Club de ciencias.png"
            ),
            rx.text(
                "Club de Ciencias - SAN JUAN",
                
                font_family="Segoe UI",
                font_style="normal",
                font_wight="700",
                font_size="23px",
                line_height="26px",
                
                color="#EEE",
            ),
            
            display="flex",
            flex_direction="row",
            align_items="center",
            gap="30px",
            
            height="40px",
        ),
        
        display="flex",
        flex_direction="row",
        justify_content="space-between",
        align_items="center",
        padding="15px 30px",
        gap="840px",
        
        position="sticky",
        width="100%",
        height="70px",
        top="0px",
        left="0px",
        
        background="#131217",
        
        z_index="100",
    )