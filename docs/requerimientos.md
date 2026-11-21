## Requerimientos Funcionales (R1 - R6)

* **R1 - Registro y Gestión de Pacientes:** Clasificación por prioridad (adultos mayores, personas vulnerables) e identificación segura mediante hashing **SHA-256** del DNI, cumpliendo estrictamente con la **Ley N.° 29733** (Ley de Protección de Datos Personales).
* **R2 - Programación de Citas sin Colisiones:** Validación automatizada de disponibilidad horaria por médico y especialidad, impidiendo el solapamiento o asignación doble de turnos.
* **R3 - Historial Clínico Digital:** Módulo de registro seguro de consultas, diagnósticos y observaciones médicas con control de accesos.
* **R4 - Cancelación y Reasignación de Cupos:** Liberación inmediata de cupos ante ausencias de pacientes y gestión orientada a eventos para su reasignación en lista de espera.
* **R5 - Control de Stock de Farmacia:** Filtrado inmutable de medicamentos y verificación automática de existencias previo a la prescripción médica.
* **R6 - Operatividad Local y RBAC:** Control de acceso basado en roles (*Administrador, Admisión, Médico, Farmacia*) que opera de forma autónoma sin depender de servidores externos.