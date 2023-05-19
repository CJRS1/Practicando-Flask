from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.tareas import TareaModel

class TareaRequestDto(SQLAlchemyAutoSchema):
    class Meta:
        model = TareaModel
        #Si queremos usar las llaves Foráneas:
        include_fk = True