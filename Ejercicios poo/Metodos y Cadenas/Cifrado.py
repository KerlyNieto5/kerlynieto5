def cifrado():
    cadena = input("Ingresa el mensaje: ")
    lista=[]
    cad = ''
    for i in cadena:
        lista.append(ord(i))
        i= i.upper()
        b = ord(i) + 2
        if b > ord('Z'):
            b = ord('A')
        cad += chr(b)
    print('el mensaje en letras es: ',cad, 'el mensaje e numeros es: ',lista)
cifrado()