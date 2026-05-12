from logger import registrar_log

# Sistema principal
class Sistema:

    def __init__(self):

        self.clientes = []
        self.reservas = []

    # Agregar cliente
    def agregar_cliente(self, cliente):

        self.clientes.append(cliente)

        registrar_log("Cliente agregado correctamente")

    # Agregar reserva
    def agregar_reserva(self, reserva):

        self.reservas.append(reserva)

        registrar_log("Reserva agregada correctamente")

    # Mostrar clientes
    def mostrar_clientes(self):

        for cliente in self.clientes:

            print(cliente.mostrar_info())