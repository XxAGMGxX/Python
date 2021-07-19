#Encontrar la superficie para un radio cualquiera.
class Superficie():
    pi= 3.141516
    Radio= int(input("El radio del circulo es de:"))
    cal= Radio*Radio
    Superficie= cal*pi
    print("La superficie del circulo es :",Superficie)

    input("Enter para salir")
