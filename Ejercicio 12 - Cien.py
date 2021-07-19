class Cien:
    def __init__(self):
        pass
    def SumaCien(self):
        i = 1
        suma = 0
        for i in range(100):
            suma = suma + i * i
            i += 1
        print("La suma de los cuadrados de los primeros 100 numeroses: {}".format(suma))
Cien = Cien()
Cien.SumaCien()