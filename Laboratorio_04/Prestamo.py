from datetime import datetime

class Prestamo:
    def __init__(self, estudiante, libro):
        self.fechaPrestamo = datetime.now().strftime("%d/%m/%Y")
        self.fechaDevolucion = "Pendiente"

        self.estudiante = estudiante
        self.libro = libro

    def mostrarInfo(self):
        print("\n--- PRESTAMO ---")
        print("Fecha prestamo:", self.fechaPrestamo)
        print("Fecha devolucion:", self.fechaDevolucion)
        print("Estudiante:", self.estudiante.nombre)
        print("Libro:", self.libro.titulo)