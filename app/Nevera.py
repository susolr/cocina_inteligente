# archivo: Receta.py
# autor: Jesús López Rodríguez
# descripción: Este archivo contiene funciones para gestionar la clase Nevera

class Nevera:
    def __init__(self):
        self.alimentos = {}
        
    def add_alimento(self, alimento, cantidad=1):
         self.alimentos[alimento] = self.alimentos.get(alimento, 0) + cantidad
    
    def get_alimentos(self):
        return self.alimentos
    
    def get_lista_de_alimentos_no_disponibles(self, receta):
        #print (receta)
        faltantes = []
        for ingrediente in receta.ingredientes:
            cantidad_en_nevera = self.alimentos.get(ingrediente, 0)
            if cantidad_en_nevera == 0:
                faltantes.append(ingrediente)
        return faltantes
    
    
            
        