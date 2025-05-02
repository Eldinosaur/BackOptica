from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.paciente import PacienteCreate, PacienteConConsultaOut
from app.crud.paciente import *
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
    if nuevo_paciente:
        return {
        "message": "Paciente creado exitosamente",
        "IDpaciente": nuevo_paciente.IDpaciente
        }

@router.get("/paciente/{paciente_id}")
def get_paciente_id(paciente_id: int, db: Session = Depends(get_db)):
    paciente = obtener_paciente_id(db, paciente_id)
    
    # Si no se encuentra el paciente, lanzamos un error 404
    if not paciente:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    
    return paciente

@router.get("/pacientes")
def get_pacientes(db: Session = Depends(get_db)):
    pacientes = obtener_todos_pacientes(db)
    return pacientes


@router.get("/pacientecedula/{paciente_cedula}")
def get_paciente_cedula(paciente_cedula: str, db: Session = Depends(get_db)):
    paciente = obtener_paciente_cedula(db, paciente_cedula)
    
    # Si no se encuentra el paciente, lanzamos un error 404
    if not paciente:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    
    return paciente

@router.get("/buscar_paciente/{termino}")
def get_paciente_nombre_apellido(termino: str, db: Session = Depends(get_db)):
    pacientes = obtener_pacientes_por_nombre_apellido(db, termino)

    if not pacientes:
        raise HTTPException(status_code=404, detail="No se encontraron pacientes con ese nombre o apellido")
    
    return pacientes

@router.put("/{paciente_id}")
def actualizar_paciente_endpoint(paciente_id: int, paciente: PacienteCreate, db: Session = Depends(get_db)):
    paciente_actualizado = actualizar_paciente(db, paciente_id, paciente)
    if paciente_actualizado:
        return {"mensaje": "Paciente actualizado correctamente"}
    else:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")


@router.get("/pacientes/{paciente_id}/detalle", response_model=PacienteConConsultaOut)
def get_paciente_con_consulta(paciente_id: int, db: Session = Depends(get_db)):
    paciente = obtener_paciente_con_ultima_consulta(db, paciente_id)
    if not paciente:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    return paciente
