from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from app.database import Base

class Paciente(Base):
    __tablename__ = "Pacientes"

    IDpaciente = Column(Integer, primary_key=True, index=True)
    Cedula = Column(String(250), nullable=False)
    Nombre = Column(String(250), nullable=False)
    Apellido = Column(String(250), nullable=False)
    FNacimiento = Column(Date, nullable=False)
    Ocupacion = Column(String(250), nullable=False)
    Telefono = Column(String(250), nullable=False)
    Correo = Column(String(250), nullable=False)
    Direccion = Column(String(250), nullable=True)
    Antecedentes = Column(String(250), nullable=True)
    CondicionesMedicas = Column(String(250), nullable=True)
    NombreBusqueda = Column(String(250), nullable=False)
    ApellidoBusqueda = Column(String(250), nullable=False)
    consultas = relationship("DatosConsulta", back_populates="paciente")
    evoluciones = relationship("EvolucionVisual", back_populates="paciente")
