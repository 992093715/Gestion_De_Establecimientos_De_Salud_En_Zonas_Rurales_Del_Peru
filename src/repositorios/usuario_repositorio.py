from src.repositorios.base_repositorio import BaseRepositorio
from src.modelos.usuario import Usuario

class UsuarioRepositorio(BaseRepositorio):

    def registrar(self, usuario):
        self.conexion.execute(
            """
            INSERT INTO usuarios
            (id_usuario, nombre, contraseña_hash, id_rol, activo)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                usuario.get_id_usuario(),
                usuario.get_nombre(),
                usuario._obtener_contraseña_hash(),
                usuario.get_rol().get_id_rol(),
                int(usuario.esta_activo())
            )
        )

        self.conexion.commit()

    def buscar_por_nombre(self, nombre):
        fila = self.conexion.execute(
            """
            SELECT *
            FROM usuarios
            WHERE LOWER(nombre) = LOWER(?)
            """,
            (nombre,)
        ).fetchone()

        if fila is None:
            return None

        return fila

    def actualizar_estado(self, id_usuario, activo):
        cursor = self.conexion.execute(
            """
            UPDATE usuarios
            SET activo = ?
            WHERE id_usuario = ?
            """,
            (int(activo), id_usuario)
        )

        self.conexion.commit()
        return cursor.rowcount > 0