from Kerly import nombre_aprendiz, edad_aprendiz, usuario, indice_masa_corporal, iva

nom=(input('ingrese nombre completo: '))
nombre_aprendiz(nom)

año_actual=2023
año_nacimiento=(int(input("ingrese su año de nacimiento: ")))
edad_aprendiz(año_actual,año_nacimiento)

identificacion=input("ingrese el numero de su documento de identidad: ")
usuario(identificacion)

peso=float(input("ingrese su peso: "))
altura=float(input("ingrese su altura: "))
indice_masa_corporal(peso,altura)

precio=(int(input("ingrese el valor de su compra: ")))
iva(precio)