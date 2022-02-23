# –– coding: utf-8 ––
from utils.calc import potencia
nbr = int(input("Introduzca un numero? : "))
print("Tiene %d años" % nbr)
nbr_mas_uno = nbr + 1
print("Su numero es: %d " % nbr_mas_uno)
nbr_potencia = potencia(nbr)
print("Su numero es: %d " % nbr_potencia)
