from sqlalchemy.orm import Session
from app.models.usuario import Usuario
from app.utils.hashing import verificar_clave

def autenticar_usuario(db: Session, usuario: str, clave: str):
    user = db.query(Usuario).filter(Usuario.Usuario == usuario).first()
    if not user or not verificar_clave(clave, user.Clave):
        return None
    return user
