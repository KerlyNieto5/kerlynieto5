"""Escribe un programa que solicite una puntuación entre 0.0 y 1.0. Si la
puntuación está fuera de ese rango, muestra un mensaje de error"""

calificacion= (input('Ingrese puntuacion:'))
 
if calificacion < 0.0 or calificacion > 1.0:
    print('Fuera de rango!!. Debe ser entre 0.0 y 1.0')
else:
    if calificacion >= 0.9:
        print('Sobresaliente')
    elif calificacion >= 0.8 and calificacion < 0.9:
        print('Notable')
    elif calificacion >= 0.7 and calificacion < 0.8:
        print('Bien')
    elif calificacion >= 0.6 and calificacion < 0.7:
        print('Suficiente')
    else:
        print('Insuficiente')