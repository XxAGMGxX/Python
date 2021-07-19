# 11. Una escuela aplica dos exámenes a sus aspirantes, por lo que cada uno de ellos obtiene dos calificaciones denotadas como C1 y C2.
# El aspirante que obtenga una calificación mayor que 90 en cualquiera de los exámenes es aceptado; en caso contrario es rechazado.
class CalM:
    def __init__(self):
        pass
    def AoR(self):
        C1 = int(input("Ingrese la primera calificación: "))
        C2 = int(input("Ingrese la segunda calificación: "))
        if C1 >= 90 or C2 >= 80:
            print("La calificacion 1: {},la calificación 2:{} es ACEPTADO".format(C1, C2))
        else:
            print("La primera calificacion es de: {},la segunda calificación es de:{} es RECHAZADO".format(C1, C2))
CalM = CalM()
CalM.AoR()
