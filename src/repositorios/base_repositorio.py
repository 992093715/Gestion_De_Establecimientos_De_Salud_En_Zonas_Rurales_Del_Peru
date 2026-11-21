from src.utils.database import obtener_conexion

class BaseRepositorio:
    def __init__(self):
        self.conexion = obtener_conexion()