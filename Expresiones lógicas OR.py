#Isaias Rafael Sandoya Vargas 
#Software A1

#EJEMPLO 1
#Un ejemplo usando el operador lógico OR sería:
#Una escuela aplica dos exámenes a sus aspirantes, por lo que cada uno de ellos obtiene dos calificaciones denotadas como C1 y C2. El aspirante que obtenga una calificación mayor que 90 en cualquiera de los exámenes es aceptado; en caso contrario es rechazado.

print("Calificaciones Denotadas Como C1 Y C2")
C1=float(input("Ingrese la calificacion de C1: "))
C2=float(input("Ingrese la calificacion de C2: "))

if C1>=90:
    print("Aprobado C1",C1)
else:
    print("Rechanado C1",C1)

if C2>=90:
    print("Aprobado C2",C2)
else:
    print("Rechazado C2",C2)

