"""Ejercicio Dada una cadena de texto, indique el número de vocales que tiene.
Entrada: Supercalifragilisticoespialidoso
Salida: 15"""

vocales = 'aeiou'
input = 'Supercalifragilisticoespialidoso'

num_vocales = 0
for letter in input.lower():
    if letter in vocales:
        num_vocales += 1

print(num_vocales)