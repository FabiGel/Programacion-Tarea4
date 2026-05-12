from abc import ABC, abstractmethod
from excepciones import ServicioError

# Clase abstracta Servicio
class Servicio(ABC):

    def __init__(self, nombre, precio_base):

        if precio_base <= 0:
            raise ServicioError("El precio debe ser mayor que cero")

        self.nombre = nombre
        self.precio_base = precio_base

    @abstractmethod
    def calcular_costo(self, tiempo):
        pass

    @abstractmethod
    def descripcion(self):
        pass


# Servicio de reserva de salas
class ReservaSala(Servicio):

    def calcular_costo(self, horas, descuento=0):

        total = self.precio_base * horas
        total -= total * descuento

        return total

    def descripcion(self):

        return f"Servicio de reserva de salas: {self.nombre}"


# Servicio de alquiler de equipos
class AlquilerEquipo(Servicio):

    def calcular_costo(self, dias, impuesto=0):

        total = self.precio_base * dias
        total += total * impuesto

        return total

    def descripcion(self):

        return f"Servicio de alquiler de equipos: {self.nombre}"


# Servicio de asesorías
class AsesoriaEspecializada(Servicio):

    def calcular_costo(self, horas):

        return self.precio_base * horas * 1.2

    def descripcion(self):

        return f"Servicio de asesoría especializada: {self.nombre}"