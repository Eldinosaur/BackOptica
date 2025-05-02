from sqlalchemy.orm import Session
from sqlalchemy import or_
from app.models.paciente import Paciente
from app.models.consulta import DatosConsulta
from app.schemas.paciente import PacienteCreate, PacienteConConsultaOut
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
        CondicionesMedicas=encrypt(paciente.CondicionesMedicas),
        NombreBusqueda = paciente.Nombre.lower(), #Nombre para busqueda
        ApellidoBusqueda = paciente.Apellido.lower() #Apellido para busqueda
    )
    db.add(nuevo_paciente)
    db.commit()
    db.refresh(nuevo_paciente)
    return nuevo_paciente

def obtener_paciente_id(db: Session, paciente_id: int):
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

def obtener_todos_pacientes(db: Session):
    pacientes_db = db.query(Paciente).all()
    
    pacientes = []
    for paciente in pacientes_db:
        ultima_consulta = (
        db.query(DatosConsulta.FConsulta)
        .filter(DatosConsulta.IDpaciente == paciente.IDpaciente)
        .order_by(DatosConsulta.FConsulta.desc())
        .first()
        )

        # Extraer la fecha si hay consulta
        ultima_fecha = ultima_consulta.FConsulta if ultima_consulta else None
        pacientes.append({
            "IDpaciente": paciente.IDpaciente,
            "Cedula": decrypt(paciente.Cedula),
            "Nombre": decrypt(paciente.Nombre),
            "Apellido": decrypt(paciente.Apellido),
            "FNacimiento": paciente.FNacimiento,
            "Ocupacion": decrypt(paciente.Ocupacion),
            "Telefono": decrypt(paciente.Telefono),
            "Correo": decrypt(paciente.Correo),
            "Direccion": decrypt(paciente.Direccion),
            "Antecedentes": decrypt(paciente.Antecedentes),
            "CondicionesMedicas": decrypt(paciente.CondicionesMedicas),
            "ultima_consulta": {"ultima_consulta_fecha": ultima_fecha} if ultima_fecha else None
        })
    
    return pacientes

def obtener_paciente_cedula(db: Session, paciente_cedula: str):

    cedula = encrypt(paciente_cedula)

    paciente = db.query(Paciente).filter(Paciente.Cedula == cedula).first()

    
    
    if paciente:
        ultima_consulta = (
        db.query(DatosConsulta.FConsulta)
        .filter(DatosConsulta.IDpaciente == paciente.IDpaciente)
        .order_by(DatosConsulta.FConsulta.desc())
        .first()
        )

        # Extraer la fecha si hay consulta
        ultima_fecha = ultima_consulta.FConsulta if ultima_consulta else None
        return {
            "IDpaciente": paciente.IDpaciente,
            "Cedula": decrypt(paciente.Cedula),
            "Nombre": decrypt(paciente.Nombre),
            "Apellido": decrypt(paciente.Apellido),
            "FNacimiento": paciente.FNacimiento,
            "Ocupacion": decrypt(paciente.Ocupacion),
            "Telefono": decrypt(paciente.Telefono),
            "Correo": decrypt(paciente.Correo),
            "Direccion": decrypt(paciente.Direccion),
            "Antecedentes": decrypt(paciente.Antecedentes),
            "CondicionesMedicas": decrypt(paciente.CondicionesMedicas),
            "ultima_consulta": {"ultima_consulta_fecha": ultima_fecha} if ultima_fecha else None
        }
    
    return None

def obtener_pacientes_por_nombre_apellido(db: Session, termino):
    if not termino:
        return []

    pacientes_db = db.query(Paciente).filter(
        or_(
            Paciente.NombreBusqueda.like(f"%{termino.lower()}%"),
            Paciente.ApellidoBusqueda.like(f"%{termino.lower()}%")
        )
    ).all()

    pacientes = []
    for paciente in pacientes_db:
        ultima_consulta = (
        db.query(DatosConsulta.FConsulta)
        .filter(DatosConsulta.IDpaciente == paciente.IDpaciente)
        .order_by(DatosConsulta.FConsulta.desc())
        .first()
        )

        # Extraer la fecha si hay consulta
        ultima_fecha = ultima_consulta.FConsulta if ultima_consulta else None
        pacientes.append({
            "IDpaciente": paciente.IDpaciente,
            "Cedula": decrypt(paciente.Cedula),
            "Nombre": decrypt(paciente.Nombre),
            "Apellido": decrypt(paciente.Apellido),
            "FNacimiento": paciente.FNacimiento,
            "Ocupacion": decrypt(paciente.Ocupacion),
            "Telefono": decrypt(paciente.Telefono),
            "Correo": decrypt(paciente.Correo),
            "Direccion": decrypt(paciente.Direccion),
            "Antecedentes": decrypt(paciente.Antecedentes),
            "CondicionesMedicas": decrypt(paciente.CondicionesMedicas),
            "ultima_consulta": {"ultima_consulta_fecha": ultima_fecha} if ultima_fecha else None
        })

    return pacientes

def actualizar_paciente(db: Session, paciente_id: int, datos_actualizados: PacienteCreate):
    paciente = db.query(Paciente).filter(Paciente.IDpaciente == paciente_id).first()
    if not paciente:
        return None  

    # Actualizar los campos, cifrando donde corresponde
    paciente.Cedula = encrypt(datos_actualizados.Cedula)
    paciente.Nombre = encrypt(datos_actualizados.Nombre)
    paciente.Apellido = encrypt(datos_actualizados.Apellido)
    paciente.FNacimiento = datos_actualizados.FNacimiento
    paciente.Ocupacion = encrypt(datos_actualizados.Ocupacion)
    paciente.Telefono = encrypt(datos_actualizados.Telefono)
    paciente.Correo = encrypt(datos_actualizados.Correo)
    paciente.Direccion = encrypt(datos_actualizados.Direccion)
    paciente.Antecedentes = encrypt(datos_actualizados.Antecedentes)
    paciente.CondicionesMedicas = encrypt(datos_actualizados.CondicionesMedicas)

    # Actualizar campos de búsqueda en texto plano
    paciente.NombreBusqueda = datos_actualizados.Nombre.lower()
    paciente.ApellidoBusqueda = datos_actualizados.Apellido.lower()

    db.commit()
    db.refresh(paciente)
    return paciente
