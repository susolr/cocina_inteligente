# archivo: Receta.py
# autor: Jesús López Rodríguez
# descripción: Este archivo contiene funciones para gestionar la clase Nevera

class Nevera:
    _instance = None
    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Nevera, cls).__new__(cls)
            cls._instance.alimentos = {}
        return cls._instance
        
    def add_alimento(self, alimento, cantidad=1):
         self.alimentos[alimento] = self.alimentos.get(alimento, 0) + cantidad
    
    def get_alimentos(self):
        return self.alimentos

    def vaciar_nevera(self):
        self.alimentos = {}
    
    def get_lista_de_alimentos_no_disponibles(self, receta):
        faltantes = []
        for ingrediente in receta.ingredientes:
            cantidad_en_nevera = self.alimentos.get(ingrediente, 0)
            if cantidad_en_nevera == 0:
                faltantes.append(ingrediente)
        return faltantes  

        