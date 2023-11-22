def segundos_a_minutos(sec):
    return sec / 60

def minutos_a_segundos(min):
    return min * 60

if __name__=="__main__":

    segundos = float(input("Ingrese los sec a convertir \n"))
    print(segundos_a_minutos(segundos))

    minutos = float(input("Ingrese los min a convertir \n"))
    print(minutos_a_segundos(minutos))