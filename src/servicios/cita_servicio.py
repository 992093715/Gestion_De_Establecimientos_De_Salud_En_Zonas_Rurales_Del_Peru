from src.modelos.cita import CitaMedica
from src.repositorios.cita_repositorio import CitaRepositorio
from src.repositorios.paciente_repositorio import PacienteRepositorio

class CitaServicio:
    def __init__(self):
        self.repositorio = CitaRepositorio()
        self.pacientes = PacienteRepositorio()
# Bloquea el acceso si el usuario carece del permiso "gestionar_citas" lanzando PermissionError.
    def programar_cita(self, id_cita, id_paciente, fecha, medico, usuario):
        if not usuario.tiene_permiso("gestionar_citas"):
            raise PermissionError("No tiene permiso para gestionar citas.")
# Valida tras hacer .strip() que id_cita, fecha y medico no estén vacíos; si lo están, lanza ValueError.
        if not all([id_cita.strip(), fecha.strip(), medico.strip()]):
            raise ValueError("Todos los campos son obligatorios.")
# Consulta el repositorio de pacientes por id_paciente y aborta con ValueError si devuelve None. 
        paciente = self.pacientes.buscar_por_id(id_paciente)

        if paciente is None:
            raise ValueError("El paciente no existe.")
# Instancia CitaMedica, la persiste mediante el repositorio y retorna el objeto creado.
        cita = CitaMedica(id_cita, paciente, fecha, medico)
        self.repositorio.registrar(cita)

        return cita

    def obtener_citas(self, usuario):
        if not usuario.tiene_permiso("gestionar_citas"):
            raise PermissionError("No tiene permiso para consultar citas.")
# Verifica el permiso "gestionar_citas" y retorna todas las citas almacenadas en el repositorio.
        return self.repositorio.obtener_todas()

    def cancelar_cita(self, id_cita, usuario):
        if not usuario.tiene_permiso("gestionar_citas"):
            raise PermissionError("No tiene permiso para cancelar citas.")
# Intenta cancelar la cita por id_cita en el repositorio y lanza ValueError si no existe o ya estaba cancelada.
        if not self.repositorio.cancelar(id_cita):
            raise ValueError(
                "La cita no existe o ya está cancelada."
            )
