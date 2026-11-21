"""
El hashlib es una librería de Python que nos permite hashear datos de manera segura.
En este caso, se utiliza para proteger el DNI de los pacientes, cumpliendo con la
Ley N.º 29733 de protección de datos personales.

Hace que el número de DNI de un paciente se transforme en un código seguro de letras
y números, de manera que no se pueda identificar a la persona a la que pertenece el DNI.
"""

import hashlib

"""
1. Creamos la clase Paciente, con atributos privados que son __nombre y __dni_hash (Aplicando POO)
"""

class Paciente:
    def __init__(self, id_paciente, nombre, dni):
        self.__id = id_paciente
        self.__nombre = nombre
        
        """
        2. Aquí usamos hashlib para hashear el DNI y cumplir con la Ley N.º 29733.
        .encode() pasa el texto a bytes y .hexdigest() lo transforma en el código
        seguro de letras y números.
        """

        self.__dni_hash = hashlib.sha256(dni.encode()).hexdigest() 

    """
    3. Getters (propiedades) para poder leer los atributos privados de forma segura
    Los getters son parte del encapsulamiento; son como una ventana blindada que solo
    te deja ver lo que hay dentro, no obstante, no te deja tocarlo ni modificarlo, y
    así se protege la información. Además, se usa doble guion bajo para indicar que
    es privado.
    """

    @property
    def nombre(self):
        return self.__nombre

    @property
    def dni_hash(self):
        return self.__dni_hash


"""
4. Aquí ponemos a prueba la viabilidad técnica de nuestro código, creando una lista
de pacientes y aplicando programación para filtrar resultados esperados.
"""

if __name__ == "__main__":
    
    """
    Creamos una lista (colección) con tres pacientes simulados (no son personas reales)
    """

    pacientes_registro = [
        Paciente("P001", "Ana Torres", "45678912"),
        Paciente("P002", "Carlos Pérez", "12345678"),
        Paciente("P003", "María Gómez", "87654321")
    ]

    """
    5. Aplicamos Programación Funcional (filter y lambda)
    lambda es una función anónima que ayuda a filtrar los datos de manera más rápida 
    sin alterar nada, y filter es como un filtro de seguridad que verifica si cumplen
    o no con las reglas.
    
    Buscamos de forma rápida dentro de la lista sin alterar los datos originales.
    """

    criterio_busqueda = "Ana"
    resultado_filtrado = list(filter(lambda p: criterio_busqueda.lower() in p.nombre.lower(), pacientes_registro))

    """
    6. Imprimimos los resultados en la consola
    len (que en inglés es length) sirve para contar la cantidad total de elementos
    que tiene una lista, un texto o cualquier colección de datos.
    """

    print("--- PRUEBA DE VIABILIDAD TÉCNICA EXITOSA ---")
    print(f"Total de pacientes revisados: {len(pacientes_registro)}")
    print(f"Coincidencias encontradas: {len(resultado_filtrado)}")
    
    for p in resultado_filtrado:

        """
        Mostramos el nombre y solo los primeros 12 caracteres del DNI hasheado
        """

        print(f"Paciente: {p.nombre} | DNI Protegido: {p.dni_hash[:12]}...")
