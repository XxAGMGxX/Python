#Isaias Rafael Sandoya Vargas 
#Software A1

#EJEMPLO 1
#En ejemplos anteriores, diseñamos un pseudocódigo para encontrar la superficie de un círculo para un radio cualquiera.

class Tarea1:
    def __init__(self):
        pass
    def Calcular(self):
        pi=3.1416
        R =int(input("Ingrese el Radio del circulo : "))
        cal =R*R
        S=cal*pi
        print("La superficie del circulo es: ")
        print(S)

        input("enter para salir")

tarea= Tarea1()
tarea.Calcular()