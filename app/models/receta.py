from sqlalchemy import Column, Integer, Date, Float, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Recetas(Base):
    __tablename__ = "Recetas"

    IDreceta = Column(Integer, primary_key=True, index=True)
    IDconsulta = Column(Integer, ForeignKey("DatosConsulta.IDconsulta"))
    TipoLente = Column(Integer)  # 1: Armazones, 2: Contacto
    Fecha = Column(Date)

    consulta = relationship("DatosConsulta", back_populates="receta")
    receta_armazones = relationship("RecetasArmazones", uselist=False, back_populates="receta")
    receta_contacto = relationship("RecetasContacto", uselist=False, back_populates="receta")


class RecetasArmazones(Base):
    __tablename__ = "RecetasArmazones"

    IDreceta = Column(Integer, ForeignKey("Recetas.IDreceta"), primary_key=True)
    OD_SPH = Column(Float)
    OD_CYL = Column(Float)
    OD_AXIS = Column(Float)
    OD_ADD = Column(Float)
    OI_SPH = Column(Float)
    OI_CYL = Column(Float)
    OI_AXIS = Column(Float)
    OI_ADD = Column(Float)
    DIP = Column(Float)

    receta = relationship("Recetas", back_populates="receta_armazones")


class RecetasContacto(Base):
    __tablename__ = "RecetasContacto"

    IDreceta = Column(Integer, ForeignKey("Recetas.IDreceta"), primary_key=True)
    OD_SPH = Column(Float)
    OD_CYL = Column(Float)
    OD_AXIS = Column(Float)
    OD_ADD = Column(Float)
    OD_BC = Column(Float)
    OD_DIA = Column(Float)
    OI_SPH = Column(Float)
    OI_CYL = Column(Float)
    OI_AXIS = Column(Float)
    OI_ADD = Column(Float)
    OI_BC = Column(Float)
    OI_DIA = Column(Float)
    MarcaLente = Column(String)
    TiempoUso = Column(String)

    receta = relationship("Recetas", back_populates="receta_contacto")
