from sqlalchemy.orm import Session
from app.models.evolucion import EvolucionVisual

def obtener_evolucion_por_paciente(db: Session, paciente_id: int):
    return (
        db.query(EvolucionVisual)
        .filter(EvolucionVisual.IDpaciente == paciente_id)
        .order_by(EvolucionVisual.Fecha.asc())  
        .all()
    )
