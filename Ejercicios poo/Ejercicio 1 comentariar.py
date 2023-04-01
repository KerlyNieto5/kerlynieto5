class Persona: #creamos una clase llamada persona 
    def __init__(self,nombre): #creamos una funcion con el constructor y su respectivo parametro self, tambien se pone otro parametro llamado nombre
        self.__nombre=nombre #se inicializa el parametro
        #print('Constructor Activado')        

    def getNombre(self): #creamos una funcion con el argumento self
        return self.__nombre #retorna el nombre de maria

    def setNombre(self,nombre): #creamos  una funcion con argumentos llamados self y nombre
        self.__nombre=nombre  #se inicializa el parametro
        
class Aprendiz(Persona): #creamos la clase aprendiz heredando de la clase persona 
    def __init__(self,nombre,ficha): #creamos una funcion con los parametros
        Persona.__init__(self,nombre) # se hereda de la clase persona
        self.__ficha=ficha #se inicializa el parametro
        

    def getFicha(self): #creamos la funcion get
        return self.__ficha #se retorna la ficha
    
class documento(Persona): #creamos la clase documento heredando de persona 
    def __init__(self,nombre,documento): #se crea la funcion con los parametros 
        self.__documento=documento #se inicializa el parametro
    def getdocumento(self): #se crea la funcion 
        return self.__documento #se retorna el documento

    def setdocumento(self,documento): #se crea la funcion 
        self.__documento=documento #se inicializa el parametro

class todo(Persona):
    def __init__(self,nombre,documento,ficha):
        self.__nombre=nombre
        self.__documento=documento
        self.__ficha=ficha
    def gettodo(self):
        print  (self.__nombre, self.__documento, self.__ficha)




app=todo("pedro" ,12345, 256)
print(app.gettodo())   