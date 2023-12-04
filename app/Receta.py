# archivo: Receta.py
# autor: Jesús López Rodríguez
# descripción: Este archivo contiene funciones para gestionar la clase Receta

class Receta:
    def __init__(self, nombre, ingredientes, preparacion):
        self.nombre = nombre
        self.ingredientes = ingredientes
        self.preparacion = preparacion
        print("Creando receta")