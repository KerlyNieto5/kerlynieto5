class Pedido:
    def __init__(self,Id_de_usuario,Titulo_del_material,Codigo_del_material,reservar_fecha, Entregar_fecha, Modificar_fecha):
        self.__Id_de_usuario=Id_de_usuario
        self.__Titulo_del_material=Titulo_del_material
        self.__Codigo_del_material=Codigo_del_material
        self.__reservar_fecha=reservar_fecha
        self.__Entregar_fecha=Entregar_fecha
        self.__Modificar_fecha=Modificar_fecha
    def getTitulo(self):
        return self.__Id_de_usuario
        return self.__Titulo_del_material
        return self.__Codigo_del_material
        return self.__reservar_fecha
        return self.__Entregar_fecha
        return self.__Modificar_fecha

