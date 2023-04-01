def funcion( ):
    cadena="la vida es mas bonita si sonrries mas"
    L=[]
    tamano=(len(cadena))

    for i in cadena:
        if i not in L:
            L.append(i)
    tamano2=len(L)
    print('cadena', L)
    print("la cadena tiene",tamano,"letras")
    print("la cadena sin repetir letras tiene",tamano2,"letras")
    
    
funcion()