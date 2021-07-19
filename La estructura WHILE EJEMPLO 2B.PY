#Isaias Rafael Sandoya Vargas 
#Software A1

#BUCLE CONTROLADO POR CONDICIÓN
#EJEMPLO 2
#Diseñe un pseudocódigo para calcular la suma y producto de N números enteros, utilizando un bucle controlado por centinela.

class Numero:
    def Calcular(self):
        prod=1
        suma=0
        num=int(input("Ingresa un número entero que no sea negativo: "))
        while num != -1 :
            num=int(input("Ingresa un número: "))
            suma=suma+num
            prod=prod*num
        print("Total de la suma es: ",suma)
        print("Total del producto es: ",prod)
        print("\n")
        print("**FIN DE LA EJECUCIÓN**") 
        
numero= Numero()
numero.Calcular()