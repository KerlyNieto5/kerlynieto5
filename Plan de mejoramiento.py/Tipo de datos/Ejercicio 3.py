#Escriba un programa en Python que acepte el nombre y los apellidos de una persona
#y los imprima en orden inverso separados por una coma. Utilice f-strings para
#implementarlo.
#Entrada: nombre=Sergio; apellidos=Delgado Quintero
#Salida: Delgado Quintero, Sergio

nombre=input("escribe el nombre:")
apellido=input("escribe el apellido:")

print(f'{apellido}, {nombre}')
