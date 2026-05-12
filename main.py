from cliente import Cliente
from servicios import (
    ReservaSala,
    AlquilerEquipo,
    AsesoriaEspecializada
)
from reserva import Reserva
from sistema import Sistema
from logger import registrar_log

sistema = Sistema()

print("===== SOFTWARE FJ =====")


# CLIENTE VÁLIDO
try:

    cliente1 = Cliente(
        "Fabio",
        "fabio@gmail.com",
        "300123456"
    )

    sistema.agregar_cliente(cliente1)

    print("Cliente registrado correctamente")

except Exception as e:

    registrar_log(str(e))

    print("Error:", e)


# CLIENTE INVÁLIDO
try:

    cliente2 = Cliente(
        "",
        "correo_malo",
        "abc"
    )

    sistema.agregar_cliente(cliente2)

except Exception as e:

    registrar_log(str(e))

    print("Error:", e)


# SERVICIO VÁLIDO
try:

    sala = ReservaSala(
        "Sala VIP",
        50000
    )

    print(sala.descripcion())

except Exception as e:

    registrar_log(str(e))

    print("Error:", e)


# RESERVA VÁLIDA
try:

    reserva1 = Reserva(
        cliente1,
        sala,
        3
    )

    costo = reserva1.procesar()

    sistema.agregar_reserva(reserva1)

except Exception as e:

    registrar_log(str(e))

    print("Error:", e)

else:

    print("Reserva procesada correctamente")
    print("Costo:", costo)

finally:

    print("Proceso de reserva finalizado")


# RESERVA INVÁLIDA
try:

    reserva2 = Reserva(
        cliente1,
        sala,
        -5
    )

except Exception as e:

    registrar_log(str(e))

    print("Error:", e)


# CLIENTE CON TELÉFONO INVÁLIDO
try:

    cliente3 = Cliente(
        "Carlos",
        "carlos@gmail.com",
        "telefono"
    )

    sistema.agregar_cliente(cliente3)

except Exception as e:

    registrar_log(str(e))

    print("Error:", e)


# SERVICIO CON PRECIO INVÁLIDO
try:

    servicio_error = ReservaSala(
        "Sala incorrecta",
        -100
    )

except Exception as e:

    registrar_log(str(e))

    print("Error:", e)


# CLIENTE CON CORREO INVÁLIDO
try:

    cliente4 = Cliente(
        "Ana",
        "correo_invalido",
        "123456789"
    )

    sistema.agregar_cliente(cliente4)

except Exception as e:

    registrar_log(str(e))

    print("Error:", e)


# SERVICIO DE ALQUILER DE EQUIPOS
try:

    equipo = AlquilerEquipo(
        "Computadores",
        80000
    )

    print(equipo.descripcion())

    costo_equipo = equipo.calcular_costo(2)

    print("Costo alquiler:", costo_equipo)

except Exception as e:

    registrar_log(str(e))

    print("Error:", e)


# SERVICIO DE ASESORÍA ESPECIALIZADA
try:

    asesoria = AsesoriaEspecializada(
        "Asesoría Python",
        120000
    )

    print(asesoria.descripcion())

    costo_asesoria = asesoria.calcular_costo(3)

    print("Costo asesoría:", int(costo_asesoria))

except Exception as e:

    registrar_log(str(e))

    print("Error:", e)


# RESERVA CON SERVICIO INVÁLIDO
try:

    reserva3 = Reserva(
        cliente1,
        None,
        2
    )

except Exception as e:

    registrar_log(str(e))

    print("Error:", e)


print("Sistema funcionando correctamente")