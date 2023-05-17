from config import conexion
from sqlalchemy import Column, types
from datetime import datetime
from sqlalchemy.sql.schema import ForeignKey #Para usar ForeignKey

class TareaModel(conexion.Model):
    __tablename__="tareas"

    id = Column(type_=types.Integer,autoincrement=True,primary_key=True)
    titulo = Column(type_=types.String(100),nullable=False)
    descripcion = Column(type_=types.Text)
    fechaCreacion = Column(type_=types.Date, name='fecha_creacion',default=datetime.now())
    observacion = Column(type_=types.Text)
    #Relaciones
    usuarioId = Column(ForeignKey(column='usuarios.id'),type_=types.Integer,nullable=False,name='usuario_id')                                                                                                                                                                                                                   