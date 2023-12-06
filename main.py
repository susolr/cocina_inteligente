# archivo: Receta.py
# autor: Jesús López Rodríguez
# descripción: Este archivo contiene funciones para gestionar la clase Nevera

from app.Alimento import Alimento
from app.Receta import Receta
from app.Nevera import Nevera
from app.Recetario import Recetario

def main():
    print("Bienvenido a la Aplicación de Recetas")

    # Crear alimentos
    manzana = Alimento("Manzana")
    salmon = Alimento("Salmon")
    langostino = Alimento("Langostino")

    # Crear recetas
    salmon_compota = Receta("Salmon con compota de manzana", [manzana,salmon], "Hacer el salmon al horno y triturar la manzana. Agregar en mitad de la coccion")
    langostinos_plancha = Receta("Langostinos plancha", [langostino], "Colocar sobre aceite caliente")

    # Crear recetario
    recetario = Recetario()
    recetario.add_receta(salmon_compota)
    recetario.add_receta(langostinos_plancha)

    # Crear nevera
    mi_nevera = Nevera()
    mi_nevera.add_alimento(manzana, cantidad=2)
    mi_nevera.add_alimento(langostino, cantidad=3)

    while True:
        print("\nMenú:")
        print("1. Ver recetas disponibles")
        print("2. Ver alimentos en la nevera")
        print("3. Salir")

        opcion = input("Seleccione una opción (1/2/3): ")

        if opcion == "1":
            mostrar_recetas_disponibles()
        elif opcion == "2":
            mostrar_alimentos_en_nevera()
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

def mostrar_recetas_disponibles():
    recetario = Recetario()
    recetas_disponibles = recetario.buscar_recetas_disponibles()
    
    if recetas_disponibles:
        print("\nRecetas disponibles:")
        for receta_disponible in recetas_disponibles:
            print(f"- {receta_disponible.nombre}")
    else:
        print("\nNo hay recetas disponibles con los ingredientes en la nevera.")

def mostrar_alimentos_en_nevera():
    nevera = Nevera()
    alimentos_en_nevera = nevera.alimentos
    
    if alimentos_en_nevera:
        print("\nAlimentos en la nevera:")
        for alimento, cantidad in alimentos_en_nevera.items():
            print(f"- {alimento.nombre}: {cantidad}")
    else:
        print("\nLa nevera está vacía.")

if __name__ == "__main__":
    main()