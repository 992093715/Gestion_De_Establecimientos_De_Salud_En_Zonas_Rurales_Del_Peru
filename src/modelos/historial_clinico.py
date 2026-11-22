class HistorialClinico:

    def __init__(self, id_historial, id_paciente, registros=None):
        if not id_paciente:
            raise ValueError("El historial debe pertenecer a un paciente.")

        self.__id_historial = id_historial
        self.__id_paciente = id_paciente
        self.__registros = list(registros) if registros else []

    def get_id_historial(self):
        return self.__id_historial

    def get_id_paciente(self):
        return self.__id_paciente

    def get_registros(self):
        return [registro.copy() for registro in self.__registros]

    def agregar_registro(self, fecha, diagnostico, observaciones, id_usuario):
        if not diagnostico or not diagnostico.strip():
            raise ValueError("El diagnóstico no puede estar vacío.")

        if not id_usuario:
            raise ValueError("Se requiere identificar al profesional responsable.")

        registro = {
            "fecha": fecha,
            "diagnostico": diagnostico.strip(),
            "observaciones": observaciones.strip() if observaciones else "",
            "id_usuario": id_usuario
        }

        self.__registros.append(registro)
        
        return registro.copy()
    
    def _agregar_nota_compatibilidad(self, nota):
        self.__registros.append({
            "fecha": None,
            "diagnostico": nota,
            "observaciones": "",
            "id_usuario": None
        })

        self.__registros.append(registro)
        return registro.copy()