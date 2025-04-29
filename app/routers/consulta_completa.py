from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.receta import ConsultaCompletaCreate
from app.crud.consulta_completa import crear_consulta_completa

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
