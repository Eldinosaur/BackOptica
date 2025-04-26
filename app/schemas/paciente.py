from pydantic import BaseModel
from datetime import date

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

class PacienteCreate(PacienteBase):
    pass

class PacienteOut(PacienteBase):
    IDpaciente: int

    class Config:
        orm_mode = True
