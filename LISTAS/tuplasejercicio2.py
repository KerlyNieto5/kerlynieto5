#comprension con tuplas de numeros aleatorios de 10 a 25 y saber cuales son primos

import random
tam=round(random.randint(10,25))
tup=tuple[round(random.random()*100) for i in range(10)]

print(tup)
for i in tup:
    cont=0
    for j in range(1,i):
        if i%j==0:
            cont+=1
    if cont ==1:

        print('primo')

