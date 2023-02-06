def funcion (t1,t2):
    if (len(t1)> len(t2)):
        return "t1 es mayor"
    elif(len(t1)<len(t2)):
        return "t2 es mayor"
    else: 
        return "son iguales"

tupla1=(1,2,3,4,5)
tupla2=(1000,2000,3000)
print(funcion(tupla1,tupla2))
