#pedir numeros,imprimirlo con el opuesto (ejemplo 5 opuesto -5, -10 opuesto de 10)

numero_del_usuario = int(input('Ingresa un numero: '))
if numero_del_usuario < 0:
    numero_del_usuario *= -1    
print(f"El numero que ingreso es {numero_del_usuario}")

