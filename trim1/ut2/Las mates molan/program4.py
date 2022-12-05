import sys
from math import sqrt

r = float(input("Radio de entrada = "))

print ("Pulse 1 para calcular el diámetro de la circunferencia") 
print ("Pulse 2 para calcular el perímetro de la circunferencia")
print ("Pulse 3 para calcular el área del circulo")
print ("Pulse 4 para salir")

opcion = input("Elige una opcion: ")
d = 2*r
p = 2*3.1416*r
a = 3.1416*r**2
  
if opcion == "1":
    print ("El diámetro es = " +str(d))
elif opcion == "2":
    print ("El perímetro es = " +str(p))
elif opcion == "3":
    print("El área es = " +str(a))
elif opcion == "4":
    salir = True
else:
    print ("Introduce un numero entre 1 y 4")
 
print ("Fin")