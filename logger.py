from datetime import datetime

# Registrar eventos y errores
def registrar_log(mensaje):

    with open("logs.txt", "a", encoding="utf-8") as archivo:

        fecha = datetime.now()

        archivo.write(f"[{fecha}] {mensaje}\n")