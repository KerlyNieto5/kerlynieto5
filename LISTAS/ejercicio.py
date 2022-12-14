#supermercado
num=0
maximo=0
cont=0

supermercado = {}

while True:
    producto = input("Ingresa el nombre del producto: ")
    if producto == '':
        break
    
    score = int(input("Ingresa el presio del producto (0-10): "))
    if score not in range(0, 11):
	    break
    
if producto in supermercado:
        supermercado[producto] += (score,)
else:
        supermercado[producto] = (score,)
        
for producto in sorted(supermercado.keys()):
    adding = 0
    counter = 0
    for score in supermercado[producto]:
        adding += score
        counter += 1
    print(producto, ":", adding / counter)

print('el promedio es: ' (adding + counter) /3)


"""while score>=0:
    score =int(input("Ingrese un número      "))
    if score>=0:
        cont +=1
    if score>maximo:
        maximo=score
if cont>0:
    print("De los",cont,"números positivos que usted digito, el número mas grande es:",maximo)
else:
    print("No digito un número positivo, fin del programa")"""


