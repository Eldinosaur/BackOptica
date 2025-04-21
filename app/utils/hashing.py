from argon2 import PasswordHasher, exceptions

ph = PasswordHasher()

# Verifica si la contraseña coincide con el hash almacenado
def verificar_clave(password_plano: str, password_hash: str) -> bool:
    try:
        return ph.verify(password_hash, password_plano)
    except exceptions.VerifyMismatchError:
        return False

# Genera un hash para la contraseña usando Argon2
def generar_hash(password_plano: str) -> str:
    return ph.hash(password_plano)
