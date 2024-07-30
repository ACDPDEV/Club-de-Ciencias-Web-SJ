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
                font_size="16px",
                line_height="26px",
                
                color="#EEE",
            ),
            
            display="flex",
            flex_direction="row",
            align_items="center",
            gap="15px",
            
            height="40px",
        ),
        rx.hstack(
            rx.text(
                "Inicio",
                
                color="#8D9C93",
            ),
            rx.text(
                "Proyectos",
                
                color="#8D9C93",
            ),
            rx.text(
                "Miembros",
                
                color="#8D9C93",
            ),
            rx.text(
                "Contacto",
                
                color="#8D9C93",
            ),
            
            font_weight="400",
            font_size="16px",
            line_height="26px",
            
            right="0px",
        ),
        
        display="flex",
        flex_direction="row",
        justify_content="space-between",
        align_items="center",
        padding="15px 15px",
        
        position="sticky",
        width="100%",
        height="70px",
        top="0px",
        left="0px",
        
        background="#131217",
        
        z_index="100",
    )