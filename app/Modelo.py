# archivo: Modelo.py
# autor: Jesús López Rodríguez
# descripción: Este archivo contiene funciones para gestionar el modelo de la aplicación

from app.Nevera import Nevera
from app.Recetario import Recetario
from app.Alimento import Alimento
from app.Receta import Receta

class Modelo:
    def __init__(self):
        self.nevera = Nevera()
        self.recetario = Recetario()
        self.inicializar_informacion_ejemplo()
    
    def inicializar_informacion_ejemplo(self):
        manzana = Alimento("Manzana")
        salmon = Alimento("Salmon")
        langostino = Alimento("Langostino")

        # Crear recetas
        salmon_compota = Receta("Salmon con compota de manzana", [manzana,salmon], "Hacer el salmon al horno y triturar la manzana. Agregar en mitad de la coccion")
        langostinos_plancha = Receta("Langostinos plancha", [langostino], "Colocar sobre aceite caliente")

        self.recetario.add_receta(salmon_compota)
        self.recetario.add_receta(langostinos_plancha)

        self.nevera.add_alimento(manzana, cantidad=2)
        self.nevera.add_alimento(langostino, cantidad=3)
