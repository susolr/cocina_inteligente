# archivo: Alimento.py
# autor: Jesús López Rodríguez
# descripción: Este archivo contiene funciones para gestionar la clase Alimento

class Alimento:
    def __init__(self, nombre):
        self.nombre = nombre
        
    def __eq__(self, alimento):
        return isinstance(alimento, Alimento) and self.nombre == alimento.nombre

    def __hash__(self):
        return hash(self.nombre)