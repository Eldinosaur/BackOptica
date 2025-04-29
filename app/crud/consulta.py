from sqlalchemy.orm import Session
from app.models.consulta import DatosConsulta
from app.schemas.consulta import ConsultaSimpleCreate

def crear_consulta_simple(db: Session, consulta_data: ConsultaSimpleCreate):
    nueva_consulta = DatosConsulta(
        IDpaciente=consulta_data.IDpaciente,
        IDusuario=consulta_data.IDusuario,
        FConsulta=consulta_data.FConsulta,
        Motivo=consulta_data.Motivo,
        Observaciones=consulta_data.Observaciones
    )
    db.add(nueva_consulta)
    db.commit()
    db.refresh(nueva_consulta)
    return nueva_consulta
