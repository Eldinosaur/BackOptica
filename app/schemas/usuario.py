from pydantic import BaseModel

class UsuarioBase(BaseModel):
    Usuario: str

class UsuarioLogin(UsuarioBase):
    Clave: str

class UsuarioOut(UsuarioBase):
    IDusuario: int
    Nombre: str
    Apellido: str

    class Config:
        orm_mode = True

#Cambio de Clave
class CambioClave(BaseModel):
    IDusuario: int
    ClaveActual: str
    NuevaClave: str
