# 9. Diseñar un algoritmo tal que dados como datos dos variables de tipo entero, obtenga el resultado de la siguiente función
class Resultado:
    def __init__(self):
        pass
    def calcuresult(self):
        va1 = int(input("Ingrese el primer valor: "))
        va2 = int(input("Ingrese el segundo valor: "))
        if va1 == 1:
            Resul = 100 * va2
        elif va1 == 2:
            Resul = 100 * va2
        elif va1 == 3:
            Resul = 100 / va2
        else:
            Resul = 0
        print("El resultado del número {} y el valor {} es de: {} ".format(va1, va2, Resul))

Resultado = Resultado()
Resultado.calcuresult()
