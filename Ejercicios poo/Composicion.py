class Curso:  #creamos la clase curso
    def __init__(self,titulo): #creamos el  constructor con sus respectivos parametros
        self.__titulo=titulo #definimos el atributo titulo

    def getTitulo(self): #creamos el metodo 
        return self.__titulo #se retorna el titulo

class Aprendiz: #creamos la clase aprendiz

    def __init__(self,nombre): #creamos el constructor con sus parametros
        self.__nombre=nombre #definimos el atributo
        self.__cursos=[]#creamos la lista

    def agregarCurso(self,nombreCursito):#creamos el metodo con sus respectivos parametros
        cursito=Curso(nombreCursito)# le asignamos a cursito la clase curso
        self.__cursos.append(cursito) #le agregamos a la lista cursito

    def getCursos(self): #creamos el metodo con su parametro 
        return self.__cursos #retornamos la lista 

ap=Aprendiz('Sofia') #creamos un objeto de la clase aprendiz
ap.agregarCurso('Python Basico') #utilizamos el metodo de la clase curso
ap.agregarCurso('Python Intermedio') #utilizamos el metodo de la clase curso

for c in ap.getCursos(): #recorreremos todos los elementos de la lista 
    print(c.getTitulo()) #se imprimen todos los elementos 

del ap #eliminamos a la clase aprendiz
