#14.	Diseñe un pseudocódigo para calcular la suma y producto de N números enteros, utilizando un bucle controlado por centinela.
class SP:
    def __init__(self):
        pass
    def EstCi(self):
        suma=0
        prodi=1
        num= int(input("Ingrese un número: "))
        while num!=-1:
            suma= suma+num
            prodi= prodi*num
            print("La suma es: {}".format(suma))
            print("El producto es: {}".format(prodi))
            num = int(input("Ingrese un número: "))


SP= SP()
SP.EstCi()