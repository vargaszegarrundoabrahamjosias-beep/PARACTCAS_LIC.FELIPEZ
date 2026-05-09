from Pagina import Pagina

class Libro:
    def __init__(self, titulo, isbn, contenidos_paginas):
        self.titulo = titulo
        self.isbn = isbn

        self.paginas = []

        num = 1

        for contenido in contenidos_paginas:
            pagina = Pagina(num, contenido)
            self.paginas.append(pagina)
            num += 1

    def leer(self):
        print("\nLibro:", self.titulo)

        for pagina in self.paginas:
            pagina.mostrarPagina()
            print("------------------")