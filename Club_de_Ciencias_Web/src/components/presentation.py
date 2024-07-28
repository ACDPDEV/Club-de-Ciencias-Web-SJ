import reflex as rx


def presentation() -> rx.Component:
    return rx.vstack(
        rx.text(
            "Bienvenidos al Club de Ciencias Abundio Sagastegui Alva"
        ),
        rx.text(
            """
            Nuestro club tiene como misión fomentar el interés y el conocimiento científico entre los estudiantes
            del colegio San Juan. Inspirados por la vida y obra de Abundio Sagastegui Alva, nos dedicamos a la 
            exploración y difusión de las ciencias naturales, tecnológicas, matemáticas, etc.
            """
        ),
        rx.text(
            """
            Fundado en 2024, nuestro club ha crecido para convertirse en un espacio de aprendizaje, 
            investigación y colaboración entre estudiantes apasionados por la ciencia.
            """
        )
    )