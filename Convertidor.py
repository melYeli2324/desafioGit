#Autor: elizabeth oyarce y melanie robles
#Fecha:08/11/2023
#Descripcion: Este Modulo es el menu de conversion de unidades

import Temperatura as temp
import masa
import tiempo

def main():
    while True:
        opcion = input("Bienvenido, que unidades desea convertir?: \n" 
                "0. Salir del programa\n"
                "1. Fahrenheit a celsius\n"
                "2. Kilogramos a gramos\n"
                "3. Segundos a minutos\n")
        try:
            opcion = int(opcion)
            if opcion == 0:
                print("Saliendo del programa. ¡Hasta luego!")
                break
            elif opcion == 1:
                fahrenheit= float(input("Ingrese los grados a convertir \n"))
                print(temp.fahrenheit_a_celsius(fahrenheit))
            elif opcion == 2:
                kilogramos = float(input("Ingrese los kg a convertir \n"))
                print(masa.kilogramos_a_gramo(kilogramos))
            elif opcion == 3:
                segundos = float(input("Ingrese los sec a convertir \n"))
                print(tiempo.segundos_a_minutos(segundos))
        except ValueError:
            print("Solo puede ingresar valores numéricos.")

main()