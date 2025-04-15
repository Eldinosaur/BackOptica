from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.usuario import UsuarioLogin, LoginResponse
from app.crud.auth import autenticar_usuario
from app.utils.jwt import crear_token

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

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
