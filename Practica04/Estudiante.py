class Estudiante:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre

    def mostrarInfo(self):
        print("Codigo:", self.codigo)
        print("Nombre:", self.nombre)