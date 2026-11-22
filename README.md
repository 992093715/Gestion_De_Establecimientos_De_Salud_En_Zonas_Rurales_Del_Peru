# GestionEsSalud

**GestionEsSalud** es una aplicación de escritorio desarrollada en Python 3.x orientada a resolver las ineficiencias administrativas, la saturación de ventanillas y la pérdida de citas en el **Policlínico EsSalud "Juan José Rodríguez Lazo"** (Chorrillos, Lima).

El proyecto adopta un enfoque de diseño multiparadigma (Programación Orientada a Objetos, Programación Funcional y Programación Orientada a Eventos) para garantizar una ejecución fluida en estaciones de trabajo de bajos recursos de hardware (RAM 4 GB) y en entornos sin conectividad continua (*offline-first*).

## Herramientas utilizadas

* **Python 3.x:** lenguaje principal de desarrollo.
* **SQLite:** sistema de gestión de base de datos.
* **Tkinter:** desarrollo de la interfaz gráfica de escritorio.
* **Git y GitHub:** control de versiones y trabajo colaborativo.

## Requisitos previos

Antes de instalar y ejecutar el proyecto, es necesario contar con:

* Python 3.x instalado.
* Git instalado.
* Un editor de código, como Visual Studio Code (opcional).

Para comprobar que Python está instalado, abre una terminal y ejecuta:

```bash
python --version
```

En Windows también puedes utilizar:

```bash
py --version
```

## Instalación y configuración

Sigue estos pasos para obtener una copia local del proyecto.

**1. Clonar el repositorio**

Abre una terminal y ejecuta:

```bash
git clone https://github.com/JemyVoid-09/Gestion_De_Establecimientos_De_Salud_En_Zonas_Rurales_Del_Peru.git
```

**2. Ingresar a la carpeta del proyecto**

```bash
cd Gestion_De_Establecimientos_De_Salud_En_Zonas_Rurales_Del_Peru
```

**3. Crear un entorno virtual**

Se recomienda crear un entorno virtual para mantener aisladas las dependencias del proyecto.

```bash
python -m venv .venv
```

En Windows también puedes utilizar:

```bash
py -m venv .venv
```

**4. Activar el entorno virtual**

En Windows PowerShell:

```bash
.venv\Scripts\Activate.ps1
```

En Windows CMD:

```bash
.venv\Scripts\activate.bat
```

En caso falle, vuelva a intentar luego de ejecutar:

```bash
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

**5. Instalar las dependencias**

Con el entorno virtual activado, ejecuta:

```bash
python -m pip install -r requerimientos.txt
```

Este comando instala las dependencias declaradas en el archivo requerimientos.txt.

## Ejecución de la aplicación

Una vez completada la instalación, asegúrate de encontrarte en la carpeta raíz del proyecto.

Para iniciar la aplicación de escritorio, ejecuta:

```bash
python main.py
```

En Windows también puedes utilizar:

```bash
py main.py
```

El archivo main.py funciona como punto de entrada del programa e inicia la aplicación mediante los módulos de la interfaz gráfica ubicados en src/gui/.

## Base de datos

El proyecto utiliza SQLite para almacenar la información de la aplicación.

La configuración y conexión con la base de datos se gestionan desde:

```bash
src/utils/database.py
```

La estructura de las tablas se encuentra definida en el siguiente archivo:

```bash
data/scripts/create_tables.sql
```

La base de datos local se almacena en:

```bash
data/gestion_essalud.db
```

El módulo de base de datos se encarga de inicializar la base de datos y ejecutar el script de creación de tablas cuando corresponde.

**Nota:** el archivo gestion_essalud.db es una base de datos local y no necesita incluirse en el repositorio. La estructura de las tablas se conserva en el archivo SQL para que pueda generarse nuevamente en cada instalación.

## Ejecución del script de viabilidad (Spike Técnico)

El proyecto incluye un script de viabilidad que permite comprobar el funcionamiento del modelo Paciente mediante datos de prueba y verificaciones con assert.

Para ejecutarlo, abre una terminal en la carpeta raíz del proyecto y utiliza:

```bash
python -m tests.test_spike_viabilidad
```

En Windows también puedes utilizar:

```bash
py -m tests.test_spike_viabilidad
```

## Distribución del equipo

* **Aragon Sanchez, Samuel Aaron**

Rol: Analista de Pruebas y Calidad de Software

Descripción de tarea: Ejecución de pruebas del módulo: registro de pacientes, validación de citas, cancelaciones, consultas y control de inventario.

* **Castillo Ramos, Fernanda Lucia**

Rol: Analista de Requerimientos y Contexto, Analista de Software y Arquitectura, Desarrolladora de Módulos Operativos

Descripción de tarea: Definición del contexto de EsSalud, requerimientos y restricciones; selección del enfoque multiparadigma; integración de validaciones, excepciones y protección de datos; y revisión final del repositorio.

* **Choqque Santiago, Jeremy Matt**

Rol: Desarrollador de Módulos Internos y Protección de Datos

Descripción de tarea: Implementación de las clases principales: Paciente, CitaMedica, HistorialClinico, Medicamento, Usuario y Rol.

* **Gamboa Mori, Carlos Bryan**

Rol: Diseñador UML y Modelado de Dominio

Descripción de tarea: Diseño de la arquitectura modular y elaboración del diagrama de clases UML.

* **Olavarria Ccora, Fernando Alonzo**

Rol: Redactor de Conclusiones y Aspectos Éticos

Descripción de tarea: Redacción de la Sección 1.6: síntesis de decisiones de diseño, limitaciones técnicas, recomendaciones y reflexión ética.

## Cuenta de demostración

Al ejecutar el programa por primera vez, el sistema crea automáticamente una cuenta de administrador de demostración si todavía no existe.

**Credenciales:**

- Usuario: `admin_demo`
- Contraseña: `GestionEsSalud2026!`
- Rol: Administrador

La cuenta está destinada exclusivamente a pruebas y demostraciones del funcionamiento de GestionEsSalud.