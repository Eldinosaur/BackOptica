from sqlalchemy.orm import Session, joinedload
from app.models.consulta import DatosConsulta
from app.models.receta import Recetas, RecetasArmazones, RecetasContacto
from app.models.evolucion import EvolucionVisual
from app.schemas.receta import ConsultaCompletaCreate

def crear_consulta_completa(db: Session, datos: ConsultaCompletaCreate):
    try:
        # 1. Crear consulta
        nueva_consulta = DatosConsulta(**datos.consulta.dict())
        db.add(nueva_consulta)
        db.flush()  # Para obtener el IDconsulta generado

        # 2. Crear receta general
        receta_general = Recetas(
            IDconsulta=nueva_consulta.IDconsulta,
            TipoLente=datos.receta.TipoLente,
            Fecha=datos.receta.Fecha
        )
        db.add(receta_general)
        db.flush()  # Para obtener el IDreceta

        # 3. Crear receta específica
        if datos.receta.TipoLente == 1 and datos.receta_armazones:
            receta_arm = RecetasArmazones(
            **datos.receta_armazones.dict()
            )
            receta_arm.IDreceta = receta_general.IDreceta
            db.add(receta_arm)
        elif datos.receta.TipoLente == 2 and datos.receta_contacto:
            receta_cont = RecetasContacto(
                **datos.receta_contacto.dict()
            )
            receta_cont.IDreceta = receta_general.IDreceta
            db.add(receta_cont)
        else:
            raise Exception("Datos de receta específica incompletos.")

        # 4. Registrar evolución visual
        evolucion = EvolucionVisual(
            IDpaciente=nueva_consulta.IDpaciente,
            Fecha=datos.evolucion.Fecha,
            OD=datos.evolucion.OD,
            OI=datos.evolucion.OI
        )
        db.add(evolucion)

        db.commit()
        return nueva_consulta.IDconsulta

    except Exception as e:
        db.rollback()
        raise e

def obtener_consultas_completas_por_paciente(db: Session, id_paciente: int):
    return db.query(DatosConsulta).\
        filter(DatosConsulta.IDpaciente == id_paciente).\
        options(
            joinedload(DatosConsulta.receta)
            .joinedload(Recetas.receta_armazones),
            joinedload(DatosConsulta.receta)
            .joinedload(Recetas.receta_contacto)
        ).\
        all()

def obtener_consulta_completa_por_id(db: Session, id_consulta: int):
    return db.query(DatosConsulta).\
        filter(DatosConsulta.IDconsulta == id_consulta).\
        options(
            joinedload(DatosConsulta.receta)
            .joinedload(Recetas.receta_armazones),
            joinedload(DatosConsulta.receta)
            .joinedload(Recetas.receta_contacto)
        ).\
        first()

def obtener_consultas_completas_tipo_armazon(db: Session, id_paciente: int):
    return db.query(DatosConsulta).\
        join(DatosConsulta.receta).\
        filter(
            DatosConsulta.IDpaciente == id_paciente,
            Recetas.TipoLente == 1
        ).\
        options(
            joinedload(DatosConsulta.receta)
            .joinedload(Recetas.receta_armazones)
        ).\
        all()

def obtener_consultas_completas_tipo_contacto(db: Session, id_paciente: int):
    return db.query(DatosConsulta).\
        join(DatosConsulta.receta).\
        filter(
            DatosConsulta.IDpaciente == id_paciente,
            Recetas.TipoLente == 2
        ).\
        options(
            joinedload(DatosConsulta.receta)
            .joinedload(Recetas.receta_contacto)
        ).\
        all()