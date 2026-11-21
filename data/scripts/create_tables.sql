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