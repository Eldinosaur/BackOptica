from sqlalchemy import Column, Integer, Date, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class EvolucionVisual(Base):
    __tablename__ = "EvolucionVisual"

    IDregistro = Column(Integer, primary_key=True, index=True)
    IDpaciente = Column(Integer, ForeignKey("Pacientes.IDpaciente"))
    Fecha = Column(Date)
    OD = Column(Float)
    OI = Column(Float)

    paciente = relationship("Paciente", back_populates="evoluciones")
