#	En una tienda se ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuánto deberá pagar finalmente por su comp
class descuento:
    totaldecompra=float(input("Ingrese el total de la compra:"))
    descuento= totaldecompra*0.15
    totalapagar= totaldecompra-descuento
    print("El total a pagar es: $",totalapagar)
    print("El descuento aplicado es de: $",descuento)
