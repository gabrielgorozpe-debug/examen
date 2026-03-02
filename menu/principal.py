
from ejercicios.ejercicio1 import ejercicio_1
from ejercicios.ejercicio2 import ejercicio_2
from ejercicios.ejercicio3 import ejercicio_3
#referenciar la clase
from POO.clases.ejer1poo import Ejercicio1
from POO.clases.ejer2poo import Ejercicio2
from POO.clases.ejer3poo import Ejercicio3
#carpeta carpeta carpeta       clase
   

def menu_principal():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Ejercicio #1: División Exacta")
        print("2. Ejercicio #2: Ecuación de Primer Grado")
        print("3. Ejercicio #3: Conversión de Distancia")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        
        match(opcion):
            case 1:
                print("\n--- Ejercicio #1 ---")         
                e1 =  ejercicio_1()
                e1.leerDatos()
                e1.calcularAprox()
                e1.mostrarResultado()

            case 2:
                print("\n--- Ejercicio #2 ---")
                e2 =  ejercicio_2()
                e2.leerDatos()
                e2.calcularAprox()
                e2.mostrarResultado()

            case 3:
                print("\n--- Ejercicio #3 ---")
                e3 =  ejercicio_3()
                e3.leerDatos()
                e3.calcularAprox()
                e3.mostrarResultado()


            case 4:
                print("Saliendo del programa.")
                break
            case _:
                print("Opción no válida. Intente de nuevo.")