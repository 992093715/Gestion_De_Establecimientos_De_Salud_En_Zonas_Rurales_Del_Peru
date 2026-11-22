import tkinter as tk
from tkinter import messagebox
from src.servicios.paciente_servicio import PacienteServicio

class VentanaPacientes:
    def __init__(self, ventana, usuario):
        self.ventana = ventana
        self.servicio = PacienteServicio()
        self.usuario = usuario

        self.ventana.title("GestiónEsSalud - Gestión de pacientes")
        self.ventana.geometry("650x500")

        tk.Label(
            ventana,
            text="GESTIÓN DE PACIENTES",
            font=("Arial", 18, "bold")
        ).pack(pady=15)

        formulario = tk.Frame(ventana)
        formulario.pack(pady=10)

        tk.Label(formulario, text="ID:").grid(row=0, column=0)
        self.id_paciente = tk.Entry(formulario)
        self.id_paciente.grid(row=0, column=1, padx=5)

        tk.Label(formulario, text="Nombre:").grid(row=1, column=0)
        self.nombre = tk.Entry(formulario)
        self.nombre.grid(row=1, column=1, padx=5)

        tk.Label(formulario, text="DNI:").grid(row=2, column=0)
        self.dni = tk.Entry(formulario, show="*")
        self.dni.grid(row=2, column=1, padx=5)

        tk.Button(
            formulario,
            text="Registrar paciente",
            command=self.registrar
        ).grid(row=3, column=0, columnspan=2, pady=10)

        busqueda = tk.Frame(ventana)
        busqueda.pack(pady=10)

        tk.Label(busqueda, text="Buscar por nombre:").pack(side=tk.LEFT)

        self.criterio = tk.Entry(busqueda)
        self.criterio.pack(side=tk.LEFT, padx=5)

        tk.Button(
            busqueda,
            text="Buscar",
            command=self.buscar
        ).pack(side=tk.LEFT)

        tk.Button(
            ventana,
            text="Mostrar todos",
            command=self.mostrar_todos
        ).pack(pady=5)

        self.resultados = tk.Listbox(ventana, width=75, height=12)
        self.resultados.pack(pady=10)

    def registrar(self):
        try:
            self.servicio.registrar_paciente(
                self.id_paciente.get(),
                self.nombre.get(),
                self.dni.get(),
                self.usuario
            )

            messagebox.showinfo(
                "Registro",
                "Paciente registrado correctamente."
            )

            self.id_paciente.delete(0, tk.END)
            self.nombre.delete(0, tk.END)
            self.dni.delete(0, tk.END)

            self.mostrar_todos()

        except Exception as error:
            messagebox.showerror("Error", str(error))

    def buscar(self):
        try:
            pacientes = self.servicio.buscar_paciente_por_nombre(
                self.criterio.get(),
                self.usuario
            )

            self.resultados.delete(0, tk.END)

            for paciente in pacientes:
                self.resultados.insert(
                    tk.END,
                    f"{paciente.get_id_paciente()} | "
                    f"{paciente.get_nombre()} | "
                    f"DNI: {paciente.get_dni_hash()[:12]}..."
                )

        except Exception as error:
            messagebox.showerror("Error", str(error))

    def mostrar_todos(self):
        pacientes = self.servicio.obtener_pacientes(self.usuario)

        self.resultados.delete(0, tk.END)

        for paciente in pacientes:
            self.resultados.insert(
                tk.END,
                f"{paciente.get_id_paciente()} | "
                f"{paciente.get_nombre()} | "
                f"DNI: {paciente.get_dni_hash()[:12]}..."
            )