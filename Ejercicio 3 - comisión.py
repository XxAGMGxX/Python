# 3 Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas.
# El vendedor desea saber cuánto dinero obtendrá por concepto de comisiones por las tres
# ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo
class comisión:
    SalarioBase=float(input("El salario base es de:"))
    V1=float(input("Valor de la primera venta:"))
    V2=float(input("Valor de la segunda venta:"))
    V3=float(input("Valor de la tercera venta:"))
    TVentas= V1 + V2 + V3
    Comi= TVentas*0.1
    TRecibir= SalarioBase + Comi
    print("Su comision por concepto de ventas es de: $",Comi)
    print("Sueldo a recibir:$",TRecibir)
