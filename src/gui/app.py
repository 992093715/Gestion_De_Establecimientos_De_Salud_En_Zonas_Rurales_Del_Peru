import tkinter as tk

from src.gui.ventanas.ventana_login import VentanaLogin
from src.gui.ventanas.ventana_pacientes import VentanaPacientes

def iniciar_app():
    ventana = tk.Tk()

    def mostrar_pacientes(usuario):
        for componente in ventana.winfo_children():
            componente.destroy()
            
        VentanaPacientes(ventana, usuario)

    VentanaLogin(ventana, mostrar_pacientes)
    
    ventana.mainloop()