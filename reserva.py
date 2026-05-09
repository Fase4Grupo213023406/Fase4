class Reserva:
    # Clase Reserva: Vincula Cliente y Servicio gestionando su estado
    def __init__(self, cliente, servicio, duracion, costo):
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.costo = costo
        self.estado = "Confirmada" 

    def __str__(self):
        return f"Servicio: {self.servicio.nombre} | Duración: {self.duracion}h | Total: ${self.costo:.2f}"
        # este aparato deben de completarlo, solo es una base aunque no esta bien desarrollada, solo para complementar por eso no
        # lo importe, sin antes de que se complementa la seccion. 