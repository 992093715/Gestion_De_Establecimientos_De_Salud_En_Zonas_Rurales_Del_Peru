CREATE TABLE IF NOT EXISTS pacientes (
    id_paciente TEXT PRIMARY KEY,
    nombre TEXT NOT NULL,
    dni_hash TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS citas (
    id_cita TEXT PRIMARY KEY,
    id_paciente TEXT NOT NULL,
    fecha TEXT NOT NULL,
    medico TEXT NOT NULL,
    activa INTEGER DEFAULT 1,
    FOREIGN KEY (id_paciente)
        REFERENCES pacientes(id_paciente)
);

CREATE TABLE IF NOT EXISTS medicamentos (
    id_medicamento TEXT PRIMARY KEY,
    nombre TEXT NOT NULL,
    stock INTEGER NOT NULL CHECK(stock >= 0)
);

CREATE TABLE IF NOT EXISTS roles (
    id_rol TEXT PRIMARY KEY,
    nombre TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS permisos (
    id_permiso TEXT PRIMARY KEY,
    nombre TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS rol_permisos (
    id_rol TEXT NOT NULL,
    id_permiso TEXT NOT NULL,
    PRIMARY KEY (id_rol, id_permiso),
    FOREIGN KEY (id_rol) REFERENCES roles(id_rol),
    FOREIGN KEY (id_permiso) REFERENCES permisos(id_permiso)
);

CREATE TABLE IF NOT EXISTS usuarios (
    id_usuario TEXT PRIMARY KEY,
    nombre TEXT NOT NULL UNIQUE,
    contraseña_hash TEXT NOT NULL,
    id_rol TEXT NOT NULL,
    activo INTEGER NOT NULL DEFAULT 1,
    FOREIGN KEY (id_rol) REFERENCES roles(id_rol)
);

CREATE TABLE IF NOT EXISTS historiales_clinicos (
    id_historial TEXT PRIMARY KEY,
    id_paciente TEXT NOT NULL UNIQUE,
    FOREIGN KEY (id_paciente)
        REFERENCES pacientes(id_paciente)
);

CREATE TABLE IF NOT EXISTS registros_clinicos (
    id_registro TEXT PRIMARY KEY,
    id_historial TEXT NOT NULL,
    fecha TEXT NOT NULL,
    diagnostico TEXT NOT NULL,
    observaciones TEXT,
    id_usuario TEXT NOT NULL,
    FOREIGN KEY (id_historial)
        REFERENCES historiales_clinicos(id_historial),
    FOREIGN KEY (id_usuario)
        REFERENCES usuarios(id_usuario)
);