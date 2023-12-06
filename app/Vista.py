# archivo: Vista.py
# autor: Jesús López Rodríguez
# descripción: Este archivo contiene funciones para gestionar la interfaz de texto de la aplicacion

class Vista:
    def mostrar_menu_principal(self):
        print("\n-----------------------------")
        print("Menú principal:")
        print("1. Ver recetas disponibles")
        print("2. Ver alimentos en la nevera")
        print("3. Ver todas las recetas")
        print("4. Inspeccionar receta")
        print("5. Salir")
        
    def mostrar_menu_inspeccionar_receta(self):
        print("\n***************************")
        print("Menú de Inspección de Receta:")
        print("1. Ver método de preparación")
        print("2. Ver alimentos necesarios")
        print("3. Ver alimentos que faltan")
        print("4. Salir")
        
    def mostrar_recetas(self, recetas):
        if not recetas:
            print("\nNo hay recetas disponibles.")
        else:
            print("\nRecetas disponibles:")
            for i, receta in enumerate(recetas, start=1):
                print(f"{i}. {receta.nombre}")
    
    def mostrar_alimentos_necesarios(self, receta):
        print(f"\nAlimentos necesarios para '{receta.nombre}':")
        for alimento in receta.ingredientes:
            print(f"- {alimento.nombre}")
            
    def mostrar_alimentos_que_faltan(self, alimentos_que_faltan):
        if not alimentos_que_faltan:
            print("\nNo faltan alimentos.")
        else:
            print("\nAlimentos que faltan:")
            for alimento in alimentos_que_faltan:
                print(f"- {alimento.nombre}")
                
    def mostrar_metodo_preparacion(self, receta):
        print(f"\nMétodo de preparación de '{receta.nombre}':")
        print(receta.preparacion)

    def mostrar_alimentos_en_nevera(self, alimentos_en_nevera):
        if not alimentos_en_nevera:
            print("\nLa nevera está vacía.")
        else:
            print("\nAlimentos en la nevera:")
            for alimento, cantidad in alimentos_en_nevera.items():
                print(f"- {alimento.nombre}: {cantidad}")
