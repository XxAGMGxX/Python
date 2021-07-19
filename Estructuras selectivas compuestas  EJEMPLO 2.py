#Isaias Rafael Sandoya Vargas 
#Software A1

#EJEMPLO 2
#Leer tres números enteros diferentes entre sí y determinar el número mayor de los tres.

numeros = []
for i in range(3):
    numero = float(input("Introduce el número {}: ".format(i + 1)))
    numeros.append(numero)
mayor = numeros[0]
for numero in numeros:
    if numero > mayor:
         mayor = numero
print("Mayor:", mayor)