import tkinter as tk
from tkinter import messagebox

class VentanaLogin:
    def __init__(self, ventana, al_ingresar):
        self.ventana = ventana
        self.al_ingresar = al_ingresar

        self.ventana.title("GestiónEsSalud - Inicio de sesión")
        self.ventana.geometry("350x250")

        tk.Label(
            ventana,
            text="GESTIÓNESSALUD",
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

    def verificar_campos(self):
        if not self.usuario.get().strip() or not self.contrasena.get():
            messagebox.showwarning(
                "Advertencia",
                "Complete todos los campos."
            )
            return

        messagebox.showinfo(
            "Aviso",
            "La autenticación real está pendiente de implementación."
        )