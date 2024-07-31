import reflex as rx


def presentation() -> rx.Component:
    return rx.vstack(
        rx.vstack(
            rx.center(
                rx.html(
                    "<strong>¿Quiénes somos?</strong>",
                    
                    font_size="50px",
                ),
                
                width="100%"
            ),
            rx.vstack(
                rx.text(
                    "Somos el Club de Ciencias Abundio Sagastegui Alva del colegio emblemático San Juan."
                ),
                rx.text(
                    """
                    Nuestro club tiene como misión fomentar el interés y el conocimiento científico entre los estudiantes
                    del colegio San Juan. Inspirados por la obra de Abundio Sagastegui Alva, nos dedicamos a la 
                    exploración y difusión de las ciencias naturales, tecnológicas, matemáticas, etc.
                    """
                ),
                rx.text(
                    """
                    Fundado en 2024, nuestro club ha crecido para convertirse en un espacio de aprendizaje, 
                    investigación y colaboración entre estudiantes interesados en la ciencia.
                    """
                ),
                
                gap="25px"
            ),
            
            gap="50px"
        ),
    )