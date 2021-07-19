#Isaias Rafael Sandoya Vargas 
#Software A1

#BUCLE CONTROLADO POR BANDERAS O INTERRUPTORES
#EJEMPLO 1
#Determinar si un número entero proporcionado por el usuario es primo. Un número primo es un entero que no tiene más divisores que él mismo y la unidad. Elaborar Pseudocódigo:

class Indentificar:
    def Numero(self):
        primo= 0
        divisor=2
        num=int(input("Ingresa un número entero: "))
        while divisor < num and primo ==0 :
            Res= num%divisor
            print(Res)
            if Res == 0:
                primo+=1
            divisor+=1
        if primo ==0:
            print("El número",num,"es primo")
        else:
            print("El número",num,"no es primo")
        print("\n")
        print("**FIN DE LA EJECUCIÓN**") 
        
identificar= Indentificar()
identificar.Numero()