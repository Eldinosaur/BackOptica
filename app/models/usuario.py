from sqlalchemy import Column, Integer, String
from app.database import Base

class Usuario(Base):
    __tablename__ = "Usuarios"

    IDusuario = Column(Integer, primary_key=True, index=True)
    Usuario = Column(String(50), unique=True, nullable=False)
    Nombre = Column(String(50))
    Apellido = Column(String(50))
    Clave = Column(String(255))  
