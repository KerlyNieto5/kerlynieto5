"""Escriba un programa en Python que lea por teclado dos números enteros y muestre por
pantalla el resultado de realizar las operaciones básicas entre ellos.
Valores de entrada 7 y 4.
Salida esperada:
7+4=11
7-4=3
7*4=28
7/4=1.75"""
numero1 = int(input("ingresa elprimer numero: "))
numero2 = int(input("ingresa el segundo numero: "))

suma = numero1 + numero2
print(numero1, numero2, sep='+', end='=')
print(suma)

resta = numero1 - numero2
print(numero1, numero2, sep='-', end='=')
print(resta)

multiplicacion = numero1 * numero2
print(numero1, numero2, sep='*', end='=')
print(multiplicacion)

division = numero1 / numero2
print(numero1, numero2, sep='/', end='=')
print(division)
