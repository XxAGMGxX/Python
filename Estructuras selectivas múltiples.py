#Isaias Rafael Sandoya Vargas 
#Software A1

#EJEMPLO 1
#Diseñar un algoritmo tal que dados como datos dos variables de tipo entero, obtenga el resultado de la siguiente función:

NUM= int(input("Ingrese primer variable: "))
V= int(input("Ingrese segunda Variable: "))
print("_____________")
if NUM== 1:
    Resp=100*V
elif NUM==2:
    Resp=pow(100,V)
elif NUM==3:
    Resp=100/V
else:
    Resp=0
                
print("Su Resultado es:",Resp)