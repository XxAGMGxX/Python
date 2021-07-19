#Isaias Rafael Sandoya Vargas 
#Software A1

#EJEMPLO 2
#Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas. El vendedor desea saber cuánto dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y sus comisiones.

#DEFINICIÓN DEL PROBLEMA:
#Obtener la cantidad de dinero que recibirá un vendedor por concepto de comisiones por tres ventas realizadas en el mes, y el total que recibirá en el mes por sueldo y comisión. Se sabe que el vendedor recibe un sueldo base y un 10% extra por comisiones de todas sus ventas.

#ANÁLISIS DEL PROBLEMA:
#Para obtener la comisión y la cantidad que recibirá el vendedor, se necesita realizar lo siguiente:
#Para obtener la cantidad total de ventas hay que conocer la cantidad de cada una de sus ventas en                                            el mes y sumarlas. Posteriormente, sobre el total de las ventas se debe aplicar el 10% para obtener la comisión. Por último, para obtener el total de dinero que debe recibir el vendedor hay que sumarle al sueldo base la comisión.

class ventas():
    def calcularcomisiones(self):
        sb,venta1,venta2,venta3,total_ventas=0,0,0,0,0
        comision,sueldo_total=0,0
        sb=float(input("Ingrese el sueldo base: "))
        venta1=float(input("Ingrese el valor de la venta 1: "))
        venta2=float(input("Ingrese el valor de la venta 2: "))
        venta3=float(input("Ingrese el valor de la venta 3: "))
        total_ventas=venta1+venta2+venta3
        comision=total_ventas*0.10
        sueldo_total=sb+comision
        print("Sueldo base es: ",sb)
        print("Total de ventas: ",total_ventas)
        print("Comision de las ventas: ",comision)
        print("El sueldo total es: ",sueldo_total)
ventas=ventas()
ventas.calcularcomisiones()