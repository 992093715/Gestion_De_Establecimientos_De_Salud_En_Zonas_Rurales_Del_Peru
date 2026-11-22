from datetime import datetime

from src.repositorios.historial_repositorio import HistorialRepositorio
from src.repositorios.paciente_repositorio import PacienteRepositorio

class HistorialServicio:

    def __init__(self):
        self.repositorio = HistorialRepositorio()
        self.pacientes = PacienteRepositorio()

    def registrar_diagnostico(self, id_paciente, diagnostico,
                              observaciones, usuario):

        if not usuario.tiene_permiso("registrar_diagnostico"):
            raise PermissionError(
                "No tiene permiso para registrar diagnósticos."
            )

        paciente = self.pacientes.buscar_por_id(id_paciente)

        if paciente is None:
            raise ValueError("El paciente no existe.")

        if not diagnostico or not diagnostico.strip():
            raise ValueError("El diagnóstico no puede estar vacío.")

        fecha = datetime.now().isoformat(timespec="seconds")

        return self.repositorio.registrar(
            id_paciente,
            fecha,
            diagnostico.strip(),
            observaciones,
            usuario.get_id_usuario()
        )

    def consultar_historial(self, id_paciente, usuario):

        if not usuario.tiene_permiso("consultar_historial"):
            raise PermissionError(
                "No tiene permiso para consultar historiales."
            )

        paciente = self.pacientes.buscar_por_id(id_paciente)

        if paciente is None:
            raise ValueError("El paciente no existe.")

        return self.repositorio.obtener_por_paciente(id_paciente)