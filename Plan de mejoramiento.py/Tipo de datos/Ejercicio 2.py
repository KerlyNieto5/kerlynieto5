#Escriba un programa en Python que acepte el radio de una esfera y obtenga su volumen
#(solución).
#Entrada: 5
#Salida: 523.3333333333334

from math import pi
r= float(input("ingrese el radio de la esfera:"))

volumen=4/3 * pi * r ** 3

print("El volumen de la esfera es {}unidades cubicas".format(volumen))
