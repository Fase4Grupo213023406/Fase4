# aca se debe agregar # Importar excepción personalizada para manejo de errores
from excepciones import ReservaError


class Reserva:

    def __init__(self, cliente, servicio, duracion):

        try:

            # Validación
            if duracion <= 0:

                raise ReservaError(
                    "La duración debe ser mayor a cero."
                )

            self.cliente = cliente
            self.servicio = servicio
            self.duracion = duracion

            # Calcular costo automáticamente
            self.costo = servicio.calcular_costo(duracion)

            self.estado = "Confirmada"

        except ReservaError as e:

            raise ReservaError(
                f"Error al crear reserva: {e}"
            )

    # Método para cancelar
    def cancelar_reserva(self):

        self.estado = "Cancelada"

    # Mostrar información
    def __str__(self):

        return (
            f"\nCliente: {self.cliente.nombre}"
            f"\nServicio: {self.servicio.nombre}"
            f"\nDuración: {self.duracion} horas"
            f"\nCosto Total: ${self.costo}"
            f"\nEstado: {self.estado}"
        )