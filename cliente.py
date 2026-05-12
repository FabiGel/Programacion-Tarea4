from entidad_base import EntidadBase
from excepciones import ClienteError

# Clase Cliente
class Cliente(EntidadBase):

    def __init__(self, nombre, correo, telefono):

        # Validación del nombre
        if nombre.strip() == "":
            raise ClienteError("El nombre no puede estar vacío")

        # Validación del correo
        if "@" not in correo:
            raise ClienteError("Correo inválido")

        # Validación del teléfono
        if not telefono.isdigit():
            raise ClienteError("El teléfono debe contener números")

        # Encapsulación
        self.__nombre = nombre
        self.__correo = correo
        self.__telefono = telefono

    # Mostrar información
    def mostrar_info(self):

        return f"""
Cliente:
Nombre: {self.__nombre}
Correo: {self.__correo}
Teléfono: {self.__telefono}
"""