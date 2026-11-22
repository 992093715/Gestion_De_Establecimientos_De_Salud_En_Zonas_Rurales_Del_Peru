from getpass import getpass

from src.servicios.autenticacion_servicio import AutenticacionServicio

def main():
    servicio = AutenticacionServicio()

    print("--- AUTENTICACIÓN DEL ADMINISTRADOR ---")

    nombre_admin = input("Usuario administrador: ").strip()
    contrasena_admin = getpass("Contraseña: ")

    administrador = servicio.autenticar(
        nombre_admin,
        contrasena_admin
    )

    if administrador is None:
        print("Credenciales incorrectas.")
        return

    if not administrador.tiene_permiso("gestionar_usuarios"):
        print("No tiene permiso para crear usuarios.")
        return

    print("\n--- REGISTRO DE NUEVO USUARIO ---")

    nombre = input("Nombre de usuario: ").strip()
    contrasena = getpass("Contraseña: ")
    confirmar = getpass("Confirmar contraseña: ")

    if contrasena != confirmar:
        print("Las contraseñas no coinciden.")
        return

    print("\nRoles disponibles:")
    print("1. Administrador")
    print("2. Medico")
    print("3. Recepcionista")

    opcion = input("Seleccione el rol: ").strip()

    roles = {
        "1": "Administrador",
        "2": "Medico",
        "3": "Recepcionista"
    }

    nombre_rol = roles.get(opcion)

    if nombre_rol is None:
        print("Opción no válida.")
        return

    try:
        servicio.crear_usuario(nombre, contrasena, nombre_rol)
        print("Usuario registrado correctamente.")

    except ValueError as error:
        print(f"Error: {error}")

if __name__ == "__main__":
    main()