from excepciones import ReservaError

# Clase Reserva
class Reserva:

    def __init__(self, cliente, servicio, duracion):

        if duracion <= 0:
            raise ReservaError("La duración debe ser mayor que cero")

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    # Confirmar reserva
    def confirmar(self):

        self.estado = "Confirmada"

    # Cancelar reserva
    def cancelar(self):

        self.estado = "Cancelada"

    # Procesar reserva
    def procesar(self):

        try:

            costo = self.servicio.calcular_costo(self.duracion)

            self.estado = "Procesada"

            return costo

        except Exception as e:

            raise ReservaError("Error procesando reserva") from e