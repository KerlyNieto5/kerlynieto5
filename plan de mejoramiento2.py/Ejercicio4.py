# escribe un programa que muestre los numeros impares de forma ascendente entre  0 al 10.
def funcion(num):
    while num>0:
        if num%2!=0:
            print(num)
        num-=1
funcion(10)
