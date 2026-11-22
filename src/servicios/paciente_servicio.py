from src.modelos.paciente import Paciente
from src.repositorios.paciente_repositorio import PacienteRepositorio

class PacienteServicio:
    def __init__(self):
        self.repositorio = PacienteRepositorio()

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

        paciente = Paciente(id_paciente, nombre, dni)
        self.repositorio.registrar(paciente)

        return paciente

    def buscar_paciente_por_nombre(self, criterio, usuario):
        if not usuario.tiene_permiso("consultar_paciente"):
            raise PermissionError(
                "No tiene permiso para consultar pacientes."
            )

        return self.repositorio.buscar_por_nombre(criterio)

    def obtener_pacientes(self):
        if not usuario.tiene_permiso("consultar_paciente"):
            raise PermissionError(
                "No tiene permiso para consultar pacientes."
            )

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