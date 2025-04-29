from pydantic import BaseModel
from datetime import date
from typing import Optional

# Parte de la consulta
class ConsultaBase(BaseModel):
    IDpaciente: int
    IDusuario: int
    FConsulta: date
    Observaciones: str
    Motivo: str

# Parte de la receta general
class RecetaBase(BaseModel):
    TipoLente: int  # 1: Armazones, 2: Contacto
    Fecha: date

# Parte de la receta de armazones
class RecetaArmazones(BaseModel):
    OD_SPH: Optional[float] = None
    OD_CYL: Optional[float] = None
    OD_AXIS: Optional[float] = None
    OD_ADD: Optional[float] = None
    OI_SPH: Optional[float] = None
    OI_CYL: Optional[float] = None
    OI_AXIS: Optional[float] = None
    OI_ADD: Optional[float] = None
    DIP: Optional[float] = None

# Parte de la receta de contacto
class RecetaContacto(BaseModel):
    OD_SPH: Optional[float] = None
    OD_CYL: Optional[float] = None
    OD_AXIS: Optional[float] = None
    OD_ADD: Optional[float] = None
    OD_BC: Optional[float] = None
    OD_DIA: Optional[float] = None
    OI_SPH: Optional[float] = None
    OI_CYL: Optional[float] = None
    OI_AXIS: Optional[float] = None
    OI_ADD: Optional[float] = None
    OI_BC: Optional[float] = None
    OI_DIA: Optional[float] = None
    MarcaLente: Optional[str] = None
    TiempoUso: Optional[str] = None

# Parte de evolución visual
class EvolucionVisual(BaseModel):
    OD: float
    OI: float
    Fecha: date

# Modelo combinado para recibir todo en un solo JSON
class ConsultaCompletaCreate(BaseModel):
    consulta: ConsultaBase
    receta: RecetaBase
    receta_armazones: Optional[RecetaArmazones] = None
    receta_contacto: Optional[RecetaContacto] = None
    evolucion: EvolucionVisual

# ========== MODELOS DE RESPUESTA (OUT) ==========

class RecetaArmazonesOut(RecetaArmazones):
    class Config:
        orm_mode = True

class RecetaContactoOut(RecetaContacto):
    class Config:
        orm_mode = True

class EvolucionVisualOut(EvolucionVisual):
    class Config:
        orm_mode = True

class RecetaBaseOut(BaseModel):
    IDreceta: int
    TipoLente: int
    Fecha: date
    receta_armazones: Optional[RecetaArmazonesOut] = None
    receta_contacto: Optional[RecetaContactoOut] = None

    class Config:
        orm_mode = True

class ConsultaCompletaOut(BaseModel):
    IDconsulta: int
    IDpaciente: int
    IDusuario: int
    FConsulta: date
    Observaciones: str
    Motivo: str
    receta: Optional[RecetaBaseOut] = None

    class Config:
        orm_mode = True

