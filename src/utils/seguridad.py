import hashlib

def generar_hash(texto):
    return hashlib.sha256(texto.encode("utf-8")).hexdigest()