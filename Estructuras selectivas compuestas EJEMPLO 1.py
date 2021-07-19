#Isaias Rafael Sandoya Vargas 
#Software A1

#EJEMPLO 1
#Determinar la cantidad de dinero que recibirá un trabajador por concepto de las horas extras trabajadas en una empresa, sabiendo que cuando las horas de trabajo exceden de 40, el resto  se consideran horas extras y que éstas se pagan al doble de una hora normal cuando no exceden de 8;  si las horas extras exceden de 8 se pagan las primeras 8 al  doble de lo que se paga por una hora normal y el resto al triple.

class Tarea:
    def _init_(self):
        pass
    def CalcularJornada(self):
    
        ht,he,het=0,0,0
        ph,phe,pt,ph8=0,0,0,0
        print("_____________")
        ht=int(input("Ingrese Horas Trabajadas: "))
        ph=float(input("ingrese valor por horas: "))
        if ht > 40:
            he=ht-40
            if he > 8:
                het=he-8
                ph8=8*ph*2
                phe=het*ph*3
            else:
                ph8=he*ph*2
            pt=ph*40+phe+ph8
        else:
            pt= ht*ph
            print()
        print("_____________")    
        print("Sobretiempo <8 :{} Sobretiempo >8: {} El pago total de horas trabajadas es:$ {}".format(ph8,phe,pt))
        print("_____________")
        input("enter para salir")
tarea= Tarea()
tarea.CalcularJornada()