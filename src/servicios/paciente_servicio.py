from src.modelos.paciente import Paciente
from src.repositorios.paciente_repositorio import PacienteRepositorio

class PacienteServicio:
    # Instancia el repositorio para delegar la persistencia y consulta de datos de pacientes.
    def __init__(self):
        self.repositorio = PacienteRepositorio()
# Verifica permiso de registro, valida campos no vacíos y DNI de 8 dígitos, persiste y retorna el paciente. 
    def registrar_paciente(self, id_paciente, nombre, dni, usuario):
        if not usuario.tiene_permiso("registrar_paciente"):
            raise PermissionError(
                "No tiene permiso para registrar pacientes."
            )

        if not id_paciente.strip():
            raise ValueError("El ID no puede estar vacío.")

        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")

        if not dni.isdigit() or len(dni) != 8:
            raise ValueError("El DNI debe tener 8 dígitos.")

# Instancia el modelo Paciente y lo guarda en el repositorio tras pasar todas las validaciones.
        paciente = Paciente(id_paciente, nombre, dni)
        self.repositorio.registrar(paciente)

        return paciente
# Verifica permiso de consulta y delega al repositorio la búsqueda de pacientes por nombre. 

    def buscar_paciente_por_nombre(self, criterio, usuario):
        if not usuario.tiene_permiso("consultar_paciente"):
            raise PermissionError(
                "No tiene permiso para consultar pacientes."
            )
# Verifica permiso de consulta y retorna todos los pacientes registrados desde el repositorio.
        return self.repositorio.buscar_por_nombre(criterio)

    def obtener_pacientes(self, usuario):
        if not usuario.tiene_permiso("consultar_paciente"):
            raise PermissionError(
                "No tiene permiso para consultar pacientes."
            )

# Obtiene pacientes autorizados y formatea cada uno con ID, nombre y prefijo de 10 caracteres del hash del DNI.
        return self.repositorio.obtener_todos()

    def generar_reporte_pacientes(self, usuario):
        pacientes = self.obtener_pacientes(usuario)

        return list(map(
            lambda p: (
                f"ID: {p.get_id_paciente()} | "
                f"Paciente: {p.get_nombre()} | "
                f"DNI Hash: {p.get_dni_hash()[:10]}..."
            ),
            pacientes
        ))
