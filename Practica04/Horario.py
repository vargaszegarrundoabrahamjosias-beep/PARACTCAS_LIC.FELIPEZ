class Horario:
    def __init__(self, dias, hora_apertura, hora_cierre):
        self.dias = dias
        self.hora_apertura = hora_apertura
        self.hora_cierre = hora_cierre

    def mostrarHorario(self):
        print("Dias:", self.dias)
        print("Apertura:", self.hora_apertura)
        print("Cierre:", self.hora_cierre)