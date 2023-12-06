# archivo: Receta.py
# autor: Jesús López Rodríguez
# descripción: Este archivo contiene funciones para gestionar la clase Receta

class Receta:
    def __init__(self, nombre, ingredientes, preparacion):
        if not ingredientes:
            raise ValueError("Una receta debe tener al menos un ingrediente.")
        self.nombre = nombre
        self.ingredientes = ingredientes
        self.preparacion = preparacion
        
    def __eq__(self, receta):
        return isinstance(receta, Receta) and self.nombre == receta.nombre
