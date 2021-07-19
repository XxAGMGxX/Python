#Isaias Rafael Sandoya Vargas 
#Software A1

#EJEMPLO 1
#Calcular el factorial de N números enteros leídos de teclado.
#El problema consistirá en realizar una estructura de N iteraciones aplicando el factorial de un número.
#El pseudocódigo es el siguiente

class tarea:
    def __init__(self):
        pass
    def factorial(self):
        n = int(input("ingrese cantidad de numero: "))
        for i in range(n):
            numero = int(input("ingrese numero: "))
            fact=1
            for num in range(numero,0,-1):
                fact=fact*num
            print("factorial del numero:{} es: {}".format(numero,fact))
                

tarea = tarea()
tarea.factorial()
            