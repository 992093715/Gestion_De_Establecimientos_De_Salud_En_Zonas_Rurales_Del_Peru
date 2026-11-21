from src.repositorios.base_repositorio import BaseRepositorio
from src.modelos.paciente import Paciente

class PacienteRepositorio(BaseRepositorio):

    def registrar(self, paciente):
        consulta = """
            INSERT INTO pacientes (id_paciente, nombre, dni_hash)
            VALUES (?, ?, ?)
        """

        self.conexion.execute(
            consulta,
            (
                paciente.get_id_paciente(),
                paciente.get_nombre(),
                paciente.get_dni_hash()
            )
        )

        self.conexion.commit()

    def obtener_todos(self):
        consulta = "SELECT * FROM pacientes ORDER BY nombre"
        filas = self.conexion.execute(consulta).fetchall()

        return [
            Paciente(
                fila["id_paciente"],
                fila["nombre"],
                dni_hash=fila["dni_hash"]
            )
            for fila in filas
        ]

    def buscar_por_nombre(self, criterio):
        consulta = """
            SELECT * FROM pacientes
            WHERE LOWER(nombre) LIKE LOWER(?)
            ORDER BY nombre
        """

        filas = self.conexion.execute(
            consulta, (f"%{criterio}%",)
        ).fetchall()

        return [
            Paciente(
                fila["id_paciente"],
                fila["nombre"],
                dni_hash=fila["dni_hash"]
            )
            for fila in filas
        ]

    def buscar_por_id(self, id_paciente):
        consulta = """
            SELECT * FROM pacientes
            WHERE id_paciente = ?
        """

        fila = self.conexion.execute(
            consulta, (id_paciente,)
        ).fetchone()

        if fila is None:
            return None

        return Paciente(
            fila["id_paciente"],
            fila["nombre"],
            dni_hash=fila["dni_hash"]
        )