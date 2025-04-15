from sqlalchemy.orm import Session
from app.models.usuario import Usuario

def autenticar_usuario(db: Session, usuario: str, clave: str):
    user = db.query(Usuario).filter(Usuario.Usuario == usuario).first()
    if not user or user.Clave != clave:  
        return None
    return user
