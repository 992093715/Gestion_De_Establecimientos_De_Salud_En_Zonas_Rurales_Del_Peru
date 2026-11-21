"""
El hashlib es una librería de Python que nos permite hashear datos de manera segura.
En este caso, se utiliza para proteger el DNI de los pacientes, cumpliendo con la
Ley N.º 29733 de protección de datos personales.

Hace que el número de DNI de un paciente se transforme en un código seguro de letras
y números, de manera que no se pueda identificar directamente a la persona a la que pertenece el DNI.
"""

import hashlib

# Importamos la clase Paciente del proyecto GestionEsSalud
from src.modelos.paciente import Paciente

"""
1. Aquí ponemos a prueba la viabilidad técnica de nuestro código,
creando una lista de pacientes y aplicando programación funcional.
"""

if __name__ == "__main__":

    """
    Creamos una lista (colección) con tres pacientes simulados (no son personas reales).
    """

    pacientes_registro = [
        Paciente("P001", "Ana Torres", "45678912"),
        Paciente("P002", "Carlos Pérez", "12345678"),
        Paciente("P003", "María Gómez", "87654321")
    ]

    """
    2. Aplicamos Programación Funcional (filter y lambda).

    lambda es una función anónima que ayuda a filtrar resultados sin alterar
    los datos originales, y filter verifica cuáles cumplen con el criterio.

    Buscamos de forma rápida dentro de la lista sin modificar los registros.
    """

    criterio_busqueda = "Ana"

    resultado_filtrado = list(
        filter(
            lambda p: criterio_busqueda.lower() in p.get_nombre().lower(),
            pacientes_registro
        )
    )

    """
    3. Imprimimos los resultados en la consola.

    len (que en inglés es length) sirve para contar la cantidad total de
    elementos que tiene una lista, un texto o cualquier colección de datos.
    """

    print("--- PRUEBA DE VIABILIDAD TÉCNICA EXITOSA ---")
    print(f"Total de pacientes revisados: {len(pacientes_registro)}")
    print(f"Coincidencias encontradas: {len(resultado_filtrado)}")

    for p in resultado_filtrado:
        print(
            f"Paciente: {p.get_nombre()} | "
            f"DNI Protegido: {p.get_dni_hash()[:12]}..."
        )

    print("\n¡Todas las comprobaciones fueron exitosas!")