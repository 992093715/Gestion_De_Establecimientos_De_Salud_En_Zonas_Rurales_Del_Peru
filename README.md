# GestionEsSalud

**GestionEsSalud** es una aplicación de escritorio desarrollada en Phyton 3.x orientada a resolver las ineficiencias administrativas, la saturación de ventanillas y la pérdida de citas en el **Policlínico EsSalud "Juan José Rodríguez Lazo"** (Chorrillos, Lima).

El proyecto adopta un enfoque de diseño multiparadigma (Programación Orientada a Objetos, Programación Funcional y Programación Orientada a Eventos) para garantizar una ejecución fluida en estaciones de trabajo de bajos recursos de hardware (RAM 4 GB) y en entornos sin conectividad continua (*offline-first*).

## Integrantes del Grupo 4
- Aragon Sanchez, Samuel Aaron
- Castillo Ramos, Fernanda Lucia
- Choqque Santiago, Jeremy Matt
- Gamboa Mori, Carlos Bryan
- Olavarria Ccora, Fernando Alonzo

## Características Principales y Requerimientos (R1 - R6)

* **R1 - Registro y Gestión de Pacientes:** Clasificación por prioridad (adultos mayores, personas vulnerables) e identificación segura mediante hashing **SHA-256** del DNI, cumpliendo estrictamente con la **Ley N.° 29733** (Ley de Protección de Datos Personales).
* **R2 - Programación de Citas sin Colisiones:** Validación automatizada de disponibilidad horaria por médico y especialidad, impidiendo el solapamiento o asignación doble de turnos.
* **R3 - Historial Clínico Digital:** Módulo de registro seguro de consultas, diagnósticos y observaciones médicas con control de accesos.
* **R4 - Cancelación y Reasignación de Cupos:** Liberación inmediata de cupos ante ausencias de pacientes y gestión orientada a eventos para su reasignación en lista de espera.
* **R5 - Control de Stock de Farmacia:** Filtrado inmutable de medicamentos y verificación automática de existencias previo a la prescripción médica.
* **R6 - Operatividad Local y RBAC:** Control de acceso basado en roles (*Administrador, Admisión, Médico, Farmacia*) que opera de forma autónoma sin depender de servidores externos.

## Ejecución del Script de Viabilidad (Spike Técnico)

Con Python instalado, abre una terminal y ejecuta:

```bash
python spike_viabilidad.py
```

En Windows también puedes utilizar `py spike_viabilidad.py`.
