from Autor import Autor
from Libro import Libro
from Estudiante import Estudiante
from Biblioteca import Biblioteca


autor1 = Autor("Abraham Josias Vargas Zegarrundo", "Bolivia")

libro1 = Libro(
    "Cien Años de Soledad",
    "12345",
    [
        "Pagina 1",
        "Pagina 2",
        "Pagina 3"
    ]
)

est1 = Estudiante("2025001", "Juan Perez")

biblioteca = Biblioteca("Biblioteca Central UMSA")

biblioteca.agregarLibro(libro1)
biblioteca.agregarAutor(autor1)

biblioteca.prestarLibro(est1, libro1)

biblioteca.mostrarEstado()

libro1.leer()

biblioteca.cerrarBiblioteca()