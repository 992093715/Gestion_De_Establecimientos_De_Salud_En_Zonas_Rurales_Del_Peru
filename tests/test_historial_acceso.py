import unittest

from src.modelos.historial_clinico import HistorialClinico
from src.modelos.rol import Rol
from src.modelos.usuario import Usuario
from src.utils.seguridad import (
    generar_hash_contrasena,
    verificar_contrasena
)

class TestHistorialClinico(unittest.TestCase):

    def test_historial_pertenece_a_un_paciente(self):
        historial = HistorialClinico("H001", "P001")

        self.assertEqual(historial.get_id_paciente(), "P001")

    def test_agregar_diagnostico(self):
        historial = HistorialClinico("H001", "P001")

        historial.agregar_registro(
            "2026-11-21",
            "Diagnóstico de prueba",
            "Observación de prueba",
            "U001"
        )

        self.assertEqual(len(historial.get_registros()), 1)

    def test_no_permite_diagnostico_vacio(self):
        historial = HistorialClinico("H001", "P001")

        with self.assertRaises(ValueError):
            historial.agregar_registro(
                "2026-11-21",
                "",
                "",
                "U001"
            )

class TestControlAcceso(unittest.TestCase):

    def test_verificar_permiso(self):
        rol = Rol(
            "MEDICO",
            "Medico",
            ["consultar_historial"]
        )

        usuario = Usuario(
            "U001",
            "medico_prueba",
            "hash_prueba",
            rol
        )

        self.assertTrue(
            usuario.tiene_permiso("consultar_historial")
        )

        self.assertFalse(
            usuario.tiene_permiso("gestionar_usuarios")
        )

    def test_usuario_desactivado_no_tiene_permisos(self):
        rol = Rol(
            "ADMIN",
            "Administrador",
            ["gestionar_usuarios"]
        )

        usuario = Usuario(
            "U002",
            "admin_prueba",
            "hash_prueba",
            rol
        )

        usuario.desactivar()

        self.assertFalse(
            usuario.tiene_permiso("gestionar_usuarios")
        )

    def test_hash_de_contrasena(self):
        contrasena = "ClavePrueba123"
        hash_generado = generar_hash_contrasena(contrasena)

        self.assertTrue(
            verificar_contrasena(contrasena, hash_generado)
        )

        self.assertFalse(
            verificar_contrasena("ClaveIncorrecta", hash_generado)
        )

if __name__ == "__main__":
    unittest.main()