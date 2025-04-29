from sqlalchemy import Column, Integer, String, Date, ForeignKey
from app.database import Base

class DatosConsulta(Base):
    __tablename__ = "DatosConsulta"

    IDconsulta = Column(Integer, primary_key=True, index=True)
    IDpaciente = Column(Integer, ForeignKey("Pacientes.IDpaciente"), nullable=False)
    IDusuario = Column(Integer, ForeignKey("Usuarios.IDusuario"), nullable=False)
    FConsulta = Column(Date, nullable=False)
    Motivo = Column(String, nullable=False)
    Observaciones = Column(String, nullable=True)
