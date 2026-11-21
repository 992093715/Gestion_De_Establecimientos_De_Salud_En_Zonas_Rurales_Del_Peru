import sqlite3
from pathlib import Path

RUTA_BASE = Path(__file__).resolve().parents[2]
RUTA_DATA = RUTA_BASE / "data"
RUTA_DB = RUTA_DATA / "esalud.db"

_conexion = None

def obtener_conexion():
    global _conexion

    if _conexion is None:
        RUTA_DATA.mkdir(parents=True, exist_ok=True)

        _conexion = sqlite3.connect(RUTA_DB)
        _conexion.row_factory = sqlite3.Row

        inicializar_base_datos()

    return _conexion

def inicializar_base_datos():
    ruta_sql = RUTA_DATA / "scripts" / "create_tables.sql"

    conexion = _conexion

    with open(ruta_sql, "r", encoding="utf-8") as archivo:
        conexion.executescript(archivo.read())

    conexion.commit()

def cerrar_conexion():
    global _conexion

    if _conexion is not None:
        _conexion.close()
        _conexion = None