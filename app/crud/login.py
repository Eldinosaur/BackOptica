from sqlalchemy.orm import Session
from app.models.usuario import Usuario
from app.utils.hashing import verificar_clave
from argon2 import PasswordHasher, exceptions

#Funcion para validar usuario
def autenticar_usuario(db: Session, usuario: str, clave: str):
    user = db.query(Usuario).filter(Usuario.Usuario == usuario).first()
    if not user or not verificar_clave(clave, user.Clave):
        return None
    return user

#Inicializacion de metodo para encriptacion de clave
ph = PasswordHasher()

# Funcion para cambio de contraseña
def cambiar_clave(db: Session, id_usuario: int, clave_actual: str, nueva_clave: str) -> tuple[bool, str]:
    user = db.query(Usuario).filter(Usuario.IDusuario == id_usuario).first()
    if not user:
        return False, "Usuario no encontrado"

    try:
        ph.verify(user.Clave, clave_actual)
    except exceptions.VerifyMismatchError:
        return False, "La contraseña actual es incorrecta"

    hashed_nueva_clave = ph.hash(nueva_clave)
    user.Clave = hashed_nueva_clave
    db.commit()
    return True, "Contraseña actualizada correctamente"