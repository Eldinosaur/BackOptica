from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.usuario import UsuarioLogin, CambioClave
from app.crud.login import autenticar_usuario, cambiar_clave
from app.utils.jwt import crear_token

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Ruta para inicio de sesion
@router.post("/login")
def login(data: UsuarioLogin, db: Session = Depends(get_db)):
    usuario = autenticar_usuario(db, data.Usuario, data.Clave)
    if not usuario:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    token = crear_token({"sub": usuario.Usuario})
    return {
        "access_token": token, 
        "token_type": "bearer",
        "IDusuario": usuario.IDusuario,
        "Nombre": usuario.Nombre,
        "Apellido": usuario.Apellido
        }

# Ruta para cambio de clave
@router.post("/cambioclave")
def cambiar_contrasena(data: CambioClave, db: Session = Depends(get_db)):
    exito, mensaje = cambiar_clave(db, data.IDusuario, data.ClaveActual, data.NuevaClave)
    if not exito:
        raise HTTPException(status_code=401, detail=mensaje)
    return {"mensaje": mensaje}
