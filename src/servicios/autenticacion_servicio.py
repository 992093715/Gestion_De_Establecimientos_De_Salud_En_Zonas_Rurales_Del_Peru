import uuid

from src.modelos.usuario import Usuario
from src.repositorios.usuario_repositorio import UsuarioRepositorio
from src.repositorios.rol_repositorio import RolRepositorio
from src.utils.seguridad import (
    generar_hash_contrasena,
    verificar_contrasena
)

class AutenticacionServicio:

    def __init__(self):
        self.usuarios = UsuarioRepositorio()
        self.roles = RolRepositorio()
        self.roles.inicializar_roles()

    def crear_usuario(self, nombre, contrasena, nombre_rol):
        if not nombre or not nombre.strip():
            raise ValueError("El nombre de usuario es obligatorio.")

        if not contrasena or len(contrasena) < 8:
            raise ValueError(
                "La contraseña debe tener al menos 8 caracteres."
            )

        if self.usuarios.buscar_por_nombre(nombre.strip()):
            raise ValueError("El nombre de usuario ya existe.")

        rol = self.roles.buscar_por_nombre(nombre_rol)

        if rol is None:
            raise ValueError("El rol indicado no existe.")

        usuario = Usuario(
            str(uuid.uuid4()),
            nombre.strip(),
            generar_hash_contrasena(contrasena),
            rol
        )

        self.usuarios.registrar(usuario)
        return usuario

    def autenticar(self, nombre, contrasena):
        if not nombre or not contrasena:
            return None

        fila = self.usuarios.buscar_por_nombre(nombre.strip())

        if fila is None:
            return None

        if not fila["activo"]:
            return None

        if not verificar_contrasena(
            contrasena,
            fila["contraseña_hash"]
        ):
            return None

        rol = self.roles.buscar_por_id(fila["id_rol"])

        if rol is None:
            return None

        return Usuario(
            fila["id_usuario"],
            fila["nombre"],
            fila["contraseña_hash"],
            rol,
            bool(fila["activo"])
        )

    def desactivar_usuario(self, id_usuario, administrador):
        if not administrador.tiene_permiso("gestionar_usuarios"):
            raise PermissionError(
                "No tiene permiso para gestionar usuarios."
            )

        if not self.usuarios.actualizar_estado(id_usuario, False):
            raise ValueError("El usuario no existe.")