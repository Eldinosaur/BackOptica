from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.receta import ConsultaCompletaCreate, ConsultaCompletaOut
from app.crud.consulta_completa import *
from typing import List

router = APIRouter()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/consulta_completa", status_code=status.HTTP_201_CREATED)
def registrar_consulta_completa(consulta_completa: ConsultaCompletaCreate, db: Session = Depends(get_db)):
    try:
        id_consulta = crear_consulta_completa(db, consulta_completa)
        return {
            "message": "Consulta completa registrada exitosamente",
            "IDconsulta": id_consulta
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/consulta_completa/paciente/{id_paciente}", response_model=List[ConsultaCompletaOut])
def listar_consultas_completas_por_paciente(id_paciente: int, db: Session = Depends(get_db)):
    return obtener_consultas_completas_por_paciente(db, id_paciente)

@router.get("/consulta_completa/{id_consulta}", response_model=ConsultaCompletaOut)
def obtener_consulta_completa(id_consulta: int, db: Session = Depends(get_db)):
    return obtener_consulta_completa_por_id(db, id_consulta)

@router.get("/consulta_completa/paciente/{id_paciente}/tipo_armazon/", response_model=List[ConsultaCompletaOut])
def listar_consultas_armazones(id_paciente: int, db: Session = Depends(get_db)):
    return obtener_consultas_completas_tipo_armazon(db, id_paciente)

@router.get("/consulta_completa/paciente/{id_paciente}/tipo_contacto/", response_model=List[ConsultaCompletaOut])
def listar_consultas_contacto(id_paciente: int, db: Session = Depends(get_db)):
    return obtener_consultas_completas_tipo_contacto(db, id_paciente)