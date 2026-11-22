from getpass import getpass
from src.servicios.autenticacion_servicio import AutenticacionServicio

def main():
    servicio = AutenticacionServicio()

    nombre = input("Nombre de usuario administrador: ").strip()
    contrasena = getpass("Contraseña: ")
    confirmar = getpass("Confirmar contraseña: ")

    if contrasena != confirmar:
        print("Las contraseñas no coinciden.")
        return

    try:
        servicio.crear_usuario(
            nombre,
            contrasena,
            "Administrador"
        )

        print("Usuario administrador creado correctamente.")

    except ValueError as error:
        print(f"Error: {error}")

if __name__ == "__main__":
    main()