# archivo: Receta.py
# autor: Jesús López Rodríguez
# descripción: Este archivo contiene funciones para gestionar la clase Nevera

class Nevera:
    def __init__(self):
        self.alimentos = {}
        
    def add_alimento(self, alimento):
        self.alimentos.append(alimento)
    
    def get_alimentos(self):
        return self.alimentos
    
    def get_lista_de_alimentos_no_disponibles(self, receta):
        faltantes = []
        for ingrediente in receta.ingredientes:
            cantidad_en_nevera = self.alimentos.get(ingrediente, 0)
            if cantidad_en_nevera == 0:
                faltantes.append(ingrediente)
        return faltantes
    
    
            
        