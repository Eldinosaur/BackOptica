from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.consulta import ConsultaSimpleCreate
from app.crud.consulta import *

router = APIRouter()

# Dependencia para obtener sesión de DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/consulta_simple")
def crear_consulta(consulta: ConsultaSimpleCreate, db: Session = Depends(get_db)):
    return crear_consulta_simple(db, consulta)
