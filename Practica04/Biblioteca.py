from Horario import Horario
from Prestamo import Prestamo


class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre

        self.libros = []
        self.autores = []
        self.prestamos = []

        self.horario = Horario(
            "Lunes a Viernes",
            "08:00",
            "20:00"
        )

    def agregarLibro(self, libro):
        self.libros.append(libro)

    def agregarAutor(self, autor):
        self.autores.append(autor)

    def prestarLibro(self, estudiante, libro):
        prestamo = Prestamo(estudiante, libro)
        self.prestamos.append(prestamo)

    def mostrarEstado(self):
        print("\n===== BIBLIOTECA =====")
        print("Nombre:", self.nombre)

        print("\nHORARIO")
        self.horario.mostrarHorario()

        print("\nLIBROS")
        for libro in self.libros:
            print("-", libro.titulo)

        print("\nAUTORES")
        for autor in self.autores:
            print("-", autor.nombre)

        print("\nPRESTAMOS")
        for prestamo in self.prestamos:
            prestamo.mostrarInfo()

    def cerrarBiblioteca(self):
        print("\nBiblioteca cerrada")
        self.prestamos.clear()