class Rol:

    def __init__(self, id_rol, nombre, permisos=None):
        self.__id_rol = id_rol
        self.__nombre = nombre
        self.__permisos = frozenset(permisos or [])

    def get_id_rol(self):
        return self.__id_rol

    def get_nombre(self):
        return self.__nombre

    def get_permisos(self):
        return self.__permisos

    def tiene_permiso(self, permiso):
        return permiso in self.__permisos