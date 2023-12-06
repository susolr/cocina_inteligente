# archivo: Receta.py
# autor: Jesús López Rodríguez
# descripción: Este archivo contiene funciones para gestionar la clase Recetario
from app.Nevera import Nevera

class Recetario:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Recetario, cls).__new__(cls)
            cls._instance.recetas = []
        return cls._instance

    def add_receta(self, receta):
        if receta not in self.recetas:
            self.recetas.append(receta)

    def buscar_recetas_disponibles(self):
        recetas_disponibles = []
        nevera = Nevera()
        for receta in self.recetas:
            faltantes = nevera.get_lista_de_alimentos_no_disponibles(receta)
            if not faltantes:
                recetas_disponibles.append(receta)
        return recetas_disponibles

    def mostrar_recetas(self):
        if not self.recetas:
            print("El recetario está vacío.")
        else:
            print("Recetas en el recetario:")
            for receta in self.recetas:
                print(f"- {receta.nombre}")