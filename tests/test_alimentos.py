# archivo: test_alimentos.py
# autor: Jesús López Rodríguez
# descripción: Este archivo contiene los test unitarios de la clase Alimento

import unittest
from app.Alimento import Alimento

class TestAlimento(unittest.TestCase):
    def test_creacion_alimento(self):
        alimento = Alimento("Manzana")
        self.assertEqual(alimento.nombre, "Manzana")
        
if __name__ == '__main__':
    unittest.main()