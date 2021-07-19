class ActS:
    def __init__(self):
        pass
    def calculoSueld(self):
        Sueld = float(input("Sueldo base:"))
        if Sueld <= 600:
            ASuel = Sueld + (Sueld * 0.1)
            print("Su nuevo sueldo es {}".format(ASuel))
        else:
            ASuel = Sueld
        print("Su sueldo se mantiene por: $ {}".format(ASuel))
ActS = ActS()
ActS.calculoSueld()
