from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.consulta import ConsultaSimpleCreate
from app.crud.consulta import crear_consulta_simple, obtener_consultas_simples_por_paciente

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

# Obtener consultas simples por paciente
@router.get("/consultas-simples/paciente/{id_paciente}")
def listar_consultas_simples(id_paciente: int, db: Session = Depends(get_db)):
    return obtener_consultas_simples_por_paciente(db, id_paciente)

