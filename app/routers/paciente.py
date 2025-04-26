from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.paciente import PacienteCreate
from app.crud.paciente import crear_paciente

router = APIRouter()

# Dependencia para obtener sesión de DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/agregarpaciente", status_code=status.HTTP_201_CREATED)
def agregar_paciente(paciente: PacienteCreate, db: Session = Depends(get_db)):
    nuevo_paciente = crear_paciente(db, paciente)
    return {
        "message": "Paciente creado exitosamente",
        "IDpaciente": nuevo_paciente.IDpaciente,
        "Nombre": nuevo_paciente.Nombre,
        "Apellido": nuevo_paciente.Apellido,
        "Cedula": nuevo_paciente.Cedula
    }
