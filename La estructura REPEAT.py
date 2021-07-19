#Isaias Rafael Sandoya Vargas 
#Software A1

#BUCLE REPEAT CONTROLADO POR BANDERAS.
#EJEMPLO 1
#Aplicar los pasos de la metodología para la solución de un problema para leer un número entero N y calcular el resultado de la siguiente serie:
#1 – 1/2+ 1/3 – 1/4 +.... +/- 1/N. Resolveremos el problema utilizando bucle Repeat controlado por contador y usando banderas.

class metodología:
    def __init__ (self):
        pass
    def Variables(self):
        print("_______________________________________") 
        l=1
        n=int(input("ingrese un numero para la serie: "))
        print("_______________________________________") 
        s=5
        ser=0
        for a in range(l,n+1):
            s=s+5
            ser=ser+s
        print("la suma de la serie es:", ser)

                  
        print("_______________________________________")
        input("enter para salir") 
        
resultado = metodología()
resultado.Variables()