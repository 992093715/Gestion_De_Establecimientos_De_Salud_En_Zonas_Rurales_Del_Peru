import tkinter as tk
from tkinter import messagebox

from src.servicios.autenticacion_servicio import AutenticacionServicio

class VentanaLogin:
    def __init__(self, ventana, al_ingresar):
        self.ventana = ventana
        self.al_ingresar = al_ingresar
        self.servicio = AutenticacionServicio()

        self.ventana.title("GestiónEsSalud - Inicio de sesión")
        self.ventana.geometry("350x250")

        tk.Label(
            ventana,
            text="GESTIONESALUD",
            font=("Arial", 16, "bold")
        ).pack(pady=15)

        tk.Label(ventana, text="Usuario").pack()
        self.usuario = tk.Entry(ventana)
        self.usuario.pack()

        tk.Label(ventana, text="Contraseña").pack()
        self.contrasena = tk.Entry(ventana, show="*")
        self.contrasena.pack()

        tk.Button(
            ventana,
            text="Ingresar",
            command=self.verificar_campos
        ).pack(pady=20)

        self.ventana.bind("<Return>", lambda evento: self.verificar_campos())

    def verificar_campos(self):
        nombre = self.usuario.get().strip()
        contrasena = self.contrasena.get()
        
        if not nombre or not contrasena:
            messagebox.showwarning(
                "Advertencia",
                "Complete todos los campos."
            )
            return
        
        usuario = self.servicio.autenticar(nombre, contrasena)

        if usuario is None:
            messagebox.showerror(
                "Acceso denegado",
                "Usuario o contraseña incorrectos, o cuenta desactivada."
            )
            return

        messagebox.showinfo(
            "Bienvenido",
            f"Inicio de sesión correcto. Rol: {usuario.get_rol().get_nombre()}"
        )

        self.al_ingresar(usuario)