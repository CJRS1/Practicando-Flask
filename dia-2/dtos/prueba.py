from marshmallow import Schema, fields

class PruebaDto(Schema):
    id = fields.Int()
    #para modificar el mensaje de error con error_message
    nombre = fields.Str(required=True, error_messages={'required':'Este campo es obligatorio'})
    correo = fields.Email(error_messages={'invalid':'Correo electrónico no válido'})