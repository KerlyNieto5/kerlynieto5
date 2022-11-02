
num=0
maximo=0
cont=0

while num >=0:
    num =int(input("Ingrese el numero"))
    if num>=0:
        cont +=1
    if num>maximo:
        maximo=num
if cont >0:
        print("De los", cont,"numeros positivos que usted digito, el numero mas grande es:", maximo)
    
else: 
    print("no digito un numero positivo, fin del programa")


