# archivo: Receta.py
# autor: Jesús López Rodríguez
# descripción: Este archivo contiene funciones para gestionar la clase Nevera

from app.Vista import Vista
from app.Modelo import Modelo
from app.Controlador import Controlador

def main():
    vista = Vista()
    modelo = Modelo()
    controlador = Controlador(vista, modelo)

    controlador.ejecutar()

if __name__ == "__main__":
    main()
