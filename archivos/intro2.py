with open('archivos/inicio.txt','rt') as flujo:
    datos=flujo.read()
    print(datos) # es importante cerrar los flujos.
    # con esta sintasis se puede oviar los cierres.
    # con with open('archivos/inicio.txt','rt') as flujo: