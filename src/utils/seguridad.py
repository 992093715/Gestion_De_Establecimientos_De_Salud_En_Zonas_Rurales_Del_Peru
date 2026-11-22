import hashlib
import secrets
import hmac

def generar_hash(texto):
    return hashlib.sha256(texto.encode("utf-8")).hexdigest()

def generar_hash_contrasena(contrasena):
    if not contrasena:
        raise ValueError("La contraseña no puede estar vacía.")

    sal = secrets.token_hex(16)
    iteraciones = 600000

    resultado = hashlib.pbkdf2_hmac(
        "sha256",
        contrasena.encode("utf-8"),
        bytes.fromhex(sal),
        iteraciones
    )

    return f"pbkdf2_sha256${iteraciones}${sal}${resultado.hex()}"

def verificar_contrasena(contrasena, hash_guardado):
    try:
        algoritmo, iteraciones, sal, hash_original = hash_guardado.split("$")

        if algoritmo != "pbkdf2_sha256":
            return False

        resultado = hashlib.pbkdf2_hmac(
            "sha256",
            contrasena.encode("utf-8"),
            bytes.fromhex(sal),
            int(iteraciones)
        )

        return hmac.compare_digest(
            resultado.hex(),
            hash_original
        )

    except (ValueError, TypeError):
        return False