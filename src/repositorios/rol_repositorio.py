from src.repositorios.base_repositorio import BaseRepositorio
from src.modelos.rol import Rol

class RolRepositorio(BaseRepositorio):

    ROLES_PREDETERMINADOS = {
        "ADMIN": {
            "nombre": "Administrador",
            "permisos": [
                "registrar_paciente",
                "consultar_paciente",
                "editar_paciente",
                "consultar_historial",
                "registrar_diagnostico",
                "gestionar_usuarios",
                "gestionar_citas"
            ]
        },
        "MEDICO": {
            "nombre": "Medico",
            "permisos": [
                "consultar_paciente",
                "consultar_historial",
                "registrar_diagnostico",
                "gestionar_citas"
            ]
        },
        "RECEPCIONISTA": {
            "nombre": "Recepcionista",
            "permisos": [
                "registrar_paciente",
                "consultar_paciente",
                "gestionar_citas"
            ]
        }
    }

    def inicializar_roles(self):
        for id_rol, datos in self.ROLES_PREDETERMINADOS.items():

            self.conexion.execute(
                """
                INSERT OR IGNORE INTO roles (id_rol, nombre)
                VALUES (?, ?)
                """,
                (id_rol, datos["nombre"])
            )

            for nombre_permiso in datos["permisos"]:

                self.conexion.execute(
                    """
                    INSERT OR IGNORE INTO permisos
                    (id_permiso, nombre)
                    VALUES (?, ?)
                    """,
                    (nombre_permiso, nombre_permiso)
                )

                self.conexion.execute(
                    """
                    INSERT OR IGNORE INTO rol_permisos
                    (id_rol, id_permiso)
                    VALUES (?, ?)
                    """,
                    (id_rol, nombre_permiso)
                )

        self.conexion.commit()

    def buscar_por_id(self, id_rol):
        fila = self.conexion.execute(
            """
            SELECT id_rol, nombre
            FROM roles
            WHERE id_rol = ?
            """,
            (id_rol,)
        ).fetchone()

        if fila is None:
            return None

        permisos = self.conexion.execute(
            """
            SELECT p.nombre
            FROM permisos p
            JOIN rol_permisos rp
                ON p.id_permiso = rp.id_permiso
            WHERE rp.id_rol = ?
            """,
            (id_rol,)
        ).fetchall()

        return Rol(
            fila["id_rol"],
            fila["nombre"],
            [permiso["nombre"] for permiso in permisos]
        )

    def buscar_por_nombre(self, nombre):
        fila = self.conexion.execute(
            """
            SELECT id_rol
            FROM roles
            WHERE LOWER(nombre) = LOWER(?)
            """,
            (nombre,)
        ).fetchone()

        if fila is None:
            return None

        return self.buscar_por_id(fila["id_rol"])