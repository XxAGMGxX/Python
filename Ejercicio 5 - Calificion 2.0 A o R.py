# 5. Dado como dato la calificación de un alumno en un examen, escriba “aprobado”
# si su calificación es mayor o igual que 7 y “Reprobado” en caso contrario.
class Calificacion():
    Calif=float(input("Ingrese su calificación:"))
    if Calif >= 7:
        print("¡Felicidades, ud ha sido A P R O B A D O!")
    else:
        print("R E P R O B A D O")
