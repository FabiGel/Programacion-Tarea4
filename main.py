from cliente import Cliente
from servicios import ReservaSala
from reserva import Reserva
from sistema import Sistema
from logger import registrar_log

sistema = Sistema()

print("===== SOFTWARE FJ =====")

# Cliente válido
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

    print(e)

# Cliente inválido
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

# Servicio válido
try:

    sala = ReservaSala(
        "Sala VIP",
        50000
    )

    print(sala.descripcion())

except Exception as e:

    registrar_log(str(e))

# Reserva válida
try:

    reserva1 = Reserva(
        cliente1,
        sala,
        3
    )

    costo = reserva1.procesar()

    sistema.agregar_reserva(reserva1)

    print("Reserva procesada correctamente")
    print("Costo:", costo)

except Exception as e:

    registrar_log(str(e))

# Reserva inválida
try:

    reserva2 = Reserva(
        cliente1,
        sala,
        -5
    )

except Exception as e:

    registrar_log(str(e))

    print("Error:", e)

print("Sistema funcionando correctamente")