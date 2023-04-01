from carga import * #Importamos modulo cargar 
from Conductor import *#Importamos el  modulo conductor 
# c1=Conductor('Luis',12345)
# carga1=Carga('aaa-123',c1,5,2)
# print(carga1)
nomConductor=input('Ingrese nombre del conductor')#le pedimos al usuario que ingrese un nombre 
docConductor=int(input('Ingrese documento del conductor'))#le pedimos al usuario que ingrese el numero de documento del cnductor.
placa=input('ingrese placa')#le pedimos al usuario que ingrese dl numero de placa
capacidad=input('ingrese capacidad en toneladas')#le pedimos  al usuario que digite una cantidad de toneladas
ejes=input('ingrese numero de ejes')#Le indicamos al usuario que ingrese el numero de ejes
c1=Conductor(nomConductor,docConductor)#llamamos el modulo conductor y le agregamos las variables nomConductor y docConductor
obCarga=Carga(placa,c1,capacidad,ejes)#llamamos el modulo cargar y le agregamos las variables restantes las cuales tienen informacion del usuario
cadConductor=obCarga.getConductor().getNombre()+','+str(obCarga.getConductor().getDocumento())#l agregamos a la variable conductor un objecto para la carga , con get llamamos los atributos
# y los conactenamos con una cadena de texto y adentro los mismos valores


cadCarga=obCarga.getPlaca()+','+cadConductor+','+str(obCarga.getCapacidad())+','+str(obCarga.getEjes())

with open('poo-archivos/listado.txt','a') as flujo:#indicamos que con open habra la siguiente direccion y con as le indicamos que la habra como flujo
    flujo.write(cadCarga+'\n')# ponemos en flujo el metodo write que indica para escribir y con \n le damos un salto de linea
