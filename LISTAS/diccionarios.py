#clave-valor
dict={
    'gato' : 'cat',
    'perro': 'dog',
    'vaca' : 'cow',
    'caballo' : 'horse'


}
#PROMEDIO Y CUALES EL VALOR MAS ALTO Y MENOR 
print(dict)
#funcion sorted
print(dict)
print(sorted(dict))
print(sorted(dict.value))
print(sorted(dict.item))
sorted(dict.value)

#metodo get
print(dict.get('perro'))
print(dict['vaca'])

#metodo del
del dict['perro']
print(dict)

#metodo update
dict.update({'perro' : 'dog'})
print(dict)

#metodo popitem
dict.popitem()
print(dict)

#metodo keys
for i in dict.keys():
    print(i)
#metodo value
for i in dict.value():
    print(i)
#metodo que devuelve la clave y el valor item

for k,v in dict.item():
    print(k, '->',v) 

for item in dict.items():
    print(item) 
#para buscar algo muestra de funcion
def busqueda(diccionario, elemento):
    if elemento in diccionario.keys:
        print('si esta')
    else:
        print('no esta')
busqueda(dict, 'perro')


