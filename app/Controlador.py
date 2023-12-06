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
    
    def mostrar_recetas_en_recetario(self):
        self.vista.mostrar_recetas(self.modelo.recetario.get_recetas())
        
    def inspeccionar_receta(self):
        recetas = self.modelo.recetario.get_recetas()
        self.vista.mostrar_recetas(recetas)
        if not recetas:
            return

        seleccion = int(input("Seleccione el número de la receta a inspeccionar: "))
        if seleccion in range(1, len(recetas) + 1):
            receta_seleccionada = recetas[seleccion - 1]
            print(f"\nInspeccionando receta: {receta_seleccionada.nombre}")
            while True:
                self.vista.mostrar_menu_inspeccionar_receta()
                opcion = input("Seleccione una opción (1/2/3/4): ")

                if opcion == "1":
                    self.vista.mostrar_metodo_preparacion(receta_seleccionada)
                elif opcion == "2":
                    self.vista.mostrar_alimentos_necesarios(receta_seleccionada)
                elif opcion == "3":
                    alimentos_que_faltan = self.modelo.nevera.get_lista_de_alimentos_no_disponibles(receta_seleccionada)
                    self.vista.mostrar_alimentos_que_faltan(alimentos_que_faltan)
                elif opcion == "4":
                    print("Volviendo al menú principal.")
                    break
                else:
                    print("Opción no válida. Inténtelo de nuevo.")
    
    def ejecutar(self):
        print("Bienvenido a la Aplicación de Recetas")
        while True:
            self.vista.mostrar_menu_principal()

            opcion = input("Seleccione una opción (1/2/3/4/5): ")

            if opcion == "1":
                self.mostrar_recetas_disponibles()
            elif opcion == "2":
                self.mostrar_alimentos_en_nevera()
            elif opcion == "3":
                self.mostrar_recetas_en_recetario()
            elif opcion == "4":
                self.inspeccionar_receta()
            elif opcion == "5":
                print("¡Hasta luego!")
                break
            else:
                print("Opción no válida. Inténtelo de nuevo.")
