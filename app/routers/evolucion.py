from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database import SessionLocal
from app.schemas.evolucion import EvolucionVisualSchema
from app.crud.evolucion import obtener_evolucion_por_paciente

router = APIRouter()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/evolucion_visual/paciente/{id_paciente}", response_model=List[EvolucionVisualSchema])
def listar_evolucion_visual_por_paciente(id_paciente: int, db: Session = Depends(get_db)):
    try:
        registros = obtener_evolucion_por_paciente(db, id_paciente)
        if not registros:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No hay registros de evolución visual para este paciente."
            )
        return registros
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
