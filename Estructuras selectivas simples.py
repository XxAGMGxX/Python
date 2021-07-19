#Isaias Rafael Sandoya Vargas 
#Software A1

#EJEMPLO 1
#Construir un algoritmo tal, que dado como dato la calificación de un alumno en un examen, escriba "Aprobado" en caso que esa calificación fuese mayor que 7.

print("Verificar si el alumno esta aprobado")
cal=float(input("Ingrese la calificacion: "))
if cal>7:
    print("Aprobado",cal)
else:
    print("Reprobado",cal)