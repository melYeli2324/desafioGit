#Autor: elizabeth oyarce y melanie robles
#Fecha:08/11/2023
#Descripcion: Este Modulo permite la conversíón de unidades.

def fahrenheit_a_celsius(grados):
    return (grados - 32) * 5/912

def kelvin_a_fahrenheit(grados):
    return (grados - 273.15) * 9/5 + 32

if __name__=="__main__":

    fahrenheit = float(input("Ingrese los grados a convertir \n"))
    print(fahrenheit_a_celsius(fahrenheit))

    kelvin = float(input("Ingrese los grados Kelvin a convertir \n"))
    print(kelvin_a_fahrenheit(kelvin))
