class Autor:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def mostrarInfo(self):
        print("Autor:", self.nombre)
        print("Nacionalidad:", self.nacionalidad)