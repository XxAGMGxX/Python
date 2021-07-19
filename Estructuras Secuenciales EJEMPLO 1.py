#Isaias Rafael Sandoya Vargas 
#Software A1

#EJEMPLO 1
#En una tienda se ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuánto deberá pagar finalmente por su compra.

#DEFINICIÓN DEL PROBLEMA:
#Obtener la cantidad de dinero que tendrá que pagar el cliente, si la tienda ofrece un 15% de descuento sobre el total de la compra.

#ANÁLISIS DEL PROBLEMA:
#Para obtener el descuento es necesario conocer la cantidad total de la compra, y sobre ésta aplicar el 15%. Posteriormente, este descuento deberá ser sustraído de la cantidad total de la compra para así obtener la cantidad con descuento, que es la que el cliente pagará.

#15% de descuento sobre el total de la compra 
total= float(input("Ingrese el total de la compra: "))

descuento= total*.15
print("El total a pagar es: $", total-descuento)
print("El descuento aplicado es: $", descuento)