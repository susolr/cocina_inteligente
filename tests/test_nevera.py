# archivo: test_alimentos.py
# autor: Jesús López Rodríguez
# descripción: Este archivo contiene los test unitarios de la clase Nevera

import unittest
from app.Alimento import Alimento
from app.Receta import Receta
from app.Nevera import Nevera

class TestNevera(unittest.TestCase):
    def setUp(self):
        self.nevera = Nevera()
        self.manzana = Alimento("Manzana")
        self.huevo = Alimento("Huevo")

    def test_add_alimento(self):
        self.nevera.add_alimento(self.manzana)
        self.assertIn(self.manzana, self.nevera.alimentos)

    def test_get_lista_de_alimentos_no_disponibles(self):
        self.nevera.add_alimento(self.manzana)
        self.nevera.add_alimento(self.huevo)

        receta = Receta("Torta", [self.manzana, self.huevo], "Mezclar y hornear")
        faltantes = self.nevera.get_lista_de_alimentos_no_disponibles(receta)
        self.assertFalse(faltantes)