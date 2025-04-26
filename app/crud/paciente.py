from sqlalchemy.orm import Session
from app.models.paciente import Paciente
from app.schemas.paciente import PacienteCreate
from app.utils.aes import encrypt

def crear_paciente(db: Session, paciente: PacienteCreate):
    nuevo_paciente = Paciente(
        Cedula=encrypt(paciente.Cedula),
        Nombre=encrypt(paciente.Nombre),
        Apellido=encrypt(paciente.Apellido),
        FNacimiento=paciente.FNacimiento,  # La fecha no la encriptamos
        Ocupacion=encrypt(paciente.Ocupacion),
        Telefono=encrypt(paciente.Telefono),
        Correo=encrypt(paciente.Correo),
        Direccion=encrypt(paciente.Direccion),
        Antecedentes=encrypt(paciente.Antecedentes),
        CondicionesMedicas=encrypt(paciente.CondicionesMedicas)
    )
    db.add(nuevo_paciente)
    db.commit()
    db.refresh(nuevo_paciente)
    return nuevo_paciente
