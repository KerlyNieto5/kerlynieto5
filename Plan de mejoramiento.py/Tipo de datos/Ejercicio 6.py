"""Escriba un programa en Python que acepte un entero n y compute el valor de n + nn + nnn .
Entrada: 5
Salida: 615 (5 + 55 + 555)"""

num_entero = 5

num_entero = str(num_entero)
resultado = int(num_entero) + int(num_entero * 2) + int(num_entero * 3)
print("el resultado es:",resultado)
