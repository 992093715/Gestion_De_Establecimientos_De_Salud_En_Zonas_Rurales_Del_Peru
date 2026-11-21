import tkinter as tk
from src.gui.ventanas.ventana_pacientes import VentanaPacientes

def iniciar_app():
    ventana = tk.Tk()
    VentanaPacientes(ventana)
    ventana.mainloop()