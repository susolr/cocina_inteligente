# archivo: Vista.py
# autor: Jesús López Rodríguez
# descripción: Este archivo contiene funciones para gestionar la interfaz de texto de la aplicacion

class Vista:
    def mostrar_menu_principal(self):
        print("\nMenú:")
        print("1. Ver recetas disponibles")
        print("2. Ver alimentos en la nevera")
        print("3. Salir")
        
    def mostrar_recetas(self, recetas):
        if not recetas:
            print("No hay recetas disponibles.")
        else:
            print("Recetas disponibles:")
            for receta in recetas:
                print(f"- {receta.nombre}")

    def mostrar_alimentos_en_nevera(self, alimentos_en_nevera):
        if not alimentos_en_nevera:
            print("La nevera está vacía.")
        else:
            print("Alimentos en la nevera:")
            for alimento, cantidad in alimentos_en_nevera.items():
                print(f"- {alimento.nombre}: {cantidad}")
