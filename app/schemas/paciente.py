from pydantic import BaseModel
from datetime import date
from typing import Optional

class PacienteBase(BaseModel):
    Cedula: str
    Nombre: str
    Apellido: str
    FNacimiento: date
    Ocupacion: str
    Telefono: str
    Correo: str
    Direccion: str
    Antecedentes: str
    CondicionesMedicas: str

class UltimaConsultaFecha(BaseModel):
    ultima_consulta_fecha: date

class PacienteCreate(PacienteBase):
    pass

class PacienteOut(PacienteBase):
    IDpaciente: int

    class Config:
        orm_mode = True

class PacienteConConsultaOut(PacienteOut):
    ultima_consulta: Optional[UltimaConsultaFecha] = None

