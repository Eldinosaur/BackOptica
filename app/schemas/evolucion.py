from pydantic import BaseModel
from datetime import date

class EvolucionVisualSchema(BaseModel):
    IDregistro: int
    Fecha: date
    OD: float
    OI: float

    class Config:
        orm_mode = True
