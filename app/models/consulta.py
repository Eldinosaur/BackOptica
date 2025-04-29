from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class DatosConsulta(Base):
    __tablename__ = "DatosConsulta"

    IDconsulta = Column(Integer, primary_key=True, index=True)
    IDpaciente = Column(Integer, ForeignKey("Pacientes.IDpaciente"))
    IDusuario = Column(Integer, ForeignKey("Usuarios.IDusuario"))
    FConsulta = Column(Date)
    Observaciones = Column(String)
    Motivo = Column(String)

    paciente = relationship("Paciente", back_populates="consultas")
    usuario = relationship("Usuario", back_populates="consultas")
    receta = relationship("Recetas", back_populates="consulta", uselist=False)
