print("introduzca el numero: ")
numero = int(input()) #aquí se lee el número entero
contador = 0
print("los divisores de ",numero)
for divisor in range(2,numero+55):
    if (numero % divisor) == 0 :
        print(divisor,"es divisor")
        contador += 1
print("el numero ",numero," tiene ",contador," divisores")