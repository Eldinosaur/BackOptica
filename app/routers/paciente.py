from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.paciente import PacienteCreate
from app.crud.paciente import crear_paciente, obtener_paciente

router = APIRouter()

# Dependencia para obtener sesión de DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/paciente", status_code=status.HTTP_201_CREATED)
def agregar_paciente(paciente: PacienteCreate, db: Session = Depends(get_db)):
    nuevo_paciente = crear_paciente(db, paciente)
    return {
        "message": "Paciente creado exitosamente",
        "IDpaciente": nuevo_paciente.IDpaciente,
        "Nombre": nuevo_paciente.Nombre,
        "Apellido": nuevo_paciente.Apellido,
        "Cedula": nuevo_paciente.Cedula
    }

@router.get("/paciente/{paciente_id}")
def get_paciente(paciente_id: int, db: Session = Depends(get_db)):
    paciente = obtener_paciente(db, paciente_id)
    
    # Si no se encuentra el paciente, lanzamos un error 404
    if not paciente:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    
    return paciente