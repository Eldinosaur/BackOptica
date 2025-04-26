from sqlalchemy.orm import Session
from app.models.paciente import Paciente
from app.schemas.paciente import PacienteCreate
from app.utils.aes import encrypt, decrypt

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

def obtener_paciente(db: Session, paciente_id: int):
    paciente = db.query(Paciente).filter(Paciente.IDpaciente == paciente_id).first()
    if paciente:
        # Desencriptar campos sensibles
        paciente.Nombre = decrypt(paciente.Nombre)
        paciente.Apellido = decrypt(paciente.Apellido)
        paciente.Cedula = decrypt(paciente.Cedula)
        paciente.FNacimiento = paciente.FNacimiento
        paciente.Ocupacion = decrypt(paciente.Ocupacion)
        paciente.Telefono = decrypt(paciente.Telefono)
        paciente.Correo = decrypt(paciente.Correo)
        paciente.Direccion = decrypt(paciente.Direccion)
        paciente.Antecedentes = decrypt(paciente.Antecedentes)
        paciente.CondicionesMedicas = decrypt(paciente.CondicionesMedicas)
    return paciente