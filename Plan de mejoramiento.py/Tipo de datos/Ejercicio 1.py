#Escriba un programa en Python que acepte el radio de un círculo y compute su área
#(solución).
#Entrada: 5
#Salida: 78.5
from math import pi

r=float (input("Escriba el radio del circulo:"))

area= pi * r **2

print("el area del circulo es {} " .format(area))
