# archivo: test_recetas.py
# autor: Jesús López Rodríguez
# descripción: Este archivo contiene los test unitarios de la clase Receta

import unittest
from app.Alimento import Alimento
from app.Receta import Receta
from app.Nevera import Nevera

class TestReceta(unittest.TestCase):
    def test_creacion_receta(self):
        alimento = Alimento("Manzana")
        receta = Receta("Ensalada de Frutas", [alimento], "Cortar y mezclar")
        self.assertEqual(receta.nombre, "Ensalada de Frutas")
        self.assertEqual(receta.ingredientes, [alimento])
        self.assertEqual(receta.preparacion, "Cortar y mezclar")
        
    def test_receta_sin_ingredientes(self):
        with self.assertRaises(ValueError) as context:
            receta = Receta("Receta Sin Ingredientes", [], "Instrucciones")

        self.assertEqual(
            str(context.exception),
            "Una receta debe tener al menos un ingrediente."
        )