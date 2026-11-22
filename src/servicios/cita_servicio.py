from src.modelos.cita import CitaMedica
from src.repositorios.cita_repositorio import CitaRepositorio
from src.repositorios.paciente_repositorio import PacienteRepositorio

class CitaServicio:
    def __init__(self):
        self.repositorio = CitaRepositorio()
        self.pacientes = PacienteRepositorio()

    def programar_cita(self, id_cita, id_paciente, fecha, medico, usuario):
        if not usuario.tiene_permiso("gestionar_citas"):
            raise PermissionError("No tiene permiso para gestionar citas.")

        if not all([id_cita.strip(), fecha.strip(), medico.strip()]):
            raise ValueError("Todos los campos son obligatorios.")

        paciente = self.pacientes.buscar_por_id(id_paciente)

        if paciente is None:
            raise ValueError("El paciente no existe.")

        cita = CitaMedica(id_cita, paciente, fecha, medico)
        self.repositorio.registrar(cita)

        return cita

    def obtener_citas(self, usuario):
        if not usuario.tiene_permiso("gestionar_citas"):
            raise PermissionError("No tiene permiso para consultar citas.")

        return self.repositorio.obtener_todas()

    def cancelar_cita(self, id_cita, usuario):
        if not usuario.tiene_permiso("gestionar_citas"):
            raise PermissionError("No tiene permiso para cancelar citas.")

        if not self.repositorio.cancelar(id_cita):
            raise ValueError(
                "La cita no existe o ya está cancelada."
            )