from pydantic import BaseModel
from datetime import date
from typing import Optional

class ConsultaSimpleCreate(BaseModel):
    IDpaciente: int
    IDusuario: int
    FConsulta: date
    Motivo: str
    Observaciones: Optional[str] = None
