# archivo: Controlador.py
# autor: Jesús López Rodríguez
# descripción: Este archivo contiene funciones para gestionar el controlador de la aplicación

class Controlador:
    def __init__(self, vista, modelo):
        self.vista = vista
        self.modelo = modelo

    def mostrar_recetas_disponibles(self):
        recetas_disponibles = self.modelo.recetario.buscar_recetas_disponibles()
        self.vista.mostrar_recetas(recetas_disponibles)

    def mostrar_alimentos_en_nevera(self):
        alimentos_en_nevera = self.modelo.nevera.get_alimentos()
        self.vista.mostrar_alimentos_en_nevera(alimentos_en_nevera)

    def ejecutar(self):
        print("Bienvenido a la Aplicación de Recetas")
        while True:
            self.vista.mostrar_menu_principal()

            opcion = input("Seleccione una opción (1/2/3): ")

            if opcion == "1":
                self.mostrar_recetas_disponibles()
            elif opcion == "2":
                self.mostrar_alimentos_en_nevera()
            elif opcion == "3":
                print("¡Hasta luego!")
                break
            else:
                print("Opción no válida. Inténtelo de nuevo.")
