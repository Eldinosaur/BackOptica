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

#Respuesta de Login
class LoginResponse(BaseModel):
    access_token: str
    token_type: str
    IDusuario: int
    Nombre: str
    Apellido: str