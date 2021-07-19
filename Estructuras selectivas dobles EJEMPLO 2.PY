#Isaias Rafael Sandoya Vargas 
#Software A1

#EJEMPLO 2
#Dado el sueldo de un empleado, encontrar el nuevo sueldo si obtiene un aumento del 10% si su sueldo es inferior a $600, en caso contrario no tendrá aumento.

print("Suerdo a Recibir")
sue=float(input("Ingrese Sueldo: "))
if sue>600:
    aum=sue*0.10
    sue=sue+aum
    print("Obtiene aumento",sue)
else:
    print("No obtiene aumento",sue)

print("El sueldo es: ",sue)