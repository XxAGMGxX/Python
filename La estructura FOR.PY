#Isaias Rafael Sandoya Vargas 
#Software A1

#EJEMPLO 1
#Calcular la suma de los cuadrados de los primeros 100 enteros y escribir el resultado.

class numero():

    def numcuadrados(self):
        num,sum=0,0
        num=int(input("ingrese el limite de cuadrado:"))
        for i in range(1,num+1):
            print(i,"^2")
            print("+")
            sum = sum+(i**2)
            print("La suma de los cuadrados es: ",sum)       
numero=numero()
numero.numcuadrados()