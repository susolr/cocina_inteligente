# archivo: test_recetario.py
# autor: Jesús López Rodríguez
# descripción: Este archivo contiene los test unitarios de la clase Recetario

import unittest
from app.Alimento import Alimento
from app.Receta import Receta
from app.Nevera import Nevera
from app.Recetario import Recetario

class TestRecetario(unittest.TestCase):
    def setUp(self):
        self.recetario = Recetario()

    def test_unica_instancia(self):
        recetario1 = Recetario()
        recetario2 = Recetario()
        self.assertIs(recetario1, recetario2)

    def test_add_receta(self):
        receta = Receta("Sopa de picadillo", [Alimento("Pollo"),Alimento("Fideos")], "Cortar y mezclar")
        self.recetario.add_receta(receta)
        self.assertIn(receta, self.recetario.recetas)

    def test_buscar_recetas_disponibles_con_nevera_vacia(self):
        receta1 = Receta("Ensalada de Frutas", [Alimento("Manzana")], "Cortar y mezclar")
        receta2 = Receta("Torta", [Alimento("Manzana"), Alimento("Huevo"), Alimento("Harina")], "Mezclar y hornear")

        self.recetario.add_receta(receta1)
        self.recetario.add_receta(receta2)
    
        nevera_vacia = Nevera()
        nevera_vacia.vaciar_nevera()
        recetas_disponibles = self.recetario.buscar_recetas_disponibles()

        self.assertEqual(recetas_disponibles, [])

    def test_buscar_recetas_disponibles_con_nevera_con_suficientes_ingredientes(self):
        receta1 = Receta("Ensalada de Frutas", [Alimento("Manzana")], "Cortar y mezclar")
        receta2 = Receta("Torta", [Alimento("Manzana"), Alimento("Huevo"), Alimento("Harina")], "Mezclar y hornear")

        self.recetario.add_receta(receta1)
        self.recetario.add_receta(receta2)
        
        nevera_con_suficientes_ingredientes = Nevera()
        nevera_con_suficientes_ingredientes.vaciar_nevera()
        nevera_con_suficientes_ingredientes.add_alimento(Alimento("Manzana"))
        nevera_con_suficientes_ingredientes.add_alimento(Alimento("Huevo"))
        nevera_con_suficientes_ingredientes.add_alimento(Alimento("Harina"))

        recetas_disponibles = self.recetario.buscar_recetas_disponibles()

        self.assertEqual(recetas_disponibles, [receta1, receta2])

    def test_buscar_recetas_disponibles_con_nevera_con_ingredientes_insuficientes(self):
        receta1 = Receta("Ensalada de Frutas", [Alimento("Manzana")], "Cortar y mezclar")
        receta2 = Receta("Torta", [Alimento("Manzana"), Alimento("Huevo"), Alimento("Harina")], "Mezclar y hornear")

        self.recetario.add_receta(receta1)
        self.recetario.add_receta(receta2)
    
        nevera_con_ingredientes_insuficientes = Nevera()
        nevera_con_ingredientes_insuficientes.vaciar_nevera()
        nevera_con_ingredientes_insuficientes.add_alimento(Alimento("Manzana"))
        nevera_con_ingredientes_insuficientes.add_alimento(Alimento("Huevo"))

        recetas_disponibles = self.recetario.buscar_recetas_disponibles()

        self.assertEqual(recetas_disponibles, [receta1])
    
    