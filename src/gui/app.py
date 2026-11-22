import tkinter as tk

from src.gui.ventanas.ventana_login import VentanaLogin
from src.gui.ventanas.ventana_pacientes import VentanaPacientes
from src.servicios.autenticacion_servicio import AutenticacionServicio

def iniciar_app():
    # Crear automáticamente la cuenta de demostración si no existe.
    servicio = AutenticacionServicio()

    if servicio.usuarios.buscar_por_nombre("admin_demo") is None:
        servicio.crear_usuario(
            "admin_demo",
            "GestionEsSalud2026!",
            "Administrador"
        )

    ventana = tk.Tk()

    def mostrar_pacientes(usuario):
        for componente in ventana.winfo_children():
            componente.destroy()

        VentanaPacientes(ventana, usuario)

    VentanaLogin(ventana, mostrar_pacientes)

    ventana.mainloop()