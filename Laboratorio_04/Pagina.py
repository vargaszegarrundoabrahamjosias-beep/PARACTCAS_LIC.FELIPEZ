class Pagina:
    def __init__(self, numero, contenido):
        self.numero = numero
        self.contenido = contenido

    def mostrarPagina(self):
        print("Pagina:", self.numero)
        print("Contenido:", self.contenido)