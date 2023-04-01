class Aprendiz: #creamos  la clase padre llamada aprendiz
    def __init__(self,nombre): #creamos el constructor con su respectivo  parametro 
        self.__nombre=nombre #definimos el atributo
        self.__cursos=[] #creamos  la lista
    def agregarCurso(self,nombreCurso): #creamos el metodo agreagar curso  con sus respectivos parametros
        self.__cursos.append(nombreCurso) #le agregamos a la lista  
    def verCursos(self): #creamos el metodo con su parametro
        return self.__cursos #retornamos

class Curso: #creamos  la clase curso
    def __init__(self,nombreCurso): #creamos el constructor con su respectivo parametro 
        self.__nombreCurso=nombreCurso #definimos el atributo en este caso nombreCurso

    def getNombreCurso(self): #creamos un metodo
        return self.__nombreCurso #retornamos

ob=Aprendiz('Miguel') #creamos un objeto de la clase aprendiz
c1=Curso('Python Basico') #creamos un objeto de la clase curso
c2=Curso('Python Intermedio') #creamos un objeto de la clase curso
c3=Curso('Java Basico') # creamos un objeto de la clase curso

ob.agregarCurso(c1) #utilizamos el metodo de la clase aprendiz
ob.agregarCurso(c2) #utilizamos el metodo de la clase aprendiz
ob.agregarCurso(c3) #utilizamos el metodo de la clase aprendiz

for curso in ob.verCursos(): #recorreremos todos los elementos de la lista 
    print(curso.getNombreCurso()) #se imprimenlos elementos

del ob #eliminamos a la clase aprendiz
#print(ob)
print('.....',c1.getNombreCurso())