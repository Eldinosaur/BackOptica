from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import Base, engine
from app.routers import login, paciente, consulta, consulta_completa, evolucion
from dotenv import load_dotenv

load_dotenv()

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(login.router, prefix="/api", tags=["Login"])
app.include_router(paciente.router, prefix="/api", tags=["Pacientes"])
app.include_router(consulta.router, prefix="/api", tags=["ConsultaSimple"])
app.include_router(consulta_completa.router, prefix="/api", tags=["ConsultaCompleta"])
app.include_router(evolucion.router, prefix="/api", tags=["EvolucionVisual"])