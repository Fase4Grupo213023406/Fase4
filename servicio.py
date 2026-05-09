
# Debe de completarse y mejorar el apartado de los servicios para que pueda calcular correctamente los costos y en el menu al soliciar informcacion del usuario debe aparecer los datos
# y ademas los servicios o reservar que se realizo con el usuario. 
from abc import ABC, abstractmethod

class Servicio(ABC):
    #Clase abstracta que define la base para todos los servicios
    def __init__(self, nombre, precio_base):
        self.nombre = nombre
        self.precio_base = precio_base

    @abstractmethod
    def calcular_costo(self, horas, **kwargs):
    # Método abstracto que obliga al polimorfismo en las subclases .
        pass

# --- SUBCLASES ----

class ReservaSala(Servicio):
    def calcular_costo(self, horas, limpieza=0): 
        # Implementa sobrecarga mediante parámetros opcionales.
        return (self.precio_base * horas) + limpieza

class AlquilerEquipo(Servicio):
    def calcular_costo(self, horas, seguro=False):
        # Implementa polimorfismo .
        total = self.precio_base * horas
        return total * 1.15 if seguro else total # Recargo del 15% por seguro.

class AsesoriaEspecializada(Servicio):
    def calcular_costo(self, horas, descuento=0):
        # Implementa variantes del cálculo con parámetros opcionales.
        return (self.precio_base * horas) - descuento