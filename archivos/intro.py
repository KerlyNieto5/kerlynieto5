flujo=open('archivos/inicio.txt','a+') 
#r+hace update y lee
#a+ hace update 
#datos=flujo.read()
#print(datos)
flujo.write('\nCuando estudian con juicio')
datos=flujo.read()
print(datos)
