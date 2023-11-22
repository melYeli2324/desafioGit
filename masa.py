#Autor: elizabeth oyarce y melanie robles
#Fecha:08/11/2023
#Descripcion: Este Modulo permite la conversíón de unidades.

def kilogramos_a_gramo(kg):
    return kg * 1000

def gramos_a_kilogramos(g):
    return  g / 1000

if __name__=="__main__":

    kilogramos = float(input("Ingrese los kg a convertir \n"))
    print(kilogramos_a_gramo(kilogramos))

    gramos = float(input("Ingrese los g a convertir \n"))
    print(gramos_a_kilogramos(gramos))