from abc import ABC, abstractmethod

# Clase abstracta base
class EntidadBase(ABC):

    @abstractmethod
    def mostrar_info(self):
        pass